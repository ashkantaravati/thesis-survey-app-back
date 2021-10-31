import pingouin as pg
import pandas as pd

ICC_RELIABILITY_THRESHOLD = 0.5
DECIMAL_PLACES = 2


def create_data_frame_for_icc(records: "list[tuple[str,str,float]]") -> pd.DataFrame:
    if records:
        df = pd.DataFrame(
            records, columns=["Rater", "Ratee", "Score"], dtype=float
        ).round(DECIMAL_PLACES)
        return df
    return pd.DataFrame()


def check_interrater_reliability_with_icc(df: pd.DataFrame) -> "tuple[bool, float]":
    if not df.empty and len(df) > 8:
        icc_results = pg.intraclass_corr(
            df, targets="Ratee", raters="Rater", ratings="Score"
        ).round(DECIMAL_PLACES)
        icc3_value: float = icc_results.ICC[2]
        is_valid = True if icc3_value > ICC_RELIABILITY_THRESHOLD else False
        return is_valid, icc3_value
    return False, 0.0
