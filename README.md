# Database Backup Utility
## Overview
The Database Backup Utility is a command-line tool designed to automate the process of backing up databases. It supports multiple database systems, provides options for full and incremental backups, and can be scheduled to run at regular intervals. The tool is designed for ease of use and reliability, ensuring your data is securely stored.

## Features
- Supports Multiple Databases: Compatible with PostgreSQL.
- Customizable Backup Locations: Save backups to local directories.

## Next steps
- Support for more databases (MYSQL, MSSQL).
- Automated Scheduling: Schedule backups to run at regular intervals.
- Notification System: Get notifications via email or webhook on backup completion or failure.
- Support for native DB backup utilities.
- 0 Compression & Encryption: Optional compression and encryption for secure storage.
- Full & Incremental Backups: Choose between full backups or incremental backups to save space.
- Logging: Detailed logs for monitoring and troubleshooting.
- Configuration File: Customize default settings in a configuration file.

## Installation
### Prerequisites

- Python 3.12+
- Pip (Python package manager)
### Steps
1. Clone the repository:

```bash
git clone https://github.com/username/db-backup-utility.git
```

2. Navigate to the project directory:
```bash 
cd db-backup-utility
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage
### Basic Commands
- Backup a Database:
```bash
python backup.py --db-type mysql --host localhost --user root --password mypassword --database mydb --backup-type full
```
Replace the placeholders with your actual database details.

- Schedule a Backup:
```bash
python schedule_backup.py --db-type mysql --host localhost --user root --password mypassword --database mydb --interval daily 
```

### Command-Line Options
- **--db-type**: Type of database (mysql, postgresql, mssql).
- **--host**: Database host.
- **--user**: Database user.
- **--password**: Database password.
- **--database**: Name of the database.
- **--backup-type**: Type of backup (full, incremental).
- **--interval**: Scheduling interval (daily, weekly, monthly).

### Example
To perform a full backup of a MySQL database and save it to a remote server with encryption enabled:

```bash
python backup.py --db-type mysql --host localhost --user root --password mypassword --database mydb --backup-type full --encrypt --remote-server user@remote-server:/backups/
```

## Configuration (Work in Progress)
**`config.yaml`** \
You can configure default settings in the config.yaml file. This includes database credentials, backup locations, and notification settings.

```yaml
default:
  db_type: mysql
  host: localhost
  user: root
  password: mypassword
  database: mydb
  backup_location: /backups
  encrypt: true
  notify:
    email: user@example.com
```
## Logging (Work in Progress)
Logs are stored in the logs/ directory by default. You can customize the log level and output format in the config.yaml file.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Support
If you encounter any issues, please open an issue on GitHub or contact the maintainer at [vmpradob@gmail.com](mailto:vmpradob@gmail.com).
