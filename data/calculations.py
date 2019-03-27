#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : calculation.py                                     ##
# Description : Module to get holdings data                        ##
#####################################################################
#
# History:
# Change 1:
#   Last Modified on: 27-Mar-2019
#   Change Specification: [ENG-002]

# Standard Modules:
import json
import datetime
# External Modules:
import requests

# Functions and Methods:
def get_value(asset_dict: dict):
    batch_asset = ""
    price_dict = {}

    for asset in asset_dict:
        batch_asset = batch_asset + asset + ","
    batch_asset = batch_asset[:-1]

    url = "https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols={}&apikey=<demo>".format(batch_asset)
    getData = requests.get(url)
    requests_data = json.loads(getData.text)

    for quotes in requests_data['Stock Quotes']:
        symbol = quotes['1. symbol']
        price_dict[symbol] = float(quotes['2. price'])

    print(price_dict)
    return price_dict

def calculate_value(asset_dict: dict):
    asset_value_dict = {}
    total_value = 0
    price_dict = get_value(asset_dict)

    for asset in asset_dict:
        shares = asset_dict[asset]
        price = price_dict[asset]
        asset_value_dict[asset] = round(shares * price, 2)
        total_value = total_value + round(shares * price, 2)

    print(asset_value_dict, total_value)
    return asset_value_dict, total_value

def calculate_percent(asset_dict: dict, total_value: int):
    holding_percent_dict = {}
    for asset in asset_dict:
        share_value = asset_dict[asset]
        percent = round((share_value * 100)/total_value, 2)
        holding_percent_dict[asset] = percent
    
    print(holding_percent_dict)
    return holding_percent_dict

