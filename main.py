import pandas as pd
import smtplib
from email.message import EmailMessage
import phonenumbers
from phonenumbers import geocoder
from phonenumbers.phonenumberutil import region_code_for_country_code


send_from = ''
send_to = ''

#read csv file
df = pd.read_csv('contacts.csv')
 
#get email
print(df['email'])

my_contact = df.loc[(df['first_name'] == 'Richard') & (df['last_name'] == 'Taujenis'), ['email']]
print(my_contact)

 
 #if individiual
def individual():
   print("Individual chosen")
   print('#'*10)
   for user in df['first_name'] + ' ' + df['last_name']:
      print(user)
   print('#'*10)
   user = input('Please write the user you want to send the email to: ')
   user_name = user.split()
   first_name = user_name[0]
   last_name = user_name[1]
   try:
      user = df.loc[(df.first_name == first_name) & (df.last_name == last_name)]
      print(user)
      return send_mail(user)
   except SystemExit:
      return

   
def bulk():
   print("bulk pressed")
      
def send_mail(user):
   phone = ''.join(user.phone)
   print(phone)
   # number = phonenumbers.parse(user['phone'][0], 'en')
   # print(number)
   number = phonenumbers.parse(phone, 'en')
   country = geocoder.description_for_number(number, 'en')
   country_index = region_code_for_country_code(number.country_code)
   print(number)
   print(country)
   print(country_index)

#prompt if send email to all contact or individual
def main():
   try:
      prompt = int(input('''Do you want to send to individual contact email or all:\n For individual press 1 \n For bulk send press 2 \n>'''))
      if prompt == 1:
         individual()
      if prompt == 2:
         bulk()
      else:
         pass
   except ValueError as e:
      print(e)
      print("Sorry. Not accepted comand or incorrect input provided...")
      return
         
   
if __name__ == '__main__':
   runing_main = True
   main() 
