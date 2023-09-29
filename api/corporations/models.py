# from django.conf import settings
from django.db import models
from django.utils import timezone


class Corporation(models.Model):
    edinet_code = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="EDINETコード",
    )
    sec_code = models.IntegerField(
        null=True,
        blank=True,
        unique=True,
        verbose_name="証券コード",
    )
    jcn = models.BigIntegerField(
        null=True,
        blank=True,
        unique=False,
        verbose_name="法人番号",
    )

    corporation_type = models.CharField(
        max_length=30,
        verbose_name="法人の種別",
        default="内国法人・組合",
    )
    listing_type = models.BooleanField(
        verbose_name="上場区分",
        null=True,
    )
    linking_type = models.BooleanField(
        verbose_name="連結の有無",
        null=True,
    )
    capital = models.IntegerField(
        blank=True,
        verbose_name="資本金",
        default=0,
    )
    setting_day = models.DateField(
        verbose_name="決算日",
        null=True
    )

    location = models.CharField(
        max_length=200,
        verbose_name="所在地",
        blank=True,
    )
    industry_type = models.CharField(
        max_length=30,
        verbose_name="業種",
        blank=True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="法人名",
    )
    name_eng = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="法人名(英字)",
    )
    name_kana = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="法人名(ヨミ)",
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.edinet_code
