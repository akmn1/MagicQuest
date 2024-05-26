# import torch
#
# print("是否可用：", torch.cuda.is_available())        # 查看GPU是否可用
# print("GPU数量：", torch.cuda.device_count())        # 查看GPU数量
# print("torch方法查看CUDA版本：", torch.version.cuda)  # torch方法查看CUDA版本
# print("GPU索引号：", torch.cuda.current_device())    # 查看GPU索引号
# print("GPU名称：", torch.cuda.get_device_name(1))    # 根据索引号得到GPU名称
import requests

url = 'http://localhost:5000/upload-folder'
# 文件部分
files = {'file': open(r"E:\MagicQuest\MagicQuest\DB\魔法少女.zip", 'rb')}
# 非文件表单字段部分
data = {'filename': 'test'}

response = requests.post(url, files=files, data=data)
print(response.text)

# 上传单个文件
# files = {'file': open(r"E:\MagicQuest\MagicQuest\DB\骑着扫帚的魔法少女.png",'rb')}
# response = requests.post(url, files=files)
# print(response.text)

