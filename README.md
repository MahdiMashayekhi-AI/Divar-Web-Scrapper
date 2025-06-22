# Divar Web Scraper

A professional Python-based web scraper built using Selenium to extract detailed data about residential apartment listings for sale in Tehran from divar.ir, one of Iran's most widely used classified ad websites.

## 🚀 Project Overview

This project is designed for accurate and robust data extraction to build a clean, structured dataset from the real estate listings on Divar. The scraper collects listing data such as:

- Title
- Price
- Location
- Meterage
- Build year
- Number of rooms
- Floor number
- Price per meter
- Amenities: parking, warehouse, balcony, elevator
- Description
- Listing URL

### The output is saved in CSV format.

## ⚙️ Key Features

Object-oriented and well-structured code

Supports resuming from the last successful scrape

Avoids duplicate listings via visited_links.txt

Saves data in batches (e.g., every 10 listings) to prevent loss on failure

Detects and handles connection issues and site structure changes

Automatically closes Divar’s map UI overlay to enable full listing view

## ⚠️ Limitations (Current Version)

### Note: This scraper is currently optimized only for:

Apartment listings for sale in Tehran (/s/tehran/buy-apartment)

It may not work properly with:

Rental listings

Commercial properties

Listings from cities other than Tehran

Listings with significantly different HTML structures

These may be supported in future versions with further development and structure generalization.

## 🛠 Technologies Used

Python 3.10+

Selenium WebDriver (Chromedriver)

pandas

CSV + Excel (xlsxwriter)

## 📦 Installation

Clone the repository:
``` bash
git clone https://github.com/your-username/divar-web-scraper.git
cd divar-web-scraper
```
Install dependencies:

```bash
pip install -r requirements.txt
```

(Optional) Update configurations by editing config.py:

- Output file names
- Number of scrolls
- Sleep time ranges
- Retry attempts

###Run the scraper:
```bash
python app.py
```

## 📂 Output Example

Each row in the exported dataset includes:

title,price,description,location,link,scraped_time,meterage,build_year,rooms,floor,price_per_meter,has_parking,has_warehouse,has_balcony,has_elevator
"طرشت /دو خوابه /میدان سما /تاپ لوکیشن",12500000000,"...","تهران، طرشت",https://divar.ir/v/...,2025-06-21 19:47:06,110,1404,2,3,113636000,True,True,False,True

## 📌 Future Improvements

Generalizing scraper to work for all Divar categories

NLP-based keyword extraction from descriptions

Adding more robust error logging and retry logic

Dockerizing the scraper for deployment

## 📄 License

This project is open source and available under the MIT License.

Feel free to fork or contribute to improve its functionality. For any issues, please open an issue on the repository.

Happy Scraping! 🏠📊