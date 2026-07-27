# 🧠 RepoMind

> **The Brain of HackingTheRepo** — A pure ML/AI engine that understands, plans, and rewrites code repositories on demand.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2%2B-green)](https://langchain.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111%2B-teal?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/your-org/repomind/ci.yml?label=CI)](/.github/workflows/)

---

## What is RepoMind?

**RepoMind** is the standalone ML core that powers [HackingTheRepo](https://github.com/your-org/hackingtherep) — a web-based platform where users describe code changes in plain English and an AI agent clones the target repository, implements the changes, and opens a Pull Request automatically.

RepoMind lives as a **separate, independently deployable ML service**. It is intentionally decoupled from the web frontend so it can be iterated on, tested, and scaled without touching the UI layer. Once mature, RepoMind is consumed by the HackingTheRepo backend over a simple REST API.

**RepoMind is responsible for:**

- Receiving a natural-language change instruction and a repository URL
- Cloning the repository and deeply understanding its structure
- Planning a step-by-step set of code edits using an LLM-powered agent
- Executing those edits via code generation tools
- Producing a diff and pushing a Pull Request back to GitHub

---

## Where RepoMind fits in the bigger picture

```text
┌─────────────────────────────────────────────────┐
│              HackingTheRepo (Web Platform)       │
│  User → describes change → selects repo → done  │
│                                                 │
│  Frontend (React/Next.js)                       │
│        │                                        │
│  Backend (Node / Django / etc.)                 │
│        │                                        │
│        │  POST /run   (REST API call)           │
│        ▼                                        │
│  ┌─────────────────────────────────┐            │
│  │        RepoMind  (this repo)    │            │
│  │  FastAPI · LangChain · GitHub   │            │
│  └─────────────────────────────────┘            │
│        │                                        │
│        ▼                                        │
│    GitHub PR created automatically              │
└─────────────────────────────────────────────────┘