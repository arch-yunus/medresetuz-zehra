import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"
target = os.path.join(root_dir, 'ogretmenlik')

if not os.path.exists(target):
    os.makedirs(target)

# README for the umbrella
meta_readme = """# 🎓 ÖĞRETMENLİK

Bu klasör, tüm öğretmenlik bölümlerini tek çatı altında barındıran Akademik İşletim Sistemi'nin eğitim deposudur.

## 📂 İçerik
Her alt klasör ayrı bir öğretmenlik programıdır. Tüm bölümler YÖK standartlarına göre adlandırılmıştır.
"""
with open(os.path.join(target, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(meta_readme)

moved = []
SKIP = {'.git', '.github', '.vs', 'assets', 'genel', 'scripts', 'templates',
        'ozel_arastirma_alanlari', 'meta_muhendislik', 'ogretmenlik'}

for d in sorted(os.listdir(root_dir)):
    full_path = os.path.join(root_dir, d)
    if not os.path.isdir(full_path):
        continue
    if d in SKIP:
        continue
    if 'ogretmen' in d.lower():
        dst = os.path.join(target, d)
        if not os.path.exists(dst):
            shutil.move(full_path, dst)
            moved.append(d)
            print(f"Moved: {d}")

print(f"\nToplam {len(moved)} öğretmenlik bölümü ogretmenlik/ altına taşındı.")
