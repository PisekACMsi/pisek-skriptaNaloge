import os

# define the name of the file to be renamed and its new name
old_file_name = "templateText.txt"
new_file_name = "bla.js"

# check if the old file exists
if os.path.isfile(old_file_name):
    # rename the file
    os.rename(old_file_name, new_file_name)
else:
    print(f"{old_file_name} does not exist.")