# Chapter 2 CVD Restructure Design

**Goal:** Reorganize Chapter 2 so that it better supports the thesis title and the later chapter flow by inserting a concise CVD process section between knowledge enhancement and morphology characterization.

**Core judgment:** The current Chapter 2 already explains knowledge enhancement, morphology characterization, and relation modeling, but it lacks an explicit bridge for where the process parameters come from and why those parameters matter. Adding a dedicated CVD section closes that gap and makes the later parameter-morphology modeling narrative more natural.

## Approved Structure

Chapter 2 will be reorganized into four sections:

1. `2.1 领域知识组织与检索增强技术`
2. `2.2 CNT 阵列化学气相沉积工艺与生长影响因素`
3. `2.3 SEM 图像表征与关键形貌表征技术`
4. `2.4 工艺参数关系建模与结果解释技术`

The current `2.2` and `2.3` will be renumbered to `2.3` and `2.4` instead of keeping an unnumbered bridge paragraph. This is the cleaner thesis structure and gives the table of contents a more complete logic chain.

## Section Intent

### 2.1 Domain Knowledge and Retrieval Augmentation

This section keeps its current role. It provides the theoretical background for Chapter 3 and should remain focused on why general-purpose large models are insufficient for CNT array analysis tasks, why retrieval augmentation is needed, and why task-oriented evidence organization matters.

### 2.2 CVD Process and Growth Factors

This is the new bridge section. It should not become a long introduction to CVD equipment or a textbook-style synthesis review. Its purpose is narrower:

- explain the basic logic of CNT array growth under CVD conditions
- introduce the main process parameters that later appear in Chapter 4
- explain why temperature, catalyst, gas composition, flow, and growth time affect morphology
- build a direct link from process conditions to array height, alignment, coverage, diameter, and local bending/waviness

The writing should stay close to the thesis task: parameter definition, physical meaning, and morphology relevance.

### 2.3 Morphology Characterization

This remains the theory basis for Chapter 4 front-half. Its wording should be lightly updated so that it now explicitly follows the new CVD section. The entry point becomes: after clarifying the process side, the next question is how to obtain stable morphology descriptors from SEM images.

### 2.4 Relation Modeling and Interpretation

This remains the theory basis for Chapter 4 back-half. Its wording should also be lightly updated so that it follows naturally from the new CVD section and the morphology characterization section: once process parameters and morphology indicators are both defined, their relationships can be modeled and interpreted.

## Citation and Figure Strategy

- Reuse existing chapter references wherever possible.
- Add only a small number of CVD growth references directly tied to CNT arrays and morphology influence.
- Keep the existing RAG figure and morphology figure.
- Do not add a new figure to the CVD section unless an immediately usable classic original figure is already available locally and directly improves understanding. The section should work even without a figure.

## Writing Style Constraints

- Keep the style close to Chapter 3: direct, task-oriented, and not over-polished.
- Do not write the CVD section as a broad review of all CNT synthesis routes.
- Do not overstate "prediction" or "closed loop" ideas in Chapter 2.
- Keep the section tightly aligned with the thesis title: `知识增强`, `关键形貌表征`, `关系建模`.

## Expected Outcome

After restructuring, Chapter 2 should read as one continuous preparation chain for later chapters:

`知识增强基础 -> 参数来源与工艺背景 -> 关键形貌表征 -> 参数-形貌关系建模与解释`

This will make Chapter 4 feel less abrupt and improve the consistency between the thesis title, the introduction, and the technical chapters.
