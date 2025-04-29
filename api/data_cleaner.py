import pandas as pd

def clean_data(raw_data):
    df = pd.DataFrame(raw_data)

    # Kolon adlarını sadeleştir ve Türkçeleştir
    df = df.rename(columns={
        "location": "lokasyon",
        "mag": "buyukluk",
        "depth": "derinlik",
        "date": "tarih",
        "lat": "enlem",
        "lng": "boylam"
    })

    # Tip dönüşümleri
    df["tarih"] = pd.to_datetime(df["tarih"], errors="coerce")
    df["buyukluk"] = pd.to_numeric(df["buyukluk"], errors="coerce")
    df["derinlik"] = pd.to_numeric(df["derinlik"], errors="coerce")

    # Eksik satırları temizle
    df = df.dropna(subset=["tarih", "buyukluk", "derinlik"])

    return df
