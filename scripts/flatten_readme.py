import os

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\\engineering-courses"

IGNORED = {'.git', '.github', '.vs', 'assets', 'genel', 'scripts', 'templates',
           'ozel_arastirma_alanlari', 'meta_muhendislik', 'ogretmenlik'}

# 1. Standard departments
all_dirs = sorted([
    d for d in os.listdir(root_dir)
    if os.path.isdir(os.path.join(root_dir, d)) and d not in IGNORED
])

# 2. Engineering
eng_path = os.path.join(root_dir, 'meta_muhendislik')
eng_dirs = sorted([d for d in os.listdir(eng_path)
    if os.path.isdir(os.path.join(eng_path, d))]) if os.path.exists(eng_path) else []

# 3. Teaching
teach_path = os.path.join(root_dir, 'ogretmenlik')
teach_dirs = sorted([d for d in os.listdir(teach_path)
    if os.path.isdir(os.path.join(teach_path, d))]) if os.path.exists(teach_path) else []

# 4. Special research
special_path = os.path.join(root_dir, 'ozel_arastirma_alanlari')
special_dirs = sorted([d for d in os.listdir(special_path)
    if os.path.isdir(os.path.join(special_path, d))]) if os.path.exists(special_path) else []

# Read README
readme_path = os.path.join(root_dir, 'readme.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_lines = f.readlines()

start_idx = end_idx = -1
for i, line in enumerate(readme_lines):
    if line.startswith('## ⚙️ META MÜHENDİSLİK') or line.startswith('## 🎓 BÖLÜMLER') or line.startswith('## 🎓 DİĞER'):
        start_idx = i
    if line.startswith('## 🧬 Mültidisipliner Sinerji Matrisi'):
        end_idx = i

def make_table(items, link_prefix=''):
    rows = []
    rows.append("| Bölüm | Bölüm | Bölüm |\n")
    rows.append("|:---|:---|:---|\n")
    row = []
    for d in items:
        title = d.replace('_', ' ').title()
        path = f"{link_prefix}/{d}" if link_prefix else d
        link = f"[{title}]({path})"
        row.append(link)
        if len(row) == 3:
            rows.append(f"| {row[0]} | {row[1]} | {row[2]} |\n")
            row = []
    if row:
        while len(row) < 3:
            row.append("")
        rows.append(f"| {row[0]} | {row[1]} | {row[2]} |\n")
    return rows

if start_idx != -1 and end_idx != -1:
    header = readme_lines[:start_idx]
    footer = readme_lines[end_idx:]
    middle = []

    middle.append("## ⚙️ META MÜHENDİSLİK — Tüm Mühendislik Bölümleri\n\n")
    middle.append(f"[`meta_muhendislik/`](meta_muhendislik/) altında **{len(eng_dirs)} mühendislik bölümü**:\n\n")
    middle += make_table(eng_dirs, 'meta_muhendislik')
    middle.append("\n---\n\n")

    middle.append("## 🎓 ÖĞRETMENLİK — Tüm Öğretmenlik Programları\n\n")
    middle.append(f"[`ogretmenlik/`](ogretmenlik/) altında **{len(teach_dirs)} öğretmenlik programı**:\n\n")
    middle += make_table(teach_dirs, 'ogretmenlik')
    middle.append("\n---\n\n")

    middle.append("## 🏛️ DİĞER BÖLÜMLER\n\n")
    middle.append("Mühendislik ve öğretmenlik dışındaki tüm bölümler (alfabetik):\n\n")
    middle += make_table(all_dirs)
    middle.append("\n---\n\n")

    middle.append("## 🔍 ÖZEL ARAŞTIRMA VE İLERİ UZMANLIK ALANLARI\n\n")
    middle.append("Lisans bölümü formatında olmayan; araştırma ve lisansüstü odak alanları:\n\n")
    middle += make_table(special_dirs, 'ozel_arastirma_alanlari')
    middle.append("\n---\n\n")

    new_readme = header + middle + footer
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(new_readme)
    print(f"README updated — Mühendislik: {len(eng_dirs)}, Öğretmenlik: {len(teach_dirs)}, Diğer: {len(all_dirs)}, Özel: {len(special_dirs)}")
else:
    print("Section markers not found.")
