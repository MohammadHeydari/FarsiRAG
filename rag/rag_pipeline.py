from hazm import Normalizer
from openai import OpenAI


class PersianRAG:
    def __init__(self, collection, llm_api_key):
        self.collection = collection
        self.normalizer = Normalizer()

        # client
        self.llm_client = OpenAI(
            base_url="https://api.gapgpt.app/v1",
            api_key=llm_api_key
        )

    def retrieve_relevant_docs(self, query, n_results=3):


        normalized_query = self.normalizer.normalize(query)

        results = self.collection.query(
            query_texts=[normalized_query],
            n_results=n_results
        )

        return results

    def generate_answer_with_llm(self, question, context):


        response = self.llm_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "تو یک دستیار هوشمند فارسی هستی. فقط بر اساس متن داده‌شده پاسخ بده. اگر پاسخ در متن نبود بگو نمی‌دانم."
                },
                {
                    "role": "user",
                    "content": f"""
Context:
{context}

Question:
{question}
"""
                }
            ]
        )

        return response.choices[0].message.content

    def generate_answer(self, question):


        # 1. retrieve
        results = self.retrieve_relevant_docs(question)

        docs = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        # 2. build context
        context = "\n\n".join(docs)

        if not context.strip():
            return {
                "answer": "هیچ اطلاعات مرتبطی پیدا نشد.",
                "sources": [],
                "metadata": []
            }

        # 3. generate
        answer = self.generate_answer_with_llm(question, context)

        return {
            "answer": answer,
            "sources": docs,
            "metadata": metadatas
        }