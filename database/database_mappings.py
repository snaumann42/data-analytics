from enum import Enum


table_name_map = {
        'ccl': 'candidate_committee_bridging',
        'cn': 'candidate',
        'itoth': 'committee_to_committee_contributions',
        'itpas2': 'committee_contributions',
        'ORG': 'Organization',
        'PAC': 'Political Action Committee',
        'PTY': 'Party Organization'
    }


class CandidateOffice(Enum):
    H = "House"
    P = "President"
    S = "Senate"


class CommitteeDesignation(Enum):
    A = "Authorized by candidate"
    B = "Lobbyist Registrant PAC"
    D = "Leadership PAC"
    J = "Joint fundraiser"
    P = "Principal campaign committee of candidate"
    U = "Unauthorized"


class IncumbentChallengerStatus(Enum):
    C = "Challenger"
    I = "Incumbent"
    O = "Open Seat"


class CandidateStatus(Enum):
    C = "statutory candidate"
    F = "statutory candidate for future election"
    N = "not yet a statutory candidate"
    P = "statutory candidate in prior cycle"

#
# committee_type_map = {
#         'C': 'communication cost',  # Organizations like corporations or
# unions may prepare communications for their employees or members that
# advocate the election of specific candidates and they must disclose them
# under certain circumstances. These are usually paid with direct corporate or
# union funds rather than from PACs.
#         'D': 'delegate committee',  # Delegate committees are organized for
# the purpose of influencing the selection of delegates to Presidential
# nominating conventions. The term includes a group of delegates, a group of
#         # individuals seeking to become delegates, and a group of in
#         'E': 'electioneering communication',  # Groups (other than PACs)
# making electioneering communications
#         'H': 'house',  # Campaign committees for candidates for the U.S.
# House of Representatives
#         'I': 'independent expenditor',  # Individuals or groups (other than
# PACs) making independent expenditures
#         # over $250 in a year must disclose those expenditures
#         'N': 'PAC - nonqualified',  # PACs that have not yet been in
# existence for six months and received contributions
#         # from 50 people and made contributions to five federal candidates.
# These committees have lower limits for their
#         # contributions to candidates.
#         'O': 'independent expenditure-only (Super PACs)',  # Political
# Committee that has filed a statement consistent
#         # with AO 2010-09 or AO 2010-11.
#         'P': 'presidential',  # Campaign committee for candidate for U.S.
# President
#         'Q': 'PAC - qualified',  # PACs that have been in existence for six
# months and received contributions from 50
#         # people and made contributions to five federal candidates
#         'S': 'senate',  # Campaign committee for candidate for Senate
#         'U': 'single-candidate independent expenditure',
#         'V': 'Hybrid PAC (with Non-Contribution Account) - Nonqualified',
#         # https://www.fec.gov/help-candidates-and-committees/registering-pac/
# bank-accounts-nonconnected-pacs/
#         'W': 'Hybrid PAC (with Non-Contribution Account) - Qualified',
#         # https://www.fec.gov/help-candidates-and-committees/registering-pac/
# bank-accounts-nonconnected-pacs/
#         'X': 'Party - nonqualified',  # Party committees that have not yet
# been in existence for six months and received
#         # contributions from 50 people, unless they are affiliated with
# another party committee that has met these
#         # requirements.
#         'Y': 'Party - qualified',  # Party committees that have existed for
# at least six months and received
#         # contributions from 50 people or are affiliated with another party
# committee that meets these requirements.
#         'Z': 'national party nonfederal account',  # National party
# nonfederal accounts. Not permitted after enactment
#         # of Bipartisan Campaign Reform Act of 2002.
#         '': None
#     }
#
#
# election_type_map = {
#         'P': 'Primary',
#         'G': 'General',
#         'O': 'Other',
#         'C': 'Convention',
#         'R': 'Runoff',
#         'S': 'Special',
#         'E': 'Recount',
#         '': None
#     }
#
# amendment_ind_map = {
#         'N': 'new report',
#         'A': 'amendment to report',
#         'T': 'termination of report',
#         '': None
#     }
#
# report_type_map = {
#         '12C': 'Pre-convention',
#         '12G': 'Pre-general',
#         '12P': 'Pre-primary',
#         '12R': 'Pre-Runoff',
#         '12S': 'Pre-special',
#         '30D': 'Post-Election',
#         '30G': 'Post-general',
#         '30P': 'Post-primary',
#         '30R': 'Post-runoff',
#         '30S': 'Post-special',
#         '60D': 'Post-convention',
#         'ADJ': 'Comprehensive adjusted amendment',
#         'CA': 'Comprehensive amendment',
#         'M10': 'October monthly',
#         'M11': 'November monthly',
#         'M12': 'December monthly',
#         'M2': 'February monthly',
#         'M3': 'March monthly',
#         'M4': 'April monthly',
#         'M5': 'May monthly',
#         'M6': 'June monthly',
#         'M7': 'July monthly',
#         'M8': 'August monthly',
#         'M9': 'September monthly',
#         'MY': 'Mid-year',
#         'Q1': 'April quarterly',
#         'Q2': 'July quarterly',
#         'Q3': 'October quarterly',
#         'TER': 'Termination',
#         'YE': 'Year end',
#         '90S': 'Post inaugural supplement',
#         '90D': 'Post inaugural',
#         '48H': '48-hour',  # Report of specific contribution of $1,000 or
#           more made to a campaign within 20 days of an election.
#           Alternatively, once a PAC or party or other person has made
#           independent expenditures exceeding $10,000 in a race these and
#           future independent expenditures must be reported. Due within 48
#           hours of receiving the contribution or public distribution of the
#           independent expenditure. 48 hour timing for independent
#           expenditures applies prior to 20 days before the election.
#         '24H': '24-hour',  # Within 20 days of an election once a PAC or
#           party or other person has made independent expenditures exceeding
#           $1,000 in a race these and future independent expenditures must be
#           reported. Due within 24 hours of the public distribution of the
#           independent expenditure.
#         '': None
#     }
#
# entity_type_map = {
#         'CAN': 'Candidate',
#         'CCM': 'Candidate Committee',
#         'COM': 'Committee',
#         'IND': 'Individual',
#         'ORG': 'Organization',
#         'PAC': 'Political Action Committee',
#         'PTY': 'Party Organization',
#         '': None
#     }


