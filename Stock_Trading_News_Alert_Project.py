import requests
from twilio.rest import Client

# ------------------- CONFIG -------------------
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# 👉 Replace with your real keys/tokens
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "+15167306982"     # Your Twilio phone number
MY_PHONE_NUMBER = "+8801XXXXXXXXX"       # Your verified phone number

# ------------------- STOCK DATA -------------------
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()

# Safety check for missing data (e.g., API limit hit)
if "Time Series (Daily)" not in data:
    raise Exception("Error fetching stock data:", data)

daily_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in daily_data.items()]

# Get yesterday's and day-before-yesterday's closing prices
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# ------------------- PRICE DIFFERENCE -------------------
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"

# Percentage difference (based on older closing price)
diff_percent = round((difference / day_before_yesterday_closing_price) * 100, 2)

print(f"{STOCK_NAME} {up_down}{diff_percent}%")

# ------------------- NEWS FETCH -------------------
if abs(diff_percent) > 1:  # Send news only if move is significant
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "sortBy": "publishedAt",
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get("articles", [])

    # Get top 3 articles (if available)
    three_articles = articles[:3]

    # Format messages
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}"
        for article in three_articles
    ]

    # ------------------- SEND SMS -------------------
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
        print(f"Sent message: {message.status}")