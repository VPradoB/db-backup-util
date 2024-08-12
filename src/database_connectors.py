from abc import ABC, abstractmethod

import psycopg2

from src.click_params import DBTypeEnum, IntervalEnum


class DatabaseConnector(ABC):
    def __init__(
        self,
        db_type: DBTypeEnum,
        host: str,
        port: int,
        database: str,
        user: str,
        password: str,
        interval: IntervalEnum,
    ):
        self.db_type = db_type
        self.host = host
        self.port = port
        self.db_name = database
        self.user = user
        self.password = password
        self.schedule_interval = interval
        self.connection = None

    @abstractmethod
    def connect(self):
        """Connect to the database"""

    @abstractmethod
    def disconnect(self):
        """Disconnect from the database"""

    @abstractmethod
    def backup(self):
        """Backup the database"""


class MySQLDatabaseConnector(DatabaseConnector):
    def connect(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def backup(self):
        raise NotImplementedError


class PostgreSQLDatabaseConnector(DatabaseConnector):

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.db_name,
            user=self.user,
            password=self.password,
        )

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def backup(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM information_schema.tables")
            tables = list(
                filter(
                    lambda x: x[1]
                    not in [
                        "pg_catalog",
                        "pg_statistic",
                        "information_schema",
                    ],
                    cursor.fetchall(),
                )
            )
            for table in tables:
                table_name = f"{table[1]}.{table[2]}"
                cursor.execute(f"SELECT * FROM {table_name}")
                columns = [desc[0] for desc in cursor.description]
                data = cursor.fetchall()
                yield {"table_name": table_name, "columns": columns, "data": data}


class MSSQLDatabaseConnector(DatabaseConnector):
    def connect(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def backup(self):
        raise NotImplementedError
