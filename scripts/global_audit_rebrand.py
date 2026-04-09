import os
import shutil

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

# Move Map: (Source Path, Target Path)
MOVE_MAP = [
    # Engineering -> Agriculture
    ("meta_muhendislik/tutun_bilimi", "tarim_ve_ziraat_bilimleri/tutun_bilimi"),
    
    # Engineering -> Law
    ("meta_muhendislik/deniz_hukuku_ve_stratejisi", "hukuk_bilimi/deniz_hukuku_ve_stratejisi"),
    
    # Agriculture -> Engineering
    ("tarim_ve_ziraat_bilimleri/kagit_bilimi_ve_muhendisligi", "meta_muhendislik/kagit_bilimi_ve_muhendisligi"),
    
    # Engineering -> Architecture/Design
    ("meta_muhendislik/mucevherat_ve_degerli_tas_bilimi", "mimarlik_ve_tasarim/mucevherat_ve_degerli_tas_bilimi"),
    
    # Research -> Engineering
    ("ozel_arastirma_alanlari/finans_muhendisligi", "meta_muhendislik/finans_muhendisligi"),
    
    # Research -> Teaching
    ("ozel_arastirma_alanlari/egitim_yonetimi", "ogretmenlik/egitim_yonetimi"),
    
    # Consolidate duplication: Remove hukuk from sosyal_ve_beseri_bilimler
    ("sosyal_ve_beseri_bilimler/hukuk", "hukuk_bilimi/hukuk"), # Assuming this is a merge
    
    # Consolidate duplication: Remove guzel_sanatlar from ozel_arastirma_alanlari
    ("ozel_arastirma_alanlari/guzel_sanatlar", "guzel_sanatlar/guzel_sanatlar_arastirma"), # Niche name
]

def execute_rebranding_moves():
    for src, dst in MOVE_MAP:
        src_path = os.path.join(ROOT_DIR, src.replace("/", os.sep))
        dst_path = os.path.join(ROOT_DIR, dst.replace("/", os.sep))
        
        if os.path.exists(src_path):
            print(f"Checking Move: {src} -> {dst}")
            if not os.path.exists(dst_path):
                # Ensure parent dir exists
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                print(f"Moving {src} to {dst}")
                shutil.move(src_path, dst_path)
            else:
                # Target exists, so merge subdirectories
                print(f"Merging {src} into {dst}")
                for item in os.listdir(src_path):
                    s_item = os.path.join(src_path, item)
                    d_item = os.path.join(dst_path, item)
                    if not os.path.exists(d_item):
                        shutil.move(s_item, dst_path)
                # Cleanup src if empty or redundant
                try:
                    shutil.rmtree(src_path)
                except:
                    pass

def cleanup_duplicates():
    # Final check for specific known duplicates to ensure they are gone
    DUPLICATES_TO_REMOVE = [
        "sosyal_ve_beseri_bilimler/hukuk",
        "ozel_arastirma_alanlari/guzel_sanatlar",
        "ozel_arastirma_alanlari/fotografcilik_ve_video" # Consolidate with Guzel Sanatlar
    ]
    for d in DUPLICATES_TO_REMOVE:
        p = os.path.join(ROOT_DIR, d.replace("/", os.sep))
        if os.path.exists(p):
            print(f"Removing duplicate: {d}")
            shutil.rmtree(p)

if __name__ == "__main__":
    execute_rebranding_moves()
    cleanup_duplicates()
