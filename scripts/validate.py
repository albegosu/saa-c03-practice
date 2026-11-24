"""Check the question bank for structural mistakes. Exit code 1 on any error."""
import json, pathlib, sys, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAINS = {1: "Secure", 2: "Resilient", 3: "High-performing", 4: "Cost-optimized"}


def load(name):
    return json.loads((ROOT / "data" / f"{name}.json").read_text(encoding="utf-8"))


def main() -> int:
    blocks, notes = load("questions"), load("notes")
    note_ids = {n["id"] for n in notes}
    errors, stems, count = [], collections.Counter(), collections.Counter()
    for block in blocks:
        for i, q in enumerate(block["q"], 1):
            qid = f"b{block['b']}-{i}"
            opts, ans, why = q["o"], q["a"], q["x"]
            if q["d"] not in DOMAINS:
                errors.append(f"{qid}: unknown domain {q['d']}")
            if not 4 <= len(opts) <= 6:
                errors.append(f"{qid}: {len(opts)} options")
            if len(why) != len(opts):
                errors.append(f"{qid}: {len(why)} explanations for {len(opts)} options")
            if not ans or any(not 0 <= a < len(opts) for a in ans) or len(set(ans)) != len(ans):
                errors.append(f"{qid}: bad answer indexes {ans}")
            if len(ans) > 1 and "Select" not in q["q"][-1]:
                errors.append(f"{qid}: multiple answers but the stem does not say 'Select'")
            if len(set(opts)) != len(opts):
                errors.append(f"{qid}: duplicate options")
            for ref in q.get("r", []):
                if not ref.startswith("https://"):
                    errors.append(f"{qid}: reference is not https: {ref}")
            for nid in q.get("nt", []):
                if nid not in note_ids:
                    errors.append(f"{qid}: unknown note {nid}")
            stems[" ".join(q["q"])] += 1
            count[q["d"]] += 1
    errors += [f"duplicate stem: {s[:70]}…" for s, n in stems.items() if n > 1]
    total = sum(count.values())
    print(f"{total} questions · " + " · ".join(f"{DOMAINS[d]} {count[d]}" for d in sorted(count)))
    for e in errors:
        print("ERROR", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
