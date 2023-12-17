# Zipcracker
The project aims to create a python script inorder to crack the password of a protected zip file.

Working:
The script basically works by accepting two parameters: The protected zipped file you want to crack + The dictionary text file that contains the list of words that you want to try that are provided as arguments into local variables.
Post which the zipped and dictionary file are opened and all tentative passwords contained in the dictionary is tried on the file using a for loop.
And finally, If the password was not found, print how many passwords were attempted.

Steps to run:
CMD to generate dictionary text file:
I used 5 lowercase names peter, Belinda, mario and pooja with dates from 01-01-19 to 31-12-
20 in the format mmddyy to generate my password list using the exrex tool
exrex tool: Exrex is a command-line tool and a Python module designed for generating regular expressions (regex) from examples. 
install the tool using: pip install exrex

CMD: exrex
'(peter|belinda|mario|pooja)(01|02|03|04|05|06|07|08|09|10|11|12)(01|02|03|04|05|06|07|08|09|10|11|12|13|14
|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31)(19|20)' > <file_to_store_output.list>

CMD to create a zip file:
zip -e <zipped_file_name.zip> <file_to _zip.txt>
(enter one of the passwords generated in a dictionary text file)

CMD to crack the password of zipped file using the script generated:
python3 zipcracker.py <zipped_file_name.zip> <generated_wordlist_file.list> 
