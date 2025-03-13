from core.base import BaseTable
from django_tables2 import columns

from web.models import *


class SemesterTable(BaseTable):
    
    class Meta:
        model = Semester
        fields = ("name",)
        attrs = {"class": "table key-buttons border-bottom"}
        