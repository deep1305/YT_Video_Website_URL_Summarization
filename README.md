# 🦜🔗 YouTube & Webpage Summarizer AI

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.0-FF4B4B.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.24-8A2BE2.svg)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama%203-orange.svg)](https://groq.com/)

Instantly summarize YouTube videos or any webpage content with the power of AI! This Streamlit application leverages LangChain and the blazing-fast Groq Llama 3 model to deliver concise summaries, helping you save time and grasp key information quickly.

---

## ✨ Features

*   **YouTube Video Summarization**: Paste any YouTube video link (full URL or `youtu.be`) and get its transcript summarized.
*   **Webpage Content Summarization**: Provide a URL for any article or webpage, and let the AI distill the core content for you.
*   **Adjustable Summary Length**: (Implicitly) Aims for a ~400-word summary, focusing on key takeaways.
*   **User-Friendly Interface**: Simple and intuitive UI built with Streamlit.
*   **Fast Processing**: Powered by the Groq API for near real-time summarization.
*   **Secure API Key Handling**: Groq API key is entered via a password field in the sidebar.

---

## 🚀 Demo

*(Consider adding a GIF or screenshot of your application in action here!)*

**Example Workflow:**

1.  Enter your Groq API Key in the sidebar.
2.  Paste a YouTube video URL or a website URL into the main input field.
3.  Click "Summarize".
4.  Voilà! Your summary appears.

---

## 🛠️ Tech Stack & Key Libraries

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **LLM Orchestration**: [LangChain](https://python.langchain.com/docs/get_started/introduction)
*   **LLM Provider**: [Groq](https://groq.com/) (using Llama 3 8B model)
*   **YouTube Transcript**: `youtube-transcript-api`
*   **Web Content Loading**: `UnstructuredURLLoader` (from `langchain-community`)
*   **URL Validation**: `validators`
*   **Core Python Libraries**: `re`

---

## ⚙️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/deep1305/YT_Video_Website_URL_Summarization.git
    cd YT_Video_Website_URL_Summarization
    ```

2.  **Create and activate a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Make sure you have a `requirements.txt` file. If not, you can create one from your `pyproject.toml` or list the core dependencies:
    ```bash
    pip install streamlit langchain-groq langchain-community youtube-transcript-api validators unstructured[all-docs]
    ```
    *(Note: `unstructured[all-docs]` installs dependencies for various file types. You might only need the base `unstructured` if web URLs are your only non-YouTube source.)*

4.  **Get a Groq API Key:**
    *   Sign up at [GroqCloud](https://console.groq.com/keys).
    *   Create an API key and copy it.

---

## ▶️ How to Run

1.  Ensure your virtual environment is activated.
2.  Navigate to the project directory where `app.py` is located (you should be in `YT_Video_Website_URL_Summarization` after cloning and `cd`).
3.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
4.  The application will open in your default web browser.

---

## 📖 How to Use

1.  Once the app is running, you'll see a sidebar asking for your "Groq API Key". Paste your key there.
2.  In the main section, enter the full URL of the YouTube video or website you want to summarize.
3.  Click the "Summarize" button.
4.  Wait a few moments while the content is fetched and processed.
5.  The generated summary will appear below the button.

---

## 💡 Future Enhancements (Ideas)

*   [ ] Allow users to specify desired summary length (e.g., short, medium, detailed).
*   [ ] Add a "Copy to Clipboard" button for the summary.
*   [ ] Support for uploading local text files for summarization.
*   [ ] Option to choose different summarization models or styles.
*   [ ] History of summarized URLs.
*   [ ] Error handling for videos without transcripts or inaccessible URLs.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or want to fix a bug, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details (you'll need to create this file if you don't have one, a standard MIT license text is fine).

---

Happy Summarizing! 🎉
