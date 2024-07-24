import config

import mysql.connector

from database import database_util
from ingests.ingest_subclasses import IngestCandidateMasterCN

connection = mysql.connector.connect(
    host=config.URL,
    database=database_util.DB_NAME,
    user=config.USERNAME,
    password=config.PASSWORD
)
cursor = connection.cursor()


def main():
    IngestCandidateMasterCN.evaluate(cursor)


if __name__ == '__main__':
    # Setup mysql database
    database_util.create_database(connection, cursor)
    database_util.create_tables(cursor)

    # Process files into tables
    main()

    # Close resources
    cursor.close()
    connection.close()
