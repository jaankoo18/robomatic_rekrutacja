def isPalindorme(text):
    if len(text) >= 1:
        str(text).lower()

        text_converted = []

        for i in str(text):
            if i.isalpha():
                text_converted.append(i)

        for i in range(0, len(text_converted)):
            if text_converted[i] != text_converted[::-1][i]:
                return "IS NOT PALINDROME"
            else:
                return "IS PALINDROME"

    else:
        raise MyError("Text is empty!")


class MyError(Exception):
    def __init__(self, p1):
        self.parametr1 = p1

    def __str__(self):
        return "Exception: " + self.parametr1






