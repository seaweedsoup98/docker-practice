# docker-practice

## 1) 프로젝트 개요
리눅스 터미널, Docker. Git/GitHub 사용 연습 프로젝트


## 2) 실행 환경
- OS: Sequoia 15.75
- Shell: zsh
- Docker version 28.5.2, build ecc6942
- Docker Compose version v2.40.3
- git version 2.53.0


## 3) 수행 체크리스트 
- [x] 터미널 기본 조작 및 폴더 구성 
- [x] 권한 변경 실습
- [x] Docker 설치/점검
- [x] hello-world 실행
- [x] Dockerfile 빌드/실행
- [x] 포트 매핑 접속
- [x] 바인드 마운트 반영
- [x] 볼륨 영속성 확인
- [x] Git 설정 + GitHub 연동
- [x] Docker Compose 세팅 및 운영
- [x] 환경 변수 주입


## 4) 수행 방법

```bash
# 현재 위치 확인
pwd

# 목록 확인(숨김 파일 포함)
ls -a

# 폴더 생성
mkdir src

# 폴더 이동
cd ./src/

# 빈 파일 생성
touch empty_file.txt

# 파일 생성
echo "Hello World" > file.txt

# 파일 내용 확인
cat file.txt

# 파일 권한 확인
ls -l file.txt

# 파일 권한 수정
chmod 600 file.txt

# 파일 복사 (폴더는 -r 옵션 필수)
cp file.txt file2.txt
cat file2.txt

# 파일 이동 (폴더 이동은 -r 옵션 필요 없음)
mv file2.txt ../
cd ../ && cat file2.txt

# 파일 이름 변경
mv file2.txt src/file3.txt
cat src/file3.txt

# 파일 삭제 (폴더는 -r 옵션 필수)
rm src/file3.txt

# Docker 버전 확인
docker version

# Docker 데몬 동작 여부 확인
docker info

# Docker hello-world 실행
docker run hello-world

# Docker 이미지 목록 확인
docker images
docker image ls

# Docker 이미지 다운로드
docker pull nginx:alpine

# Docker 이미지 빌드
docker build -t basic-web:1.0 ./web
docker build -t basic-linux:1.0 ./linux
docker image ls

# Docker 컨테이너 네트워크 생성
docker network create practice-net
docker network ls

# Linux 컨테이너 실행
docker run -d \
    --name linux \
    --network practice-net \
    -e APP_MODE=manual \
    -e PORT=8080 \
    basic-linux:1.0

# Web 컨테이너 실행
docker run -dit \
    --name web \
    --network practice-net \
    -p 8080:80 \
    -v "$PWD/logs:/logs" \
    basic-web:1.0

# Docker 컨데이터 상태
docker ps
docker ps -a

# 포트 매핑 확인
docker port web

# 정적 페이지 요청
curl http://localhost:8080

# Web에서 Linux 컨테이너로 요청
curl http://localhost:8080/who

# 환경변수 변경 (포트)
docker run -d \
    --name linux-env \
    -e APP_MODE=port-test \
    -e PORT=9090 \
    -p 9090:9090 \
    basic-linux:1.0

# 환경변수 변경 확인
docker exec linux-env printenv APP_MODE PORT
curl http://localhost:9090

# 변경 실험 정리
docker rm -f linux-env

# 컨테이너 간 직접 통신 확인 (exec)
docker exec web curl -s http://linux:8080/who

# Linux 사용자 확인
docker exec linux whoami

# Linux curl 설치 확인
docker exec linux curl -s http://localhost:8080

# 볼륨 마운트와 로그 확인
ls -l logs
cat logs/access.log
docker exec web cat /logs/access.log

# 요청을 한 번 더 보낸 후 로그 추가 확인
curl http://localhost:8080/who
tail logs/access.log
docker exec web tail /logs/access.log

# exec vs attach: exec은 새로운 프로세스를 실행
docker exec -it linux sh
whoami
pwd
ps
exit

# exec vs attach: 따라서 exec은 shell에서 exit해도 메인 서버는 계속 실행됨
docker ps
curl http://localhost:8080/who

# exec vs attach: attach는 컨테이너 메인 프로세스인 Nginx의 표준 출력과 표준 오류에 현재 터미널을 연결한다.
docker attach web

# exec vs attach: 두 번째 터미널을 열어 Web 컨테이너에 요청을 보내면 Nginx 접근 로그가 나타난다.

# exec vs attach: attach는 메인 프로세스에 직접 접근하기 때문에 Ctrl-c로 중지하면 안 된다! (Ctrl-p, Ctrl-q 로 detach)

# 실행 환경 정리 (docker compose 실습용)
docker rm -f web linux
docker network rm practice-net
docker ps -a

# 컨테이너가 종료되더라도 마운트한 로그는 남아있어야 한다.
cat logs/access.log

# 환경변수 파일 생성
cp .env.example .env

# Compose 버전 확인
docker compose version

# Compose 파일 문법 확인
docker compose config

# Compose 빌드하고 백그라운드 실행 (-d)
docker compose up -d --build

# Compose 상태 확인
docker compose ps

# Compose 환경변수 확인
docker compose exec linux printenv APP_MODE
docker compose exec linux printenv PORT

# 서비스 호출
curl http://localhost:8081
curl http://localhost:8081/who

# Compose 전체 로그 확인
docker compose logs
docker compose logs --tail 10

# Compose Web 로그 실시간 확인 (로그 추적 끝낼 땐 Ctrl-c)
docker compose logs -f web
docker compose ps

# Compose 환경에서 exec
docker compose exec linux whoami
docker compose exec web curl -s http://linux:8081/who
docker compose exec linux sh
whoami
exit

# Compose 종료 및 제거
docker compose down
docker compose ps

# 로그 파일은 여전히 영속성을 지니므로 남는다.
cat logs/access.log

# GitHub logs/ 폴더 업로드
touch logs/.gitkeep

# GitHub 사용자 설정
git config --local user.name seaweedsoup98
git config --local user.email seaweedsoup98@gmail.com

# GitHub 업로드
git add .
git commit -m "Add basic Docker practice codes"
git push
git status
```


## 5) 수행 로그
`terminal.log` 참고


## 6) 트러블슈팅 내역

### 1. zsh에서 ₩!₩ 사용 문제

```bash
echo "Hello World!" > src/file.txt
```

위 명령 실행 시 ₩dquote>` 라는 따옴표 마무리 요구 명령이 표출됨. 원인 파악 결과 ₩!₩는 zsh(또는 bash)에서 히스토리 확장을 담당하는 특수 문자로, 이전에 실행한 명령을 다시 불러오는 기능이 있었음. 따라서 명령어에서 느낌표를 제거하거나, 혹은 사용하고 싶은 경우 escape 표기로 사용할 수 있음을 알게됨.
