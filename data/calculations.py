#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : calculation.py                                     ##
# Description : Module to get holdings data                        ##
#####################################################################
#
# History:
# Change 1:
#   Modified on: 24-Mar-2019
#   Change Specification: [ENG-002]

# Standard Modules:
import json
import datetime
# External Modules:
import requests

# Functions and Methods:
def calculate_value(asset_dict: dict):
    print(asset_dict)
    asset_value_dict = {}
    for asset in asset_dict:
        shares = asset_dict[asset]
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

        getData = requests.post(url)
