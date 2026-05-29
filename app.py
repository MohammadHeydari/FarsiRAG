import streamlit as st

from rag.vector_db import collection
from rag.rag_pipeline import PersianRAG

st.set_page_config(page_title="Farsi RAG Chat", page_icon="💬")

st.title("Farsi RAG-based Chat")

# Add your API KEY here
api_key = st.text_input("", type="password")


@st.cache_resource
def get_rag():
    return PersianRAG(
        collection=collection,
        llm_api_key=api_key
    )


if api_key:
    rag = get_rag()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])


    user_input = st.chat_input("سوالت رو بنویس...")

    if user_input:

        st.chat_message("user").write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})


        with st.chat_message("assistant"):
            with st.spinner("Thinking ..."):
                result = rag.generate_answer(user_input)
                answer = result["answer"]

                st.write(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )


        with st.expander("Sources ..."):
            for i, src in enumerate(result["sources"]):
                st.write(f"{i+1}. {src}")

else:
    st.info("Add API Key")