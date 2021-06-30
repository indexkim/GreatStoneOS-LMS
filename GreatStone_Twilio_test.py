#!/usr/bin/env python
# coding: utf-8


import datetime

tomorrow = datetime.date(2021,7,1) # 괄호 안에 예약문자를 전송할 날짜를 입력하세요. ex) 2021,7,1
days =['월', '화', '수', '목', '금', '토', '일']
tomorrow_day = days[tomorrow.weekday()]
tomorrow_daydate = tomorrow.strftime('%m/%d ('+tomorrow_day+')') 

if tomorrow_day == '일':
    later = datetime.timedelta(days=1) #월요일
    tomorrow = tomorrow + later
    tomorrow_day = days[tomorrow.weekday()]
    tomorrow_daydate = tomorrow.strftime('%m/%d ('+tomorrow_day+')')
    tomorrow = tomorrow.strftime("%Y-%m-%d") 
    print(f'입력하신 날짜는 일요일입니다. 다음 날짜 {tomorrow} 로 넘어갑니다.')

else:
    tomorrow = tomorrow.strftime("%Y-%m-%d")
    print(f'{tomorrow} 예약 문자 전송을 시작합니다.\n\n')


import pandas as pd

df1 = pd.read_excel(r'C:\Users\Jisoo\Desktop/emr_test.xlsx', sheet_name='SCHEDULE')
df2 = pd.read_excel(r'C:\Users\Jisoo\Desktop/emr_test2.xlsx', sheet_name='CONTACT')


is_A = df1[df1.iloc[:,2] == 'A']
is_tomorrow = is_A[['TIME', '선생님', tomorrow]]
A_tomorrow = is_tomorrow.join(df2.set_index('NAME')['NUMBER'], on=tomorrow)
A_tomorrow['NUMBER'] = A_tomorrow['NUMBER'].str.replace('-','')


number_error = A_tomorrow[A_tomorrow[tomorrow].notna() & A_tomorrow['NUMBER'].isna()]
reservation_cnt = len(A_tomorrow[A_tomorrow[tomorrow].notna()])
number_error_cnt = len(number_error[tomorrow].values)


for i in number_error.values:
    if len(i) >= 1 :
        print(tomorrow, i[0], i[2], '- 문자 전송 보류: 연락처를 확인하세요.')
        
    
A_tomorrow_pass = A_tomorrow.dropna()


from twilio.rest import Client

def send_message():
    account_sid = 'ACCOUNTSID000000000000000000'  # Twilio account sid
    auth_token = 'authtoken1111111111111111111' # Twilio auth token
    client = Client(account_sid, auth_token)
    from_number = "+827012345678" #고정
    message = client.messages.create(
        to=to_number, 
        from_=from_number,
        body=text)
    
for a in A_tomorrow_pass.values:
    time = a[0]
    tomorrow_daydatetime = tomorrow_daydate + ' ' +a[0]
    to_number = '+82'+a[3]
    send_msg = f'[XXX정형외과 도수치료실] {tomorrow_daydatetime} 도수치료 예약입니다. 변경 및 취소 문의시 070-1234-5678 연락 부탁드립니다.\n\n※병원위치 안내※\n▶XXX 건물(XXX 건물 옆, 1층에 XXXX,XXXX 위치해 있음.)X층으로 오시면 됩니다.'
    text = send_msg

    try:
        send_message()
        print(tomorrow, a[0], a[2], a[3], '전송 완료했습니다. 미리보기:', text[:41])
    except:
        print(tomorrow, a[0], a[2], a[3], '전송 실패했습니다. 미리보기:', text[:41])
        

tomorrow_xlsx = 'C:/Users/Jisoo/Desktop/' + tomorrow + '.xlsx'
with pd.ExcelWriter(tomorrow_xlsx, engine = 'xlsxwriter') as writer:
    A_tomorrow.reset_index(inplace=True)
    A_tomorrow.index = A_tomorrow.index + 1
    A_tomorrow = A_tomorrow.drop(['index'],axis=1)
    A_tomorrow.to_excel(writer, sheet_name=tomorrow+'_전체')
    
    A_tomorrow_pass.reset_index(inplace=True)
    A_tomorrow_pass.index = A_tomorrow_pass.index + 1
    A_tomorrow_pass = A_tomorrow_pass.drop(['index'],axis=1)
    A_tomorrow_pass.to_excel(writer, sheet_name=tomorrow+'_전송완료')
    
    number_error.reset_index(inplace=True)
    number_error.index = number_error.index + 1
    number_error = number_error.drop(['index'],axis=1)
    number_error.to_excel(writer, sheet_name='전송보류-연락처오류')
    writer.book.use_zip64()

    
cnt=len(A_tomorrow_pass)
if cnt == 0:
    print(f'{tomorrow} 일 예약된 내역이 없습니다. \n\n예약 문자 전송을 종료합니다.')    
else:
    print(f'\n\n{tomorrow} 일 총 예약 {reservation_cnt}건 중 {cnt}건 전송 완료, {number_error_cnt}건 전송 보류. \n{tomorrow_xlsx}로 결과를 저장합니다.\n예약 문자 전송을 종료합니다.')

    



