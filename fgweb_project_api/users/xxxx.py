import base64,json

# 第一部分内容
header_data = {"typ":"jwt","alg":"HS256"}
print(type(header_data))
# # 转换成json格式的字符串
jo = json.dumps(header_data)
print(type(jo))
print(jo)
# # 将字符串转换成字节形式
jo_encode = jo.encode()
print(jo_encode)
# # 将字节数据进行base64编码
bs = base64.b64encode(jo_encode)
print(bs)

jwt_hd = bs.decode()
print(jwt_hd)

header = base64.b64encode(json.dumps(header_data).encode()).decode()
print(header)