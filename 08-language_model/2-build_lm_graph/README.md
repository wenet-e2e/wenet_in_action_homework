# 构图示例

1. 编译 wenet runtime

``` bash
cd YOUR_WENET_DIR/runtime/libtorch
mkdir build && cd build && cmake -DGRAPH_TOOLS=ON .. && cmake --build .
```

2. 导入环境变量

``` bash
export WENET_DIR=YOUR_WENET_DIR
export BUILD_DIR=${WENET_DIR}/runtime/libtorch/build
export OPENFST_PREFIX_DIR=${BUILD_DIR}/../fc_base/openfst-subbuild/openfst-populate-prefix
export PATH=$PWD:${BUILD_DIR}/bin:${BUILD_DIR}/kaldi:${OPENFST_PREFIX_DIR}/bin:$PATH
```

3. 构图

``` bash
bash run.sh
```

4. 查看构图和可视化结果

 * graph: 生成构图的目录
 * pdf: 可视化 pdf 目录
