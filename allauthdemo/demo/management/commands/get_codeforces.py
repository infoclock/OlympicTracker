import os
import json
import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from allauthdemo.auth.models import DemoUser
from allauthdemo.demo.models import ContestParticipation


class Command(BaseCommand):
    CODEFORCES_JSON_DIR = os.path.join(settings.BASE_DIR, 'codeforces_json')
    CONTEST_IDS = [658, 657, 639, 659, 660, 661, 640, 662, 664, 663, 665, 669, 668, 641, 643, 673, 674, 670, 666, 667,
                   671, 672, # codeforces 352
                   675] # codeforces 353

    def add_arguments(self, parser):
        parser.add_argument('--user',
            action='store',
            dest='user_handle',
            default=False,
        )

    def handle(self, *args, **options):
        users = []
        if options['user_handle']:
            users.append(DemoUser.objects.get(codeforces_handle=options['user_handle']))
        else:
            users = DemoUser.objects.all()

        for contest in self.CONTEST_IDS:
            contest_json_path = os.path.join(self.CODEFORCES_JSON_DIR, str(contest) + '.json')
            if (not os.path.isfile(contest_json_path)):
                self.get_codeforces_json(contest)

        for user in users:
            self.get_user_results(user)

    def get_codeforces_json(self, contest_id):
        print("Getting contest ", contest_id)
        contest_json_path = os.path.join(self.CODEFORCES_JSON_DIR, str(contest_id) + '.json')

        resp = requests.get('http://codeforces.com/api/contest.standings?contestId=' + str(contest_id))
        if resp.status_code == 200:
            with open(contest_json_path, 'wb') as stream:
                stream.write(resp.content)
        else:
            print("Nu a mers.", resp.content)

    def get_user_results(self, user):
        print(user.codeforces_handle)
        ContestParticipation.objects.filter(user=user).delete()
        for contest in self.CONTEST_IDS:
            contest_json_path = os.path.join(self.CODEFORCES_JSON_DIR, str(contest) + '.json')

            with open(contest_json_path) as stream:
                data = json.load(stream)['result']

            for row in data['rows']:
                if row['party']['members'][0]['handle'] == user.codeforces_handle:
                    participation = ContestParticipation(user=user, place=row['rank'], name=data['contest']['name'])
                    percentile = row['rank'] / len(data['rows']) * 100
                    participation.score = self.get_score(percentile, 'Div. 1' in participation.name)
                    participation.save()
                    print(participation.name, participation.score, "{0}/{1}".format(participation.place, len(data['rows'])))
                    break

    def get_score(self, percentile, is_div_1):
        DIV2 = [
            [5, 12],
            [10, 10],
            [20, 8],
            [30, 7],
            [40, 6],
            [50, 5],
            [60, 4],
            [70, 3],
            [80, 2],
            [90, 1],
        ]

        DIV1 = [
            [5, 100],
            [10, 75],
            [20, 40],
            [30, 30],
            [40, 20],
            [50, 19],
            [60, 18],
            [70, 17],
            [80, 16],
            [90, 15],
        ]

        schema = DIV1 if is_div_1 else DIV2
        for row in schema:
            if percentile <= row[0]:
                return row[1]
        return 0
