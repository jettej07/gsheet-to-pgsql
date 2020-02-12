from database import Database
from my_gsheets import Gsheets


if __name__ == "__main__":
    g = Gsheets()
    data = g.get_data('employee')
    d = Database()
    d.upsert_data(data, 'employee')
    d.close_connection()
