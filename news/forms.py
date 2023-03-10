from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announcement', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of title'
            }),

            'announcement': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Announcement'
            }),

            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article'
            }),

            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publishing'
            })
        }