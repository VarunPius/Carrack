#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : holdings.py                                        ##
# Description : Module to get holdings data                        ##
#####################################################################

# Standard Modules:
import json

# Functions and Methods:
def get_holdings():
    with open('data/assets_main.json') as data_file:
        asset_data = json.load(data_file)
    
    holding_dict = {}
    for company in asset_data:
        holding_dict[company] = asset_data[company]["shares"]
        
    return holding_dict