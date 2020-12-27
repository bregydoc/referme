from typing import List
import scholarly
from core import Publication
from reflinter import extract_references
from googletrans import Translator
from scholarly import _Scholarly

file = "bregy2020.1.md"
total_pubs = 5

translator = Translator()
scholarly = _Scholarly()
sentences = extract_references(file)

for s in sentences:
    sentence_in_english = translator.translate(s.sentence, dest="en")
    sentence = sentence_in_english.text
    print(f"{s.file}:{s.line}:{s.col}: {sentence}\n")

    publications: List[Publication] = []

    pubs = scholarly.search_pubs(sentence)
    for p in range(total_pubs):
        with next(pubs) as pub:
            # if pub is None:  # and "bib" in pub
            bib = pub["bib"]
            publications.append(Publication(
                title=bib["title"],
                author=bib["author"],
                year=bib["pub_year"],
                references=10  # bib["num_citations"]
            ))

    # pub_url = first_pub["pub_url"]
    pubs_str = "\n".join(
        [f"{pub.title} [{pub.author}]" for pub in publications])
    print(f"publications:\n-{pubs_str}")
