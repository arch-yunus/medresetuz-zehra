import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"
template_file = os.path.join(root_dir, 'templates', 'COURSE_TEMPLATE.md')

directories_to_scaffold = [
    '01_Temel_Bilimler_ve_Giris',
    '02_Alan_Dersleri',
    '03_Secmeli_ve_Ileri_Uygulama',
    '04_Arastirma_ve_Bitirme'
]

readme_append_text = """

---

## 📂 Çekirdek Ders Ağacı
Akademik sistem entegrasyonu kapsamında bu bölüm için önerilen ve standartlaştırılmış ders/çalışma klasörleri:

- [01 Temel Bilimler ve Seminerler](01_Temel_Bilimler_ve_Giris/)
- [02 Alan Dersleri ve Pratik](02_Alan_Dersleri/)
- [03 Seçmeli, İleri ve Uzmanlık Dersleri](03_Secmeli_ve_Ileri_Uygulama/)
- [04 Bitirme, Araştırma ve Çapraz Projeler](04_Arastirma_ve_Bitirme/)

> [!TIP]
> Yeni bir ders eklerken ana dizindeki `DERS_SABLONU.md` dosyasını kopyalayarak ilgili alt klasörün içine koyabilir ve kolayca kendi not şablonunuzu oluşturabilirsiniz!
"""

def scaffold_dir(target_dir):
    # Create subdirs
    for struct_dir in directories_to_scaffold:
        dpath = os.path.join(target_dir, struct_dir)
        if not os.path.exists(dpath):
            os.makedirs(dpath)
            
    # Copy template
    if os.path.exists(template_file):
        dest_template = os.path.join(target_dir, 'DERS_SABLONU.md')
        if not os.path.exists(dest_template):
            shutil.copy2(template_file, dest_template)
            
    # Append to README if not already there
    readme_path = os.path.join(target_dir, 'README.md')
    if not os.path.exists(readme_path):
        readme_path = os.path.join(target_dir, 'readme.md') # case fallback
        
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if "## 📂 Çekirdek Ders Ağacı" not in content and "Akademik sistem entegrasyonu" not in content:
            with open(readme_path, 'a', encoding='utf-8') as f:
                f.write(readme_append_text)

# 1. Main Departments
ignored_dirs = ['.git', '.github', '.vs', 'assets', 'genel', 'scripts', 'templates', 'ozel_arastirma_alanlari']
for d in os.listdir(root_dir):
    full_path = os.path.join(root_dir, d)
    if os.path.isdir(full_path):
        if d in ignored_dirs:
            continue
        scaffold_dir(full_path)

# 2. Special Research Areas
special_path = os.path.join(root_dir, 'ozel_arastirma_alanlari')
if os.path.exists(special_path):
    for d in os.listdir(special_path):
        full_path = os.path.join(special_path, d)
        if os.path.isdir(full_path):
            scaffold_dir(full_path)

print("Scaffolding completed securely across all academic domains.")
