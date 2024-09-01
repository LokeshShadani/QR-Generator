import qrcode as qr
from PIL import Image

## Creating Qr 
def qr_create():
    link = input("Enter The Url Or The Text Of You want to create qr code : ")
    return link

link = qr_create()

## Taking input from user that what should be the name of qr code so it can be easy to decide instead of other things


def name(link):
    img= qr.make_image(back_color=(255,195,235), fill_color=(55,95,35))(link)
    name = input(" Enter The Name By Which You Want To Save The Image : ")
    img.save(name+".png")

name(link)