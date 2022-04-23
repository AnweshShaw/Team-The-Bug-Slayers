# Team-The-Bug-Slayers
It consists of our proposed solution to the problem statement of "Document Creation Using QR Code" of the Coding Sprint Hackathon 2022 hosted by SRMIIC.
We have used HTML5 and CSS3 for the frontend part of our website.
The backend part is managed by a flask server.
The generation of a Dynamic QR Code after a regular interval of time, generating a 6 digit OTP and sending it to the user by mail is managed by using Python and its modules like qrcode,time,random, and smtplib.

Project Methodology and Working:
1) In the beginning, the user will scan the QR Code which will direct him/her to a document creation and sharing website landing page.
2) After he/she fills his details and uploads the document, it will redirect him/her to the submission page and the document and the data of the user will be saved in a SQL database.
3) A random OTP will generated and sent via mail to the another user.
4)  Now when another user will scan the QR code, he/she will be asked to authenticate the OTP which he has received via mail.
5)  Then, he will get access to the document shared which is saved in the database.

In brief, our project provides a simple,convenient,reliable and a secure way of transferring documents between 2 users or an organisation.
