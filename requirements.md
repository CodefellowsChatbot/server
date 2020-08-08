# Software Requirements
## Vision

New students or returning students often have simple, easy-to-answer questions which could be answered by a chatbot using AI and a Machine learning model. This would be much faster than waiting for a human to answer them and hopefully save people some in-depth searches of the code fellows website. 

## Scope (In/Out)
* __IN SCOPE__: <br>
- The app will be able to scrape the Code Fellows web site for current data from which to compose responses to User queries.
- The app will provide info about available courses on the codefellows website.
- The app will provide a "best guess" for a link when it doesn't have the exact answer.
- The app will be able to provide the current tuition cost ("rack rate") for each class. <br>

* __OUT OF SCOPE__ - *What will your product not do*: 
My app does not attempt to convince the user that they are in conversation with another human.

### Minimum Viable Product
A Chat bot which you can interact with on the command line to get questions about code fellows answered (command line input and responses).

### Stretch Goals
To make the ChatBot recognize voice input and verbally respond.

## Functional Requirements
- A user can type any questions related to the code fellows website.
- A user can verballly ask a related questions and get a verbal respond from the ChatBot. <br>

### Data Flow
- There is a terminal version of the ChatBot. A user types some question in the terminal making request to the server part of the app. Then, on the server side, a request will be processed through the web scraper and machine learning (deep learning) model. The best match will be selected and sent to the user side as a response in text format. 
- As a stretch goal there will be ability for the voice input and voice output.

## Non-Functional Requirements (301 & 401 only)
* Our project will be __checked *Under Load*__ for the performance of the target application to represent the User Experience. It describes how fast or slow the Device-Under-Test responds, and how satisfied the user is with (or how the user actually perceives) performance.

* There also will be __usability testing__. The app will be tested for how often the user gets what they are looking for (how well the answer fit the original query). So we can track a percentage of 'right/fitting response'.