# M365 / AI privacy configuration checklist

Verify these with the client's admin before building. For each, record the current
state and the assurance it backs. **Always confirm against current Microsoft docs
for the client's licenses and region — settings and product behaviour change.**

## 1. Data residency & tenant boundary
- [ ] Confirm the tenant's data region(s) and where processing occurs.
- [ ] Confirm M365/Copilot data stays within the Microsoft 365 service boundary and
      isn't shared outside the tenant.
- *Assurance:* "Your data stays in your tenant, in <region>."

## 2. Copilot / Azure OpenAI — no public-model training
- [ ] **Microsoft 365 Copilot:** confirm prompts/responses/tenant data are **not**
      used to train the foundation models (per Microsoft's data-protection commitments).
- [ ] **Azure OpenAI:** confirm your data is **not** used to train/improve Microsoft
      or OpenAI models, and review the data-retention/abuse-monitoring settings
      (request the no-retention option where eligible).
- [ ] If a **non-Microsoft model** (e.g. Claude) is used, confirm via the vendor's
      enterprise terms that inputs aren't used for training, and prefer an
      enterprise/API tier with that guarantee.
- *Assurance:* "Your data is never used to train public AI models."

## 3. Identity & least privilege
- [ ] Service account / app registration uses least-privilege scopes only.
- [ ] Conditional Access / MFA enforced for accounts touching the solution.
- [ ] Access reviewed and time-boxed; no shared admin creds.

## 4. Data loss prevention & sensitivity
- [ ] DLP policies cover the data the solution touches (PII/financial/health).
- [ ] Sensitivity labels applied where relevant; encryption at rest/in transit confirmed.
- [ ] Connectors restricted (Power Platform DLP) so data can't flow to unapproved services.

## 5. Build-time hygiene (your practice)
- [ ] Build and test with **dummy / sample data**, never real client data —
      regulated clients typically require this contractually.
- [ ] No secrets in code or exports; use the tenant's secret store / connection refs.
- [ ] Audit logging on for the solution's actions.

## 6. Sign-off
- [ ] Client compliance owner reviews and approves the recorded configuration.
- [ ] Configuration captured in the handover pack.
