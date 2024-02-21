from collections import deque

def is_palindrome(s):
    # Перетворення рядка: видалення пробілів та перетворення на нижній регістр
    s = ''.join(s.split()).lower()
    
    # Створення двосторонньої черги з символів рядка
    char_deque = deque(s)
    
    while len(char_deque) > 1:
        # Видалення та порівняння першого та останнього символів
        if char_deque.popleft() != char_deque.pop():
            return False
            
    return True

# Приклади використання функції
print(is_palindrome("A man a plan a canal Panama"))  # Повинно вивести True
print(is_palindrome("Abba")) # Повинно вивести True парна кількість символів
print(is_palindrome("madam")) # Повинно вивести True непарнв кількість символів
print(is_palindrome("Hello"))  # Повинно вивести False 