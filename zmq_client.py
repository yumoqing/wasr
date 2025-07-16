import json
import os

from appPublic.dictObject import DictObject
from appPublic.zmq_reqrep import ZmqRequester
from appPublic.jsonConfig import getConfig

zmq_url = "tcp://127.0.0.1:9999"
from time import time

class ASRClient:
    def __init__(self, zmq_url):
        self.zmq_url = zmq_url
        self.requester = ZmqRequester(self.zmq_url)

    def generate(self, audio_file):
        d = {
            "audio_file":audio_file
        }
        msg = json.dumps(d)
        resp = self.requester.send(msg)
        if resp != None:
            ret = json.loads(resp)
            print(f'response={ret}')
        else:
            print(f'response is None')

    def run(self):
        print(f'running {self.zmq_url}')
        while True:
            print('input audio_file:')
            af = input()
            if len(af) > 0:
                self.generate(af)
        print('ended ...')

if __name__ == '__main__':
    workdir = os.getcwd()
    config = getConfig(workdir)
    asr = ASRClient(config.zmq_url or zmq_url)
    asr.run()
