from django.test import TestCase
from parameterized import parameterized

from main.constants import (
    CORRECT_ANSWER_STATUS_INDICATOR,
    OVERCONFIDENT_STATUS_INDICATOR,
    UNDERCONFIDENT_STATUS_INDICATOR,
)
from .calculations import (
    check_interrater_reliability_with_icc,
    create_data_frame_for_icc,
    determine_overconfidence_score,
)


class TestStatisticalCalculations(TestCase):
    def test_icc_score(self):
        test_records = [
            ("A", "1", 1),
            ("A", "2", 1),
            ("A", "3", 3),
            ("A", "4", 6),
            ("A", "5", 6),
            ("A", "6", 7),
            ("A", "7", 8),
            ("A", "8", 9),
            ("B", "1", 2),
            ("B", "2", 3),
            ("B", "3", 8),
            ("B", "4", 4),
            ("B", "5", 5),
            ("B", "6", 5),
            ("B", "7", 7),
            ("B", "8", 9),
            ("C", "1", 0),
            ("C", "2", 3),
            ("C", "3", 1),
            ("C", "4", 3),
            ("C", "5", 5),
            ("C", "6", 6),
            ("C", "7", 7),
            ("C", "8", 9),
            ("D", "1", 1),
            ("D", "2", 2),
            ("D", "3", 4),  # asdasdad
            ("D", "4", 3),
            ("D", "5", 6),
            ("D", "6", 2),
            ("D", "7", 9),
            ("D", "8", 8),
        ]
        df = create_data_frame_for_icc(test_records)
        is_valid, icc_value = check_interrater_reliability_with_icc(df, "ICC1")
        self.assertAlmostEqual(icc_value, 0.728)


class TestOverconfidenceCalculations(TestCase):
    @parameterized.expand(
        [
            (
                "Overconfident due to higher range",
                40,
                (38, 42),
                (41, 70),
                OVERCONFIDENT_STATUS_INDICATOR,
            ),
            (
                "Overconfident due to lower range",
                40,
                (38, 42),
                (20, 39),
                OVERCONFIDENT_STATUS_INDICATOR,
            ),
            (
                "OK covering higher side of accepted range",
                40,
                (38, 42),
                (40, 42),
                CORRECT_ANSWER_STATUS_INDICATOR,
            ),
            (
                "OK covering lower side of accepted range",
                40,
                (38, 42),
                (38, 40),
                CORRECT_ANSWER_STATUS_INDICATOR,
            ),
            (
                "Underconfident overflowing from lower side of accepted range",
                40,
                (38, 42),
                (30, 42),
                UNDERCONFIDENT_STATUS_INDICATOR,
            ),
            (
                "Underconfident overflowing from higher side of accepted range",
                40,
                (38, 42),
                (38, 45),
                UNDERCONFIDENT_STATUS_INDICATOR,
            ),
            (
                "Underconfident overflowing from both sides of accepted range",
                40,
                (38, 42),
                (35, 45),
                UNDERCONFIDENT_STATUS_INDICATOR,
            ),
        ]
    )
    def test_overconfidence_score_determination(
        self, name, correct_answer, accepted_range, given_range, expected_outcome
    ):
        score, outcome = determine_overconfidence_score(
            given_range, accepted_range, correct_answer
        )
        self.assertEqual(outcome, expected_outcome)
