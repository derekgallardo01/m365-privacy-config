# Diagrams

This is a templates kit — the diagrams here are about how the privacy-
config checklist fits into an engagement, not about a runnable system.

## 1. Where the privacy-config runs in the engagement lifecycle

```mermaid
flowchart LR
    SOW["Signed SOW<br/>(discovery kit)"] --> HLD["HLD<br/>(architecture kit)"]
    HLD --> PRIV["**Privacy-config checklist**<br/>(THIS kit)"]
    PRIV --> SIGN{"Compliance owner<br/>signs off?"}
    SIGN -- "no, more work needed" --> CONFIG["Configure missing controls<br/>(via client change-mgmt)"]
    CONFIG --> PRIV
    SIGN -- "yes" --> BUILD["AI build proceeds<br/>(Copilot Studio / RAG / etc)"]
    BUILD --> HO["Handover<br/>(includes completed checklist<br/>as evidence)"]
```

The checklist gates the AI build. If §6 (sign-off) doesn't get signed,
the build doesn't start. Regulated clients require this; even
unregulated ones benefit from it as a procurement-readiness signal.

## 2. Checklist structure — six concerns, in order

```mermaid
flowchart TB
    S1["§1 Data residency & tenant boundary<br/>(M365 + Copilot stay in-tenant?)"] --> S2["§2 Copilot / Azure OpenAI -<br/>no public-model training<br/>(BAA / no-retention?)"]
    S2 --> S3["§3 Identity & least privilege<br/>(no standing admin, CA + MFA, time-boxed access)"]
    S3 --> S4["§4 Data loss prevention & sensitivity<br/>(DLP covers PII/PHI, labels applied, connector restrictions)"]
    S4 --> S5["§5 Build-time hygiene<br/>(synthetic data only, secret management, audit logging)"]
    S5 --> S6["§6 Sign-off<br/>(compliance owner reviews + approves; attached to handover)"]
```

The ordering matches the buyer's mental model: "where does our data
go?" → "is it used to train someone else's model?" → "who can access
it?" → "what stops it leaking?" → "how was the build itself safe?" →
"who signed off?"

## 3. Validator behaviour — placeholder + checkbox modes

```mermaid
flowchart TB
    CL["checklist-X.md"] --> V["python validate.py checklist-X.md"]
    V --> SCAN["Scan line-by-line"]
    SCAN --> P{"Line matches<br/><[^<>\\n]{1,80}> pattern?"}
    P -- "yes (not in code fence, not allowed HTML)" --> FLAG_P["Flagged: unfilled placeholder"]
    SCAN --> U{"Line matches<br/>^- \\[ \\]?"}
    U -- "yes" --> FLAG_U["Flagged: unchecked item"]
    FLAG_P --> REPORT["Per-line report"]
    FLAG_U --> REPORT
    REPORT --> EXIT["exit 0 if both lists empty<br/>exit 1 otherwise"]
```

Unlike the other template kits' validators (placeholder only), this one
ALSO flags unchecked items — because a checklist with an `- [ ]` item is
by definition incomplete, regardless of placeholders.

## 4. Two worked checklists — different regulatory contexts

```mermaid
flowchart TB
    subgraph MA["Meridian Advisory checklist"]
      M1["Region: Australia East"]
      M2["Regulatory: APP (Australian Privacy Principles)"]
      M3["AI: M365 Copilot + Azure OpenAI<br/>(no-retention approved)"]
      M4["Sign-off: CISO + Privacy Officer<br/>via internal approval workflow"]
    end
    subgraph NC["Northwind Clinical checklist"]
      N1["Region: US East"]
      N2["Regulatory: HIPAA BAA with Microsoft"]
      N3["AI: M365 Copilot only<br/>(no custom AOAI in scope)"]
      N4["Sign-off: CISO + Privacy Officer<br/>via change-approval workflow"]
    end
```

Same checklist structure; different evidence emphases (data residency,
which BAA, which regulatory regime, where the no-retention commitment
lives). The kit is region- and industry-agnostic by design.
