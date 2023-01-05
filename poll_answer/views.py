from django.shortcuts import render
import django.http as http
from django.contrib import messages
from .models import Answers_poll
from polls.models import Options, Polls
# Create your views here.

def save_answer(request: http.HttpRequest, id):
    if request.method != "POST":
        return http.HttpResponseNotAllowed(["GET"])

    data = request.POST

    email = data.get("email")
    answer = data.get("answer")
    poll_id = id
    if email is None:
        messages.add_message(request, messages.ERROR, "O campo e-mail é obrigatório", extra_tags="danger")
    if answer is None:
        messages.add_message(request, messages.ERROR, "É necessário selecionar uma resposta", extra_tags="danger")

    if poll_id is None:
        messages.add_message(request, messages.ERROR, "Enquete é obrigatória", extra_tags="danger")

    if None in [email, answer, poll_id]:
        return http.HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    option_model = Options.objects.filter(id=answer).first()
    if option_model is None:
        messages.add_message(request, messages.ERROR, "Opção id {} não existe".format(answer), extra_tags="danger")
        return http.HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    poll_model = Polls.objects.filter(id=poll_id).first()

    if poll_model is None:
        messages.add_message(request, messages.ERROR, "Enquete id {} não existe".format(poll_id), extra_tags="danger")
        return http.HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    

    new_answer = Answers_poll(
        email_user=email,
        answers= option_model,
        poll=poll_model)
    new_answer.save()
    
    messages.add_message(request, messages.SUCCESS, "Resposta enviada com sucesso", extra_tags="success")

    return http.HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))