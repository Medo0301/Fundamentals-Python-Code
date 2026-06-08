import string


def validate_length(password_: str):
    return 6 <= len(password_) <= 10


def contains_only_letters_and_digits(password_: str):
    return password_.isalnum()


def has_at_least_two_digits(password_: str):
    count = 0
    digits_check = "0123456789"
    for char in password_:
        if char in digits_check:
            count += 1
    if count >= 2:
        return True
    else:
        return False


password = input()
is_valid = True

if not validate_length(password):
    is_valid = False
    print("Password must be between 6 and 10 characters")
if not contains_only_letters_and_digits(password):
    is_valid = False
    print("Password must consist only of letters and digits")
if not has_at_least_two_digits(password):
    is_valid = False
    print("Password must have at least 2 digits")
if is_valid:
    print("Password is valid")
