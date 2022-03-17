import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("PROFIT_ROOT", "~/.profit/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("PROFIT_KEYS_ROOT", "~/.profit_keys"))).resolve()
