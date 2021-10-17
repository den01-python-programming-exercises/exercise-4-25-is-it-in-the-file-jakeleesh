def main():
    #write your code below this line
    file_name = input("Name of the file:")
    try:
        search = input("Search for:")
        f = open(file_name, "r")
        data = f.read().splitlines()
        if search in data:
            print("Found!")
        else:
            print("Not found.")
    except:
        print("Reading the file " + file_name + " failed.")

if __name__ == '__main__':
    main()
