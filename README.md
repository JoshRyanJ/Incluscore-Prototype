# IncluScore AI

 An open-source Digital Inclusion Scorecard for evaluating EdTech tools — built in Ghana, aligned with UN SDGs.

**Live demo:** [incluscore-ai.streamlit.app](https://incluscore-ai.streamlit.app) · **Landing page:** [incluscoreai.netlify.app](https://incluscoreai.netlify.app)

[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)
[![Standard: WCAG 2.1](https://img.shields.io/badge/Standard-WCAG%202.1%20AA-blue)](https://www.w3.org/WAI/WCAG21/quickref/)
[![SDG 4](https://img.shields.io/badge/SDG-4%20Quality%20Education-red)](https://sdgs.un.org/goals/goal4)
[![Status: Prototype](https://img.shields.io/badge/Status-Active%20Prototype-gold)]()

---

## The Problem

Schools across Ghana and the Global South are adopting digital learning tools fast — without any standard way to evaluate whether those tools are safe, accessible, or fair for every child. Children with learning disabilities, learners in low-bandwidth environments, and students from low-income schools are disproportionately excluded by platforms that were never designed with them in mind.

Existing "inclusion score" tools measure workplace diversity inside corporations. None address whether EdTech platforms meet child safety, accessibility, or equity standards — particularly in Global South contexts. IncluScore AI fills that gap.

> IncluScore AI is an independent open-source project and is not affiliated with any similarly named commercial products.

---

## What It Does

IncluScore AI evaluates digital learning platforms across three pillars:

| Pillar | Standard | Weight |
|---|---|---|
 Accessibility | WCAG 2.1 AA | 40% |
| Child Safety | UNICEF CRC / COPPA / GDPR-K / EU AI Act | 35% |
| Equity & Inclusion | UDL (CAST) + SDG 4 | 25% |

Every score is traceable to a specific international standard — not a number pulled from nowhere, but a defensible verdict schools and policymakers can act on.

---

## Scoring Framework

### Accessibility (WCAG 2.1)

| Criterion | Standard | Weight |
|---|---|---|
| Text alternatives for non-text content | WCAG 1.1.1 | 15% |
| Captions for audio and video | WCAG 1.2.2 | 10% |
| Text contrast ratio 4.5:1 minimum | WCAG 1.4.3 | 12% |
| Text resizable to 200% without loss | WCAG 1.4.4 | 8% |
| Full keyboard accessibility | WCAG 2.1.1 | 18% |
| No content flashing more than 3x/second | WCAG 2.3.1 | 7% |
| Page language programmatically identified | WCAG 3.1.1 | 10% |
| Input errors identified and described | WCAG 3.3.1 | 10% |
| Compatible with major screen readers | WCAG 4.1.2 | 10% |

### Child Safety

| Criterion | Standard | Weight |
|---|---|---|
| Data minimization | GDPR-K / COPPA | 20% |
| Verifiable parental consent | COPPA Art.5 | 18% |
| Child data encrypted in transit and at rest | GDPR Art.32 | 15% |
| Effective content moderation | UNICEF CRC Art.17 | 15% |
| Age-appropriate content and interface | UNICEF Digital Rights | 12% |
| No manipulative dark patterns | EU AI Act Art.5 | 10% |
| No unsupervised messaging between unknown users | UNICEF CRC Art.19 | 10% |

### Equity & Inclusion (UDL + SDG 4)

| Criterion | Standard | Weight |
|---|---|---|
| Content in multiple formats | UDL Guideline 1 | 18% |
| Multilingual or home language support | UDL Guideline 2 | 15% |
| Multiple input types accepted | UDL Guideline 4 | 12% |
| Self-paced and learner-directed | UDL Guideline 7 | 12% |
| Functions on low-bandwidth connections | SDG 4 / ITU | 18% |
| Works on low-cost and older devices | SDG 4 | 13% |
| Free tier or affordable pricing | SDG 4.1 | 12% |

### Score Thresholds

| Score | Verdict |
|---|---|
| 85–100 | High Inclusion — Meets standards across all pillars |
| 70–84 | Good Inclusion — Minor improvements recommended |
| 50–69 | Moderate Inclusion — Significant gaps identified |
| 30–49 | Low Inclusion — Major barriers present |
| 0–29 | Critical Failure — Not recommended for child use |

---

## Getting Started

**Requirements:** Python 3.9+

```bash
git clone https://github.com/JoshRyanJ/Incluscore-Prototype.git
cd Incluscore-Prototype
pip install -r requirements.txt
streamlit run app.py
```

Or use the scoring engine directly:

```python
from scoring import calculate_survey_score, print_score_report

result = calculate_survey_score(
    text_alternatives=7, keyboard_navigation=5, color_contrast=8,
    data_minimization=4, parental_consent=3,
    low_bandwidth=3, language_support=4,
)

print_score_report(result, "Platform Name")
```

---

## Project Structure

```
Incluscore-Prototype/
├── app.py                  # Streamlit application
├── scoring.py              # Core scoring engine
├── sample_data.csv         # Full 23-column sample data
├── sample_data_simple.csv  # Simplified 3-column sample
├── requirements.txt        # Dependencies
└── README.md
```

---

## Standards Referenced

| Standard | Body | Relevance |
|---|---|---|
| WCAG 2.1 AA | W3C / WAI | Accessibility for users with disabilities |
| UDL Guidelines | CAST | Inclusive learning design |
| COPPA | US FTC | Children's online privacy |
| GDPR-K | EU | Child data protection |
| UNICEF CRC | United Nations | Convention on the Rights of the Child |
| UNESCO AI Ethics 2021 | UNESCO | AI in education |
| EU AI Act (2024) | EU | High-risk AI in education |
| SDG 4 | United Nations | Quality Education for All |

---

## Roadmap

- [x] Weighted scoring engine — 23 criteria across 3 pillars
- [x] CSV and survey input modes
- [x] Live Streamlit prototype
- [ ] PDF report generation for school procurement officers
- [ ] Automated WCAG checks via accessibility API
- [ ] Pilot evaluation of EdTech tools used in Ghanaian schools
- [ ] Framework validation with educators and child-safety advocates
- [ ] Public API for school procurement workflows
---

*IncluScore AI is an active prototype. Contributions, feedback, and partnership inquiries are welcome.*
