# Contributing to RepoMind

Thank you for taking the time to contribute. RepoMind is the AI engine that powers HackingTheRepo — it clones real repositories, generates code with an LLM, and opens pull requests autonomously. That makes quality and correctness especially important.

This document covers everything you need to go from zero to a merged pull request.

---

## Table of Contents

1. [Before You Start](#1-before-you-start)
2. [Development Setup](#2-development-setup)
3. [Project Structure at a Glance](#3-project-structure-at-a-glance)
4. [Making Changes](#4-making-changes)
5. [Code Style](#5-code-style)
6. [Testing](#6-testing)
7. [Commit Messages](#7-commit-messages)
8. [Opening a Pull Request](#8-opening-a-pull-request)
9. [Adding a New Tool](#9-adding-a-new-tool)
10. [Working with Prompts](#10-working-with-prompts)
11. [Security Guidelines](#11-security-guidelines)

---

## 1. Before You Start

- **Search existing issues and PRs** before opening a new one — your idea may already be in progress.
- **Open an issue first** for any non-trivial change. This saves everyone time if the approach isn't right.
- **Security issues** must be reported privately — see [SECURITY.md](SECURITY.md), not as a public issue.

---

## 2. Development Setup

### Prerequisites

| Tool | Minimum Version |
|------|----------------|
| Python | 3.11+ |
| Git | Any recent |
| A GitHub PAT | `repo` scope |
| A Groq API key | — |

### Clone and install

```bash
git clone [https://github.com/your-org/repomind.git](https://github.com/your-org/repomind.git)
cd repomind

python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

pip install -e ".[dev]"