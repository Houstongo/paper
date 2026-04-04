# Chapter 2 CVD Restructure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Insert a concise CVD process section into Chapter 2, renumber the existing sections, and align the chapter flow with the thesis title and later modeling chapters.

**Architecture:** Preserve the current Chapter 2 material for knowledge enhancement, morphology characterization, and relation modeling, then insert a new CVD bridge section between knowledge enhancement and morphology characterization. The new section will define process context and morphology-relevant parameters without expanding into a textbook-style review.

**Tech Stack:** LaTeX, BibTeX, XeLaTeX, thesis template, `chapters/chapter2.tex`, existing bibliography files

---

### Task 1: Reorder Chapter 2 top-level sections

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Update the section order**

Move from the current three-part structure:
- `2.1 领域知识组织与检索增强技术`
- `2.2 SEM 图像表征与关键形貌量化技术`
- `2.3 工艺参数关联建模与结果解释技术`

to the new four-part structure:
- `2.1 领域知识组织与检索增强技术`
- `2.2 CNT 阵列化学气相沉积工艺与生长影响因素`
- `2.3 SEM 图像表征与关键形貌表征技术`
- `2.4 工艺参数关系建模与结果解释技术`

**Step 2: Adjust Chinese and English section titles**

Keep terminology aligned with the thesis title:
- use `关键形貌表征`
- use `关系建模`

**Step 3: Update the chapter summary**

Revise the Chapter 2 summary so it reflects the new four-part chain.

### Task 2: Draft the new CVD bridge section

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Add the section opening paragraph**

Write a direct overview paragraph stating that this section provides the process background for later morphology characterization and relation modeling.

**Step 2: Add subsection `2.2.1` for CVD basic process**

Cover:
- catalyst-assisted growth logic
- carbon source decomposition and precipitation/growth
- why array growth depends on process stability

**Step 3: Add subsection `2.2.2` for key process parameters**

Cover:
- temperature
- catalyst and substrate conditions
- carbon source / carrier gas / auxiliary gas
- flow and growth time

Focus on why these parameters matter later in Chapter 4.

**Step 4: Add subsection `2.2.3` for morphology-relevant growth effects**

Cover the connection from process parameters to:
- height
- alignment
- coverage
- diameter
- local bending / waviness

End by bridging into SEM-based morphology characterization.

### Task 3: Update downstream section transitions

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Revise the opening of the new `2.3`**

Make `SEM 图像表征与关键形貌表征技术` explicitly follow the CVD process section.

**Step 2: Revise the opening of the new `2.4`**

Make `工艺参数关系建模与结果解释技术` explicitly follow the process and morphology sections.

**Step 3: Keep existing figures**

Retain:
- `fig:ch2_rag_workflow`
- `fig:ch2_cnt_morph`

Do not add more figures unless a directly usable local original figure clearly improves the new CVD section.

### Task 4: Compile and verify numbering stability

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter2.tex`

**Step 1: Run full compile chain**

Run:
- `bibtex demo`
- `xelatex --interaction=nonstopmode demo.tex`
- `xelatex --interaction=nonstopmode demo.tex`

Expected:
- section numbering updates correctly
- TOC updates correctly
- `demo.pdf` generates successfully

**Step 2: Check for regression**

Confirm:
- Chapter 2 figures still render
- no new undefined citations appear
- only existing non-fatal layout warnings remain