#내일 날짜 자동계산

import datetime

today = datetime.date.today()
later = datetime.timedelta(days=1)
tomorrow = today + later
days =['월', '화', '수', '목', '금', '토', '일']
tomorrow_day = days[tomorrow.weekday()]
tomorrow_daydate = tomorrow.strftime('%m/%d ('+tomorrow_day+')') 

if tomorrow_day == '일':
    later = datetime.timedelta(days=2) #월요일
    tomorrow = today + later
    tomorrow_day = days[tomorrow.weekday()]
    tomorrow_daydate = tomorrow.strftime('%m/%d ('+tomorrow_day+')')
    tomorrow = tomorrow.strftime("%Y-%m-%d") 
    print(f'내일은 일요일입니다. 다음 날짜 {tomorrow} 로 넘어갑니다.')

else:
    tomorrow = tomorrow.strftime("%Y-%m-%d")
    print(f'{tomorrow} 예약 문자 전송을 시작합니다.\n\n')


import pandas as pd

df1 = pd.read_excel(r'C:\Users\Jisoo\Desktop/emr_test2.xlsx', sheet_name='SCHEDULE')
df2 = pd.read_excel(r'C:\Users\Jisoo\Desktop/emr_test2.xlsx', sheet_name='CONTACT')


is_A = df1[df1.iloc[:,2] == 'A']
is_tomorrow = is_A[['TIME', '선생님', tomorrow]]
A_tomorrow = is_tomorrow.join(df2.set_index('NAME')['NUMBER'], on=tomorrow)
A_tomorrow['NUMBER'] = A_tomorrow['NUMBER'].str.replace('-','')


number_error = A_tomorrow[A_tomorrow[tomorrow].notna() & A_tomorrow['NUMBER'].isna()]
reservation_cnt = len(A_tomorrow[A_tomorrow[tomorrow].notna()])
number_error_cnt = len(number_error[tomorrow].values)


for i in number_error.values:
    if len(i) >= 1 :
        print(tomorrow, i[0], i[2], '- 문자 전송 보류: 연락처를 확인하세요.')
        
   
A_tomorrow_pass = A_tomorrow.dropna()


from twilio.rest import Client

def send_message():
    account_sid = 'ACCOUNTSID000000000000000000'  # Twilio account sid
    auth_token = 'authtoken1111111111111111111' # Twilio auth token
    client = Client(account_sid, auth_token)
    from_number = "+827012345678" #고정
    message = client.messages.create(
        to=to_number, 
        from_=from_number,
        body=text)
    
for a in A_tomorrow_pass.values:
    time = a[0]
    tomorrow_daydatetime = tomorrow_daydate + ' ' +a[0]
    to_number = '+82'+a[3]
    send_msg = f'[XXX정형외과 도수치료실] {tomorrow_daydatetime} 도수치료 예약입니다. 변경 및 취소 문의시 070-1234-5678 연락 부탁드립니다.\n\n※병원위치 안내※\n▶XXX 건물(XXX 건물 옆, 1층에 XXXX,XXXX 위치해 있음.)X층으로 오시면 됩니다.'
    text = send_msg

    try:
        send_message()
        print(tomorrow, a[0], a[2], a[3], '전송 완료했습니다. 미리보기:', text[:41])
    except:
        print(tomorrow, a[0], a[2], a[3], '전송 실패했습니다. 미리보기:', text[:41])

    
tomorrow_xlsx = 'C:/Users/Jisoo/Desktop/' + tomorrow + '.xlsx'
with pd.ExcelWriter(tomorrow_xlsx, engine = 'xlsxwriter') as writer:
    A_tomorrow.reset_index(inplace=True)
    A_tomorrow.index = A_tomorrow.index + 1
    A_tomorrow = A_tomorrow.drop(['index'],axis=1)
    A_tomorrow.to_excel(writer, sheet_name=tomorrow+'_전체')
    
    A_tomorrow_pass.reset_index(inplace=True)
    A_tomorrow_pass.index = A_tomorrow_pass.index + 1
    A_tomorrow_pass = A_tomorrow_pass.drop(['index'],axis=1)
    A_tomorrow_pass.to_excel(writer, sheet_name=tomorrow+'_전송완료')
    
    number_error.reset_index(inplace=True)
    number_error.index = number_error.index + 1
    number_error = number_error.drop(['index'],axis=1)
    number_error.to_excel(writer, sheet_name='전송보류-연락처오류')
    writer.book.use_zip64()

    
cnt = len(A_tomorrow_pass)
if cnt == 0:
    print(f'{tomorrow} 일 예약된 내역이 없습니다. \n\n예약 문자 전송을 종료합니다.')    
else:
    print(f'\n\n{tomorrow} 일 총 예약 {reservation_cnt}건 중 {cnt}건 전송 완료, {number_error_cnt}건 전송 보류. \n{tomorrow_xlsx}로 결과를 저장합니다.\n예약 문자 전송을 종료합니다.')

    



