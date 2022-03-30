from rest_framework import viewsets
from shopid.models.douyinmodels import ListModel
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from douyin.utils.api import API
from douyin.filter import Filter
from rest_framework.exceptions import APIException
import os, logging
from django.conf import settings

class BrandGetSug(viewsets.ModelViewSet):
    """
        create:
            通过前缀匹配召回品牌信息
            通过输入品牌名称进行模糊查询，支持品牌中文名(拼音)、英文名，并返回品牌信息
            本接口适用于通过前缀匹配的形式对品牌信息，例如想要“安踏”，可以通过搜索“安”来查询，但是搜索“踏”是无法找到的。
            注意点：1. 召回的第一个为品牌名称严格匹配项。
            2. 单次召回数量最多为10个。
            3. 支持中文名称或英文名称，但不可以两个名称一起输入来查询
            4. 不支持特殊符号，例如“/”，“ ”，“·”，以及除中英文外的语言
        """
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def __init__(self):
        self.params = {}

    def get_queryset(self):
        if self.request.user:
            return ListModel.objects.filter(shop_mode='douyin')
        else:
            return ListModel.objects.none()

    def api_init(self):
        if os.path.exists(os.path.join(settings.BASE_DIR, 'media/' + self.request.auth.openid + '/' + 'douyin.log')) is True:
            logging.basicConfig(
                filename=os.path.join(settings.BASE_DIR, 'media/' + self.request.auth.openid + '/' + 'douyin.log'),
                level=logging.DEBUG, filemode='a',
                format='%(asctime)s - %(process)s - %(levelname)s: %(message)s')
        else:
            with open(os.path.join(settings.BASE_DIR, 'media/' + self.request.auth.openid + '/' + 'douyin.log'), "w") as f:
                f.close()
            logging.basicConfig(
                filename=os.path.join(settings.BASE_DIR, 'media/' + self.request.auth.openid + '/' + 'douyin.log'),
                level=logging.DEBUG, filemode='a',
                format='%(asctime)s - %(process)s - %(levelname)s: %(message)s')
        t_code_data = self.request.data
        if 't_code' not in t_code_data:
            raise APIException({'detail': '店铺唯一值不在Post Data中'})
        shop_data = ListModel.objects.filter(t_code=t_code_data['t_code']).first()
        if shop_data.proxy == 1:
            proxy = shop_data.proxy_ip
        else:
            proxy = None
        if shop_data.sandbox == 1:
            sandbox = True
        else:
            sandbox = False
        if os.path.exists(os.path.join(settings.BASE_DIR, 'media/' + self.request.auth.openid + '/' + shop_data.shop_id + '.token')) is False:
            with open(os.path.join(settings.BASE_DIR, 'media/' + self.request.auth.openid + '/' + shop_data.shop_id + '.token'), 'w') as f:
                f.close()
        gdoudian = API(
            app_key=shop_data.shop_appid,
            app_secret=shop_data.shop_app_secret,
            shop_id=shop_data.shop_id,
            token_file=os.path.join(settings.BASE_DIR, 'media/' + self.request.auth.openid + '/' + shop_data.shop_id + '.token'),
            logger=logging.getLogger("douyin"),
            proxy=proxy,
            test_mode=sandbox
        )
        return gdoudian

    def create(self, request, *args, **kwargs):
        path = '/brand/getSug'
        params = self.params
        result = self.api_init().request(path=path, params=params)
        return Response({'result': result if result else ''})