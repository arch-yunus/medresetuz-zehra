import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

# Container mappings for display
CONTAINERS = {
    'meta_muhendislik': '🛠️ Mühendislik & İleri Teknoloji',
    'mimarlik_ve_tasarim': '🏛️ Mimarlık, Tasarım & Şehircilik',
    'guzel_sanatlar': '🖼️ Güzel Sanatlar & Estetik',
    'saglik': '🩺 Sağlık Bilimleri & Tıp',
    'ogretmenlik': '🎓 Eğitim Fakültesi & Pedagoji',
    'spor_bilimleri': '🏅 Spor Bilimleri & Performans',
    'sosyal_ve_beseri_bilimler': '⚖️ Sosyal, Beşeri & İdari Bilimler',
    'temel_bilimler': '🧪 Temel Fen Bilimleri',
    'edebiyat_ve_diller': '📚 Filoloji, Dil & Edebiyat',
    'iletisim': '📡 İletişim & Medya Bilimleri',
    'turizm_ve_gastronomi': '🏨 Turizm, Otelcilik & Gastronomi',
    'tarim_ve_ziraat_bilimleri': '🌱 Tarım, Ziraat & Doğa Bilimleri',
    'askeri_bilimler_ve_savunma_teknolojileri': '⚔️ Savunma Sanayii & Güvenlik Stratejileri',
    'hukuk_bilimi': '⚖️ Adalet & Hukuk Bilimleri',
    'ilahiyat_ve_din': '🕌 İlahiyat, Din & Felsefe',
    'on_lisans_programlari': '📋 Mesleki Yüksekokul (Ön Lisans)',
    'ozel_arastirma_alanlari': '🔬 Disiplinlerarası & Özel Araştırma',
    'kariyer_ve_sertifikasyonlar': '🚀 Kariyer, Portfolyo & Sertifika',
    'meta_yetkinlikler_ve_gelisim': '🧠 Meta-Zihin & Kişisel Disiplin',
    'genel': '📂 Genel Arşiv & Ortak Alanlar'
}

SPECIAL_DESCRIPTIONS = {
    'elektrik_elektronik_muhendisligi': 'Enerji, sinyal ve sistem teorisinin modern mühendislik zirvesi.',
    'yapay_zeka_ve_veri_muhendisligi': 'Veriden anlam çıkaran otonom sistemlerin mimarisi.',
    'siber_guvenlik_muhendisligi': 'Dijital kalelerin savunma ve strateji merkezi.',
    'havacilik_ve_uzay_muhendisligi': 'Yeryüzü sınırlarını aşan yüksek fizik ve itki mühendisliği.',
    'monk_mode_disiplin_sistemi': 'Yüksek odaklanma ve sarsılmaz bir irade için zihinsel işletim sistemi.',
}

def get_desc(folder, container):
    if folder in SPECIAL_DESCRIPTIONS:
        return SPECIAL_DESCRIPTIONS[folder]
    t = folder.lower()
    if 'muhendis' in t: return 'Sistem tasarımı ve ampirik çözümleme odaklı ileri mühendislik alanı.'
    if 'dili' in t: return 'Filolojik yapı ve kültürel mirasın derinlemesine incelenmesi.'
    if 'yonetimi' in t: return 'Operasyonel ve stratejik karar destek mekanizmalarının yönetimi.'
    return f"{folder.replace('_', ' ').title()} disiplinine ait teorik ve pratik uzmanlık deposu."

