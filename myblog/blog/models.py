from django.db import models
from mdeditor.fields import MDTextField #必须导入

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='文章标题')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    comment = models.IntegerField(default=0, verbose_name='评论量')
    content = MDTextField(default=0)    #注意为MDTextField()
    class Meta:
        db_table = 'Article'
        verbose_name="文章"