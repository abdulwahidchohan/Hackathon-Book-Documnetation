# Validation Checklists

## Plagiarism Self-Check Plan

- [ ] **Policy Adherence**: Confirm 0% tolerance for plagiarism as per `spec/quality.yaml`.
- [ ] **Tools**: Identify and plan to use plagiarism detection software (e.g., Turnitin, Grammarly Premium, Copyscape).
- [ ] **Process**:
    - [ ] Run each chapter/section through chosen plagiarism checker.
    - [ ] Review reports for any matched content, even if minor.
    - [ ] Ensure all direct quotes are properly cited and enclosed in quotation marks.
    - [ ] Paraphrased content is rephrased sufficiently and accurately cited.
    - [ ] Self-plagiarism (reusing own previously published work without citation) is avoided or properly handled.
- [ ] **Documentation**: Maintain records of plagiarism check results for each major section or chapter.

## Readability Plan and Quick Testing Method

- [ ] **Target Score**: Aim for Flesch-Kincaid Grade 10-12 as per `spec/quality.yaml`.
- [ ] **Tools**: Utilize readability calculators (e.g., online tools, Microsoft Word, dedicated software).
- [ ] **Process**:
    - [ ] After drafting each chapter, run a readability analysis.
    - [ ] Identify sections with scores outside the target range.
    - [ ] Simplify complex sentences, replace jargon with more accessible terms where appropriate for the target audience, and break down long paragraphs.
    - [ ] Re-run analysis until the target range is met.
- [ ] **Quick Check**: For a quick spot-check, select a few paragraphs from each chapter and manually assess sentence length, word complexity, and active vs. passive voice.

## Fact-Checking Matrix Template

Create a spreadsheet or markdown table with the following columns for each factual claim:

| Claim (Snippet from Text) | Primary Source(s) (APA Citation) | Source Type (e.g., Journal, Conf, Doc) | Verification Notes (e.g., page #, specific section) | Verified (Y/N) | Reviewer | Date Verified |
|---------------------------|----------------------------------|---------------------------------------|----------------------------------------------------|----------------|----------|---------------|
| [e.g., Humanoids use SEAs for compliant control] | (Author, Year) | Journal Article | (Author, Year, p. 123) | N | | |
| [e.g., ROS 2 Humble is LTS] | (ROS Documentation, Year) | Official Doc | (ROS Documentation, Year, Section 2.1) | N | | |

- [ ] **Process**:
    - [ ] As content is drafted, populate this matrix with every factual claim.
    - [ ] For each claim, identify at least one authoritative primary source.
    - [ ] Systematically verify each claim against its source.
    - [ ] Document specific details (page numbers, section headings) from the source.
- [ ] **Coverage**: Ensure every chapter has claims tracked in this matrix.

## Source Coverage Report Template

Create a spreadsheet or markdown table to track source types and coverage:

| Chapter | Total Claims | Total Unique Sources | Peer-Reviewed Sources | % Peer-Reviewed | Missing Citations (Claims) | Citation Format Issues |
|---------|--------------|----------------------|-----------------------|-----------------|----------------------------|------------------------|
| 00      | 5            | 3                    | 1                     | 33%             | 0                          | 0                      |
| 01      | 10           | 6                    | 4                     | 66%             | 1                          | 0                      |
| ...     | ...          | ...                  | ...                   | ...             | ...                        | ...                    |
| **Total** | [Sum]        | [Sum]                | [Sum]                 | [Overall %]     | [Total Missing]            | [Total Issues]         |

- [ ] **Process**:
    - [ ] Populate this report after drafting each chapter and after fact-checking.
    - [ ] Track the count of claims, unique sources, and peer-reviewed sources.
    - [ ] Calculate the percentage of peer-reviewed sources (target ≥ 50%).
    - [ ] Note any claims that are missing citations or have incorrect APA formatting.
- [ ] **Action**: Use this report to identify and address gaps in citation coverage and quality.