##########################################################
#                                                        #
#               MEK Technopat Grabber CLI               #
#                                                        #
#  To Do (implemented):                                 #
#  - İlk sayfadan haberleri çek                          #
#  - 403 hatasını önledik (User-Agent eklendi)         #
#  - Haber başlıkları ve linkleri CLI'de gösteriliyor   #
#                                                        #
##########################################################
import requests
from bs4 import BeautifulSoup

# Haber sayfası (default page)
BASE_URL = "https://www.technopat.net/haber/"

def fetch_news():
    """
    Sadece ilk sayfadaki haberleri çeker.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0.0.0 Safari/537.36"
        )
    }

    try:
        resp = requests.get(BASE_URL, headers=headers)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Hata: {e}")
        return

    soup = BeautifulSoup(resp.text, "html.parser")
    articles = soup.select("article.jeg_post")  # Tüm haberler

    if not articles:
        print("Haber bulunamadı.")
        return

    for idx, article in enumerate(articles, start=1):
        title_tag = article.select_one("h3.jeg_post_title a")
        link = title_tag['href'] if title_tag else "Link yok"
        title = title_tag.text.strip() if title_tag else "Başlık yok"

        img_tag = article.select_one(".jeg_thumb img")
        img_src = img_tag['src'] if img_tag else "Görsel yok"

        print(f"{idx}. {title}\n   Link: {link}\n   Görsel: {img_src}\n")

if __name__ == "__main__":
    fetch_news()