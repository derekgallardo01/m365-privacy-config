# M365 / AI privacy configuration — Meridian Advisory (worked example)

*Worked example. A fictional regulated advisory firm enabling Microsoft 365
Copilot for staff use, with Azure OpenAI also in scope for a small RAG-over-
SharePoint pilot. Tenant region Australia East. Engagement date: 2026-08-12.*

**Tenant:** `meridianadvisory.onmicrosoft.com` · **M365 plan:** E5 + Microsoft 365 Copilot licenses · **Region:** Australia East · **Compliance owner:** R. Vasquez, Head of IT & Security · **Builder:** Derek G.

## 1. Data residency & tenant boundary
- [x] **Confirmed tenant data region.** All M365 / SharePoint / Exchange data
      stored in Australia East per the Microsoft 365 admin centre →
      Organization profile → Data location. Verified screenshot saved as
      `evidence/01-data-region.png`.
- [x] **Confirmed Copilot data stays within the M365 service boundary.**
      Verified against the Microsoft Learn page
      "Data, Privacy, and Security for Microsoft 365 Copilot" (retrieved
      2026-08-12; URL + page-revision-id captured in `evidence/01-copilot-boundary.md`).
- *Assurance:* "Your data stays in your tenant, in Australia East."

## 2. Copilot / Azure OpenAI — no public-model training
- [x] **Microsoft 365 Copilot:** confirmed prompts / responses / tenant
      grounding data are **not** used to train Microsoft's foundation
      models, per the data-protection commitments in Microsoft's Product
      Terms (DPA) and the Copilot data-handling article above.
- [x] **Azure OpenAI:** the pilot subscription (`med-aoai-prod-01`) has
      "Modified Content Filtering" disabled and the customer-managed
      no-retention option enabled (Microsoft application approved 2026-07-30,
      ref. CRM-2026-… in the engagement notes). Verified via Azure portal →
      OpenAI resource → Data privacy.
- [x] **Non-Microsoft model usage:** N/A — only M365 Copilot and Azure
      OpenAI are in scope. If a future enhancement adds Anthropic or
      another vendor, this row reopens for that vendor's enterprise terms.
- *Assurance:* "Your data is never used to train public AI models."

## 3. Identity & least privilege
- [x] **Service account / app registration scopes:** the Copilot Studio
      RAG pilot uses an app registration (`med-rag-pilot`) limited to
      `Sites.Selected` on three specific SharePoint sites
      (`/sites/policies`, `/sites/hr`, `/sites/it`). No tenant-wide
      `Sites.Read.All`.
- [x] **Conditional Access / MFA:** existing tenant CA policy "Require
      MFA for all users" applies; the service principal is exempt only
      from MFA (per Microsoft guidance) and is covered by a CA policy that
      restricts sign-in to a specific named IP range
      (Azure Function outbound IP).
- [x] **Access reviewed and time-boxed:** quarterly access review configured
      in Entra ID Identity Governance, owners = R. Vasquez and A. Okafor.
      No shared admin credentials in use; admin actions audited.

## 4. Data loss prevention & sensitivity
- [x] **DLP policies cover the data the solution touches.** The pilot
      indexes HR / Policies / IT SharePoint sites. Existing tenant DLP
      policy "PII — TFN / Medicare / Credit Card" applies to these sites;
      no new policy needed for the pilot scope.
- [x] **Sensitivity labels applied where relevant.** "Confidential —
      Internal" applied to the HR site by default; "General" on Policies.
      Encryption at rest (Microsoft-managed keys) and in transit (TLS 1.2+)
      confirmed.
- [x] **Connector restrictions (Power Platform DLP).** Default environment
      DLP policy "Business / Non-business / Blocked" was already in place;
      added the Copilot Studio connector to Business so it can read from
      SharePoint and write to Teams (only). Verified the pilot can't post
      to non-business connectors like X / public web.

## 5. Build-time hygiene (your practice)
- [x] **Built and tested with dummy / sample data.** The simulator in the
      [copilot-studio-support-agent](https://github.com/derekgallardo01/copilot-studio-support-agent)
      kit was used for pre-tenant work; production grounding documents
      were only attached after sign-off on this checklist.
- [x] **No secrets in code or exports.** App registration secrets stored
      in Azure Key Vault (`med-kv-prod-01`); flow uses a connection
      reference, never an embedded credential. The pilot repo has a
      `.gitignore` that blocks `*.env` / `secrets.json`.
- [x] **Audit logging on.** Microsoft 365 unified audit log is enabled
      (verified via Purview compliance portal); RAG-pilot service principal
      activity is filterable by app id.

## 6. Sign-off
- [x] **Compliance owner review.** R. Vasquez reviewed this configuration
      record on 2026-08-12 and signed off via the Meridian internal
      approval workflow (ticket COMP-2026-…).
- [x] **Configuration captured in the handover pack.** This document is
      attached to the engagement's
      [handover pack](https://github.com/derekgallardo01/project-handover-pack)
      and stored in `/sites/internal-it/Engagements/2026-08-meridian-rag-pilot/`
      with the evidence screenshots.
