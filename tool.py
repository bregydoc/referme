import pathlib
from typing import List, Tuple
from core import Publication
from reflinter import extract_references
from googletrans import Translator
from scholarly import _Scholarly
from scholarly import ProxyGenerator
from tqdm import tqdm


def find_publications(scholarly: _Scholarly, sentence: str, max_publications: int = 5) -> List[Tuple[Publication, str]]:
    publications: List[Tuple[Publication, str]] = []

    pubs = scholarly.search_pubs(sentence)

    for pub in pubs:
        if len(publications) > max_publications:
            break

        bib = pub["bib"]
        try:
            publications.append((Publication(
                title=bib["title"],
                author=bib["author"],
                year=bib["pub_year"],
                references=pub["num_citations"],
                url=pub["pub_url"]
            ), scholarly.bibtex(pub)))
        except:
            continue

    return publications


def seed_reference(filepath: str):
    filename = pathlib.Path(filepath).name  # bregy2020.1.md
    ref_file = filename[-4:] if filename.endswith(".md") else filename

    ref_md_filename = f"{ref_file}.refs.md"
    ref_bibtex_filename = f"{ref_file}.bib"

    keywords = ["computation", "hardware", "computational"]

    pg = ProxyGenerator()
    # pg.FreeProxies()
    pg.Tor_Internal(tor_cmd="tor")
    # pg.Luminati(usr="bregy@minsky.cc", passwd="Alanturing1802!", proxy_port=1200)

    translator = Translator()
    scholarly = _Scholarly()
    sentences = extract_references(filepath)

    scholarly.use_proxy(pg)

    md_doc = f"### Result for {filename}\n"
    bibtext_doc = ""

    for s in tqdm(sentences):
        sentence_in_english = translator.translate(s.sentence, dest="en")
        sentence = sentence_in_english.text

        sentence = ", ".join(keywords) + f", {sentence}"

        publications = find_publications(scholarly, sentence)

        md_doc += f"-   **Pos \[{s.line}:{s.col}\]:** {s.sentence}\n"
        md_doc += f"    **English:** {sentence_in_english.text}\n"
        md_doc += f"    **Publications:**\n"

        # print("\n".join(publications))
        # return
        publications.sort(key=lambda p: p[0].references, reverse=True)

        for (pub, bibtext) in publications:
            md_doc += f"    -   [{pub.title}]({pub.url}) ({pub.author[0]}, {pub.year}, {pub.references})\n"
            bibtext_doc += f"{bibtext}\n\n"

        md_doc += "---\n"

    print(ref_file)

    with open(ref_md_filename, "w+") as file:
        file.write(md_doc)

    with open(ref_bibtex_filename, "w+") as file:
        file.write(bibtext_doc)


file = "bregy2020.1.md"
seed_reference(file)
