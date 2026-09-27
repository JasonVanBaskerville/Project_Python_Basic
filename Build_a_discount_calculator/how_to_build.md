## Discount Calculator

Program ini merupakan latihan **Object-Oriented Programming (OOP)** untuk menghitung harga terbaik berdasarkan beberapa strategi diskon.

### Fitur
- `Product` menyimpan informasi produk dan harga.
- Mendukung beberapa strategi diskon: persentase, nominal tetap, dan diskon khusus pengguna premium.
- `DiscountEngine` mengevaluasi seluruh strategi yang tersedia dan memilih harga terendah.
- Setiap strategi dapat ditambahkan tanpa mengubah kode utama `DiscountEngine`.

### Konsep OOP
- **Abstraction**: `DiscountStrategy` menjadi abstract base class untuk seluruh strategi diskon.
- **Inheritance**: setiap jenis diskon mewarisi `DiscountStrategy`.
- **Polymorphism**: setiap strategi memiliki implementasi `is_applicable()` dan `apply_discount()` yang berbeda.
- **Strategy Pattern**: metode perhitungan diskon dipisahkan menjadi beberapa strategi yang dapat digunakan secara fleksibel.
- **Composition**: `DiscountEngine` menerima dan mengelola kumpulan objek strategi diskon.