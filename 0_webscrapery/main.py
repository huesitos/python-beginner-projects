from bs4 import BeautifulSoup
import requests


def main():
    search = input("Enter search term: ")
    params = {"q": search}
    r = requests.get("https://www.bing.com/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup.prettify())
    results = soup.find("ol", {"id": "b_results"})
    print("results", results)
    links = results.findAll("li", {"class": "b_algo"})
    print("links", links)
    print()

    for item in links:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]

        if item_text and item_href:
            print(item_text)
            print(item_href)
            # print("Parent", item.find("a").parent)
            print("Summary:", item.find("a").parent.parent.find("p").text)

            # children = item.children
            # for child in children:
            #     print("Child:", child)

            print("Next sibling:", item.next_sibling)
            print()


if __name__ == "__main__":
    main()
