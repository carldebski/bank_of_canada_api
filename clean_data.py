# This module contains data cleanup functions for dataframe created from json data from
# the Bank of Canada's Valet API


import pandas as pd 

def clean_data(df):
    """
    Clean up series V122150, federal fund rate data from Valet API
    
    Parameters:
    - df (pd.DataFrame): df converted from json 

    Returns:
    - dataframe: cleaned dataframe
    """

    df['date'] = pd.to_datetime(df['date'])
    col_name = df.columns[-1]
    df[col_name] = [float(i['v']) for i in df.iloc[:, -1]]

    return df



if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('dataframe', help='Dataframe from Bank of Canada json file')
    args = parser.parse_args()

    clean_data(args.dataframe)
    