"""
Midnight Manuscript
Story Generation Module
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output" / "stories"


def main():
    print("=" * 50)
    print("Midnight Manuscript")
    print("=" * 50)
    print(f"Project Root : {PROJECT_ROOT}")
    print(f"Stories Path : {OUTPUT_DIR}")


if __name__ == "__main__":
    main()