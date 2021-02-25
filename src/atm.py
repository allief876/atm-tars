# TUGAS BESAR KU1102 PENGENALAN KOMPUTASI 2019/2020 - PROGRAM ATM
# 16519097 Reynaldo Averill
# 16519117 Allief Nuriman
# 16519207 Theodore Maximillan Jonathan 
# 16519217 Mohammad Sheva          

# PROGRAM SIMULASI_ATM
# Deksripsi : Program akan mensimulasikan ATM

# KAMUS
# jumlahorang, jeniskartu, regisulang, ModeTransaksi, coba, indeksorang, saldo, transaksi : integer
# pilihan, yakin, setor, tujuantrf, norek, notelpon, jumlahtransfer, kodekartu, kodebank : integer
# atmbarunyala, cobapertamakali, pinadadidatabase, pinangkasemua : boolean
# history : 3d matriks of string and integer
# data : matriks of string and integer
# Deklarasi Fungsi Registrasi
def registrasi (data):
	#Registrasi digunakan untuk menambahkan user baru pada database
	#KAMUS LOKAL
	#databaru : array of integer
	#ALGORITMA FUNGSI
	databaru=[0 for i in range (3)]	
	databaru[0]=input('Masukkan nama: ')
	databaru[1]=input('Masukkan PIN anda (Terdiri dari 6 digit angka): ')
	while((databaru[1].isdigit()==False)or(len(databaru[1])!=6)):
		print('PIN harus terdiri dari 6 digit angka')
		databaru[1]=input('Masukkan ulang PIN anda: ')
	databaru[2]=input('Masukkan saldo: ')
	while(databaru[2].isdigit()==False):
		print('Saldo harus berupa bilangan bulat')
		databaru[2]=input('Masukkan setoran awal anda: ')
	data.append(databaru)
	return data
#Deklarasi Fungsi jejaktransaksi
def jejaktransaksi(history,nominal,jenistransaksi):
	#jejaktransaksi digunakan untuk mencatat transaksi yang dilakukan suatu akun
	#KAMUS LOKAL
	#history : matriks 3d of integer
	#nominal : int
	#jenistransaksi : str
	#ALGORITMA FUNGSI
	history[indeksorang][2][0]=history[indeksorang][1][0]
	history[indeksorang][2][1]=history[indeksorang][1][1]
	history[indeksorang][1][0]=history[indeksorang][0][0]
	history[indeksorang][1][1]=history[indeksorang][0][1]
	history[indeksorang][0][0]=nominal
	history[indeksorang][0][1]=jenistransaksi
	return history
#Deklarasi Fungsi Konfirmasi Pulsa
def konfirmasipulsa(saldo,history,nominalpulsa,nohp) :
	#Program menampilkan layar konfirmasi saat melakukan pembelian pulsa
	#KAMUS LOKAL
	#saldo, nominal pulsa, nohp : int
	#history : 3d matriks of integer and string
	#ALGORITMA FUNGSI
	if saldo >= nominalpulsa:
		print('Anda yakin ingin isi pulsa',nominalpulsa,'ke nomor',nohp,'?')
		print('0. Tidak')
		print('1. Ya')
		yakin=int(input())
		if yakin == 1 :
			print('Isi ulang berhasil.')	
			saldo=saldo-nominalpulsa
			jejaktransaksi(history,nominalpulsa,"Pembayaran Pulsa")
		else :
			print('Masukan tidak valid.')
	else:
		print('Saldo tidak cukup')
	return saldo
#Deklarasi Fungsi Pulsa
def pulsa(saldo,history,namakartu):
	#Program menampilkan menu pilihan pengisian pulsa
	#KAMUS LOKAL
	#saldo, kodepulsa : int
	#history : 3d matriks of integer and string
	#namakartun: string
	#ALGORITMA FUNGSI
	print('Anda akan mengisi pulsa kartu',namakartu)
	print('Pilih nominal yang anda inginkan')
	print('1. 50.000')
	print('2. 100.000')
	print('3. 150.000')
	print('4. 200.000')
	kodepulsa=int(input())
	print('Masukkan nomor HP Anda')
	nohp=int(input())
	for i in range (4):
		if i+1==kodepulsa :
			saldo=konfirmasipulsa(saldo,history,((i+1)*50000),nohp)
	return saldo

# ALGORITMA UTAMA
jumlahorang=4
data=[[0 for j in range (3)] for i in range (jumlahorang)]
history=[[[0 for j in range (2)] for i in range (3)] for k in range(jumlahorang)]
atmbarunyala=True

#Kolom pertama berisi nama
#Kolom kedua berisi PIN
#Kolom ketiga berisi saldo

