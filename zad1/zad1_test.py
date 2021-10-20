from palindorme_functions import isPalindorme

if __name__ == "__main__":
    try:
        potential_palindrome = input("Give potential palindrome: ")
        answer = isPalindorme(potential_palindrome)
        print(answer)

    except Exception as err:
        print(err)

    else:
        print("The program ran without exceptions!")

    finally:
        print("The program ended correctly!")