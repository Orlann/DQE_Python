import sqlite3
import logging
import logging.config


class SQLWorker:
    def __init__(self, database_name):
        self.database_name = database_name
        logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
        self.logger = logging.getLogger("SQL_worker")

    def __get_connection(self):
        self.logger.info("Connection to DB")
        return sqlite3.connect(self.database_name)

    def execute_sql(self, command):
        with self.__get_connection() as connection:
            connection.cursor().execute(command)
            self.logger.info(f"Execute command: {command}")

    def insert_sql(self, table, values):
        with self.__get_connection() as connection:
            connection.cursor().execute(f'INSERT INTO {table} VALUES(?, ?, ?, ?, ?, ?)', values)
            self.logger.info(f"INSERT INTO {table}")
