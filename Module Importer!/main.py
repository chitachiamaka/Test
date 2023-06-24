from functions import display_file_content

display_file_content('data.txt')

with open('db.py', 'w') as file:
    with open('main.py', 'r') as main_file:
        file.write(main_file.read())





