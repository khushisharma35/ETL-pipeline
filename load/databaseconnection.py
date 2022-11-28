import psycopg2
import sys
sys.path.insert(1, '/Users/apple/PycharmProjects/etlproject/')
import config
from load import createtable


# establishing the connection
class Database:
    """PostgreSQL Database class."""

    def __init__(self):
        self.host = config.host
        self.username = config.username
        self.password = config.password
        self.port = config.port
        self.databasename = config.databaseName
        self.conn = None
        self.cur = None


    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    database=self.databasename
                )
                self.cur = self.conn.cursor()


                try:
                    # command = createtable.create_food_item()
                    # command1 =createtable.create_nutrients()
                    # command2 = createtable.create_food_nutrients_mapping()
                    command3 = createtable.create_recipe()
                    # self.cur.execute(command)
                    # self.cur.execute(command1)
                    # self.cur.execute(command2)
                    self.cur.execute(command3)
                    self.conn.commit()
                    self.cur.close()


                    # close communication with the PostgreSQL database server
                except Exception as e:
                    pass
                self.conn.commit()
                self.cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)


# Connection established to: (
#    'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
# )


    def insert_rows(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()
        self.cur.close()