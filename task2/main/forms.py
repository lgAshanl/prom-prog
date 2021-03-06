from django import forms
from main.models import Questions


class QuestionForm(forms.ModelForm):
    question = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Questions
        fields = ('question',)
