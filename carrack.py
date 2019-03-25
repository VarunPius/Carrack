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
#
# //TODO: Check naming :=> Dataframe Checked; variables pending
# //TODO: Verify if combined data is needed

# Standard Modules:
import datetime
# External Modules:
import requests
# Project Modules:
import data.holdings as holdings
import data.calculations as calculations

# Functions and Methods:

# Main method:
def main():
    holding_dict = holdings.get_holdings()
    calculations.calculate_value(holding_dict)

if __name__ == "__main__":
    main()


#################################################
## Rough:
## https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo
## naming convention:module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name
