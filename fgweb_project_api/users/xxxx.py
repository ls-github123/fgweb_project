import base64, json, time, hashlib

# 第一部分内容
header_data = {"typ":"jwt","alg":"HS256"}
# print(type(header_data))
# # # 转换成json格式的字符串
# jo = json.dumps(header_data)
# print(type(jo))
# print(jo)
# # # 将字符串转换成字节形式
# jo_encode = jo.encode()
# print(jo_encode)
# # # 将字节数据进行base64编码
# bs = base64.b64encode(jo_encode)
# print(bs)

# jwt_hd = bs.decode()
# print(jwt_hd)

# header = base64.b64encode(json.dumps(header_data).encode()).decode()
# print(header)

header = base64.b64encode(json.dumps(header_data).encode()).decode()
print(header)

# 获取当前时间戳
current_time = time.time()

payload_data = {
    "sub":"admin",
    "exp":current_time+(60*60),
    "nbf":current_time,
    "name":"admin",
    "user_id":1,
    "mobile":"18090001999"
}

# base64转码后结果
# cookie sindcookie
# 需要字节类型数据 (pythoh没有字节数据类型) 字典转成字符串:json
# 把字符串转成字节 字节转成字符串
payloads =base64.b64encode(json.dumps(payload_data).encode()).decode()
print(payloads)


# 生成签证部分
# 密钥:django项目中的settings中随机生成密钥
# 密钥不能泄漏
SECRET_KEY = 'django-insecure-pefco&-*6-$hr&+!6xa)7&v9cxyxrf$igv7g)5ly3^g0@o-@zy'
data = header+payloads+SECRET_KEY

# 获取加密对象, hs256
HS256 = hashlib.sha256()
HS256.update(data.encode('utf-8'))
signatrue = HS256.hexdigest()
print(f'签证数据:{signatrue}')


# 头部、载荷部分、签证部分
token = f"{header}.{payloads}.{signatrue}"
print('----------------')
print(token)