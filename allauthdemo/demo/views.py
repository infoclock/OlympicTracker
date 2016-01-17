from django.shortcuts import render
from django.views import generic

from allauthdemo.demo.models import Problem
from fileupload.models import Submission


class ProblemView(generic.ListView):
	model = Problem
	template_name = '../templates/bases/problem-list.html'
	context_object_name = 'problems_retrieved'

	def get_queryset(self):
		return Problem.objects.all()


class SubmissionView(generic.ListView):
    model = Submission
    template_name = '../templates/bases/submission-list.html'
    context_object_name = 'submissions'

    def get_queryset(self):
        result = []
        submissions = Submission.objects.filter(user=self.request.user)
        for problem in Problem.objects.all():
            result.append(submissions.filter(problem=problem).order_by('-last_modified').first())
        return result
