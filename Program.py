import datetime

def hitung_umur(nama, tahun_lahir):
  tahun_sekarang = datetime.datetime.now().year
  umur = tahun_sekarang - tahun_lahir
  print(f"Hallo {nama}, Selamat umur kamu sekarang adalah {umur} tahun.")

nama = input("Masukkan nama kamu: ")
tahun_lahir = int(input("Masukkan tahun lahirmu: "))
hitung_umur(nama, tahun_lahir)
