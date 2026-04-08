import os

def generate_summary(root_dir):
    summary_md = "# 🗂️ Otomatik Ders Dokümantasyon İndeksi\n\n"
    summary_md += "Bu dosya `scripts/generate_summary.py` tarafından otomatik oluşturulmuştur.\n\n"
    
    summary_md += "## YÖK Standart Bölümler\n\n"
    summary_md += "| Bölüm | Yol |\n"
    summary_md += "|-------|-----|\n"

    all_dirs = []
    for d in os.listdir(root_dir):
        full_path = os.path.join(root_dir, d)
        if os.path.isdir(full_path):
            if d.startswith('.') or d in ['assets', 'genel', 'scripts', 'templates', 'ozel_arastirma_alanlari']:
                continue
            all_dirs.append(d)
    all_dirs.sort()

    for d in all_dirs:
        course_name = d.replace('_', ' ').title()
        link = f"[{d}]({d}/)"
        summary_md += f"| {course_name} | {link} |\n"
        
    special_path = os.path.join(root_dir, 'ozel_arastirma_alanlari')
    if os.path.exists(special_path):
        summary_md += "\n## Özel Araştırma Alanları\n\n"
        summary_md += "| Özel Alan | Yol |\n"
        summary_md += "|-----------|-----|\n"
        
        special_dirs = [d for d in os.listdir(special_path) if os.path.isdir(os.path.join(special_path, d))]
        special_dirs.sort()
        for d in special_dirs:
            course_name = d.replace('_', ' ').title()
            link = f"[{d}](ozel_arastirma_alanlari/{d}/)"
            summary_md += f"| {course_name} | {link} |\n"

    with open(os.path.join(root_dir, 'SUMMARY.md'), 'w', encoding='utf-8') as f:
        f.write(summary_md)
    print("SUMMARY.md generated successfully.")

if __name__ == "__main__":
    # Run from root
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generate_summary(root)
