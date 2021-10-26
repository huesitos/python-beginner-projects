import requests


def main():
    my_data = {"name": "Denisse", "email": "denisse@gmail.com"}
    r = requests.post("https://tryphp.w3schools.com/demo/welcome.php", data=my_data)

    f = open("my_file.html", "w+")
    f.write(r.text)


if __name__ == "__main__":
    main()