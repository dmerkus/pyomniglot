from typing import List, Optional

from documental import Text, Tokens
from documental.token import Token, NumberToken


def combine_numbers(text: Text, tokenized: Tokens) -> None:
    combined_tokens: List[Token] = []

    combined_number: Optional[str] = None

    for token in tokenized.tokens:
        if isinstance(token, NumberToken):
            if combined_number is None:
                combined_number = token.text
            else:
                combined_number += token.text
        else:
            if combined_number is not None:
                combined_tokens.append(NumberToken(combined_number))
                combined_number = None

            combined_tokens.append(token)

    if combined_number is not None:
        combined_tokens.append(NumberToken(combined_number))

    tokenized.tokens = combined_tokens
