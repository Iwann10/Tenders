from typing import TypedDict

from docx import Document


# Define the input and output types for the tokenizer function
class Input(TypedDict):
    doc: str


class Output(TypedDict):
    metadata: dict[str, str]


def metadata(input: Input) -> Output:

    doc = Document(input["doc"])
    p = doc.core_properties
    paragraphs = [par.text.strip() for par in doc.paragraphs]

    return {
        "metadata": {
            "author": p.author,
            "category": p.category,
            "comments": p.comments,
            "content_status": p.content_status,
            "created": p.created.isoformat() if p.created else None,
            "identifier": p.identifier,
            "keywords": p.keywords,
            "language": p.language,
            "last_modified_by": p.last_modified_by,
            "last_printed": p.last_printed.isoformat() if p.last_printed else None,
            "modified": p.modified.isoformat() if p.modified else None,
            "revision": p.revision,
            "subject": p.subject,
            "title": p.title,
            "version": p.version,
            "name": input["doc"],
            "paragraphs": paragraphs,
            "text": " ".join(paragraphs),
        }
    }


# example if this file is run as a script
if __name__ == "__main__":
    print(metadata({"doc": "file.docx"}))
