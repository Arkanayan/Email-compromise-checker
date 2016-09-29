# Mass email compromise checker
##### Check if your emails has been compromised with haveibeenpwned.com

###### Features
* Check mass emails
* Get the result in txt format in **database.txt** and in csv **breached.csv**
* Resume checking from where it left off

###### Steps
1. Create a file **emails.txt** and put your emails there, comma separated. Usually from gmail **to** field.
2. Run the script with the command `python3 compromise.py`
3. Check the data in **database.txt**, updated as the script runs
4. After finish, the compromised emails with site names are available in **breached.csv** (with each column indicates one site)
