from rake_nltk import Rake

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()

text="i am trying but could not understand matrix transverse.i love matrix so much i can eats it"
# Extraction given the text.
r.extract_keywords_from_text(text)

# Extraction given the list of strings where each string is a sentence.
#r.extract_keywords_from_sentences(<list of sentences>)

# To get keyword phrases ranked highest to lowest.
print(r.get_ranked_phrases())
