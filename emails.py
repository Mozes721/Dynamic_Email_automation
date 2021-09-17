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
