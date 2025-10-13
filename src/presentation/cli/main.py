import os
import sys
from pathlib import Path

import typer


current_file = Path(__file__).resolve()
src_dir = current_file.parents[2]
sys.path.insert(0, str(src_dir))

from domain.entities.file import FileHashType
from infrastructure.persistence.json.repositories.json_report_repository import JsonReportRepository
from infrastructure.storage.local.repositories.local_file_repository import LocalFileRepository

app = typer.Typer(help="Backups CLI")

@app.command()
def main(
    mode: str = typer.Argument(..., help="Mode: inventory or verify"),
    directory: str = typer.Argument(..., help="Directory to scan"),
    output_file: str = typer.Option("inventory.json", help="Inventory file path"),
    hash_algo: str = typer.Option("sha1", help="Hash algorithm (e.g., sha1, sha256, sha3_512, blake2b)"),
    workers: int = typer.Option(8, help="Number of parallel workers"),
):
    """
    Disk Integrity Checker: Create or verify file inventory.
    """
    print("=" * 60)
    print("   🔒 Disk Integrity Checker - Verification Tool")
    print("   Ensure that no files were modified between transfers")
    print("=" * 60)

    if workers is None:
        workers = os.cpu_count()

    file_repository = LocalFileRepository()
    repository = JsonReportRepository()
    repository.generate(
        root_path = directory,
        hash_type = FileHashType.SHA1,
        workers = workers,
        file_repository = file_repository
    )

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    app()