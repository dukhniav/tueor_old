# -*- encoding: utf-8 -*-
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Wallet, Transaction
from datetime import date
from django.template.response import TemplateResponse

from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# from .models import Choice, Question


@login_required(login_url="/login/")
def portfolio(request):
    context = {"segment": "portfolio"}
    html_template = loader.get_template("portfolio/index.html")
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def wallets(request):
    template = loader.get_template("portfolio/wallets.html")
    args = {}

    t = date.today()
    latest_question_list = Wallet.objects.all()
    output = ', '.join([q.name for q in latest_question_list])

    args['time'] = t
    args['output'] = output
    args['qs'] = latest_question_list
    # return HttpResponse(html_template.render(context, request))
    return TemplateResponse(request, template, args)
    # template_name = 'portfolio/wallets.html'
    # context_object_name = 'wallet_list'
    #
    # def get_queryset(self):
    #     """
    #     Return list of wallets
    #     """
    #     return Wallet.objects







@login_required(login_url="/login/")
def transactions(request):
    context = {"segment": "transactions"}
    html_template = loader.get_template("portfolio/transactions.html")
    return HttpResponse(html_template.render(context, request))

#
# # --------------------------
#
#
# class IndexView(generic.ListView):
#     template_name = 'portfolio/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Wallet.objects
#
#
# class DetailView(generic.DetailView):
#     model = Wallet
#     template_name = 'portfolio/wallets.html'
#
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Wallet.objects
#
#
# class ResultsView(generic.DetailView):
#     model = Wallet
#     template_name = 'polls/wallets.html'
#
#
# def wallets(request, question_id):
#     question = get_object_or_404(Wallet, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Wallet.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'portfolio/wallet.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('wallets:results', args=(question.id,)))
#
