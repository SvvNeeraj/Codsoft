import random
import string
def generate_password(length=12, complex=True):
    """Generate a random password."""
    if complex:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
        
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length<=0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    while True:
        special=input("Do you want to include special characters? (yes/no): ").lower()
        if special in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    complex_flag = True if special == 'yes' else False
    
    password = generate_password(length, complex_flag)
    print("Generated Password:", password)





















 
if __name__ == "__main__":
    main()
