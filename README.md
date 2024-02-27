
# Vention recruitment task

This project was created for recruitment purposes for a python internship at Vention.

## Setup
1. Clone the repository:
```
git clone https://github.com/Tarnac/vention_recruitment_task.git
cd vention_recruitment_task
```   
2. Create .env file based on .env.example:
```
SECRET_KEY=""
DEBUG=False
ALLOWED_HOSTS=*
```
3. Build the Docker image:
```
docker-compose up
```
4. Connect to created container using CONTAINER_ID:
```
docker ps -a
docker exec -it {CONTAINER_ID} bash
```
5.Run Django migration:
```
python manage.py migrate
```
6. Create admin account:
```
python manage.py createsuperuser
```
7. Visit http://127.0.0.1:8000/api/token/ to get JWT Token to access API.
8. To test existing endpoints visit http://127.0.0.1:8000/api/swagger-ui/.

## Testing
To run unit tests, follow the instruction below:
```
python manage.py test
```
