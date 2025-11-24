import os
import re

# Menü kısmını çekeceğimiz referans dosya
SOURCE_FILE = "index.html"

# Menü sınır etiketleri
START_MARKER = "<!-- START MENU -->"
END_MARKER = "<!-- END MENU -->"

# Tüm HTML dosyaları üzerinde işlem yapılacak klasör
TARGET_DIR = "."

# index.html içindeki menü kısmını al
with open(SOURCE_FILE, "r", encoding="utf-8") as f:
    source_html = f.read()

menu_section = re.search(f"{START_MARKER}(.*?){END_MARKER}", source_html, re.DOTALL)
if not menu_section:
    raise ValueError("Menü kısmı bulunamadı. Lütfen START ve END etiketlerini kontrol et.")
menu_html = menu_section.group(0)  # START ve END dahil

# Tüm .html dosyalarını tara
for filename in os.listdir(TARGET_DIR):
    if filename.endswith(".html") and filename != SOURCE_FILE:
        path = os.path.join(TARGET_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Eski menüyü yenisiyle değiştir
        updated = re.sub(f"{START_MARKER}.*?{END_MARKER}", menu_html, content, flags=re.DOTALL)

        # Eğer değişiklik yapıldıysa dosyayı kaydet
        if updated != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(updated)
            print(f"Güncellendi: {filename}")

print("✅ Tüm sayfalardaki menü başarıyla güncellendi!")
