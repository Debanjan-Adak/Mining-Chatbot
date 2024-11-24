def search_docs(question):
    # Load the FAISS database and retrieve relevant documents
    docs_db = FAISS.load_local("/content/docs_db/", embeddings, allow_dangerous_deserialization=True)
    docs = docs_db.similarity_search(question)

    # Initialize empty strings for the results
    all_page_contents = ""
    all_contents_with_sources = ""

    # Loop through the documents and build the strings
    for doc in docs:
        page_content = doc.page_content
        source = doc.metadata.get("source")
        page=doc.metadata.get("page")
        # Concatenate page contents
        all_page_contents += page_content + "\n"

        # Concatenate page content with source
        all_contents_with_sources += f"{page_content}\nSource: {source}\nPage: {page}\n____________________________________\n\n"

    return all_page_contents.strip(), all_contents_with_sources.strip()