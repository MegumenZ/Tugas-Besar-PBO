### Nyemil Naga
## About Nyemil Naga
Game ini akan mengadopsi gameplay Pac-Man, dimana player berusaha menghindar dari hantu-hantu naga yang mengejar dengan perilaku yang berbeda-beda.
Jika player tersentuh hantu naga, maka game akan berakhir.
Player dapat mengambil power up agar dapat menyelesaikan permainan dengan lebih mudah.

## Deskripsi
Nyemil Naga adalah permainan arkade klasik yang didasarkan pada game Pac-Man. Pemain mengendalikan karakter Pac-Man, yang harus mengumpulkan semua titik di papan sambil menghindari hantu naga. Game ini dikembangkan menggunakan Python dan Pygame.

## Fitur
- **Permainan Klasik Pac-Man**: Mengumpulkan titik-titik dan menghindari hantu naga.
- **Power-ups**: Mengkonsumsi power-up untuk sementara dapat memakan hantu naga.
- **Karakter Hantu Naga**: Blinky, Inky, Pinky, dan Clyde dengan perilaku unik.
- **Sistem Skor**: Dapatkan skor berdasarkan titik yang dikumpulkan dan hantu naga yang dimakan.
- **Nyawa Pemain**: Pemain memiliki sejumlah nyawa yang terbatas.

## Instalasi
1. **Persyaratan**:
    - Python 3.x
    - Pygame

2. **Instalasi Pygame**:
    ```bash
    pip install pygame
    ```

3. **Menjalankan Game**:
    - Clone repositori ini atau unduh semua file.
    - Jalankan game dengan perintah:
    ```bash
    python main.py
    ```

## Cara Bermain
- Gunakan tombol panah untuk menggerakkan Pac-Man.
- Kumpulkan semua titik di papan untuk menyelesaikan level.
- Hindari hantu naga yang berpatroli.
- Makan power-up untuk membuat hantu bisa dimakan sementara waktu.
- Setelah semua titik dikumpulkan, Anda memenangkan permainan.
- Jika Pac-Man ditangkap hantu dan kehilangan semua nyawa, permainan berakhir.

## Kontrol
- **Panah Kanan**: Gerak ke kanan
- **Panah Kiri**: Gerak ke kiri
- **Panah Atas**: Gerak ke atas
- **Panah Bawah**: Gerak ke bawah
- **Spasi**: Memulai kembali permainan dari menu game over atau kemenangan

## Struktur Proyek
- **main.py**: Berisi loop utama permainan dan logika utama permainan.
- **Ghost.py**: Berisi kelas `Ghost` dan perilaku hantu naga.
- **board.py**: Berisi fungsi untuk menggambar papan permainan dan pemain.
- **utils.py**: Berisi fungsi utilitas untuk permainan.
- **assets/**: Berisi gambar dan suara yang digunakan dalam permainan.

## Diagram UML
![Diagram UML.](https://github.com/MegumenZ/Tugas-Besar-PBO/blob/main/assets/Gambar%20WhatsApp%202024-05-20%20pukul%2019.53.44_48b1c5a7.jpg)

### Collaborator
| **Nama**  | **NIM** |
| ------------- | ------------- |
| Luthfiandri Ardanie | 122140089 |
| Dhias Erpangga Yoga | 122140109 |
| Figri Aldiansyah | 122140152 |
| Aldi Sanjaya | 122140150 |
| Bayu Ega Ferdana | 122140129 |
| Rizky Abdillah | 122140127 |
### Progress
_Closed Beta Test Version._
