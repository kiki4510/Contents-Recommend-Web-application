# Contents-Recommend-Web-application
OTT platform Contents Recommendation
## 문제정의 
* OTT 플랫폼 별 컨텐츠를 추천해주는 웹 어플리케이션 제작
## 데이터의 구성
* 데이터 크롤링을 통한 각 OTT플랫폼 별 데이터 마이닝 > 컨텐츠 제목, 장르 등의 DATA > 해당 데이터 사용의 어려움(보완 필요사항)
* IBDM RATING 데이터 From Kaggle 
## 프로젝트 진행과정
* 셀레니움을 이용해서 OTT 사이트 별 컨텐츠와 장르 크롤링
* SQLITE로 데이터 DB화 > DB화 시킨 데이터 사용 불가
* Movie Ratings Data로 추천 모델 생성(추천 비추천 일종의 이진분류모델)
* 타이틀과 장르 기입시 추천,비추천으로 결과 도출하는 웹어플리케이션(by FLASK)
### 보완 필요사항
* 크롤링 데이터를 이용한 검색 어플리케이션으로의 개선 필요/ 자체 모델의 성능 개선 필요
