import pandas as pd
import sys
import time
from emails import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import goslate
import phonenumbers
from phonenumbers import geocoder
from phonenumbers.phonenumberutil import region_code_for_country_code
 
send_from = ''
send_to = ''

# text = 'My name is Richard'


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
   print("You will send emails to the whole list...")
   for index, row in df.iterrows():
      full_name = ''.join(row['first_name'] + ' ' + row['last_name'])
      send_email(full_name, row['email'])
      time.sleep(2)
      print("To %s to leads email: %s " % (full_name, row['email']))
      
def check_contact(user, user_name):
   phone = ''.join(user.phone)
   number = phonenumbers.parse(phone, 'en')
   global country
   country = geocoder.description_for_number(number, 'en')
   country_index = region_code_for_country_code(number.country_code).lower()
   choose_lang = input('Would you like to transalte email to users native language? \n >Yes or No: \n').lower()
   if choose_lang == 'yes':
      choose_lang_fnc(user, user_name ,country_index)
   if choose_lang == 'no':
      choose_lang_fnc(user, user_name)


def choose_lang_fnc(user, user_name, lang='en'):
   full_name = ' '.join(user_name)
   email = ''.join(user.email)
   # language = ''.join(lang)
   print("X"*20)
   time.sleep(6)
   if lang != 'en':
      time.sleep(4)
      gs = goslate.Goslate()
      print("You will send email to %s who's email is %s and email will be transated to native language of %s." % (full_name, email, country))
      translated = []
      # translated_subject = gs.translate(selected_email_temlate[0], 'fr')
      # translated_text = gs.translate(selected_email_temlate[1], 'fr')
      # print(translated_subject)
      translated.append(gs.translate(selected_email_temlate[0]), lang)
      translated.append(gs.translate(selected_email_temlate[1]), lang)
      print(translated)
   else:
      print("You will send email to %s who's email is %s and email will be written in English" % (full_name, email))
      send_email(full_name, email)
   
def send_email(full_name, email):
   sender_address = 'taujenisrichard@gmail.com'
   sender_pass = 'yourPW'
   #Setup the MIME
   message = MIMEMultipart()
   message['From'] = sender_address
   message['To'] = email
   message['Subject'] = selected_email_temlate[0]
   #The body and the attachments for the mail
   message.attach(MIMEText('Dear %s \n' %(full_name) + ',' + selected_email_temlate[1] + '\n Best Regards, \n Richard Taujenis', 'plain'))
   #Create SMTP session for sending the mail
   session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
   session.starttls() #enable security
   session.login(sender_address, sender_pass) #login with mail_id and password
   text = message.as_string()
   session.sendmail(sender_address, email, text)
   session.quit()
   print('Mail Sent')

#prompt if send email to all contact or individual
def main():
   choose_email()
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
