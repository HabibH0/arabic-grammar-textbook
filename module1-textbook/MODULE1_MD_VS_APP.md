# Module 1: the markdown vs. what the app shows

The Module 1 markdown in `modules/` is **unchanged**. It is byte-for-byte the same as the original
`source/` copy. The "polish" for the interactive textbook is not in the markdown. It is applied by
the Module 1 generator (`generator/build_app.py`, `terms.py`, `common.py`, `teach.py`, `app_items.py`)
every time the app is built. To see or change the polish, look in those files, not in the `.md`.

Modules 2–7 do **not** get these transformations (see the last section).

## 1. English grammar terms are replaced with Arabic terms (`terms.py`)

About 110 English phrases are swapped for their Arabic term wherever they appear: in lesson text,
headings, titles, tables, prompts, options and solutions. The list runs most-specific first, and it
keeps an English term when it sits right after the Arabic word it glosses.

| Markdown | App |
|---|---|
| it does not mean that **إنّ** is a noun. **إنّ** is a particle; **كان** is a verb. | it does not mean that إنّ is a اسم. إنّ is a حرف; كان is a فعل. |
| For the verb's ending, … For the subject, **يكتب** is the governor | For the فعل's ending, … For the فاعل, يكتب is the عامل |
| Which sign identifies **قَلَمٌ** … as a noun | Which sign identifies قَلَمٌ … as a اسم |

This changes every lesson title except Lesson 8:

| Lesson | Markdown title | App title |
|---|---|---|
| 1 | Words and nouns | Words and أسماء |
| 2 | Verbs, particles, and the forms you need | أفعال, حروف, and the forms you need |
| 3 | Building a sentence and beginning tarkīb | Building a جملة and beginning تركيب |
| 4 | Sentence structure and sentences inside sentences | جملة structure and جمل inside جمل |
| 5 | Meaning, complete speech, and independent classifications | Meaning, كلام, and independent classifications |
| 6 | Phrases and what they attach to | شبه جملة and what they attach to |
| 7 | The roles of an implied-predicate phrase | The roles of a ظرف مستقرّ |
| 8 | Governing and being governed | *(unchanged)* |
| 9 | Visible, estimated, and positional iʿrāb | Visible, estimated, and positional إعراب |

## 2. Transliteration is removed (`TRANSLIT` in `common.py`)

- Transliteration in brackets is deleted: "**كَلِمَة** (*kalimah*, word)" becomes "كَلِمَة (word)", and
  "**جُمْلَة اِسْمِيَّة** (*jumlah ismiyyah*)" loses its bracket entirely.
- Transliterated terms are written in Arabic script: tanwīn → تنوين, fatḥah → فتحة, ḍammah → ضمة,
  kasrah → كسرة, sukūn → سكون, iḍāfah → إضافة, naṣb → نصب, jazm → جزم, rafʿ → رفع, tarkīb → تركيب,
  iʿrāb → إعراب, nāsikh → ناسخ, tāʾ → تاء, nūn → نون.

## 3. Punctuation and layout

- Em dashes become colons: "**لَنْ يَكْتُبَ خَالِدٌ.** — Khalid will not write." shows as an example
  block with the English gloss in italics. In running text, " — " becomes ": ".
- "Before you begin" becomes the **Introduction** page.
- Sections whose heading starts with "Worked" are put in a boxed "Worked example" panel.
- Lines that are a bold Arabic sentence, optionally with a gloss, become indented example blocks.

## 4. Reading tasks ("Read: …") are taken out of the lesson text

- **Lessons 2, 5 and 8:** the reading task becomes a separate **Reading** exercise (`2-Read`, `5-Read`,
  `8-Read`) at the end of Practice, with its answer as the worked solution.
- **Lessons 1, 3 and 4: the reading task is dropped and appears nowhere in the app.** These are
  الكَلِمَةُ ثَلَاثَةُ أَقْسَامٍ…, خَالِدٌ فَاعِلٌ مَرْفُوعٌ…, and الجُمْلَةُ الكُبْرَى تَشْتَمِلُ…. This looks like an
  oversight in the original generator. Their answers exist in the answers file.

## 5. Exercises were re-written as auto-checked questions (`app_items.py`)

The markdown's practice tasks are open questions. In the app, each was re-authored by hand as an
auto-checked item, mostly one-for-one with the same IDs. Of the 94 items, 34 are single-choice
questions and 60 are tables of choices (pills or dropdowns). What this changes:

- **Prompts are shortened**, because the choices now carry the content:
  - Markdown 5G-1: "Classify **هَلْ فَتَحَ خَالِدٌ البَابَ؟** on three axes: nominal/verbal,
    report/performative, affirmative/non-affirmative."
  - App: "Classify هَلْ فَتَحَ خَالِدٌ البَابَ؟ on three axes." The axes become table columns with choices.
- **Answers are fixed choices.** Questions that asked students to explain, correct or analyse in their
  own words are now "pick the right explanation" questions. For example, 2I-2 offers options (a) and (b).
- **Option order is shuffled** at build time, with a fixed seed per exercise. Fixed sets such as
  Yes/No are not shuffled.
- **Extra items the markdown doesn't have:**
  - **Split from one task:** `2R-b` and `6G-1b`, plus `C1-b`, `C2-b`, `C2-c` and `E1-b` in the review.
  - **Review B2 and D2:** each is split into three items (`B2-1…3`, `D2-1…3`).
- **Worked solutions** are cut out of the answers file per numbered item. They get the same term
  conversion as the lessons. `sol='…'` in `app_items.py` points an item at a different solution.

## Modules 2–7

Modules 2–7 are rendered by the general parser (`generator/book.py`). Their English grammar terms are converted to
Arabic like Module 1's (§1), using `generator/terms_book.py`. Its list runs before Module 1's and handles these modules'
wordings: “first object” → مفعول به أوّل, “subject–predicate” → مبتدأ–خبر, “fixed on” → مبني على, “prohibitive لا” →
لا الناهية, “implicit هو” → ضمير مستتر تقديره هو. It keeps an English gloss only when it sits directly after the Arabic
term it defines, and leaves quoted English translations alone. They also get:

- the bracketed-transliteration removal and dash clean-up from §2–3
- the Introduction page, worked-example boxes and example blocks

Their exercises now follow Module 1's approach (§5). Every practice task was re-authored as auto-checked items in
`generator/items_m02.py` … `items_m07.py`, with the correct answers taken from each module's answers file. Each lesson's
"Read: …" task became a Reading exercise. Module 4's answers file has no reading answers, so its 12 reading items carry
short worked solutions written into `items_m04.py`.
