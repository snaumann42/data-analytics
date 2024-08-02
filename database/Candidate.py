from tortoise import fields
from tortoise.models import Model
from database.database_mappings import CandidateOffice, IncumbentChallengerStatus, CandidateStatus


# Candidate Master - contains one record for each candidate who has either registered with the
# Federal Election Commission or appeared on a ballot list prepared by a state election's office.
class Candidate(Model):
    candidate_id = fields.CharField(max_length=9, primary_key=True)
    candidate_name = fields.CharField(max_length=200, null=True)
    candidate_party_affiliation = fields.CharField(max_length=3, null=True)
    candidate_election_year = fields.SmallIntField()
    candidate_office_state = fields.CharField(max_length=2, null=True)
    candidate_office = fields.CharEnumField(
        enum_type=CandidateOffice,
        null=True,
        max_length=9
    )
    candidate_office_district = fields.CharField(max_length=2, null=True)
    incumbent_challenger_status = fields.CharEnumField(
        enum_type=IncumbentChallengerStatus,
        null=True,
        max_length=10
    )
    candidate_status = fields.CharEnumField(
        enum_type=CandidateStatus,
        null=True,
        max_length=39
    )
    candidate_principal_campaign_committee = fields.CharField(max_length=9, null=True)
    candidate_street1 = fields.CharField(max_length=34, null=True)
    candidate_street2 = fields.CharField(max_length=34, null=True)
    candidate_city = fields.CharField(max_length=30, null=True)
    candidate_state = fields.CharField(max_length=2, null=True)
    candidate_zip = fields.CharField(max_length=9, null=True)