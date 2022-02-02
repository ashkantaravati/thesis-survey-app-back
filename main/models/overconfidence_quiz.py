from tabnanny import verbose
from weakref import proxy
from .response import Response


class OverconfidenceQuiz(Response):
    class Meta:
        proxy = True
        verbose_name = "Overconfidence Quiz"
        verbose_name_plural = "Overconfidence Quizzes"
