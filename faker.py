from faker import Faker

# Create a Faker instance (optional, specify locale for localized data)
fake = Faker()

# Generate some random data
name = fake.name()
address = fake.address()
email = fake.email()
phone_number = fake.phone_number()
company = fake.company()
job_title = fake.job()
credit_card_number = fake.credit_card_number()
text = fake.text()
password = fake.password()
website = fake.url()

# Print the generated data
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Email: {email}")
print(f"Phone Number: {phone_number}")
print(f"Company: {company}")
print(f"Job Title: {job_title}")
print(f"Credit Card Number (masked): {credit_card_number}")  # Consider masking for security
print(f"Text: {text}")
print(f"Password (for demonstration purposes only, avoid storing actual passwords in plain text): {password}")
print(f"Website: {website}")

# Generate random data for specific locales (optional)
# fake = Faker('fr_FR')  # Example: French locale
# ... use fake object to generate data in French
