# Introduction Technical Route Figure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a concise technical route figure to Chapter 1 and strengthen the explanation for why the selected key morphology indicators are used.

**Architecture:** Extend the thesis preamble with lightweight TikZ support, embed a single thesis-style route figure directly in `chapter1.tex`, and refine one paragraph in Section 1.3 so the figure and text reinforce the same research mainline.

**Tech Stack:** LaTeX, TikZ, XeLaTeX

---

### Task 1: Enable TikZ support

**Files:**
- Modify: `D:\Apaper\paperformat\demo.tex`

**Step 1: Add the package**

Add `\usepackage{tikz}` and the minimal libraries needed for node positioning and arrows.

**Step 2: Keep scope minimal**

Only add the libraries needed by the route figure, avoiding unrelated drawing packages.

### Task 2: Add the Chapter 1 technical route figure

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter1.tex`

**Step 1: Insert a concise paragraph transition**

Place the figure immediately after the technical route description so the text introduces the diagram first.

**Step 2: Insert one thesis-style figure**

Build a compact route figure showing:
- multi-source data
- knowledge organization and evidence-chain construction
- key morphology quantification
- process-parameter-driven prediction
- knowledge-enhanced interpretation
- parameter recommendation and platform validation

**Step 3: Add chapter mapping cues**

Use brief labels such as Chapter 3, Chapter 4, and Chapter 5 without overloading the figure.

### Task 3: Strengthen the indicator-selection rationale

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter1.tex`

**Step 1: Refine the Section 1.3 research-content paragraph**

Add one sentence explaining that curvature, alignment, diameter distribution, and coverage density together cover both global order and local geometric disturbance, with curvature used as a key focus because it better reflects local bending and instability.

### Task 4: Verify the thesis build

**Files:**
- Verify: `D:\Apaper\paperformat\demo.tex`

**Step 1: Run XeLaTeX and BibTeX sequence**

Run the full compilation chain and confirm the PDF is generated successfully.

**Step 2: Check for regressions**

Confirm there are no new fatal errors and that any remaining warnings are pre-existing template/layout warnings.
