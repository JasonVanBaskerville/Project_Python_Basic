## Media Catalogue

Program ini merupakan latihan **Object-Oriented Programming (OOP)** yang mengelola data film dan serial TV menggunakan konsep **Inheritance, Encapsulation, Polymorphism**, dan **Custom Exception**.

### Fitur
- `Movie` sebagai parent class untuk menyimpan informasi film.
- `TVSeries` sebagai child class yang mewarisi atribut dan validasi dari `Movie`.
- `MediaCatalogue` digunakan untuk menyimpan dan mengelompokkan berbagai media.
- Validasi data seperti tahun, durasi, jumlah season, dan episode.
- `MediaError` digunakan sebagai custom exception ketika object yang bukan media ditambahkan.
- `__str__()` digunakan untuk menampilkan informasi media dan katalog dengan format yang rapi.

### Konsep OOP
- **Inheritance**: `TVSeries` mewarisi `Movie`.
- **Polymorphism**: `Movie` dan `TVSeries` memiliki implementasi `__str__()` masing-masing.
- **Encapsulation**: setiap class mengatur data dan validasinya sendiri.
- **Custom Exception**: `MediaError` menangani kesalahan khusus terkait media.
- **Composition**: `MediaCatalogue` menyimpan berbagai object media dalam `items`.