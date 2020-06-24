import csv

user_name = input('Enter your name: ')
user_email = input('Enter your email: ')
user_phone = input('Enter your phone: ')
user_github = input('Enter your github: ')
user_save = input('Save to CSV? ')

if user_save == 'yes':
    user_file = open('results.csv', 'a')
    csv_writer = csv.writer(user_file)
    csv_writer.writerow([user_name, user_github, user_email, user_phone])