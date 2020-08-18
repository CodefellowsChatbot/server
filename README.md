# Codefellows ChatBot

## Team: Lee-Roy King, Thomas Sherer, Roman Sydoruk

## Description
Chat bot which you can interact with on the command line to get questions about code fellows answered (command line input and responses).



## Wire Frames
![img](./resources/wireframe.png)


## User Stories
https://github.com/orgs/CodefellowsChatbot/projects/2

## Software Requirements
[Software Requirements](./requirements.md)

## Domain Modeling
https://docs.google.com/drawings/d/1e66-ylESSl5mYymCikQwHw4gtOq5ZoySrtPB-eQhDbk/edit?usp=sharing

## Database
This app is not expecting to use a database.  


## Infrastructure/Orchestration
Primary build technology will be Docker and we will be deploying that container to heroku, but that should be easy to lift and shift to another hosting service if needed since it will already be containerized.

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

## Citations and Attributions

- Original inspiration and starter code - YouTube "Python Chat Bot Tutorial - Chatbot with Deep Learning," a five-part tutorial, the first of which is [here.](https://www.youtube.com/watch?v=wypVcNIH6D4&list=PLzMcBGfZo4-ndH9FoC4YWHGXG5RZekt-Q)

- __Skyler Burger__ helped with parsing JSON files and with mock test setup.

- __Merry Cimakasky__, __Lee-Roy King__ and [Real Python](https://realpython.com/testing-third-party-apis-with-mocks/) helped with mock testing.

- __.gitignore__ content courtesy of https://www.toptal.com/developers/gitignore/api/python

- [UML documentation intro](https://tallyfy.com/uml-diagram/#:~:text=A%20UML%20diagram%20is%20a,document%20information%20about%20the%20system.)


* __StackOverflow__ helped with 
- How to get POSTed JSON in Flask:
https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask/35614301#35614301
- How to exit Python script in Command Prompt:
https://stackoverflow.com/questions/41524734/python-how-to-exit-python-script-in-command-prompt

