# 如何使用 srilm 训练语言模型？

1. 安装 srilm: 在 wenet 代码根目录下安装

``` bash
cd YOUR_WENET_DIR/tools
bash install_srilm.sh
```

2. 导入 srilm 环境变量

``` bash
source YOUR_WENET_DIR/tools/env.sh
```

3. 训练语言模型: 切换作业目录，这里使用 `train.txt` 作为训练语料

``` bash
bash run.sh
```

