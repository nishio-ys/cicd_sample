@echo off
echo "Hello, Jenkins!"
echo %date% %time%

cd docker_mysql

echo '----------'
echo 'docker-compose up -d'
docker-compose up -d

echo '----------'
echo 'docker-compose ps'
docker-compose ps

echo '----------'
echo 'docker ps -a'
docker ps -a

echo '----------'
echo 'docker images -a'
docker images -a

echo '------------------------------------------------------------'
rem docker exec docker_mysql_db_1 bash -c "cd /var/dummy && ./failure.sh"
docker exec docker_mysql_db_1 bash -c "cd /var/dummy && ./success.sh"
IF %ERRORLEVEL% == 0 (
    docker stop docker_mysql_db_1
    docker rm docker_mysql_db_1
    docker rmi mysql:8.0
) ELSE (
    echo bat resulted in faiure
)
