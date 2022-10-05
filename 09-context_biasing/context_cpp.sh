decoder_main=/home/binbzha/github/wenet/runtime/libtorch/build/bin/decoder_main
export GLOG_logtostderr=1
export GLOG_v=1
wav_scp=wav.scp
model_dir=model
$decoder_main \
  --chunk_size 16 \
  --wav_scp $wav_scp \
  --model_path $model_dir/final.zip \
  --unit_path $model_dir/units.txt \
  --context_path context.txt \
  --context_score 9.0
