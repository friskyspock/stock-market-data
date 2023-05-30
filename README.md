# Stock Market data import

- This code will import historical stock data for any company of choice.

- It is using GOOGLEFINANCE function in Google sheets to get data. For more information about this visit [here](https://support.google.com/docs/answer/3093281?hl=en)

- This data from sheet is accessed using Google Sheets API. Read more about Google Sheets API [here](https://developers.google.com/sheets/api/guides/concepts)

- Get valid credentials for service account from Google Cloud Console. Read the instructions [here](https://cloud.google.com/iam/docs/service-accounts-create)

- The sample credential file is shown: [service.json](service.json)

Run the script scrape_data.py. Sample terminal snip is shown:
```bash
***********************************
Stock Market Data Scrapper
by: Aniket Masaye
***********************************
This will give you default stock history of NSE:RELIANCE
Do you want data for other company?
enter y/n:y
Input appropriate symbol for company:NSE:TATASTEEL
Input start date in format yyyy-mm-dd:2020-01-01
Input end date in format yyyy-mm-dd:2023-01-01
writing data to google sheet.
3 cells updated.
reading from google sheet.
data fetched.
data saved in data.csv
```