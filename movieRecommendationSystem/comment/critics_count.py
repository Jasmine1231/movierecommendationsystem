from .models import ShortComments
from django.db.models import Count

def get_critic():
    critics=ShortComments.objects.values()
