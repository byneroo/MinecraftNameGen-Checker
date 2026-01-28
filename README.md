# MinecraftNameGen-Checker
Rare Name Generator-Checker For Minecraft


🇬🇧 English:
About the Project
This project is a Minecraft rare username generator & checker written in Python.
It generates 3–4 letter OG-style usernames and checks their availability using the official Mojang API.
Already checked names are never checked again, even after restarting the program.

Features
-Automatic 3–4 letter name generator
-OG-focused letter set (x, z, y, v, etc.)
-Real-time Mojang API availability check
-Persistent storage of checked names
-Saves only AVAILABLE usernames
-Prevents duplicate checks
-Rate-limit safe

checker.py
checked.txt # All previously checked usernames
rare_available.txt # Available rare usernames

Disclaimer
This project is for educational and personal use only.
Please respect Mojang API rate limits.

🇩🇪 Deutsche
Projektübersicht
Dieses Projekt ist ein Minecraft Name Generator & Checker, geschrieben in Python.
Es erzeugt seltene 3–4-buchstabige (OG) Benutzernamen und prüft deren Verfügbarkeit über die offizielle Mojang API.

Funktionen

Automatischer 3–4-Buchstaben-Generator
OG-Buchstabenfokus (x, z, y, v usw.)
Echtzeit-Verfügbarkeitsprüfung
Permanente Speicherung geprüfter Namen
Speichert nur verfügbare Namen
Keine doppelten API-Anfragen
Rate-Limit-sicher

Dateistruktur
checker.py
checked.txt # Bereits geprüfte Namen
rare_available.txt # Verfügbare seltene Namen

Hinweis
Dieses Projekt dient Lern- und Privat­zwecken.
Bitte die Mojang-API-Limits beachten.

🇹🇷 Türkçe
Proje Hakkında
Bu proje, Minecraft için 3–4 harfli nadir (OG) kullanıcı adlarını otomatik olarak üreten ve Mojang API üzerinden boş / dolu kontrolü yapan bir Python scriptidir.
Script, daha önce kontrol edilen isimleri bir daha asla kontrol etmez ve sadece boş olan isimleri kaydeder.

Dosya Yapısı
checker.py
checked.txt # Daha önce kontrol edilen tüm isimler
rare_available.txt # Boş bulunan nadir isimler

pip install requests
python checker.py
