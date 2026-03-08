# scoring.py — IncluScore AI
# Evaluation framework built on WCAG 2.1, UDL (CAST), UNICEF Child Safety,
# UNESCO AI Ethics Recommendation (2021), and UN SDG 4.
#
# Author: Josiah Ryan Ofosuhene
# Version: 2.0

import pandas as pd
from dataclasses import dataclass, field
from typing import Optional

# ─────────────────────────────────────────────
# PILLAR WEIGHTS
# Accessibility is weighted highest because it
# is the most technically measurable and most
# directly linked to WCAG obligations.
# ─────────────────────────────────────────────
PILLAR_WEIGHTS = {
    "accessibility": 0.40,   # WCAG 2.1 AA — 40%
    "child_safety":  0.35,   # UNICEF / COPPA / GDPR-K — 35%
    "equity":        0.25,   # UDL + SDG 4 — 25%
}

# ─────────────────────────────────────────────
# SCORE THRESHOLDS & VERDICTS
# ─────────────────────────────────────────────
VERDICTS = [
    (85, "✅ High Inclusion — Meets standards across all pillars"),
    (70, "🟡 Good Inclusion — Minor improvements recommended"),
    (50, "⚠️  Moderate Inclusion — Significant gaps identified"),
    (30, "🔴 Low Inclusion — Major barriers present"),
    (0,  "❌ Critical Failure — Not recommended for child use"),
]

def get_verdict(score: float) -> str:
    for threshold, label in VERDICTS:
        if score >= threshold:
            return label
    return VERDICTS[-1][1]


# ─────────────────────────────────────────────
# CRITERIA DEFINITIONS
# Each criterion maps to a specific standard.
# ─────────────────────────────────────────────

ACCESSIBILITY_CRITERIA = {
    # WCAG 2.1 — Perceivable
    "text_alternatives":    {"standard": "WCAG 1.1.1", "description": "Non-text content has text alternatives (alt text, captions)", "weight": 0.15},
    "captions_audio":       {"standard": "WCAG 1.2.2", "description": "Captions provided for all audio/video content", "weight": 0.10},
    "color_contrast":       {"standard": "WCAG 1.4.3", "description": "Text has at least 4.5:1 contrast ratio against background", "weight": 0.12},
    "resize_text":          {"standard": "WCAG 1.4.4", "description": "Text can be resized up to 200% without loss of content", "weight": 0.08},
    # WCAG 2.1 — Operable
    "keyboard_navigation":  {"standard": "WCAG 2.1.1", "description": "All functionality accessible via keyboard alone", "weight": 0.18},
    "no_seizure_content":   {"standard": "WCAG 2.3.1", "description": "No content flashes more than 3 times per second", "weight": 0.07},
    # WCAG 2.1 — Understandable
    "readable_language":    {"standard": "WCAG 3.1.1", "description": "Language of page is programmatically identified", "weight": 0.10},
    "error_identification": {"standard": "WCAG 3.3.1", "description": "Input errors are clearly identified and described", "weight": 0.10},
    # WCAG 2.1 — Robust
    "screen_reader_compat": {"standard": "WCAG 4.1.2", "description": "Compatible with common screen readers (NVDA, JAWS, VoiceOver)", "weight": 0.10},
}

CHILD_SAFETY_CRITERIA = {
    # Data Privacy
    "data_minimization":    {"standard": "GDPR-K / COPPA", "description": "Only collects data strictly necessary for the educational function", "weight": 0.20},
    "parental_consent":     {"standard": "COPPA Art.5", "description": "Verifiable parental consent obtained before collecting child data", "weight": 0.18},
    "data_encryption":      {"standard": "GDPR Art.32", "description": "All stored and transmitted child data is encrypted", "weight": 0.15},
    # Content Safety
    "content_moderation":   {"standard": "UNICEF CRC Art.17", "description": "Effective content moderation preventing harmful material", "weight": 0.15},
    "age_appropriateness":  {"standard": "UNICEF Digital Rights", "description": "Content and interface designed appropriately for target age group", "weight": 0.12},
    # Interaction Safety
    "no_dark_patterns":     {"standard": "EU AI Act Art.5", "description": "No manipulative design patterns exploiting child vulnerabilities", "weight": 0.10},
    "safe_communication":   {"standard": "UNICEF CRC Art.19", "description": "No unsupervised direct messaging between unknown users", "weight": 0.10},
}

