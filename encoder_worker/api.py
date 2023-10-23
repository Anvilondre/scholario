from encoder import Encoder


def encode_text(text: str) -> list[int]:
    model = Encoder()
    return model(text=text)
