''' Application to check password validation'''

import re

class Validator:

    def test_password_strength(password):
        ''' Method to check password against rules and determine its strength'''

        error_message = ""
        validity_score = 0
        password_strength = "None"

        # Check against a list of common passwords 10-20 common password = very weak

        common_passwords_list =["123456","123456789","picture1","password",
                                "12345678","111111","123123","12345","1234567890","senha"]
        if password in common_passwords_list:
            error_message = "Password is most common password list."
            validity_score = 1
            password_strength = "Very Weak"
            return error_message,validity_score,password_strength

        # Check if password is at least 8 characters long

        if len(password) < 8:
            error_message = "Password should be at least 8 characters long."
        else: 
            validity_score += 1
        # Check if password contains at least one uppercase letter

        if not re.search(r'[A-Z]', password):
            error_message = "Password should contain at least one uppercase letter."
        else: 
            validity_score += 1

        # Check if password contains at least one lowercase letter

        if not re.search(r'[a-z]', password):
            error_message = "Password should contain at least one lowercase letter."
        else: 
            validity_score += 1

        # Check if password contains at least one digit

        if not re.search(r'\d', password):
            error_message = "Password should contain at least one digit."
        else: 
            validity_score += 1

        # Check if password contains at least one special character

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            error_message = "Password should contain at least one special character."
        else: 
            validity_score += 1


        # ratings should be very weak - weak - moderate - strong - very strong 

        if validity_score >= 5:
            password_strength = "Very Strong"  
        elif validity_score == 4:
            password_strength = "Strong"
        elif validity_score == 3:
            password_strength = "Moderate"
        elif validity_score == 2:
            password_strength = "Week"
        else:
            password_strength = "Very Week"

        return error_message,validity_score,password_strength

# Uncommentb below code to test password strength from the user

# while True:
#     password = input("Enter a password: ")

#     result = Validator.test_password_strength(password)

#     if result[1] < 5:
#         print(f"The passowrd '{password}' entered is {result[2]}, {result[0]} \n Please try again.")
#     else:
#         print(f"The passowrd '{password}' entered is {result[2]}.")
#         break
    