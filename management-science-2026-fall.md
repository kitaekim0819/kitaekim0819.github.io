---
layout: page
title: AI Tutor & Course Materials
permalink: /teaching/management-science-2026-fall/
---

<link rel="stylesheet" href="{{ "/assets/css/course-materials.css" | relative_url }}">

Fall 2026 · Professor Kitae Kim · Korea Aerospace University

**kau-ms-tutor** is your study companion for Management Science. Install the tutor, give it a name of your own, and explore the course materials with it.

### Install AI Tutor

#### Set up with an AI agent

Use this copy button in Codex or another AI agent that can access the public web and install local skills:

<textarea id="codex-setup-prompt" hidden readonly aria-label="AI tutor setup prompt">Set up the kau-ms-tutor skill from https://kitaekim0819.github.io/assets/teaching/management-science-2026-fall/kau-ms-tutor.zip for this Codex account. First inspect the package and official Codex skill installation instructions. Explain the installation steps before making changes. Do not install software, run downloaded scripts, change MCP settings, or authenticate with any service unless you show me the exact commands and I approve them. Never ask me to provide or paste an API key, password, or access token. If installation is supported and I approve, install the skill in my user skills folder, then verify it is available in a new Codex session. The skill requires public web access to the course website; tell me if that access is unavailable. Do not access private exams, grades, or student records.</textarea>
<button type="button" id="copy-codex-setup-prompt">Copy prompt for Agent</button>
<span id="codex-copy-status" role="status" aria-live="polite"></span>

This installs the tutor instructions as a local skill. It does not install the third-party `@hasna/skills` CLI or register that service’s MCP server.

<details>
<summary>Download AI Tutor</summary>

**[Download AI Tutor](/assets/teaching/management-science-2026-fall/kau-ms-tutor.zip)**

Download the tutor package, then upload it to Claude using the steps below. The package contains tutor instructions. **Web browsing is required:** the tutor reads the current course materials directly from this website.

1. In Claude, enable **Settings → Capabilities → Code execution and file creation** (or **Create and edit files**).
2. Open **Customize → Skills → Create skill → Upload a skill**, upload the ZIP, and enable **kau-ms-tutor**. In the updated interface, look under **Plugins**.
3. **Start a new chat** and send the two prompts below, one at a time.

