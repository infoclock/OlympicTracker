# encoding: utf-8
from django.db import models
from allauthdemo.auth.models import DemoUser
from allauthdemo.demo.models import Problem

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    extension = filename.split('.')

    if len(extension) != 0:
        extension = extension[-1]
    return 'user_{0}/{1}.{2}'.format(instance.user.id, instance.problem.name, extension)

class Submission(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    slug = models.SlugField(max_length=50, blank=True)
    user = models.ForeignKey(DemoUser, null=True)
    problem = models.ForeignKey(Problem, null=True)
    
    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Submission, self).save(*args, **kwargs)