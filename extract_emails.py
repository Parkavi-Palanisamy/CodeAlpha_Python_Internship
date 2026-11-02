import re

# Read the input text file
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Find email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

# Display extracted emails
print("Extracted Email Addresses:")
for email in emails:
    print(email)

# Save emails to output file
with open("emails.txt", "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

print("\nEmails saved to emails.txt")