import mysql.connector


class UseDatabase:

    def __init__(self, db_config: dict):
        self.configuration = db_config

    def __enter__(self):
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionErrors(err)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLErrors(exc_val)


class ConnectionErrors(Exception):
    pass


class SQLErrors(Exception):
    pass
