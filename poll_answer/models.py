from django.db import models
from polls.models import Polls, Options
# Create your models here.
class Answers_poll(models.Model):
    email_user = models.EmailField()
    answers = models.ForeignKey(Options, on_delete=models.CASCADE)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} Respondeu {} na {} ".format(self.email_user, self.answers.option, self.poll.title)