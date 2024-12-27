# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# 파이썬 라이브러리
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# +
# 데이터 불러오기 > population.csv


population = pd.read_csv("./data/population.csv",index_col = "도시")



# -

population

<<<<<<< HEAD
=======
>>>>>>> 25e36674efc8db341eb0e9886e03bbfe4afc2574
# 원하는 데이터 추출하기
# loc(Location) : 인덱스를 기준으로 행을 추출, '컬럼 이름으로 접근'
# loc[행, 열] -> ㄱ끝 열을 포함하지 않는다. ex) df명.loc[부산 : 인천]
# iloc(Integer Location) : 행 번호를 기준으로 데이터를 추출, '행 번호로 접근'
# iloc[행,열] -> 끝 열을 포함하는
population.loc['부산' : '인천']



# +
# 인천에 2015년도 인구수 행을 추출 > 2925815.0
# loc를 사용

population.loc['인천','2015']
# -

# 부산에서 인천까지의 2020년~2010년까지의 인구 수를 추출
population.iloc[1:3,1:4]

population.iloc[0:3,2:4]

population.loc['부산':'인천','2010']

# ### 그외 함수를 사용하기
#     - count() : 데이터 개수를 세는 함수
#     - values_counts() : 값이 숫자, 문자열, 카테고리 값인 경우에 각각의 값이 나온 횟수를 세는 함수
#     - sort_index() : 인덱스 값을 기준으로 정렬
#     - sort_values() : 데이터 값을 기준으로 정렬
#     - fillna() :  결측치(NaN) 에 원하는 값 지정

# +
# count()
# axis : 축방향
# axis = 0 :  행 축: 위에서 아래로 축 행을 기준으로 작업
# axis = 1 : 열 축: 왼쪽에서 오른쪽로 축 컬럼을 기준으로 작업

population.count(axis = 0)

# +
# 2020년도 특정 컬럼의 카룬트를 세워보자

population['2020'].value_counts()
# -

population.sort_values(by = '2010', ascending = False)
population.sort_values(by = ['지역','2020'], ascending = False)

# +
# 데이터 프레임 형태로 확인하고 싶은면 []안에 []를 쓴다.
population[['2015']]


population.fillna(value = 0)

# +
# 1. 라이브러리 불러오기 : train.csv
train = pd.read_csv("./train.csv", index_col = 'PassengerId')

# 2. train 이라는 변수에 저장
train

# +
# 데이터 정보
# PassengerId : 승객별 아이디
# Survived : 생존여부 > 0: 사망 1: 생존
# Pclass : 객싱 등급 1등급, 2등급, 3등급
# Sibsp : 합성어 > 배우자와 형제 자매가 같이 탑승한 수
# Parch : 합성어 > 같이 탑승 가족 수
# Fare : 요금
# Cabin : 객실 번호
# Embarked : 생선지 > S, C, Q

# +
# head() : 상단의 5개의 데이터만 보여줌
# tail(): 하단의 5개의 데이터만 보여줌

train.head()
train.count()

train['Embarked'].value_counts()

# +
# 연습문제 1
# 타이타닉호 승객 중 성별 인원수(Sex), 선실별 인원수(Pclass), 사망/생존의 인원수(survived)를 구하라.
print(train['Sex'].value_counts())

print(train['Pclass'].value_counts())

print(train['Survived'].value_counts())
# -

train[train['Sex']  == 'female'].value_counts('Survived')

# +
# 성별이 남자에 해당하는 사망/생존 의 인원수를 구하고
# male_survived 변수에 저장해보자!
male_survived = train[train['Sex']  == 'male'].value_counts('Survived')

male_survived

# +
<<<<<<< HEAD
## del(train['Age'])
## del(train['Cabin'])
##train['Embarked'].value_counts('S')
train['Embarked'].fillna(value = 'S',inplace = True)

train.count()
# -

import chardet
with open ('./data/hr-info.csv', 'rb') as f : 
    data = f.read()

chardet.detect(data)

# +
## 한글 인코딩의 종류 : EUC-KR, UTF-8, UTF-8-SIG, cp949
hr_info = pd.read_csv('./data/hr-info.csv',encoding = 'EUC-KR')
hr_info


# -


#DESC(Describe)



# +
# 급여의 총 합계

# df명.loc[행,열]
# df명.iloc[행,열]

# 1) 급여의 데이터를 시리즈 형태로 추출
hr_info.loc[:,'SALARY']
# 2) 급여의 데이터를 데이터프레임 형태로 추출
hr_info[['SALARY']]

# +
# 급여의 총 합계

hr_info.loc[: ,'SALARY'].sum()
### github체크
# -
# 급여의 평균 구하기 (전체 급여 합계 / 급여자의 수)
hr_info.loc[: ,'SALARY'].sum() / hr_info['SALARY'].count()


# +
# RETIRE_DATE(퇴직날짜) > NaN이 아닌 사항은 퇴작한 사람

# 퇴직한 직원의 수를 확인하기

# 정답
hr_info.loc[: ,'RETIRE_DATE'].count()
hr_info[hr_info['RETIRE_DATE'].notnull()].count()
# -

# 남/여 비율을 확인하기
hr_info.value_counts('GENDER')
hr_info[['GENDER']]
print(hr_info[hr_info['GENDER'] == 'M'].value_counts('GENDER'))
print(hr_info[hr_info['GENDER'] == 'F'].value_counts('GENDER'))

print(hr_info[hr_info.iloc[:, 2] == 'M'].value_counts('GENDER'))
print(hr_info[hr_info.iloc[:, 2] == 'F'].value_counts('GENDER'))
