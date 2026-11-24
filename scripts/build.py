"""Inline data/*.json into src/template.html and write dist/index.html."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAMES = ["questions", "glossary", "plan", "notes"]


def main() -> None:
    html = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    for name in NAMES:
        data = json.loads((ROOT / "data" / f"{name}.json").read_text(encoding="utf-8"))
        # Escape "</" so a value can never close the <script> tag early.
        payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        html = html.replace("{{" + name + "}}", payload, 1)
    assert "{{" not in html.split("<script>", 1)[0], "unfilled placeholder"
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")
    print(f"dist/index.html: {len(html) // 1024} KB")


if __name__ == "__main__":
    main()
