'''
Script to populate polls table
'''

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'one_django_project.settings')
django.setup()
from polls.models import Question

from django.utils import timezone

q = Question.objects.get_or_create(question_text='Whats up', pub_date=timezone.now())
q_saved = Question.objects.get(pk=1)
# q_saved = Question.objects.filter(question_text__startswith='What')
q_saved.choice_set.create(choice_text='Not much', votes=0)
q_saved.choice_set.create(choice_text='The sky', votes=0)
q_saved.choice_set.create(choice_text='Just hacking again', votes=0)
q_saved.save()