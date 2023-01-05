from django.shortcuts import render
from .models import Polls
from poll_answer import models
# Create your views here.
def list_polls(request):
    polls = Polls.objects.all().order_by("-id")
    return render(request, "polls/polls.html", context={
        "polls": polls
    })
    
def poll(request, id):
    poll = Polls.objects.filter(id=id).first()

    TOTAL_VOTOS = 0

    TOTAL_VOTOS = models.Answers_poll.objects.filter(poll=poll).count()

    options = []

    for option in poll.options.all():
        votos_questao = models.Answers_poll.objects.filter(poll=poll, answers=option).count()
        options.append({
            "option": option,
            "per_votos": (100 * votos_questao) / TOTAL_VOTOS
        })

    return render(request, "polls/poll.html", context={
        "poll": poll,
        "poll_id": id,
        "options": options
    })