import csv
f = open('faculty.csv')
csv_f = csv.reader(f)

emails = []

for i in csv_f: 
    emails.append(i[3])
emails_no_header = emails[1:]

with open('emails.csv', 'wb') as f:
    wr = csv.writer(f, delimiter='\n')
    wr.writerows([emails_no_header])
