import requests
from bs4 import BeautifulSoup
import re

def extract_emails(url):
    response = requests.get(url)

    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        text = soup.get_text()
        
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, text)
        
        return set(emails)  
    else:
        print(f"Failed to retrieve {url}: {response.status_code}")
        return set()

url = 'https://www.keralapsc.gov.in' 
emails = extract_emails(url)

with open('extracted_emails.txt', 'w') as f:
    for email in emails:
        f.write(email + '\n')

print(f"Extracted {len(emails)} email addresses to 'extracted_emails.txt'.")
