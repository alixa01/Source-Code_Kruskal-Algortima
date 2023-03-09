class Grafik:
    def __init__(inti, sudut):
        inti.V = sudut
        inti.grafik = []

    def tambah_sisi(inti, u, v, w):
        inti.grafik.append([u, v, w])

    # Fungsi Pencarian
    def cari(inti, induk, i):
        if induk[i] == i:
            return i
        return inti.cari(induk, induk[i])

    def satuan(inti, induk, tingkat, x, y):
        akarX = inti.cari(induk, x)
        akarY = inti.cari(induk, y)
        if tingkat[akarX] < tingkat[akarY]:
            induk[akarX] = akarY
        elif tingkat[akarX] > tingkat[akarY]:
            induk[akarY] = akarX
        else:
            induk[akarY] = akarX
            tingkat[akarX] += 1

    #  Menerapkan Algoritma Kruskal
    def kruskal_algo(inti):
        result = []
        i, e = 0, 0
        inti.grafik = sorted(inti.grafik, key=lambda item: item[2])
        induk = []
        tingkat = []
        for node in range(inti.V):
            induk.append(node)
            tingkat.append(0)
        while e < inti.V - 1:
            u, v, w = inti.grafik[i]
            i = i + 1
            x = inti.cari(induk, u)
            y = inti.cari(induk, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                inti.satuan(induk, tingkat, x, y)
        for u, v, bobot in result:
            print("%d - %d: %d" % (u, v, bobot))


g = Grafik(6)
g.tambah_sisi(0, 1, 4)
g.tambah_sisi(0, 2, 4)
g.tambah_sisi(1, 2, 2)
g.tambah_sisi(1, 0, 4)
g.tambah_sisi(2, 0, 4)
g.tambah_sisi(2, 1, 2)
g.tambah_sisi(2, 3, 3)
g.tambah_sisi(2, 5, 2)
g.tambah_sisi(2, 4, 4)
g.tambah_sisi(3, 2, 3)
g.tambah_sisi(3, 4, 3)
g.tambah_sisi(4, 2, 4)
g.tambah_sisi(4, 3, 3)
g.tambah_sisi(5, 2, 2)
g.tambah_sisi(5, 4, 3)
g.kruskal_algo()