# Getting started

The privacy-config kit runs before any Copilot / Azure OpenAI work
touches a client's tenant. Here's how to use it.

## 1. Walk the checklist with the client's admin

Copy [`privacy-config-checklist.md`](../privacy-config-checklist.md) to
`checklist-<client>-<date>.md` and work through it with the client's IT /
compliance owner **present**. For each item:

- **Verify** the current state against the relevant Microsoft / vendor
  documentation (always retrieved fresh — settings and product behaviour
  change; record the URL + retrieved date in your notes).
- **Configure** if needed (configuration goes through the client's
  change-management process, not this checklist).
- **Capture evidence** — screenshots, ticket numbers, signed records —
  in a sibling `evidence/` folder. Reference inline so an auditor
  doesn't have to ask twice.

## 2. Use the worked examples as level-of-detail reference

Two worked checklists ship in the kit:

- [`examples/checklist-meridian-advisory.md`](../examples/checklist-meridian-advisory.md)
  — Australian regulated advisory firm, M365 Copilot + Azure OpenAI
  RAG. AU East tenant, no-retention approved.
- [`examples/checklist-northwind-clinical.md`](../examples/checklist-northwind-clinical.md)
  — US healthcare provider, HIPAA Business Associate Agreement with
  Microsoft. PHI in scope, DLP policies cover SSN/DOB/MRN.

Each `- [x]` row in the worked examples shows:
- **What** was verified (the specific Microsoft control)
- **Where** the evidence lives (file path / ticket / screenshot)
- **By whom** (compliance owner name) and **when** (date)

That's the standard a real compliance auditor expects.

## 3. Validate before sign-off

```bash
python validate.py
```

Flags two things:
- Unfilled `<...>` placeholders
- Unchecked `- [ ]` items

Exit 0 only when both lists are empty. Run before the compliance
owner's review — handing them a doc with leftover placeholders or
untouched checkboxes is the fastest way to lose their trust.

## 4. Deliver as the client's privacy assurance document

Attach the completed checklist (plus the evidence folder) to the
engagement's handover pack — the client has the audit trail when their
compliance team asks. Pairs naturally with the
[copilot-studio-support-agent](https://github.com/derekgallardo01/copilot-studio-support-agent)
/ [rag-over-docs-kit](https://github.com/derekgallardo01/rag-over-docs-kit)
build the checklist supports.

## What to read next

- [Usage](usage.md) · [Diagrams](diagrams.md) · [FAQ](faq.md)
