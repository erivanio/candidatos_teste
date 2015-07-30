from django import forms
from apps.core.models import Candidate


class CandidateForm(forms.ModelForm):
    html = forms.ChoiceField(choices=[(i, i) for i in range(11)])
    css = forms.ChoiceField(choices=[(i, i) for i in range(11)])
    javascript = forms.ChoiceField(choices=[(i, i) for i in range(11)])
    python = forms.ChoiceField(choices=[(i, i) for i in range(11)])
    django = forms.ChoiceField(choices=[(i, i) for i in range(11)])
    ios = forms.ChoiceField(choices=[(i, i) for i in range(11)])
    android = forms.ChoiceField(choices=[(i, i) for i in range(11)])

    class Meta:
        model = Candidate
        fields = ['name', 'email', 'html', 'css', 'javascript', 'python', 'django', 'ios', 'android']