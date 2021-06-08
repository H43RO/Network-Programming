import requests

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
REST_API_KEY = '0c6b943595fb299f1edd9a630623de49'

headers = {
    'Authorization': "KakaoAK {}".format(REST_API_KEY)
}

files = {
    'image': open('profile.jpg', 'rb')
}

rsp = requests.post(API_URL, headers=headers, files=files)
print(rsp.json())
