ERROR_FLAG = "LOW ICC"
MIN_REQUIRED_RESPONSE_RATE = 0.5

SEX_CHOICES = [("male", "آقا"), ("female", "خانم")]
OVERCONFIDENCE_QUIZ_OUTCOME_CHOICES = [
    (-1, "Too Broad: Underconfident"),
    (0, "OK"),
    (1, "Miss: Overconfident"),
]

OVERCONFIDENCE_QUIZ_ACCEPTABLE_RANGE = {
    1: (28, 33),
    2: (2005, 2010),
    3: (40, 50),
    4: (1995, 2005),
    5: (20, 26),
    6: (1985, 1995),
    7: (1990, 2000),
    8: (30, 34),
    9: (800, 1000),
    10: (45, 60),
}

OVERCONFIDENCE_SCORE = 1.0
UNDERCONFIDENCE_SCORE = 0.0
CORRECT_ANSWER_SCORE = 0.0

OVERCONFIDENCE_QUIZ_CORRECT_ANSWERS = {
    1: 31,
    2: 2007,  # 1386-7
    3: 44,
    4: 2000,  # 1380
    5: 23,
    6: 1368,  # 1368
    7: 1993,  # (1993~1998 | 1371~1377)
    8: 32,
    9: 900,  # 899~926
    10: 50,
}

ICC_RELIABILITY_THRESHOLD = 0.5
DECIMAL_PLACES = 2
ICC_TARGET_INDEX_MAP = {
    "ICC1": 0,
    "ICC2": 1,
    "ICC3": 2,
    "ICC1K": 3,
    "ICC2K": 4,
    "ICC3K": 5,
}
