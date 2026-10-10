import re
import unicodedata
from nltk.tokenize import TreebankWordTokenizer


class InputProcessor:
    MAX_LENGTH = 2000

    def __init__(self):
        self.tokenizer = TreebankWordTokenizer()

    def process(self, raw_text: str) -> dict:
        if not isinstance(raw_text, str):
            raise ValueError("Message must be text.")

        text = unicodedata.normalize("NFKC", raw_text)

        text = "".join(
            char for char in text
            if unicodedata.category(char) != "Cc"
            or char in "\n\t"
        )

        text = re.sub(r"\s+", " ", text).strip()

        if not text:
            raise ValueError("Please enter a message.")

        if len(text) > self.MAX_LENGTH:
            raise ValueError(
                f"Message must be {self.MAX_LENGTH} characters or fewer."
            )

        tokens = self.tokenizer.tokenize(text)

        return {
            "original": text,
            "normalized": text.casefold(),
            "tokens": tokens,
        }
