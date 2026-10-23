import argparse
import json
import sys
from pathlib import Path

from extractor import extract_resume


def main():
    parser = argparse.ArgumentParser(
        description="Extract information from a PDF or DOCX resume."
    )
    parser.add_argument("resume", help="Path to the resume file")
    parser.add_argument(
        "--output",
        help="Optional path to save the JSON output"
    )
    args = parser.parse_args()

    try:
        result = extract_resume(args.resume)
        output = json.dumps(result, indent=4, ensure_ascii=False)

        if args.output:
            destination = Path(args.output)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(output + "\n", encoding="utf-8")
            print(f"Saved JSON to: {destination}")
        else:
            print(output)

    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()