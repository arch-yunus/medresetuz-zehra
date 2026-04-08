import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"
target = os.path.join(root_dir, 'meta_muhendislik')

if not os.path.exists(target):
    os.makedirs(target)

# Create a META README for the umbrella folder
meta_readme = """# 🏗️ META MÜHENDİSLİK

Bu klasör, tüm mühendislik dallarını tek çatı altında barındıran **Akademik İşletim Sistemi**'nin çekirdek mühendislik deposudur.

## 📂 İçerik
Her alt klasör ayrı bir mühendislik bölümüdür. Tüm bölümler YÖK standartlarına göre adlandırılmıştır.
"""
with open(os.path.join(target, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(meta_readme)

moved = []
skipped = ['.git', '.github', '.vs', 'assets', 'genel', 'scripts', 'templates',
           'ozel_arastirma_alanlari', 'meta_muhendislik']

for d in sorted(os.listdir(root_dir)):
    full_path = os.path.join(root_dir, d)
    if not os.path.isdir(full_path):
        continue
    if d in skipped:
        continue
    # Match any directory with "muhendis" in the name
    if 'muhendis' in d.lower():
        dst = os.path.join(target, d)
        if not os.path.exists(dst):
            shutil.move(full_path, dst)
            moved.append(d)
            print(f"Moved: {d}")

print(f"\nToplam {len(moved)} mühendislik bölümü meta_muhendislik klasörüne taşındı.")
