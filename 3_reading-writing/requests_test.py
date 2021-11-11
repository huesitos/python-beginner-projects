import requests


def main():
    params = {"q": "pizza"}
    r = requests.get("http://bing.com/search", params=params)
    print("Status:", r.status_code)

    print(r.url)
    # text has the html and any text returned
    # print(r.text)

    f = open("./page.html", "w+")
    f.write(r.text)
    f.close()


if __name__ == "__main__":
    main()
