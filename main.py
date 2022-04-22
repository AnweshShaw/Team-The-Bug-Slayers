import qrcode,image
import random, smtplib

# This generates the QR Code and links it with the URL.

qr = qrcode.QRCode(version=15,box_size=10,border=5)
data = "https://thebugslayers.000webhostapp.com/"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save('document_qr.jpg')

# The random module will be used to generate an OTP.

num = random.randint(1,9)
num2 = random.randint(1,9)
num3 = random.randint(1,9)
num4 = random.randint(1,9)
num5 = random.randint(1,9)
num6 = random.randint(1,9)

otp = num*100000+num2*10000+num3*1000+num4*100+num5*10+num6
print(otp)

# The smtp library is used to mail the OTP to the participants. This provides security to the user.

MY_EMAIL = "anweshofficial16@gmail.com"
MY_PASSWORD = "abcd1234()"
RECEIVER_EMAIL = "xyz@gmail.com"

''''
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs=RECEIVER_EMAIL,
                        msg=f"Subject:OTP\n\n Your OTP for accessing document is = {otp}")
    connection.close()'''