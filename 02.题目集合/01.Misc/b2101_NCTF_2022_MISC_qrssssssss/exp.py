from PIL import Imagefrom pyzbar.pyzbar
import decode
pipimport os

def maskanalysis(img):
    sign=''
    for ii in range(510,670,20):
        pi=img.getpixel((ii,170))
        if(pi == 0):
            sign += '1'
            if(pi == 255):
                sign += '0'
                return sign

def scanqr(img):
    decocdeQR = decode(img)
    return decocdeQR[0].data.decode('ascii')
qrlist = os.listdir(r"g:\temp\qrssssssss")
flag=[0]*32
masklist = ['11000100','11110011','10101010','10011101','00101111','00011000','01000001','01110110','00010010','00100101','01111100','01001011','11111001','11001110','10010111','10100000','01011111','01101000','00110001','00000110','10110100','10000011','11011010','11101101','10001001','10111110','11100111','11010000','01100010','01010101','00001100','00111011']
for i in qrlist:
    img=Image.open(r"g:\temp\qrssssssss\{}".format(i))
    qrmask=maskanalysis(img)
    for j in range(32):
        if(masklist[j]==qrmask):
            flag[j]=scanqr(img)
print(''.join(flag))