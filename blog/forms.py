from django import forms
from blog.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'tags', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'article-title', 'placeholder': 'タイトル'}),
            'tags': forms.TextInput(attrs={'class': 'article-tags', 'placeholder': 'タグ'}),
            'text': forms.Textarea(
                attrs={'class': 'edit', 'placeholder': 'マークダウン'})

        }

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('author', 'text')
#
#         widgets = {
#             'author': forms.TextInput(attrs={'class': 'textinputclass'}),
#             'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
#         }
