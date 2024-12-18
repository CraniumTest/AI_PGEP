from transformers import pipeline

def setup_virtual_assistant():
    nlp_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")
    return nlp_pipeline

def interact_with_guest(nlp_pipeline, user_input):
    response = nlp_pipeline(user_input)
    return response

assistant = setup_virtual_assistant()
print(interact_with_guest(assistant, "Can you suggest a good restaurant?"))
