from rest_framework import viewsets
from shopid.models import ListModel
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from douyin.utils.api import API
from douyin.filter import Filter
from rest_framework.exceptions import APIException
import os, logging
from django.conf import settings

class AfterSaleOperate(viewsets.ModelViewSet):
    """
        create:
            售后审核接口聚合版
            type说明:
            值 说明 必须参数
            101 同意退货申请（一次审核） Logistics.ReceiverAddressId 或 Logistics.AfterSaleAddressDetail
            102 拒绝退货申请（一次审核）reason , evidence
            111 同意退货（二次审核）
            112 拒绝退货 (二次审核) reason , evidence
            121 退货转退款
            201 同意仅退款
            202 拒绝仅退款 reason , evidence
            203 同意拒签后退款
            301 同意换货申请（一次审核)Logistics.ReceiverAddressId 或 Logistics.AfterSaleAddressDetail
            302 拒绝换货申请（一次审核）reason,evidence
            311 同意换货（二次审核）logistics.companyCode,logistics.logisticsCode
            312 拒绝换货（二次审核）reason,evidence
            321 换货转退款
            401 同意售前退申请
            ps. 通过发货拒绝售前退申请，所以审核接口不支持售前退
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
        path = '/afterSale/operate'
        params = self.params
        result = self.api_init().request(path=path, params=params)
        return Response({'result': result if result else ''})