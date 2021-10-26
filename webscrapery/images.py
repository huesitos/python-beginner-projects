from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO


def main():
    search = input("Search for image: ")
    params = {"q": search}
    r = requests.get("https://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)

    links = soup.findAll("img", {"class": "mimg"})
    print(links)

    count = 1
    for item in links:
        img_obj = requests.get(item.attrs["src"])
        img = Image.open(BytesIO(img_obj.content))
        img.save(f"./scraped_images/{search}{count}.{img.format}", str(img.format).lower())
        count += 1


if __name__ == "__main__":
    main()