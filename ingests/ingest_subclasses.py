from ingests.ingest import Ingest
from database import Candidate, database_mappings


def lookup_enum(value, enum):
    try:
        return enum[value].value
    except KeyError:
        return None


class IngestCandidateMasterCN(Ingest):

    ingest_file_format = "cn.txt"
    destination_table = "candidate"
    model = Candidate

    @classmethod
    def _transform(cls, rows):
        return [Candidate(candidate_id=row[0],
                          candidate_name=row[1],
                          candidate_party_affiliation=row[2],
                          candidate_election_year=row[3],
                          candidate_office_state=row[4],
                          candidate_office=database_mappings.
                          CandidateOffice[row[5]],
                          candidate_office_district=row[6],
                          incumbent_challenger_status=database_mappings.
                          IncumbentChallengerStatus[row[7]],
                          candidate_status=database_mappings.
                          CandidateStatus[row[8]],
                          candidate_principal_campaign_committee=row[9],
                          candidate_street1=row[10],
                          candidate_street2=row[11],
                          candidate_city=row[12],
                          candidate_state=row[13],
                          candidate_zip=row[14])
                for row in rows]
