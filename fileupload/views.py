# encoding: utf-8
import json

from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, ListView
from .models import Submission
from allauthdemo.demo.models import Problem
from allauthdemo.auth.models import DemoUser

from .response import JSONResponse, response_mimetype
from .serialize import serialize

class SubmissionCreateView(CreateView):
    model = Submission
    fields = ['file', 'slug']

    def form_valid(self, form):
        form.instance.user = self.request.user

        problem_pk = self.request.POST.get('problem_pk')
        problem_object = Problem.objects.filter(pk=problem_pk)
        problem_object = problem_object[0]

        form.instance.problem = problem_object

        self.object = form.save()

        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')

class SubmissionDeleteView(DeleteView):
    model = Submission

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class SubmissionListView(ListView):
    model = Submission

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() if p.user == self.request.user]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

class BasicVersionCreateView(SubmissionCreateView):
    template_name_suffix = '_basic_form'
    context_object_name = 'submission'

    def get_context_data(self, **kwargs):
        context = super(BasicVersionCreateView, self).get_context_data(**kwargs)
        context['problems_retrieved'] = Problem.objects.all()
        return context

class SubmitList(ListView):
    model = Submission
    template_name_suffix = '_list'
    context_object_name = 'submissions'

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)
