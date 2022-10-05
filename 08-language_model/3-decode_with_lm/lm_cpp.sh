decoder_main=/home/binbzha/github/wenet/runtime/libtorch/build/bin/decoder_main
export GLOG_logtostderr=1
export GLOG_v=1
wav_path=BAC009S0764W0121.wav
model_dir=model
$decoder_main \
    --chunk_size 16 \
    --wav_path $wav_path \
    --model_path $model_dir/final.zip \
    --unit_path $model_dir/units.txt \
    --fst_path $model_dir/TLG.fst \
    --dict_path $model_dir/words.txt
