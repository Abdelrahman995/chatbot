import json, requests
import urllib.request
import io
import numpy as np
import ast ,cv2
import base64


#url = 'http://72.52.111.176:80/'
url='http://localhost:5000'
image = cv2.imread("images.jpg", 0).tolist()
params = dict(image1=image)
headers={"Token":"kdjsdskacvbbc217vpewe"}
resp = requests.post(url=url, data=json.dumps(params), headers=headers)
print ((resp.text))
