import os
import random
from PIL import Image
from pathlib import Path
import shutil

# SETTINGS
input_dir = "COM31006-DATASET"
output_dir = "dataset"
img_size = (128, 128)
train_split = 0.8

random.seed(42)  # reproducibility

classes = os.listdir(input_dir)

for cls in classes:
    cls_path = os.path.join(input_dir, cls)
    images = [f for f in os.listdir(cls_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

    # Shuffle images
    random.shuffle(images)

    split_idx = int(len(images) * train_split)
    train_imgs = images[:split_idx]
    test_imgs = images[split_idx:]

    for split, img_list in zip(['train', 'test'], [train_imgs, test_imgs]):
        out_dir = os.path.join(output_dir, split, cls)
        os.makedirs(out_dir, exist_ok=True)

        for i, img_name in enumerate(img_list):
            img_path = os.path.join(cls_path, img_name)

            try:
                img = Image.open(img_path).convert("RGB")
                img = img.resize(img_size)

                new_name = f"{cls}_{(i+1):03d}.jpg"
                img.save(os.path.join(out_dir, new_name))

            except Exception as e:
                print(f"Error with {img_name}: {e}")