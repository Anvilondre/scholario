from redis import Redis
from rq import Worker
from encoder import Encoder

if __name__ == "__main__":
    encoder = Encoder()
    w = Worker(['high', 'low'], connection=Redis('redis'))
    w.work()
