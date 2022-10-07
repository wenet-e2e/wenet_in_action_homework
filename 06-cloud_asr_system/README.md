# 搭建云端语音识别系统

1. 准备模型：分别下载预编训练好的模型文件。

```
wget https://wenet-1256283475.cos.ap-shanghai.myqcloud.com/models/aishell/20210601_u2%2B%2B_conformer_libtorch.tar.gz
tar zxvf 20210601_u2++_conformer_libtorch.tar.gz
mkdir -p model
cp 20210601_u2++_conformer_libtorch/* model
```

2. 编译 runtime 后，启动 ASR 服务

```
export GLOG_logtostderr=1
export GLOG_v=2
model_dir=model
./build/bin/websocket_server_main \
    --port 10086 \
    --chunk_size 16 \
    --model_path $model_dir/final.zip \
    --unit_path $model_dir/units.txt 2>&1 | tee server.log
```

3. 实现客户端 `client.py` 中的逻辑代码后，完成与服务端的通信

```
pip install -r requirements
python client.py
```