# Chapter 3 Revision Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reorganize Chapter 3 into a single, defensible method chapter centered on "multi-source knowledge -> MSFU -> relation constraints -> TCCER -> evidence chains -> evaluation".

**Architecture:** Keep Chapter 3 focused on one lightweight knowledge-enhanced retrieval framework instead of expanding into a graph-learning or heavy algorithm chapter. Use 3.1 to define the problem and chapter scope, 3.2 to define knowledge representation, 3.3 to define TCCER as the unified retrieval algorithm, and 3.4 to define evaluation design in a thesis-style tone rather than a proposal-style tone.

**Tech Stack:** LaTeX, XeLaTeX thesis template, `chapters/chapter3.tex`

---

### Task 1: Lock the chapter tone in 3.1

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:5`

**Step 1: Rewrite the opening paragraph around chapter positioning**

Delete or weaken:
- Excessive "innovation announcement" tone
- Early algorithmic hype
- Any wording that makes Chapter 3 read like a project pitch

Add one positioning sentence near the end of 3.1:

`本章不追求构建复杂的图学习模型，而是以最小语义事实单元为基础，通过轻量级领域关系结构和任务约束检索机制，实现面向科研分析任务的链式证据组织与调用。`

**Step 2: Align the chapter roadmap with the real structure**

Replace the current "三个方面" expression with a roadmap that matches the final structure:
- 3.1 问题与本章工作
- 3.2 知识如何表示
- 3.3 知识如何检索并组织成证据链
- 3.4 如何验证方法有效

**Step 3: Remove method detail leakage from 3.1**

Cut or compress:
- Detailed explanation of TCCER internals
- Repeated value statements that belong in 3.3 or 3.4

**Step 4: Verify the section reads as a chapter introduction**

Check that 3.1 only does four things:
- Why knowledge enhancement is needed
- Why text-chunk retrieval is insufficient
- What this chapter does
- How the rest of the chapter is organized


### Task 2: Tighten 3.2.1 and 3.2.2 without adding new concepts

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:31`
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:57`

**Step 1: Add an explicit intermediate-output sentence to 3.2.1**

Add one sentence after the normalization definition:

`规范化处理的目标不是保留所有原始格式细节，而是将不同来源知识统一映射为后续切分、抽取与索引所需的中间表示。`

**Step 2: Strengthen the contrast sentence in 3.2.2**

Add one sentence after the segmentation motivation:

`与仅以长度为依据的滑动窗口切分不同，本文优先依据科研事实边界进行分段，以尽量保留“条件—现象—解释”的局部表达完整性。`

**Step 3: Fix the segmentation notation ambiguity**

Clarify whether the final indexed segment is `c_{k,j}` or `c'_{k,j}`.

Preferred fix:
- Introduce the overlap-enhanced segment once
- Explicitly state that the final segment used later is denoted uniformly as `c_{k,j}`

**Step 4: Remove repeated value-summary sentences**

Compress paragraph endings that only repeat:
- "为后续提供基础"
- "支撑后续任务"
- "提高可解释性/可追溯性"


### Task 3: Strengthen 3.2.3 as the chapter boundary section

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:79`

**Step 1: Add the vectorization boundary sentence**

Insert this sentence after the MSFU definition and before retrieval discussion:

`本文仅对最小语义事实单元的文本内容及扩展语义字段进行向量化表示，用于支持语义召回；其关系断言及约束信息保留为符号化表示，用于后续关系约束扩展与证据链组织。`

**Step 2: Make incomplete-unit handling explicit**

Retain and sharpen the current idea:

`并非所有候选片段都强制转换为完整关系单元；对于无法形成明确关系断言的片段，仅保留其文本索引和元数据，用于补充召回而不参与关系路径扩展。`

**Step 3: Add one concrete micro-example**

Add a short example showing:
- Original sentence
- Extracted source entity / relation / target entity
- Condition scope
- Resulting MSFU fields

Goal:
- Make the method look implemented, not only defined


### Task 4: Reframe 3.2.4 as symbolic support, not graph learning

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:129`

**Step 1: Keep the object types, relation types, and constraints**

Preserve:
- Four core object categories
- Five major relation types
- Four kinds of constraints

**Step 2: Reduce graph-learning flavor**

Replace or weaken wording that makes this section sound like:
- Complex graph construction
- Rich graph reasoning
- A graph representation learning setup

**Step 3: Add the explicit non-graph-learning sentence at the end**

Add:

`需要说明的是，本文构建该领域关系结构的目的并非进行复杂图表示学习，而是为后续任务模板约束、条件一致性筛选和链式证据组织提供符号化支撑。`


### Task 5: Rewrite 3.3.1 as the TCCER entry point

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:196`

**Step 1: Keep the three task types, but shorten the prose**

Retain:
- 工艺分析任务
- 形貌解释任务
- 预测解释任务

Compress:
- Overlong examples
- Repeated statements about "链路完整性" and "结构一致性"

**Step 2: Define structured query explicitly**

Keep:
- `z(q)=(E_q,C_q,D_q,Y_q,t_q)` or equivalent

If `t_q` is not used later, either:
- Add it consistently across 3.3, or
- Remove it from the definition and keep `t` as algorithm input

**Step 3: Define TCCER input and output in one place**

Ensure 3.3.1 clearly states:
- Input: `q, t, U, G`
- Output: `P^{*}(q,t)`

**Step 4: End 3.3.1 with the algorithm overview sentence**

Use a sentence close to:

`据此，本文提出面向科研任务的约束链式证据检索算法（TCCER），其总体流程包括查询解析、混合召回、种子边构建、局部关系约束扩展以及路径评分与证据链输出五个阶段。`

Replace high-frequency "局部关系子图" wording here with:
- `局部关系约束扩展`
- `局部路径扩展`


### Task 6: Rewrite 3.3.2 as TCCER Step 1 and Step 2

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:256`

