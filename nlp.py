from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

file_path = "/home/oindrilabanerjee/Desktop/text.txt"


def getData():
    with open(file_path, "r") as f:
        data = f.read()

    return data


model_name = "deepset/roberta-base-squad2"

# nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
nlp = pipeline("summarization", model="facebook/bart-large-cnn")

# QA_input = {
#     'question': 'How many words are there in a paragraph?',
#     'context': getData()
# }

res = nlp(getData(), max_length=150, min_length=100, do_sample=False)
#
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

print(res)
