import textwrap

n = 60

def format_text(text: str, n: int) -> str:

    paragraphs = text.split("\n\n")
    formatted_paragraphs = ["\n".join(textwrap.wrap(paragraph, width=n)) for paragraph in paragraphs]

    return "\n\n".join(formatted_paragraphs)

text = "Життя — це подорож, сповнена несподіванок. Кожен день приносить нові можливості, і тільки від нас залежить, як ми їх використаємо"

formatted_text = format_text(text, n)
print(formatted_text)
