import os
import config
import mysql.connector
from database import database_util

file_path = "./data-files/"

connection = mysql.connector.connect(
    host=config.URL,
    database=database_util.DB_NAME,
    user=config.USERNAME,
    password=config.PASSWORD
)
cursor = connection.cursor()


# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS test (
#         column1 int NOT NULL
#     );
#     """
# )


def main():
    header_files = filter(lambda f: os.path.isfile(file_path + f) and f.endswith(".csv") and f.find("header") != -1, os.listdir(file_path))

    for file in header_files:
        with open(file_path + file) as infile:
            headers = infile.readline().rstrip("\n").split(",")
        translated_headers = tuple(map(lambda h: database_util.translate_columns(h), headers))

        table_short_name = file.split("_")[0]
        num_of_columns = len(headers)
        table_name = database_util.TABLES[table_short_name][0]

        # fancy tuple logic to allow for processing additional files without too much boilerplate
        values_statement = ("%s, " * num_of_columns).rstrip(', ')

        # Create insert statement for file, using fancy tuple logic
        statment = ((("INSERT INTO %s %s values (" % (table_name, translated_headers)) + values_statement + ")")
                    .replace("'", "")
                    .replace("TRANSACTION_PGI,", "election_type, election_year,"))
        print("statment: " + statment)
        count = 0
        bad_lines = 0
        row_data = []
        with open(file_path + table_short_name + ".txt") as data_file:
            for line in data_file:
                row = line.split("|")
                if len(row) != num_of_columns:
                    bad_lines += 1
                else:
                    row_data.append(tuple(row))
                    count += 1
                if count % 5000 == 0:  # write every 5000 rows to the database
                    # translate ENUMs
                    enumerated_row_data = process_enums(row)
                    cursor.executemany(statment, row_data)
                    row_data = []
            if row_data:  # ensure if there are any leftover rows are written to the database
                # translate ENUMs
                cursor.executemany(statment, row_data)
        print("file: %s, lines: %s, bad lines: %s" % (file, count, bad_lines))

# TRANSACTION_PGI -> election_type & yyyy
    # election_type
    # election_year


if __name__ == '__main__':
    # Setup mysql database
    database_util.create_database(connection, cursor)
    database_util.create_tables(cursor)

    # Process files into tables
    main()

    # Close resources
    cursor.close()
    connection.close()
