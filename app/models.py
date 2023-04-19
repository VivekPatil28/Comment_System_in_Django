from django.db import models
from datetime import datetime, timezone
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def how_old(self):
        date = self.created_at.replace(tzinfo=None)
        if (datetime.now()-date).total_seconds() < 60:
            return f"{int((datetime.now() - date).total_seconds())}s"
        elif (datetime.now()-date).total_seconds() < 3600:
            return f"{int((datetime.now() - date).total_seconds() // 60)}m"
        elif (datetime.now() - date).days < 1:
            return f'{int((datetime.now() - date).total_seconds()//3600)}h'
        elif (datetime.now() - date).days < 7:
            return f'{int((datetime.now() - date).total_seconds()//84600)}d'
        elif (datetime.now() - date).days < 30:
            return (datetime.now() - date).days//7+"w"
        elif (datetime.now() - date).days < 365:
            return (datetime.now() - date).days//30.5+"m"
        else:
            return (datetime.now() - date).days//365+"y"

    def __str__(self) -> str:
        return str(self.content)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
