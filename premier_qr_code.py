# importation du module pour le fonctionement du programme
import qrcode

# créé le qr code
img = qrcode.make('https://www.youtube.com/watch?v=oMHzXp-z83s')
# enregistre le qr code
img.save('qrcode.png')
