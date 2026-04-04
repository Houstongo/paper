# Chapter 2 Sources and Figures Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Strengthen Chapter 2 with representative citations and a small number of directly cited classic figures while keeping the writing concise and aligned with later chapters.

**Architecture:** Keep the existing three-part Chapter 2 structure unchanged, then enrich each subsection with only the most necessary references. Add at most two or three classic original figures at the points that most improve comprehension: one around RAG workflow and one around CNT/SEM morphology characterization. Verify each round with the thesis compile chain instead of expanding the chapter into a textbook survey.

**Tech Stack:** LaTeX, BibTeX, XeLaTeX, existing thesis template, `chapters/chapter2.tex`, `reference/chapter1.bib`

---

### Task 1: Audit Chapter 2 structure and mark citation gaps

**Files:**
- Modify: `D:\Apaper\paperformat\docs\plans\2026-03-26-chapter2-sources-and-figures.md`
- Read: `D:\Apaper\paperformat\chapters\chapter2.tex`
- Read: `D:\Apaper\paperformat\reference\chapter1.bib`

**Step 1: Inspect the current chapter**

Read `D:\Apaper\paperformat\chapters\chapter2.tex` and list each subsection:
- `2.1.1` pre-trained LLMs and domain knowledge enhancement
- `2.1.2` RAG workflow
- `2.1.3` knowledge extraction/segmentation/vectorization
- `2.1.4` hybrid retrieval and evidence organization
- `2.2.1` SEM preprocessing
- `2.2.2` CNT image representation
- `2.2.3` morphology quantification basis
- `2.3.1` supervised regression basics
- `2.3.2` modeling methods
- `2.3.3` evaluation and interpretation

**Step 2: Mark the minimum citation targets**

Assign a reference target for each subsection:
- `2.1.x`: 2-4 references each
- `2.2.x`: 2-3 references each
- `2.3.x`: 2-4 references each

**Step 3: Define the image budget**

Limit figures to:
- one classic RAG workflow figure in `2.1.2`
- one classic CNT/SEM morphology figure in `2.2`
- optional third figure only if it directly supports morphology indicators

**Step 4: Record the selection rule**

Use only figures that are:
- classic and directly relevant
- easy to caption as “引自文献” or “引自文献，经裁剪”
- supportive of the subsection’s argument, not decorative

**Step 5: Commit**

Skip commit for now. This task is planning-only.

### Task 2: Select representative references for Section 2.1

**Files:**
- Modify: `D:\Apaper\paperformat\reference\chapter1.bib`
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Reuse existing Chapter 1 references first**

Prefer already-present entries relevant to:
- `Venugopal2024`
- `Choi2024`
- `Jiang2025`
- `Statt2023`
- `Miret2025`
- `Mostafa2024`
- `Soudani2024`

**Step 2: Add only missing backbone references**

If needed, add a small number of foundational RAG or retrieval references for:
- generic RAG workflow
- hybrid retrieval or evidence organization

**Step 3: Insert citations subsection by subsection**

Modify `D:\Apaper\paperformat\chapters\chapter2.tex` so that:
- `2.1.1` cites domain LLM/materials references
- `2.1.2` cites RAG workflow references
- `2.1.3` cites segmentation/chunking/vector retrieval references
- `2.1.4` cites hybrid retrieval/evidence chain references

**Step 4: Keep Chapter 2 general**

Do not move `MSFU`, `TCCER`, or Chapter 3-specific mechanism names into Chapter 2.

**Step 5: Verify formatting**

Run: `xelatex --interaction=nonstopmode demo.tex`
Expected: chapter compiles with citations rendered or with only expected rerun warnings.

### Task 3: Select representative references for Section 2.2

**Files:**
- Modify: `D:\Apaper\paperformat\reference\chapter1.bib`
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Reuse current morphology references**

Prefer current entries such as:
- `Brandley2018`
- `Imtiaz2023`
- `Yadav2024`
- `Jackman2013`
- `Zhang2009Morphology`

**Step 2: Add one general CNT characterization review if needed**

Use one review to support the contrast between SEM and other methods rather than adding many instrument references.

**Step 3: Add citations by task**

