# 需要更改为列表输出
from funasr import AutoModel
import soundfile
import os

# 初始化模型
model = AutoModel(model="paraformer-zh-streaming")


def real_time_transcribe(audio_path):
    text_result = ''  # 用于累积完整的翻译结果
    chunk_size = [0, 10, 5]  # [0, 10, 5] 600ms, [0, 8, 4] 480ms
    encoder_chunk_look_back = 4  # number of chunks to look back for encoder self-attention
    decoder_chunk_look_back = 1  # number of encoder chunks to look back for decoder cross-attention

    # 读取音频文件
    speech, sample_rate = soundfile.read(audio_path)
    chunk_stride = chunk_size[1] * 960  # 600ms

    cache = {}
    total_chunk_num = int((len(speech) - 1) / chunk_stride + 1)

    for i in range(total_chunk_num):
        speech_chunk = speech[i * chunk_stride:(i + 1) * chunk_stride]
        is_final = i == total_chunk_num - 1
        res = model.generate(input=speech_chunk, cache=cache, is_final=is_final, chunk_size=chunk_size,
                             encoder_chunk_look_back=encoder_chunk_look_back,
                             decoder_chunk_look_back=decoder_chunk_look_back)

        # 累积每一块的转录结果
        if res and 'text' in res[0]:
            text_result += res[0]['text']
    #!!!!!!!!       在这里插入Qt显示的代码实现实时转录和显示

    return text_result.strip()  # 返回完整的翻译结果，并去除尾部的空格

# 使用函数进行实时转录
audio_file_path = r"E:\MagicQuest\MagicQuest\DB\audio_za1p36p7.wav"  # 确保这里的路径是音频文件路径
full_text = real_time_transcribe(audio_file_path)
print(full_text)  # 打印完整的转录结果
