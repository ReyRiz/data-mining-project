import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "https://www.scrapethissite.com/pages/forms/"
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Daftar tahun
years = list(range(1990, 2014))

# Siapkan CSV
with open("data_hockey_tim.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Team", "Year", "Wins", "Losses", "OT Losses", "Win %", "Goals For", "Goals Against", "+/- Goals"])

    for year in years:
        print(f"🔄 Mengambil data tahun {year}...")
        max_retry = 3
        for attempt in range(max_retry):
            try:
                response = requests.post(base_url, data={"year": year}, headers=headers, timeout=10)
                soup = BeautifulSoup(response.content, "html.parser")
                rows = soup.find_all("tr", class_="team")

                for row in rows:
                    cols = row.find_all("td")
                    data = [col.text.strip() for col in cols]
                    writer.writerow(data)

                break  # keluar dari loop retry jika sukses
            except Exception as e:
                print(f"⚠️ Gagal mengambil data untuk tahun {year}, percobaan {attempt+1}: {e}")
                time.sleep(2)  # jeda 2 detik sebelum retry

        time.sleep(1)  # delay antar tahun (menghindari deteksi bot)

print("✅ Semua data berhasil disimpan ke 'data_hockey_tim.csv'")
