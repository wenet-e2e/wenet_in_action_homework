import sys
import wenetruntime as wenet

wenet.set_log_level(1)

model_dir = sys.argv[1]
wav_file = sys.argv[2]
decoder = wenet.Decoder(model_dir)
ans = decoder.decode_wav(wav_file)
print(ans)
