from transformers import pipeline

# Initialize summarization pipeline (loads model on first use)
summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

def summarize_text(text, max_length=130, min_length=30, do_sample=False):
    """
    Summarize the input text using a pre-trained model.
    Args:
        text (str): The clinical note to summarize.
        max_length (int): Maximum length of summary.
        min_length (int): Minimum length of summary.
        do_sample (bool): Whether to use sampling; use greedy decoding otherwise.
    Returns:
        str: The summarized text.
    """
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]['summary_text'] 