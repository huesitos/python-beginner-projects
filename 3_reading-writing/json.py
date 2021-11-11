import simplejson as json
import os


def main():
    file = "./ages.json"
    file_exists = os.path.isfile(file)

    if file_exists and os.stat(file).st_size != 0:
        old_file = open("./ages.json", "r+")
        data = json.loads(old_file.read())
        print("Current age is", data["age"], "--- adding a year.")
        data["age"] += 1
        print("New age is", data["age"])
    else:
        old_file = open("./ages.json", "w+")
        data = {"name": "Nick", "age": 27}
        print("No file found, setting default age to", data["age"])

    old_file.seek(0)
    old_file.write(json.dumps(data))
    old_file.close()


if __name__ == "__main__":
    main()
