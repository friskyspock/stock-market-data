def fetch_data(start_date,end_date,company="NSE:RELIANCE"):
    
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    import numpy as np
    import pandas as pd

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'service.json'
    SPREADSHEET_ID = '1X-xoG2XtUp4CGE5UBZgVeXE5pQMQQLR4S7By-WrKBn8'

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    # Please enter dates in format yyyy-mm-dd
    days = np.busday_count(start_date,end_date)

    body = {'values':[[company,start_date,end_date]]}
    # Writing dates in spreadsheet
    print("writing data to google sheet.")
    try:
        sheet = service.spreadsheets()
        output = sheet.values().update(spreadsheetId=SPREADSHEET_ID,range="A1:C1",valueInputOption="USER_ENTERED",body=body).execute()
        print(f"{output.get('updatedCells')} cells updated.")
    except HttpError as error:
        print(f"An error occurred: {error}")
    
    # Reading data from spreadsheet
    print("reading from google sheet.")
    try:
        data_range = "A3:F"+str(days)
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=data_range).execute()
        values = result.get('values', [])
        if not values:
            print("no data found")
    except HttpError as error:
        print(error)

    print("data fetched.")
    data = pd.DataFrame(values[1:],columns=values[0])
    return data

def main():
    print("***********************************\nStock Market Data Scrapper\nby: Aniket Masaye\n***********************************")
    print("This will give you default stock history of NSE:RELIANCE")
    y = input("Do you want data for other company?\nenter y/n:")
    if y=="y":
        company = input("Input appropriate symbol for company:")
    elif y=="n":
        company = "NSE:RELIANCE"
    start = str(input("Input start date in format yyyy-mm-dd:"))
    end = str(input("Input end date in format yyyy-mm-dd:"))
    data = fetch_data(start,end,company=company)
    data.to_csv("data.csv",index=False)
    print("data saved in data.csv")

if __name__ == '__main__':
    main()