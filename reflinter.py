import re
from typing import List, Optional, Tuple
import pathlib
from dataclasses import dataclass


@dataclass
class Sentence:
    sentence: str
    file: str
    line: Optional[int]
    col: Optional[int]


def extract_references(file: str, ref_form: re.Pattern = r"\\\[ref.", cut_chars: List[str] = [".", "\n", "]"]) -> List[Sentence]:
    sentences: List[Sentence] = []

    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        doc = "".join(lines)

        chars_per_line = [len(l) for l in lines]

        refs = re.compile(ref_form).finditer(doc)

        filename = pathlib.Path(file).name

        for ref in refs:
            ref_index_match = ref.start()

            sentece_start = -1
            while sentece_start == -1:
                char = doc[ref_index_match]
                if char in cut_chars or ref_index_match < 1:
                    sentece_start = ref_index_match+1
                ref_index_match -= 1

            chars_accum = 0
            sentence_line = -1
            sentence_col = -1
            for line, chars_line in enumerate(chars_per_line):
                chars_accum += chars_line
                if chars_accum > sentece_start:
                    sentence_line = line
                    sentence_col = chars_accum - sentece_start
                    break

            s = Sentence(
                sentence=doc[sentece_start: ref.start()],
                file=filename,
                line=sentence_line,
                col=sentence_col,
            )

            sentences.append(s)

    return sentences


def references_lint(file: str):
    sentences = extract_references(file)
    for sentence in sentences:
        print(f"{sentence.file}:{sentence.line}:{sentence.col}: {sentence.sentence}\n")


# references_lint("bregy2020.1.md")
