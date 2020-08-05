from django import forms
from django.forms import Textarea
from django.db import models

from pp_site.utils.models import TimeStampMixin


class ForumPost(TimeStampMixin):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    media_file = models.FileField()
    rating = models.IntegerField(default=0)

    @staticmethod
    def fields():
        """ Used for post searching """
        whitelist = {
            models.CharField,
            models.IntegerField,
            models.TextField
        }
        for field in ForumPost._meta.local_fields:
            if type(field) in whitelist:
                yield field.name
            else:
                continue

        return


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ["title", "author", "description", "media_file"]


class ForumPostReply(TimeStampMixin):
    author = models.CharField(max_length=30)
    content = models.TextField()
    forum_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)


class ForumPostReplyForm(forms.ModelForm):
    class Meta:
        model = ForumPostReply
        fields = ["author", "content"]
        widgets = {
            "content": Textarea(attrs={'width': '100%', 'height': '3em'})
        }
