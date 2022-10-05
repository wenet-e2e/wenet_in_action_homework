# 热词解码示例

1. 准备模型：分别下载预编训练好的模型文件。

```
wget https://wenet-1256283475.cos.ap-shanghai.myqcloud.com/models/aishell/20210601_u2%2B%2B_conformer_libtorch.tar.gz
tar zxvf 20210601_u2++_conformer_libtorch.tar.gz
mkdir -p model
cp 20210601_u2++_conformer_libtorch/* model
```

2. 解码 python 版

``` sh
pip3 install wenetruntime
python context_python.py
```


3. 解码 c++ 版：请先修改 `lm_cpp.sh` 中 `decode_main` 的路径

``` sh
bash context_cpp.sh
```