def generate_encyclopedic_readme():
    header = """<div align="center">

![AOS Hero Banner](assets/aos_hero_banner.png)

# 🏛️ AKADEMİK İŞLETİM SİSTEMİ (AOS)
### *Yapay Zeka Çağı İçin Evrensel Bilgi Ontolojisi ve Mültidisipliner Zihin Mimarisi* 🌐💎🚀

[![Versiyon](https://img.shields.io/badge/VERSİYON-2025.Elite-00A9E0?style=for-the-badge&logo=target)](./)
[![Kapsam](https://img.shields.io/badge/KAPSAM-372_Branş-D4AF37?style=for-the-badge&logo=rocket)](./SUMMARY.md)
[![Standart](https://img.shields.io/badge/STANDART-7--Kademeli_Nizam-black?style=for-the-badge&logo=gitbook)](./)
[![Mimari](https://img.shields.io/badge/MİMARİ-Zülcenahayn-18453B?style=for-the-badge&logo=openai&logoColor=white)](./)

---

## 📜 AOS MANİFESTOSU: EPİSTEMOLOJİK BÜTÜNLÜK
**Akademik İşletim Sistemi (AOS)**, bilginin ekstrem düzeyde parçalandığı ve dezenformasyonun arttığı Post-AI döneminde, rasyonel zihni korumak ve geliştirmek için tasarlanmış **"Büyük Birleşik Bilgi Çerçevesi"**dir. 

AOS, bilgiyi sadece tüketilen bir meta olarak değil, inşa edilen bir mimari olarak ele alır. Bu ekosistem, disiplinler arasındaki duvarları yıkarak; mühendislik matematiğini, sosyal bilimlerin derinliği ve ahlakın vizyonu ile tek bir potada eritir. AOS, bir disiplinler bütünü değil, bir zihin disiplinidir.

---

</div>

## ⚙️ SİSTEMATİK YAPI: 7-KADEMELİ ELİT NİZAM (00-06)
AOS içindeki her branş, rastgele notlar yerine **Systemum Standardı** adı verilen 7 katmanlı rijit bir hiyerarşi üzerine inşa edilmiştir. Bu yapı, Bologna Süreci ve ABET standartlarının ötesine geçerek, bireysel uzmanlığı otonom üretim seviyesine taşır:

> [!NOTE]
> **Hiyerarşik Ontoloji:** Veri -> Enformasyon -> Bilgi -> Hikmet dönüşümünü sağlamak için her alan dikey olarak bu 7 kademeye bölünmüştür.

1. **`00 — Hazırlık & Oryantasyon`**: Terminoloji hakimiyeti, yabancı dil yeterliliği ve metodolojik giriş.
2. **`01 — Teorik Temeller`**: Matematiksel modelleme, fiziksel yasalar ve disiplinin kuramsal omurgası.
3. **`02 — Çekirdek Müfredat`**: Zorunlu ana branş yetkinlikleri ve uygulama pratikleri.
4. **`03 — İleri Uzmanlık`**: Niş alanlarda derinleşme, seçmeli uzmanlık dökümantasyonu.
5. **`04 — AR-GE & Üretim`**: Bitirme projeleri, Capstone çalışmaları ve orijinal akademik çıktılar.
6. **`05 — Akademik Kariyer`**: Lisansüstü araştırma metodolojileri ve bilimsel yayın hazırlığı.
7. **`06 — Portfolyo & Endüstri`**: Küresel sertifikasyonlar, endüstriyel standartlar (ISO, IEEE, MIL-STD) ve profesyonel ağ.

---

## 🕌 FELSEFİ MİRAS VE VİZYONER RUH
AOS, modern bilimsel metodolojiyi rasyonel bir **Yöntem** olarak kullanır. Ancak bu devasa iskelete can veren "Ruh"; kalp ve aklın, fenle dinin imtizacını hedefleyen **Medresetü’z-Zehra** vizyonundan beslenir. Bu vizyon, salt bilgi yığınını bir "Hikmet" (Wisdom) seviyesine taşıma gayretidir.

Bu proje, bilginin sadece maddeden ibaret olmadığını savunan; maddeyi aklın nuruyla, manayı ise vicdanın ziyasıyla aydınlatan kadim bir mirasın dijital izdüşümüdür. Medresetü’z-Zehra, sadece bir eğitim kurumu değil; fen ilimleriyle din ilimlerinin barıştığı, modernitenin köklerle buluştuğu ve insanın "Zülcenahayn" (Çift Kanatlı) bir varlık olarak yeniden inşasını hedefleyen bir ideadır.

AOS mimarisi, bu idea doğrultusunda şu temel direkler üzerine yükselir:
- **Envanter Metodolojisi:** Varlık âleminin her bir hücresini (her bir branş) birer ayet/kanıt olarak görüp dökümante etmek.
- **İmtizac Sırrı:** Mühendisliğin soğuk rasyonalitesini, edebiyatın ve felsefenin sıcak estetiğiyle birleştirerek "Bütüncül İnsan" modelini oluşturmak.
- **Evrensel Nizam:** Mikro-kozmostan makro-kozmosa kadar her alanda var olan o büyük nizamı (Operating System), akademik branşların nizamıyla eşleştirmek.

| ✍️ Temel Düstur | 🏛️ AOS Uygulama Prensibi |
| :--- | :--- |
| **"Eyleme dökülmeyen ilim, yerinde sayan bir gölge gibidir."** | **Otonom Üretim & Aktif Mühendislik** |
| **"Hakikat için Din ve Fen el eledir."** | **Zülcenahayn (Çift Kanatlı) Entegrasyon** |
| **"Varlığın büyük nizamını bilmek için çabala."** | **Ampirik Sorgulama & Rasyonel Titizlik** |

---

## 🛠️ MODERN ENSTRÜMANTASYON (TEKNOLOJİ YIĞINI)
AOS, 21. yüzyılın en ileri araçlarıyla donatılmış bir "Dijital Medrese"dir:
- **Çekirdek Zeka:** Gemini 2.0 & Claude 3.5 Sonnet (Bilgi Sentezleyici)
- **Geliştirme Ortamı:** Cursor / Windsurf (Agentic Coding & Otomasyon)
- **Araştırma Motoru:** Perplexity Pro (Gerçek Zamanlı Akademik Arama)
- **Bilgi Yönetimi:** Obsidian & Markdown Hiyerarşisi (Epistemolojik Graft)

---

## 🎯 KULLANIM REHBERİ: AOS NASIL ÇALIŞIR?
AOS bir depodan (Repository) ziyade, bir yaşam tarzı ve kariyer yönetim mekanizmasıdır:
1. **Navigasyon:** SUMMARY.md üzerinden ilgilenen alanı seçin.
2. **Standardizasyon:** Her alandaki 00-06 yapısını takip edin.
3. **Üretim:** Öğrendiğiniz her bilgiyi 04 katmanında somut bir projeye dönüştürün.
4. **Sinerji:** Farklı konteynerlar (Örn: Mühendislik ve Felsefe) arasındaki bağları `cross-references` ile kurun.

---

## 📚 ANSİKLOPEDİK BÖLÜM DİZİNİ (372 BRANŞ)

Aşağıdaki kategoriler, AOS ekosisteminin 372 benzersiz hücresini temsil eder.

"""

    body = ""
    total_count = 0
    
    for folder, title in CONTAINERS.items():
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        depts = sorted([d for d in os.listdir(container_path) if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')])
        if not depts:
            continue
            
        section = f"<details>\n<summary><b>{title} ({len(depts)} Alan)</b></summary>\n<br>\n\n"
        section += "| Branş / Alan | Akademik Misyon & Stratejik Odak |\n"
        section += "| :--- | :--- |\n"
        
        for d in depts:
            dept_name = d.replace('_', ' ').title()
            # Turkish specific title fix
            dept_name = dept_name.replace('Muhendisligi', 'Mühendisliği').replace('Bilisim', 'Bilişim').replace('Insaat', 'İnşaat').replace('Ulasim', 'Ulaşım').replace('Isletme', 'İşletme')
            link = f"[{dept_name}]({folder}/{d}/)"
            desc = get_desc(d, folder)
            section += f"| {link} | {desc} |\n"
            total_count += 1
            
        section += "\n"
        section += "</details>\n\n"
        body += section

    footer = f"""
---

<div align="center">

## ⚖️ HUKUKİ STATÜ VE LİSANS
Bu proje, açık kaynak felsefesine sadık kalarak **MIT Lisansı** altında korunmaktadır. Tüm akademik dökümantasyon metodolojisi, evrensel bilim standartlarına göre yapılandırılmıştır.

**Geliştirici & Mimar**  
### Bahattin Yunus Çetin  
*Engineer - Researcher - AOS Architect*

[Linkedin](https://linkedin.com/in/bahattinyunuscetin) | [GitHub](https://github.com/bahattinyunus)

---
*"The ink of the scholar is more sacred than the blood of the martyr."*

---
© 2025 Akademik İşletim Sistemi (AOS).
</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"README.md expanded successfully. Total: {total_count}")

if __name__ == "__main__":
    generate_encyclopedic_readme()