**Step 1: Keep the stage framing**

The opening sentence should say this section corresponds to:
- Query parsing
- Hybrid retrieval

It should not sound like an independent retrieval module chapter.

**Step 2: State the retrieval target boundary explicitly**

Add one sentence near the retrieval-score definition:

`混合召回阶段的目标不是直接生成最终解释结果，而是从事实单元库中获得与任务约束相一致的高质量种子候选。`

**Step 3: Add the "vectorize facts, not graph" sentence if it is not already placed in 3.2.3**

Only one location should carry this boundary clearly. Preferred priority:
- First choice: 3.2.3
- Second choice: 3.3.2

**Step 4: Remove overexplaining after formulas**

After each score formula, keep:
- Variable meaning
- Why this score matters in the current stage

Delete:
- Repeated global value claims
- Early promises that belong to 3.4


### Task 7: Rewrite 3.3.3 around constrained path expansion

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:296`

**Step 1: Keep the essentials**

Preserve:
- Seed edges
- Relation transfer matrix
- Max hop number
- Condition-consistency threshold
- Direction-consistency threshold

**Step 2: Change the narrative center**

Shift the emphasis from:
- Building local subgraphs

To:
- Expanding candidate paths under task-allowed relation patterns

Use wording like:
- `沿任务允许的关系模式扩展候选路径`
- `在关系约束下进行局部路径扩展`

**Step 3: Reduce "局部关系子图" density**

Keep the concept if needed for notation, but do not make it the dominant reader impression.

**Step 4: Shorten the subgraph-scoring explanation**

Retain only what is necessary to support transition into path scoring in 3.3.4.


### Task 8: Tighten 3.3.4 as the TCCER closing stage

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:363`

**Step 1: Keep all six scoring factors**

Retain:
- Path relevance
- Template match
- Condition consistency
- Direction consistency
- Evidence confidence
- Redundancy penalty

**Step 2: Add one sentence that lowers the graph-algorithm tone**

Insert a sentence close to:

`路径评分阶段的目标不是寻找全局最长路径，而是选择在任务匹配、条件一致性和证据可信度之间达到较好平衡的局部主链式证据。`

**Step 3: Emphasize why the output is a set of complementary chains**

Use one sentence to explain:
- Why final output is not a pile of similar text fragments
- Why redundancy suppression matters

**Step 4: Remove repeated "可解释、可追溯" praise**

Keep one concise closing sentence only.


### Task 9: Add a new 3.3.5 retrieval walkthrough example

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex` after current 3.3.4 and before 3.4

**Step 1: Add a short example query**

Recommended example structure:
- Query asks why a morphology indicator changes under a process condition

Example style:
- `在较高生长温度条件下，覆盖密度下降的可能机理是什么？`

**Step 2: Walk through the whole chain in 5 compact steps**

Show:
- Parsed query constraints
- Retrieved seed MSFUs
- Allowed relation-pattern expansion
- Retained main path
- Final evidence-chain output

**Step 3: Keep the example textual, not implementation-heavy**

Do not add new formulas here.
Do not introduce new symbols unless necessary.

Goal:
- Maximize credibility
- Let the reader see the full pipeline once


### Task 10: Rewrite 3.4 into evaluation-design prose

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex:427`

**Step 1: Change the section tone from proposal to evaluation design**

Replace or minimize:
- `拟`
- `将`
- `计划`

Use thesis-style wording such as:
- `本节围绕……构建评测框架`
- `评测从……三个层面展开`
- `评测指标包括……`

**Step 2: Keep 3.4 focused on validation logic**

3.4 should only answer:
- What is evaluated
- Compared with what
- Measured by which metrics
- Why those metrics can validate the method

**Step 3: Avoid fake completed-results language**

If actual results are not yet available:
- Do not invent outcome statements
- Do not call it "结果分析" in a way that implies finished numbers

If needed, rename the section to:
- `实验设计与评测方案`
- or another title consistent with current progress


### Task 11: Compress repetition across the whole chapter

**Files:**
- Modify: `D:\Apaper\paperformat\chapters\chapter3.tex`

**Step 1: Remove repeated background restarts**

Check every subsection opening and cut repeated restatements of:
- Why CNT array research is complex
- Why text chunks are insufficient
- Why later tasks need support

**Step 2: Remove repetitive value statements after formulas**

Delete repeated statements about:
- `可解释`
- `可追溯`
- `为后续提供基础`
- `支撑后续任务`

Keep these claims only where they are proved or operationalized.

**Step 3: Keep each subsection on one job**

Use this mapping as the final pass:
- 3.1: problem + chapter work
- 3.2: knowledge representation
- 3.3: retrieval and evidence-chain organization
- 3.4: validation design


### Task 12: Verify the revised chapter end-to-end

**Files:**
- Verify: `D:\Apaper\paperformat\chapters\chapter3.tex`
- Verify: `D:\Apaper\paperformat\demo.tex`

**Step 1: Run a compile check**

Run one of:
- `xmu-thesis-run.cmd`
- or the current XeLaTeX build command used in this repo

Expected:
- Chapter 3 compiles without new LaTeX errors
- New subsection numbering is correct

**Step 2: Read Chapter 3 once in PDF order**

Check:
- 3.1 -> 3.2 -> 3.3 -> 3.4 transitions are smooth
- TCCER is the only algorithm line in 3.3
- 3.4 reads as validation design, not a project proposal

**Step 3: Final editorial checklist**

Confirm:
- The chapter does not feel like a design draft
- The graph flavor is light, not dominant
- "Only vectorize facts, not the whole graph" is clearly stated once
- There is one end-to-end retrieval example
- Repetition is visibly reduced
