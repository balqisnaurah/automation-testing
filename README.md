# Automation Testing dengan Pytest

Automated testing untuk REST API menggunakan Python dan pytest framework. Mencakup pengujian operasi CRUD dengan terorganisir dalam test classes.

---

## Daftar File

### `test_api.py`

Test script utama yang berisi automation testing untuk JSONPlaceholder API.

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

## Jenis Pengujian

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

## Cara Menggunakan

### Prasyarat

```bash
pip install pytest selenium webdriver-manager requests
```

### Menjalankan Test

```bash
python -m pytest test_api.py -v
```

### Menjalankan Test Class Tertentu

```bash
python -m pytest test_api.py::TestGetUsers -v
```

### Menyimpan Hasil ke File

```bash
python -m pytest test_api.py -v > test_results.txt 2>&1
```

---

## API yang Diuji

**Base URL:** https://jsonplaceholder.typicode.com

JSONPlaceholder adalah free fake REST API yang umum digunakan untuk testing dan prototyping.

---

## Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| Python 3 | Bahasa pemrograman utama |
| pytest | Testing framework dengan fitur fixtures, assertions, dan reporting |
| requests | Library untuk HTTP requests |
| selenium | Library untuk browser automation (untuk pengembangan selanjutnya) |
| webdriver-manager | Otomatis mengelola driver browser |

---

## Struktur File

```
automation-testing/
├── test_api.py          # Script automation testing API
├── test_results.txt     # Output hasil testing (opsional)
└── README.md
```

---

## Tentang

Proyek ini dibuat sebagai bagian dari proses belajar Quality Assurance, khususnya dalam automation testing. Penggunaan test class membantu mengorganisir test berdasarkan fungsionalitas yang diuji, yang merupakan praktik standar dalam testing automation.
