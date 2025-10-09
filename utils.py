from difflib import SequenceMatcher

def find_similar_petitions(text, existing_texts, threshold=0.7):
    for pid, prev_text in existing_texts.items():
        ratio = SequenceMatcher(None, text.lower(), prev_text.lower()).ratio()
        if ratio >= threshold:
            return pid
    return None
