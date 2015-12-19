from django.shortcuts import render
from django.views import generic

from allauthdemo.demo.models import Problem
# Create your views here.

class ProblemView(generic.ListView):
	model = Problem
	template_name = '../templates/bases/problem-list.html'
	context_object_name = 'problems_retrieved'
	
	def get_queryset(self):
		return Problem.objects.all()
