import torch
from fairseq.models.bart import BARTModel
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bart = BARTModel.from_pretrained('bart.large.cnn/', checkpoint_file='model.pt')
bart.eval()
if torch.cuda.is_available():
    bart.cuda()

@app.route('/summarize',methods=['POST'])
def summarize():
    text = request.json["document"]
    with torch.no_grad():
        hypotheses_batch = bart.sample([text], beam=4, lenpen=2.0, max_len_b=140, min_len=55, no_repeat_ngram_size=3)
    return jsonify({"summary":hypotheses_batch[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)