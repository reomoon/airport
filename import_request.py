import requests
import time

url = "https://api.amanopark.co.kr/api/web/setting/booking/check?date=2025-08-01&type=BASIC"

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            if result.get("data") is True:
                print("✅data가 True로 변경되었습니다!")
                break
            else:
                print("❗아직 data가 True가 아닙니다.")
        else:
            print(f"HTTP 오류: {response.status_code}")
    except Exception as e:
        print(f"오류 발생: {e}")
    time.sleep(3)