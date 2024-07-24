from ingests.ingest import Ingest
from database import database_mappings


class IngestCandidateMasterCN(Ingest):

    ingest_file_format = "cn.txt"
    destination_table = "candidate"
    destination_columns = ('candidate_id', 'candidate_name', 'candidate_party_affiliation', 'candidate_election_year',
                           'candidate_office_state', 'candidate_office', 'candidate_office_district',
                           'incumbent_challenger_status', 'candidate_status', 'candidate_principal_campaign_committee',
                           'candidate_street1', 'candidate_street2', 'candidate_city', 'candidate_state',
                           'candidate_zip')

    _candidate_office_index = destination_columns.index('candidate_office')
    _incumbent_challenger_status_index = destination_columns.index('incumbent_challenger_status')
    _candidate_status_index = destination_columns.index('candidate_status')

    # This will result in "INSERT INTO table_name (column1, column2...) VALUES (%s, %s...)" using
    # the overridden class variables
    _insert_statement = """INSERT INTO candidate (candidate_id, candidate_name, candidate_party_affiliation,
     candidate_election_year, candidate_office_state, candidate_office, candidate_office_district,
      incumbent_challenger_status, candidate_status, candidate_principal_campaign_committee, candidate_street1,
       candidate_street2, candidate_city, candidate_state, candidate_zip) VALUES 
       (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    @classmethod
    def _transform(cls, rows):
        for row in rows:
            row[cls._candidate_office_index] = (
                database_mappings.candidate_office_map[
                    row[cls._candidate_office_index]])
            row[cls._incumbent_challenger_status_index] = (
                database_mappings.incumbent_challenger_status_map[
                    row[cls._incumbent_challenger_status_index]])
            row[cls._candidate_status_index] = (
                database_mappings.candidate_status_map[
                    row[cls._candidate_status_index]])

        return [tuple(row) for row in rows]  # inorder to use row to format the query string, it must be a tuple
