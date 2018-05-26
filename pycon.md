# Pycon 5월 세미나 '나만의 파이썬 레시피'
## docker compose로 python 사용 환경 구성하기
### docker 
- 웹 서버 환경을 컨테이너로 추상화하여 개발 및 배포를 편리화한 도구  

- **개발 및 배포의 편리성 외에도 새로운 팀원이 on board할 경우, 인계가 수월해지는 효과가 있음**  
(현실적으로 개발 서버 실행시 겪은 수많은 오류들을 기록해놓을 수 없는데, Dockerfile, docker-compose.yml과 버전 관리 툴을 합치면 해당 서버 실행, 배포시 필요한 것이 정확히 무엇인지 알 수 있음)

### docker 실행

```python
docker run -it python:3
# python3 = docker 이미지 -> 클래스 (build)
# 실행 중인 python3 = 실제 컨테이너 -> 인스턴스 (run)
```

### 실제 사용 팁
- 개발용 (dockerfile-dev) /배포용 (dockerfile)을 따로 만들어서 개발, 배포, 관리

- docker error 예: no space left on device 
1. meaning: build가 쌓여서 가상 디스크가 꽉 차서 발생함
2. solution: docker for osx's setup ->  reset -> reset disc -> start all over again

### Q&A
Q1. 배포시 docker에 다 넣고 하는게 좋았는지, volumn을 쓰는게 좋았는지?  
A1. docker스러운 것은 docker에 관련 파일을 모두 넣고 배포하는 것이 맞는 것 같음

Q2. sudo pip 비추천하는 이유는?  
A2. sudo를 사용하여 설치하는 경우, 설치했던 root 계정과 나의 로컬 사용자 계정이 매칭이 안 되어서 나중에 권한 문제가 생길 수도 있음  
도커는 기본적으로 sudo 권한이나 컨테이너 안에서 무슨 일이 있어도 로컬 컴에 영향을 미치지 않기 때문에 문제 없음

Q3. docker가 인계에 도움이 된다는 표현이 잘 와닿지 않는다  
A3. dockerfile에 작성하지 않고, 배포 서버에서 명령어를 직접 쳐서 관리하다보면 기록으로 남지 않고, 해당 내용을 알려줄 사람이 없는 경우, 나중에 서버를 변경하게 되는 파편화도 일어날 수 있음