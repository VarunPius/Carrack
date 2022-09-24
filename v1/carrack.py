#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : carrack.py                                         ##
# Description : Main program                                       ##
#####################################################################
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
