import cv2
import os
import shutil
import pathlib
import numpy as np

img_dir = "./img"
processed_save_dir = f"{img_dir}/processed"

# processedというフォルダの画像は含まない
img_list = [
    (img_path.parent.name, str(img_path))  # 親フォルダ名とファイルパスをタプルで格納
    for img_path in pathlib.Path(img_dir).glob("**/*.jpg")
    if processed_save_dir not in str(img_path)
]

# 保存先ディレクトリ作成
os.makedirs(processed_save_dir, exist_ok=True)

for folder_name, img_path in img_list:
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)  # 画像を読み込む
    if img is not None:  # 画像が正しく読み込まれたか確認
        img_resized = cv2.resize(img, (128, 128))
        img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        save_path = os.path.join(processed_save_dir, f"proc_{folder_name}_{pathlib.Path(img_path).name}")
        cv2.imwrite(save_path, img_gray)  # 前処理した画像を保存
    else:
        print(f"画像の読み込みに失敗しました: {img_path}")

processed_img_list = list(pathlib.Path(processed_save_dir).glob("*.jpg"))
rotate = [0, 90, 180, 270]

rotate_save_dir = f"{img_dir}/rotate"
os.makedirs(rotate_save_dir, exist_ok=True)  # 保存先ディレクトリ作成
for i in rotate:
    os.makedirs(f"{rotate_save_dir}/{i}", exist_ok=True)  # 回転用ディレクトリ作成

for img_path in processed_img_list:
    img_file_name = str(img_path)  # Path オブジェクトを文字列に変換
    img = cv2.imread(img_file_name, cv2.IMREAD_COLOR)  # 画像を読み込む
    if img is not None:  # 画像が正しく読み込まれたか確認
        for angle in rotate:
            if angle == 0:
                rotated_img = img
            elif angle == 90:
                rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            elif angle == 180:
                rotated_img = cv2.rotate(img, cv2.ROTATE_180)
            elif angle == 270:
                rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            
            save_path = os.path.join(f"{rotate_save_dir}/{angle}", f"rotated_{angle}_{img_path.name}")
            cv2.imwrite(save_path, rotated_img)  # 回転した画像を保存
    else:
        print(f"画像の読み込みに失敗しました: {img_file_name}")

# processedディレクトリを削除
shutil.rmtree(processed_save_dir)