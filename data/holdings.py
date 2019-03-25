#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : holdings.py                                        ##
# Description : Module to get holdings data                        ##
#####################################################################
#
# History:
# Change 1:
#   Modified on: 23-Mar-2019
#   Change Specification: [ARCH-001]

# Standard Modules:
import json

# Functions and Methods:
def get_holdings():
    with open('data/assets.json') as data_file:
        asset_data = json.load(data_file)
    
    holding_dict = {}
    for company in asset_data:
        holding_dict[company] = asset_data[company]["shares"]
        
    return holding_dict