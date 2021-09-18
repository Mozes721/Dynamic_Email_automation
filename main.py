import pandas as pd
from emails import *
from mailer import Mailer
import goslate
import phonenumbers
from phonenumbers import geocoder
from phonenumbers.phonenumberutil import region_code_for_country_code

send_from = ''
send_to = ''

# text = 'My name is Richard'
# gs = goslate.Goslate()

# print(gs.translate(text, 'ru'))
# #read csv file
df = pd.read_csv('contacts.csv')
 
# #get email
# print(df['email'])

# my_contact = df.loc[(df['first_name'] == 'Richard') & (df['last_name'] == 'Taujenis'), ['email']]
# print(my_contact)

 
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
      return check_contact(user, user_name)
   except SystemExit:
      return

   
def bulk():
   print("bulk pressed")
      
def check_contact(user, user_name):
   phone = ''.join(user.phone)
   number = phonenumbers.parse(phone, 'en')
   global country
   country = geocoder.description_for_number(number, 'en')
   country_index = region_code_for_country_code(number.country_code).lower()
   choose_lang = input('Would you like to transalte email to users native language? \n >Yes or No: \n').lower()
   if choose_lang == 'yes':
      send_email(user, user_name ,country_index)
   if choose_lang == 'no':
      send_email(user, user_name)


def send_email(user, user_name, lang='en'):
   full_name = ' '.join(user_name)
   email = ''.join(user.email)
   language = ''.join(lang)
   print("You will send email to %s who's email is %s and will be written in native language of %s." % (full_name, email, country))
   for index, (key, value) in enumerate(email_content.items()):
      print(index, key)
      print("#"*10)
      print(value)

      #input = int("Please select subject by integer value start from 0, 1 etc")
  




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
