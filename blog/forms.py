from .models import Posts
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'main_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form form_textinput',
                'placeholder': 'Post title'
            }),
            'main_text': Textarea(attrs={
                'class': 'form form_textarea',
                'placeholder': 'Main text'
            }),
        }
