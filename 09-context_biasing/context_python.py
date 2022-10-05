import wenetruntime as wenet

wenet.set_log_level(1)

model_dir = './model'
# decoder = wenet.Decoder(model_dir)  # 不带 context
decoder = wenet.Decoder(model_dir, context=['停滞', '宋芳'], context_score=9.0)  # 带 context
ans = decoder.decode_wav('BAC009S0764W0121.wav')
print(ans)
ans = decoder.decode_wav('BAC009S0765W0133.wav')
print(ans)
