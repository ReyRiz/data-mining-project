import requests
from bs4 import BeautifulSoup
import csv

# URL target
url = "https://www.scrapethissite.com/pages/simple/"

# Kirim request dan parsing HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Ambil semua data negara
countries = soup.find_all("div", class_="col-md-4 country")

# Buat file CSV dan tulis header
with open("negara_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nama Negara", "Ibukota", "Populasi", "Luas Wilayah"])

    # Loop tiap negara dan tulis ke CSV
    for country in countries:
        name = country.find("h3", class_="country-name").text.strip()
        capital = country.find("span", class_="country-capital").text.strip()
        population = country.find("span", class_="country-population").text.strip()
        area = country.find("span", class_="country-area").text.strip()

        writer.writerow([name, capital, population, area])

print("✅ Data berhasil disimpan ke 'negara_data.csv'")
