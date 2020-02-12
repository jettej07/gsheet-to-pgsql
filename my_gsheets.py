import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Gsheets:
    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', self.scope)
        self.auth = gspread.authorize(self.creds)
        self.key = '1SdbxY0XxiV6EqaoKNhW_jRCGK3013q5ayns4_lYrzRU'
        self.gs = self.auth.open_by_key(self.key)
        self.sheets = ['employee', 'manager', 'sales', 'items']

    def get_data(self, tab_name):
        sheet = self.gs.worksheet(tab_name)
        data = sheet.get_all_values()[1:]
        return data

    def get_all_data(self):
        all_data = {}
        for sheet in self.sheets:
            # get all values except the header
            all_data[sheet] = self.gs.worksheet(sheet).get_all_values()[1:]
        return all_data
