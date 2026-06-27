# python-cert — project guide

Runnable study materials for Python certification prep (PCAP-31-03),
organized as lesson scripts under `pcap/NN_topic/`. (A DataQuest GenAI
Fundamentals skill track is also part of this prep.)

## Authoring conventions for study scripts
- **Untyped, to match the exam.** Lessons use plain, UNTYPED Python — PCAP-31-03
  tests untyped code. Keep type hints out of `pcap/NN_*/`; any typing/
  production-Python content goes in `pcap/99_bonus_not_on_exam/`.
- **Demonstrate errors live.** Show runtime errors with real `try/except` that
  catches the exception and `print()`s its message — never commented-out
  "this would raise X" lines. (Only true *syntax* errors stay as comments.)
  Before the exceptions module (`06_exception_handling`), add a pointer to it.
- **Teach the "why".** Explanations include design rationale, history, and the
  reasoning behind behavior — not just what, but why.
- **Verify before claiming.** Run new/changed scripts with the project venv
  (`.venv/Scripts/python.exe`, Python 3.14); confirm output matches the inline
  `# expected` comments. Use `PYTHONIOENCODING=utf-8` for Unicode demos.

## Quizzes
- Real PCAP format: 4 options (A–D), single- or multi-select, plausible
  distractors including error/exception outcomes. Grade with full rationale
  for every question, especially misses.
- When presenting answers, reprint each question with its options in a code
  block (monospace alignment), replacing the leading bullet with a marker:
  `+` = correct answer the user selected (got it right), `>` = correct answer
  the user missed (didn't select), `X` = wrong choice the user selected,
  space = an unselected distractor. Put the explanation after each question.