EQUITY_CRITERIA = {
    # UDL — Multiple Means of Representation (Principle 1)
    "multiple_formats":     {"standard": "UDL Guideline 1", "description": "Content available in multiple formats (text, audio, visual, video)", "weight": 0.18},
    "language_support":     {"standard": "UDL Guideline 2", "description": "Supports learners' home language or multilingual interface", "weight": 0.15},
    # UDL — Multiple Means of Action & Expression (Principle 2)
    "flexible_input":       {"standard": "UDL Guideline 4", "description": "Accepts multiple forms of input (voice, touch, keyboard, drawing)", "weight": 0.12},
    # UDL — Multiple Means of Engagement (Principle 3)
    "learner_autonomy":     {"standard": "UDL Guideline 7", "description": "Learners can set their own goals and work at their own pace", "weight": 0.12},
    # Equity — Infrastructure
    "low_bandwidth":        {"standard": "SDG 4 / ITU", "description": "Functions on low-bandwidth or intermittent internet connections", "weight": 0.18},
    "device_agnostic":      {"standard": "SDG 4", "description": "Works on low-cost devices (Android, basic tablets, older browsers)", "weight": 0.13},
    # Equity — Cost
    "affordability":        {"standard": "SDG 4.1", "description": "Free tier or affordable pricing appropriate for low-income schools", "weight": 0.12},
}

ALL_CRITERIA = {
    "accessibility": ACCESSIBILITY_CRITERIA,
    "child_safety": CHILD_SAFETY_CRITERIA,
    "equity": EQUITY_CRITERIA,
}


# ─────────────────────────────────────────────
# SCORING FUNCTIONS
# ─────────────────────────────────────────────

def normalize(value: float, min_val: float = 0, max_val: float = 10) -> float:
    """Normalize a raw score to 0–1 range."""
    if max_val == min_val:
        return 0.0
    return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))


def calculate_pillar_score(scores: dict, criteria: dict) -> float:
    """
    Calculate a weighted pillar score (0–100) from a dict of criterion scores.
    Each score should be on a 0–10 scale.
    """
    total_weight = 0
    weighted_sum = 0
    for key, meta in criteria.items():
        if key in scores:
            normalized = normalize(float(scores[key]))
            weighted_sum += normalized * meta["weight"]
            total_weight += meta["weight"]
    if total_weight == 0:
        return 0.0
    return round((weighted_sum / total_weight) * 100, 2)


def calculate_composite_score(pillar_scores: dict) -> float:
    """
    Calculate the final IncluScore (0–100) from pillar scores.
    """
    total = 0
    for pillar, weight in PILLAR_WEIGHTS.items():
        total += pillar_scores.get(pillar, 0) * weight
    return round(total, 2)


def calculate_survey_score(
    # Accessibility
    text_alternatives: int = 5,
    captions_audio: int = 5,
    color_contrast: int = 5,
    resize_text: int = 5,
    keyboard_navigation: int = 5,
    no_seizure_content: int = 5,
    readable_language: int = 5,
    error_identification: int = 5,
    screen_reader_compat: int = 5,
    # Child Safety
    data_minimization: int = 5,
    parental_consent: int = 5,
    data_encryption: int = 5,
    content_moderation: int = 5,
    age_appropriateness: int = 5,
    no_dark_patterns: int = 5,
    safe_communication: int = 5,
    # Equity
    multiple_formats: int = 5,
    language_support: int = 5,
    flexible_input: int = 5,
    learner_autonomy: int = 5,
    low_bandwidth: int = 5,
    device_agnostic: int = 5,
    affordability: int = 5,
) -> dict:
    """
    Full survey-based scoring. Returns pillar scores, composite score, and verdict.
    All inputs on a 0–10 scale.
    """
    accessibility_scores = {
        "text_alternatives": text_alternatives,
        "captions_audio": captions_audio,
        "color_contrast": color_contrast,
        "resize_text": resize_text,
        "keyboard_navigation": keyboard_navigation,
        "no_seizure_content": no_seizure_content,
        "readable_language": readable_language,
        "error_identification": error_identification,
        "screen_reader_compat": screen_reader_compat,
    }
    safety_scores = {
        "data_minimization": data_minimization,
        "parental_consent": parental_consent,
        "data_encryption": data_encryption,
        "content_moderation": content_moderation,
        "age_appropriateness": age_appropriateness,
        "no_dark_patterns": no_dark_patterns,
        "safe_communication": safe_communication,
    }
    equity_scores = {
        "multiple_formats": multiple_formats,
        "language_support": language_support,
        "flexible_input": flexible_input,
        "learner_autonomy": learner_autonomy,
        "low_bandwidth": low_bandwidth,
        "device_agnostic": device_agnostic,
        "affordability": affordability,
    }

    pillar_scores = {
        "accessibility": calculate_pillar_score(accessibility_scores, ACCESSIBILITY_CRITERIA),
        "child_safety": calculate_pillar_score(safety_scores, CHILD_SAFETY_CRITERIA),
        "equity": calculate_pillar_score(equity_scores, EQUITY_CRITERIA),
    }

    composite = calculate_composite_score(pillar_scores)

    return {
        "composite_score": composite,
        "pillar_scores": pillar_scores,
        "verdict": get_verdict(composite),
        "detail": {
            "accessibility": accessibility_scores,
            "child_safety": safety_scores,
            "equity": equity_scores,
        }
    }


