import os
from sentence_transformers import SentenceTransformer

class Encoder:
    _instance = None

    def __new__(cls):
        if cls._instance is not None:
            return cls._instance
        cls._instance = super(Encoder, cls).__new__(cls)

        device = os.environ['DEVICE']

        if device == 'auto':
            import torch
            if torch.cuda.is_available():
                device = 'cuda'
            elif torch.backends.mps.is_available() and torch.backends.mps.is_built():
                device = 'mps'
            else:
                device = 'cpu'

        cls.model = SentenceTransformer('all-mpnet-base-v2').to(device)

        return cls._instance

    def __call__(self, text: str) -> list[int]:
        return self.model.encode(text).tolist()
