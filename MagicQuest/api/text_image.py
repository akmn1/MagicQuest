# 这个模块是用来当主机服务器没能部署成功的替代方案
# 目前已经不再使用
from diffusers import StableDiffusionPipeline
import torch
import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# model_id = os.path.join(PROJECT_ROOT, 'runwayml')
model_id =r"E:\runwayml"

# 好的我们试试单浮点精度
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

# 生成图像
prompt = "a  girl with white hair, red eyes who under the sea"
image = pipe(prompt).images[0]

# 保存图像
# 指定保存图像的完整路径
image_path = os.path.join(PROJECT_ROOT, 'DB',f'{prompt}.png')
image.save(image_path)
