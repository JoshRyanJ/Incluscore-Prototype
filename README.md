# IncluScore

### The first child-centered digital inclusion assessment platform built for schools in the Global South.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Standard: WCAG 2.1](https://img.shields.io/badge/Standard-WCAG%202.1-blue.svg)](https://www.w3.org/WAI/WCAG21/quickref/)
[![SDG 4](https://img.shields.io/badge/SDG-4%20Quality%20Education-red.svg)](https://sdgs.un.org/goals/goal4)
[![Status: Prototype](https://img.shields.io/badge/Status-Prototype-orange.svg)](https://github.com/JoshRyanJ/Incluscore-Prototype)

**Live demo:** [incluscore-ai.streamlit.app](https://incluscore-ai.streamlit.app) · **Landing page:** [incluscoreai.netlify.app](https://incluscoreai.netlify.app)

---

## The Problem

Schools across Ghana and the Global South are adopting digital tools faster than anyone is asking whether those tools are safe, accessible or fair for the children using them.

A platform that works perfectly for a child on fiber internet in Accra performs entirely differently for a child on mobile data in Tamale. A tool that collects personal data from children without transparent consent doesn't stop doing so just because the school had no better option. Children with disabilities, learners in low-bandwidth environments and students from low-income schools are disproportionately excluded by platforms that were never designed with them in mind.

Existing inclusion tools measure workplace diversity inside corporations. None address whether EdTech platforms meet child safety, accessibility or equity standards. Particularly in Global South contexts.

IncluScore fills that gap.

---

## Why Context Matters

Most evaluation frameworks produce one universal score regardless of where a child is learning or what device they are using. IncluScore does not.

Before any assessment begins, the evaluator defines their school's context:

- **School type** — government, private, international
- **Primary student device** — smartphone, tablet, shared computer
- **Typical connectivity** — reliable WiFi, mobile data, limited or none

Truthfully, the same platform can score differently across different contexts. A tool that scores High Inclusion for a well-resourced private school in East Legon may score Low Inclusion for a rural government school in the Upper East Region. IncluScore reflects that reality honestly.

## What IncluScore Does

IncluScore enables school administrators and procurement officers to evaluate any digital learning platform across three core pillars — **Accessibility, Child Safety and Equity**  through observable, context-aware criteria that produce a defensible, actionable verdict.

The output is not just a score but a clear report that tells a decision maker:
- How inclusive the platform is for their specific school context
- The top risks identified across all three pillars
- Concrete recommendations they can act on immediately

## The Three Pillars

| Pillar | What It Evaluates | Weight |
|---|---|---|
| **Accessibility** | Can every child use this platform regardless of device, connectivity, ability or language? | 40% |
| **Child Safety** | Does this platform handle children's data responsibly, transparently and in compliance with applicable frameworks? | 35% |
| **Equity & Inclusion** | Does this platform assume resources, infrastructure or prior digital experience that many children in the Global South simply do not have? | 25% |

> Full scoring criteria, weighted sub-questions and standard mappings — [view SCORING.md](./SCORING.md)

## Score Thresholds

| Score | Verdict |
|---|---|
| 85–100 | **High Inclusion** — Meets standards across all pillars |
| 70–84 | **Good Inclusion** — Minor improvements recommended |
| 50–69 | **Moderate Inclusion** — Significant gaps identified |
| 30–49 | **Low Inclusion** — Major barriers present |
| 0–29 | **Critical Failure** — Not recommended for child use |

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
├── SCORING.md              # Full criteria, weights and standard mappings
└── README.md
```


## International Standards

These standards do not lead the evaluation — they validate it. Every criterion in IncluScore is grounded in observable, real-world questions relevant to Global South schools. The frameworks below are the evidence base that makes each criterion defensible to policymakers, funders and academic reviewers.

| Standard | Body | Relevance |
|---|---|---|
| WCAG 2.1 AA | W3C / WAI | Accessibility for users with disabilities |
| Ghana Data Protection Act 2012 | Republic of Ghana | Local child data protection |
| UDL Guidelines | CAST | Inclusive learning design |
| COPPA | US FTC | Children's online privacy |
| GDPR-K | EU | Child data protection |
| UNICEF CRC | United Nations | Convention on the Rights of the Child |
| UNESCO AI Ethics 2021 | UNESCO | AI in education |
| EU AI Act 2024 | EU | High-risk AI in education |
| SDG 4 | United Nations | Quality Education for All |

## Roadmap

- [x] Weighted scoring engine — 23 criteria across 3 pillars
- [x] CSV and survey input modes
- [x] Live Streamlit prototype
- [ ] Context-aware scoring calibration by school type and connectivity
- [ ] Automated privacy policy analysis cross-referenced against Ghana's Data Protection Act
- [ ] One-page actionable report output for school procurement officers
- [ ] PDF report generation
- [ ] Pilot evaluation with schools in Ghana
- [ ] Framework validation with educators and child safety advocates
- [ ] Public API for school procurement workflows

---

## Built By

**Josiah Ryan** — Software Engineering student, founder of [NoteWorthy Holdings](https://noteworthyholdings.netlify.app), and builder at the intersection of AI, education equity and child safety in the Global South.

Built in Ghana. For the Global South.

*IncluScore is an independent open source project and is not affiliated with any similarly named commercial products.*

## Contributing

IncluScore is open source and welcomes contributions from educators, researchers, developers and policy practitioners working in digital inclusion and EdTech accountability. Feedback, issues and pull requests are welcome.

## Contact

**GitHub:** [JoshRyanJ](https://github.com/JoshRyanJ)
**Medium:** [@josiahmail21](https://medium.com/@josiahmail21)
**LinkedIn:** [Josiah Ryan](https://linkedin.com/in/josiah-ryan-o-)
