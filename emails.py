
import sys
selected_email_temlate = []
f = open('email_text.txt')

email_text = f.read()
content_split = email_text.splitlines()

meetup_subject = content_split[0]
meetup_text = content_split[1]
 
job_rejection_subject =  content_split[2]
job_rejection_text =  content_split[3]

discount_subject = content_split[4]
discount_text = content_split[5]

subjects = [meetup_subject, job_rejection_subject, discount_subject]
texts = [meetup_text, job_rejection_text, discount_text]

email_content = dict(zip(subjects, texts))
email_list = list(email_content.items())
 
def choose_email():
   for index, (key, value) in enumerate(email_content.items()):
      print("*"*10)
      print(index)
      print("*"*10)
      print(key)
      print("#"*10)
      print(value)
   index = int(input("Please select subject by integer value start from 0, 1 etc: "))
   if index in range(len(email_list)):
      selected_email_temlate.append(subjects[index])
      selected_email_temlate.append(texts[index])
   else:
      print("Wrong input or index provided")
      sys.exit()