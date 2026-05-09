from pathlib import Path
import sys

# Make repo root importable for tests (so `import aes_socket_utils` works)
REPO_ROOT = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

