import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

def merge_and_remove(src_name, dst_name, move_to_ozel=False):
    """
    Merges src into dst: copies any unique files from src to dst, then deletes src.
    If move_to_ozel=True, moves src to ozel_arastirma_alanlari instead of merging.
    """
    src = os.path.join(root_dir, src_name)
    if not os.path.exists(src):
        print(f"SKIP (not found): {src_name}")
        return

    if move_to_ozel:
        dst = os.path.join(root_dir, 'ozel_arastirma_alanlari', src_name)
        if not os.path.exists(dst):
            shutil.move(src, dst)
            print(f"MOVED to ozel_arastirma_alanlari: {src_name}")
        else:
            shutil.rmtree(src)
            print(f"REMOVED (already in ozel): {src_name}")
        return

    dst = os.path.join(root_dir, dst_name)
    if not os.path.exists(dst):
        os.makedirs(dst)

    # Walk source and copy files that don't exist in dst
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)
        if os.path.isfile(src_item):
            # Skip if canonical already has it (README, DERS_SABLONU etc.)
            if not os.path.exists(dst_item):
                shutil.copy2(src_item, dst_item)
                print(f"  Copied file: {item} -> {dst_name}/")
        elif os.path.isdir(src_item):
            # Only copy subdirs that don't exist in canonical
            if not os.path.exists(dst_item):
                shutil.copytree(src_item, dst_item)
                print(f"  Copied dir: {item}/ -> {dst_name}/")

    shutil.rmtree(src)
    print(f"MERGED & REMOVED: {src_name} -> {dst_name}")

# ── Kesin tekrarlar ──────────────────────────────────────────────────────────
merge_and_remove('cografya_bolumu',         'cografya')
merge_and_remove('kimya_bolumu',            'kimya')
merge_and_remove('moda_ve_tekstil_tasarimi','tekstil_ve_moda_tasarimi')
merge_and_remove('sinema_ve_televizyon',    'radyo_televizyon_ve_sinema')
merge_and_remove('biyomuhendislik',         'biyomedikal_muhendisligi')
merge_and_remove('basin_yayin',             'gazetecilik')

# fotografcilik_ve_video → ozel_arastirma_alanlari (YÖK'te ayrı lisans bölümü değil)
merge_and_remove('fotografcilik_ve_video', None, move_to_ozel=True)

print("\nBirleştirme işlemi tamamlandı.")
