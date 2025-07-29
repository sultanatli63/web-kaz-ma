import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/turkce"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # BBC Türkçe'de haber başlıkları genellikle <h3> etiketinde ve belirli class'larda oluyor.
    # Bunu kontrol edip aşağıdaki gibi seçebiliriz:
    headlines = soup.find_all("h3")
    
    print("BBC Türkçe Güncel Haber Başlıkları:")
    for i, headline in enumerate(headlines[:10], 1):  # İlk 10 başlık
        print(f"{i}. {headline.text.strip()}")
else:
    print("Sayfa çekilirken hata oluştu:", response.status_code)
