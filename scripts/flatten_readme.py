import os

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

# 1. Collect standard departments
all_dirs = []
for d in os.listdir(root_dir):
    full_path = os.path.join(root_dir, d)
    if os.path.isdir(full_path):
        if d in ['.git', '.github', '.vs', 'assets', 'genel', 'scripts', 'templates', 'ozel_arastirma_alanlari']:
            continue
        all_dirs.append(d)
all_dirs.sort()

# 2. Collect special research fields
special_dirs = []
special_path = os.path.join(root_dir, 'ozel_arastirma_alanlari')
if os.path.exists(special_path):
    for d in os.listdir(special_path):
        if os.path.isdir(os.path.join(special_path, d)):
            special_dirs.append(d)
special_dirs.sort()

# Read original README
readme_path = os.path.join(root_dir, 'readme.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(readme_lines):
    if line.startswith('## 🎓 BÖLÜMLER'):
        start_idx = i
    if line.startswith('## 🧬 Mültidisipliner Sinerji Matrisi'):
        end_idx = i

if start_idx != -1 and end_idx != -1:
    header = readme_lines[:start_idx]
    footer = readme_lines[end_idx:]
    
    middle = ["## 🎓 BÖLÜMLER\n\n"]
    middle.append("Birim bazlı sınıflandırma olmaksızın, alfabetik sıraya göre YÖK standartlarındaki tam bölümler:\n\n")
    middle.append("| Bölüm | Bölüm | Bölüm |\n")
    middle.append("|:---|:---|:---|\n")
    
    row = []
    for d in all_dirs:
        title = d.replace('_', ' ').title()
        link = f"[{title}]({d})"
        row.append(link)
        if len(row) == 3:
            middle.append(f"| {row[0]} | {row[1]} | {row[2]} |\n")
            row = []
    if len(row) > 0:
        while len(row) < 3:
            row.append("")
        middle.append(f"| {row[0]} | {row[1]} | {row[2]} |\n")
        
    middle.append("\n---\n\n")
    
    middle.append("## 🔍 ÖZEL ARAŞTIRMA VE İLERİ UZMANLIK ALANLARI\n\n")
    middle.append("Doğrudan lisans bölümü formatında olmayan ancak spesifik teknoloji alanları, lisansüstü programlar veya araştırma başlıkları (örneğin BCI, vb.):\n\n")
    middle.append("| Özel Alan | Özel Alan | Özel Alan |\n")
    middle.append("|:---|:---|:---|\n")
    
    row = []
    for d in special_dirs:
        title = d.replace('_', ' ').title()
        link = f"[{title}](ozel_arastirma_alanlari/{d})"
        row.append(link)
        if len(row) == 3:
            middle.append(f"| {row[0]} | {row[1]} | {row[2]} |\n")
            row = []
    if len(row) > 0:
        while len(row) < 3:
            row.append("")
        middle.append(f"| {row[0]} | {row[1]} | {row[2]} |\n")
        
    middle.append("\n---\n\n")
    
    new_readme = header + middle + footer
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(new_readme)
    print("README updated.")
else:
    print("Could not find section markers.")
