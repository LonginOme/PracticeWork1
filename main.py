import re

def validate_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    pattern = r'^\+7\d{10}$'
    return bool(re.match(pattern, phone))

def sanitize_input(text: str) -> str:
    return re.sub(r'[<>"\']', '', text)

if __name__ == "__main__":
    print(validate_email("user@example.com"))   # True
    print(validate_phone("+79991234567"))        # True
    print(sanitize_input('Hello <script>'))      # Hello script
