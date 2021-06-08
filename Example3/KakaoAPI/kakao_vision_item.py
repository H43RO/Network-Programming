import requests
from PIL import Image, ImageDraw
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/product/detect'
REST_API_KEY = '0c6b943595fb299f1edd9a630623de49'


def detect_product(image_url):  # app_key와 이미지 파일의 URL을 POST로 전송하여 상품 검출을 수행
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'image_url': image_url}
    resp = requests.post(API_URL, headers=headers, data=data)
    return resp.json()  # 검출 결과를 딕셔너리로 변환하여 반환


# 상품 검출 결과를 이미지에 표시하는 함수
def show_products(image_url, detection_result):
    image_rsp = requests.get(image_url)
    file_jpgdata = BytesIO(image_rsp.content)
    image = Image.open(file_jpgdata)
    # URL 이미지 다운로드
    draw = ImageDraw.Draw(image)
    for obj in detection_result['result']['objects']:
        x1 = int(obj['x1'] * image.width)
        y1 = int(obj['y1'] * image.height)
        x2 = int(obj['x2'] * image.width)
        y2 = int(obj['y2'] * image.height)
        # 검출 위치에 사각형 그리기
        draw.rectangle([(x1, y1), (x2, y2)], fill=None, outline='red', width=2)
        draw.text((x1 + 5, y1 + 5), obj['class'], (255, 255, 0))  # 상품 이름 그리기
    del draw
    return image


if __name__ == "__main__":
    IMAGE_URL = 'https://p.kakaocdn.net/th/talkp/wmbOXVOIV9/aKtMoWYi4P4NrK5nrCodk0/s2rwz0_640x640_s.jpg'
    detection_result = detect_product(IMAGE_URL)
    image = show_products(IMAGE_URL, detection_result)
    image.show()
