from sentence_transformers import SentenceTransformer

class Encoder:
    _instance = None

    def __new__(cls):
        if cls._instance is not None:
            return cls._instance
        cls._instance = super(Encoder, cls).__new__(cls)

        import torch
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        cls.model = SentenceTransformer('all-mpnet-base-v2').to(device)

        return cls._instance

    def __call__(self, text: str) -> list[int]:
        return self.model.encode(text).tolist()
