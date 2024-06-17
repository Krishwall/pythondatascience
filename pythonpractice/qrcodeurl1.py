import qrcode
data="file:///D:/pythondatascience/NEWFILE.html"
qr=qrcode.QRCode(version=1,
                 box_size=10,
                 border=5)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save('MYQRCode2.png')