from .models import Post
from django import forms
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "category", "tags"]

        def __init__(self, *args, **kwargs):
            for field in self.base_fields.values():
                field.widget.attrs["class"] = "form-control"
            super().__init__(*args, **kwargs)