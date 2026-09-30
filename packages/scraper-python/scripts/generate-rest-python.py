from pathlib import Path
import subprocess
import sys


root = Path(__file__).resolve().parents[3]
source = root / "contracts" / "scraper.openapi.generated.json"
output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else root / "packages" / "scraper-python" / "src" / "mcpscraper" / "models.py"
subprocess.run(
    [
        sys.executable, "-m", "datamodel_code_generator",
        "--input", str(source),
        "--input-file-type", "openapi",
        "--output", str(output),
        "--output-model-type", "pydantic_v2.BaseModel",
        "--field-constraints",
        "--use-schema-description",
        "--target-python-version", "3.10",
        "--disable-timestamp",
    ],
    check=True,
)
