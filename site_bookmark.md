북마크 앱 만들기
====

1. 가상환경 구축
2. 파이썬 장고 설치
3. 수퍼 유저 생성
4. 앱 만들기

- blank 는 공백이라도 데이터가 있다
- null 은 아예 데이터가 없다

5. model 추가 등 DB에 변동 있을때는
    - python manage.py makemigrations  : 마이그레이션할 내용 생성
    - python manage.py migrate : 마이그레이션 실행
    
6. urls.py
    - namespace : 그룹에서 하위
    - name : url에서 찾는 것으로 지정
