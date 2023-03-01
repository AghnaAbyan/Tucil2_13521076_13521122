# Tugas Kecil 2 IF2211 Strategi Algoritma 2022/2023: Mencari Pasangan Titik Terdekat 3D dengan Algoritma *Divide and Conquer*
<img width="947" alt="image" src="https://user-images.githubusercontent.com/110531746/222017316-0cbfc5f4-4fe7-4052-80b8-03a1dbd5e8ae.png">

Program ini dibuat untuk memenuhi capaian kurikulum Tugas Kecil 2 IF2211 Strategi Algoritma 2022/2023, yaitu implementasi algoritma *Divide and Conquer* pada suatu masalah (dalam kasus ini yaitu mencari pasangan titik terdekat).

## Deskripsi Singkat Program
Program akan menerima masukan dari pengguna berupa dimensi (m) serta jumlah titik (n) yang diinginkan oleh pengguna. Program akan merancang sebuah "peta" (2D/3D tergantung masukan pengguna) yang berisi titik-titik berjumlah n tersebar secara acak pada peta. Lalu, program akan mengeluarkan statistik berupa:

- Jarak terdekat
- Koordinat titik pertama
- Koordinat titik kedua
- Banyak operasi *euclidian distance*
- Waktu eksekusi

Program mengeluarkan statistik tersebut pada 2 algoritma yang berbeda, yaitu algoritma *Brute-force* dan algoritma *Divide and Conquer*, yang dilaksanakan secara bersamaan.

Setelah itu, program menanyakan pengguna apabila pengguna ingin memvisualisasikan peta yang telah dibuat. Jika ingin, maka pengguna cukup menekan tombol "Y" atau "y" dan jika tidak, pengguna cukup menekan tombol lainnya. Setelah menekan tombol "Y" atau "y" tersebut, program akan memberikan visualisasi yang menampilkan peta (2D/3D tergantung masukan pengguna) berisikan titik-titik sejumlah n, dan 2 titik terdekat akan diberi warna merah sebagai pembeda dengan titik-titik lainnya yang bukan titik terdekat. Jika pengguna menggunakan dimensi diatas 3, program akan memberi pesan bahwa program tidak bisa melakukan visualisasi untuk dimensi diatas 3.
Jika sudah selesai, tutup visualisasi dan program selesai berjalan dengan memberi pesan "Bye!!".

## *Requirement* Program dan Instalasi Tertentu
Sebelum menjalankan program, diperlukan instalasi Python 3 dikarenakan program secara keseluruhan menggunakan bahasa Python. Python dapat diunduh melalui tautan berikut: https://www.python.org/downloads/

Setelah itu, diperlukan instalasi beberapa *library* Python supaya program dapat berjalan. Yang diperlukan adalah:
- colorama
- matplotlib
- mpl_toolkits
- numpy
- random
- time

## Cara Menggunakan Program
1. Pastikan direktori sudah berada pada folder ``src``.
2. Ketik ``python3 main.py`` pada terminal.

Selamat! program dapat berjalan! Selamat menikmati program yang telah kami buat!

## Identitas Pembuat
| Nama                     | NIM      | Username   |
| :---: | :---: | :---: |
| Moh. Aghna Maysan Abyan  | 13521076 | AghnaAbyan |
| Ulung Adi Putra          | 13521122 | Ulung32    |
