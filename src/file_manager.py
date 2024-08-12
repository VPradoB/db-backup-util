from typing import TypedDict


class ExportData(TypedDict):
    table_name: str
    columns: list[str]
    data: list[list]


class FileManager:
    def __init__(self, output_file_path: str):
        self.output_file_path = output_file_path

    def export(self, data: [ExportData]):
        with open(self.output_file_path, "w", encoding="utf-8") as f:
            for row in data:
                values = []
                for value in row.get("data"):
                    if isinstance(value, str):
                        values.append(f"'{value}'")
                    elif value is None:
                        values.append("NULL")
                    else:
                        values.append(str(value))
                values_str = ", ".join(values)
                sql = f"INSERT INTO {row.get("table_name")} ({', '.join(row.get("columns"))}) VALUES ({values_str});\n"
                f.write(sql)
