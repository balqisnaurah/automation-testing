# Automation Testing dengan Pytest

Automated testing untuk REST API dan UI menggunakan Python, pytest framework, dan Selenium WebDriver. Mencakup pengujian operasi CRUD pada API dan interaksi UI pada web application.

---

## Daftar File

### `test_api.py`

Test script untuk API testing menggunakan pytest dan library requests.

**Test Suite yang Dibuat:**

| Test Class | Endpoint yang Diuji | Jumlah Test |
|-----------|---------------------|-------------|
| `TestGetUsers` | GET /users dan /users/{id} | 5 |
| `TestCreateUser` | POST /users | 2 |
| `TestUpdateUser` | PUT /users/{id} | 2 |
| `TestDeleteUser` | DELETE /users/{id} | 1 |
| `TestPosts` | GET /posts dan /posts/{id}/comments | 4 |
| **Total** | | **14** |

---

### `test_ui_demo.py`

Test script untuk UI automation testing menggunakan Selenium WebDriver. Menguji situs the-internet.herokuapp.com yang khusus disediakan untuk latihan automation testing.

**Test Suite yang Dibuat:**

| Test Class | Fungsi yang Diuji | Jumlah Test |
|-----------|-------------------|-------------|
| `TestLogin` | Login flow (valid, invalid, logout) | 5 |
| `TestCheckboxes` | Interaksi dengan checkbox | 3 |
| `TestDropdown` | Interaksi dengan dropdown | 2 |
| **Total** | | **10** |

---

## Jenis Pengujian API (test_api.py)

### Test Class: TestGetUsers
- Status code response harus 200 untuk request valid
- Endpoint mengembalikan 10 user
- ID user yang diminta sesuai dengan response
- Status code 404 untuk user yang tidak ada
- Validasi field wajib pada response (id, name, email, username, address)

### Test Class: TestCreateUser
- Status code 201 untuk POST yang berhasil
- Data yang dikirim sama dengan data yang dikembalikan
- Response mengandung ID yang auto-generated

### Test Class: TestUpdateUser
- Status code 200 untuk PUT yang berhasil
- Data yang diupdate tercermin dalam response

### Test Class: TestDeleteUser
- Status code 200 setelah penghapusan

### Test Class: TestPosts
- Status code 200 untuk endpoint posts
- Total posts yang dikembalikan = 100
- Setiap post memiliki field title dan body
- Setiap comment terkait dengan postId yang benar

---

## Jenis Pengujian UI (test_ui_demo.py)

### Test Class: TestLogin
- Halaman login berhasil dimuat
- Login dengan kredensial valid berhasil dan menampilkan pesan sukses
- Login dengan username salah menampilkan pesan error
- Login dengan password salah menampilkan pesan error
- Logout berhasil mengarahkan kembali ke halaman login

### Test Class: TestCheckboxes
- Halaman checkbox berhasil dimuat dengan 2 checkbox
- Centang checkbox pertama berhasil
- Hapus centang checkbox kedua berhasil

### Test Class: TestDropdown
- Halaman dropdown berhasil dimuat
- Pemilihan opsi dari dropdown berhasil

---

## Cara Menggunakan

### Prasyarat

```bash
pip install pytest selenium webdriver-manager requests
```

### Menjalankan Test API

```bash
python -m pytest test_api.py -v
```

### Menjalankan Test UI

```bash
python -m pytest test_ui_demo.py -v
```

### Menjalankan Semua Test

```bash
python -m pytest -v
```

### Menjalankan Test Class Tertentu

```bash
python -m pytest test_api.py::TestGetUsers -v
python -m pytest test_ui_demo.py::TestLogin -v
```

### Menyimpan Hasil ke File

```bash
python -m pytest -v > test_results.txt 2>&1
```

---

## API dan Situs yang Diuji

| Tipe Test | URL | Deskripsi |
|-----------|-----|-----------|
| API Testing | https://jsonplaceholder.typicode.com | Free fake REST API untuk testing |
| UI Testing | https://the-internet.herokuapp.com | Situs latihan automation testing standar industri |

---

## Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| Python 3 | Bahasa pemrograman utama |
| pytest | Testing framework dengan fitur fixtures, assertions, dan reporting |
| requests | Library untuk HTTP requests (API testing) |
| selenium | Library untuk browser automation (UI testing) |
| webdriver-manager | Otomatis mengelola Chrome driver |

---

## Struktur File

```
automation-testing/
├── test_api.py          # Automation testing API
├── test_ui_demo.py      # Automation testing UI
├── test_results.txt     # Output hasil testing (opsional)
└── README.md
```

---

## Tentang

Proyek ini dibuat sebagai bagian dari proses belajar Quality Assurance, khususnya dalam automation testing. Mencakup dua pendekatan automation yang umum di industri: API testing menggunakan pytest dengan library requests, dan UI testing menggunakan Selenium WebDriver. Penggunaan test class membantu mengorganisir test berdasarkan fungsionalitas yang diuji, yang merupakan praktik standar dalam testing automation.
