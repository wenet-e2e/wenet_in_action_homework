import wenetruntime as wenet
import wave

wenet.set_log_level(1)

model_dir = './model'
decoder = wenet.Decoder(model_dir, continuous_decoding=False)

with wave.open('slice.wav', 'rb') as fin:
    assert fin.getnchannels() == 1
    wav = fin.readframes(fin.getnframes())

# We suppose the wav is 16k, 16bits, and decode every 0.5 seconds
interval = int(0.5 * 16000) * 2
for i in range(0, len(wav), interval):
    last = False if i + interval < len(wav) else True
    chunk_wav = wav[i: min(i + interval, len(wav))]
    ans = decoder.decode(chunk_wav, last)
    print(ans)
