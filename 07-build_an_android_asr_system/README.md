# 搭建基于 android 的离线语音识别系统

1. fork WeNet，使用 Github Actions 编译 WeNet 的 android apk 和可执行文件。

2. 通过 `adb push` 将可执行文件发送到 android 手机，并且在 `adb shell` 中运行。
