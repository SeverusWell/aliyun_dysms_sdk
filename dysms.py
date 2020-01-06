# -*- coding: utf-8 -*-
"""
短信业务调用接口示例，版本号：v20170525

Created on 2017-06-12 aliyun

modify by Severus Well(thinkweiwei@msn.com ) on 2020-01-06
    Proper for python3.
"""

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


import json
import os
import uuid
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.request import RpcRequest

# ACCESS_KEY_ID/ACCESS_KEY_SECRET 根据实际申请的账号信息进行替换
ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID') or 'yourAccessKeyId'
ACCESS_KEY_SECRET = os.environ.get('ACCESS_KEY_SECRET') or 'yourAccessKeySecret'

# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.modify_point(PRODUCT_NAME, REGION, DOMAIN)


class SendSMSRequest(RpcRequest):

    def __init__(self):
        RpcRequest.__init__(self, 'Dysmsapi', '2017-05-25', 'SendSms')

    def get_template_code(self):
        return self.get_query_params().get('TemplateCode')

    def set_template_code(self, template_code):
        self.add_query_param('TemplateCode', template_code)

    def get_phone_numbers(self):
        return self.get_query_params().get('PhoneNumbers')

    def set_phone_numbers(self, phone_numbers):
        self.add_query_param('PhoneNumbers', phone_numbers)

    def get_sign_name(self):
        return self.get_query_params().get('SignName')

    def set_sign_name(self, sign_name):
        self.add_query_param('SignName', sign_name)

    def get_resource_owner_account(self):
        return self.get_query_params().get('ResourceOwnerAccount')

    def set_resource_owner_account(self, resource_owner_account):
        self.add_query_param('ResourceOwnerAccount', resource_owner_account)

    def get_template_param(self):
        return self.get_query_params().get('TemplateParam')

    def set_template_param(self, template_param):
        self.add_query_param('TemplateParam', template_param)

    def get_resource_owner_id(self):
        return self.get_query_params().get('ResourceOwnerId')

    def set_resource_owner_id(self, resource_owner_id):
        self.add_query_param('ResourceOwnerId', resource_owner_id)

    def get_owner_id(self):
        return self.get_query_params().get('OwnerId')

    def set_owner_id(self, owner_id):
        self.add_query_param('OwnerId', owner_id)

    def get_sms_up_extend_code(self):
        return self.get_query_params().get('SmsUpExtendCode')

    def set_sms_up_extend_code(self, sms_up_extend_code):
        self.add_query_param('SmsUpExtendCode', sms_up_extend_code)

    def get_out_id(self):
        return self.get_query_params().get('OutId')

    def set_out_id(self, out_id):
        self.add_query_param('OutId', out_id)


def send_sms(_business_id, _phone_numbers, _sign_name, _template_code, _template_param=None):
    sms_request = SendSMSRequest()
    # 申请的短信模板编码,必填
    sms_request.set_template_code(_template_code)

    # 短信模板变量参数
    if _template_param is not None:
        sms_request.set_template_param(_template_param)

    # 设置业务请求流水号，必填。
    sms_request.set_out_id(_business_id)

    # 短信签名
    sms_request.set_sign_name(_sign_name)

    # 数据提交方式
    # sms_request.set_method(MT.POST)

    # 数据提交格式
    # sms_request.set_accept_format(FT.JSON)

    # 短信发送的号码列表，必填。
    sms_request.set_phone_numbers(_phone_numbers)

    # 调用短信发送接口，返回json
    sms_response = acs_client.do_action_with_exception(sms_request)

    # TODO 业务处理

    return sms_response


if __name__ == '__main__':
    _business_id = uuid.uuid1()
    _phone_numbers = '18888888888'  # 接收人手机号码
    _sign_name = 'Your sign name'  # 签名
    _template_code = 'SMS_123456789'  # 短信模板ID
    params = {
        "username": "小可爱",
        "time": "2020-01-01",
        "msg": "啦啦啦2"
    }

    send_sms_resp = send_sms(_business_id, _phone_numbers, _sign_name, _template_code, json.dumps(params))
    print(send_sms_resp)
