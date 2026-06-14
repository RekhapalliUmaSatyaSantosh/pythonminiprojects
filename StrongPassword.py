import random
import string
def check_strength(password):
    """Check password strength and return score with feedback"""
    score = 0
    feedback = []
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Excellent length (12+ chars)")
    elif len(password) >= 8:
        score += 1
        feedback.append("👍 Good length (8-11 chars)")
    else:
        feedback.append("❌ Too short (minimum 8 characters recommended)")
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    if has_upper:
        score += 1
        feedback.append("✅ Has uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")        
    if has_lower:
        score += 1
        feedback.append("✅ Has lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
    if has_digit:
        score += 1
        feedback.append("✅ Has numbers")
    else:
        feedback.append("❌ Missing numbers")
        
    if has_special:
        score += 1
        feedback.append("✅ Has special characters")
    else:
        feedback.append("❌ Missing special characters (!@#$% etc.)")
    common_patterns = ['password', '123456', 'qwerty', 'abc123', 'admin']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        feedback.append("⚠️ Contains common weak pattern")
    return score, feedback
def generate_password(length=12, use_upper=True, use_lower=True, 
                      use_digits=True, use_special=True):
    """Generate a random strong password"""
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation  
    if not characters:
        return "Error: No character types selected!"
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    for _ in range(length - len(password)):
        password.append(random.choice(characters))
    random.shuffle(password)
    return ''.join(password)
print("🔐 Password Strength Checker & Generator 🔐")
print("="*50)

while True:
    print("\n1. Check password strength")
    print("2. Generate strong password")
    print("3. Exit")
    choice = input("\nChoose option (1/2/3): ")
    if choice == '1':
        password = input("Enter password to check: ")
        score, feedback = check_strength(password)
        print(f"\n📊 Password Score: {score}/7")
        if score >= 6:
            print("💪 Strength: STRONG - Excellent password!")
        elif score >= 4:
            print("👍 Strength: MEDIUM - Could be improved")
        else:
            print("⚠️ Strength: WEAK - Consider changing this password")
        print("\n📝 Detailed feedback:")
        for item in feedback:
            print(f"  {item}")    
    elif choice == '2':
        print("\n⚙️ Password Options:")
        length = int(input("Length (default 12): ") or 12)
        use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special chars? (y/n): ").lower() == 'y'
        print("\n🎲 Generated passwords:")
        for i in range(3):
            password = generate_password(length, use_upper, use_lower, 
                                        use_digits, use_special)
            print(f"  {i+1}. {password}")
        print("\n🔍 Strength check for first password:")
        score, _ = check_strength(password)
        if score >= 5:
            print("  ✅ Strong password!")
        else:
            print("  ⚠️ Consider adjusting settings for stronger password")   
    elif choice == '3':
        print("\n🔒 Stay safe online! Goodbye!")
        break
    else:
        print("❌ Invalid choice!")
