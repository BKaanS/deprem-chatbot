import requests

url = "https://deprem.afad.gov.tr/event-service"
response = requests.get(url)
if response.status_code == 200:
    print('Veri çekme başarıyla sonuçlandı.')
else:
    print("Hata oluştu:", response.status_code)
data = response.json()


def fetch_raw_data():
    try:
        res = requests.get("https://deprem.afad.gov.tr/event-service")
        res.raise_for_status()  # status code 200 değilse hata fırlatır
        return res.json()
    except requests.exceptions.RequestException as e:
        print("AFAD verisi alınamadı:", e)
        return []
