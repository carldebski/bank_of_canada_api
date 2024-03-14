# This module contains api data retrieval functions for the Bank of Canada's Valet API. 


import requests
import pandas as pd

def get_series_data(series, start_date, end_date):
    """
    Return json data from Bank of Canada series using the Bank of Canada Valet API 
    API Docs: https://www.bankofcanada.ca/valet/docs
    Series Observation API: https://www.bankofcanada.ca/valet/observations/...

    Parameters:
    - series (str): Bank of Canada Series name
    - start_date (str): start of the historical period (format YYYY-MM-DD)
    - end_date (str): end of the historical period (format YYYY-MM-DD)
    
    Returns:
    - dataframe: series data for the selected time period
    - csv: saves the data in a local csv file (api_data_[SERIES].csv) 
    """
    

    url = "https://www.bankofcanada.ca/valet/observations/{}/json?start_date={}&end_date={}".format(series, start_date, end_date)
    
    try:
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            json_data = response.json()['observations']
            df = pd.DataFrame(json_data)
            df.to_csv('api_data_{}.csv'.format(series))
            return df
        else:
            print("Request error: {}".format(response.status_code))
    
    except:
        print('Error: No response')
        return None


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('series', help='Series Name')
    parser.add_argument('start_date', help='Start Date (YYYY-MM-DD)')
    parser.add_argument('end_date', help='End Date (YYYY-MM-DD)')
    args = parser.parse_args()

    get_series_data(args.series, args.start_date, args.end_date)
