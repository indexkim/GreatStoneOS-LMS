# GreatStoneOS_LMS



## 도수치료 예약 안내 문자 전송하기
- 예약 스케줄 관리는 Google Spread Sheet를 사용하며, A, B, C 선생님과 대표원장이 내용을 공유한다.
- A선생님은 익일 예약 내역을 확인한 후 EMR(Electronic Medical Record) 솔루션의 문자 전송 기능을 통해 환자에게 예약 문자를 발송한다.
- 파일 열기 > 6월 26일 예약 내역 확인 > 9시 예약 김지수 > EMR에서 김지수 검색 및 문자 발송 > 10시 예약 이지수 > EMR에서 이지수 검색 및 문자 발송 > ... > 전원 문자 발송 완료
- 목표: 익일 예약 환자에게 예약 문자를 일괄 발송하고 싶다.

## check
- 진료시간: 평일 9:00 ~ 19:00, 화,목(야간진료) 9:00 ~ 20:00, 점심시간 1:00 ~ 2:00, 토요일 09:00 ~ 14:00(점심시간 없음), 공휴일 휴무
- A선생님 환자만을 대상으로 한다.
- 예약 스케줄 관리 파일의 테이블 구조는 기억나는 대로 최대한 유사하게 구현했으며, 환자 연락처 DB는 임의로 구성함.
- 사용중인 EMR의 API 지원 여부는 아직 확인되지 않아 Twilio로 테스트함
- 문자 양식을 그대로 사용한다.

  [Web발신]

  [###정형외과 도수치료실] 6/25(금) 5시 도수치료 예약입니다. 변경 및 취소 문의시 ###-####-#### 연락 부탁드립니다.

  ※병원위치 안내※ 

  ▶### 건물(### 건물 옆, 1층에 ####, ### 위치해 있음.)#층으로 오시면 됩니다.
