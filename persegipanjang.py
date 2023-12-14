def luasPersegiPanjang(panjang, lebar):
    return panjang * lebar


def KelilingPersegiPanjang(panjang, lebar):
    return 2 * (panjang + lebar)


panjang = int(input("Masukan persegi Panjang = "))
lebar = int(input("Masukan lebar persegi panjang = "))

print(luasPersegiPanjang(panjang, lebar))
print(KelilingPersegiPanjang(panjang, lebar))