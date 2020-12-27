from typing import List
import scholarly
from core import Publication
from reflinter import extract_references
from googletrans import Translator
from scholarly import _Scholarly
from scholarly import ProxyGenerator
from tqdm import tqdm

file = "bregy2020.1.md"
total_pubs = 5

pg = ProxyGenerator()
# pg.FreeProxies()
pg.Tor_Internal(tor_cmd="tor")
# pg.Luminati(usr="bregy@minsky.cc", passwd="Alanturing1802!", proxy_port=1200)

translator = Translator()
scholarly = _Scholarly()
sentences = extract_references(file)

scholarly.use_proxy(pg)


def find_publications(sentence: str, max_publications: int = 5) -> List[Publication]:
    publications: List[Publication] = []
    pubs = scholarly.search_pubs(sentence)

    for pub in pubs:
        if len(publications) > max_publications:
            break

        bib = pub["bib"]
        try:
            publications.append(Publication(
                title=bib["title"],
                author=bib["author"],
                year=bib["pub_year"],
                references=pub["num_citations"],
                url=pub["pub_url"]
            ))
        except:
            continue

    return publications


md_doc = f"### Result for {file}\n"

keywords = ["computation", "hardware", "computational"]

process = tqdm(sentences)

for s in process:
    sentence_in_english = translator.translate(s.sentence, dest="en")
    sentence = sentence_in_english.text

    sentence = ", ".join(keywords) + f", {sentence}"

    # process.set_description(f"{s.sentence}")

    publications = find_publications(sentence)

    md_doc += f"-   **Pos \[{s.line}:{s.col}\]:** {s.sentence}\n"
    md_doc += f"**English:** {sentence_in_english.text}\n"
    md_doc += f"**Publications:**\n"

    publications.sort(key=lambda p: p.references, reverse=True)

    for pub in publications:
        md_doc += f"  -   [{pub.title}]({pub.url}) ({pub.author[0]}, {pub.year}, {pub.references})\n"

    md_doc += "---\n"

with open("bregy2020.1.ref.md", "w+") as file:
    file.write(md_doc)
