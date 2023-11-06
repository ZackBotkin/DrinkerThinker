import sqlite3

class QueryRunner(object):

    def __init__(self, config):
        self.config = config
        self.database_file_name = "%s\\%s.db" % (
            self.config.get("database_directory"),
            self.config.get("database_name")
        )

    def run_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        conn.execute(sql_str)
        conn.commit()

    def fetch_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        query = conn.execute(sql_str)
        results = query.fetchall()
        return results

    def create_all_tables(self):
        self.create_table()
        self.create_drinks_table()

    def create_table(self):
        sql_str = "CREATE TABLE test(date DATE, count INT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def create_drinks_table(self):
        sql_str = "CREATE TABLE drinks(num_drinks INT, comment VARCHAR, date DATE)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def record_drinks(self, num_drinks, comment, date):
        sql_str = "INSERT INTO drinks VALUES ('%s', '%s', '%s')" % (num_drinks, comment, date)
        self.run_sql(sql_str)
        
    def read_drinks(self):
        sql_str = "SELECT * FROM drinks"
        return self.fetch_sql(sql_str)

