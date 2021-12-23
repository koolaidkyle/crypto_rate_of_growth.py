import streamlit as st
import requests
import pandas as pd

st.write("""
# Simple Crypto Rate of Growth APP
""")
st.write("""
### Rate of Growth formula: (d2-d1)/d1*100
""")

start = st.date_input("Enter start date for rate of growth calculation: ")
end = st.date_input("Enter end date for rate of growth calculation: ")

def get_crypto_price(symbol, exchange, start):
    api_key = 'YOUR API'
    api_url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={symbol}&tsym={exchange}&limit={start}&api_key={api_key}'
    raw = requests.get(api_url).json()
    df = pd.DataFrame(raw['Data']['Data'])[['time', 'high']].set_index('time')
    df.index = pd.to_datetime(df.index, unit = 's')
    return df

BTC = get_crypto_price('BTC', 'USD', start)
BTC
