import pandas as pd
import smtplib
from email.message import EmailMessage
import phonenumbers as phonenumbers
from phonenumbers import geocoder

#read csv file
df = pd.read_csv('contacts.csv')

#get email
print(df['email'])

my_contact = df.loc[(df['first_name'] == 'Richard') & (df['last_name'] == 'Taujenis'), ['email']]
print(my_contact)


 #if individiual
def individual():
   print("individual pressed")
      #if bulk
def bulk():
   print("bulk pressed")
      
#prompt if send email to all contact or individual
def main():
   running = True
   prompt = int(input('''Do you want to send to individual contact email or all:\n For individual press 1 \n For bulk send press 2 \n>'''))
   while running:
      try:
         if prompt == 1:
            individual()
            running = False
         if prompt == 2:
            bulk()
            running = False
         else:
            print("Try again")
         break
      except ValueError as e:
         print("wrong value given")
         break
         
     

if __name__ == '__main__':
   main()
