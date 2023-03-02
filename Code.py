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

# Soal 2
angka1 = str(input('Masukkan angka\t: '))
angka2 = str(input('Masukkan angka\t: '))
angka3 = str(input('Masukkan angka\t: '))

angka1 = list(angka1)
angka2 = list(angka2)
angka3 = list(angka3)

def cek_digit_belakang(a, b, c):
    if a[-1] == b[-1] or a[-1] == c[-1] or b[-1] == c[-1]:
        return True
    else:
        return False

if cek_digit_belakang(angka1, angka2, angka3) == True:
    print('True')
else:
    print('False')

# Soal 3 tipe 1
fahrenheit  =  lambda c : (9/5)*c + 32
reamur      =  lambda c : (4/5)*c

a = int(input('Masukkan angka\t: '))
print(fahrenheit(a))
b = int(input('Masukkan angka\t: '))
print(reamur(b))

# Soal 3 tipe 2
def fahrenheit(c):
    return lambda a : (9/5)*c + 32

def reamur(c):
    return lambda b : (4/5)*c

suhu_fahrenheit = int(input('Masukkan suhu celcius\t: '))
suhu_reamur = int(input('Masukkan suhu celcius\t: '))

print(fahrenheit(suhu_fahrenheit)(a=0))
print(reamur(suhu_reamur)(b=0))