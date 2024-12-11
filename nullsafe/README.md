# NullSafe

A Python library providing null-safe attribute and key access through a simple chaining API.

## Installation

```bash
pip install nullsafe
```

## Usage

```python
from nullsafe import ns

# Basic usage
data = {"user": {"name": "John"}}
name = ns(data)["user"]["name"]()  # Returns "John"
missing = ns(data)["user"]["age"]()  # Returns None

# Object attribute access
class User:
    def __init__(self):
        self.name = "John"
        self.address = None

user = User()
name = ns(user).name()  # Returns "John"
city = ns(user).address.city()  # Returns None

# Chaining
data = {
    "users": [
        {"profile": {"address": {"city": "New York"}}}
    ]
}
city = ns(data)["users"][0]["profile"]["address"]["city"]()  # Returns "New York"
missing = ns(data)["users"][1]["profile"]["address"]["city"]()  # Returns None
```

## Features

- Null-safe attribute access
- Null-safe dictionary/list access
- Method chaining
- Immutable wrapper objects
- Type hints support
- Zero dependencies

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.