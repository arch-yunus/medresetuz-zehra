import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

ADDITIONS = {
    'meta_muhendislik': [
        'beyin_bilgisayar_arayuzu_bci_muhendisligi',
        'yumusak_madde_bilimi_ve_muhendisligi',
        'akilli_malzemeler_ve_teknoloji',
        'mikro_nano_sistemler_ve_cihazlar',
        'fonksiyonel_malzeme_bilimi'
    ],
    'ozel_arastirma_alanlari': [
        'yurtdisi_cikarlarin_guvenligi_ve_korunmasi',
        'ulusal_guvenlik_arastirmalari_ileri',
        'kamu_guvenligi_muhendisligi'
    ],
    'spor_bilimleri': [
        'buz_ve_kar_dansi_performansi',
        'geleneksel_cin_savas_sanatlari_wushu'
    ],
    'saglik': [
        'nukleer_eczacilik'
    ],
    'edebiyat_ve_diller': [
        'dogu_kulturleri_ve_bolge_arastirmalari'
    ]
}

def create_jade_emperor_seal_expansion():
    count = 0
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        for d in depts:
            d_path = os.path.join(c_path, d)
            if not os.path.exists(d_path):
                os.makedirs(d_path)
                count += 1
                print(f"Jade Emperor's Seal Created: {container}/{d}")
    print(f"\nJade Emperor's Seal Expansion Complete: {count} new final-boss areas added.")

if __name__ == "__main__":
    create_jade_emperor_seal_expansion()
