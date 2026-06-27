# Microsoft 365 AI privacy & data-handling config

A practical checklist for configuring Microsoft 365 and Copilot so that
**client data stays in-tenant and is never used to train public AI models**
— the assurance regulated and privacy-conscious clients need before they'll
adopt AI features. Ships with a fully worked example for a fictional
regulated client and a linter that flags both unfilled placeholders and
unchecked items so a half-completed checklist can't be filed as the
client's privacy assurance document.

```bash
python validate.py                                          # check examples/ are fully responded-to
python validate.py checklist-meridian-advisory.md           # check your draft before sign-off
python -m pytest -q                                         # 3 tests gating the kit
```

## Why it exists

The first question a serious client asks about AI on their tenant is
"where does our data go, and is it used to train someone's model?" Being
able to answer that concretely — and configure it correctly — is often
the deciding factor in winning Copilot / AI work in regulated industries.

## What's inside

| File | Purpose |
|------|---------|
| [privacy-config-checklist.md](privacy-config-checklist.md) | Step-by-step settings and verifications: data residency, training/opt-out posture, tenant boundaries, identity, DLP / sensitivity, build-time hygiene, sign-off. |
| [examples/checklist-meridian-advisory.md](examples/checklist-meridian-advisory.md) | A fully completed checklist for a fictional regulated advisory firm enabling M365 Copilot + Azure OpenAI RAG. Shows the level of evidence to capture per item. |
| [validate.py](validate.py) | Linter — flags unfilled `<…>` placeholders **and** unchecked `- [ ]` items. Run before sign-off. |
| [tests/](tests/) | Self-tests: example validates clean; bare template still has unchecked items; defensive check that no internal-engagement tokens leaked into the template. |
| [docs/usage.md](docs/usage.md) | Step-by-step usage + how to customize per industry. |

## How to use it

1. Walk [privacy-config-checklist.md](privacy-config-checklist.md) against
   the client's tenant during setup with their IT / compliance owner
   present. Save the live copy as `checklist-<client>-<date>.md`.
2. Configure each item and **record the evidence** (screenshots,
   ticket numbers, retrieved Microsoft docs) in a sibling `evidence/`
   folder. Reference inline so an auditor can verify without asking.
3. Run `python validate.py checklist-<client>-<date>.md` before the
   compliance owner's review — half-completed checklists with leftover
   `<…>` markers or untouched checkboxes are the fastest way to lose
   trust.
4. Hand the completed checklist + evidence to the client as their privacy
   assurance document. It pairs naturally with any Copilot / AI build —
   see the
   [copilot-studio-support-agent](https://github.com/derekgallardo01/copilot-studio-support-agent)
   and [rag-over-docs-kit](https://github.com/derekgallardo01/rag-over-docs-kit)
   builds, and the
   [project-handover-pack](https://github.com/derekgallardo01/project-handover-pack)
   handover.

[docs/usage.md](docs/usage.md) walks the process end-to-end with the worked
example, and covers how to extend the checklist per industry (healthcare,
financial services, government).