Your installed skill remains available for future chats, subject to your AI service’s settings and your own account’s usage limits. On first use in each chat, it checks the website and reuses materials it has read during that conversation for faster replies. This is not permanent storage. Ask it to check the website again for updates. Course material changes do not require reinstalling the skill; instruction changes may require a new download. [Claude installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

#### First prompt — Name your tutor

Copy this prompt into your new chat. Choose a name when the tutor asks you.

> Use kau-ms-tutor as my Management Science study tutor. Let me give you a name: ask what I would like to call you, then wait for my answer. Once I choose, use that name in this conversation and briefly explain how you can help me learn.

The name is your personal nickname for the tutor. In a new chat, remind it of your chosen name if needed.

#### Second prompt — Explore your course materials

After naming your tutor, send this prompt to check which materials it can actually read.

> Use kau-ms-tutor and open the current HTML reference index at https://kitaekim0819.github.io/assets/teaching/management-science-2026-fall/read/index.html. Report the materials date and revision you actually read, then inspect the linked HTML course texts. List the available materials by week or topic, including the syllabus, lecture slides, quizzes and examples, assignments, CVXPY practice, and released solutions. Read each accessible reference and give a brief summary of what it covers without solving any problems. Distinguish files you actually read from titles you could only list, and clearly identify anything inaccessible. Reuse the materials you read within this conversation. If web access is unavailable, explain that this tutor requires web access and identify what could not be read. Do not guess missing contents. Finish by asking which topic I would like to study first.

</details>

Figures and mathematical notation may require the original documents below.

### Course materials

All course materials are organized by week below. Problem sets include quizzes, additional examples, and assignments, with released solutions alongside them. Select **View notebook** to read formatted cells, or **Download** to run a notebook in VS Code, Jupyter, or Google Colab.

<div class="course-materials-table" markdown="1">

| Week | Topic | Lecture materials | Problem set |
| --- | --- | --- | --- |
| Week 0 | Syllabus | <a href="/assets/teaching/management-science-2026-fall/syllabus-management-science-syllabus-2026-fall.pdf" target="_blank" rel="noopener noreferrer">Syllabus</a> | — |
| Week 1 | Course introduction and linear programming | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-1-week-1-course-introduction-fall-2026.pdf" target="_blank" rel="noopener noreferrer">Course Introduction</a><br><a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-1-chapter-1-introduction-english.pdf" target="_blank" rel="noopener noreferrer">Chapter 1 - Introduction</a><br><a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-1-chapter-2-linear-programming-english.pdf" target="_blank" rel="noopener noreferrer">Chapter 2 - Linear Programming</a> | Quiz 1: [Problems](/assets/teaching/management-science-2026-fall/quizzes-chapter-2-quiz-1.pdf) · [Solutions](/assets/teaching/management-science-2026-fall/quizzes-chapter-2-quiz-1-solutions.pdf)<br>Chapter 2 examples: [Problems](/assets/teaching/management-science-2026-fall/quizzes-chapter-2-additional-examples-for-chapter-2.pdf) · [Solutions](/assets/teaching/management-science-2026-fall/quizzes-chapter-2-additional-examples-for-chapter-2-solutions.pdf) |
| Week 2 | Chapter 3 - Analysis of LP Models (Part 1) | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-2-chapter-3-analysis-of-lp-models.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | — |
| Week 3 | Chapter 3 - Analysis of LP Models (Part 2) | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-3-chapter-3-analysis-of-lp-models-part-2.pdf" target="_blank" rel="noopener noreferrer">Slides</a> <br><a href="/assets/teaching/management-science-2026-fall/week-3-colab-basics.pdf" target="_blank" rel="noopener noreferrer">Colab Basics</a> | Quiz 2: [Problems](/assets/teaching/management-science-2026-fall/quizzes-chapter-3-quiz-2.pdf) · [Solutions](/assets/teaching/management-science-2026-fall/quizzes-chapter-3-quiz-2-solutions.docx)<br>Chapter 3 examples: [Problems](/assets/teaching/management-science-2026-fall/quizzes-chapter-3-additional-examples-for-chapter-3.docx) · [Solutions](/assets/teaching/management-science-2026-fall/quizzes-chapter-3-additional-examples-for-chapter-3-solutions.docx) |
| Week 4 | Chapter 3 - Analysis of LP Models (Part 3) | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-4-chapter-3-analysis-of-lp-models-part-3-slides.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | Quiz 3: <a href="/assets/teaching/management-science-2026-fall/week-4-quiz-3-python-codes-for-lp.pdf" target="_blank" rel="noopener noreferrer">Worksheet</a> · <a href="/assets/teaching/management-science-2026-fall/notebooks/week-4-quiz-3-python-codes-for-lp-solutions.html" target="_blank" rel="noopener noreferrer">Solutions</a> · <a href="/assets/teaching/management-science-2026-fall/week-4-quiz-3-python-codes-for-lp-solutions.ipynb" download>Download</a><br><a href="/assets/teaching/management-science-2026-fall/notebooks/week-4-example-3-1.html" target="_blank" rel="noopener noreferrer">Example 3-1</a> · <a href="/assets/teaching/management-science-2026-fall/week-4-example-3-1.ipynb" download>Download</a><br><a href="/assets/teaching/management-science-2026-fall/notebooks/week-4-example-3-2.html" target="_blank" rel="noopener noreferrer">Example 3-2</a> · <a href="/assets/teaching/management-science-2026-fall/week-4-example-3-2.ipynb" download>Download</a> |
| Week 5 | Chapter 4 - Post-Optimal and Sensitivity Analysis | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-5-chapter-4-post-optimal-and-sensitivity-analysis-slides.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | Assignment 1: [Problems](/assets/teaching/management-science-2026-fall/assignments-assignment-1.pdf) · [Solutions](/assets/teaching/management-science-2026-fall/assignments-assignment-1-solutions.pdf)<br>LP examples: <a href="/assets/teaching/management-science-2026-fall/notebooks/week-5-lp-examples.html" target="_blank" rel="noopener noreferrer">Practice</a> · <a href="/assets/teaching/management-science-2026-fall/week-5-lp-examples.ipynb" download>Download</a><br><a href="/assets/teaching/management-science-2026-fall/notebooks/week-5-lp-examples-solutions.html" target="_blank" rel="noopener noreferrer">Solutions</a> · <a href="/assets/teaching/management-science-2026-fall/week-5-lp-examples-solutions.ipynb" download>Download</a> |
| Week 6 | Chapter 5 - Business Applications of Linear Programming | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-6-chapter-5-business-applications-of-linear-programming-slides.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | — |
| Week 7 | Chapter 5 - Business Applications of Linear Programming (CVXPY Practice) | [Practice — View notebook](/assets/teaching/management-science-2026-fall/notebooks/week-7-chapter-5-practice.html) · <a href="/assets/teaching/management-science-2026-fall/week-7-chapter-5-practice.ipynb" download>Download</a><br>[Solutions — View notebook](/assets/teaching/management-science-2026-fall/notebooks/week-7-chapter-5-practice-solutions.html) · <a href="/assets/teaching/management-science-2026-fall/week-7-chapter-5-practice-solutions.ipynb" download>Download</a> | — |
| Week 8 | Midterm exam | Exam materials are not published. | — |
| Week 9 | Chapter 7 - Integer Programming | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-9-chapter-7-integer-programming-slides.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | Quiz 4: <a href="/assets/teaching/management-science-2026-fall/week-9-quiz-4-integer-programming.pdf" target="_blank" rel="noopener noreferrer">Integer programming problems</a> |

</div>

<!-- Reference text retained in HTML for tools that can read hidden content. -->
<div id="tutor-reference-library" hidden>
{% include course-tutor/references.html %}
</div>

<script src="{{ '/assets/js/course-tutor.js' | relative_url }}" defer></script>
