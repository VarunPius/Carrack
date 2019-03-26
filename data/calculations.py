#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : calculation.py                                     ##
# Description : Module to get holdings data                        ##
#####################################################################
#
# History:
# Change 1:
#   Last Modified on: 25-Mar-2019
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
    price_dict = get_value(asset_dict)

    for asset in asset_dict:
        shares = asset_dict[asset]
        price = price_dict[asset]
        asset_value_dict[asset] = round(shares * price, 2)

    print(asset_value_dict)
    return asset_value_dict

