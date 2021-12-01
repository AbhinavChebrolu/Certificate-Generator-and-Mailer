from email.mime.multipart import MIMEMultipart #headings like from, to, subject
from email.mime.application import MIMEApplication #attachments
from email.mime.text import MIMEText #text
import pandas as pd #rows, csv
import smtplib #mail settings
df = pd.read_csv('list1.csv')
for index,j in df.iterrows():
#Sender Credentials
    gmail_user = 'xyz@gmail.com'
    gmail_password = 'xyz@123'
#Mailing Details
    email_from = gmail_user
    email_to = j['Mail-ID']
    subject='Congratulations Mr.'
    body=("Go Greetings")
#Mail Headings
    msg=MIMEMultipart()
    msg['From']=email_from
    msg['To']=email_to
    msg['Subject']=subject
    a=msg.attach(MIMEText(body,'Plain'))
    msg.as_string(a)
#pdf attachment
    Certificate_doc = 'Certificates/{}.pdf'.format(j['Club & Chapter Name'] + '/' + j['Rename Date Org']+j['Name of Guest Speaker']) 
    pdf = MIMEApplication(open(Certificate_doc, 'rb').read())
    pdf.add_header('Content-Disposition','attachment',filename=Certificate_doc)
    msg.attach(pdf)
    print(j['sl.no'], 'Mailing Certificate of', j['Name of Guest Speaker'])
#Email Settings
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(email_from, email_to, msg.as_string())
    except Exception as ex:
        print ("Error Occured.",ex)

print("-------------------------------------")
print ("All Email sent successfully!")
