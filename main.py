#!/usr/bin/env python3
##########################################################
#                                                        #
#              MEK Technopat Grabber CLI v3              #
#                                                        #
#  Features:                                             #
#  - Kutu içinde outline (liste görünümü)                #
#  - Renk optimizasyonu                                  #
#  - İleri / Geri navigasyon                             #
#                                                        #
##########################################################

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import os

init(autoreset=True)

BASE_URL = "https://www.technopat.net/haber/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/118.0.0.0 Safari/537.36"
    )
}


def clear_screen():
    """Terminal ekranını temizler."""
    os.system("cls" if os.name == "nt" else "clear")


def draw_box(title, content_lines, color=Fore.CYAN):
    """Kutulu metin çizimi."""
    width = max(len(line) for line in content_lines + [title]) + 4
    print(color + "┌" + "─" * (width - 2) + "┐")
    print(color + f"│ {Style.BRIGHT}{title.ljust(width - 4)} │")
    print(color + "├" + "─" * (width - 2) + "┤")
    for line in content_lines:
        print(color + f"│ {line.ljust(width - 4)} │")
    print(color + "└" + "─" * (width - 2) + "┘" + Style.RESET_ALL)


def fetch_news_list():
    """Technopat haber listesini çeker."""
    try:
        resp = requests.get(BASE_URL, headers=HEADERS)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"{Fore.RED}Hata: {e}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    articles = soup.select("article.jeg_post")
    news_list = []

    for article in articles:
        title_tag = article.select_one("h3.jeg_post_title a")
        title = title_tag.text.strip() if title_tag else "Başlık yok"
        link = title_tag["href"] if title_tag else "Link yok"
        img_tag = article.select_one(".jeg_thumb img")
        img_src = img_tag["src"] if img_tag else "Görsel yok"
        news_list.append({"title": title, "link": link, "img": img_src})
    return news_list


def fetch_news_content(link):
    """Tek bir haberin içeriğini çeker."""
    try:
        resp = requests.get(link, headers=HEADERS)
        resp.raise_for_status()
    except requests.RequestException:
        return f"{Fore.RED}İçerik alınamadı."

    soup = BeautifulSoup(resp.text, "html.parser")
    content_div = soup.select_one(".content-inner")
    if not content_div:
        return f"{Fore.YELLOW}İçerik bulunamadı."

    paragraphs = content_div.find_all("p")
    content = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
    return content if content else f"{Fore.YELLOW}İçerik yok."


def show_outline(news_list):
    """Kutu içinde outline (başlık listesi)."""
    clear_screen()
    print(Style.BRIGHT + Fore.CYAN + "\n📰  TECHNOPAT HABERLERİ  📰\n")
    for i, news in enumerate(news_list, start=1):
        draw_box(
            f"Haber {i}",
            [Fore.GREEN + news['title'], Fore.BLUE + news['link']],
            color=Fore.CYAN,
        )
    print(Style.DIM + "-" * 70)


def navigate_news(news_list):
    """Kullanıcı haberleri kutu içinde gezebilir."""
    if not news_list:
        print(f"{Fore.RED}Haber bulunamadı.")
        return

    idx = 0
    while True:
        clear_screen()
        news = news_list[idx]
        title = f"[{idx + 1}/{len(news_list)}] {news['title']}"
        lines = [
            Fore.BLUE + f"🔗 {news['link']}",
            Fore.MAGENTA + f"🖼  {news['img']}",
            "",
            Fore.GREEN + fetch_news_content(news["link"]),
        ]
        draw_box(title, lines, color=Fore.YELLOW)

        print(Style.BRIGHT + Fore.CYAN + "\n⬅️  [P]rev | ➡️  [N]ext | [O]utline | [Q]uit")
        choice = input(Fore.WHITE + "\nSeçim: ").strip().lower()

        if choice == "n":
            idx = (idx + 1) % len(news_list)
        elif choice == "p":
            idx = (idx - 1) % len(news_list)
        elif choice == "o":
            show_outline(news_list)
            input(Fore.CYAN + "\nDevam etmek için Enter'a bas...")
        elif choice == "q":
            print(Fore.RED + "\nÇıkılıyor...")
            break
        else:
            print(Fore.RED + "Geçersiz giriş.")
            input(Fore.YELLOW + "Devam için Enter...")


if __name__ == "__main__":
    news = fetch_news_list()
    navigate_news(news)