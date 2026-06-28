# M365 / AI privacy configuration — Northwind Clinical (worked example)

*Worked example. A fictional US-based multi-clinic healthcare provider
enabling Microsoft 365 Copilot for clinical administrative workflows
(scheduling, billing inquiries, internal HR Q&A) — explicitly NOT for
clinical decision-support. HIPAA Business Associate Agreement (BAA) in
place with Microsoft. Tenant region: US East. Engagement date: 2026-08-22.*

**Tenant:** `northwindclinical.onmicrosoft.com` · **M365 plan:** E5 + Microsoft 365 Copilot · **Region:** US East · **Compliance owners:** S. Hayes (CISO), Dr. M. Lin (Privacy Officer) · **Builder:** Derek G.

## 1. Data residency & tenant boundary
- [x] **Confirmed tenant data region.** All M365 / Exchange / SharePoint /
      Teams data stored in the US (multi-geo not used). Verified via the
      M365 admin center → Organization profile → Data location. Screenshot
      in `evidence/01-data-region.png`.
- [x] **Confirmed Copilot data stays within the M365 service boundary.**
      Verified against Microsoft Learn → "Data, Privacy, and Security for
      Microsoft 365 Copilot" (retrieved 2026-08-22; page revision id +
      URL in `evidence/01-copilot-boundary.md`).
- [x] **HIPAA-specific boundary check.** Microsoft is a Business Associate
      under the existing BAA between Northwind Clinical and Microsoft Corp
      (signed 2024-03; renewed 2026-03). M365 services in scope of the BAA
      include Exchange, SharePoint, OneDrive, Teams, and **Microsoft 365
      Copilot when used with the same in-scope services**. Confirmed in
      writing with the Microsoft account team (email thread saved as
      `evidence/01-baa-scope.eml`).
- *Assurance:* "Your data stays in your US tenant, covered by the HIPAA
  BAA with Microsoft."

## 2. Copilot / Azure OpenAI — no public-model training
- [x] **Microsoft 365 Copilot:** confirmed prompts / responses / tenant
      grounding data are **not** used to train Microsoft's foundation
      models, per Microsoft's Product Terms and the Copilot data-handling
      article above. Combined with the BAA, this covers PHI that
      Copilot may incidentally process from in-scope mailboxes.
- [x] **Azure OpenAI:** not in scope for this engagement. Northwind
      Clinical is not deploying any custom AI applications that call
      Azure OpenAI directly; only M365 Copilot is enabled. This row
      reopens if a future enhancement adds a custom application.
- [x] **Non-Microsoft model usage:** N/A — Northwind Clinical policy
      explicitly prohibits using non-Microsoft AI models for any
      workflow that may touch PHI.
- *Assurance:* "Your data is never used to train public AI models."

## 3. Identity & least privilege
- [x] **No standing admin in production.** All Global Admin and
      Exchange Admin roles are PIM-eligible only (just-in-time, max 4-hour
      activation, requires MFA + approval for >1 hour). Confirmed via Entra
      ID → Identity Governance → Privileged Identity Management.
- [x] **Conditional Access / MFA:** existing tenant policy "Require MFA
      for all users" applies; clinical staff additionally fall under a
      stricter CA policy that requires compliant device + named-location
      sign-in (clinic IP ranges) for any session that may access PHI.
- [x] **Access reviewed and time-boxed:** monthly access reviews
      configured in Entra ID Identity Governance for the
      "PHI-Authorized-Users" group. Owners = S. Hayes and the relevant
      clinic manager. No shared admin credentials in use; admin actions
      audited; activity reviewed by the CISO monthly.

## 4. Data loss prevention & sensitivity
- [x] **DLP policies cover PHI categories.** Existing tenant DLP policy
      "PHI — Names + DOB + SSN + Medical Record Numbers" applies to
      Exchange Online, SharePoint, OneDrive, and Teams chats. Microsoft
      365 Copilot inherits these policies — verified that a test prompt
      containing a fake SSN was correctly blocked from being included
      in the response history.
- [x] **Sensitivity labels applied where relevant.** "Highly Confidential
      — PHI" applied (encrypted, watermarked) to clinical-record
      libraries; "Confidential — Internal" applied to admin libraries.
      Encryption at rest (Microsoft-managed keys) and in transit
      (TLS 1.2+) confirmed.
- [x] **Connector restrictions (Power Platform DLP).** Default
      environment DLP policy is "Block-by-default"; only Microsoft 365
      connectors are in the Business group. Any new connector requires
      CISO approval and a documented business case.

## 5. Build-time hygiene (your practice)
- [x] **Built and tested with synthetic data only.** No real patient
      data, demographics, or identifiers used during any build or
      simulator work. The
      [copilot-studio-support-agent](https://github.com/derekgallardo01/copilot-studio-support-agent)
      simulator was used for the pre-tenant work with its bundled
      workplace corpus.
- [x] **No secrets in code or exports.** All client deliverables are
      reviewed for accidentally-included tenant ids, app secrets, or
      PHI before delivery. The engagement repo's `.gitignore` blocks
      `*.env` and `secrets/*`.
- [x] **Audit logging on.** Microsoft 365 unified audit log enabled
      (Purview compliance portal); Copilot activity audit is enabled
      and integrated with the SIEM (Microsoft Sentinel). Retention:
      365 days for unified audit, 7 years for HIPAA-relevant audit
      events (per Northwind's retention policy).

## 6. Sign-off
- [x] **Compliance owner review.** Both S. Hayes (CISO) and Dr. M. Lin
      (Privacy Officer) reviewed this configuration record on
      2026-08-22 and approved via Northwind's internal change-approval
      workflow (ticket CHG-2026-…).
- [x] **Configuration captured in the handover pack.** This document is
      attached to the engagement's
      [handover pack](https://github.com/derekgallardo01/project-handover-pack)
      and stored in `/sites/internal-compliance/Engagements/2026-08-copilot-rollout/`
      with the evidence screenshots.
