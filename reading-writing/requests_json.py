import requests
import simplejson as json


def main():
    url = "https://api-ssl.bitly.com/v4/shorten"
    # data that you send through a url
    payload = {
        "domain": "fiver.com",
        "longUrl": "https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/133376403/original/6a00ce34a936bc0c7eb6f54b705049e311856d7f/joseph-joestar-voice-actor.jpg"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "<token>"
    }

    r = requests.post(url, json=payload, headers=headers)

    print(r.headers)
    print(r.text)
    # print(json.loads(r.text)["errors"][0]["error_code"])


if __name__ == "__main__":
    main()