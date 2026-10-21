# UTF-8 Validation

`validUTF8(data)` returns `True` if `data` is a valid UTF-8 encoding and
`False` otherwise. `data` is a list of integers and each integer stands for
one byte, so only its 8 least significant bits are used.

## Approach

A UTF-8 character takes 1 to 4 bytes. The first byte tells how many bytes
the character has, and every byte after it must start with the bits `10`.

| Bytes | Byte pattern |
|-------|--------------|
| 1 | `0xxxxxxx` |
| 2 | `110xxxxx 10xxxxxx` |
| 3 | `1110xxxx 10xxxxxx 10xxxxxx` |
| 4 | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

The list is read once. A counter holds how many continuation bytes are
still expected. The data is valid when no byte breaks a pattern and the
counter is 0 at the end.

## Files

| File | Description |
|------|-------------|
| `0-validate_utf8.py` | `validUTF8(data)` returns a boolean |
| `0-main.py` | Example run |

## Usage

    $ ./0-main.py
    True
    True
    False
