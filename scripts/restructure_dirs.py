import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

renames = {
    'adli_bilisim_mühendisligi': 'adli_bilisim_muhendisligi',
    'astronomi_ve_astrofizik': 'astronomi_ve_uzay_bilimleri',
    'bilgisayar_ve_ogretim_teknolojileri': 'bilgisayar_ve_ogretim_teknolojileri_egitimi',
    'bilişim_sistemleri_mühendisligi': 'bilisim_sistemleri_muhendisligi',
    'din_kulturu_ogretmenligi': 'din_kulturu_ve_ahlak_bilgisi_ogretmenligi',
    'elektrik_elektronik_mühendisligi': 'elektrik_elektronik_muhendisligi',
    'elektronik_haberlesme_muhendisligi': 'elektronik_ve_haberlesme_muhendisligi',
    'endüstri_mühendisligi': 'endustri_muhendisligi',
    'enerji-sistemleri_mühendisligi': 'enerji_sistemleri_muhendisligi',
    'fen_bilimleri_ogretmenligi': 'fen_bilgisi_ogretmenligi',
    'harita_mühendisligi': 'harita_muhendisligi',
    'havacilik_uzay_mühendisligi': 'havacilik_ve_uzay_muhendisligi',
    'imalat_mühendisligi': 'imalat_muhendisligi',
    'inşaat_mühendisligi': 'insaat_muhendisligi',
    'jeoloji_mühendisligi': 'jeoloji_muhendisligi',
    'kamu_yonetimi': 'siyaset_bilimi_ve_kamu_yonetimi',
    'kimya_mühendisligi': 'kimya_muhendisligi',
    'kontrol-otomasyon_mühendisligi': 'kontrol_ve_otomasyon_muhendisligi',
    'makine_mühendisligi': 'makine_muhendisligi',
    'matematik_ogretmenligi': 'ilkogretim_matematik_ogretmenligi',
    'mekatronik_mühendisligi': 'mekatronik_muhendisligi',
    'metalurji_malzeme_mühendisligi': 'metalurji_ve_malzeme_muhendisligi',
    'molekuler_biyoloji_genetik': 'molekuler_biyoloji_ve_genetik',
    'nano_mühendislik': 'nanoteknoloji_muhendisligi',
    'ormancilik': 'orman_muhendisligi',
    'pdr': 'rehberlik_ve_psikolojik_danismanlik',
    'piskoloji': 'psikoloji',
    'radyo_tv_sinema': 'radyo_televizyon_ve_sinema',
    'restorasyon_ve_koruma': 'kultur_varliklarini_koruma_ve_onarim',
    'sehircilik_ve_peyzaj': 'sehir_ve_bolge_planlama',
    'su_urunleri': 'su_urunleri_muhendisligi',
    'tıp': 'tip',
    'yapay_zeka_ve_veri_mühendisligi': 'yapay_zeka_ve_veri_muhendisligi',
    'yazilim_mühendisligi': 'yazilim_muhendisligi',
    'ziraat_mühendisligi': 'ziraat_muhendisligi',
    'çevre_mühendisligi': 'cevre_muhendisligi'
}

for old_name, new_name in renames.items():
    old_path = os.path.join(root_dir, old_name)
    new_path = os.path.join(root_dir, new_name)
    if os.path.exists(old_path) and not os.path.exists(new_path):
        os.rename(old_path, new_path)

# Ensure base grouping directories exist
groups = ['hukuk', 'mimarlik', 'ilahiyat', 'ozel_arastirma_alanlari']
for g in groups:
    gp = os.path.join(root_dir, g)
    if not os.path.exists(gp):
        os.makedirs(gp)

moves = {
    'hukuk': ['kamu_hukuku', 'medeni_hukuk', 'ticaret_hukuku', 'uluslararasi_hukuk'],
    'mimarlik': ['tasarim_studyolari', 'mimarlik_tarihi_ve_teorisi', 'yapi_fizigi_ve_cevre', 
                 'yapi_teknolojisi_ve_malzeme', 'bilgisayar_destekli_tasarim', 'gorsel_iletisim_ve_anlatim'],
    'ilahiyat': ['islam_tarihi_ve_sanatlari', 'temel_islam_bilimleri'],
    'ozel_arastirma_alanlari': ['3d_print_ai', 'akustik_mühendisligi', 'artırılmıs_gerceklik_mühendisligi',
                                'bci', 'biyoteknik_nanotıp', 'contex_engineering', 'egitim_yonetimi', 
                                'finans_mühendisligi', 'fintek_ai', 'guzel_sanatlar', 'hukuk_ve_ai_etigi', 
                                'kuantum_mühendisligi', 'metaverse', 'mühendislik_ortak', 'nanoteknoloji_ai',
                                'nöro_mühendisligi', 'optik_mühendisligi', 'patlayıcı_mühendisligi']
}

for group_name, dirs in moves.items():
    group_path = os.path.join(root_dir, group_name)
    for d in dirs:
        old_path = os.path.join(root_dir, d)
        new_path = os.path.join(group_path, d)
        # Rename inside specific to ozel_arastirma_alanlari
        if 'mühendisligi' in new_path:
            new_path = new_path.replace('mühendisligi', 'muhendisligi')
        if 'artırılmıs' in new_path:
            new_path = new_path.replace('artırılmıs_gerceklik_mühendisligi', 'artirilmis_gerceklik_muhendisligi')
            
        if os.path.exists(old_path):
            shutil.move(old_path, new_path)

print("Restructuring Complete.")
