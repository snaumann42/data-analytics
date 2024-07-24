import os
import re


class Ingest:
    """A class to define the basic functionality of our ingests."""

    base_ingest_path = './data-files/'
    ingest_file_format = ''
    destination_columns = ()
    destination_table = ''

    # This will result in "INSERT INTO table_name (column1, column2...) VALUES (%s, %s...)" using
    # the overridden class variables
    _insert_statement = ''

    @classmethod
    def evaluate(cls, database_cursor):
        base_path = cls.base_ingest_path
        ingest_files = filter(lambda f: os.path.isfile(base_path + f)
                                        and re.search(cls.ingest_file_format, f),
                              os.listdir(base_path))

        for file in ingest_files:
            print("processing file: " + file)
            with open(base_path + file) as file_handle:
                count = 0
                bad_lines = 0
                row_data = []
                for line in file_handle:
                    row = line.rstrip('\n').split("|")
                    if len(row) != len(cls.destination_columns):
                        bad_lines += 1
                    else:
                        row_data.append(list(row))  # inorder to modify values in the transform, it must be a list
                        count += 1
                    if count % 5000 == 0:  # write every 5000 rows to the database
                        processed_date = cls._transform(row_data)
                        cls._load(database_cursor, processed_date)
                        row_data = []
                if row_data:  # ensure if there are any leftover rows are written to the database
                    processed_date = cls._transform(row_data)
                    cls._load(database_cursor, processed_date)
            print("Completed file: %s, %s lines ingested, %s bad lines ignored" % (file, count, bad_lines))

    @classmethod
    def _transform(cls, rows):
        pass

    @classmethod
    def _load(cls, database_cursor, rows):
        database_cursor.executemany(cls._insert_statement, rows)

