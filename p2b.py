"""
Convert a picture to base64 string.
"""
import base64

# 二进制方式打开图文件
f = open('Deep-Learning-with-PyTorch-cover.jpg', 'rb')

# 读取文件内容，转换为base64编码
ls_f = base64.b64encode(f.read())

# 关闭图文件
f.close()

# 输出base64格式的图文件
print(ls_f)