cd docker_mysql
docker-compose up -d
docker-compose ps

docker exec docker_mysql_db_1 bash -c "cd /var/dummy && ./failure.sh"
echo %errorlevel%

docker exec docker_mysql_db_1 bash -c "cd /var/dummy && ./success.sh"
echo %errorlevel%
