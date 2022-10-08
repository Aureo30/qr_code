# import le module qr code
import qrcode
# import le module error_correct pour le fonctionnement correct
from qrcode.constants import ERROR_CORRECT_L
# créé l'objet du qr code
qr = qrcode.QRCode(
    # défini la complexité du qr code
    version=10,
    # défini le % de chance de réussite si il y a une erreur
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    # défini la boxe
    box_size=4,
    # défini la taille de la bordure
    border=3,
)
qr.add_data('https://www.youtube.com/c/Dali12')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')
