This is a basic readme for the server


## Current build/deploy instructions

**build command**
```
docker build -t mvpflask:latest .
```

**run container locally (requires docker)**
```
docker run -d -p 5000:5000 mvpflask:latest
```
Should now be reachable on localhost:5000/ and localhost:5000/question


**heroku deployment** where `mvpflask` is name of app on heroku
```
heroku create mvpflask
heroku container:push web --app mvpflask
heroku container:release web --app mvpflask
```

