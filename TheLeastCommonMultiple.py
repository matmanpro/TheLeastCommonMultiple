from math import gcd
try:
    bir = int(input('1. sayiyi giriniz: '))
    iki = int(input('2. sayiyi giriniz: '))
    uc = int(input('3. sayiyi giriniz: '))
    dort = int(input('4. sayiyi giriniz: '))

except(ZeroDivisionError,ValueError):
    Print('dikkat sayi giriniz')

print("4 the least common multiple = ", gcd(bir,iki,uc,dort))