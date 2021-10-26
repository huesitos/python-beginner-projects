def main():
    newfile = open("newfile.txt", "w+")
    string = "This is the content that will be written to the text file."
    newfile.write(string)


if __name__ == "__main__":
    main()