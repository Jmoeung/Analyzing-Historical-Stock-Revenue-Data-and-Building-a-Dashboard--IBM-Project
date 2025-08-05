# Analyzing Historical Stock Revenue Data and Building a Dashboard

This project analyzes historical stock price and revenue data for Tesla (TSLA) and GameStop (GME) using Python. It fetches stock data from Yahoo Finance and revenue data from Macrotrends, then visualizes the relationship between stock price and revenue for each company.

## Features
- Downloads historical stock price data using `yfinance`
- Scrapes revenue data from Macrotrends using `requests` and `BeautifulSoup`
- Cleans and processes the data with `pandas`
- Visualizes stock price and revenue trends using `matplotlib`

## Requirements
- Python 3.7+
- `yfinance`
- `requests`
- `beautifulsoup4`
- `pandas`
- `matplotlib`

## Installation
Install the required packages with pip:

```bash
pip install yfinance requests beautifulsoup4 pandas matplotlib
```

## Usage
1. Clone or download this repository.
2. Run the Python script:
   ```bash
   python Analyzing-Historical-Stock-Revenue-Data-and-Building-a-Dashboard--IBM-Project.py
   ```
3. The script will display plots comparing stock price and revenue for Tesla and GameStop.

## File Structure
- `Analyzing-Historical-Stock-Revenue-Data-and-Building-a-Dashboard--IBM-Project.py`: Main analysis and visualization script
- `README.md`: Project overview and instructions

## Notes
- Revenue data is scraped from Macrotrends and may change format over time.
- The script is for educational purposes and may require updates if data sources change.

## License
This project is provided for educational use. Please check data source terms for any restrictions.
