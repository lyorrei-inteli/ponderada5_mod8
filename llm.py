from langchain.llms import Ollama
import gradio as gr
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

class SafetyExpertChatbot:
    def __init__(self, base_url, model_name, context_file):
        loader = TextLoader(context_file)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = Chroma.from_documents(docs, embedding_function)
        retriever = vectorstore.as_retriever()

        template = """
                    You will receive context from a text file containing details about Workshop rules and safety considerations. Your task is to respond to user queries using this context when relevant. 

                    Responding to Queries: Keep the response concise and focused solely on answering the user query. Do not add any additional information or dialogue.

                    Context from File:
                    {context}
 
                    ---

                    User Query: {question}
                    """
        prompt = ChatPromptTemplate.from_template(template)
        self.chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | Ollama(base_url=base_url, model=model_name)
        )
        self.demo = gr.Blocks()
        self._setup_ui()

    def _setup_ui(self):
        with self.demo:
            self.chatbot = gr.Chatbot()
            self.msg = gr.Textbox()
            self.clear = gr.ClearButton([self.msg, self.chatbot])
            self.msg.submit(self.run_ollama, inputs=[self.msg, self.chatbot], outputs=[self.msg, self.chatbot])

    def run_ollama(self, text, chat_history):
        ollama_response = ""
        for s in self.chain.stream(text):
            ollama_response += s
            print(s)
        chat_history.append((text, ollama_response))
        return "", chat_history

    def launch(self):
        self.demo.launch()

if __name__ == "__main__":
    print("Loading Safety Expert Chatbot...")
    chatbot_app = SafetyExpertChatbot(base_url='http://localhost:11434', model_name="dolphin2.2-mistral", context_file='./safety_expert.txt')
    chatbot_app.launch()