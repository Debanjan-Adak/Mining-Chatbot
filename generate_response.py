def generate_response(input_text):
    """
    Generate a response based on the given instruction and input text.

    Args:
        instruction (str): The instruction or question for the model.
        input_text (str): The input context or data for the model.
        model: The pre-trained model for inference.
        tokenizer: The tokenizer associated with the model.
        max_new_tokens (int, optional): The maximum number of tokens to generate. Default is 64.

    Returns:
        str: The generated response as a string.
    """
    alpaca_prompt = """You are an expert at Indian Laws on Mining. You are provided a question along with a set of relavent documents. Please answer the question based on the documents.
    ### Input:
    {}

    ### Response:
    {}"""

    # Format the prompt with the given instruction and input text
    prompt = alpaca_prompt.format( input_text, "")

    # Tokenize the input for the model
    inputs = tokenizer([prompt], return_tensors="pt").to("cuda")

    # Generate the output
    outputs = model.generate(**inputs, max_new_tokens=128, use_cache=True)

    # Decode and return the response
    response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    response_start = "### Response:"
    response_content = response.split(response_start, 1)[-1].strip()
    return response_content