from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import AddWords



class AddWordsForm(ModelForm):
    class Meta:
        model = AddWords
        fields = '__all__'