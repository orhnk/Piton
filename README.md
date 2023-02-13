# This is Turkish Python:
  every keyword transpiles to python keywords.
  **This language transpilation is pretty slight and not ideal for real applications**
# For Fun:
  This project is created just for fun! not for functioning!
# Installation:
  ```shell
  git clone https://github.com/KoBruhh/Piton.git
  cd Piton
  cd src
  chmod +x install.sh
  ./install.sh
  piton test.ptn
  ```
# How?
  It just binds turkish keywords to english python. Thats why it is not scalable and practical for big projects (Strings get bind too!)

# Samples:

```python

tanımla baloncuk_sıralama(liste):
  n = uzunluk(liste)
  için i içinde aralık(n):
    için j içinde aralık(0, n-i-1):
     eğer liste[j] > liste[j+1]:
      liste[j], liste[j+1] = liste[j+1], liste[j]

liste = [3,9,7,8,5,6,1,2,4,0]
yaz(f"önce: {liste}")
baloncuk_sıralama(liste)
yaz(f"sonra: {liste}")

```
