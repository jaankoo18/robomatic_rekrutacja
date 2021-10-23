import sys
from sort_files import sort_files

if __name__ == "__main__":
    try:
        if len(sys.argv) >= 2:
            sort_files(sys.argv[1])
        else:
            print("No arguments!")

    except Exception as err:
        print(err)

    else:
        print("The program ran without exceptions!")

    finally:
        print("The program ended correctly!")