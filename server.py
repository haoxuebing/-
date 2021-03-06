
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from model import Model
from gevent.pywsgi import WSGIServer
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

vocab_file = './couplet/vocabs'
model_dir = './models/tf-lib/output_couplet'

m = Model(
    None, None, None, None, vocab_file,
    num_units=1024, layers=4, dropout=0.2,
    batch_size=32, learning_rate=0.0001,
    output_dir=model_dir,
    restore_model=True, init_train=False, init_infer=True)


@app.route('/<in_str>')
def chat_couplet(in_str):
    if len(in_str) == 0 or len(in_str) > 50:
        output = u'您的输入太长了'
    else:
        output = m.infer(' '.join(in_str))
        output = ''.join(output.split(' '))
    logger.info('上联：%s；下联：%s' % (in_str, output))
    return jsonify({'下联': output})


http_server = WSGIServer(('127.0.0.1', 5000), app)
http_server.serve_forever()
