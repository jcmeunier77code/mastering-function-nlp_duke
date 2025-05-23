from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search Wikipedia for a name and return a page object."""
    print("Searching Wikipedia for: ", name)
    # Search Wikipedia for the name
    return wikipedia.search(name)


def wikipedia_summary(name):
    """Get the summary of a Wikipedia page."""
    print("Getting Wikipedia summary for: ", name)
    # Get the summary of the Wikipedia page
    return wikipedia.summary(name)


def get_text_blob(text):
    """Get the text blob of a text and return."""
    blob = TextBlob(text)
    return blob


def get_sentences(name):
    """Find wikipedia namee and return back phrase."""
    text = wikipedia_summary(name)
    blob = get_text_blob(text)
    phrase = blob.noun_phrases
    return phrase
