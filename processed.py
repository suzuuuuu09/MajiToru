import cv2
import os
import pathlib
import numpy as np

# save_dir = "./img"
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     resized_image = cv2.resize(image, (128, 128))
#     gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
#     return gray_image

# 例として、ダウンロードした画像を前処理
# for image_name in os.listdir(save_dir):
#     image_path = os.path.join(save_dir, image_name)
#     processed_image = preprocess_image(image_path)
#     # 前処理した画像を保存
#     cv2.imwrite(os.path.join(save_dir, f"processed_{image_name}"), processed_image)

img_dir = "./img"
img_list = list(pathlib.Path(img_dir).glob("**/*.jpg"))
save_dir = f"{img_dir}/processed"

for i in range(len(img_list)):
    img_file_name = str(img_list[i])
    img_np = np.fromfile(img_file_name, dtype=np.uint8)
    img = cv2.imread(img_np, cv2.IMREAD_COLOR)
    img_resized = cv2.resize(img, (128, 128))
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(save_dir, f"processed_{img_file_name}"), img_gray)