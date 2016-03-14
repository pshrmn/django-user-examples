from django import forms

from .models import Choice


class ChoiceForm(forms.ModelForm):

    choice = forms.ChoiceField(
        choices=[(True, True), (False, False)],
        label='Choose Between:',
        widget=forms.widgets.RadioSelect()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # override the choices to use the pair strings
        if self.initial.get('pair') is not None:
            pair = self.initial['pair']
            self.fields['choice'].choices = [
                (True, pair.a),
                (False, pair.b)
            ]

    class Meta:
        model = Choice
        fields = ('choice', 'pair')

        widgets = {
            'pair': forms.widgets.HiddenInput()
        }
