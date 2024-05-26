# 端口号可能会改变
import json
import requests
import io
import base64
from PIL import Image
import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

url = "http://127.0.0.1:7860"

def web_ui_api(inprompt):
    prompt =inprompt+ "1boy,Brown hair,warrior,Under the streetlights,A calm expression,(full body shot), <lora:Loraeyes_V1:1>"
    negative_prompt = "badhandv4,easynegative"

    payload = {

        # 模型设置
        "override_settings": {
            "sd_model_checkpoint": "counterfeitV30_v30.safetensors",
            "sd_vae": "Automatic",
            "CLIP_stop_at_last_layers": 2,
        },

        # 基本参数
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "steps": 50,
        "sampler_name": "DPM++ 2M Karras",
        "width": 512,
        "height": 720,
        "batch_size": 1,
        "n_iter": 1,
        "seed": 1,
        "CLIP_stop_at_last_layers": 2,

        # 面部修复 face fix
        "restore_faces": False,

        # 高清修复 highres fix
        # "enable_hr": True,
        # "denoising_strength": 0.4,
        # "hr_scale": 2,
        # "hr_upscaler": "Latent",

    }

    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))
    # image_path = os.path.join(PROJECT_ROOT, 'DB',f'{prompt}.png')
    image_path = os.path.join(PROJECT_ROOT, 'DB',f'{inprompt}.png')
    image.show()
    image.save(image_path)
# inprompt = "{bestquality}"
# web_ui_api(inprompt)