from core.base import BaseForm
from web.models import *

class DepartmentForm(BaseForm):
    class Meta:
        model = Department
        fields = "__all__"
        
    
class SemesterForm(BaseForm):
    class Meta:
        model = Semester
        fields = "__all__"
        
    
class SubjectForm(BaseForm):
    class Meta:
        model = Subject
        fields = "__all__"
        
    
class NoteForm(BaseForm):
    class Meta:
        model = Note
        fields = "__all__"