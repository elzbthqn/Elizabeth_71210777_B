class NodeMahasiswa:
    def __init__(self, nama, ipk, n=None, p=None):
        self._element = nama
        self._ipk = ipk
        self._next = n
        self._prev = p

    def getNama(self):
        return self._element

    def getIpk(self):
        return self._ipk

    def setNama(self, nama):
        self._element = nama

    def setIpk(self, ipk):
        self._ipk = ipk

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addElementTail(self, nama, ipk):
        baru = NodeMahasiswa(nama, ipk)
        if (self.size == 0):
            self.head = baru
            self.tail = baru
        else:
            self.tail._next = baru
            baru._prev = self.tail
            self.tail = baru
        print("data masuk ke tail\n")
        self.size = self.size + 1

    def printDescending(self):
        bantu = self.tail
        print("===== Print Descending =====")
        while (bantu != None):
            print("============================")
            print("Nama:", bantu._element, "IPK:", bantu._ipk)
            bantu = bantu._prev
        print()
    
    def deleteLast(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            hapus = self.tail
            self.tail = self.tail._prev
            hapus._prev = None
            self.tail._next = None
            print(f"# Data {hapus._element} terhapus #\n")
            del hapus
        self.size = self.size - 1
    
    def rataIpk(self):
        n = 0
        jumlah = 0
        bantu = self.tail
        print("===== Print Descending =====")
        while (bantu != None):
            jumlah += bantu._ipk
            n += 1
            bantu = bantu._prev
        rata2 = jumlah / n
        print("============================")
        print("Rata-rata IPK: {:.1f}".format(rata2))

DLLNC = DoubleList()
DLLNC.addElementTail('Shalom', 3.9)
DLLNC.addElementTail('Nabilla', 3.8)
DLLNC.addElementTail('Kurniadi', 3.7)
DLLNC.addElementTail('Harris', 3.6)
DLLNC.printDescending()
DLLNC.deleteLast()
DLLNC.printDescending()
DLLNC.rataIpk()