class Manusia(object):
    """Class manusia dengan inisiasi 'nama'"""
    keadaan='lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapSalam(self):
        print("halo namaku: ", self.nama)
    def makan(self,s):
        print("saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olah(self,k):
        print('saya baru saja latihan', k)
        self.keadaan='lapar'
    def kali(self,n):
        return n*2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUang(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKota(self):
        return self.kota
    def perbaruiKota(self,k):
        self.kota=k
    def tambahUang(self,n):
        self.uang+=n


    
