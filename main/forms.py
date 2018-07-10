from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import AddWords
from .models import CreateNotes



class AddWordsForm(ModelForm):
    class Meta:
        model = AddWords
        fields = '__all__'

class CreateNotesForm(ModelForm):
    class Meta:
        model = CreateNotes
        fields = '__all__'