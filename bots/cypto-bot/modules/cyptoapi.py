import json
import requests
import pandas as pd

def fetch_rates():
    res = requests.get('https://api.coincap.io/v2/rates?') 
    l = res.json()['data']
    df = pd.DataFrame(l)
    df.rateUsd = pd.to_numeric(df.rateUsd)
    return df

def get_price(df=df, symbol='BTC'):
    pr  = float(df[df.symbol == symbol].rateUsd.values[0])
    return pr

def get_info(df=df, symbol='BTC'):
    info = df[df.symbol == symbol]
    return info

def get_id_from_symbol(df=df, symbol='BTC'):
    i_d = df[df.symbol == symbol].id.values[0]
    return i_d



