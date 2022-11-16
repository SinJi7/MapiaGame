Mapia Game (판넬 이미지 readme 동일 경로 panel.png)
================
Lib, framework, language
----------------
- Python
- javascript
- react
- flask

소개
-----------------
react 사용 front 구현
flask 사용 back 구현

개발 진행상황
-----------------
front
- 채팅구현 완료
- class components에서 fucntion components로 변경 
    + 대략적 인게임 UI? 디자인 수정 예정 https://codepen.io/SinJi7/pen/vYrNgrp (class components UI)
- 페이지 하나에 전부 구현 예정이기에, class components로 다시 변경
- 조작 구현 완료

back
- Server
    + 채팅방 분리 완료
- Game Core
    + 대략적 구현 완료
    + 인터페이스 구체화 필요

프로그램 구조
-----------------
- 대략적 구조
```
<App.js>
<server.py>
<container.py>
<Core.py>
순서대로 구조화
```
- container has a Core
- App: front, User로 부터 데이터를 받음
- server: continer로 유저들을 관리한다
- contaner: 채팅방 컨테이너, 채팅방 관리 기능
- Core: 게임 기능 담당


계획
-----------------
- 채팅 부분 구현
    + 컨테이너 부분을 만들며, 같이 처리 하려하는 중 (완료)
- 방별로 채팅 구분 (완료)
- 방에 게임 추가 (진행중)
    + 낮/투표/밤 사이클 구현 (완료)
    + 직업분배 기능 구현 (테스트 미완료)
    + 상태에 따라 채팅 가능 여부 구분 (테스트 미완료) 

기타
-----------------
새로 프로젝트 변경 관계로 ReadMe 새로 작성

