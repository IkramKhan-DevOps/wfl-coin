

import requests
import json

while True:
    product_id = int(input("Enter Product ID: "))
    response = requests.get(f"https://exarth.com/api/exarth/project/{product_id}/")
    if response.status_code == 200:

        print(json.dumps(response.json(), indent=4))
        output = json.loads(json.dumps(response.json()))
        print(json.dumps(response.json()).id)
        print(output['id'])
        print(output['name'])
    else:
        print("There is issue code: ", response.status_code)

