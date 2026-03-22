IncluScore — Scoring Framework
This document contains the full scoring criteria, sub-weightings and international standard mappings for IncluScore's three evaluation pillars.

Note: Current weightings are based on research literature and are subject to revision following field validation with Ghanaian educators and child safety advocates. If you are an educator, researcher or practitioner working in this space, your input is welcome — open an issue or reach out directly.

Pillar Weightings
PillarWeightAccessibility40%Child Safety35%Equity & Inclusion25%

Pillar 1 — Accessibility (40%)
Validated against WCAG 2.1 AA
CriterionStandardWeight within PillarText alternatives for non-text contentWCAG 1.1.115%Captions for audio and videoWCAG 1.2.210%Text contrast ratio 4.5:1 minimumWCAG 1.4.312%Text resizable to 200% without lossWCAG 1.4.48%Full keyboard accessibilityWCAG 2.1.118%No content flashing more than 3x per secondWCAG 2.3.17%Page language programmatically identifiedWCAG 3.1.110%Input errors identified and describedWCAG 3.3.110%Compatible with major screen readersWCAG 4.1.210%

Pillar 2 — Child Safety (35%)
Validated against UNICEF CRC / COPPA / GDPR-K / EU AI Act
CriterionStandardWeight within PillarData minimizationGDPR-K / COPPA20%Verifiable parental consentCOPPA Art.518%Child data encrypted in transit and at restGDPR Art.3215%Effective content moderationUNICEF CRC Art.1715%Age-appropriate content and interfaceUNICEF Digital Rights12%No manipulative dark patternsEU AI Act Art.510%No unsupervised messaging between unknown usersUNICEF CRC Art.1910%

Pillar 3 — Equity & Inclusion (25%)
Validated against UDL Guidelines + SDG 4
CriterionStandardWeight within PillarContent available in multiple formatsUDL Guideline 118%Multilingual or home language supportUDL Guideline 215%Multiple input types acceptedUDL Guideline 412%Self-paced and learner-directedUDL Guideline 712%Functions on low-bandwidth connectionsSDG 4 / ITU18%Works on low-cost and older devicesSDG 413%Free tier or affordable pricingSDG 4.112%

How Scores Are Calculated
Each criterion within a pillar is scored on a scale of 0–10 by the evaluator. The score for each criterion is multiplied by its weight within the pillar. The weighted pillar scores are then multiplied by the pillar's overall weight and summed to produce the final IncluScore out of 100.
Example:

A platform scores 8/10 on keyboard accessibility (WCAG 2.1.1)
Keyboard accessibility carries 18% weight within the Accessibility pillar
Accessibility carries 40% of the total score
Contribution to total score: 8 × 0.18 × 0.40 = 0.576 points from this criterion alone


Score Thresholds
ScoreVerdict85–100High Inclusion — Meets standards across all pillars70–84Good Inclusion — Minor improvements recommended50–69Moderate Inclusion — Significant gaps identified30–49Low Inclusion — Major barriers present0–29Critical Failure — Not recommended for child use

Context Adjustment (In Development)
Future versions of IncluScore will calibrate scores based on the evaluating school's context — device type, connectivity level and school classification. A criterion like "functions on low-bandwidth connections" will carry higher weight for a rural government school than for an international school with reliable WiFi.
This context layer is currently in the roadmap. See README.md for full roadmap details.

Contributing to the Framework
The scoring framework is the intellectual core of IncluScore and benefits most from input by people closest to the problem — teachers, school administrators, child safety advocates and researchers working in Global South education contexts.
If you have expertise in any of the standards referenced above or direct experience with EdTech in low-resource environments, your input on the criteria and weightings is especially welcome.
Open an issue on GitHub or reach out via the contact details in README.md.
