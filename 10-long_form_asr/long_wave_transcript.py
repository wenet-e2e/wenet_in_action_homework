import wenetruntime as wenet
from myvad import Vad
from multiprocessing import Pool

wenet.set_log_level(1)
decoder = wenet.Decoder('./model')  # 初始化解码器

vad = Vad()  # 初始化 VAD, 详请参考 https://github.com/wiseman/py-webrtcvad
segments = vad.process('./slice.wav')  # VAD 语音切分

def decode(segment):
    ans = decoder.decode(segment)
    print(ans)
    decoder.reset()
    return ans

with Pool(2) as p:  # 进程池并发解码
    all_ans = p.map(decode, segments)
    print(all_ans)


