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
        good_result = []
        bad_result = []
        submissions = Submission.objects.filter(user=self.request.user)
        for problem in Problem.objects.all():
            submission = submissions.filter(problem=problem).order_by('-last_modified').first()
            if submission:
                good_result.append(submission)
            else:
                bad_result.append(problem)
        return {'good': good_result, 'bad':bad_result}
