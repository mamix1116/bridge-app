from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime

class ManagementOrganization(models.Model):
    """管理者モデル"""
    class Meta:
        # テーブル名を定義
        db_table = 'management_organization'
        verbose_name_plural = "管理者"

    # テーブルのカラムに対応するフィールドを定義
    management_organization = models.CharField(verbose_name='管理者', max_length=100)

    def __str__(self):
        return self.management_organization


class Bridge(models.Model):
    """橋梁モデル"""
    class Meta:
        db_table = 'bridge'
        verbose_name_plural = "橋梁"
        unique_together = (
            ('bridge_id', 'management_organization'),
        )

    management_organization = models.ForeignKey(ManagementOrganization, on_delete=models.PROTECT, verbose_name='管理者', related_name="bridges")
    bridge_id = models.IntegerField(verbose_name='橋梁ID')
    bridge_name = models.CharField(verbose_name='橋梁名称', max_length=100)
    bridge_name_yomi = models.CharField(verbose_name='橋梁名称カタカナ', max_length=100, blank=True)
    location_city = models.CharField(verbose_name='所在地 市町村', max_length=100)
    location_address = models.CharField(verbose_name='所在地', max_length=255, blank=True)
    road_cd = models.IntegerField(verbose_name='路線番号')
    road_name = models.CharField(verbose_name='路線名', max_length=100 )
    fyear_start = models.IntegerField(verbose_name='供用年',  null=True, blank=True)
    len_m = models.DecimalField(verbose_name='橋長m', max_digits=10, decimal_places=2, null=True, blank=True)
    wid_m = models.DecimalField(verbose_name='幅員m', max_digits=10, decimal_places=2, null=True, blank=True)
    span_num = models.IntegerField(verbose_name='径間数', null=True, blank=True)
    latitude = models.FloatField(verbose_name='緯度', null=True, blank=True)
    longtitude = models.FloatField(verbose_name='経度', null=True, blank=True)
    have_alternative = models.BooleanField(verbose_name='代替路', null=True, default=False, blank=True)
    date_register = models.DateField(verbose_name='入力年月日', default=timezone.datetime.now,  null=True, blank=True)
    image_main = models.ImageField(verbose_name='メイン画像', blank=True, upload_to='img/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bridge_name


class Inspection(models.Model):
    """点検モデル"""
    class Meta:
        db_table = 'inspection'
        verbose_name_plural = "点検"

    bridge_name = models.ForeignKey(Bridge, on_delete=models.PROTECT, verbose_name="橋梁名称", related_name="inspections")
    date_inspect = models.DateField(verbose_name='点検年月日', default=timezone.datetime.now)
    eval_overall = models.CharField(verbose_name='橋梁毎の判定', max_length=10, blank=True)
    eval_comment = models.TextField(verbose_name='所見', blank=True, null=True, max_length=1000,)
    eval_superstructure01 = models.CharField(verbose_name='判定 上部床版', max_length=10, blank=True)
    eval_superstructure02 = models.CharField(verbose_name='判定 上部横桁', max_length=10, blank=True)
    eval_superstructure03 = models.CharField(verbose_name='判定 上部床版', max_length=10, blank=True)
    eval_substructure = models.CharField(verbose_name='判定 下部構造', max_length=10, blank=True)
    eval_bearing = models.CharField(verbose_name='判定 支承部', max_length=10, blank=True)
    eval_other = models.CharField(verbose_name='判定 その他', max_length=10, blank=True)

    def __str__(self):
        return self.date_inspect.strftime("%Y-%m-%d")
