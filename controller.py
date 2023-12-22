from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
from service import *

app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/getSummary", methods=['GET'])
@cross_origin(origins='*')
def get_context_summary():
    print(request.values)
    context = request.args.get('query_context')
    print(context)
    return get_summary(context=context)


@app.route("/askQuestion", methods=['GET'])
@cross_origin(origins='*')
def get_context_qa():
    print(request.args.values())
    question = request.args.get('question')
    print(question)
    context = request.args.get('query_context')
    print(context)
    return get_answer_to_context(question=question, context=context)
