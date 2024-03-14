""" 
This module contains api data retrieval functions for the Bank of Canada's Valet API.
"""

import requests
import pandas as pd

def get_series_data(series, start_date, end_date):
    """
    Return json data from Bank of Canada series using the Bank of Canada Valet API 
    API Docs: https://www.bankofcanada.ca/valet/docs
    Series Observation API: https://www.bankofcanada.ca/valet/observations/...
    Series Description API: "https://www.bankofcanada.ca/valet/series/...

    Parameters:
    - series (str): Bank of Canada Series name
    - start_date (str): start of the historical period (format YYYY-MM-DD)
    - end_date (str): end of the historical period (format YYYY-MM-DD)
    
    Returns:
    - dataframe: series data for the selected time period
    - csv: saves the data in a local csv file (api_data_[SERIES].csv) 
    """


    url = (f"https://www.bankofcanada.ca/valet/observations/{series}/json"
            f"?start_date={start_date}&end_date={end_date}")
    desc_url = f"https://www.bankofcanada.ca/valet/series/{series}/json"

    # return data observations and variable description
    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            json_data = response.json()['observations']
            df = pd.DataFrame(json_data)

            try:
                response = requests.get(desc_url)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    desc = response.json()['seriesDetails']['description']

                else:
                    print(f"Request error: {response.status_code}")

            except Exception as e:
                print(f"An error occured {e}")

            df.columns = ['date', desc]
            df.to_csv(f"api_data_{series}.csv")
            return df

    except Exception as e:
        print(f"An error occured {e}")



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('series', help='Series Name')
    parser.add_argument('start_date', help='Start Date (YYYY-MM-DD)')
    parser.add_argument('end_date', help='End Date (YYYY-MM-DD)')
    args = parser.parse_args()

    get_series_data(args.series, args.start_date, args.end_date)
