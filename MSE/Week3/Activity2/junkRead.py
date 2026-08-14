# Open and read the file
from datetime import datetime

with open("junk.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
         print(line[0:-1])

# override a file
# with open("junk.txt", "w") as file:
#     file.write(f'hello world \n')

# append sth to a current file
with open("junk.txt", "a") as file:
    file.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] This is a log. \n')