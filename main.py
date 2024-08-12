from datetime import datetime
from os import path

import click
from src.click_params import DBType, DBTypeEnum, IntervalType, IntervalEnum

from src.database_connectors import (
    MySQLDatabaseConnector,
    PostgreSQLDatabaseConnector,
    MSSQLDatabaseConnector,
)
from src.exporter import Exporter
from src.file_manager import FileManager


def sanitize_input(
    db_type, host, port, database, user, password, output_path, interval
):
    if not path.isdir(output_path):
        raise ValueError("Output path is not a directory")

    if db_type == DBTypeEnum.MYSQL.value:
        user = user if user else "root"
        port = port if port else 3306

    if db_type == DBTypeEnum.POSTGRESQL.value:
        user = user if user else "postgres"
        port = port if port else 5432

    if db_type == DBTypeEnum.MSSQL.value:
        user = user if user else "sa"
        port = port if port else 1433

    return {
        "db_type": db_type,
        "host": host,
        "port": port,
        "database": database,
        "user": user,
        "password": password,
        "output_path": output_path,
        "interval": interval,
    }


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--db-type",
    type=DBType(),
    required=True,
    help="database type, options: mysql, postgresql, mssql",
)
@click.option("--host", default="localhost", help="database host")
@click.option("--port", help="database port")
@click.option("--database", required=True, help="database name")
@click.option("--user", default="root", help="database user")
@click.option("--password", help="database password")
@click.option(
    "--output-path",
    default="./",
    help="output file path to store the backup. Default is current directory.",
)
@click.option(
    "--interval",
    type=IntervalType(),
    default=IntervalEnum.NEVER.value,
    help="Scheduling interval (daily, weekly, monthly).",
)
def backup(db_type, host, port, database, user, password, output_path, interval):
    params = sanitize_input(
        db_type, host, port, database, user, password, output_path, interval
    )

    output_path = params.pop("output_path")

    match db_type:
        case DBTypeEnum.MYSQL.value:
            db_connector = MySQLDatabaseConnector(**params)
        case DBTypeEnum.POSTGRESQL.value:
            db_connector = PostgreSQLDatabaseConnector(**params)
        case DBTypeEnum.MSSQL.value:
            db_connector = MSSQLDatabaseConnector(**params)
        case _:
            raise ValueError("Invalid database type")

    file_manager = FileManager(
        output_file_path=path.join(
            output_path,
            f"{database}_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql",
        )
    )
    exporter = Exporter(db_connector, file_manager)
    exporter.execute()


cli.add_command(backup)

if __name__ == "__main__":
    try:
        cli()
    except Exception as e:
        print(e)
