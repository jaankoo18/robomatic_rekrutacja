import sys
from find_bigest_blue_element import find_biggest_blue_element

#parametrem wywołania powinna być ścieżka do zdjęcia
if __name__ == "__main__":
    try:
        if len(sys.argv) >= 2:
            find_biggest_blue_element(sys.argv[1])
        else:
            print("No arguments!")

    except Exception as err:
        print(err)

    else:
        print("The program ran without exceptions!")

    finally:
        print("The program ended correctly!")