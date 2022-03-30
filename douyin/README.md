## GreaterWMS 抖音SDK调用教程

### SDK具体功能:

- 1，一仓多店，多仓多店
- 2，库存同步，商品同步
- 3，快递发货，物流轨迹
- 4，订单拦截
- 5，字节云仓
- 6，精选联盟
- 7，供应分销
- 8，售后退款，账单
### 对应的API链接
- [抖音API文档](https://op.jinritemai.com/docs/api-docs/13)
- [抖音消息推送文档](https://op.jinritemai.com/docs/message-docs/30)

### 创建抖店
- 去抖音官方创建个商家应用
- 抖店应用会给到3个Key，APPID，APP_SECRET，SHOP_ID
- 在GreaterWMS电商店铺中，抖音页面添加一个店铺
- 填入之前获得的3个Key和店铺名称
- GreaterWMS会给这个店铺生成一个唯一值，用来实现一仓多店的唯一性

### 沙箱环境开启
- 沙箱环境为了安全起见，并不能通过前端去修改，以免用户误点
- 向以下路径post一个json data
- http://127.0.0.1:8008/shopid/douyin/sandbox/
~~~json
{
  "t_code": "{ 你刚才在GreaterWMS会给这个店铺生成一个唯一值 }",
  "sandbox": "{ 将sandbox调整成开启还是关闭，开始是1，关闭是0 }"
}
~~~
- 由此来控制店铺是否正式运营上线，默认是正式环境

### 代理IP开启
- 代理IP为了安全起见，并不能通过前端去修改，以免用户误点
- 向以下路径post一个json data
- http://127.0.0.1:8008/shopid/douyin/proxy/
~~~json
{
  "t_code": "{ 你刚才在GreaterWMS会给这个店铺生成一个唯一值 }",
  "proxy": "{ 将代理调整成开启还是关闭，开始是1，关闭是0 }",
  "proxy_ip": "{ 代理ip，是一个json数据 }"
}
~~~ 
- 代理设置，None或者{"https": "http://10.10.1.10:1080"}，详细格式参见https://docs.python-requests.org/zh_CN/latest/user/advanced.html
- 由此来控制店铺是否正式使用代理，默认是不使用

### 安装
- 下载插件
- [https://community.56yhz.com/plugMarket/118.html](https://community.56yhz.com/plugMarket/118.html)
- 放到GreaterWMS根目录下面
~~~python
    pip install GreaterWMS_DouYin-1.0.0-py3-none-any.whl
~~~
- 版本的更新，安装的插件名会不同，请自行调整版本
- 注册app
~~~python
INSTALLED_APPS = [
    '...',
    '...',
    'douyin'
]
~~~

### API调用例子
~~~python
# 在views.py
from douyin.views.ding_dan.order_searchList import OrderSearchList

class Test(OrderSearchList):
    def __init__(self):
        self.params = {}
        self.param.product_id = "3539925204033339668"
        self.param.out_product_id = "11111"
        self.param.show_draft = "true"

# urls.py
from django.urls import path
from .views import Test

urlpatterns = [
    path(r'test/', Test.as_view({"post": "create"}), name="test")
]
~~~
- 接下来只要向这个接口POST一个之前提到的店铺唯一值，"t_code" 就可以获取数据
##### 回调的示例
~~~json
{
  "data": {
    "account_template_id": "1",
    "after_sale_service": "{\"supply_7day_return\":\"2\"}",
    "appoint_delivery_day": "2",
    "brand_id": "12344",
    "car_vin_code": "VIN11111111111111",
    "category_detail": {
      "first_cid": "23264",
      "first_cname": "教育培训",
      "fourth_cid": "0",
      "fourth_cname": "-",
      "second_cid": "0",
      "second_cname": "学习卡",
      "third_cid": "0",
      "third_cname": "-"
    },
    "cdf_category": "1",
    "check_status": "1",
    "create_time": "2021-03-29 15:52:52",
    "delivery_delay_day": "2",
    "delivery_method": "7",
    "description": "<img src=\\\"https://tosv.boe.byted.org/obj/temai/54cbf542128eff94a3549284817c0af5bf5c2960www800-800\\\" style=\\\"width:100%;\\\">",
    "discount_price": "12000",
    "draft_status": "2",
    "extra": "-",
    "img": "https://xxxx.byted.org/obj/temai/54cbf542128eff94a3549284817c0af5bf5c2960www800-800",
    "is_create": "1",
    "is_sub_product": "true",
    "limit_per_buyer": "5",
    "logistics_info": {
      "brand_country_id": "123",
      "customs_clear_type": "1",
      "net_weight_qty": "100",
      "origin_country_id": "123",
      "source_country_id": "123",
      "tax_payer": "0"
    },
    "market_price": "12000",
    "maximum_per_order": "5",
    "minimum_per_order": "1",
    "mobile": "15677775555",
    "name": "xxx爽肤水",
    "need_recharge_mode": "false",
    "open_user_id": "1",
    "out_product_id": "11111",
    "outer_product_id": "11111",
    "pay_type": "1",
    "pic": "[\"https://sf6-ttcdn-tos.pstatp.com/obj/temai/0c71ce6acb4e3b508e0d30042b1a94262818ab41www800-800\"]",
    "poi_resource": {
      "coupon_return_methods": "[1]"
    },
    "presell_config_level": "2",
    "presell_delay": "4",
    "presell_type": "1",
    "price_has_tax": "0",
    "product_format": "{\"货号\":\"8888\"}",
    "product_format_new": "{\"1088\":[{\"Value\":0,\"Name\":\"小33学二年级\",\"PropertyId\":1088,\"PropertyName\":\"适用学龄段\",\"diy_type\":1}],\"1319\":[{\"Value\":0,\"Name\":\"1\",\"PropertyId\":1319,\"PropertyName\":\"适用地区\",\"diy_type\":0}],\"1618\":[{\"Value\":0,\"Name\":\"9787218122861\",\"PropertyId\":1618,\"PropertyName\":\"ISBN编号\",\"diy_type\":0}],\"1831\":[{\"Value\":0,\"Name\":\"小学英语看图说话写话二年级\",\"PropertyId\":1831,\"PropertyName\":\"书名\",\"diy_type\":0}],\"2000\":[{\"Value\":34762,\"Name\":\"无\",\"PropertyId\":2000,\"PropertyName\":\"作者地区\",\"diy_type\":0}],\"2229\":[{\"Value\":0,\"Name\":\"1\",\"PropertyId\":2229,\"PropertyName\":\"编者\",\"diy_type\":0}],\"3271\":[{\"Value\":0,\"Name\":\"1\",\"PropertyId\":3271,\"PropertyName\":\"出版时间\",\"diy_type\":0}],\"449\":[{\"Value\":0,\"Name\":\"1\",\"PropertyId\":449,\"PropertyName\":\"作者\",\"diy_type\":0}],\"501\":[{\"Value\":7310,\"Name\":\"否\",\"PropertyId\":501,\"PropertyName\":\"是否是套装\",\"diy_type\":0}],\"855\":[{\"Value\":0,\"Name\":\"陕西人民教育出版社\",\"PropertyId\":855,\"PropertyName\":\"出版社名称\",\"diy_type\":0}]}",
    "product_id": "3539925204033339668",
    "product_id_str": "3539925204033339668",
    "quality_list": [
      {
        "quality_attachments": [
          {
            "media_type": "1",
            "url": "http://www.byted***.com/YYYY"
          }
        ],
        "quality_key": "3457***9470978",
        "quality_name": "进货凭证"
      }
    ],
    "recommend_remark": "真的很好啊",
    "spec_id": "1",
    "spec_pics": [
      {
        "pic": "temai/b637513c50b994f4c89de56a17886caca5d6569awww800-800",
        "spec_detail_id": "1695459998447656"
      }
    ],
    "spec_prices": [
      {
        "code": "aaa",
        "customs_report_info": {
          "bar_code": "-",
          "first_measure_qty": "1",
          "first_measure_unit": "-",
          "g_model": "-",
          "hs_code": "1564564",
          "report_brand_name": "-",
          "report_name": "-",
          "second_measure_qty": "1",
          "second_measure_unit": "-",
          "unit": "-",
          "usage": "-"
        },
        "lock_step_stock_num": "1",
        "lock_stock_num": "1",
        "out_sku_id": "0",
        "outer_sku_id": "0",
        "presell_delay": "5",
        "price": "102",
        "prom_step_stock_num": "0",
        "prom_stock_num": "0",
        "promotion_step_stock_num": "0",
        "promotion_stock_num": "0",
        "sku_id": "1695459998495774",
        "sku_type": "0",
        "spec_detail_id1": "1695459998494734",
        "spec_detail_id2": "1695459998494734",
        "spec_detail_id3": "0",
        "spec_detail_ids": "[1695459998494734, 1695459998494766]",
        "step_stock_num": "0",
        "stock_num": "13",
        "stock_num_map": {},
        "supplier_id": "123",
        "tax_exemption_sku_info": {
          "is_suit": "1",
          "suit_num": "10",
          "volume": "100"
        }
      }
    ],
    "specs": [
      {
        "id": "1713023986705415",
        "is_leaf": "0",
        "name": "颜色",
        "pid": "1713023986705415",
        "spec_id": "1713023983665214",
        "values": [
          {
            "id": "1695459998447656",
            "is_leaf": "1",
            "name": "红色",
            "pid": "1695459998447640",
            "spec_id": "1713023983665214",
            "status": "1"
          }
        ]
      }
    ],
    "standard_brand_id": "121354",
    "status": "1",
    "update_time": "2021-03-29T15:52:52+08:00"
  },
  "err_no": 0,
  "message": "success",
  "code": 10000,
  "msg": "success",
  "sub_code": "",
  "sub_msg": ""
}
~~~
- 一定要POST店铺唯一值，这样系统才会判断是哪个店铺发起的请求

### 消息推送
~~~python
# 在views.py
from douyin.views.notify import NotifyAPI

class Notify(NotifyAPI):
    def __init__(self):
        self.params = {}

# urls.py
from django.urls import path
from .views import Notify

urlpatterns = [
    path(r'notify/', Notify.as_view({"post": "create"}), name="notify")
]
~~~
- 接下来只要向这个接口POST一个之前提到的店铺唯一值，"t_code" 就可以获取数据
- 一定要POST店铺唯一值，这样系统才会判断是哪个店铺发起的请求

### 对应的接口列表
<html>
 <head>
     <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
     <title>excel转html by toolscat.com</title>
 </head>
<body style="">
<div>
  <table style="border-collapse:collapse;background-color: white" width="100%">
 <tbody>
  <tr height="13.5px">
   <td valign="bottom" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">api文件夹名</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">文件名</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">类名</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">对应的api</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">对应的api链接</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="3" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BIC_API</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">orderCode_batchGetOrderCodeByShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderCodeBatchGetOrderCodeByShops</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/orderCode/batchGetOrderCodeByShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/51/688</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">orderCode_downloadOrderCodeByShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderDownatchGetOrderCodeByShops</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/orderCode/downloadOrderCodeByShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/51/479</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">orderCode_erpShopBindOrderCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderCodeErpShopBinOrderCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/orderCode/erpShopBindOrderCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/51/806</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="6" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BTAS_API</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">btas_getInspectionOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BtasGetInspectionOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/btas/getInspectionOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/49/473</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">btas_getOrderInspectionResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BtasGetOrderInspectionResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/btas/getOrderInspectionResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/49/573</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">btas_listBrand</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BtasListBrand</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/btas/listBrand</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/49/575</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">btas_saveInspectionInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BtassaveInspectionInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/btas/saveInspectionInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/49/574</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">btas_saveInspectionOnline</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BtassaveInspectionOnline</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/btas/saveInspectionOnline</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/49/572</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">btas_shipping</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BtasShipping</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/btas/shipping</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/49/489</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="29" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">wu_liu_fa_huo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">address_getAreasByProvince</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AddressgetAreasByProvince</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/address/getAreasByProvince</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/334</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">address_getProvince</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AddressgetProvince</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/address/getProvince</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/336</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">crossborder_orderCustomClearance</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CrossorderCustomClearance</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/crossborder/orderCustomClearance</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/527</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">crossBorder_orderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CrossBorderorderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/crossBorder/orderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/528</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">crossBorder_orderOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CrossBorderOrderOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/crossBorder/orderOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/526</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">dutyFree_orderOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">DutyFreeorderOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/dutyFree/orderOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/714</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_appendSubOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticsappendSubOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/appendSubOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/1075</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_cancelOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticcancelOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/cancelOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/397</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_createSFOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticcreateSFOrde</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/createSFOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/486</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_deliveryNotice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticsdeliveryNotice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/deliveryNotice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/1578</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_getCustomTemplateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticsgetCustomTemplateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/getCustomTemplateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/785</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_getOutRange</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticsgetOutRange</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/getOutRange</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/327</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_getShopKey</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticsgetShopKey</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/getShopKey</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/478</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_listShopNetsite</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticlistShopNetsite</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/listShopNetsite</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/576</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_newCreateOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticsnewCreateOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/newCreateOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/1339</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_templateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticstemplateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/templateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/476</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_trackNoRouteDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticstrackNoRouteDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/trackNoRouteDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/784</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_updateOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticsupdateOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/updateOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/494</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">logistics_waybillApply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">LogisticswaybillApply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/logistics/waybillApply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/490</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_logisticsAdd</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderlogisticsAdd</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/logisticsAdd</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/718</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_logisticsAddMultiPack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderlogisticsAddMultiPack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/logisticsAddMultiPack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/562</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_logisticsAddSinglePack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderlogisticsAddSinglePack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/logisticsAddSinglePack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/563</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_logisticsCompanyList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderlogisticsCompanyList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/logisticsCompanyList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/541</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_logisticsEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderlogisticsEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/logisticsEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/390</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_logisticsEditByPack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderlogisticsEditByPack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/logisticsEditByPack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/539</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">power_pushCustomSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">PowerpushCustomSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/power/pushCustomSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/1486</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">power_pushFirstSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">PowerpushFirstSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/power/pushFirstSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/1488</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">power_pushSecondSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">PowerpushSecondSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/power/pushSecondSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/1484</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">power_pushThirdSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">PowerpushThirdSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/power/pushThirdSortCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/16/1485</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="15" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">cang_ku_zuo_ye</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">storage_notifySaleReturnStatus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">StorageNotifySaleReturnStatus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/storage/notifySaleReturnStatus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/538</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">wms_inboundDetailNotify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WMSInboundDetailNotify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/wms/inboundDetailNotify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/1357</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">wms_outboundDetailNotify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WMSOutnboundDetailNotify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/wms/outboundDetailNotify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/941</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_adjustInventory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YuncAdjustInventory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/adjustInventory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/930</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_cancelOutboundOrderToB</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YunccannelOutboundOrderToB</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/cancelOutboundOrderToB</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/745</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_cerpCargoSinglePush</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WMSdlieryInfoNotify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/erpCargoSinglePush</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/932</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_cloudCancelInboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YunccloudCannelInboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/cloudCancelInboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/931</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_cloudCreateInboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YuncCloudCancelOutboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/cloudCancelOutboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/873</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_cloudCreateOutboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YunccloudCreateInboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/cloudCreateInboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/872</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_createOutboundOrderToB</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YunccloudCreateOutboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/cloudCreateOutboundOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/898</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_erpInboundCancel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YuncErpInboundCancel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/erpInboundCancel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/928</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_erpInboundCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YuncErpInboundCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/erpInboundCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/899</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_pushOutboundFeedback</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YuncPushOutboundFeedback</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/pushOutboundFeedback</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/842</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_shopWarehouseRefQuery</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YuncshopWarehouseRefQuery</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/shopWarehouseRefQuery</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/839</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">yunc_wmsInboundCallback</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">YuncWmsInboundCallback</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/yunc/wmsInboundCallback</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/50/929</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="12" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">dai_fa</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_orderInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopOrderInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/orderInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/678</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_orderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/orderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/673</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_roleGet</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IoproleGet</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/roleGet</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/672</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_sellerCancleDistribute</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopsellerCancleDistribute</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/sellerCancleDistribute</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/962</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_sellerDistribute</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopsellerDistribute</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/sellerDistribute</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/958</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_sellerOrderInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopSellerOrderInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/sellerOrderInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/959</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_sellerOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopSellerOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/sellerOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/960</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_sellerSupplierList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopSellerSupplierList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/sellerSupplierList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/961</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_waybillCancel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopwaybillCancel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/waybillCancel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/675</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_waybillGet</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopWaybillGet</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/waybillGet</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/674</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_waybillReturn</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopWaybillReturn</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/waybillReturn</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/676</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">iop_waybillUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">IopWaybillUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/iop/waybillUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/59/677</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="6" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ka_juan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">coupons_abandon</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CouponsAbandont</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/coupons/abandon</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/52/669</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">coupons_cancelVerify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CouponsCancelVerify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/coupons/cancelVerify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/52/668</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">coupons_certVerifyUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CouponsCertVerifyUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/coupons/certVerifyUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/52/900</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">coupons_list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CouponsList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/coupons/list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/52/369</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">coupons_syncV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CouponsSyncV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/coupons/syncV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/52/712</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">coupons_verifyV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CouponsVerifyV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/coupons/verifyV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/52/797</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="32" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">shang_pin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">brand_convert</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BrandConvert</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/brand/convert</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/1500</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">brand_getSug</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BrandGetSug</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/brand/getSug</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/1436</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">brand_list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BrandList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/brand/list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/1267</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">freightTemplate_list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">FreightTemplateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/freightTemplate/list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/565</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">opptyProduct_applyopptyProduct_apply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OpptyProductApply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/opptyProduct/apply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/738</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">opptyProduct_clue</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OpptyProductClue</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/opptyProduct/clue</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/739</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">opptyProduct_getApplyProgress</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OpptyProductGetApplyProgress</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/opptyProduct/getApplyProgress</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/740</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_addCbProduct</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductAddCbProduct</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/addCbProduct</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/499</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_addV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductAddV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/addV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/249</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_del</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductDel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/del</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/61</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_detail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/detail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/56</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_editBuyerLimit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductEditBuyerLimit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/editBuyerLimit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/262</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_editCbProduct</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductEditCbProduct</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/editCbProduct</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/553</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_editV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductEditV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/editV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/250</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_getCatePropertyV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductGetCatePropertyV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/getCatePropertyV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/1373</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_getProductUpdateRule</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;"> ProductGetProductUpdateRule</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/getProductUpdateRule</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/1614</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_listV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductListV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/listV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/633</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_qualificationConfig</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductQualificationConfig</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/qualificationConfig</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/1382</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_qualityDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductQualityDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/qualityDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/939</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_qualityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;"> ProductQualityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/qualityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/938</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_qualityTask</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductQualityTask</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/qualityTask</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/937</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_setOffline</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductSetOffline</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/setOffline</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/252</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">product_setOnline</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ProductSetOnline</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/product/setOnline</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/251</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">promise_deliveryList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">PromiseDeliveryList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/promise/deliveryList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/1529</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sku_detail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SkuDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sku/detail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/566</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sku_editCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SkuEditCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sku/editCode</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/86</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sku_editPrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SkuEditPrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sku/editPrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/84</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sku_list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SkuList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sku/list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/82</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sku_syncStockBatch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SkuSyncStockBatch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sku/syncStockBatch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/298</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">spu_getKeyPropertyByCid</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SpuGetKeyPropertyByCid</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/spu/getKeyPropertyByCid</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/642</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">spu_getSpuInfoBySpuId</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SpuGetSpuInfoBySpuId</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/spu/getSpuInfoBySpuId</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/643</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">spu_getSpuTpl</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;"> SpuGetSpuTpl</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/spu/getSpuTpl</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/14/644</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="10" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">hui_shou_ji_mai</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">recycle_buyerGetOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">RecycleBuyerGetOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/recycle/buyerGetOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/914</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">recycle_buyerGetOrderDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">RecycleBuyerGetOrderDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/recycle/buyerGetOrderDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/915</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">recycle_createPrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">RecycleCreatePrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/recycle/createPrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/904</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">recycle_changePrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">RecycleChangePrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/recycle/changePrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/908</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">recycle_qualityTestingResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">RecycleQualityTestingResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/recycle/qualityTestingResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/907</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">recycle_applyChangePrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">RecycleApplyChangePrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/recycle/applyChangePrice</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/909</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">recycle_confirmReceive</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">RecycleConfirmReceive</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/recycle/confirmReceive</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/906</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">recycle_sellSucceed</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">RecycleSellSucceed</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/recycle/sellSucceed</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/910</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">recycle_logisticsBack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">RecycleLogisticsBack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/recycle/logisticsBack</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/911</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">shop_setFinalPayment</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ShopSetFinalPayment</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/shop/setFinalPayment</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/68/1659</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="14" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">shou_hou_tui_kuan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_operate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/operate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/560</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_Detail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/Detail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/1095</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_List</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/List</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/1295</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_addOrderRemark</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleAddOrderRemark</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/addOrderRemark</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/585</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_OpenAfterSaleChannel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleOpenAfterSaleChannel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/OpenAfterSaleChannel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/764</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_submitEvidence</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleSubmitEvidence</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/submitEvidence</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/255</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_buyerExchangeConfirm</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleBuyerExchangeConfirm</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/buyerExchangeConfirm</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/768</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_applyLogisticsIntercept</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleApplyLogisticsIntercept</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/applyLogisticsIntercept</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/897</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_CancelSendGoodsSuccess</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleCancelSendGoodsSuccess</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/CancelSendGoodsSuccess</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/816</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_returnGoodsToWareHouseSuccess</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleReturnGoodsToWareHouseSuccess</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/returnGoodsToWareHouseSuccess</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/815</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">trade_refundListSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">TradeRefundListSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/trade/refundListSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/254</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_timeExtend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleTimeExtend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/timeExtend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/770</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_buyerExchange</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleBuyerExchange</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/buyerExchange</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/769</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">afterSale_rejectReasonCodeList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AfterSaleRejectReasonCodeList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/afterSale/rejectReasonCodeList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/17/1540</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="7" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">dian_pu</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">address_update</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AddressUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/address/update</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/13/1511</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">shop_brandList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ShopBrandList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/shop/brandList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/13/54</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">antispam_userLogin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AntispamUserLogin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/antispam/userLogin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/13/635</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">shop_getShopCategory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ShopGetShopCategory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/shop/getShopCategory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/13/821</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">address_create</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AddressCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/address/create</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/13/1510</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">member_getShopShortLink</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MemberGetShopShortLink</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/member/getShopShortLink</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/13/1455</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">address_list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AddressList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/address/list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/13/1435</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="40" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ding_dan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_earchList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderSearchList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/searchList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/1342</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_orderDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderOrderDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/orderDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/1343</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_batchDecrypt</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderBatchDecrypt</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/batchDecrypt</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/982</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_addOrderRemark</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderAddOrderRemark</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/addOrderRemark</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/568</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_updatePostAmount</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderUpdatePostAmount</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/updatePostAmount</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/264</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_AddressAppliedSwitch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderAddressAppliedSwitch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/AddressAppliedSwitch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/500</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_updateOrderAmount</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderUpdateOrderAmount</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/updateOrderAmount</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/263</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_addressModify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderAddressModify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/addressModify</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/290</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_addressConfirm</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderAddressConfirm</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/addressConfirm</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/505</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_addresSwitchConfig</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderAddresSwitchConfig</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/addresSwitchConfig</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/501</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_invoiceList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderInvoiceList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/invoiceList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/660</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_batchEncrypt</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderBatchEncrypt</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/batchEncrypt</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/487</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_batchSensitive</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderBatchSensitive</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/batchSensitive</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/508</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_invoiceUpload</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderInvoiceUpload</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/invoiceUpload</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/892</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_BatchSearchIndex</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderBatchSearchIndex</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/BatchSearchIndex</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/516</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">antispam_orderSend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AntispamOrderSend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/antispam/orderSend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/649</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">antispam_orderQuery</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AntispamOrderQuery</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/antispam/orderQuery</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/650</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_getCrossBorderFulfillInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderGetCrossBorderFulfillInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/getCrossBorderFulfillInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/495</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_getServiceList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderGetServiceList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/getServiceList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/266</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_addSerialNumber</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderAddSerialNumber</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/addSerialNumber</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/1289</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_replyService</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderReplyService</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/replyService</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/75</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_serviceDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderServiceDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/serviceDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/253</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_ordeReportList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderOrdeReportList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/ordeReportList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/1550</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">freightTemplate_update</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">FreightTemplateUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/freightTemplate/update</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/1662</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">freightTemplate_create</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">FreightTemplateCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/freightTemplate/create</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/1661</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">coupons_extendCertValidEndByOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CouponsExtendCertValidEndByOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/coupons/extendCertValidEndByOrder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/15/1730</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_template_apply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsTemplate/apply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/template/apply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1527</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_public_template</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsPublicTemplate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/public/template</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1526</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_sign_apply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsSignApply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/sign/apply</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1525</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_template_revoke</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsTemplateRevoke</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/template/revoke</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1524</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_sign_apply_list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsSignApplyList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/sign/apply/list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1523</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_send</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsSend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/send</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1522</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_batchSend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsBatchSend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/batchSend</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1521</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_sign_delete</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsSignDelete</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/sign/delete</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1520</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_sign_apply_revoke</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsSignApplyRevoke</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/sign/apply/revoke</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1519</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_template_delete</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsTemplateDelete</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/template/delete</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1518</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_sendResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsSendResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/sendResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1517</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_template_apply_list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsTemplateApplyList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/template/apply/list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1516</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_sign_search</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsSignSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/sign/search</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1515</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sms_template_search</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SmsTemplateSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sms/template/search</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/163/1514</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="2" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">gong_ju</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">token_refresh</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">TokenRefresh</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/token/refresh</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/162/1601</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">token_create</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">TokenCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/token/create</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/162/1600</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="56" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">jing_xuan_lian_meng</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_simplePlan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinSimplePlan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/simplePlan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/923</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_exclusivePlan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinExclusivePlan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/exclusivePlan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/922</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_activitySearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinActivitySearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/activitySearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/743</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_ShopActivityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinShopActivityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/ShopActivityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1671</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_applyActivities</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinApplyActivities</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/applyActivities</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/744</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_activityProductExtendList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinActivityProductExtendList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/activityProductExtendList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1674</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_activityProductExtendApprove</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinActivityProductExtendApprove</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/activityProductExtendApprove</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1673</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_createOrUpdateOrienPlan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinCreateOrUpdateOrienPlan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/createOrUpdateOrienPlan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/708</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_orienPlanAuthorsAdd</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinOrienPlanAuthorsAdd</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/orienPlanAuthorsAdd</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/706</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_orienPlanList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinOrienPlanList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/orienPlanList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/705</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_orienPlanAuthors</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinOrienPlanAuthors</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/orienPlanAuthors</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/709</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_orienPlanCtrl</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinOrienPlanCtrl</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/orienPlanCtrl</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/704</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_orienPlanAudit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinOrienPlanAudit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/orienPlanAudit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/707</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_colonelActivityCreateOrUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceColonelActivityCreateOrUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/colonelActivityCreateOrUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/966</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_activityProductCategoryList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceActivityProductCategoryList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/activityProductCategoryList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/970</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_instituteColonelActivityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceInstituteColonelActivityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/instituteColonelActivityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1330</td>
  </tr>
  <tr height="27.0px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_instituteColonelActivityOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceInstituteColonelActivityOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/instituteColonelActivityOperate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/972</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_colonelActivityProduct</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceColonelActivityProduct</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/colonelActivityProduct</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/968</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_colonelActivityProductAudit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceColonelActivityProductAudit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/colonelActivityProductAudit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/971</td>
  </tr>
  <tr height="27.0px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_colonelActivityProductExtension</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceColonelActivityProductExtension</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/colonelActivityProductExtension</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/967</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_colonel/specialApplyList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinColonelSpecialApplyList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/colonel/specialApplyList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1552</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_colonel/specialApplyDeal</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinColonelSpecialApplyDeal</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/colonel/specialApplyDeal</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1553</td>
  </tr>
  <tr height="27.0px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_originColonelEnrollableActivityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinOriginColonelEnrollableActivityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/originColonelEnrollableActivityList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1675</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_colonelActivityDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinColonelActivityDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/colonelActivityDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1670</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_originColonelUnappliedProductList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinOriginColonelUnappliedProductList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/originColonelUnappliedProductList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1677</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_originColonelApplyActivities</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinOriginColonelApplyActivities</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/originColonelApplyActivities</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1672</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_materialsProductsSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceMaterialsProductsSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/materialsProductsSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/924</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_materialsProductsDetails</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceMaterialsProductsDetails</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/materialsProductsDetails</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1356</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_productSkus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinProductSkus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/productSkus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1626</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_materialsProductCategory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceMaterialsProductCategory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/materialsProductCategory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/637</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_materialsProductStatus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinMaterialsProductStatus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/materialsProductStatus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1497</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_kolMaterialsProductsDetails</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinKolMaterialsProductsDetails</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/kolMaterialsProductsDetails</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1589</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_queryInstituteOrders</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinQueryInstituteOrders</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/queryInstituteOrders</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1398</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_instituteOrderMCN</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstituteOrderMCN</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/instituteOrderMCN</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1602</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_instituteOrderColonel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstituteOrderColonel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/instituteOrderColonel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1603</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_instPickSourceConvert</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstPickSourceConvert</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/instPickSourceConvert</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1454</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_instGmv</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstGmv</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/instGmv</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1652</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_instGmvDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstGmvDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/instGmvDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1653</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_kolPidCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinKolPidCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/kolPidCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1460</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_kolPidList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinKolPidList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/kolPidList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1461</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_kolPidEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinKolPidEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/kolPidEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1462</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_kolPidDel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinKolPidDel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/kolPidDel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1463</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_kolProductShare</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinKolProductShare</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/kolProductShare</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1464</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_getProductShareMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinGetProductShareMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/getProductShareMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1588</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_institutePidCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstitutePidCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/institutePidCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1273</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_institutePidList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstitutePidList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/institutePidList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1269</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_institutePidEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstitutePidEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/institutePidEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1270</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_institutePidDel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstitutePidDel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/institutePidDel</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1271</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_liveShareMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinLiveShareMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/liveShareMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1396</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_instituteLiveShare</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstituteLiveShare</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/instituteLiveShare</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1297</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_instituteOrderAds</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinInstituteOrderAds</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/instituteOrderAds</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1296</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_kolOrderAds</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinKolOrderAds</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/kolOrderAds</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1459</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_shopPidMemberCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinShopPidMemberCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/shopPidMemberCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1493</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_shareCommandParse</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinShareCommandParse</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/shareCommandParse</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1726</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_kolMaterialsProductsSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinKolMaterialsProductsSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/kolMaterialsProductsSearch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1725</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">buyin_kolLiveShare</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">BuyinKolLiveShare</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/buyin/kolLiveShare</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/61/1724</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="13" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">ku_cun</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sku_stockNum</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SkuStockNum</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sku/stockNum</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/936</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">sku_syncStock</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">SkuSyncStock</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/sku/syncStock</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/155</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">promise_setSkuShipTime</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">PromiseSetSkuShipTime</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/promise/setSkuShipTime</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/569</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_create</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseCreate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/create</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/691</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_edit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseEdit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/edit</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/692</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_setAddr</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseSetAddr</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/setAddr</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/697</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_createBatch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseCreateBatch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/createBatch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/695</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_setAddrBatch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseSetAddrBatch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/setAddrBatch</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/696</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_setPriority</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseSetPriority</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/setPriority</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/698</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_removeAddr</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseRemoveAddr</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/removeAddr</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#800080;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/699</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_adjustInventory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseAdjustInventory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/adjustInventory</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/760</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/list</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/693</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">warehouse_info</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">WarehouseInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/warehouse/info</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/34/694</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="8" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">kua_jing</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">dutyFree_orderConfirm</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">DutyFreeOrderConfirm</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/dutyFree/orderConfirm</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/53/702</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">dutyFree_orderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">DutyFreeOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/dutyFree/orderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/53/703</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">crossborder_stockTaking</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CrossborderStockTaking</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/crossborder/stockTaking</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/53/883</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">crossborder_stockTransform</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CrossborderStockTransform</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/crossborder/stockTransform</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/53/918</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">crossborder_OrderInterception</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CrossborderOrderInterception</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/crossborder/OrderInterception</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/53/920</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">crossborder_takingLogisticsInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CrossborderTakingLogisticsInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/crossborder/takingLogisticsInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/53/1293</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">crossborder_warehouseInOutboundEvent</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CrossborderWarehouseInOutboundEvent</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/crossborder/warehouseInOutboundEvent</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/53/1205</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">crossBorder_getTradeOrderStatus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">CrossBorderGetTradeOrderStatus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/crossBorder/getTradeOrderStatus</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/53/1650</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="18" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">su_cai_zhong_xin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_createFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialCreateFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/createFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/946</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_editFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialEditFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/editFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/948</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_moveFolderToRecycleBin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialMoveFolderToRecycleBin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/moveFolderToRecycleBin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/947</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_moveMaterialToRecycleBin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialMoveMaterialToRecycleBin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/moveMaterialToRecycleBin</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/951</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_recoverMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialRecoverMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/recoverMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/954</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_editMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialEditMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/editMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/956</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_batchUploadVideoAsync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialBatchUploadVideoAsync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/batchUploadVideoAsync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1617</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_batchUploadImageSync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialBatchUploadImageSync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/batchUploadImageSync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1616</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_getFolderInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialGetFolderInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/getFolderInfo</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1150</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_searchFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialSearchFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/searchFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1149</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_searchMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialSearchMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/searchMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1148</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_uploadVideoAsync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialUploadVideoAsync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/uploadVideoAsync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1147</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_uploadImageSync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialUploadImageSync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/uploadImageSync</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1146</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_queryMaterialDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialQueryMaterialDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/queryMaterialDetail</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1145</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_deleteFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialDeleteFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/deleteFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1139</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_deleteMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialDeleteMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/deleteMaterial</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1138</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_recoverFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialRecoverFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/recoverFolder</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1096</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">material_get_cap_info</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MaterialGet_cap_info</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/material/get_cap_info</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/69/1694</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="2" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">xu_ni_chong_zhi</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">topup_result</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">TopupResult</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/topup/result</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/164/1639</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">topup_accountTemplateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">TopupAccountTemplateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/topup/accountTemplateList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/164/1638</td>
  </tr>
  <tr height="13.5px">
   <td rowspan="8" colspan="1" valign="center" style="font-weight:400;font-size: 11px;width:4704px;text-align:center;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">zhang_dan</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">alliance_getOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">AllianceGetOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/alliance/getOrderList</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/46/469</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">member_batchUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">MemberBatchUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/member/batchUpdate</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/46/329</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_downloadShopAccountItemFile</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderDownloadShopAccountItemFile</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/downloadShopAccountItemFile</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/46/1433</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_downloadShopAccountItem</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderDownloadShopAccountItem</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/downloadShopAccountItem</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/46/1431</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_getShopAccountItem</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderGetShopAccountItem</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/getShopAccountItem</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/46/1430</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_getSettleBillDetailV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderGetSettleBillDetailV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/getSettleBillDetailV2</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/46/1390</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_downloadToShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderDownloadToShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/downloadToShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/46/1193</td>
  </tr>
  <tr height="13.5px">
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">order_downloadSettleItemToShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9504px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">OrderDownloadSettleItemToShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:9792px;text-align:left;color:#000000;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">/order/downloadSettleItemToShop</td>
   <td valign="center" style="font-weight:400;font-size: 11px;width:13216px;text-align:left;color:#0000FF;border-top:solid #000000 1px;border-right:solid #000000 1px;border-bottom:solid #000000 1px;border-left:solid #000000 1px;">https://op.jinritemai.com/docs/api-docs/46/1191</td>
  </tr>
 </tbody>
</table>
</div>
</body>
</html>

