import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

ADDITIONS = {
    'saglik': [
        'geleneksel_cin_veteriner_hekimligi'
    ],
    'meta_muhendislik': [
        'mucevherat_ve_degerli_tas_bilimi',
        'tutun_bilimi',
        'ambalaj_muhendisligi',
        'akilli_sebeke_bilgi_ve_muhendisligi',
        'sevk_ve_itki_muhendisligi',
        'seramik_tasarimi_ve_muhendisligi',
        'nukleer_kimya_muhendisligi',
        'rayli_sistemler_sinyalizasyon_ve_kontrol'
    ],
    'tarim_ve_ziraat_bilimleri': [
        'kagit_bilimi_ve_muhendisligi'
    ],
    'sosyal_ve_beseri_bilimler': [
        'su_sektoru_ekonomisi_ve_yonetimi'
    ],
    'ozel_arastirma_alanlari': [
        'kuantum_iletisim_ve_kriptografi'
    ]
}

def create_forbidden_city_expansion():
    count = 0
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        for d in depts:
            d_path = os.path.join(c_path, d)
            if not os.path.exists(d_path):
                os.makedirs(d_path)
                count += 1
                print(f"Forbidden City Export Created: {container}/{d}")
    print(f"\nForbidden City Expansion Complete: {count} new final areas added.")

if __name__ == "__main__":
    create_forbidden_city_expansion()
