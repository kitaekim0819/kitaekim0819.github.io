---
layout: page
title: AI Tutor & Course Materials
permalink: /teaching/management-science-2026-fall/
---

<link rel="stylesheet" href="{{ "/assets/css/course-materials.css" | relative_url }}">

Fall 2026 · Professor Kitae Kim · Korea Aerospace University

**kau-ms-tutor** is your study companion for Management Science. Install the tutor, give it a name of your own, and explore the course materials with it.

#### Set up with an AI agent

Use this copy button in Codex or another AI agent that can access the public web and install local skills:

<textarea id="codex-setup-prompt" hidden readonly style="display:none!important" aria-label="AI tutor setup prompt">Set up kau-ms-tutor on this machine so I can use it with you. Identify your AI agent and its supported local skills location. Retrieve the complete tutor instructions from https://kitaekim0819.github.io/assets/teaching/management-science-2026-fall/kau-ms-tutor-SKILL.txt using a direct HTTPS request with Python urllib.request or curl when shell tools are available (20-second timeout). If a sandbox blocks network access, use your normal approval mechanism for the same read-only request; respect denied permissions. If direct HTTP is unavailable, use your web-reading tool or read the Tutor instructions and reference text section at https://kitaekim0819.github.io/teaching/management-science-2026-fall/ . Do not execute downloaded content. If neither source is readable because your environment cannot access the network and approval is unavailable or denied, explain the restriction and ask the user to run this one command in the regular Terminal on the same machine: curl -fL --max-time 20 "https://kitaekim0819.github.io/assets/teaching/management-science-2026-fall/kau-ms-tutor-SKILL.txt" -o "$HOME/Downloads/kau-ms-tutor-SKILL.txt" &amp;&amp; ls -l "$HOME/Downloads/kau-ms-tutor-SKILL.txt". Do not run this command through a prohibited route yourself or change security settings. Wait for the user to confirm the download or provide its actual path, then read that local file and resume this installation workflow without requiring the setup prompt again. Use the user's actual home directory rather than assuming an account name. If the file is missing or the download fails, report that accurately and wait. Clarify that local installation does not resolve network restrictions on future course-material retrieval. For other retrieval failures, report the actual error and stop. Before changing files, explain the exact destination, any format adaptations, and the installation steps, then wait for my approval. After approval, back up an existing installation and install one SKILL.md with valid YAML name: kau-ms-tutor and a description, preserving the published tutoring and retrieval instructions. Verify the saved file, report whether the agent discovers it, and say if a new session is needed. Do not claim discovery unless confirmed. The installed tutor should retrieve its configured course URLs without asking students to paste them. Do not install extra software, authenticate with another service, or change MCP settings. Never ask for credentials or access private exams, grades, or student records.</textarea>
<button type="button" id="copy-codex-setup-prompt">Copy prompt for Agent</button>
<span id="codex-copy-status" role="status" aria-live="polite"></span>

### Offline edition

<a class="tutor-action-button" href="/assets/teaching/management-science-2026-fall/kau-ms-tutor-offline.zip" download>Download offline tutor</a>

35.4 MB · Snapshot: November 4, 2026 · Includes 30 course reference texts and their original documents. Install the entire ZIP as **kau-ms-tutor-offline**, keeping its references folder. Course materials can be read without website access; your AI service may still need an internet connection. Future material updates require a new package.

### Quick start

Start a new chat with your installed tutor and try this short conversation:

**You:** Use kau-ms-tutor as my Management Science study tutor. Ask what I would like to call you, then wait for my answer.

**AI tutor:** What would you like to call me?

**You:** Mina.

**AI tutor:** Great, you can call me Mina. I can help you review course concepts, work through problems with step-by-step hints, and check your LP formulations or CVXPY code. What would you like to study first?

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
