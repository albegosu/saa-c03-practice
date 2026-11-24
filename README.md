# SAA-C03 Practice

Free, open practice for the **AWS Certified Solutions Architect – Associate (SAA-C03)** exam: 573 original scenario questions, a glossary, 48 concept notes and a study plan, in a single static page.

**[Open the app →](https://albegosu.github.io/saa-c03-practice/)**

Every option of every question has its own explanation, so a wrong answer teaches the rule you were missing. Missed questions come back for review. Exams are scored on the real 100–1000 scale with a 720 pass mark.

## What it is, and what it is not

- **Original questions.** They were written from the [official exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) and the AWS documentation each explanation links to. There are no braindumps and no copied exam content.
- **Not a replacement for a full mock exam.** Use it for daily drills and to learn concepts. Before the real exam, also sit at least two timed full mocks from a source such as AWS Skill Builder's official practice set or Tutorials Dojo.
- **Not affiliated with AWS.** AWS and SAA-C03 are trademarks of Amazon.com, Inc.

## Coverage

| Exam domain | Exam weight | Questions here | Share |
| --- | --- | --- | --- |
| 1. Design secure architectures | 30 % | 166 | 29 % |
| 2. Design resilient architectures | 26 % | 132 | 23 % |
| 3. Design high-performing architectures | 24 % | 155 | 27 % |
| 4. Design cost-optimized architectures | 20 % | 120 | 21 % |

The bank is close to the exam weights. Domain 2 (resilience) is the most useful place to add questions.

## How to study with it

1. **Daily:** a 10-question *Quick drill* or *Review due*, 20–30 minutes.
2. **Weekly:** one *Full exam* (65 questions, 130 minutes) under real conditions.
3. **After every session:** add each miss to your own [error log](docs/error-log.md) as one line: the rule you did not know. Re-read that log in the last week before the exam; it is worth more than any new material.

Progress is saved in your browser (`localStorage`), so it stays on that device.

## Run locally

```bash
python3 scripts/validate.py   # checks every question's structure
python3 scripts/build.py      # writes dist/index.html
python3 -m http.server 8000 --directory dist
```

## Data

| File | Content |
| --- | --- |
| `data/questions.json` | Questions grouped in 8 study blocks. Fields: `d` domain (1–4), `q` stem paragraphs, `o` options, `a` correct indexes, `x` one explanation per option, `k` the key rule, `r` AWS doc links, `nt` related notes |
| `data/notes.json` | 48 concept notes (`id`, `t` title, `s` summary, `p` points, `tip` exam tip) |
| `data/glossary.json` | Terms per study block |
| `data/plan.json` | A 28-day plan |

To add a question, append it to the right block in `data/questions.json`, run `scripts/validate.py`, and open a pull request. Every explanation must link the AWS page that backs it.

## License

Code under the [MIT License](LICENSE). Questions, notes and glossary under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
