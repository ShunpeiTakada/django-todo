from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() #CharFieldより文字数が多い場合（引数は必須でない）
    updated_date = models.DateTimeField(auto_now=True) #更新日時ー保存される度、現在日時をセット
    author = models.CharField(max_length=100) #todo作成者
    # 追加
    is_done = models.BooleanField(default=False)