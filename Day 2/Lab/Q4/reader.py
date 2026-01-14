from writer import write_numbers_to_file

def read_numbers_from_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()

        print("File Content:")
        print(content)

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")

    except Exception as e:
        print("Unexpected error:", e)


# Program execution
filename = "numbers.txt"

write_numbers_to_file(filename)
read_numbers_from_file(filename)
