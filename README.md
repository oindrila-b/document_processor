# Documento [Client Side]

## What is Documento?

Documento is a Fullstack application built using React JS and Python. 
This repository contains the backend, i.e, the Server Side of the application. Documento allows the user to make a summary out of their document or get answer to questions regarding their document. Documento uses two NLP models to process the Document.
The first model is :
1. [The Bart Large CNN model by Facebook](https://huggingface.co/facebook/bart-large-cnn) - This model was used to process the data or content sent to the backend server and create a summary out of the context.
2. [Deepset's Roberta Base Squad2](https://huggingface.co/deepset/roberta-base-squad2) - This model was used to process the data or content sent to the backend server and answer questions regarding the context sent to it.
    

This application runs on `http://localhost:5000`

### Repositories :

1. Frontend - [document-processor-client](https://github.com/oindrila-b/document-processor-client)
2. Backend - [document-processor](https://github.com/oindrila-b/document_processor)


### Main Functionalities
The main functionalities of the backend server are the : 
1. Summary Feature - This feature can be found on the endpoint - `http://localhost:5000/getSummary`. It has only one parameter that needs to be passed, `context`. The context parameter is needed for the server to create a summery for the client side. A sample request to this endpoint should look like this  : `http://localhost:5000/getSummary?context={your_context}`. Once it has the context, it uses the model and generates a summary with respect to the context.
2. Question Answering Feature -  This feature can be found on the endpoint - http://localhost:5000/askQuestion. It has two parameters that needs to be passed, `query_context` and `question`. The questions are answered with respect to the query_context send to the server. A sample request to this endpoint should look like this : `http://localhost:5000/askQuestion?question={your+question}&query_context={your_context}`

### Key Challenges Faced
 The Key Challenges Faced during this project was 
 1. Making sure cross origins was enabled.
 2. Dealing with large chunks of data. Since summarization model has a token limit of 1024 words, it wasn't possible to directly send the data to the model for summary. There were only two options, either we could truncate the large sized context or we could've separated it into chunks of 1024 tokens. Truncating would defeat the purpose of summarization. So I created a check to see if the context size was greater than 1024 tokens, and based on that I created a method to break the context into chunks of 1024 tokens and getting summary for each of them. The individual summaries are then concatenated to form an ultimate summary which is then returned as a response.


### Future Improvements

With more time in hand, I would like to create a custom model and train that model with different business reports and other types of document so that it can create better summaries. Same for the question answering model, currently the models only give compact answers, with a custom model, the answer could be well-structured and precise.
