from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

from .auth.models import Problem

@login_required
def member_index(request):
    return render_to_response("member/member-index.html", RequestContext(request))

@login_required
def member_action(request):
    return render_to_response("member/member-action.html", RequestContext(request))

class ProblemView(generic.ListView):
	template_name = '../templates/bases/problem-list.html'
	context_object_name = 'problem_list'

	def get_queryset(self):
		return Problem.objects.all()
