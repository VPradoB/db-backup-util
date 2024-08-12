from enum import Enum

import click


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    @classmethod
    def values(cls):
        return [attr.value for attr in cls]

    @classmethod
    def names(cls):
        return [attr.name for attr in cls]


class DBTypeEnum(BaseEnum):
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"
    MSSQL = "mssql"


class IntervalEnum(BaseEnum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    NEVER = "never"


class IntervalType(click.ParamType):
    name = "interval"

    def convert(self, value, param, ctx):
        if value not in IntervalEnum.values():
            self.fail(f"Invalid interval: {value}", param, ctx)
        return value


class DBType(click.ParamType):
    name = "db-type"

    def convert(self, value, param, ctx):
        if value not in DBTypeEnum.values():
            self.fail(f"Invalid database type: {value}", param, ctx)
        return value
