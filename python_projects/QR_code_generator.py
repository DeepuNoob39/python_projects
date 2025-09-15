import qrcode

data = input("Enter the lists of text or URL using commas(,) : ").split(",")
new_data = []
for d in data:
    d = d.strip()
    new_data.append(d)
    
    
# filename = input("Enter the filename: ").split(",")

    
# filler_color = input("Enter the filler color of the QR code: ")
# background_color = input("Enter the background color of the QR code: ")

qr = qrcode.QRCode(
    box_size=10,
    border=4
)
for i, data in enumerate(new_data, start=1):
    filename = f"qr_code{i}.png"
    
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    
    print(f"QR for '{data}' saved as {filename}")
    
# qr.add_data(data)

# img = qr.make_image(fill_color= filler_color, back_color = background_color)
# img.save(filename)

# print(f"QR is saved as {filename}")