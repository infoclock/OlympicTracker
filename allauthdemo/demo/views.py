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

            d['homework_points'] = 0
            submissions = Submission.objects.filter(user=user)
            problem_ids = set()
            for submission in submissions:
                if submission.problem.id not in problem_ids:
                    problem_ids.add(submission.problem.id)
                    d['homework_points'] += submission.problem.score

            d['codeforces_points'] = sum([x.score for x in ContestParticipation.objects.filter(user=user)])
            d['no_stress'] = user.score_fmi_no_stress / 20
            d['csacademy'] = user.score_csacademy / 20
            d['max_points'] = 100 if user.school_year == 1 else 140
            d['score_extra'] = user.score_extra
            d['total'] = d['homework_points'] + d['codeforces_points'] + d['no_stress'] + d['csacademy'] + d['score_extra']
            pure_grade = round(float(d['total']) / float(d['max_points']) * 10)
            d['nota'] = min(pure_grade, 10.0)
            if d['nota'] >= 1:
                users.append(d)
        context['users'] = sorted(users, key=lambda x: x['nota'], reverse=True)
        return context
