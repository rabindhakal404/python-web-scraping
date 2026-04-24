# 🌐 Python Web Scraping Project

## 🔍 Overview

This project demonstrates a basic web scraping workflow using Python. It extracts data from a website, processes it, and saves the results in a structured format for analysis.

## 🎯 Objective

To collect raw data from web pages and convert it into a usable dataset for further analysis.

## 🛠 Tools & Libraries

* Python
* Requests
* BeautifulSoup
* Pandas

## ⚙️ How It Works

1. Send HTTP request to the target website using `requests`
2. Parse HTML content using `BeautifulSoup`
3. Extract relevant data fields (e.g., titles, prices, links, etc.)
4. Clean and structure the extracted data
5. Save the data into a CSV file using `pandas`

## 📂 Project Structure

```
web-scraping-project/
│── companies_scraping.py          # Main Python script
│── Companies.csv                  # Scraped dataset
│── README.md                      # Project documentation
```

## ▶️ How to Run

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/python-web-scraping.git
   ```
2. Install required libraries:

   ```
   pip install requests beautifulsoup4 pandas
   ```
3. Run the script:

   ```
   python companies_scraping.py
   ```

## 📊 Output

* The script generates a CSV file (`Companies.csv`) containing the scraped data.

## ⚠️ Disclaimer

This project is for educational purposes only. Please ensure you respect the website's terms of service before scraping.

## ✅ Conclusion

This project showcases basic skills in data collection, parsing, and preprocessing using Python.
