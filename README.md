# bank_of_canada_api

Retrieve and chart historical financial data from Bank of Canada (BOC) using Valet API.
API Docs: https://www.bankofcanada.ca/valet/docs

Parameters:
- series (str): Bank of Canada Series name
- start_date (str): start of the historical period (format YYYY-MM-DD)
- end_date (str): end of the historical period (format YYYY-MM-DD)

Returns:
- image (png): saves a png file of series charted as a line chart
- api_data (csv): saves a csv file of the series data