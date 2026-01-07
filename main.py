from __future__ import annotations

import re
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=1)
    max_sentences: int = Field(3, gt=0)


class SummarizeResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int


SENTENCE_SPLIT_REGEX = re.compile(r"(?<=[.!?])\s+")
WORD_REGEX = re.compile(r"\b\w+\b")


def split_sentences(text: str) -> List[str]:
    sentences = [sentence.strip() for sentence in SENTENCE_SPLIT_REGEX.split(text.strip())]
    return [sentence for sentence in sentences if sentence]


def count_words(text: str) -> int:
    return len(WORD_REGEX.findall(text))


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/summarize", response_model=SummarizeResponse)
def summarize(payload: SummarizeRequest) -> SummarizeResponse:
    sentences = split_sentences(payload.text)
    summary_sentences = sentences[: payload.max_sentences]
    summary_text = " ".join(summary_sentences)
    return SummarizeResponse(
        summary=summary_text,
        original_length=count_words(payload.text),
        summary_length=count_words(summary_text),
    )
