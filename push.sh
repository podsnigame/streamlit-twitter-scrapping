#!/bin/bash

echo "Menambahkan semua file..."
git add *

echo "Membuat commit..."
read -p "Masukkan pesan commit: " commit_message
git commit -m "$commit_message"

echo "Mengecek status branch..."
status=$(git status)
if [[ $status == "nothing to commit, working tree clean" ]]; then
echo "Tidak ada perubahan baru, keluar dari script."
exit 0
fi

echo "Menyimpan perubahan ke repository remote..."
git push
if [[ $? -eq 0 ]]; then
echo "Perubahan berhasil diterbitkan ke repository remote."
else
echo "Error: Terjadi kesalahan saat menerbitkan perubahan."
fi

echo "Script selesai."