#Deklarasi database awal
data[0][0]='Theodore Jonathan'
data[0][1]=519207
data[0][2]=8000000
data[1][0]='Reynaldo Averill'
data[1][1]=519097
data[1][2]=9000000
data[2][0]='Allief Nuriman'
data[2][1]=519117
data[2][2]=8500000
data[3][0]='Mohammad Sheva'
data[3][1]=519217
data[3][2]=9500000

# Layar login awal (Reynaldo Averill)
while True:
	print('ATM Bank TARS')
	print('Tekan 0 jika kartu ATM anda adalah kartu ATM TARS')
	print('Tekan 1 jika kartu ATM anda berasal dari bank lain dan anda belum mengisi database di ATM ini')
	print('Tekan 2 jika anda ingin registrasi data baru, dan kartu ATM anda adalah kartu ATM TARS')
	if atmbarunyala==False:
		print('Tekan 3 jika kartu ATM anda berasal dari bank lain dan ada sudah mengisi database di ATM ini')
	jeniskartu=int(input())
	cobapertamakali=True
	
	# Registrasi kartu ATM non TARS
	if(jeniskartu==1):
		print('Maaf, kami tidak memiliki database anda. Silahkan isi database berikut: ')
		registrasi(data)
		jumlahorang+=1
		#Memperluas array history karena jumlah orang bertambah
		historybaru=[[[0 for j in range (2)] for i in range (3)] for k in range (jumlahorang)]
		for k in range(jumlahorang-1):
			for i in range (3):
				for j in range(2):
					historybaru[k][i][j]=history[k][i][j]
		history=historybaru
		print('Registrasi data selesai')
	
	# Registrasi kartu ATM TARS
	elif(jeniskartu==2):
		regisulang=1
		while(regisulang==1):
			print('Silahkan lengkapi data berikut')
			registrasi(data)
			jumlahorang+=1
			print('Registrasi data selesai. Apakah anda ingin melakukan registrasi data lagi ?')
			print('Tekan 1 untuk ya')
			print('Tekan 0 untuk tidak')
			regisulang=int(input())
	elif(jeniskartu==3):
		jeniskartu=1
	#Menghentikan program ATM
	elif(jeniskartu==16519):
		print('Program ATM akan dihentikan')
		exit()
	
	#Menu Utama (Mohammad Sheva)
	ModeTransaksi = 1
	while ModeTransaksi == 1 :
		# PIN kartu
		print('Silakan masukkan PIN anda')
		print('Jagalah kerahasiaan PIN anda')
		coba=0
		pinadadidatabase=False
		pinangkasemua=False
		while((coba<3)and((pinangkasemua!=True)or(pinadadidatabase!=True))):
			pin=input()
			pinadadidatabase=False
			pinangkasemua=False
			if((pin.isdigit()==True) and (len(pin)==6)):
				pinangkasemua=True
				if cobapertamakali==True:
					for i in range (jumlahorang):
						if(int(data[i][1])==int(pin)):
							pinadadidatabase=True
							indeksorang=i
				else:
					if(int(data[indeksorang][1])==int(pin)):
						pinadadidatabase=True
			if(pinangkasemua==False)and (coba<2):
				print('Pin harus berupa kombinasi dari 6 digit angka')
				print('Silahkan masukkan ulang PIN anda')
			elif((pinadadidatabase==False)and(coba<2)):
				print('Pin anda salah, silahkan masukkan ulang PIN anda')
			coba+=1
		if((coba==3)and(pinangkasemua!=True)and(pinadadidatabase!=True)):
			print('Anda telah memasukkan pin sebanyak 3 kali. Kartu ATM anda akan diblokir')
			print('Silahkan datangi kantor cabang Bank TARS terdekat di daerah anda')
			exit()
		saldo = int(data[indeksorang][2])
		if jeniskartu == 1 :
			print("Transaksi di ATM ini akan dikenakan biaya administrasi sebesar Rp 6.500")    
		print("Pilihan transaksi :")
		print("1. Setoran tunai dan Informasi Rekening")
		print("2. Pembayaran")
		print("3. Transfer")
		transaksi = int(input("Masukkan pilihan transaksi : "))
	
		# Setor tunai & Informasi Rekening
		if transaksi == 1 :
			print("Pilihan transaksi : ")
			print("1. Setoran Tunai")
			print("2. Informasi Saldo")
			print("3. Transaksi Terakhir")
			pilihan = int(input("Pilihan : "))
			#Setoran tunai
			if pilihan == 1 :
				setor = int(input("Masukkan jumlah setoran : "))
				print("Apakah Anda yakin akan menyetor sebanyak", setor, "?")
				print("0. Tidak")
				print("1. Ya")
				yakin = int(input("Jawaban : "))
				if yakin == 1 :
					saldo = saldo + setor
					jejaktransaksi(history,setor,'Setor Tunai')
					print('Setor Tunai Berhasil')
			#Informasi saldo
			elif pilihan == 2 :
				print("Saldo Anda tersisa", saldo)
			#Transaksi terakhir
			elif pilihan == 3 :
				print('Tiga Transaksi Terakhir Anda: ')
				print('| Nominal | Jenis Transaksi |')
				for i in range (3):
					print('|',end=' ')
					for j in range (2):
						print(history[indeksorang][i][j],end=' | ' )
					print()
	
		# Pembayaran listrik, air, pendidikan, pulsa(Allief Nuriman)
		elif transaksi == 2 :
			print("1. Listrik")
			print("2. Air")
			print("3. Pendidikan")
			print("4. Pulsa")
			tujuantrf = int(input("Masukkan kode tujuan transfer : "))
			#Pembayaran Listrik
			if tujuantrf == 1 :
				norek = int(input("Silakan masukkan 12 digit kode pelanggan : "))
				print("Pastikan Anda membawa gawai Anda")
				notelpon = int(input("Masukkan nomor handphone Anda : "))
				print ("Kami telah mengirim SMS jumlah tagihan, denda, nama pelanggan ke nomor Anda, silakan dicek")
				print("Silakan masukkan jumlah uang yang harus Anda bayar")
				jumlahtransfer = int(input())
				print("Apakah Anda yakin akan transfer sebanyak",jumlahtransfer,"?")
				print("0. Tidak")
				print("1. Ya")
				yakin = int(input())
				if yakin == 1 :
					if jumlahtransfer > saldo :
						print("Saldo tidak cukup")
					else:
						print("Pembayaran Berhasil")
						saldo = saldo - jumlahtransfer
						jejaktransaksi(history,jumlahtransfer,"Pembayaran Listrik")
				else :
					print("Masukan tidak valid")
			#Pembayaran PDAM
			elif tujuantrf == 2 :
				print("Masukkan kode perusahaan PDAM daerah Anda")
				print("Saat ini PDAM yang bisa dibayar lewat bank TARS adalah:")
				print("PDAM X: 30100")
				print("PDAM Y: 30101")
				print("PDAM Z: 30102")
				print("PDAM A: 30103")
				print("PDAM B: 30104")
				print("PDAM C: 30105")
				print("PDAM D: 30106")
				norek = int(input("Masukkan kode perusahaan diikuti nomor hp Anda : "))
				print("Kami telah mengirim SMS tagihan air Anda ke gawai Anda. Silakan dicek")
				jumlahtransfer = int(input("Masukkan jumlah tagihan yang harus Anda bayar : "))
				print("Apakah Anda yakin akan membayar tagihan Anda sebanyak "+str(jumlahtransfer)+" ?")
				print("0. Tidak")
				print("1. Ya")
				yakin=int(input())
				if yakin == 1 :
					if jumlahtransfer > saldo :
						print("Saldo tidak cukup")
					else:
						print("Pembayaran Berhasil")
						saldo = saldo - jumlahtransfer
						jejaktransaksi(history,jumlahtransfer,"Pembayaran PDAM")
				else:
					print("Masukkan tidak valid")
			#Pembayaran Pendidikan
			elif tujuantrf == 3 :
				print("Kode SBMPTN: 101")
				print("Kode ITB: 102")
				print("Kode UNPAD: 103")
				print("Kode UI: 104")
				print("Kode IPB: 105")
				print("Kode UNDIP: 106")
				print("Kode UNBRAW: 107")
				print("Kode UGM: 108")
				print("Kode UNSRI: 109")
				print("Masukkan Kode Institusi atau Lembaga diikuti oleh Kode Bayar")
				norek=int(input()) # Asumsikan user menginput sesuai petunjuk
				jumlahtransfer = int(input("Masukkan uang yang ingin Anda transfer ： "))
				print("Apakah Anda yakin akan membayar tagihan Anda sebanyak "+str(jumlahtransfer)+" ?")
				print("0. Tidak")
				print("1. Ya")
				yakin=int(input())
				if yakin == 1 :
					if jumlahtransfer > saldo :
						print("Saldo tidak cukup")
					else:
						print("Pembayaran Berhasil")
						saldo = saldo - jumlahtransfer
						jejaktransaksi(history,jumlahtransfer,"Pembayaran Pendidikan")
				else:
					print("Masukkan tidak valid")
			#Pulsa
			elif tujuantrf == 4 :
				print("Pilih kartu yang ingin Anda isi pulsanya")
				print("1. XL")
				print('2. Telkomsel')
				print('3. Indosat')
				print('4. Smartfren')
				kodekartu=int(input())
				if kodekartu == 1 :
					saldo=pulsa(saldo,history,'XL')
				elif kodekartu == 2 :
					saldo=pulsa(saldo,history,'Telkomsel')
				elif kodekartu == 3 :
					saldo=pulsa(saldo,history,'Indosat')
				elif kodekartu == 4 :
					saldo=pulsa(saldo,history,'Smartfren')
				else:
					print('Masukan tidak valid')
					
		# Transfer Antarrekening, Antarbank, dan Virtual Account (Theodore Jonathan)
		elif transaksi == 3 :
			print("MENU TRANSFER")
			print("Silakan pilih tujuan transfer Anda.")
			print("1. Transfer Antar Rekening")
			print("2. Transfer Antar Bank")
			print("3. Transfer Virtual Account")
			tujuantrf = int(input("Masukkan kode tujuan transfer : "))
			#Transfer Antar Rekening
			if tujuantrf == 1 :
				norek = int(input("Masukkan 10 digit nomor rekening tujuan : "))
				if norek < 10000000000 :
					jumlahtransfer = int(input("Masukkan jumlah transfer : "))
					print("Apakah Anda yakin akan transfer sebanyak", jumlahtransfer, "ke rekening", norek, "?")
					print("0. Tidak")
					print("1. Ya")
					yakin = int(input("Jawaban : "))
					if yakin == 1 :
						if jumlahtransfer > saldo :
							print("Saldo anda tidak mencukupi. Silakan isi ulang saldo.")
						else :
							print("Transfer sebesar "+str(jumlahtransfer)+" ke rekening "+str(norek)+" berhasil.")
							saldo = saldo - jumlahtransfer
							jejaktransaksi(history,jumlahtransfer,"Transfer Antar Rekening")
					else :
						print("Masukan tidak valid.")
			#Transfer Antar Bank
			elif tujuantrf == 2 :
				print("Daftar Kode Bank : ")
				print("101 - Bank Teorema Nilai Rata-Rata")
				print("102 - Bank Teorema Nilai Antara")
				print("103 - Bank Teorema Rolle")
				print("104 - Bank Teorema Sumbu Sejajar")
				print("105 - Bank Teorema Euler")
				print("106 - Bank Soal Pengenalan Komputasi")
				print("107 - Bank Soal Matematika 1A")
				print("108 - Bank Soal Fisika 1A")
				print("109 - Bank Tolong Minta Duit Dong")
				kodebank = int(input("Masukkan kode bank tujuan : "))
				if kodebank > 100 and kodebank < 110 :
					norek = int(input("Masukkan nomor rekening, maksimal 16 digit : "))
					if norek < 10000000000000000 :
						print("Transfer antarbank akan dikenai biaya admin Rp4.000")
						jumlahtransfer = int(input("Masukkan jumlah transfer : "))
						print("Apakah Anda yakin akan transfer sebanyak", jumlahtransfer, "ke rekening", norek, "?")
						print("0. Tidak")
						print("1. Ya")
						yakin = int(input("Jawaban : "))
						if yakin == 1 :
							if jumlahtransfer > saldo :
								print("Saldo anda tidak mencukupi. Silakan isi saldo.")
							else :
								print("Transfer ke rekening nomor "+str(norek)+" sebesar "+str(jumlahtransfer)+" berhasil. ")
								saldo = saldo - jumlahtransfer - 4000
								jejaktransaksi(history,(jumlahtransfer+4000),"Transfer Antar Bank")
						else :
							print("Nomor tidak valid.")
			#Virtual account
			elif tujuantrf == 3 :
				norek = int(input("Masukkan 16 digit nomor rekening virtual account : "))
				if norek < 10**16 :
					jumlahtransfer = int(input("Masukkan jumlah transfer : "))
					print("Apakah Anda yakin akan transfer sebanyak", jumlahtransfer, "ke rekening", norek, "?")
					print("0. Tidak")
					print("1. Ya")
					yakin = int(input("Jawaban : "))
					if yakin == 1 :
						if jumlahtransfer > saldo :
							print("Saldo anda tidak mencukupi. Silakan isi ulang saldo.")
						else :
							print("Transfer sebesar "+str(jumlahtransfer)+" ke virtual account "+str(norek)+" berhasil.")
							saldo = saldo - jumlahtransfer
							jejaktransaksi(history,jumlahtransfer,"Transfer Virtual Account")
					else :
						print("Masukan tidak valid.")
				else :
					print("Masukan salah.")
	            
		#Pilihan kembali ke menu awal
		print("Apakah Anda masih mau melanjutkan transaksi lain?")
		print("0. Tidak")
		print("1. Ya")
		ModeTransaksi = int(input("Pilihan : "))
		cobapertamakali=False
		data[indeksorang][2]=saldo
	#Pengurangan saldo untuk ATM non TARS
	if jeniskartu == 1:
		saldo = saldo - 6500
		jejaktransaksi(history,6500,'Biaya administrasi ATM')
	data[indeksorang][2]=saldo
	atmbarunyala=False
	#ATM selesai digunakan
	print("Transaksi selesai. Terima kasih sudah menggunakan ATM TARS. Saldo Anda sekarang tersisa", saldo)