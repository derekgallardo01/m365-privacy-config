# FAQ

## Do I need this for every engagement?

For any AI build (Copilot / Azure OpenAI / RAG) in a regulated industry
or a privacy-conscious client: yes. For a small Power Automate flow
with no PII: no — overkill. The threshold is roughly "would a
compliance officer be unhappy if they discovered this build six months
in?"

## What does "in scope" mean in the BAA / no-retention context?

Microsoft's Business Associate Agreement (BAA) covers specific services
— not every Azure service is in scope. For HIPAA work, confirm that the
specific Azure / M365 services you're using are listed in the current
BAA scope. The Northwind Clinical example records the email thread
where this was confirmed in writing.

## Is "private API tier" enough to claim "no public-model training"?

For OpenAI / Anthropic via their enterprise tiers, yes — but record the
specific contractual commitment. For Azure OpenAI, the no-retention +
customer-managed-keys options need to be explicitly enabled by Microsoft
on request (default behaviour has 30-day retention for abuse
monitoring). The Meridian Advisory example records the Microsoft
approval ticket.

## What if the client doesn't have a compliance owner?

Then the engagement IS the compliance review. Make sure someone with
authority signs off on §6 — usually the IT director or whoever holds
"security" in their job title. If no one will sign, that's a red flag
about the client's readiness for AI, not a problem with the checklist.

## How often should this be re-walked?

- **On significant changes**: new connector enabled, new SharePoint
  site added to scope, new AI model adopted, BAA renewed.
- **Annually**: even when nothing changed, settings drift and Microsoft
  product behaviour evolves.
- **On audit request**: pull out the most recent walked-version and
  refresh the date stamps after re-confirming.

## How is this different from Microsoft Purview?

Purview is Microsoft's *tooling* for compliance / DLP / sensitivity
labels. This checklist is a *process artefact* — a record of "we
checked these things, here's the evidence". They complement: Purview
provides the controls; the checklist documents that you confirmed they
were active for this engagement.

## Why a defensive test against internal-engagement tokens?

Because the template was originally drafted with a reference to a
specific past client engagement, which slipped through the public-
release scrub. The defensive test in `tests/test_validate.py` checks
the bare template for tokens like `claude client`, `copilot&claude`,
`internal client`, `for derek`, `playbook` — if any of these reappear,
CI fails loud. Belt-and-braces against "did past-me leave something
private here?"

## What if the client uses a different cloud (AWS, GCP)?

This checklist is M365-specific. The structure (data residency, no-
training, identity, DLP, sign-off) is portable; the specific
verifications aren't. Forking + adapting the structure for AWS/GCP is
a legitimate use — and a useful contribution back if you do.

## Industry-specific extensions?

Add sections per industry:
- **Healthcare**: HIPAA / NHS DSPT / HDS — see Northwind example for the
  US case.
- **Financial services**: FCA / APRA / SOX-style control evidence.
- **Government**: FedRAMP / IRAP / IL5 boundary verification.

After adding, run `python validate.py` on the bare template — the new
checkboxes must appear as unchecked.
