import mysql.connector
from mysql.connector import errorcode
from database.database_mappings import column_mapping

DB_NAME = 'data_analysis'

TABLES = {'ccl': (  # Candidate-committee linkages - contains one record for each candidate to committee linkage.
    'candidate_committee_bridging',
    "CREATE TABLE IF NOT EXISTS `candidate_committee_bridging` ("
    "  `candidate_id` varchar(9) NOT NULL,"
    "  `candidate_election_year` SMALLINT NOT NULL,"
    "  `FEC_election_year` SMALLINT NOT NULL,"
    "  `committee_id` varchar(9),"
    "  `committee_type` varchar(4) NOT NULL,"
    "  `committee_designation` ENUM('Authorized by a candidate', 'Lobbyist/Registrant PAC', 'Leadership PAC', "
    "'Joint fundraiser', 'Principal campaign committee of a candidate', 'Unauthorized'),"
    "  `linkage_id` BIGINT NOT NULL"
    ") ENGINE=InnoDB"),
    'cn': (  # Candidate Master - contains one record for each candidate who has either registered with the
        # Federal Election Commission or appeared on a ballot list prepared by a state election's office.
        'candidate',
        "CREATE TABLE IF NOT EXISTS `candidate` ("
        "  `candidate_id` varchar(9) NOT NULL,"
        "  `candidate_name` varchar(200),"
        "  `candidate_party_affiliation` varchar(3),"
        "  `candidate_election_year` smallint,"
        "  `candidate_office_state` varchar(2),"
        "  `candidate_office` ENUM('House', 'President', 'Senate'),"  # enums expanded from H, P, S
        "  `candidate_office_district` varchar(2),"
        "  `incumbent_challenger_status` ENUM('Challenger', 'Incumbent', 'Open Seat'),"  # enums expanded from C, I, O
        "  `candidate_status` ENUM('statutory candidate', 'statutory candidate for future election', "
        "'not yet a statutory candidate', 'statutory candidate in prior cycle'),"
        # enums expaned from 
        # C - statutory candidate, 
        # F - statutory candidate for future election, 
        # N - not yet a statutory candidate, 
        # P - statutory candidate in prior cycle
        "  `candidate_principal_campaign_committee` varchar(9),"
        "  `candidate_street1` varchar(34),"
        "  `candidate_street2` varchar(34),"
        "  `candidate_city` varchar(30),"
        "  `candidate_state` varchar(2),"
        "  `candidate_zip` varchar(9),"
        "  PRIMARY KEY (`candidate_id`)"
        ") ENGINE=InnoDB"), 'itcont': (  # Contributions by individuals - This file gives overall receipts and
        # disbursements for each PAC and party committee registered with the commission, along with a breakdown of overall
        # receipts by source and totals for contributions to other committees, independent expenditures made and other
        # information.
        'individual_contributions',
        "CREATE TABLE IF NOT EXISTS `individual_contributions` ("
        "  `committee_id` varchar(9) NOT NULL,"
        "  `amendment_ind` ENUM('new report', 'amendment to report', 'termination of report'),"  # ENUM amendment_mappings
        "  `report_type` ENUM('Pre-convention', 'Pre-general', 'Pre-primary', 'Pre-Runoff', 'Pre-special', "
        "'Post-Election', 'Post-general', 'Post-primary', 'Post-runoff', 'Post-special', 'Post-convention', "
        "'Comprehensive adjusted amendment', 'Comprehensive amendment', 'October monthly', 'November monthly', "
        "'December monthly', 'February monthly', 'March monthly', 'April monthly', 'May monthly', 'June monthly', "
        "'July monthly', 'August monthly', 'September monthly', 'Mid-year', 'April quarterly', 'July quarterly', "
        "'October quarterly', 'Termination', 'Year end', 'Post inaugural supplement', 'Post inaugural', '48-hour', "
        "'24-hour'),"  # ENUM report_type_mappings
        "  `primary_general_indicator` varchar(5),"  # ENUM election_type_mappings - separated from TRANSACTION_PGI
        "  `primary_general_year` SMALLINT,"  # separated from TRANSACTION_PGI
        "  `IMAGE_NUM` varchar(18),"
        "  `transaction_type` varchar(3),"
        "  `entity_type` ENUM('Candidate', 'Candidate Committee', 'Committee', 'Individual', 'Organization', "
        "'Political Action Committee', 'Party Organization'),"  # ENUM entity_type_mappings
        "  `NAME` varchar(200),"
        "  `CITY` varchar(30),"
        "  `STATE` varchar(2),"
        "  `ZIP_CODE` varchar(9),"
        "  `EMPLOYER` varchar(38),"
        "  `OCCUPATION` varchar(38),"
        "  `transaction_date` varchar(8),"
        "  `transaction_amount` DECIMAL(14,2),"
        "  `OTHER_ID` varchar(9) NOT NULL,"  # For contributions from individuals this column is null. For contributions 
        # from candidates or other committees this column will contain that contributor's FEC ID.
        "  `transaction_id` varchar(32),"
        "  `report_id` varchar(22),"
        "  `memo_code` varchar(1),"
        "  `MEMO_TEXT` varchar(100),"
        "  `FEC_record_id` varchar(19) NOT NULL,"
        "  PRIMARY KEY (`FEC_record_id`)"
        ") ENGINE=InnoDB"),
    'itoth': (  # Any transaction from one committee to another - itemized records (miscellaneous transactions)
        # file contains all transactions (contributions, transfers, etc. among federal committees). It contains all data
        # in the itemized committee contributions file plus PAC contributions to party committees, party transfers from
        # state committee to state committee, and party transfers from national committee to state committee. This file
        # only includes federal transfers not soft money transactions.
        'committee_to_committee_contributions',
        "CREATE TABLE IF NOT EXISTS `committee_to_committee_contributions` ("
        "  `committee_id` varchar(9) NOT NULL,"
        "  `amendment_ind` ENUM('new report', 'amendment to report', 'termination of report'),"  # ENUM amendment_mappings
        "  `report_type` ENUM('Pre-convention', 'Pre-general', 'Pre-primary', 'Pre-Runoff', 'Pre-special', "
        "'Post-Election', 'Post-general', 'Post-primary', 'Post-runoff', 'Post-special', 'Post-convention', "
        "'Comprehensive adjusted amendment', 'Comprehensive amendment', 'October monthly', 'November monthly', "
        "'December monthly', 'February monthly', 'March monthly', 'April monthly', 'May monthly', 'June monthly', "
        "'July monthly', 'August monthly', 'September monthly', 'Mid-year', 'April quarterly', 'July quarterly', "
        "'October quarterly', 'Termination', 'Year end', 'Post inaugural supplement', 'Post inaugural', '48-hour', "
        "'24-hour'),"  # ENUM report_type_mappings
        "  `primary_general_indicator` varchar(5),"  # ENUM election_type_mappings - separated from TRANSACTION_PGI
        "  `primary_general_year` SMALLINT,"  # separated from TRANSACTION_PGI
        "  `IMAGE_NUM` varchar(18),"
        "  `transaction_type` varchar(3),"
        "  `entity_type` ENUM('Candidate', 'Candidate Committee', 'Committee', 'Individual', 'Organization', "
        "'Political Action Committee', 'Party Organization'),"  # ENUM entity_type_mappings
        "  `NAME` varchar(200),"
        "  `CITY` varchar(30),"
        "  `STATE` varchar(2),"
        "  `ZIP_CODE` varchar(9),"
        "  `EMPLOYER` varchar(38),"
        "  `OCCUPATION` varchar(38),"
        "  `transaction_date` varchar(8),"
        "  `transaction_amount` DECIMAL(14,2),"
        "  `OTHER_ID` varchar(9),"  # For contributions from individuals this column is null. For contributions 
        # from candidates or other committees this column will contain that contributor's FEC ID.
        "  `transaction_id` varchar(32),"
        "  `report_id` varchar(22),"
        "  `memo_code` varchar(1),"
        "  `MEMO_TEXT` varchar(100),"
        "  `FEC_record_id` varchar(19) NOT NULL,"
        "  PRIMARY KEY (`FEC_record_id`)"
        ") ENGINE=InnoDB"),
    'itpas2': (  # Contributions from committees to candidates & independent expenditures - itemized committee
        # contributions file contains each contribution or independent expenditure made by a PAC, party committee,
        # candidate committee, or other federal committee to a candidate during the two-year election cycle.
        'committee_contributions',
        "  CREATE TABLE IF NOT EXISTS `committee_contributions` ("
        "  `committee_id` varchar(9) NOT NULL,"
        "  `amendment_ind` ENUM('new report', 'amendment to report', 'termination of report'),"  # ENUM amendment_mappings
        "  `report_type` ENUM('Pre-convention', 'Pre-general', 'Pre-primary', 'Pre-Runoff', 'Pre-special', "
        "'Post-Election', 'Post-general', 'Post-primary', 'Post-runoff', 'Post-special', 'Post-convention', "
        "'Comprehensive adjusted amendment', 'Comprehensive amendment', 'October monthly', 'November monthly', "
        "'December monthly', 'February monthly', 'March monthly', 'April monthly', 'May monthly', 'June monthly', "
        "'July monthly', 'August monthly', 'September monthly', 'Mid-year', 'April quarterly', 'July quarterly', "
        "'October quarterly', 'Termination', 'Year end', 'Post inaugural supplement', 'Post inaugural', '48-hour', "
        "'24-hour'),"  # ENUM report_type_mappings
        "  `primary_general_indicator` varchar(5),"  # ENUM election_type_mappings - separated from TRANSACTION_PGI
        "  `primary_general_year` SMALLINT,"  # separated from TRANSACTION_PGI
        "  `IMAGE_NUM` varchar(18),"
        "  `transaction_type` varchar(3),"
        "  `entity_type` ENUM('Candidate', 'Candidate Committee', 'Committee', 'Individual', 'Organization', "
        "'Political Action Committee', 'Party Organization'),"  # ENUM entity_type_mappings
        "  `NAME` varchar(200),"
        "  `CITY` varchar(30),"
        "  `STATE` varchar(2),"
        "  `ZIP_CODE` varchar(9),"
        "  `EMPLOYER` varchar(38),"
        "  `OCCUPATION` varchar(38),"
        "  `transaction_date` varchar(8),"
        "  `transaction_amount` DECIMAL(14,2),"
        "  `OTHER_ID` varchar(9),"  # For contributions from individuals this column is null. For contributions 
        # from candidates or other committees this column will contain that contributor's FEC ID.
        "  `candidate_id` varchar(9),"
        "  `transaction_id` varchar(32),"
        "  `report_id` varchar(22),"
        "  `memo_code` varchar(1),"
        "  `MEMO_TEXT` varchar(100),"
        "  `FEC_record_id` varchar(19) NOT NULL,"
        "  PRIMARY KEY (`FEC_record_id`)"
        ") ENGINE=InnoDB")}


def create_database(connection, cursor):
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as error:
        print("Database {} does not exists.".format(DB_NAME))
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            try:
                cursor.execute(
                    "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
            except mysql.connector.Error as error:
                print("Failed creating database: {}".format(error))
                exit(1)
            print("Database {} created successfully.".format(DB_NAME))
            connection.database = DB_NAME
        else:
            print(error)
            exit(1)


def create_tables(cursor):
    for table_short_name in TABLES:
        table_tuple = TABLES[table_short_name]
        try:
            print("Creating table {}: ".format(table_tuple[0]), end='')
            cursor.execute(table_tuple[1])
        except mysql.connector.Error as error:
            print(error.msg)
        else:
            print('ok')


def translate_columns(column_name):
    if column_name in column_mapping:
        return column_mapping.get(column_name)
    else:
        return column_name
