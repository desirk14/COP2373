import re

# Function that validates phone number input
def validate_phone(phone):
    # Check if the input for the phone number is valid
    pattern = r'^(\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}$'
    return bool(re.match(pattern, phone))

# Function that validates SSN
def validate_ssn(ssn):
    # Check if the input for the SSN is valid
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))

# Function that validates zip code
def validate_zip(zip_code):
    # Check if the input for the zip code is valid
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))

def main():
    # Ask user to input phone number, SSN, and zip code
    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number: ")
    zip_code = input("Enter a ZIP code: ")

    # Display validation results
    print("\nValidation Results:")

    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    if validate_ssn(ssn):
        print("SSN is valid.")
    else:
        print("SSN is invalid.")

    if validate_zip(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")

# Call main function
if __name__ == "__main__":
    main()