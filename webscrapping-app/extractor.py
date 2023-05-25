import re
import requests

def extract_data(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Extract phone numbers using regular expression
    phone_numbers = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', response.text)
    
    # Extract email addresses using regular expression
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)
    
    # Extract links using regular expression
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text)
    
    return phone_numbers, email_addresses, links

# Example usage
website_url = 'https://www.unionbankng.com/'
phone_numbers, email_addresses, links = extract_data(website_url)

# Get the desired file name from the user
file_name = input("Enter the file name to store the details: ")

# Write the extracted details to the file
with open(file_name, 'w') as file:
    file.write("Phone Numbers:\n")
    for number in phone_numbers:
        file.write(number + "\n")
    
    file.write("\nEmail Addresses:\n")
    for email in email_addresses:
        file.write(email + "\n")
    
    file.write("\nLinks:\n")
    for link in links:
        file.write(link + "\n")

print("Extraction completed. Details are stored in the file:", file_name)