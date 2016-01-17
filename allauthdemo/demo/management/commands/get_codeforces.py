import os
import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from allauthdemo.auth.models import DemoUser


class Command(BaseCommand):
    CODEFORCES_JSON_DIR = os.path.join(settings.BASE_DIR, 'codeforces_json')
    CONTEST_IDS = range(592, 616+1)

    def add_arguments(self, parser):
        parser.add_argument('--user',
            action='store_true',
            dest='user_handle',
            default=False,
        )

    def handle(self, *args, **options):
        users = []
        if options['user_handle']:
            users.append(DemoUser.objects.get(codeforces_handle=options['user_handle']))
        else:
            users = DemoUser.objects.all()

        for contest in CONTEST_IDS:
            contest_json_path = os.path.join(self.CODEFORCES_JSON_DIR, str(contest) + '.json')
            if (not os.path.isfile(contest_json_path)):
                self.get_codeforces_json(contest)

        for user in users:
            self.get_user_results(user)

    def get_codeforces_json(self, contest_id):
        print("Getting contest ", contest_id)
        contest_json_path = os.path.join(self.CODEFORCES_JSON_DIR, str(contest_id) + '.json')

        resp = requests.get('http://codeforces.com/api/contest.standings?contestId=' + str(contest_id) + '&showUnofficial=true')
        if resp.status_code == 200:
            with open(contest_json_path, 'wb') as stream:
                stream.write(resp.content)
        else:
            print("Nu a mers.", resp.content)

    def get_user_results(self, user):
        pass
