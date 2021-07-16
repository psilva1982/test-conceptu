# test-conceptu

## Create python3 environment
```
python3 -m venv venv
```

### Activate environment
```
source venv/bin/activate
```

### Install dependencies 
```
pip install -r requirements-dev
```

### Run migrations 
``` 
python manage.py migrate
```

### Run local
```
python manage.py runserver
```

### Users 
- admin / 1234
- test / 1234  

### Test
- See on [localhost](http://127.0.0.1:8000/)
- See on [heroku](https://test-conceptu.herokuapp.com)


### API Documentation 
- See on [postman doc](https://documenter.getpostman.com/view/2491745/TzmCfsbM)

### Get access token   
```
curl -d '{"username":"admin", "password":"1234"}' -H "Content-Type: application/json" -X POST https://test-conceptu.herokuapp.com/api/token/
```

### Sending request with token 
```
curl https://test-conceptu.herokuapp.com/books/ -H "Accept: application/json" -H "Authorization: Bearer {token}"
```