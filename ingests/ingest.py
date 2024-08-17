import os
import re


class Ingest:
    """A class to define the basic functionality of our ingests."""

    base_ingest_path = './data-files/'
    ingest_file_format = ''
    number_of_columns = 0
    destination_table = ''
    model = None

    # This will result in "INSERT INTO table_name (column1, column2...) VALUES
    # (%s, %s...)" using the overridden class variables
    _insert_statement = ''

    @classmethod
    async def evaluate(cls, database_conn):
        base_path = cls.base_ingest_path
        ingest_files = filter(lambda f: os.path.isfile(base_path + f)
                              and re.search(cls.ingest_file_format, f),
                              os.listdir(base_path))

        for file in ingest_files:
            print("processing file: " + file)
            with open(base_path + file) as file_handle:
                count = 0
                row_data = []
                for line in file_handle:
                    row = line.rstrip('\n').split("|")
                    # inorder to modify values in the transform, it must be a
                    # list
                    row_data.append(list(row))
                    count += 1
                    # write every 5000 rows to the database
                    if count % 5000 == 0:
                        processed_date = cls._transform(row_data)
                        await cls._load(database_conn, processed_date)
                        row_data = []
                # ensure if there are any leftover rows are written to the
                # database
                if row_data:
                    processed_date = cls._transform(row_data)
                    await cls._load(database_conn, processed_date)
            print("Completed file: %s, %s lines ingested" % (file, count))

    @classmethod
    def _transform(cls, rows):
        pass

    @classmethod
    async def _load(cls, database_conn, rows):
        cls.model.bulk_create(rows)
