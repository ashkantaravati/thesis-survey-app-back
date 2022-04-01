import pingouin as pg
import pandas as pd
from main.constants import (
    CORRECT_ANSWER_SCORE,
    CORRECT_ANSWER_STATUS_INDICATOR,
    DECIMAL_PLACES,
    ICC_RELIABILITY_THRESHOLD,
    ICC_TARGET_INDEX_MAP,
    OVERCONFIDENCE_SCORE,
    OVERCONFIDENT_STATUS_INDICATOR,
    UNDERCONFIDENCE_SCORE,
    UNDERCONFIDENT_STATUS_INDICATOR,
)

from main.typing import ListOfICCFrameRecord


def create_data_frame_for_icc(records: ListOfICCFrameRecord) -> pd.DataFrame:
    if records:
        df = pd.DataFrame(records, columns=["Rater", "Ratee", "Score"]).round(
            DECIMAL_PLACES
        )
        return df
    return pd.DataFrame()


def check_interrater_reliability_with_icc(
    df: pd.DataFrame, icc_type="ICC1K"
) -> "tuple[bool, float]":
    icc_value_index = ICC_TARGET_INDEX_MAP[icc_type]
    if not df.empty:
        icc_results = pg.intraclass_corr(
            df, targets="Ratee", raters="Rater", ratings="Score"
        ).round(3)
        icc_value: float = icc_results.ICC[icc_value_index]
        is_valid = True if icc_value > ICC_RELIABILITY_THRESHOLD else False
        return is_valid, icc_value
    return False, 0.0


def get_mean_value_of_list(values: "list[float]") -> float:
    if values:
        return round(sum(values) / len(values), DECIMAL_PLACES)
    return 0.0


def round_as_default(value: float) -> float:
    return round(value, DECIMAL_PLACES)


def check_if_value_is_in_range(value: float, range: "tuple[int, int]") -> bool:
    if range:
        min_value, max_value = range
        return min_value <= value <= max_value
    return False


def check_if_range_contains_range(
    range1: "tuple[int, int]", range2: "tuple[int, int]"
) -> bool:
    if range1 and range2:
        min_value1, max_value1 = range1
        min_value2, max_value2 = range2
        return min_value1 <= min_value2 and max_value1 >= max_value2
    return False


def check_if_range_is_wider_than_range(
    range1: "tuple[int, int]", range2: "tuple[int, int]"
) -> bool:
    if range1 and range2:
        min_value1, max_value1 = range1
        min_value2, max_value2 = range2
        return max_value1 - min_value1 > max_value2 - min_value2
    return False


def check_if_range_contains_but_is_not_equal_to_range(
    range1: "tuple[int, int]", range2: "tuple[int, int]"
) -> bool:
    if range1 and range2:
        return check_if_range_contains_range(
            range1, range2
        ) and check_if_range_is_wider_than_range(range1, range2)

    return False


def determine_overconfidence_score(
    min_max_response: "tuple[float, float]",
    reference_range: "tuple[float, float]",
    correct_answer: int,
) -> float:
    includes_correct_answer = check_if_value_is_in_range(
        correct_answer, min_max_response
    )
    if includes_correct_answer:
        is_underconfident = check_if_range_contains_but_is_not_equal_to_range(
            min_max_response, reference_range
        )
        if is_underconfident:
            return (UNDERCONFIDENCE_SCORE, UNDERCONFIDENT_STATUS_INDICATOR)
        return CORRECT_ANSWER_SCORE, CORRECT_ANSWER_STATUS_INDICATOR
    else:  # then it is a miss
        return OVERCONFIDENCE_SCORE, OVERCONFIDENT_STATUS_INDICATOR
