# test-conceptu

## Installation with docker-compose

```
git clone https://github.com/psilva1982/test-conceptu
cd test-conceptu
docker-compose up -d
```

### Instalation with virtual env

```
git clone https://github.com/psilva1982/test-conceptu
cd test-conceptu
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py runserver
```

### Documentation
- See on [postman doc](https://documenter.getpostman.com/view/2491745/TzmCfsbM)

### Users
- admin / 1234
- test / 1234

### Access on 
- [Local](http://localhost:8000) - http://localhost:8000
- [Heroku](https://test-conceptu.herokuapp.com/) - https://test-conceptu.herokuapp.com/
