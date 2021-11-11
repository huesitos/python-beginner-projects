import requests
from io import BytesIO
from PIL import Image


def main():
    r = requests.get("https://m.media-amazon.com/images/I/61oI2+vCOeL._AC_SL1500_.jpg")
    print("Status code:", r.status_code)

    # content is binary data
    image = Image.open(BytesIO(r.content))

    print(image.size, image.format, image.mode)
    path = f"./joseph.{str(image.format).lower()}"

    try:
        image.save(path, image.format)
    except IOError:
        print("Cannot save image")


if __name__ == "__main__":
    main()