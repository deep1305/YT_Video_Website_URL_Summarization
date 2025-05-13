import re
import validators
import streamlit as st

from youtube_transcript_api import YouTubeTranscriptApi
from langchain.schema import Document
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader


def get_yt_docs(url: str) -> list[Document]:
    """
    Extract the video ID, fetch its transcript via youtube-transcript-api,
    and wrap it in a single LangChain Document.
    """
    m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    if not m:
        raise ValueError("Could not extract YouTube video ID from URL.")
    vid = m.group(1)

    # this may raise if no transcript exists
    transcript = YouTubeTranscriptApi.get_transcript(vid)

    # join all text chunks into one document
    full_text = " ".join(chunk["text"] for chunk in transcript)
    return [Document(page_content=full_text)]


def main():
    st.set_page_config(
        page_title="LangChain: Summarize YouTube & Web Pages",
        page_icon="🦜"
    )
    st.title("🦜 LangChain: YouTube & Webpage Summarizer")

    # Sidebar: API key input
    with st.sidebar:
        groq_api_key = st.text_input("Groq API Key", type="password")

    # Main URL input
    url = st.text_input("Enter a YouTube or website URL")

    # Initialize the Groq LLM
    llm = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)

    # Prompt for summarization
    prompt = PromptTemplate(
        template="""
        Provide a concise ~400-word summary of the following content:

        Content:{text}
       """,
        input_variables=["text"],
    )

    if st.button("Summarize"):
        # Basic validation
        if not groq_api_key or not url:
            st.error("Please enter both your Groq API key and a URL.")
            return
        if not validators.url(url):
            st.error("That doesn’t look like a valid URL.")
            return

        try:
            # Load content
            with st.spinner("Loading content…"):
                if "youtube.com" in url or "youtu.be" in url:
                    docs = get_yt_docs(url)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[url],
                        ssl_verify=False,
                        headers={
                            "User-Agent": (
                                "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/116.0.0.0 Safari/537.36"
                            )
                        },
                    )
                    docs = loader.load()

            # Summarize
            with st.spinner("Summarizing…"):
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)#We used stuff in chain_type because content can be bigger or smaller.
                summary = chain.run(docs)

            st.success(summary)

        except Exception as e:
            st.exception(e)


if __name__ == "__main__":
    main()