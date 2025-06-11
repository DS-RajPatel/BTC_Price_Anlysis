
import requests
from datetime import datetime, timedelta
import pyodbc
import time

# Azure SQL Connection String
server = 'btc-sql-server.database.windows.net'
database = 'BTCData'
username = 'Raj_btcadmin'
password = 'Shivam@73598'  # replace with your actual password

connection_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

def get_latest_btc_binance():
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": "BTCUSDT", "interval": "1m", "limit": 1}
    response = requests.get(url, params=params)
    data = response.json()[0]
    
    utc_time = datetime.utcfromtimestamp(data[0] / 1000)
    ist_time = utc_time + timedelta(hours=5, minutes=30)

    open_, high, low, close, volume = map(float, data[1:6])
    price_change_pct = ((close - open_) / open_) * 100
    direction = "Up" if close > open_ else "Down"
    volatility = ((high - low) / open_) * 100

    return {
        "datetime": ist_time,
        "open": open_,
        "high": high,
        "low": low,
        "close": close,
        "volume": volume,
        "price_change_pct": price_change_pct,
        "direction": direction,
        "volatility": volatility
    }

def push_to_sql(data):
    try:
        conn = pyodbc.connect(connection_str)
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO BTCData (datetime, open_price, high, low, close_price, volume, price_change_pct, direction, volatility)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, data["datetime"], data["open"], data["high"], data["low"],
                       data["close"], data["volume"], data["price_change_pct"],
                       data["direction"], data["volatility"])
        conn.commit()
        print(f"✅ Inserted at {data['datetime']}")
    except Exception as e:
        print(f"❌ Failed to insert: {e}")

while True:
    btc_data = get_latest_btc_binance()
    push_to_sql(btc_data)
    time.sleep(60)  # Push every 1 minute
