import re

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r'[A-Z]', password):
        score += 1

    if re.search(r'[a-z]', password):
        score += 1

    if re.search(r'\d', password):
        score += 1

    if re.search(r'[!@#$%^&*(),.?":{}|_]', password):  # Updated pattern for special characters
        score += 1

    return score

def password_strength_rating(score):
    if score == 0:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    elif score == 4:
        return "Very Strong"
    else:
        return "Invalid"

while True:
    password = input("Enter a password: ")

    # Check for at least one lowercase letter, one uppercase letter, and one special character
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password) or not re.search(r'[!@#$%^&*(),.?":{}|_]', password):
        print("Password must include at least one lowercase letter, one uppercase letter, and one special character.")
        continue

    strength_score = password_strength(password)
    strength_rating = password_strength_rating(strength_score)

    print("Password Strength: ", strength_rating)

    choice = input("Do you want to enter another password? (yes/no): ")
    if choice.lower() != "yes":
        break
