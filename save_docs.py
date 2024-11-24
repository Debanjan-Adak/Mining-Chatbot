def save_docs(docs):

    import shutil
    import os

    destination_dir = "/content/docs/"
    os.makedirs(destination_dir, exist_ok=True)

    output_dir="/content/docs/"

    for doc in docs:
      shutil.copy(doc.name, output_dir)

    return "File(s) saved successfully!"