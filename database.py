import psycopg2
import os

class Database:
    def __init__(self):
        self.creds = os.environ['PGSQL_CREDS'].split(';')
        self.user = self.creds[0]
        self.pw = self.creds[1]
        self.conn_string = f"host='localhost' dbname='postgres' user='{self.user}' password='{self.pw}'"
        self.conn = psycopg2.connect(self.conn_string)
        self.cur = self.conn.cursor()

    def get_table(self, table_name):
        sql = f"SELECT * FROM {table_name}"
        self.cur.execute(sql)
        records = cur.fetchall()
        return records

    def upsert_data(self, data, table_name):
        col_len = len(data[0])
        # create str format of (%s,%s,%s...)
        str_format = '(' + ','.join('%s' for x in range(col_len)) + ')'
        print(str_format)

        # divide list into chunks of 10000
        for i in range(0, len(data), 10000):
            array = data[i:i + 10000]

            # mogrify row using str_format
            args_str = ','.join(self.cur.mogrify(str_format, x).decode('utf-8') for x in array)

            self.cur.execute(f"INSERT INTO {table_name} VALUES " + args_str + "ON CONFLICT DO NOTHING;")
            self.conn.commit()

    def close_connection(self):
        self.cur.close()
        self.conn.close()
