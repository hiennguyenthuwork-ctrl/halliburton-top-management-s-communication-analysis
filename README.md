# Wehkamp Wannagive Days Campaign Analysis
[![R](https://img.shields.io/badge/R-276DC3?style=flat&logo=r&logoColor=white)](https://www.r-project.org)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Result](https://img.shields.io/badge/Fair-Role-Distribution-brightgreen)
---
## Project Overview

An end-to-end textual analysis of Halliburton Co. (HAL) earnings conference calls (2016–2020). The project evaluates how top management communicates with investors, measuring executive participation, sentiment tone, and response specificity. By linking textual data with financial performance, the analysis uncovers critical gaps in CFO engagement and communication consistency.

**Goal**: Evaluate the transparency and effectiveness of executive communication in a cyclical industry to provide data-driven recommendations for Investor Relations (IR) strategy.

---

## Business Problem & Objective

In the volatile Oil & Gas sector, clear communication is currency. Halliburton needed to:
- Evaluate the distribution of communication responsibilities between CEO and CFO.
- Quantify the "informativeness" (specificity) vs. "evasiveness" of management.
- Validate if management's tone aligns with actual financial surprises.

**My task**: Process 514 responses from 19 calls, perform dictionary-based sentiment analysis, and validate results using **FinBERT (LLM)**.

---

## Key Results & Business Impact

**Executive Participation**
- **CEO Dominance**: Jeffrey Miller participated in 100% of calls (357 responses).
- **CFO Gap**: Lance Loeffler participated in only 42% of calls, falling below industry expectations for financial leadership presence.

**Communication Quality**
- **The "Specificity" Trade-off**: While the CEO maintains a consistently positive tone (+0.0098), the **CFO provides 2.5x more numerical specificity**, but at the cost of **a higher non-answer rate (7.51%)**.
- **Tone vs. Performance**: CEO tone correlates with positive earnings surprises (+20.1% positivity), whereas CFO tone showed an unusual inverse trend (-13.4%), suggesting a need for better messaging alignment.

**Methodology Validation**
- LLM Consistency: FinBERT validation confirmed dictionary-based sentiment results, ensuring the robustness of the Loughran-McDonald financial sentiment scoring.

---

## Methodology & Tech Stack

- Language: Python
- Libraries: pandas, nltk, re, scipy (Pearson correlation)
- NLP Models: Loughran-McDonald Financial Dictionary, FinBERT (Transformer model)
**Metrics:**
- Tone Score: (Positive−Negative)/TotalWords
- Specificity: Numerical token density per response.
- Non-Answer Score: Measuring evasiveness in Q&A.


## Project Structure
halliburton-top-management-s-communication-analysis
├── README.md
├── data/
│   └── conference_call_metadata.csv
├── scripts/
│   ├── 01_data_cleaning_matching.py
│   ├── 02_sentiment_analysis_lm.py
│   ├── 03_specificity_numerical_scoring.py
│   └── 04_performance_correlation.py
├── notebooks/
│   └── LLM_Validation_FinBERT.ipynb
├── visualizations/
│   ├── ceo_vs_cfo_participation.png
│   ├── tone_performance_correlation.png
│   └── specificity_by_role.png
└── requirements.txt

## How to Run the Code

```bash
git clone https://github.com/hiennguyenthuwork-ctrl/halliburton-top-management-s-communication-analysis.git
cd Wehkamp-Wannagive-Days

# Restore R environment
Rscript -e "renv::restore()"

# Run analysis
Rscript scripts/01_data_cleaning.R
