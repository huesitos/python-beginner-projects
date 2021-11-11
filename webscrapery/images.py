from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def start_search():
    search = input("Search for image: ")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("https://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("img", {"class": "mimg"})

    count = 1
    for item in links:
        try:
            print("Getting", item.attrs["src"])
            img_obj = requests.get(item.attrs["src"])

            img = Image.open(BytesIO(img_obj.content))
            img.save(f"./{dir_name}/{search}{count}.{img.format}", str(img.format).lower())
            count += 1
        except:
            print("Could not save image.")

    start_search()


def main():
    start_search()


if __name__ == "__main__":
    main()
