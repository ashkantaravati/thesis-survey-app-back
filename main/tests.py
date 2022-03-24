from django.test import TestCase
from .calculations import (
    check_interrater_reliability_with_icc,
    create_data_frame_for_icc,
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
