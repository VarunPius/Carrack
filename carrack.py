#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : carrack.py                                         ##
# Description : Main program                                       ##
#####################################################################
#
# History:
# Change 1:
#   Modified on: 23-Mar-2019
#   Change Specification: [ARCH-001]
# Change 2:
#   Modified on: 25-Mar-2019
#   Change Specification: [ENG-003]
# Change 3:
#   Modified on: 25-Mar-2019
#   Change Specification: [ENG-002]
#
# //TODO: Check naming :=> Dataframe Checked; variables pending
# //TODO: Verify if combined data is needed

# Standard Modules:
import datetime
import argparse
# External Modules:
import requests
# Project Modules:
import data.holdings as holdings
import data.calculations as calculations

# Functions and Methods:

# Main method:
def main():
    parser = argparse.ArgumentParser(description="Personal financial help scripts")
    #parser.add_argument("--values", '-v', help='get current value of equity in personal holdings')
    #parser.add_argument("--calculate", '-c', help='calculate current value of all personal holdings')
    parser.add_argument("--mode", '-m', choices=['v','ct'], default='calculate',
                        help="a) v | values: Get current value of equity in personal holdings."
                             "b) ct | calculate total: Calculate current value of all personal holdings")

    args = parser.parse_args()

    holding_dict = holdings.get_holdings()

    if args.mode == "v":
        calculations.get_value(holding_dict)
    elif args.mode == "ct":
        asset_value_dict, total_value = calculations.calculate_value(holding_dict)
        holding_percent_dict = calculations.calculate_percent(asset_value_dict, total_value)

if __name__ == "__main__":
    main()



#####################################################
##    Rough:                                       ##
#####################################################
## https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo
## naming convention:module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name
## Quandl url: not used since last date available is 2018-03-27
##   url = "https://www.quandl.com/api/v3/datasets/WIKI/{}/data.json?api_key=reuP1L2Rue8aB3kBL9P6".format("MSFT")
##   url = "https://www.quandl.com/api/v3/datasets/WIKI/MSFT.json?column_index=4&start_date=2019-03-24&end_date=2019-03-25&api_key=reuP1L2Rue8aB3kBL9P6"
