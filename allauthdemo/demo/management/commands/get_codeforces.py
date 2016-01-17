import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from allauthdemo.auth.models import DemoUser


class Command(BaseCommand):
    CODEFORCES_JSON_DIR = os.path.join(settings.BASE_DIR, 'codeforces_json')

    def add_arguments(self, parser):
        parser.add_argument('--user',
            action='store_true',
            dest='user_id',
            default=False,
        )

    def handle(self, *args, **options):
        contest_ids = range(592, 616+1)
        user_ids = []
        if options['user_id']:
            user_ids.append(DemoUser.objects.get(pk=options['user_id']))
        else:
            user_ids = DemoUser.objects.all()

        for contest in contest_ids:
            contest_json_path = os.path.join(self.CODEFORCES_JSON_DIR, str(contest) + '.json')
            if (not os.path.isfile(contest_json_path)):
                self.get_codeforces_json(contest)

        for user in user_ids:
            self.get_user_results(user)


    def get_codeforces_json(self, contest_id):
        contest_json_path = os.path.join(self.CODEFORCES_JSON_DIR, str(contest) + '.json')

    def get_user_results(self, user_id):
        pass
