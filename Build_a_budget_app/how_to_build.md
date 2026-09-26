# Budget App

Program sederhana untuk mengelola anggaran berdasarkan kategori menggunakan **Object-Oriented Programming (OOP)** dengan Python.

## Fitur

Program memiliki class `Category` yang digunakan untuk membuat kategori anggaran. Setiap kategori memiliki:

- `name` — nama kategori.
- `ledger` — menyimpan seluruh transaksi.

### Method pada `Category`

- `deposit()` — menambahkan pemasukan ke ledger.
- `withdraw()` — melakukan pengeluaran jika saldo mencukupi.
- `get_balance()` — menghitung saldo berdasarkan seluruh transaksi.
- `transfer()` — memindahkan sejumlah dana ke kategori lain.
- `check_funds()` — mengecek apakah saldo mencukupi.
- `__str__()` — menampilkan ringkasan kategori dan transaksi dalam format tabel.
- `__len__()` — mengembalikan panjang nama kategori.

## Spending Chart

Fungsi `create_spend_chart()` digunakan untuk menampilkan persentase pengeluaran setiap kategori dalam bentuk grafik vertikal.

Persentase pengeluaran dihitung berdasarkan total pengeluaran seluruh kategori dan dibulatkan ke bawah ke kelipatan 10.

Contoh kategori yang digunakan:

- Food
- Clothing
- Auto

## Konsep yang Dipelajari

Project ini melatih beberapa konsep Python dan OOP, seperti:

- Class dan object
- Constructor `__init__`
- Instance attributes
- Methods
- List dan dictionary
- Loop dan conditional statement
- String formatting
- Special methods `__str__()` dan `__len__()`
- Perhitungan dan visualisasi data sederhana