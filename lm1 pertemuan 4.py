# Soal 1
def cek_angka(a, b, c):
    if a != b != c:
        if a + b == c or a + c == b or b + c == a:
            return True
        else:
            return False
    else:
        return False

x = int(input('Masukkan angka\t: '))
y = int(input('Masukkan angka\t: '))
z = int(input('Masukkan angka\t: '))
if cek_angka(x, y, z) == True:
    print('True')
else:
    print('False')