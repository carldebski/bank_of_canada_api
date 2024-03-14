# bank_of_canada_api

bank_of_canada_api is a python library for retrieving and charting historical financial data from Bank of Canada (BOC) using Valet API.
API Docs: https://www.bankofcanada.ca/valet/docs

## Environment
Requires the following libraries 
- Pandas 
- Seaborn
- Matplotlib
- Requests

Requires internet access to Bank of Canada API

## Parameters
- series (str): Bank of Canada Series name
- start_date (str): start of the historical period (format YYYY-MM-DD)
- end_date (str): end of the historical period (format YYYY-MM-DD)

## Returns
- image (png): saves a png file of series charted as a line chart
- api_data (csv): saves a csv file of the series data

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)