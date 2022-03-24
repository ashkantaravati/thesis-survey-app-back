from tabnanny import verbose
from weakref import proxy

from main.calculations import determine_overconfidence_score
from .response import Response


class OverconfidenceQuiz(Response):
    @property
    def overconfidence_question_1_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[1]

    @property
    def overconfidence_question_2_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[2]

    @property
    def overconfidence_question_3_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[3]

    @property
    def overconfidence_question_4_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[4]

    @property
    def overconfidence_question_5_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[5]

    @property
    def overconfidence_question_6_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[6]

    @property
    def overconfidence_question_7_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[7]

    @property
    def overconfidence_question_8_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[8]

    @property
    def overconfidence_question_9_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[9]

    @property
    def overconfidence_question_10_outcome(self):
        scores = self.get_overconfidence_outcomes(as_dict=True)
        return scores[10]

    class Meta:
        proxy = True
        verbose_name = "Overconfidence Quiz"
        verbose_name_plural = "Overconfidence Quizzes"