# keeping for now for documentation of field/column remapping
# column_mapping = {
#     'CAND_ID': 'candidate_id',
#     'CAND_NAME': 'candidate_name',
#     'CAND_PTY_AFFILIATION': 'candidate_party_affiliation',
#     'CAND_ELECTION_YR': 'candidate_election_year',
#     'CAND_OFFICE_ST': 'candidate_office_state',
#     'CAND_OFFICE': 'candidate_office',
#     'CAND_OFFICE_DISTRICT': 'candidate_office_district',
#     'CAND_ICI': 'incumbent_challenger_status',
#     'CAND_STATUS': 'candidate_status',
#     'CAND_PCC': 'candidate_principal_campaign_committee',
#     'CAND_ST1': 'candidate_street1',
#     'CAND_ST2': 'candidate_street2',
#     'CAND_CITY': 'candidate_city',
#     'CAND_ST': 'candidate_state',
#     'CAND_ZIP': 'candidate_zip',
#     'FEC_ELECTION_YR': 'fec_election_year',
#     'CMTE_ID': 'committee_id',
#     'CMTE_TP': 'committee_type',
#     'CMTE_DSGN': 'committee_designation',
#     'LINKAGE_ID': 'linkage_id',
#     'AMNDT_IND': 'amendment_ind',
#     'RPT_TP': 'report_type',
#     'TRANSACTION_PGI': 'primary_general_indicator',
#     'ENTITY_TP': 'entity_type',
#     'TRANSACTION_DT': 'transaction_date',
#     'TRANSACTION_AMT': 'transaction_amount',
#     'TRAN_ID': 'transaction_id',
#     'FILE_NUM': 'report_id',
#     'MEMO_CD': 'memo_code',
#     'SUB_ID': 'FEC_record_id',
#     'TRANSACTION_TP': 'transaction_type',
# }
