## Settings Manager

Program ini digunakan untuk **mengelola user settings dalam dictionary**, seperti menambah, mengubah, menghapus, dan melihat pengaturan.

### Fitur

* `lowercase()` → mengubah key dan value string menjadi lowercase.
* `add_setting()` → menambahkan setting baru dan mengecek apakah key sudah tersedia.
* `update_setting()` → mengubah value dari setting yang sudah ada.
* `delete_setting()` → menghapus setting berdasarkan key.
* `view_settings()` → menampilkan seluruh setting yang tersedia atau memberikan pesan jika dictionary kosong.

Program juga menggunakan `isinstance()` untuk memastikan value yang akan diubah menjadi lowercase merupakan string.

### Contoh

```python
settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}
```

Dengan fungsi yang tersedia, user dapat melakukan operasi **Create, Read, Update, dan Delete (CRUD)** pada dictionary settings.
