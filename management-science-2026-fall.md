---
layout: page
title: AI Tutor & Course Materials
permalink: /teaching/management-science-2026-fall/
---

<link rel="stylesheet" href="{{ "/assets/css/course-materials.css" | relative_url }}">

Fall 2026 · Professor Kitae Kim · Korea Aerospace University

**kau-ms-tutor** uses this webpage as its course reference source. Start a new AI chat with web browsing available, copy the prompt below, and ask about a lecture, quiz, or assignment by name.

### 1. Try AI Tutor

{% include course-tutor/start.html %}

Try the tutor in **one conversation**: click **Copy tutor prompt**, paste it into a new AI chat with browsing available, and ask a study question. The copied prompt includes direct HTML text links so the tutor can read course content without opening PDFs. This does not create an installed skill. Start a new chat with a fresh prompt if you want to try it again.

To check that it is working, ask: **“Tell me the materials version you read, then summarize Quiz 2’s Problem 1 without solving it.”** The tutor should read the page and identify what it actually accessed. If you like the tutor, install it below for repeated use.

### 2. Install AI Tutor

**[Download tutor skill (ZIP)](/assets/teaching/management-science-2026-fall/kau-ms-tutor.zip)** · <a href="/assets/teaching/management-science-2026-fall/kau-ms-tutor-SKILL.md" download="SKILL.md">Download SKILL.md</a>

The ZIP contains **SKILL.md and all 22 reference text files**. Upload the complete ZIP to install the tutor with its materials; SKILL.md alone contains the instructions but not the references.

1. In Claude, enable **Settings → Capabilities → Code execution and file creation** (or **Create and edit files**).
2. Open **Customize → Skills → Create skill → Upload a skill**, upload the ZIP, and enable **kau-ms-tutor**. In the updated interface, look under **Plugins**.
3. **Start a new chat** and say: **“Use kau-ms-tutor and help me with Quiz 2.”**

Your installed skill remains available for future chats, subject to your AI service’s settings and your own account’s usage limits. It includes a snapshot of the course text: import a new ZIP when materials are updated, then start a new chat. [Claude installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

Figures and mathematical notation may require the original documents below.

### Course materials

All course materials are organized by week below. Problem sets include quizzes, additional examples, and assignments, with released solutions alongside them. Select **View notebook** to read formatted cells, or **Download** to run a notebook in VS Code, Jupyter, or Google Colab.

<div class="course-materials-table" markdown="1">

| Week | Topic | Lecture materials | Problem set |
| --- | --- | --- | --- |
| Week 0 | Syllabus | <a href="/assets/teaching/management-science-2026-fall/syllabus-management-science-syllabus-2026-fall.pdf" target="_blank" rel="noopener noreferrer">Syllabus</a> | — |
| Week 1 | Course introduction and linear programming | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-1-week-1-course-introduction-fall-2026.pdf" target="_blank" rel="noopener noreferrer">Course Introduction</a><br><a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-1-chapter-1-introduction-english.pdf" target="_blank" rel="noopener noreferrer">Chapter 1 - Introduction</a><br><a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-1-chapter-2-linear-programming-english.pdf" target="_blank" rel="noopener noreferrer">Chapter 2 - Linear Programming</a> | Quiz 1: [Problems](/assets/teaching/management-science-2026-fall/quizzes-chapter-2-quiz-1.pdf) · [Solutions](/assets/teaching/management-science-2026-fall/quizzes-chapter-2-quiz-1-solutions.pdf)<br>Chapter 2 examples: [Problems](/assets/teaching/management-science-2026-fall/quizzes-chapter-2-additional-examples-for-chapter-2.pdf) · [Solutions](/assets/teaching/management-science-2026-fall/quizzes-chapter-2-additional-examples-for-chapter-2-solutions.pdf) |
| Week 2 | Chapter 3 - Analysis of LP Models (Part 1) | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-2-chapter-3-analysis-of-lp-models.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | Quiz 2: [Problems](/assets/teaching/management-science-2026-fall/quizzes-chapter-3-quiz-2.pdf) · [Solutions](/assets/teaching/management-science-2026-fall/quizzes-chapter-3-quiz-2-solutions.docx)<br>Chapter 3 examples: [Problems](/assets/teaching/management-science-2026-fall/quizzes-chapter-3-additional-examples-for-chapter-3.docx) · [Solutions](/assets/teaching/management-science-2026-fall/quizzes-chapter-3-additional-examples-for-chapter-3-solutions.docx) |
| Week 3 | Chapter 3 - Analysis of LP Models (Part 2) | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-3-chapter-3-analysis-of-lp-models-part-2.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | Assignment 1: [Problems](/assets/teaching/management-science-2026-fall/assignments-assignment-1.pdf) · [Solutions](/assets/teaching/management-science-2026-fall/assignments-assignment-1-solutions.pdf) |
| Week 4 | Chapter 3 - Analysis of LP Models (Part 3) | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-4-chapter-3-analysis-of-lp-models-part-3-slides.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | — |
| Week 5 | Chapter 4 - Post-Optimal and Sensitivity Analysis | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-5-chapter-4-post-optimal-and-sensitivity-analysis-slides.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | — |
| Week 6 | Chapter 5 - Business Applications of Linear Programming | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-6-chapter-5-business-applications-of-linear-programming-slides.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | — |
| Week 7 | Chapter 5 - Business Applications of Linear Programming (CVXPY Practice) | [Practice — View notebook](/assets/teaching/management-science-2026-fall/notebooks/week-7-chapter-5-practice.html) · <a href="/assets/teaching/management-science-2026-fall/week-7-chapter-5-practice.ipynb" download>Download</a><br>[Solutions — View notebook](/assets/teaching/management-science-2026-fall/notebooks/week-7-chapter-5-practice-solutions.html) · <a href="/assets/teaching/management-science-2026-fall/week-7-chapter-5-practice-solutions.ipynb" download>Download</a> | — |
| Week 8 | Midterm exam | Exam materials are not published. | — |
| Week 9 | Chapter 7 - Integer Programming | <a href="/assets/teaching/management-science-2026-fall/lecture-slides-week-9-chapter-7-integer-programming-slides.pdf" target="_blank" rel="noopener noreferrer">Slides</a> | — |

</div>

### Tutor instructions and reference text

The sections below contain the tutor’s instructions and the course text it reads. Expand a section to read it yourself. If your AI cannot read a section, you can copy its text into the chat.

{% include course-tutor/references.html %}

<script src="{{ '/assets/js/course-tutor.js' | relative_url }}" defer></script>
