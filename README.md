# README

## 运行与使用

本说明文档介绍了如何运行和使用图像处理脚本。

### 运行环境
需要安装python3.10

首先，确保您的环境中安装了以下依赖库：

- PIL (Pillow)
- numpy
- opencv-python
- argparse

您可以使用以下命令来安装这些依赖：

```bash
pip install Pillow numpy opencv-python argparse
```

### 脚本使用方法

1. 打开终端或命令行界面。

2. 使用以下命令运行脚本：

```bash
python <script_name.py> --sourcefolder <源文件夹路径> --targetfolder <目标文件夹路径> [--targetscale <压缩比例>] [--enhancescale <增强比例>]
```

其中：
- `<script_name.py>` 为您的脚本文件名。
- `--sourcefolder` 参数指定要处理的源文件夹路径。
- `--targetfolder` 参数指定处理后图像的保存文件夹路径。
- `--targetscale` 参数可选，指定图像压缩比例，默认值为0.8。
- `--enhancescale` 参数可选，指定图像增强比例，默认值为1.1。

默认压缩比例为0.8,增强比例为1.1。当增强比例设置为1.0时，压缩效果等同于PS 
### 示例

假设您有一个源文件夹 `images`，并希望将处理后的图像保存到 `processed_images` 文件夹，使用默认的压缩比例和增强比例，可以使用以下命令：

```bash
python <script_name.py> --sourcefolder images --targetfolder processed_images
```
一个例子
```bash
python resize.py --sourcefolder "F:\图片像素压缩相关脚本\images" --targetfolder "F:\图片像素压缩相关脚本\新建文件夹" --targetscale 0.5 --enhancescale 1.1

```

如果希望指定压缩比例为0.5，增强比例为1.2，可以使用以下命令：

```bash
python <script_name.py> --sourcefolder images --targetfolder processed_images --targetscale 0.5 --enhancescale 1.2
```

### 结果

处理完成后，处理后的图像将保存在您指定的目标文件夹中。
