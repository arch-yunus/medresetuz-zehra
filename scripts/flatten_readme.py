import os

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\\engineering-courses"

SPECIAL_GROUPS = {
    'meta_muhendislik', 'ogretmenlik', 'saglik',
    'temel_bilimler', 'sosyal_ve_beseri_bilimler',
    'mimarlik_ve_tasarim', 'ozel_arastirma_alanlari'
}
IGNORED = {'.git', '.github', '.vs', 'assets', 'genel', 'scripts', 'templates'} | SPECIAL_GROUPS

def get_subdirs(path):
    if not os.path.exists(path):
        return []
    return sorted([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])


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

# Collect dirs
eng_dirs     = get_subdirs(os.path.join(root_dir, 'meta_muhendislik'))
teach_dirs   = get_subdirs(os.path.join(root_dir, 'ogretmenlik'))
saglik_dirs  = get_subdirs(os.path.join(root_dir, 'saglik'))
temel_dirs   = get_subdirs(os.path.join(root_dir, 'temel_bilimler'))
sosyal_dirs  = get_subdirs(os.path.join(root_dir, 'sosyal_ve_beseri_bilimler'))
arch_dirs    = get_subdirs(os.path.join(root_dir, 'mimarlik_ve_tasarim'))
special_dirs = get_subdirs(os.path.join(root_dir, 'ozel_arastirma_alanlari'))
other_dirs   = sorted([d for d in os.listdir(root_dir)
                       if os.path.isdir(os.path.join(root_dir, d)) and d not in IGNORED])

# Read README
readme_path = os.path.join(root_dir, 'readme.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_lines = f.readlines()

start_idx = end_idx = -1
for i, line in enumerate(readme_lines):
    s = line.strip()
    if s.startswith('## ⚙️') or s.startswith('## 🎓') or s.startswith('## 🏛️') or s.startswith('## 🔬') or s.startswith('## 🏥') or s.startswith('## 👥'):
        if start_idx == -1:
            start_idx = i
    if s.startswith('## 🧬 Mültidisipliner'):
        end_idx = i

if start_idx != -1 and end_idx != -1:
    header = readme_lines[:start_idx]
    footer = readme_lines[end_idx:]
    m = []

    sections = [
        ("⚙️", "META MÜHENDİSLİK", "meta_muhendislik", eng_dirs),
        ("🔬", "TEMEL BİLİMLER", "temel_bilimler", temel_dirs),
        ("🏥", "SAĞLIK BİLİMLERİ", "saglik", saglik_dirs),
        ("👥", "SOSYAL ve BEŞERİ BİLİMLER", "sosyal_ve_beseri_bilimler", sosyal_dirs),
        ("🎓", "ÖĞRETMENLİK", "ogretmenlik", teach_dirs),
        ("🏛️", "MİMARLIK ve TASARIM", "mimarlik_ve_tasarim", arch_dirs),
    ]

    for emoji, title, folder, dirs in sections:
        m.append(f"## {emoji} {title}\n\n")
        m.append(f"[`{folder}/`]({folder}/) altında **{len(dirs)} bölüm**:\n\n")
        m += make_table(dirs, folder)
        m.append("\n---\n\n")

    if other_dirs:
        m.append("## 📚 DİĞER BÖLÜMLER\n\n")
        m.append("Yukarıdaki gruplara girmeyen bölümler:\n\n")
        m += make_table(other_dirs)
        m.append("\n---\n\n")

    m.append("## 🔍 ÖZEL ARAŞTIRMA ve İLERİ UZMANLIK ALANLARI\n\n")
    m.append("Lisans bölümü formatında olmayan araştırma ve lisansüstü odak alanları:\n\n")
    m += make_table(special_dirs, 'ozel_arastirma_alanlari')
    m.append("\n---\n\n")

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(header + m + footer)

    print(f"README updated:")
    print(f"  Mühendislik: {len(eng_dirs)}, Temel: {len(temel_dirs)}, Sağlık: {len(saglik_dirs)}")
    print(f"  Sosyal: {len(sosyal_dirs)}, Öğretmenlik: {len(teach_dirs)}, Mimarlık+Tasarım: {len(arch_dirs)}, Diğer: {len(other_dirs)}, Özel: {len(special_dirs)}")
else:
    print("Section markers not found.")
