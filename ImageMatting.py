
from rembg import remove
import os
from tqdm import tqdm
import cv2

class ImageMatting:
    def __init__(self, input_dir, output_dir):
        self.input_dir=input_dir
        self.output_dir=output_dir

    def Predict(self):
        for img_file in tqdm(os.listdir(self.input_dir), desc='Image Matting'):
            with open(os.path.join(self.input_dir, img_file), 'rb') as i:
                with open(os.path.join(self.output_dir, img_file), 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)

if __name__ == '__main__':
    Object = ImageMatting("Original_Image", "Output")
    Object.Predict()
