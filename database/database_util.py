from tortoise import Tortoise
import urllib.parse

import config

DB_NAME = "data_analysis"


async def db_init():
    await Tortoise.init(
        db_url=f"""mysql://{config.USERNAME}:{urllib.parse.quote_plus(config.PASSWORD)}@{config.HOST}:{config.PORT}/{DB_NAME}""",
        modules={"models": ['database.__init__']}
    )

    await Tortoise.generate_schemas()



    #
    #      "itcont ": (  # Contributions by individuals - This file gives overall receipts and
    #     # disbursements for each PAC and party committee registered with the commission, along with a breakdown of overall
    #     # receipts by source and totals for contributions to other committees, independent expenditures made and other
    #     # information.
    #      "individual_contributions ",
    #     "CREATE TABLE IF NOT EXISTS `individual_contributions` ("
    #     "  `committee_id` varchar(9) NOT NULL,"
    #     "  `amendment_ind` ENUM( "new report ",  "amendment to report ",  "termination of report "),"  # ENUM amendment_mappings
    #     "  `report_type` ENUM( "Pre-convention ",  "Pre-general ",  "Pre-primary ",  "Pre-Runoff ",  "Pre-special ", "
    #     " "Post-Election ",  "Post-general ",  "Post-primary ",  "Post-runoff ",  "Post-special ",  "Post-convention ", "
    #     " "Comprehensive adjusted amendment ",  "Comprehensive amendment ",  "October monthly ",  "November monthly ", "
    #     " "December monthly ",  "February monthly ",  "March monthly ",  "April monthly ",  "May monthly ",  "June monthly ", "
    #     " "July monthly ",  "August monthly ",  "September monthly ",  "Mid-year ",  "April quarterly ",  "July quarterly ", "
    #     " "October quarterly ",  "Termination ",  "Year end ",  "Post inaugural supplement ",  "Post inaugural ",  "48-hour ", "
    #     " "24-hour "),"  # ENUM report_type_mappings
    #     "  `primary_general_indicator` varchar(5),"  # ENUM election_type_mappings - separated from TRANSACTION_PGI
    #     "  `primary_general_year` SMALLINT,"  # separated from TRANSACTION_PGI
    #     "  `IMAGE_NUM` varchar(18),"
    #     "  `transaction_type` varchar(3),"
    #     "  `entity_type` ENUM( "Candidate ",  "Candidate Committee ",  "Committee ",  "Individual ",  "Organization ", "
    #     " "Political Action Committee ",  "Party Organization "),"  # ENUM entity_type_mappings
    #     "  `NAME` varchar(200),"
    #     "  `CITY` varchar(30),"
    #     "  `STATE` varchar(2),"
    #     "  `ZIP_CODE` varchar(9),"
    #     "  `EMPLOYER` varchar(38),"
    #     "  `OCCUPATION` varchar(38),"
    #     "  `transaction_date` varchar(8),"
    #     "  `transaction_amount` DECIMAL(14,2),"
    #     "  `OTHER_ID` varchar(9) NOT NULL,"  # For contributions from individuals this column is null. For contributions
    #     # from candidates or other committees this column will contain that contributor "s FEC ID.
    #     "  `transaction_id` varchar(32),"
    #     "  `report_id` varchar(22),"
    #     "  `memo_code` varchar(1),"
    #     "  `MEMO_TEXT` varchar(100),"
    #     "  `FEC_record_id` varchar(19) NOT NULL,"
    #     "  PRIMARY KEY (`FEC_record_id`)"
    #     ") ENGINE=InnoDB"),
    #  "itoth ": (  # Any transaction from one committee to another - itemized records (miscellaneous transactions)
    #     # file contains all transactions (contributions, transfers, etc. among federal committees). It contains all data
    #     # in the itemized committee contributions file plus PAC contributions to party committees, party transfers from
    #     # state committee to state committee, and party transfers from national committee to state committee. This file
    #     # only includes federal transfers not soft money transactions.
    #      "committee_to_committee_contributions ",
    #     "CREATE TABLE IF NOT EXISTS `committee_to_committee_contributions` ("
    #     "  `committee_id` varchar(9) NOT NULL,"
    #     "  `amendment_ind` ENUM( "new report ",  "amendment to report ",  "termination of report "),"  # ENUM amendment_mappings
    #     "  `report_type` ENUM( "Pre-convention ",  "Pre-general ",  "Pre-primary ",  "Pre-Runoff ",  "Pre-special ", "
    #     " "Post-Election ",  "Post-general ",  "Post-primary ",  "Post-runoff ",  "Post-special ",  "Post-convention ", "
    #     " "Comprehensive adjusted amendment ",  "Comprehensive amendment ",  "October monthly ",  "November monthly ", "
    #     " "December monthly ",  "February monthly ",  "March monthly ",  "April monthly ",  "May monthly ",  "June monthly ", "
    #     " "July monthly ",  "August monthly ",  "September monthly ",  "Mid-year ",  "April quarterly ",  "July quarterly ", "
    #     " "October quarterly ",  "Termination ",  "Year end ",  "Post inaugural supplement ",  "Post inaugural ",  "48-hour ", "
    #     " "24-hour "),"  # ENUM report_type_mappings
    #     "  `primary_general_indicator` varchar(5),"  # ENUM election_type_mappings - separated from TRANSACTION_PGI
    #     "  `primary_general_year` SMALLINT,"  # separated from TRANSACTION_PGI
    #     "  `IMAGE_NUM` varchar(18),"
    #     "  `transaction_type` varchar(3),"
    #     "  `entity_type` ENUM( "Candidate ",  "Candidate Committee ",  "Committee ",  "Individual ",  "Organization ", "
    #     " "Political Action Committee ",  "Party Organization "),"  # ENUM entity_type_mappings
    #     "  `NAME` varchar(200),"
    #     "  `CITY` varchar(30),"
    #     "  `STATE` varchar(2),"
    #     "  `ZIP_CODE` varchar(9),"
    #     "  `EMPLOYER` varchar(38),"
    #     "  `OCCUPATION` varchar(38),"
    #     "  `transaction_date` varchar(8),"
    #     "  `transaction_amount` DECIMAL(14,2),"
    #     "  `OTHER_ID` varchar(9),"  # For contributions from individuals this column is null. For contributions
    #     # from candidates or other committees this column will contain that contributor "s FEC ID.
    #     "  `transaction_id` varchar(32),"
    #     "  `report_id` varchar(22),"
    #     "  `memo_code` varchar(1),"
    #     "  `MEMO_TEXT` varchar(100),"
    #     "  `FEC_record_id` varchar(19) NOT NULL,"
    #     "  PRIMARY KEY (`FEC_record_id`)"
    #     ") ENGINE=InnoDB"),
    #  "itpas2 ": (  # Contributions from committees to candidates & independent expenditures - itemized committee
    #     # contributions file contains each contribution or independent expenditure made by a PAC, party committee,
    #     # candidate committee, or other federal committee to a candidate during the two-year election cycle.
    #      "committee_contributions ",
    #     "  CREATE TABLE IF NOT EXISTS `committee_contributions` ("
    #     "  `committee_id` varchar(9) NOT NULL,"
    #     "  `amendment_ind` ENUM( "new report ",  "amendment to report ",  "termination of report "),"  # ENUM amendment_mappings
    #     "  `report_type` ENUM( "Pre-convention ",  "Pre-general ",  "Pre-primary ",  "Pre-Runoff ",  "Pre-special ", "
    #     " "Post-Election ",  "Post-general ",  "Post-primary ",  "Post-runoff ",  "Post-special ",  "Post-convention ", "
    #     " "Comprehensive adjusted amendment ",  "Comprehensive amendment ",  "October monthly ",  "November monthly ", "
    #     " "December monthly ",  "February monthly ",  "March monthly ",  "April monthly ",  "May monthly ",  "June monthly ", "
    #     " "July monthly ",  "August monthly ",  "September monthly ",  "Mid-year ",  "April quarterly ",  "July quarterly ", "
    #     " "October quarterly ",  "Termination ",  "Year end ",  "Post inaugural supplement ",  "Post inaugural ",  "48-hour ", "
    #     " "24-hour "),"  # ENUM report_type_mappings
    #     "  `primary_general_indicator` varchar(5),"  # ENUM election_type_mappings - separated from TRANSACTION_PGI
    #     "  `primary_general_year` SMALLINT,"  # separated from TRANSACTION_PGI
    #     "  `IMAGE_NUM` varchar(18),"
    #     "  `transaction_type` varchar(3),"
    #     "  `entity_type` ENUM( "Candidate ",  "Candidate Committee ",  "Committee ",  "Individual ",  "Organization ", "
    #     " "Political Action Committee ",  "Party Organization "),"  # ENUM entity_type_mappings
    #     "  `NAME` varchar(200),"
    #     "  `CITY` varchar(30),"
    #     "  `STATE` varchar(2),"
    #     "  `ZIP_CODE` varchar(9),"
    #     "  `EMPLOYER` varchar(38),"
    #     "  `OCCUPATION` varchar(38),"
    #     "  `transaction_date` varchar(8),"
    #     "  `transaction_amount` DECIMAL(14,2),"
    #     "  `OTHER_ID` varchar(9),"  # For contributions from individuals this column is null. For contributions
    #     # from candidates or other committees this column will contain that contributor "s FEC ID.
    #     "  `candidate_id` varchar(9),"
    #     "  `transaction_id` varchar(32),"
    #     "  `report_id` varchar(22),"
    #     "  `memo_code` varchar(1),"
    #     "  `MEMO_TEXT` varchar(100),"
    #     "  `FEC_record_id` varchar(19) NOT NULL,"
    #     "  PRIMARY KEY (`FEC_record_id`)"
    #     ") ENGINE=InnoDB")}


# def create_database(connection, cursor):
#     try:
#         cursor.execute("USE {}".format(DB_NAME))
#     except mysql.connector.Error as error:
#         print("Database {} does not exists.".format(DB_NAME))
#         if error.errno == errorcode.ER_BAD_DB_ERROR:
#             try:
#                 cursor.execute(
#                     "CREATE DATABASE {} DEFAULT CHARACTER SET  "utf8 "".format(DB_NAME))
#             except mysql.connector.Error as error:
#                 print("Failed creating database: {}".format(error))
#                 exit(1)
#             print("Database {} created successfully.".format(DB_NAME))
#             connection.database = DB_NAME
#         else:
#             print(error)
#             exit(1)
#
#
# def create_tables(cursor):
#     for table_short_name in TABLES:
#         table_tuple = TABLES[table_short_name]
#         try:
#             print("Creating table {}: ".format(table_tuple[0]), end= " ")
#             cursor.execute(table_tuple[1])
#         except mysql.connector.Error as error:
#             print(error.msg)
#         else:
#             print( "ok ")
