import re
from typing import List, Optional, Tuple
import pathlib
from dataclasses import dataclass

cut_chars = [".", "\n", "]"]


@dataclass
class Sentence:
    sentence: str
    start: int
    end: int
    line: Optional[int]
    col: Optional[int]


# sentences_index: List[Tuple[int, int]] = []
sentences: List[Sentence] = []

filepath = 'bregy2020.1.md'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    doc = "".join(lines)

    chars_per_line = [len(l) for l in lines]

    refs = re.compile(r"\\\[ref.").finditer(doc)

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
            doc[sentece_start: ref.start()],
            sentece_start,
            ref.start(),
            line=sentence_line,
            col=sentence_col,
        )

        sentences.append(s)


filename = pathlib.Path(filepath).name
for sentence in sentences:
    print(f"{filename}:{sentence.line}:{sentence.col}: {sentence.sentence}\n")
    # print(sentence + "\n")
