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

class MaterialUploadImageSync(viewsets.ModelViewSet):
    """
        create:
            支持获取店铺数据
            同步上传素材
            素材中心同步创建图片素材接口
            （1）如果一次性要上传多个素材，请使用批量上传图片接口（/material/batchUploadImageSync）
            （2）图片大小限3M，支持的格式有：jpeg/png/jpg；
            （3）创建素材成功，就能拿到素材的url；
            （4）素材中心会对素材进行异步审核，对于审核失败的素材，素材中心会在一定时间内将其删除；
            （5）接口返回“素材URL无效”怎么办？第一步，确保url能正常访问；第二步，确保图片格式为jpeg/png/jpg；如果上述步骤都没问题，重新上传试试。
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
        path = '/material/uploadImageSync'
        params = self.params
        result = self.api_init().request(path=path, params=params)
        return Response({'result': result if result else ''})