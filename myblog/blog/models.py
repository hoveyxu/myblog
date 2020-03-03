from django.db import models
from mdeditor.fields import MDTextField  # 必须导入


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='文章标题')
    category = models.CharField(default=0, max_length=30, verbose_name='文章分类')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    comment = models.IntegerField(default=0, verbose_name='评论量')
    content = MDTextField(default=0)  # 注意为MDTextField()

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Article'
        verbose_name = "文章"
