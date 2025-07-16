import json
import os

from appPublic.dictObject import DictObject
from appPublic.zmq_reqrep import ZmqReplier
from appPublic.jsonConfig import getConfig

from time import time
import whisper

class ZmqASR:
    def __init__(self, zmq_url, model_dir, device):
        self.model = whisper.load_model(model_dir, device=device)
        self.model_dir = model_dir
        self.device = device
        self.zmq_url = zmq_url
        self.replier = ZmqReplier(self.zmq_url, self.generate)

    def run(self):
        print(f'running {self.zmq_url}')
        self.replier._run()
        print('ended ...')

    def generate(self, d):
        msg= d.decode('utf-8')
        data = DictObject(**json.loads(msg))
        t1 = time()
        res = self.model.transcribe(data.audio_file)
        t2 = time()
        text = res['text']
        d = {k:v for k, v in res.items() if k!='text'}
        d['content'] = text
        d['time_cost'] = t2 - t1
        print(f'{d}')
        return json.dumps(d)

if __name__ == '__main__':
    workdir = os.getcwd()
    config = getConfig(workdir)
    print(f'{config=}')
    asr = ZmqASR(config.zmq_url or zmq_url,
                    config.model_dir or model_dir,
                    config.device or device)
    print('here')
    asr.run()
