## Pin Extractor

Program ini digunakan untuk **mengekstrak kode rahasia dari beberapa puisi**. Kode rahasia dibuat berdasarkan **panjang kata tertentu pada setiap baris puisi**.

### Cara Kerja

Fungsi utama yang digunakan adalah:

```python
def pin_extractor(poems):
```

Fungsi menerima kumpulan puisi dalam bentuk list.

Untuk setiap puisi:

1. Puisi dipecah menjadi beberapa baris menggunakan `split('\n')`.
2. Setiap baris dipecah menjadi kata-kata menggunakan `split()`.
3. Program menggunakan posisi baris (`line_index`) untuk menentukan kata yang akan digunakan.

   * Baris ke-0 → mengambil kata ke-0
   * Baris ke-1 → mengambil kata ke-1
   * Baris ke-2 → mengambil kata ke-2
   * dan seterusnya.
4. Program menghitung jumlah karakter dari kata tersebut menggunakan `len()`.
5. Jumlah karakter tersebut digabungkan menjadi sebuah kode.
6. Jika pada suatu baris tidak terdapat kata pada posisi yang dibutuhkan, program memasukkan angka `0`.

Contoh:

```text
The grass is green
here and there
hoping for rain
before it turns yellow
```

Pemilihan katanya:

```text
Baris 0 → The      → 3 karakter
Baris 1 → and      → 3 karakter
Baris 2 → rain     → 4 karakter
Baris 3 → yellow   → 6 karakter
```

Sehingga kode yang dihasilkan:

```text
3346
```

### Bagian Penting

```python
for line_index, line in enumerate(lines):
```

`enumerate()` digunakan agar program mendapatkan **nomor indeks baris** sekaligus isi baris.

```python
words = line.split()
```

Digunakan untuk memisahkan setiap baris menjadi daftar kata.

```python
if len(words) > line_index:
```

Digunakan untuk memastikan kata pada indeks yang dibutuhkan tersedia.

```python
secret_code += str(len(words[line_index]))
```

Menghitung jumlah karakter dari kata yang dipilih, kemudian mengubahnya menjadi string dan menambahkannya ke `secret_code`.

```python
else:
    secret_code += '0'
```

Jika kata pada posisi tersebut tidak tersedia, program menambahkan `0`.

### Output

Ketika tiga puisi diberikan ke fungsi:

```python
print(pin_extractor([poem, poem2, poem3]))
```

program menghasilkan:

```text
['3550', '3346', '4311']
```

Dengan demikian, program ini merupakan latihan penggunaan **function, loop, `enumerate()`, string manipulation, list, indexing, dan conditional statement** dalam Python.
