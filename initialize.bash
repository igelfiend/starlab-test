docker container stop starlab_postgres_db
docker-compose down --rmi all --volumes
docker-compose build
docker-compose up -d db
sleep 1
docker-compose run starlab-test-app alembic upgrade head
