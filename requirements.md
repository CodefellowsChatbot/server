# Software Requirements
## Vision

New students or recurring students often have simple easy to answer questions which could be answered by a chatbot using AI and Machine learning model. This would be much faster than waiting for a human to answer them and hopefully save people some in depth searches of the code fellows website. 

## Scope (In/Out)
* IN - The app will be able to scrape the Code Fellows web site for current data from which to compose responses to User queries.
The app will provide info about available courses on the codefellows website.
The app will provide a "best guess" for a link when it doesn't have the exact answer.
The app will be able to provide what the tuition for each class is.
* OUT - What will your product not do.
My app will never have a human be like conversation with a user.

### Minimum Viable Product vs
Chat bot which you can interact with on the command line to get questions about code fellows answered (command line input and responses).

### Stretch
To make the ChatBot to recognize the voice and verbally respond.

## Functional Requirements

A user can type any questions related to the code fellows website.
A user can verballly ask a related questions and get a verbal respond from the ChatBot.
### Data Flow
There is a terminal version of the ChatBot. A user type some question in the terminal making request to the server part of the app. Than on the server side a reguest will be processed through web scraper and machine learning model (deep learning). The best match will be taken and sent a respond to hte user side in text format. As a stretch goal there will be ability for the voice input and voice output.

## Non-Functional Requirements (301 & 401 only)
Our project will be checked for the performance of the target application here would be the User Experience Under Load. It describes how fast or slow the DUT responds, and how satisfied or how the user actually perceives performance.


Security
Usability
Testability
etc….
Pick 2 non-functional requirements and describe their functionality in your application.

If you are stuck on what non-functional requirements are, do a quick online search and do some research. Write a minimum of 3-5 sentences to describe how the non-functional requirements fits into your app.

You MUST describe what the non-functional requirement is and how it will be implemented. Simply saying “Our project will be testable for testibility” is NOT acceptable. Tell us how, why, and what.