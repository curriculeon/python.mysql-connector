# Created by Leon Hunter at 8:01 PM 10/25/2020
import mysql.connector


class MySqlConfigurator(object):
    def __init__(self, database_name):
        self.database_name = database_name

    def get_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

    def drop(self):
        self.execute("DROP DATABASE IF EXISTS {};".format(self.database_name))

    def create(self):
        self.execute("CREATE DATABASE IF NOT EXISTS {};".format(self.database_name))

    def use(self):
        self.execute("USE {};".format(self.database_name))

    def execute(self, statement):
        print("Executing statement `{}`".format(statement))
        self.get_connection().cursor().execute(statement)
