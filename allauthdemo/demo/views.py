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
        context['minimum'] = 12 * 3.0

        users = []
        for user in DemoUser.objects.all():
            d = {}
            d['name'] = user.get_full_name()
            d['id'] = user.id
            d['codeforces_handle'] = user.codeforces_handle
            d['echivaleaza'] = user.is_participating_2016
            d['codeforces_points'] = sum([x.score for x in ContestParticipation.objects.filter(user=user)])
            d['codeforces_grade'] = round(min(d['codeforces_points'] / context['minimum'] * 10, 10.0), 1)
            d['1st'] = user.problems_solved_first_exam
            d['2nd'] = user.problems_solved_second_exam
            best_solved = max(user.problems_solved_first_exam, user.problems_solved_second_exam)
            d['exam_grade'] = 0
            if best_solved > 4:
                d['exam_grade'] = 10.0
            elif best_solved < 2:
                d['exam_grade'] = '-'
            else:
                distribution = {
                    # no solved problems - grade
                    2: 5,
                    3: 7,
                    4: 9,
                }
                d['exam_grade'] = distribution[best_solved]

            if d['exam_grade'] != '-':
                d['final_grade'] =  (d['exam_grade'] + d['codeforces_grade']) / 2
            else:
                d['final_grade'] = 0

            if d['echivaleaza']:
                users.append(d)

        context['users'] = sorted(users, key=lambda x: (x['final_grade'], x['codeforces_points']), reverse=True)
        return context


class ParticipantView(generic.TemplateView):
    template_name = '../templates/bases/participant.html'

    def get_context_data(self, **kwargs):
        context = super(ParticipantView, self).get_context_data(**kwargs)
        user = DemoUser.objects.get(pk=int(context['user_id']))
        context['name'] = user.get_full_name()

        res = []
        for participation in ContestParticipation.objects.filter(user=user):
            p = {}
            p['name'] = participation.name
            p['place'] = participation.place
            p['score'] = participation.score
            res.append(p)

        context['participations'] = res
        return context
