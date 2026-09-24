## Medical Records Validator

Program ini digunakan untuk **memvalidasi format data rekam medis** agar setiap data memiliki struktur dan tipe data yang sesuai dengan aturan yang telah ditentukan.

### Validasi yang dilakukan

* `patient_id` → harus berupa format seperti `P1001`
* `age` → harus berupa angka dan minimal 18 tahun
* `gender` → hanya `male` atau `female`
* `diagnosis` → harus berupa string atau `None`
* `medications` → harus berupa list yang berisi string
* `last_visit_id` → harus berupa format seperti `V2301`

Program juga memeriksa:

* Apakah data berupa `list` atau `tuple`
* Apakah setiap record berupa `dictionary`
* Apakah semua key yang dibutuhkan tersedia
* Apakah nilai setiap field memenuhi constraint

Jika ditemukan data yang tidak valid, program akan menampilkan **pesan error beserta posisi record yang bermasalah**.

Jika seluruh data memenuhi aturan, program akan menampilkan:

```text
Valid format.
```

Program ini merupakan latihan penggunaan **function, dictionary, list, loop, conditional statement, `isinstance()`, `set`, `enumerate()`, regular expression (`re`), dan validasi data**.
