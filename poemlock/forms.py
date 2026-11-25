from django import forms


class AnswerForm(forms.Form):
    answer1 = forms.CharField(label="Antwoord 1", max_length=200)
    answer2 = forms.CharField(label="Antwoord 2", max_length=200)
    answer3 = forms.CharField(label="Antwoord 3", max_length=200)
