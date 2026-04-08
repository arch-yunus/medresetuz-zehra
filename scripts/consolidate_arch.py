import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"
target = os.path.join(root_dir, 'mimarlik_ve_tasarim')

if not os.path.exists(target):
    os.makedirs(target)

with open(os.path.join(target, 'README.md'), 'w', encoding='utf-8') as f:
    f.write("# 🏛️ MİMARLIK ve TASARIM\n\nBu klasör mimarlık, iç mimarlık, kentsel tasarım ve endüstriyel tasarım bölümlerini barındırır.\n")

members = [
    'mimarlik',
    'ic_mimarlik_ve_cevre_tasarimi',
    'peyzaj_mimarligi',
    'sehir_ve_bolge_planlama',
    'kultur_varliklarini_koruma_ve_onarim',
    'endustriyel_tasarim',
    'endustriyel_tasarim_muhendisligi',  # if still at root
    'grafik_tasarimi',
    'gorsel_iletisim_tasarimi',
    'tekstil_ve_moda_tasarimi',
    'seramik_ve_cam_tasarimi',
    'kuyumculuk_ve_mucevher_tasarimi',
    'cizgi_film_ve_animasyon',
    'muzik',
    'tiyatro_oyunculuk',
    'sanat_tarihi',  # moving from root if still there
]

moved = []
for d in members:
    src = os.path.join(root_dir, d)
    dst = os.path.join(target, d)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.move(src, dst)
        moved.append(d)
        print(f"Moved: {d}")

print(f"\nToplam {len(moved)} bölüm mimarlik_ve_tasarim/ altına taşındı.")
