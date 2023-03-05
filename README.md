# ⭐ GaBo-SiJang

전통시장에 대한 정보를 알려주는 웹 사이트
<br> <br><br>


## ⭐ 문제 인식
 조선비즈의 한 신문기사에 따르면 15년 간 서울 중구 남대문시장에서 장사를 한 서모(58)씨는 하루에 옷 한 벌 파는 것도 힘들다고 말했다. 이 사실을 접하고 현대인들의 소비 행태가 예전과 많이 달라졌음을 실감하였고, 특히 젊은 층의 전통시장 이용률을 높이는 방안이 필요하다고 생각했다. 그래서 전통시장 현황과 시장에 파는 음식과 여러 리뷰를 제공하여 커뮤니케이션 하는 웹사이트를 통해 전통시장 이용을 활성화하는 방안을 채택하였다.<br> 
	<br><br>
	
	
## ⭐ 사용 기술 
### FrontEnd<br>
  - html, css<br>
  - Bootstrap : 프론트엔드 개발을 빠르고 쉽게 할 수 있는 프레임워크이다. <br>
  - html과 css 기반의 템플릿 양식, 버튼 등의 여러 컴포넌트를 지원한다. <br>
  - jinja2<br>
### BackEnd<br>
  - Python3 <br>
  - Flask : 파이썬으로 작성된 마이크로 웹 프레임워크 중 하나로 Werkzeug 툴킷과 Jinja2 템플릿 엔진에 기반을 둔다.<br>
  - sqlite <br>
  - sqlalchemy : 파이썬으로 작성된 ORM이며 특정 데이터베이스용으로 구축된 DBAPI 구현과 함께 작동하도록 설계되었다. 다양한 유형의 DBAPI 구현 및 데이터베이스와 통신하기 위해 dialect 시스템을 사용한다.<br>
  <br><br>
  
## ⭐ 개발 일정 (5/10 ~ 6/7)
5/10&#126;5/16 : 화면 구성 (정적 파일 만들기, 라우터 구현), URL 구조 구성 <br>
5/17&#126;5/23 : 데이터베이스 설계<br>
5/24&#126;5/30 : 시장 정보 보여주기 기능 추가, 리뷰 작성 기능 추가<br>
5/31&#126;6/6 : 리뷰 수정/삭제 기능 추가, 리뷰란 평점 추가 <br>
6/7&#126;6/13 : 평점 순, 지역이름 순으로 시장리스를 정렬하는 기능 추가, 코드 리팩토링
<br><br>

## ⭐ UI 구성
- index.html
![image](https://user-images.githubusercontent.com/81086966/194271780-834042e2-cb2c-43ec-be33-eb0ff18c116d.png)

- market-list.html
![image](https://user-images.githubusercontent.com/81086966/194271840-a192c18c-b946-4907-aba1-68f3161db531.png)

- datail.html
![image](https://user-images.githubusercontent.com/81086966/194271871-c1e98bd9-f5c4-473e-ba34-f02b6cb11c55.png)

- create.html
![image](https://user-images.githubusercontent.com/81086966/194271902-f1719cb8-5ef9-49a7-bd36-d4583399a277.png)

<br><br>


## ⭐ 프로젝트 기능
- 리뷰 CRUD
	- create : http 메소드가 post인 경우, 폼데이터를 통해 review 객체를 만든다. 그	  리고 controller로 create_review 함수를 호출하여 데이터베이스에 추가한다
	- read : market과 그 market의 review들을 전부 데이터베이스에서 찾아 뷰로 넘	  긴다. 아래 코드는 controller의 정렬한 데이터를 가져오는 함수이다.
	- update : http 메소드가 post인 경우, 입력된 password가 데이터베이스에 있는 	  값과 일치하면, 기존 객체의 값을 새로 입력된 값으로 바꾸고 controller로 		  update_review 함수를 호출하여 데이터베이스에 반영한다.
	- delete : review 객체를 찾아 삭제하고 controller로 delete_review 함수를 호출	  하여 데이터베이스에 반영한다.
- 평점 계산 
	- controller에 평점을 계산하는 함수를 만들었다. review의 개수만큼 반복하여 평	  점 합계와 리뷰 개수를 구하고, 평점 평균을 구해 데이터베이스를 commit한다.
	- 이 함수는 리뷰가 추가, 수정, 삭제되었을 때 마다 controller에서 호출하였다. 
- 평점 순, 지역 명 순으로 전통시장 리스트 보기
	- market-list 라우터에서 controller의 order_by_city 함수와 order_by_score 함수를 호출하여 평점 순, 지역 명 순으로 정렬된 데이터를 모두 가져와 뷰에 넘긴다.
	- 뷰는 버튼 클릭 이벤트에 따라 데이터를 선택적으로 보여준다.
  
  
## ⭐ URL 구조
router|host명|query string|렌더링 할 html(get 요청일 경우)
:---:|:---:|:---:|:---:
index|/|없음|index.html
market_list|/market-list|area_id|market-list.html
detail|/detail|market_id|detail.html
create|/create|market_id|create.html
update|/update|review_id|update.html
delete|/delete|review_id|index.html로 redirect


<br><br>


## ⭐ 프로젝트 아키텍처
![image](https://user-images.githubusercontent.com/81086966/194269009-7a456292-4b53-40e3-bfd8-693d84d43e9b.png)

- App 
	- User의 요청을 받아 요청 정보를 파악하여 Controller를 호출한다.
	- Controller에서 받은 정보를 총해 html을 렌더링하여 User에게 response를 제공한다.

- Controller 
	- 핵심적인 로직을 모아둔 곳이다.
	- Controller는 리뷰 만들기, 리뷰 수정하기, 리뷰 삭제하기, 평점 계산하기, 쿼리를 통해 데이터베이스에 접근하기 핵심적인 함수들을 포함한다. 

- Model
	- SQLAlchemy를 이용해 테이블로 만들 파이썬 클래스들을 모아두었다.

<br><br>

## ⭐ 데이터베이스 구조
![image](https://user-images.githubusercontent.com/81086966/194268835-2a40114a-df50-4bff-86d6-9c18ba8facd5.png)
<br><br>


