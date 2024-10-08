from enum import Enum

class Quarter(Enum):
    
    FRESH_FALL = 0
    FRESH_WINTER = 1
    FRESH_SPRING = 2
    FRESH_SUMMER = 3
    
    SOPH_FALL = 4
    SOPH_WINTER = 5
    SOPH_SPRING = 6
    SOPH_SUMMER = 7
    
    JUNIOR_FALL = 8
    JUNIOR_WINTER = 9
    JUNIOR_SPRING = 10
    JUNIOR_SUMMER = 11
    
    SENIOR_FALL = 12
    SENIOR_WINTER = 13
    SENIOR_SPRING = 14
    SENIOR_SUMMER = 15

class GER(Enum):
    WAY_A_II = "way a-ii"
    WAY_AQR = "way aqr"
    WAY_CE = "way ce"
    WAY_EDP = "way edp"
    WAY_ER = "way er"
    WAY_FR = "way fr"
    WAY_SI = "way si"
    WAY_SMA = "way sma"
    WRITING_1 = "writing 1"
    WRITING_2 = "writing 2"
    SLE = "sle"
    COLLEGE = "college"
    LANGUAGE = "language"


class Grade(Enum):
    A_PLUS = 4.3
    A = 4.0
    A_MINUS = 3.7
    B_PLUS = 3.3
    B = 3.0
    B_MINUS = 2.7
    C_PLUS = 2.3
    C = 2.0
    C_MINUS = 1.7
    D_PLUS = 1.3
    D = 1.0
    D_MINUS = 0.7
    NP = 0.0
    INCOMPLETE = 0.0
    CREDIT = "credit"
    NO_CREDIT = "no credit"

class Grading(Enum):
    LETTER = "letter"
    C_NC = "credit/no credit"
    MIXED = "letter or credit/no credit"