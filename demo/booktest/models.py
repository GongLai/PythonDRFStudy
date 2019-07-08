from django.db import models


class BookInfo(models.Model):
    """定义图书模型类"""
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)

    class Meta:
        db_table = 'tb_books'  # 数据库表名
        verbose_name = '图书'  # 在admin站点的显示名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """对应每个数据对象的显示信息"""
        return self.btitle


class HeroInfo(models.Model):
    # 定义英雄模型类HeroInfo
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname
