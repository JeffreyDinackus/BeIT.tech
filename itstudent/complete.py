import requests
import random
def complete():

#this is a random number that is added to the NFT referencing the job
    job_number = random.randomint("1000, 9999") 

    url = "https://api.verbwire.com/v1/nft/mint/mintFromMetadata"

    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"chain\"\r\n\r\ngoerli\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        "accept": "application/json",
        "content-type": "multipart/form-data; boundary=---011000010111000001101001"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)