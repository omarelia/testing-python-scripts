import json

from pprint import pprint
from octopus import Octopus


def create_request(urls):
    data = []

    otto = Octopus(
           concurrency=4, auto_start=True, cache=True, expiration_in_seconds=10
    )

    def handle_url_response(url, response):
        if "Not found" == response.text:
            print ("URL Not Found: %s" % url)
        else:
            data.append(response.text)


    for url in urls:
        otto.enqueue(url, handle_url_response)

    otto.wait()

    json_data = json.JSONEncoder(indent=None,
                                 separators=(',', ': ')).encode(data)

    return pprint(json_data)


print(create_request(['http://www.mocky.io/v2/5eae014f2f000058001988d6']))



