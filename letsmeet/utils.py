from enum import IntEnum
from random import randrange
import hashlib

LINK_LEN = 7


class ShortenMethod(IntEnum):
    HASH = 1
    RANDOM = 1


alphabet = [chr(i) for i in range(ord('a'), ord('z'))] + [
    chr(i) for i in range(ord('A'), ord('Z'))
] + [chr(i) for i in range(ord('0'), ord('9'))]


def get_url_shortcut(url: str,
                     method: ShortenMethod = ShortenMethod.HASH,
                     width: int = LINK_LEN) -> str:
    def shorten_with_hash(url: str, width: int) -> str:
        result = hashlib.sha256()
        result.update(str.encode(url))
        result = result.hexdigest()
        result = result[:width]
        return result

    def shorten_with_random(url: str, width: int) -> str:
        result = [alphabet[randrange(len(alphabet))] for i in range(width)]
        return "".join(result)

    method_map = {
        ShortenMethod.HASH: shorten_with_hash,
        ShortenMethod.RANDOM: shorten_with_random,
    }
    return method_map[method](url, width)
