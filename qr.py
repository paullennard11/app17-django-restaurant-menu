import qrcode

image = qrcode.make("http://127.0.0.1:8005")
image.save("qr.png")

