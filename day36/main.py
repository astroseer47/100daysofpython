from telnetlib import theNULL

import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "27WQQZO6GKNOJO1E"
NEWS_API_KEY = "52cbe606c06e4a47ab5986e8c17ca9c5"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_daily_url = f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}"
response = requests.get(stock_daily_url)
response.raise_for_status()
data = response.json()

daily = data["Time Series (Daily)"]
daily_data_list = [value for (key, value) in daily.items()]

yesterday = daily_data_list[0]
yesterday_close = yesterday["4. close"]

day_before_yesterday = daily_data_list[1]
day_before_yesterday_close = day_before_yesterday["4. close"]

print(yesterday_close)
print(day_before_yesterday_close)
positive_difference = abs(float(yesterday_close) - float(day_before_yesterday_close))
print(positive_difference)

diff_percent = (positive_difference / float(day_before_yesterday_close)) * 100
print(diff_percent)

if diff_percent > 2:
    news_url = f"{NEWS_ENDPOINT}"
    news_response = requests.get(news_url , params={'apikey': NEWS_API_KEY, "qInTitle": COMPANY_NAME})
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]

    three_articles = articles[:3]
new_list = [f"Headline: {item.title}. \n Brief: {item.description}" for item in three_articles]

print(new_list)