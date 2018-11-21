from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    # 어디에 속해있냐, 글삭제시 자동 삭제기능, has_many 구현기능
    author = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
