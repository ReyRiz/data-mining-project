# Data Mining Project - Web Scraping

Proyek ini berisi kumpulan script Python untuk melakukan web scraping dari berbagai sumber data, dengan fokus utama pada website [scrapethissite.com](http://scrapethissite.com/).

## Deskripsi Proyek

Repository ini dikembangkan sebagai bagian dari mata kuliah Data Mining Semester 3. Proyek ini bertujuan untuk mempelajari dan menerapkan teknik-teknik web scraping untuk mengumpulkan data dari berbagai sumber web, kemudian menganalisis data tersebut menggunakan teknik data mining.

## Website Target: Scrapethissite.com

[Scrapethissite.com](http://scrapethissite.com/) adalah website yang dirancang khusus untuk pembelajaran web scraping. Website ini menyediakan berbagai tantangan scraping dengan tingkat kesulitan yang berbeda-beda, mulai dari scraping sederhana hingga yang memerlukan penanganan JavaScript dan AJAX.

### Jenis Data yang Akan Di-scrape:

1. **Countries Data** - Data negara-negara dengan informasi populasi, luas area, dan ibukota
2. **Hockey Teams** - Data tim hockey dengan statistik menang, kalah, dan seri
3. **AJAX/JavaScript Content** - Data yang dimuat secara dinamis menggunakan JavaScript
4. **Film Data** - Data film dengan informasi tahun rilis, rating, dan detail lainnya

## Struktur Proyek

```
data-mining-project/
├── scraping_scripts/
│   ├── scrape_countries.py      # Script untuk scraping data negara
│   ├── scrape_hockey_teams.py   # Script untuk scraping data tim hockey
│   ├── scrape_ajax_selenium.py  # Script untuk scraping konten AJAX
│   └── scrape_films.py          # Script untuk scraping data film
├── data/
│   ├── countries_data.csv       # Data negara hasil scraping
│   ├── data_hockey_tim.csv      # Data tim hockey hasil scraping
│   ├── data_film_ajax_selenium.csv # Data film hasil scraping
│   └── data_negara_advanced.csv # Data negara dengan analisis lanjut
├── analysis/
│   ├── data_analysis.py         # Script analisis data
│   └── visualization.py        # Script visualisasi data
└── output/
    ├── output1.json            # Output hasil analisis
    └── output2.json            # Output hasil analisis lanjutan
```

## Tools dan Library yang Digunakan

### Web Scraping:
- **requests** - Untuk HTTP requests sederhana
- **BeautifulSoup4** - Untuk parsing HTML
- **Selenium** - Untuk scraping konten JavaScript/AJAX
- **pandas** - Untuk manipulasi dan analisis data
- **csv** - Untuk handling file CSV

### Data Analysis:
- **numpy** - Untuk operasi numerik
- **matplotlib** - Untuk visualisasi data
- **seaborn** - Untuk visualisasi statistik
- **scikit-learn** - Untuk algoritma machine learning

## Metodologi Scraping

### 1. Static Content Scraping
Untuk konten statis menggunakan kombinasi `requests` + `BeautifulSoup`:
- Mengambil HTML page menggunakan requests
- Parsing HTML menggunakan BeautifulSoup
- Ekstraksi data menggunakan CSS selectors atau XPath

### 2. Dynamic Content Scraping
Untuk konten yang dimuat dengan JavaScript menggunakan `Selenium`:
- Menggunakan WebDriver untuk mengontrol browser
- Menunggu konten dimuat secara dinamis
- Handling AJAX requests dan DOM manipulation

### 3. Data Processing
- Cleaning dan preprocessing data hasil scraping
- Validasi dan handling data yang hilang
- Export ke format CSV atau JSON

## Tantangan Scraping dari Scrapethissite.com

### Level 1: Sandbox - Countries
- **Target**: Data negara dengan informasi dasar
- **Teknik**: Static HTML scraping
- **Kompleksitas**: Beginner

### Level 2: Hockey Teams
- **Target**: Data tim hockey dengan statistik
- **Teknik**: HTML table scraping dengan pagination
- **Kompleksitas**: Intermediate

### Level 3: AJAX dan JavaScript
- **Target**: Konten yang dimuat dinamis
- **Teknik**: Selenium WebDriver
- **Kompleksitas**: Advanced

### Level 4: Forms dan Login
- **Target**: Data yang memerlukan form submission
- **Teknik**: Session handling dan form automation
- **Kompleksitas**: Advanced

## Instalasi dan Setup

### Prerequisites
- Python 3.8+
- Chrome/Firefox browser (untuk Selenium)
- ChromeDriver/GeckoDriver

### Langkah Instalasi
1. Clone repository ini
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download dan setup WebDriver untuk Selenium
4. Jalankan script sesuai kebutuhan

## Penggunaan

### Menjalankan Scraping
```bash
# Scraping data negara
python scrape_countries.py

# Scraping data tim hockey
python scrape_hockey_teams.py

# Scraping konten AJAX
python scrape_ajax_selenium.py
```

### Analisis Data
```bash
# Analisis data hasil scraping
python data_analysis.py

# Visualisasi data
python visualization.py
```

## Ethical Scraping Guidelines

Proyek ini mengikuti praktik ethical scraping:
- Menghormati robots.txt
- Tidak melakukan overload pada server
- Menggunakan delay yang wajar antar requests
- Hanya mengambil data yang diperlukan untuk pembelajaran

## Output dan Hasil

Hasil scraping akan disimpan dalam berbagai format:
- **CSV files** untuk data tabular
- **JSON files** untuk data kompleks
- **Visualization charts** untuk analisis visual

## Kontributor

- **Nama**: Fariz Idham Ramdhani
- **NIM**: H071231066
- **Program Studi**: Sistem Informasi
- **Mata Kuliah**: Data Mining - Semester 4

## Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dalam mata kuliah Data Mining.

## Referensi

- [Scrapethissite.com](http://scrapethissite.com/) - Website target scraping
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Requests Documentation](https://docs.python-requests.org/)

---
*Project ini merupakan bagian dari pembelajaran Data Mining untuk memahami teknik web scraping dan analisis data.*