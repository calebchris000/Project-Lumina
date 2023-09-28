from enum import Enum


class RELATIONSHIP(Enum):
    MOTHER = "mother"
    FATHER = "father"
    STEPMOTHER = "step_mother"
    STEPFATHER = "step_father"
    LEGAL_GUARDIAN = "legal_guardian"
    GRANDPARENT = "grandparent"
    AUNT = "aunt"
    UNCLE = "uncle"
    COUSIN = "cousin"
    SISTER = "sister"
    BROTHER = "brother"
    FOSTER_PARENT = "foster_parent"
    OTHER_RELATIVE = "other_relative"
    FAMILY_FRIEND = "family_friend"
    UNKNOWN = "unknown"