Place citations so that:
- `2.2.1` supports preprocessing and robustness
- `2.2.2` supports geometric/statistical representation
- `2.2.3` supports curvature, alignment, coverage density, and diameter distribution as morphology indicators

**Step 4: Keep the wording task-oriented**

Do not turn `2.2` into a digital image processing handbook.

**Step 5: Verify formatting**

Run: `xelatex --interaction=nonstopmode demo.tex`
Expected: no fatal errors, only expected rerun/layout warnings.

### Task 4: Select representative references for Section 2.3

**Files:**
- Modify: `D:\Apaper\paperformat\reference\chapter1.bib`
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Reuse existing modeling references**

Prefer current entries such as:
- `Hajilounezhad2021`
- `Lookman2019`
- `Chang2020`
- `Gao2023`
- `Li2025Matter`

**Step 2: Add only model-family references actually used later**

If Chapter 4 compares specific methods such as SVR, random forest, XGBoost, or MLP, add only those needed to justify the shortlist.

**Step 3: Emphasize the thesis stance**

Ensure `2.3.1` explicitly supports:
- relationship modeling over black-box prediction
- limited-sample materials context

**Step 4: Support interpretation**

If Chapter 4 later uses SHAP or feature importance, cite only the interpretation methods actually used.

**Step 5: Verify formatting**

Run: `xelatex --interaction=nonstopmode demo.tex`
Expected: successful compile with updated citations.

### Task 5: Insert one classic original figure in Section 2.1

**Files:**
- Create: `D:\Apaper\paperformat\figures\chapter2_rag_workflow.*`
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Choose a figure**

Select one classic, directly relevant RAG workflow figure that can be cited as an original figure with minimal editing.

**Step 2: Prepare the asset**

Save the image into `D:\Apaper\paperformat\figures\` with a stable filename such as:
- `chapter2_rag_workflow.png`

**Step 3: Insert it at `2.1.2`**

Add a single figure environment after the paragraph that introduces the standard RAG pipeline.

**Step 4: Write a restrained caption**

Use wording like:
- `检索增强生成的典型流程（引自文献[xx]）`
- or `……（引自文献[xx]，经裁剪）`

**Step 5: Verify**

Run: `xelatex --interaction=nonstopmode demo.tex`
Expected: figure renders, numbering updates correctly.

### Task 6: Insert one classic original figure in Section 2.2

**Files:**
- Create: `D:\Apaper\paperformat\figures\chapter2_cnt_sem.*`
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Choose a figure**

Select one classic CNT array morphology / SEM figure that directly supports:
- why SEM is important for array-scale morphology
- or why different morphology states matter

**Step 2: Prepare the asset**

Save the image into `D:\Apaper\paperformat\figures\` with a stable filename such as:
- `chapter2_cnt_sem.png`

**Step 3: Insert it near `2.2` or `2.2.3`**

Place it where it supports morphology characterization rather than duplicating Chapter 1’s role.

**Step 4: Write a restrained caption**

Use wording like:
- `CNT 阵列的典型 SEM 形貌（引自文献[xx]）`
- or `……（引自文献[xx]，经裁剪）`

**Step 5: Verify**

Run: `xelatex --interaction=nonstopmode demo.tex`
Expected: figure renders and does not break chapter flow.

### Task 7: Normalize Chapter 2 wording and compile the full thesis

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Remove any textbook-like padding**

Edit only if needed to keep the prose:
- compact
- directly useful to Chapters 3 and 4
- consistent with the user’s Chapter 3 style

**Step 2: Check title and terminology consistency**

Keep terms aligned with the current thesis title:
- `知识增强`
- `关键形貌表征`
- `关系建模`

**Step 3: Run the full compile chain**

Run:
- `bibtex demo`
- `xelatex --interaction=nonstopmode demo.tex`
- `xelatex --interaction=nonstopmode demo.tex`

Expected:
- `demo.pdf` generated successfully
- only existing layout/template warnings remain

**Step 4: Final inspection**

Check:
- figure numbering
- citation numbering
- Chapter 2 flow and spacing
- no abrupt figure placement

**Step 5: Commit**

```bash
git add chapters/chapter2.tex reference/chapter1.bib figures/ demo.tex
git commit -m "docs: strengthen chapter 2 references and figures"
```
