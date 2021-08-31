import pandas as pd
import smtplib
from email.message import EmailMessage
import phonenumbers as phonenumbers
from phonenumbers import geocoder

df = pd.read_csv('contacts.csv')

print(df.columns)

#get email
print(df['email'])

my_contact = df.loc[(df['first_name'] == 'Richard') & (df['last_name'] == 'Taujenis'), ['email']]
print(my_contact)
	

if __name__ == '__main__':
   pass