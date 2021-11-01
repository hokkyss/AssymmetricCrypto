# Asymmetric Cryptography

Asymmetric Cryptography merupakan aplikasi berbasis web yang berfungsi untuk melakukan proses enkripsi dan dekripsi terhadap suatu plainteks atau cipherteks dengan menggunakan algoritma kriptografi kunci publik tertentu. Terdapat 4 buah algoritma kunci publik yang difasilitasi, yaitu RSA, ElGamal, Paillier, dan Elliptic Curve.

## Getting Started

Instruksi-instruksi berikut ini akan membimbing Anda dalam tahap instalasi aplikasi dan cara menjalankannya.

### Prerequisites

Berikut ini adalah persiapan environment yang dibutuhkan untuk menjalankan aplikasi.

```
- Flask Framework for Integration
- HTML and CSS for Front End
- Python 3.9.7 for Back End
```

### Installing

Instalasi dilakukan dengan mengetikkan command dibawah ini.
```
pip install -r requirements.txt
```

## How to Run Program
1. Untuk menjalankan program, dari root directory jalankan command berikut.
```
python app.py
```
2. Untuk menampilkan aplikasi web, buka browser kemudian masuk ke laman berikut ini.
```
localhost:5000
```
3. Bila muncul tampilan tanpa adanya error message, maka program berhasil dijalankan.

## Guideline: How To Use
1. Gunakan generator key bila ingin membangkitkan key pada algoritma kriptografi yang diinginkan.
2. Masukkan public key / private key terlebih dahulu..
3. Anda bisa mengunggah public / private key dengan memilih file tersebut pada lokasi folder keys.
4. Pilih metode kriptografi kunci publik yang diinginkan.
5. Pilih mode pemrosesan teks (enkripsi atau dekripsi).
6. Masukkan plainteks / cipherteks yang akan diproses.
7. Tekan tombol Execute untuk memproses plainteks / cipherteks tersebut.

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web Framework
* HTML - Front End
* CSS - Front End
* [Python](https://www.python.org/) - Back End

## Authors

- 13518056 - Michael Hans
- 13519143 - Hokki Suwanda

## Acknowledgments

* Dosen IF4020 Kriptografi, Rinaldi Munir
* Asisten IF4020 Kriptografi, Dean dan Zunan