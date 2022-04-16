from django.db import models

# Create your models here.
class Article(models.Model):
    '''齐物逍遥游博客的文章'''
    title = models.CharField(max_length=200)    #title标题，CharField存储文本的字符，必带参数max_length
    author = models.CharField(max_length=50)    #author作者
    text = models.CharField(max_length=99999)   #text 内容
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''需要告诉django，默认使用哪个属性来显示有关BlogPost的信息'''