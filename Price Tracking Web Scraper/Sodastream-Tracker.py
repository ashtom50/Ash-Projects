#Created by Ash Horton
from email.message import EmailMessage
from bs4 import BeautifulSoup
import requests

#Email details
email = "YOUR EMAIL HERE"
password = 'YOUR EMAIL PASSWORD'

#Product details
product = "Pepsi Max 6 Pack"
url = 'https://sodastream.co.uk/products/pepsi-max-6-pack'
target_price = 25

response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

#Product page details
price = content.find("meta", property="og:price:amount")
price = price["content"]

if float(price) <= target_price :

    msg = EmailMessage()
    msg.set_content("The price of " +  product +  " has dropped below the target value of £" + str(target_price) + " to £" + price +  ". The product can be purchased here, " +  u>
    msg['Subject'] = "Price Alert: " + product
    msg['From'] = email
    msg['To'] = email
    try:
        server = smtplib.SMTP_SSL('mail.privateemail.com', 465)
        server.login(email, password)
        server.send_message(msg)
        server.quit()

        print ('Email sent!')
    except:
        print ('Something went wrong...')

else :
    print("Current price is " + price + " ,target price is " + str(target_price) +  ". Not good enough!")
