from pathlib import Path
import random
import shutil

base_dir = Path(__file__).resolve().parent
source_dir = base_dir/"OTS_human_selected"
target_dir = base_dir/"testset"

count = 50
images = list(source_dir.glob("*.jpg"))
if not images :
    raise SystemExit("源文件夹中未找到jpg图片")
selected = random.sample(images, min(count, len(images)))

if target_dir.exists():
    shutil.rmtree(target_dir)

target_dir.mkdir(parents=True, exist_ok=True)

for img in selected:
    shutil.copy2(img, target_dir / img.name)

print(f"已复制 {len(selected)} 张图片到 {target_dir}")

