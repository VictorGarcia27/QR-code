import qrcode
import os
version = input("version (the version 1 to 40): ")
box_siz = input("box size (size of 'pixel'): ")
border = input("border (the border): ")
fill_color = input("color (black): ")
bg = input("Back Ground color (white): ")
name = input("name (.png): ")
place = input("dirrectory (not \ but /): ")+name
data = input("data (your data): ")

qr = qrcode.QRCode(
    version=version,
    box_size=box_siz,
    border=border
    )
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color=fill_color, back_color=bg)
img.save(place)
os.system("color f0")
qr.print_ascii()