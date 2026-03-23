```python
import random
import string

def generate_password():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    for i in range(12):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return ''.join(password)

if __name__ == '__main__':
    print(generate_password())
```