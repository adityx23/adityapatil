import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
failures: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


project_pages = sorted((ROOT / "projects").glob("*.md"))
if not project_pages:
    fail("no project pages found")

for page in project_pages:
    text = page.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{page.relative_to(ROOT)}: missing YAML front matter")
    if text.count("---") < 2:
        fail(f"{page.relative_to(ROOT)}: unterminated YAML front matter")

    for asset in re.findall(r"/assets/[^\s\)\"'}<>]+", text):
        asset = asset.rstrip(".,:;")
        if not (ROOT / asset.lstrip("/")).exists():
            fail(f"{page.relative_to(ROOT)}: missing asset {asset}")

tracked_text = "\n".join(
    path.read_text(encoding="utf-8", errors="ignore")
    for path in [*project_pages, ROOT / "index.md", ROOT / "projects.md"]
)
for pattern, label in [
    (r"hf_[A-Za-z0-9]{10,}", "Hugging Face token"),
    (r"sk-[A-Za-z0-9_-]{10,}", "API key"),
    (r"github_pat_[A-Za-z0-9_]{10,}", "GitHub token"),
    (r"[A-Za-z]:\\Users\\", "machine-specific user path"),
]:
    if re.search(pattern, tracked_text, flags=re.IGNORECASE):
        fail(f"portfolio content contains a {label}")

if failures:
    raise SystemExit("\n".join(f"ERROR: {item}" for item in failures))

print(f"Validated {len(project_pages)} project pages and their local assets.")
