from rag.vector_db import collection

documents = [
    {
        "text": "هوش مصنوعی شاخه‌ای از علوم کامپیوتر است که به ماشین‌ها توانایی یادگیری و تصمیم‌گیری می‌دهد.",
        "metadata": {"topic": "AI", "source": "wikipedia"}
    },
    {
        "text": "یادگیری عمیق زیرمجموعه‌ای از یادگیری ماشین است که از شبکه‌های عصبی عمیق استفاده می‌کند.",
        "metadata": {"topic": "Deep Learning", "source": "academic"}
    },
    {
        "text": "پردازش زبان طبیعی به کامپیوترها امکان درک و تولید زبان انسانی را می‌دهد.",
        "metadata": {"topic": "NLP", "source": "textbook"}
    }
]


for i, doc in enumerate(documents):
    collection.add(
        documents=[doc["text"]],
        metadatas=[doc["metadata"]],
        ids=[f"doc_{i}"]
    )

print(f"تعداد {len(documents)} سند به پایگاه داده اضافه شد.")
