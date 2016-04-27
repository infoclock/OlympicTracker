import math

from django.shortcuts import render
from django.views import generic

from allauthdemo.auth.models import DemoUser
from allauthdemo.demo.models import Problem
from fileupload.models import Submission
from allauthdemo.demo.models import ContestParticipation


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


class RankingView(generic.TemplateView):
    template_name = '../templates/bases/ranking-list.html'

    def get_context_data(self, **kwargs):
        context = super(RankingView, self).get_context_data(**kwargs)

        users = []
        for user in DemoUser.objects.all():
            d = {}
            d['name'] = user.get_full_name()
            d['id'] = user.id
            d['codeforces_points'] = sum([x.score for x in ContestParticipation.objects.filter(user=user)])

        context['users'] = sorted(users, key=lambda x: (x['nota'], x['total']), reverse=True)
        return context
