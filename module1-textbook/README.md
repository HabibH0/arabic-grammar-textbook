# Arabic Grammar: interactive textbook

Module 21 (`وجوه الكلمات`) adds 15 lessons and a cumulative review: 98 automatically checked exercises with 124 single-answer controls. It teaches how context distinguishes the functions of recurring words and letters, including alternative analyses, connected passages, and full تركيب. The paired Markdown files are `Module 21 - Words with Multiple Functions.md` and `Module 21 - Answers and Worked Solutions.md`; interactive questions are in `generator/items_m21.py`. Open it at `#M21/L0` after building.

Module 19 (`أحكام الفعل`) adds 11 lessons and a cumulative review: 78 automatically checked exercises with 139 single-answer controls. It covers verb forms, التصرف, النفي, التأكيد, التأنيث and التوحيد, with connected reading and worked تركيب. Its paired Markdown files are `Module 19 - Verb Forms and Agreement.md` and `Module 19 - Answers and Worked Solutions.md`; questions are in `generator/items_m19.py`. Open it at `#M19/L0` after building.

Module 18 (`التذكير والتأنيث والعدد`) adds 12 lessons and a cumulative review: 80 automatically checked exercises with 122 single-answer controls. Its lesson and solution Markdown are in `../modules/`; `generator/items_m18.py` supplies the matching interactive items. Open it at `#M18/L0` after building. Module 20 teaches الرسم والوصل والوقف in 8 lessons with 58 auto-checked exercises (98 answer controls), explicit writing/pronunciation distinctions, and full تركيب. Its paired Markdown files are `Module 20 - Writing Wasl and Waqf.md` and `Module 20 - Answers and Worked Solutions.md`; questions are in `generator/items_m20.py`.
Each question or table row has exactly one correct choice and a linked worked explanation.

Module 14 (`إعراب الاسم وبناؤه`) adds 10 lessons and a cumulative review: 68 automatically checked exercises with 114 single-answer controls. Its lesson and solution Markdown are in `../modules/`; `generator/items_m14.py` supplies the matching interactive items. Open it at `#M14/L0` after building. Module 15 teaches غير المنصرف in 8 lessons with 57 auto-checked exercises (95 answer controls), connected reading, and full تركيب. Its paired Markdown files are `Module 15 - Ghayr al-Munsarif.md` and `Module 15 - Answers and Worked Solutions.md`; questions are in `generator/items_m15.py`.
Each question or table row has exactly one correct choice and a linked worked explanation.

Source and build scripts for the interactive textbook (all modules) and the printable Module 1 workbook.

## Folders

| Folder | What it holds |
|---|---|
| `../modules/` | The markdown for every module: `Module NN - <Title>.md` and `Module NN - Answers and Worked Solutions.md`. Everything is generated from these. (Set in `SOURCE_DIR`, `generator/common.py`.) |
| `generator/` | Python scripts that turn the markdown into the textbook and the workbook. |
| `app/` | The interactive textbook. `index.html` is the shell and contents page; `modules/mNN.js` holds one module each and is loaded only when opened. |
| `workbook/project/` | The printable A4 Module 1 workbook pages (`.dc.html`) and their layout file `canvas.json`. |
| `source/` | The original Module 1 markdown. No longer read by the build (identical to `../modules/Module 01 …`); safe to delete. |

## Rebuilding

Needs Python 3, no extra packages. Run from inside `generator/`:

```
cd generator
python build_book.py   # writes app/index.html and app/modules/m01.js … mNN.js
python build.py        # writes the Module 1 workbook pages into workbook/project/
```

`build_book.py` finds every module pair in the source folder automatically. To add a module, drop its two
markdown files in and rebuild. It prints a "Check these" list if an exercise has no matching worked solution.

The app is a static site: serve the `app/` folder with any web server (locally: `python -m http.server --directory app`).
Opening `index.html` straight from disk also works.

## How modules are built

Modules 1–10 use **auto-checked** exercises: each one is a single-choice question or a table of choices with exactly one
correct answer, the page marks it, and the worked solution from the answers file can be revealed.
Module 8 includes 89 automatically checked tasks, including choice tables for connected reading and full tarkīb.
Module 9 adds 10 lessons and 68 automatically checked exercises (175 answer controls), with worked solutions.
Module 10 covers the eight مرفوعات in 10 lessons and 68 automatically checked exercises (175 answer controls), with worked solutions.
Module 11 covers المنصوبات in 12 lessons with 81 auto-checked exercises (132 answer controls), Arabic grammatical terminology, connected reading and worked تركيب. Its content and answers are in `../modules/Module 11 - Al-Mansubat.md` and `../modules/Module 11 - Answers and Worked Solutions.md`; interactive items are in `generator/items_m11.py`.
Module 12 covers المجرورات والتوابع in 11 lessons with 78 auto-checked exercises (169 answer controls), progressive Arabic reading, connected passages and full تركيب. Its standalone content and solutions are in `../modules/Module 12 - Al-Majrurat and Al-Tawabi.md` and `../modules/Module 12 - Answers and Worked Solutions.md`; the interactive bank is `generator/items_m12.py`. Open it at `#M12/L0`.
Module 13 covers محل الجملة وشبه الجملة in 9 lessons with 63 auto-checked exercises (159 answer controls), connected passages and full تركيب. Its standalone lessons and solutions are in `../modules/Module 13 - Sentence and Phrase Roles.md` and `../modules/Module 13 - Answers and Worked Solutions.md`; interactive items are in `generator/items_m13.py`. Open it at `#M13/L0`.
Module 16 covers إعراب الفعل وبناؤه in 9 lessons with 66 auto-checked exercises (150 answer controls). It includes the three نونات, weak endings, إعراب لفظي وتقديري ومحلّي, connected reading and full تركيب. Lessons and solutions are in `../modules/Module 16 - Verb Irab and Bina.md` and `../modules/Module 16 - Answers and Worked Solutions.md`; the interactive bank is `generator/items_m16.py`. Open it at `#M16/L0`.
Module 17 covers أقسام الاسم والمعرفة والنكرة in 11 lessons with 76 auto-checked exercises (182 answer controls), progressive Arabic reading, connected passages and full تركيب. Its standalone lessons and solutions are in `../modules/Module 17 - Noun Types and Definiteness.md` and `../modules/Module 17 - Answers and Worked Solutions.md`; interactive items are in `generator/items_m17.py`. Open it at `#M17/L0`.
Each question or table row has exactly one correct choice and a revealable worked solution.

