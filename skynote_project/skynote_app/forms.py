from django import forms

class notes_form(forms.Form):
    title = forms.CharField(max_length=255,label="", widget=forms.TextInput(attrs={'class': 'notes__title', 'placeholder': 'Enter a title...'}))
    note_text = forms.CharField(required=False,label="", widget=forms.Textarea(attrs={'class': 'notes__body', 'rows': 11, 'placeholder': 'Write your note here...'}))
