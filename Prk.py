import tkinter as tk #tkinter ialah pustaka utama untuk membuat antarmuka grafis.
from tkinter import messagebox #messagebox untuk menampilkan kotak pesan, seperti error dan informasi


def hasil_prediksi(): #memproses input dari pengguna
    try:
        for entry in nilai_entries:
            nilai = int(entry.get()) #Mengonversi nilai tersebut ke tipe integer dan memeriksa apakah nilai tersebut berada dalam rentang 0 hingga 100.
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100") #Jika ada nilai yang tidak valid (kurang dari 0 atau lebih dari 100), fungsi akan mengangkat.
        hasil_label.config(text="Prodi yang diprediksi: Teknologi Informasi")
    except ValueError as e:
        messagebox.showerror("Error") # menampilkan pesan kesalahan menggunakan messagebox.showerror().

#mengatur objek utama tkinter(root)
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan") #membuat judul
root.geometry("300x400")#mengatur ukuran aplikasi
root.configure(bg="#f0f0f0") #mengatur warna aplikasi

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16), bg="#f0f0f0") #Membuat label yang berfungsi sebagai judul aplikasi dengan teks "Aplikasi Prediksi Prodi Pilihan".
judul_label.grid(row=0, column=0, columnspan=2, pady=10) #Menggunakan metode grid untuk menempatkan label di baris 0 dan kolom 0, dengan menggabungkan dua kolom (columnspan=2) dan memberi jarak vertikal (pady=10).

mata_pelajaran = [ #Mendefinisikan daftar mata pelajaran yang akan digunakan dalam aplikasi.
    "Matematika",
    "Fisika",
    "Kimia",
    "Biologi",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Ekonomi",
    "Geografi",
    "Seni Budaya",
    "Pendidikan Agama"
]

nilai_entries = [] #Menginisialisasi list kosong untuk menyimpan entry widget.
for i, pelajaran in enumerate(mata_pelajaran): #Menggunakan loop untuk membuat label dan entry untuk setiap mata pelajaran
    label = tk.Label(root, text=pelajaran, bg="#f0f0f0")
    label.grid(row=i+1, column=0, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, pady=5)
    nilai_entries.append(entry)

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi) ##Membuat tombol dengan teks "Hasil Prediksi".
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

hasil_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0") #Membuat label untuk menampilkan hasil prediksi, dengan teks awal yang kosong.
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop() #Memanggil mainloop() untuk menjalankan aplikasi dan menunggu interaksi dari pengguna.