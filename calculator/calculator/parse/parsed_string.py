from typing import List, Union

from calculator.ast import BinOp, Constant, Node, UnaryOp
from pydantic.dataclasses import dataclass


def begins_with_digit(d: str) -> bool:
    return "0" <= d[0] <= "9"


@dataclass
class ParsedString:
    input: str

    def _is_done(self) -> bool:
        return len(self.input) == 0

    def _get_token(self) -> Union[int, str]:
        ans = ""
        self.input = self.input.strip()  # Remove whitespace
        while begins_with_digit(self.input):
            ans += self.input[0]
            self.input = self.input[1:]
            if len(self.input) == 0 or not begins_with_digit(self.input):
                break
        if len(ans) != 0:  # Was a number, return the converted int
            return int(ans)
        # Was not a number, return the (presumed) symbol
        ans = self.input[0]
        self.input = self.input[1:]
        return ans

    def tokenize(self) -> List[Union[int, str]]:
        ans: List[str] = []
        while not self._is_done():
            ans.append(self._get_token())
        return ans
