##########################################################
#                                                        #
#               MEK Technopat Grabber CLI               #
#                                                        #
#  To Do (implemented):                                 #
#                            
#                                                       #
#  -   
#  - >> Done. Navigator ile haberler arasında gezinme ekleyecegim.  
##########################################################
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.technopat.net/haber/"

def fetch_news():
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
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    articles = soup.select("article.jeg_post")

    news_list = []
    for article in articles:
        title_tag = article.select_one("h3.jeg_post_title a")
        title = title_tag.text.strip() if title_tag else "Başlık yok"
        link = title_tag['href'] if title_tag else "Link yok"

        img_tag = article.select_one(".jeg_thumb img")
        img_src = img_tag['src'] if img_tag else "https://www.technopat.net/wp-content/themes/jnews/assets/img/jeg-empty.png"

        news_list.append({
            "title": title,
            "link": link,
            "img": img_src
        })

    return news_list

def navigate_news(news_list):
    if not news_list:
        print("Haber bulunamadı.")
        return

    idx = 0
    while True:
        news = news_list[idx]
        print(f"\n[{idx+1}/{len(news_list)}] {news['title']}\nLink: {news['link']}\nGörsel: {news['img']}\n")
        print("n: sonraki, p: önceki, q: çıkış")
        choice = input("Seçiminiz: ").lower()
        if choice == 'n':
            if idx < len(news_list) - 1:
                idx += 1
            else:
                print("Son haber.")
        elif choice == 'p':
            if idx > 0:
                idx -= 1
            else:
                print("İlk haber.")
        elif choice == 'q':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, n/p/q kullanın.")

if __name__ == "__main__":
    news = fetch_news()
    navigate_news(news)