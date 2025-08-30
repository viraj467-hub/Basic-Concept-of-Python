def read_file(sample):
    try:
        with open('sample.txt', "r") as file:
            print("Reading file content:\n")
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{sample}' was not found.")
read_file("sample.txt")
