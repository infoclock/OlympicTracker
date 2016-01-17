# encoding: utf-8
from django.db import models
from allauthdemo.auth.models import DemoUser
from allauthdemo.demo.models import Problem


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<problem>/<user_id>_<problem>.<extension>
    extension = filename.split('.')

    if len(extension) != 0:
        extension = extension[-1]
    return '{1}/{1}_user_{0}.{2}'.format(instance.user.id, instance.problem.name, extension)


class Submission(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    slug = models.SlugField(max_length=50, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(DemoUser, null=True)
    problem = models.ForeignKey(Problem, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        # delete the file if it already exists
        try:
            submissions = Submission.objects.filter(user_id=self.user_id, problem_id=self.problem_id)
            for submission in submissions:
                submission.file.delete(save=False)
        except:
            pass

        super(Submission, self).save(*args, **kwargs)
