# ==========================
# 💡 Python Naming Conventions (PEP 8)
# ==========================

# ✅ Class Names
# - Use CamelCase
# - No underscores
# - Name should represent a thing or concept
# Example:
# class Student:
# class BankAccount:

# ✅ Method and Function Names
# - Use snake_case
# - Lowercase letters with underscores
# - Should be verbs or describe an action
# Example:
# def calculate_total():
# def send_email():

# ✅ Attribute (Instance Variable) Names
# - Use snake_case
# - Lowercase letters with underscores
# - Should clearly describe the data
# Example:
# self.user_name
# self.total_price

# ✅ Constant Names
# - Use ALL_CAPS
# - Words separated by underscores
# - Used for fixed values that don't change
# Example:
# MAX_USERS = 100
# PI = 3.14

# ✅ Private Variables and Methods
# - Start with a single underscore: _var
# - Or double underscore for name mangling: __var
# Example:
# self._password
# self.__secret_token

# ✅ Magic / Dunder Methods
# - Start and end with double underscores: __method__
# - These are special built-in methods
# Example:
# def __init__(self):
# def __str__(self):
# def __len__(self):

# ==========================
# 📌 General Tips
# ==========================
# - Use clear and descriptive names
# - Avoid using single-letter names like x, y, tmp (unless for short loops)
# - Follow consistency for better readability and maintainability
