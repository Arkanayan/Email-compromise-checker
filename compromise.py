filename = "emails.txt"

myemails = []

with open(filename) as f:
    for line in f:
        myemails = line

import re

email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

# email regex
regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
emails = []

for n in myemails.split(','):
    if regex.search(n.strip()):
        emails.append(regex.search(n.strip()).group(0))

# haveibeenpawned.com api url to query
url = "https://haveibeenpwned.com/api/v2/breachedaccount/{}"

import requests
import json, time

breached_data = {}

# lastemail queried, to resume from where it has left
with open("lastemail.txt", 'w+') as f:
    last_email = f.read()
    ind = 0
    try:
        ind = emails.index(last_email)
    except:
        ind = 0
    for email in emails[ind:]:
        try:
            r = requests.get(url.format(email))
            # go to the beginning of lastemail.txt and overwrite with current email
            f.seek(0)
            f.write(email)
            f.truncate()
            if len(r.text) != 0:
                sites = r.json()
                # store results in database.txt
                with open('database.txt', 'a') as datab:
                    print("Email: ", email)
                    datab.write('{}\t'.format(email))
                    for site in sites:
                        # Get the title of the breached site
                        breached_data.setdefault(site['Title'], []).append(email)
                        print(site['Title'])
                        datab.write('{},'.format(site['Title']))
                    datab.write('\n\n')
            else:
                print("Email: ", email, " Result: None")
        except:
            print("Error, email: ", email)
        # sleep 1 second to avoid rate limiting
        time.sleep(1)

# Write to csv, where each column is a compromised site
import csv
with open('breached.csv', 'w') as f:
    w = csv.DictWriter(f, breached_data.keys())
    w.writeheader()
    w.writerow(breached_data)


