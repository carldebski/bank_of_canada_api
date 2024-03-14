"""
Retrieve and chart historical financial data from Bank of Canada (BOC) using Valet API.
API Docs: https://www.bankofcanada.ca/valet/docs

Parameters:
- series (str): Bank of Canada Series name
- start_date (str): start of the historical period (format YYYY-MM-DD)
- end_date (str): end of the historical period (format YYYY-MM-DD)

Returns:
- image (png): saves a png file of series  
"""


from get_boc_data import get_series_data
from clean_data import clean_data
import seaborn as sns 
import matplotlib.pyplot as plt


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('series', help='file path (csv)')
    parser.add_argument('start_date', help='file path (csv)')
    parser.add_argument('end_date', help='file path (csv)')
    args = parser.parse_args()

    # retrieve and clean API data
    series_df = get_series_data(args.series, args.start_date, args.end_date)
    series_df = clean_data(series_df)

    # save a png file of the charted data
    series_name = series_df.columns[-1]
    sns.lineplot(x='date', y=series_name, data=series_df)
    plt.figure(figsize=(3, 3))
    plt.savefig("seaborn_plot.png")
    plt.close()
