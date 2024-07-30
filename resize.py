from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import cv2
import os
import argparse

def remove_noise(image):
    """
    图像去噪。
    """
    return image.filter(ImageFilter.MedianFilter(size=3))

def progressive_resize(image, target_scale):
    """
    逐步缩放图像，以减少模糊效果。
    """
    width, height = image.size
    current_scale = 1.0
    
    while current_scale > target_scale:
        intermediate_scale = max(target_scale / current_scale, 0.9)  # 每次至少缩小一半，避免过小变化
        intermediate_size = (int(width * intermediate_scale), int(height * intermediate_scale))
        
        if intermediate_size[0] <= 0 or intermediate_size[1] <= 0:
            break  # 确保尺寸有效
        
        image = image.resize(intermediate_size, Image.LANCZOS)
        current_scale *= intermediate_scale
        width, height = image.size
    
    return image

def sharpen_image(image, factor=1.5):
    """
    应用锐化滤镜来增强图像的清晰度。
    """
    enhancer = ImageEnhance.Sharpness(image)
    return enhancer.enhance(factor)

def enhance_contrast(image, factor=1.1):
    """
    增强图像对比度。
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def enhance_details(image):
    """
    增强图像细节。
    """
    return image.filter(ImageFilter.DETAIL)

def edge_preserving_smoothing(image):
    """
    边缘保护和细节处理。
    """
    np_image = np.array(image)
    
    # 如果有 alpha 通道，将 alpha 通道分离
    if np_image.shape[2] == 4:
        alpha_channel = np_image[:, :, 3]
        np_image = np_image[:, :, :3]
    
    # 使用 OpenCV 的边缘保护滤波器
    smooth_image = cv2.edgePreservingFilter(np_image, flags=1, sigma_s=60, sigma_r=0.4)
    
    # 如果有 alpha 通道，重新加入 alpha 通道
    if 'alpha_channel' in locals():
        smooth_image = np.dstack((smooth_image, alpha_channel))
    
    return Image.fromarray(smooth_image)


def process_image(image_path, output_path, target_scale=0.8,target_enhance = 1.1):
    image = Image.open(image_path).convert('RGBA')
    image = progressive_resize(image, target_scale)
    image = enhance_contrast(image,factor=target_enhance)
    image = enhance_details(image)
    image = sharpen_image(image, factor=target_enhance)
    image.save(output_path)

def process_all_images(input_folder, output_folder, target_scale=0.8,target_enhance = 1.1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            process_image(input_path, output_path, target_scale,target_enhance)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="这是关于图片压缩的")

    # 定义一个命令行参数
    parser.add_argument('--sourcefolder', type=str, help='源文件夹')
    parser.add_argument('--targetfolder', type=str, help='目标文件夹')
    parser.add_argument('--targetscale', type=float, default=0.8, help='压缩比例')
    parser.add_argument('--enhancescale', type=float, default=1.1 ,help='增强比例')

    # 解析命令行参数
    args = parser.parse_args()


    # 处理所有图像
    process_all_images(args.sourcefolder,args.targetfolder,args.targetscale,args.enhancescale)

