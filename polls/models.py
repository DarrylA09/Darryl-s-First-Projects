from django.db import models


class Question(models.Model):
    """
    This class represents a question in the poll application.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        This method returns the question_text field of the Question class.
        """
        return self.question_text


class Choice(models.Model):
    """
    This class represents a choice in the poll application.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        This method returns the choice_text field of the Choice class."""
        return self.choice_text