- **Lesson text** comes from the module's markdown. Module 1 goes through its own pipeline (`build_app.py`, `teach.py`,
  `terms.py`); see `MODULE1_MD_VS_APP.md`. Modules 2 onwards are rendered by `generator/book.py`. In every module,
  English grammar terms in lessons, exercises and solutions are converted to their Arabic terms at build time for
  Modules 1–10. Modules 8–10 also use Arabic terminology directly in their authored lessons, questions, and solutions.
- **Exercises** are hand-authored, one file per module: `generator/app_items.py` (Module 1) and
  `generator/items_m02.py` … `items_m10.py`. Each markdown practice task becomes one or more items, using the same IDs
  (`3I-2`, `B2`, …) so the right worked solution is found automatically. Extra items split from one task use a suffix
  (`3G-1b`, `B2-1`) and point at the parent's solution with `sol='…'`.
- A module **without** an items file still works: its tasks appear as self-checked cards (write an answer, reveal the
  solution, mark yourself). Add `items_mNN.py` to make it auto-checked.

The markdown conventions `book.py` expects:

- `# Module N: Title`, optionally followed by an Arabic title line.
- `## Before you begin`, then `## Lesson N: Title` sections with `### ` sub-sections and a `### Practice` section.
- Practice sets as `**1G — Guided**` (or `**1G**`, `**1R — Review:** text`), with numbered tasks.
- One closing section (`## Module review…`, `## Cumulative practice`, …) with `### A. …` parts and `**A1.**` tasks.
  `### Ready to continue?` and any later `##` sections (Completion check, Self-check) are shown after the exercises.
- In the answers file: `## Lesson N`, then `### 1G` or `**1G**` blocks with numbered answers, `**Arabic reading:**`
  for the reading task, and the review section with matching `### A.` / `**A1.**` labels.

## Where to change things

| To change | Edit |
|---|---|
| Lesson text, tables, examples, exercises | The module's markdown in `../modules/`, then rebuild |
| Worked solutions | The module's answers markdown, then rebuild |
| Interactive exercises (options and correct answers) | `generator/app_items.py` (Module 1) or `generator/items_mNN.py` (other modules); shared helpers in `generator/item_kit.py`. `M(...)` is a single-choice question, `G(...)` is a table of choices. The correct answer is given as the option text. Option order is shuffled at build time. |
| Which solution an exercise shows | The exercise id (for example `3I-2`) matches the answer file's heading and number. Use `sol='2R'` to point an exercise at another solution, or `sol=SOLMD('…')` to write one where the answers file has none (Module 4's reading tasks). |
| English term to Arabic term conversion | Module 1: `generator/terms.py`, list `T`. Modules 2 onwards: `generator/terms_book.py`, list `T_BOOK` (runs before `T`). Most specific phrases first; an English word placed right after the Arabic term it defines is kept as a gloss, and quoted English translations are left alone. |
| Transliteration and dash clean-up (all modules) | `TRANSLIT` in `generator/common.py`. |
| Book title | `BOOK_TITLE` in `generator/build_book.py`. |
| Textbook look and behaviour | `app/template.html` (CSS at the top, JavaScript at the bottom). `__BOOK__` is replaced with the module list when building. |
| Printable workbook exercises and page style | `generator/lessons.py` (exercises and answer space) and `CSS` in `generator/common.py`. |

## Notes

- **Addresses.** `#home` is the contents page; `#M2/L3` is Module 2, Lesson 3 (`L0` introduction, `LR` the closing
  review). Links from the old single-module page (`#L3`) open Module 1.
- **Saving progress.** In a browser the textbook keeps progress in `localStorage` (key `textbook`; progress saved
  by the old single-module page is carried over). Username/password accounts save progress through the
  Neon API configured in `app/config.js`. Guest progress and account caches stay separate; use Account
  to import guest progress, sync manually or resolve changes made on another device. See `../README.md`.
- **Fonts.** Calibri and Traditional Arabic are used where installed, otherwise Carlito and Scheherazade New from Google Fonts.
- **Workbook pages.** The `.dc.html` files are written for the claude.ai Design canvas. They load a `support.js`
  runtime that only exists there, so they will not render correctly when opened directly. Their HTML and CSS are
  still plain and readable.
