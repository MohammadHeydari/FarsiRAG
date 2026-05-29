import chromadb
from chromadb.utils import embedding_functions

from rag.embedding import get_persian_embedding

class PersianEmbeddingFunction(embedding_functions.EmbeddingFunction):
    def __call__(self, texts):
        embeddings = []
        for text in texts:
            embedding = get_persian_embedding(text)
            embeddings.append(embedding.tolist())
        return embeddings

# client = chromadb.Client()
client = chromadb.PersistentClient(path="./chroma_db")

persian_ef = PersianEmbeddingFunction()

collection = client.get_or_create_collection(
    name="persian_documents",
    embedding_function=persian_ef
)