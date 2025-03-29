import requests
import time
import json
api_key = "7239ccb0-8d34-41c1-a08e-3dbe3b3bbcdc"
authorization = f"Bearer {api_key}"
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": authorization
}
# url = "https://cloud.leonardo.ai/api/rest/v1/init-image"
payload = {"extension": "jpg"}
# print(response.status_code)
def Generate_Image():
    try:
        url = "https://cloud.leonardo.ai/api/rest/v1/generations"
        payload = {
            "height": 512,
            "width": 512,
            "modelId": "6b645e3a-d64f-4341-a6d8-7a3690fbf042",
            "prompt": "A realistic Harry Potter-style cat on a table that holds a magic wand in his right paw and wears a red mantle."
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            print("errror")
        else:
            generation_id = response.json()["sdGenerationJob"]["generationId"]
            print("Waiting for image tgeneration to complete.")
            time.sleep(20)
            url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}"
            print(url)
            response = requests.get(url, headers=headers)
            print(response.json())
    except:
        print("error")
Generate_Image()
