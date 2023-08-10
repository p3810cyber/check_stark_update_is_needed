import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tqdm import tqdm

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('serviceaccount.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/13PgmCtjcvApTdMSvdK7RqBdf9s5WE3_SoLX7KISV33M/edit#gid=0")
worksheet = spreadsheet.get_worksheet(0)

with open('addresses.txt', 'r') as file:
    addresses_to_check = [line.strip() for line in file.readlines()]

matching_addresses = []
for address in tqdm(addresses_to_check, desc="Address analysis"):
    if address in worksheet.col_values(1):
        matching_addresses.append(address)

with open('results.txt', 'w') as file:
    for address in matching_addresses:
        file.write(address + '\n')

print("Analysis completed. Check results in the results.txt.")
