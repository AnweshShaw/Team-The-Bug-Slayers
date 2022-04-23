import qrcode
import random, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# This generates the QR Code and links it with the URL.

qr = qrcode.QRCode(version=15, box_size=10, border=5)
data = "https://thebugslayers.000webhostapp.com/"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save('document_qr.jpg')

# The random module will be used to generate an OTP.

num = random.randint(1, 9)
num2 = random.randint(1, 9)
num3 = random.randint(1, 9)
num4 = random.randint(1, 9)
num5 = random.randint(1, 9)
num6 = random.randint(1, 9)

otp = num * 100000 + num2 * 10000 + num3 * 1000 + num4 * 100 + num5 * 10 + num6
print(otp)

# The smtp library is used to mail the OTP to the participants. This provides security to the user.

USER_EMAIL = "anweshofficial16@gmail.com"
USER_PASSWORD = "abcd1234()"
RECEIVER_EMAIL = "xyz@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(USER_EMAIL, USER_PASSWORD)
    connection.sendmail(from_addr=USER_EMAIL, to_addrs=RECEIVER_EMAIL,
                        msg=f"Subject:OTP\n\n Your OTP for accessing document is = {otp}")
    connection.close()

# To send a an attachment/document which the user sends to the other user/party via mail

msg = MIMEMultipart()
msg['From'] = USER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg['Subject'] = "Document Transfer after scanning of QR Code"
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain'))
filename = "document.pdf"
# inst is the instance of the MIMEbase
attachment = open("Path of the file", "rb")
inst = MIMEBase('application', 'octet-stream')
inst.set_payload(attachment.read())
encoders.encode_base64(inst)
inst.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(inst)
connection2 = smtplib.SMTP('smtp.gmail.com', 587)
connection2.starttls()
connection2.login(USER_EMAIL, USER_PASSWORD)
text = msg.as_string()
connection2.sendmail(USER_EMAIL, RECEIVER_EMAIL, text)
connection2.close()

