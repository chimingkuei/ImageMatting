from rembg import remove
import os
from tqdm import tqdm
from PIL import Image
import numpy as np
import io

class ImageMatting:
    def __init__(self, input_dir, output_dir):
        self.input_dir=input_dir
        self.output_dir=output_dir
    
    def remove_background_and_set_white(self, input_path, output_path):
        # 读取输入图像
        with open(input_path, 'rb') as i:
            input_data = i.read()
        # 使用 rembg 移除背景
        output_data = remove(input_data)
        # 将输出数据转换为 PIL Image 对象
        image = Image.open(io.BytesIO(output_data))
        # 创建一个白色背景
        white_background = Image.new('RGBA', image.size, (255, 255, 255, 255))
        # 将原图粘贴到白色背景上
        white_background.paste(image, (0, 0), image)
        # 转换为 RGB 模式（去除 alpha 通道）
        final_image = white_background.convert('RGB')
        # 保存结果
        final_image.save(output_path)

    def Predict(self):
        for img_file in tqdm(os.listdir(self.input_dir), desc='Image Matting'):
            self.remove_background_and_set_white(os.path.join(self.input_dir, img_file), os.path.join(self.output_dir, img_file))


if __name__ == '__main__':
    Object = ImageMatting("Original_Image", "Output")
    Object.Predict()

