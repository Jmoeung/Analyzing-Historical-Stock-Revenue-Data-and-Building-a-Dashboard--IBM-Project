import yfinance as yf

tesla = yf.Ticker("TSLA")
tesla_stock = tesla.history(period="max")
tesla_stock.reset_index(inplace=True)

print(tesla_stock.tail())
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tables = soup.find_all("table")
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for table in tables:
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) == 2:
            date = cols[0].text.strip()
            revenue = cols[1].text.strip().replace("$", "").replace(",", "")
            if revenue:
                tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])], ignore_index=True)

tesla_revenue["Revenue"] = pd.to_numeric(tesla_revenue["Revenue"], errors="coerce")
print(tesla_revenue.tail())
gamestop = yf.Ticker("GME")
gme_stock = gamestop.history(period="max")
gme_stock.reset_index(inplace=True)

print(gme_stock.tail())
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tables = soup.find_all("table")
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for table in tables:
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) == 2:
            date = cols[0].text.strip()
            revenue = cols[1].text.strip().replace("$", "").replace(",", "")
            if revenue:
                gme_revenue = pd.concat([gme_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])], ignore_index=True)

gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"], errors="coerce")
print(gme_revenue.tail())
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(figsize=(14,6))

ax1.plot(tesla_stock['Date'], tesla_stock['Close'], color='blue', label='Tesla Stock Price')
ax1.set_ylabel('Stock Price')
ax1.set_xlabel('Date')
ax1.legend(loc='upper left')

# Align revenue dates
tesla_revenue['Date'] = pd.to_datetime(tesla_revenue['Date'])
ax2 = ax1.twinx()
ax2.plot(tesla_revenue['Date'], tesla_revenue['Revenue'], color='green', label='Tesla Revenue')
ax2.set_ylabel('Revenue (in billions)')
ax2.legend(loc='upper right')

plt.title('Tesla Stock Price vs Revenue')
plt.show()
fig, ax1 = plt.subplots(figsize=(14,6))

ax1.plot(gme_stock['Date'], gme_stock['Close'], color='red', label='GameStop Stock Price')
ax1.set_ylabel('Stock Price')
ax1.set_xlabel('Date')
ax1.legend(loc='upper left')

# Align revenue dates
gme_revenue['Date'] = pd.to_datetime(gme_revenue['Date'])
ax2 = ax1.twinx()
ax2.plot(gme_revenue['Date'], gme_revenue['Revenue'], color='orange', label='GameStop Revenue')
ax2.set_ylabel('Revenue (in billions)')
ax2.legend(loc='upper right')

plt.title('GameStop Stock Price vs Revenue')
plt.show()
