from django.forms import ModelForm
from . models import lapInfo

class lapform(ModelForm):
    class Meta:
        model = lapInfo
        fields = '__all__'


