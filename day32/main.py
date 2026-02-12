import random
import smtplib
import datetime as dt
import random
import pandas

my_email = ""  # email id goes here


def send_email(to_name, to_address, subject, message):
    print(to_name, to_address, subject, message)
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login('', '') #email and password goes here
    connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=f"Subject:{subject}!\n\n Dear {to_name} \n {message}")



def send_quote(to_name, to_address, subject):
    with open('quotes.txt', 'r') as f:
        quotes = f.readlines()
        quote = random.choice(quotes)
        send_email(to_name, to_address, subject, message=quote)

now  = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    #Monday
    send_quote()


try:
    data = pandas.read_csv('birthdays.csv')
    dict_data  = data.to_dict('records')

    current_month = dt.datetime.today().month
    current_day = dt.datetime.today().day

    for d in dict_data:
        if d['month'] == current_month and d['day'] == current_day:
            send_quote(to_name=d['name'], to_address=d['email'], subject="Happy Birthday!")

    print(dict_data)
except:
    print("Error")