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

배포시 도커에 다 넣고 하는게 좋았는지, volumn을 쓰는게 좋을지? -> 도커스럽게 하려면 도커에 다 넣고.
sudo pip 비추천 이유: sudo로 사용하는 경우, 내 로컬은 사용자 계정이기 때문에 둘이 매칭이 안 되어서 나중에 권한 문제가 생길 수 있음
-> 그러나 도커는 기본적으로 sudo. 컨테이너 안에서 무슨 일이 있어도 로컬 컴에 영향을 미치지 않기 때문에 문제 없다.

도커파일에 작성하지 않고, 배포 서버에서 명령어를 치다보면 기록으로 남지 않고 나중에 서버를 변경하게 되는 파편화도 일어날 수 있음