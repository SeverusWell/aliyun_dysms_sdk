阿里云 短信服务 SDK for Python3 
==

---

  本项目为阿里云短信(大鱼 dysms) SDK 针对 Python3 的优化版本,将官方 SDK 中的 SMS 短信部分提取出来合并为一个文件方便使用,变量名优化为Python3推荐命名规范,消除了代码中的飘黄.

详情参照:[官方帮助文档](https://help.aliyun.com/product/44282.html?spm=5176.12212976.0.0.25dc1cbe8wpUWh)



### 使用方式

#### 1. 安装阿里云 SDK 核心库

```
pip install aliyun-python-sdk-core
```

#### 2. 将 dysms.py 复制到您的项目中

#### 3. 配置您的云短信 ACCESS_KEY_ID 和 ACCESS_KEY_SECRET

```
ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID') or 'yourAccessKeyId'
ACCESS_KEY_SECRET = os.environ.get('ACCESS_KEY_SECRET') or 'yourAccessKeySecret'
```

#### 4. 开始使用

使用  send_sms 函数发送短信. (记得填写可用的签名和模板ID) ,params 为模板中的参数,调用时转换为字符串json.dumps(params)).

```
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
```

#### 5. 搞定 !

![](https://tva1.sinaimg.cn/large/006tNbRwly1gamz20gbtvj30ku11279e.jpg)