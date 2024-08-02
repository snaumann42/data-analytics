from tortoise import fields
from tortoise.models import Model

from database.database_mappings import CommitteeDesignation


# Candidate-committee linkages - contains one record for each candidate to committee linkage.
class CandidateCommitteeBridging(Model):
    candidate_election_year = fields.SmallIntField()
    FEC_election_year = fields.SmallIntField()
    committee_id = fields.CharField(max_length=9, null=True)
    committee_type = fields.CharField(max_length=4, null=True)
    committee_designation = fields.CharEnumField(
        enum_type=CommitteeDesignation,
        null=True,
        max_length=41
    )
    linkage_id = fields.BigIntField()

    candidate_id = fields.ForeignKeyField("models.Candidate", related_name="candidate_id")