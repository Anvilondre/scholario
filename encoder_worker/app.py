from redis import Redis
from rq import SimpleWorker
from encoder import Encoder

if __name__ == "__main__":
    encoder = Encoder()
    w = SimpleWorker(['high', 'low'], connection=Redis('redis'))
    w.work()
