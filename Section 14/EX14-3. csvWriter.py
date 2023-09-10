import csv
'''
with open('차량관리.csv', 'w', encoding='UTf-8') as file:
    csv_maker = csv.writer(file,delimiter=',') #객체 만들기 
    csv_maker.writerow([1,'08러1234','2023-06-11,12:00']) #쓰는 친구 1줄씩 써서 추가 
    csv_maker.writerow([2,'25다1234','2023-06-11,12:00'])
    csv_maker.writerow([1,'28하1234','2023-06-11,12:00'])

print('차량관리.csv 파일이 생성되었습니다.')
'''
#2번 방식
with open('차량관리.csv', 'w', newline='', encoding='UTf-8') as file:
    csv_maker = csv.writer(file,delimiter=',') #객체 만들기
    csv_maker.writerow([1,'08러1234','2023-06-11,12:00']) #쓰는 친구 1줄씩 써서 추가
    csv_maker.writerow([2,'25다1234','2023-06-11,12:00'])
    csv_maker.writerow([1,'28하1234','2023-06-11,12:00'])

print('차량관리.csv 파일이 생성되었습니다.')

#3번 방식
with open('차량관리.csv', 'w', newline='', encoding='UTf-8') as file:
    csv_maker = csv.writer(file,delimiter=',', quotechar=' ') #쌍따옴표 안붙어질때 해당
    csv_maker.writerow([1,'08러1234','2023-06-11,12:00']) #쓰는 친구 1줄씩 써서 추가
    csv_maker.writerow([2,'25다1234','2023-06-11,12:00'])
    csv_maker.writerow([1,'28하1234','2023-06-11,12:00'])

print('차량관리.csv 파일이 생성되었습니다.')