# Changelog

Notable changes to the M365 / AI privacy configuration kit. Dates are when
the change landed on `main`.

## 2026-06-27 — Second worked checklist (Northwind Clinical, US healthcare)
- `examples/checklist-northwind-clinical.md` — fully completed privacy
  configuration for a fictional US healthcare provider enabling M365
  Copilot under a Microsoft HIPAA Business Associate Agreement
- `tests/test_validate.py` extended to cover both example checklists

## 2026-06-27 — GitHub Actions CI
- `.github/workflows/ci.yml` running pytest + validate on Python 3.11
- CI status badge added to README

## 2026-06-27 — Build-out: worked example + linter + tests + usage doc
- `examples/checklist-meridian-advisory.md` — fully completed checklist for
  a fictional regulated advisory firm enabling M365 Copilot + Azure OpenAI
  RAG, with evidence/where-to-find-it notes per item
- `validate.py` — flags both unfilled `<…>` placeholders AND unchecked
  `- [ ]` items; suitable as a pre-sign-off gate
- 3 tests including a defensive check that internal-engagement tokens
  can't leak back into the template
- `docs/usage.md` — step-by-step usage including evidence capture,
  validation, per-industry customization
- README expanded with usage steps, file index, link to docs/usage.md
- Scrubbed a lingering reference to a past internal engagement from the
  bare template

## 2026-06-27 — Initial public release
- `privacy-config-checklist.md` — step-by-step settings and verifications:
  data residency, training/opt-out posture, tenant boundaries, identity,
  DLP / sensitivity, build-time hygiene, sign-off
