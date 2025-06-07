from pathlib import Path
from typing import List
from crewai.tools.base_tool import BaseTool


class ListTestFilesTool(BaseTool):
    """Tool to list Python test files within a directory."""

    name: str = "list_test_files"
    description: str = (
        "List all python test files (test_*.py or *_test.py) in a directory recursively"
    )

    def _run(self, directory: str) -> List[str]:
        base = Path(directory)
        if not base.is_dir():
            raise FileNotFoundError(f"{directory} is not a valid directory")
        files = set()
        for pattern in ("test_*.py", "*_test.py"):
            for file in base.rglob(pattern):
                files.add(str(file))
        return sorted(files)


class ReadFileTool(BaseTool):
    """Tool to read a file content."""

    name: str = "read_file"
    description: str = "Read a text file using UTF-8 encoding"

    def _run(self, filepath: str) -> str:
        path = Path(filepath)
        if not path.is_file():
            raise FileNotFoundError(f"File {filepath} not found")
        return path.read_text(encoding="utf-8")
