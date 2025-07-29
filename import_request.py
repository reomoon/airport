import requests
import time

# 인천공항 제2터미널 주차장 예약 API를 사용하여
# check?date 날짜를 변경하여 true false를 확인할 수 있습니다.
url = "https://api.amanopark.co.kr/api/web/setting/booking/check?date=2025-08-01&type=BASIC"

while True: # true가 될 때까지 반복
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json() # JSON 응답을 파싱
            if result.get("data") is True:
                print("✅data가 True로 변경되었습니다!")
                break # true가 되면 반복문 종료
            else: # data가 False인 경우
                print("❗data가 False 입니다.")
        else:
            print(f"HTTP 오류: {response.status_code}")
    except Exception as e:
        print(f"오류 발생: {e}")
    time.sleep(3)