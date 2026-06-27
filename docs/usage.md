# Usage

How to actually use this kit before any Copilot / Azure OpenAI build in a
client tenant.

## Step 1 — Walk the checklist with the client's admin

Copy `privacy-config-checklist.md` to `checklist-<client>-<date>.md` and
work through it with the client's IT / compliance owner present. For each
item:

- **Verify** the current state against the relevant Microsoft / vendor
  documentation (always retrieved fresh — settings and product behaviour
  change; record the URL + retrieved date in your notes).
- **Configure** if needed (the configuration steps belong in the client's
  change-management process, not in this checklist).
- **Capture evidence** — screenshots, ticket numbers, signed records — in
  a sibling `evidence/` folder. Reference them inline so the auditor
  doesn't have to ask twice.

The worked example
[examples/checklist-meridian-advisory.md](../examples/checklist-meridian-advisory.md)
shows the level of specificity that actually constitutes assurance:

- Each `- [x]` item names **what** was verified, **where** the evidence
  lives, and the **specific Microsoft control** that was used (e.g. the
  exact Entra ID setting name, the exact Azure OpenAI portal path).
- Items don't reach `- [x]` until the evidence is captured. "We agreed
  verbally" doesn't count.
- **N/A is a legitimate response** — used in the example for the
  "non-Microsoft model" row. Mark it explicitly so the auditor knows it
  wasn't skipped.

## Step 2 — Validate before sign-off

```bash
python validate.py examples/checklist-meridian-advisory.md   # check a specific file
python validate.py                                            # check every file under examples/
```

The linter flags two things:

- **Angle-bracket placeholders** (`<tenant>`, `<region>`) that you forgot
  to fill.
- **Unchecked `- [ ]` items** that haven't been responded to.

Exit code 0 if both lists are empty. Run it before the compliance owner's
review — handing them a doc with leftover `<…>` markers or untouched
checkboxes is the single fastest way to lose their trust.

## Step 3 — Deliver as the client's privacy assurance document

Attach the completed checklist (plus the evidence folder) to the
engagement's handover pack so the client has the audit trail when their
compliance team asks. Pair naturally with:

- [project-handover-pack](https://github.com/derekgallardo01/project-handover-pack)
  — the operational handover.
- [copilot-studio-support-agent](https://github.com/derekgallardo01/copilot-studio-support-agent)
  / [rag-over-docs-kit](https://github.com/derekgallardo01/rag-over-docs-kit)
  — the actual AI build the checklist supports.

## Customizing the kit

### Adding a new checklist section

Edit `privacy-config-checklist.md`. Useful additions per industry:

- **Healthcare:** sections for HIPAA / HDS / NHS DSPT obligations
  depending on jurisdiction.
- **Financial services:** sections for FCA / APRA / SOX-style control
  evidence.
- **Government:** sections for FedRAMP / IRAP / IL5 boundary verification.

After adding, run validate on the bare template — the new checkboxes
must appear as unchecked (otherwise they're not actually required).

### Adding a worked example

Copy your engagement's completed checklist into `examples/` under a
non-real client name. Run validate — it should pass clean. Add the file
to `tests/test_validate.py` so the new example is regression-tested.

### Defensive checks worth keeping

`tests/test_validate.py` includes a "no internal-engagement leaks in
template" test that fails if specific client / internal tokens appear in
the bare template. Extend this list if you ever spot another leak — the
test is cheap and it's the only thing that catches "did past-me leave
something private here?" before publication.

## What this kit is not

- **Not a substitute for legal review.** The checklist captures
  *technical configuration*; data-protection clauses, indemnities, and
  liability live in the contract.
- **Not exhaustive of Microsoft's surface area.** Tenant-level features
  change. Always verify the current Microsoft Learn page for the
  setting; the checklist tells you *what to confirm*, not *what the
  current product behaviour is*.
- **Not a one-time exercise.** Re-run before each significant change —
  enabling a new connector, adding a new Copilot scope, pointing the RAG
  pilot at a new SharePoint site.
