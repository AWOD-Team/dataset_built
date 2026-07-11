from pathlib import Path
import random
import shutil

base_dir = Path(__file__).resolve().parent
source_dir = base_dir/"OTS_human_selected"
train_dir = base_dir/"trainset"
target_dir = base_dir/"testset"

image_exts = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}
images = [p for p in source_dir.iterdir() if p.is_file() and p.suffix.lower() in image_exts]
if not images:
    raise SystemExit("源文件夹中未找到图片")

random.shuffle(images)
test_count = max(1, round(len(images) * 0.2)) if len(images) > 1 else 0
test_images = images[:test_count]
train_images = images[test_count:]

for output_dir in (train_dir, target_dir):
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

for img in train_images:
    shutil.copy2(img, train_dir / img.name)

for img in test_images:
    shutil.copy2(img, target_dir / img.name)

print(f"共 {len(images)} 张图片")
print(f"训练集：{len(train_images)} 张，保存到 {train_dir}")
print(f"测试集：{len(test_images)} 张，保存到 {target_dir}")

