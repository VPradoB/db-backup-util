import click

from src.database_connectors import DatabaseConnector
from src.file_manager import FileManager


class Exporter:
    def __init__(self, db_connector: DatabaseConnector, file_manager: FileManager):
        self.db_connector = db_connector
        self.file_manager = file_manager

    def execute(self):
        click.echo("connecting to the database")
        self.db_connector.connect()
        click.echo("backup started...")
        backup = list(self.db_connector.backup())
        self.file_manager.export(backup)
        self.db_connector.disconnect()
        click.echo("backup done")
