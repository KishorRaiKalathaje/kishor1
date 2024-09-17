import datetime

def generate_aadhaar_reference(aadhaar_number):
    # Get the last 4 digits of the Aadhaar number
    last_four_digits = aadhaar_number[-4:]

    # Get the current timestamp in the format YYYYMMDDHHMMSSmmm
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]

    # Combine the last four digits and the timestamp to form the reference number
    reference_number = last_four_digits + timestamp

    return reference_number

# Example usage
aadhaar_number = '506491179002'
reference_number = generate_aadhaar_reference(aadhaar_number)
print(f"Aadhaar Reference Number: {reference_number}")