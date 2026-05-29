from rag.vector_db import collection
from rag.rag_pipeline import PersianRAG

rag_system = PersianRAG(
    collection=collection,
    # add your API KEY here
    llm_api_key=""
)

question = "یادگیری عمیق چیست؟"
result = rag_system.generate_answer(question)

print(f"سوال: {question}")
print(f"پاسخ: {result['answer']}")
print(f"\nمنابع استفاده شده:")
for i, source in enumerate(result['sources']):
    print(f"{i+1}. {source[:50]}...")
