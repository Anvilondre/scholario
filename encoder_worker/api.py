from encoder import Encoder


def encode_text(text: str) -> list[float]:
    model = Encoder()
    return model(text=text)
