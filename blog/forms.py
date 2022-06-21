from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=265,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Enter todo delete',
                                   'aria_describedby': 'add-btn'
                               }
                           ))
