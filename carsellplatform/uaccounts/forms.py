from django import forms 
from .models import Comment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                                   'class': 'form-control', 'rows': 2, 
                                   'placeholder': 'Enter your comment here...'})
        }
        
        labels = {
            'text': 'Comment'
        }