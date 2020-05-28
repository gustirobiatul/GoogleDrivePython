import gspread 
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('*yourapi*.json', scope)
client = gspread.authorize(creds)

sheet = client.open('amount').sheet1
quantity = sheet.get_all_values()
print(quantity)
q=sheet.col_values(1)
cell = sheet.find("0")
print("The amount that empty is on column R%sC%s, or called %s" % (cell.row, cell.col, sheet.cell(cell.row,1).value))


