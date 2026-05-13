#!/usr/bin/env python3
##########################################################
#                                                        #
#              MEK Technopat Grabber CLI v4              #
##########################################################

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import os
import shutil
import textwrap

init(autoreset=True)

BASE_URL = "https://www.technopat.net/haber/"
REQUEST_TIMEOUT = 10
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/118.0.0.0 Safari/537.36"
    )
}


def clear_screen():
    """Clear the terminal before rendering a new navigation view."""
    os.system("cls" if os.name == "nt" else "clear")


def draw_box(title, content_lines, color=Fore.CYAN):
    """Render wrapped terminal content inside a simple box."""
    term_width = shutil.get_terminal_size((100, 40)).columns
    max_width = min(term_width - 4, 100)  # Keep the layout within 100 characters.

    wrapped_lines = []
    for line in content_lines:
        wrapped = textwrap.wrap(line, width=max_width - 4) or [""]
        wrapped_lines.extend(wrapped)

    width = max(len(title), *(len(l) for l in wrapped_lines)) + 4
    width = min(width, max_width)

    print(color + "┌" + "─" * (width - 2) + "┐")
    print(color + f"│ {Style.BRIGHT}{title.ljust(width - 4)} │")
    print(color + "├" + "─" * (width - 2) + "┤")

    for line in wrapped_lines:
        print(color + f"│ {line.ljust(width - 4)} │")

    print(color + "└" + "─" * (width - 2) + "┘" + Style.RESET_ALL)


def fetch_news_list():
    """Fetch the latest Technopat news cards from the listing page."""
    try:
        resp = requests.get(BASE_URL, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"{Fore.RED}Error: {e}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    articles = soup.select("article.jeg_post")
    news_list = []

    for article in articles:
        title_tag = article.select_one("h3.jeg_post_title a")
        title = title_tag.text.strip() if title_tag else "No title"
        link = title_tag["href"] if title_tag else "No link"
        img_tag = article.select_one(".jeg_thumb img")
        img_src = img_tag["src"] if img_tag else "No image"
        news_list.append({"title": title, "link": link, "img": img_src})
    return news_list


def fetch_news_content(link):
    """Fetch and normalize the article body for a single news URL."""
    try:
        resp = requests.get(link, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException:
        return f"{Fore.RED}Content could not be fetched."

    soup = BeautifulSoup(resp.text, "html.parser")
    content_div = soup.select_one(".content-inner")
    if not content_div:
        return f"{Fore.YELLOW}Content could not be found."

    paragraphs = content_div.find_all("p")
    content = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
    return content if content else f"{Fore.YELLOW}No content available."


def show_outline(news_list):
    """Render a compact boxed outline of all fetched news items."""
    clear_screen()
    print(Style.BRIGHT + Fore.CYAN + "\nTECHNOPAT NEWS\n")
    for i, news in enumerate(news_list, start=1):
        draw_box(
            f"News {i}",
            [Fore.GREEN + news["title"], Fore.BLUE + news["link"]],
            color=Fore.CYAN,
        )
    print(Style.DIM + "-" * 80)


def navigate_news(news_list):
    """Run the interactive terminal navigator for fetched news items."""
    if not news_list:
        print(f"{Fore.RED}No news items were found.")
        return

    idx = 0
    while True:
        clear_screen()
        news = news_list[idx]
        title = f"[{idx + 1}/{len(news_list)}] {news['title']}"
        lines = [
            Fore.BLUE + f"Link: {news['link']}",
            Fore.MAGENTA + f"Image: {news['img']}",
            "",
            Fore.GREEN + fetch_news_content(news["link"]),
        ]
        draw_box(title, lines, color=Fore.YELLOW)

        print(Style.BRIGHT + Fore.CYAN + "\n[P]revious | [N]ext | [O]utline | [Q]uit")
        choice = input(Fore.WHITE + "\nChoice: ").strip().lower()

        if choice == "n":
            idx = (idx + 1) % len(news_list)
        elif choice == "p":
            idx = (idx - 1) % len(news_list)
        elif choice == "o":
            show_outline(news_list)
            input(Fore.CYAN + "\nPress Enter to continue...")
        elif choice == "q":
            print(Fore.RED + "\nExiting...")
            break
        else:
            print(Fore.RED + "Invalid input.")
            input(Fore.YELLOW + "Press Enter to continue...")


if __name__ == "__main__":
    news = fetch_news_list()
    navigate_news(news)
