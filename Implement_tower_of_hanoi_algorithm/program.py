def hanoi_solver(n: int) -> str:
    A = [x for x in range(n, 0, -1)]
    B = []
    C = []
    langkah = 0
    teks = f"{A} {B} {C}"
    
    while len(C) < n:
        langkah += 1
        
        if langkah % 2 == 1:
            if n % 2 == 1:
                # Rotasi Ganjil: Piringan 1 harus pindah A -> C -> B -> A
                # Kita cek di mana piringan 1 berada saat ini
                if A and A[-1] == 1:
                    t = A.pop()
                    C.append(t)
                elif C and C[-1] == 1:
                    t = C.pop()
                    B.append(t)
                elif B and B[-1] == 1:
                    t = B.pop()
                    A.append(t)
            else:
                # Rotasi Genap: Piringan 1 harus pindah A -> B -> C -> A
                if A and A[-1] == 1:
                    t = A.pop()
                    B.append(t)
                elif B and B[-1] == 1:
                    t = B.pop()
                    C.append(t)
                elif C and C[-1] == 1:
                    t = C.pop()
                    A.append(t)
        else:
            # Langkah Genap: Gerakan legal antara 2 tiang yang tidak ada piringan 1
            # Menggunakan struktur if-elif-else agar hanya satu blok yang dieksekusi
            if A and A[-1] == 1:
                # Piringan 1 di A, maka gerakkan antara B dan C
                if not B:
                    t = C.pop()
                    B.append(t)
                elif not C:
                    t = B.pop()
                    C.append(t)
                elif B[-1] < C[-1]:
                    t = B.pop()
                    C.append(t)
                else:
                    t = C.pop()
                    B.append(t)
                    
            elif B and B[-1] == 1:
                # Piringan 1 di B, maka gerakkan antara A dan C
                if not A:
                    t = C.pop()
                    A.append(t)
                elif not C:
                    t = A.pop()
                    C.append(t)
                elif A[-1] < C[-1]:
                    t = A.pop()
                    C.append(t)
                else:
                    t = C.pop()
                    A.append(t)
                    
            else:
                # Piringan 1 di C, maka gerakkan antara A dan B
                if not A:
                    t = B.pop()
                    A.append(t)
                elif not B:
                    t = A.pop()
                    B.append(t)
                elif A[-1] < B[-1]:
                    t = A.pop()
                    B.append(t)
                else:
                    t = B.pop()
                    A.append(t)


        # Simpan state list ke string teks
        teks += f"\n{A} {B} {C}"
        
    return teks

# Uji coba fungsi
print(hanoi_solver(2))
