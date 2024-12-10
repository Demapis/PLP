try:
    def file_handling(inFile, new_File):
        with open(inFile , "r") as file:
            content = file.read()
            print(content)
        modifie_cont = content + "/n hello python"

        with open(new_File , "w") as file2:
            file2.write(modifie_cont)

    inFile = input("enter the name of the file: ")
    new_File = input("enter the name of the new file: ")

    file_handling(inFile, new_File)

except FileNotFoundError:
    print("file not found")

