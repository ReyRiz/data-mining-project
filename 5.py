import requests
import csv

url = "https://www.scrapethissite.com/pages/advanced/?ajax=true"

headers = {
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.scrapethissite.com/pages/advanced/"
}

response = requests.get(url, headers=headers)

# Cek jika berhasil
if response.status_code == 200:
    data = response.json()
    
    # Simpan ke CSV
    with open("data_negara_advanced.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Capital", "Population", "Area (km²)"])

        for country in data:
            writer.writerow([
                country["name"],
                country["capital"],
                country["population"],
                country["area_km2"]
            ])

    print("✅ Data berhasil disimpan ke 'data_negara_advanced.csv'")
else:
    print(f"❌ Gagal mengambil data. Status code: {response.status_code}")
