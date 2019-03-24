####
# main code
# Author: Varun Pius Rodrigues
####

#import requests
import datetime
import data.holdings as holdings

#def get_holdings():
#    
#    return

def main():
    holdings.get_holdings()

if __name__ == "__main__":
    main()

## https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo
## naming convention:module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name
