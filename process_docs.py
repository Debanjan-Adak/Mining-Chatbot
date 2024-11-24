def process_docs():
    loader1 = DirectoryLoader('/content/docs/', glob="./*.pdf", loader_cls=PyPDFLoader)
    document1 = loader1.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    docs = text_splitter.split_documents(document1)

    docs_db = FAISS.from_documents(docs, embeddings)
    docs_db.save_local("/content/docs_db/")

    return "File(s) processed successfully!"

process_docs()