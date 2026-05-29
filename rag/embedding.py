from hazm import Normalizer, word_tokenize, sent_tokenize
import torch
from transformers import AutoTokenizer, AutoModel


normalizer = Normalizer()


tokenizer = AutoTokenizer.from_pretrained("HooshvareLab/bert-base-parsbert-uncased")
model = AutoModel.from_pretrained("HooshvareLab/bert-base-parsbert-uncased")


def get_persian_embedding(text):
    normalized_text = normalizer.normalize(text)

    inputs = tokenizer(
        normalized_text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model(**inputs)

        # mean pooling
        embeddings = outputs.last_hidden_state.mean(dim=1)

        embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)

    return embeddings.numpy()[0]
