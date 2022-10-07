# runtime 设计框架

1. fork WeNet，使用 Github Actions 编译 WeNet 的 runtime。

2. 修改 `decoder/asr_decder.cc` 中的 `AttentionRescoring()` 函数，编译运行 & 输出原始分数和 rescore 分数。

``` c++
LOG(INFO) << result_[i].sentence;
LOG(INFO) << result_[i].score;
LOG(INFO) << rescoring_score[i];
```