def calculate_csv_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate IncluScore from a CSV DataFrame.

    Expected columns (all scored 0–10):
    Accessibility columns: text_alternatives, captions_audio, color_contrast,
      resize_text, keyboard_navigation, no_seizure_content, readable_language,
      error_identification, screen_reader_compat

    Child Safety columns: data_minimization, parental_consent, data_encryption,
      content_moderation, age_appropriateness, no_dark_patterns, safe_communication

    Equity columns: multiple_formats, language_support, flexible_input,
      learner_autonomy, low_bandwidth, device_agnostic, affordability

    Falls back to simplified scoring (Accessibility, Safety, Equity as averages)
    if full columns are not present.
    """
    # Check for full column set
    accessibility_cols = list(ACCESSIBILITY_CRITERIA.keys())
    safety_cols = list(CHILD_SAFETY_CRITERIA.keys())
    equity_cols = list(EQUITY_CRITERIA.keys())

    all_full_cols = accessibility_cols + safety_cols + equity_cols

    if all(col in df.columns for col in all_full_cols):
        # Full scoring mode
        rows = []
        for _, row in df.iterrows():
            a_score = calculate_pillar_score(row.to_dict(), ACCESSIBILITY_CRITERIA)
            s_score = calculate_pillar_score(row.to_dict(), CHILD_SAFETY_CRITERIA)
            e_score = calculate_pillar_score(row.to_dict(), EQUITY_CRITERIA)
            composite = calculate_composite_score({
                "accessibility": a_score,
                "child_safety": s_score,
                "equity": e_score,
            })
            rows.append({
                "Accessibility_Score": a_score,
                "ChildSafety_Score": s_score,
                "Equity_Score": e_score,
                "IncluScore": composite,
                "Verdict": get_verdict(composite),
            })
        return df.join(pd.DataFrame(rows))

    # Fallback: simplified 3-column mode
    fallback_cols = ["Accessibility", "Safety", "Equity"]
    if all(col in df.columns for col in fallback_cols):
        df = df.copy()
        df["Accessibility_Score"] = df["Accessibility"].apply(lambda x: round(normalize(float(x)) * 100, 2))
        df["ChildSafety_Score"]   = df["Safety"].apply(lambda x: round(normalize(float(x)) * 100, 2))
        df["Equity_Score"]        = df["Equity"].apply(lambda x: round(normalize(float(x)) * 100, 2))
        df["IncluScore"] = df.apply(lambda r: calculate_composite_score({
            "accessibility": r["Accessibility_Score"],
            "child_safety":  r["ChildSafety_Score"],
            "equity":        r["Equity_Score"],
        }), axis=1)
        df["Verdict"] = df["IncluScore"].apply(get_verdict)
        return df

    raise ValueError(
        "CSV must contain either the full criteria columns or at minimum: "
        "Accessibility, Safety, Equity (0–10 scale)."
    )


def print_score_report(result: dict, platform_name: str = "Platform"):
    """Pretty-print a scoring result to the console."""
    print(f"\n{'═'*50}")
    print(f"  IncluScore AI Report — {platform_name}")
    print(f"{'═'*50}")
    print(f"  Overall IncluScore:  {result['composite_score']:.1f} / 100")
    print(f"  Verdict: {result['verdict']}")
    print(f"\n  Pillar Breakdown:")
    for pillar, score in result["pillar_scores"].items():
        bar = "█" * int(score / 5) + "░" * (20 - int(score / 5))
        weight_pct = int(PILLAR_WEIGHTS[pillar] * 100)
        print(f"  {pillar.replace('_',' ').title():<20} [{bar}] {score:.1f}  (weight: {weight_pct}%)")
    print(f"{'═'*50}\n")


# ─────────────────────────────────────────────
# QUICK TEST
# ─────────────────────────────────────────────
if __name__ == "__main__":
    result = calculate_survey_score(
        # A platform with decent accessibility but weak safety and low equity
        text_alternatives=7, captions_audio=6, color_contrast=8,
        resize_text=7, keyboard_navigation=5, no_seizure_content=9,
        readable_language=8, error_identification=6, screen_reader_compat=5,
        data_minimization=4, parental_consent=3, data_encryption=6,
        content_moderation=5, age_appropriateness=7, no_dark_patterns=6,
        safe_communication=4,
        multiple_formats=6, language_support=4, flexible_input=5,
        learner_autonomy=6, low_bandwidth=3, device_agnostic=4,
        affordability=5,
    )
    print_score_report(result, "Sample EdTech Platform")
