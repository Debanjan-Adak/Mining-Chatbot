from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Alibaba-NLP/gte-large-en-v1.5
embeddings = HuggingFaceEmbeddings(
    model_name="Alibaba-NLP/gte-large-en-v1.5",
    model_kwargs = {'device': 'cuda','trust_remote_code':True}
    )