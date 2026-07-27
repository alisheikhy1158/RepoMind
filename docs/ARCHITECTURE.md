# RepoMind — Architecture

This document describes how RepoMind is structured, how data flows through the system, and the design decisions behind each layer. Read this before making changes to the agent, tools, or API.

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Layer Breakdown](#2-layer-breakdown)
3. [Request Lifecycle](#3-request-lifecycle)
4. [Agent Internals](#4-agent-internals)
5. [Tool System](#5-tool-system)
6. [API Layer](#6-api-layer)
7. [Job Management](#7-job-management)
8. [Memory System](#8-memory-system)
9. [Configuration](#9-configuration)
10. [Data Models](#10-data-models)
11. [Known Limitations & Future Work](#11-known-limitations--future-work)

---

## 1. System Overview

RepoMind is a stateless FastAPI service that wraps a LangChain-based AI agent. A caller sends a repository URL and a plain-English instruction. The agent plans a sequence of code edits, executes them using tools, and opens a pull request with the result.

```text
External Caller (HackingTheRepo platform)
        │
        │  POST /run  { repo_url, instruction, branch_name, pr_title }
        ▼
┌─────────────────────────────────────────────┐
│               FastAPI  (api/)               │
│  routes.py → job_manager → background task  │
└─────────────────┬───────────────────────────┘
                  │  async background task
                  ▼
┌─────────────────────────────────────────────┐
│              Agent Chain  (agent/)          │
│                                             │
│  MemoryManager ──► TaskPlanner ──► StepExecutor
│       │                                 │   │
│       │ conversation history            │   │
│       └─────────────────────────────────┘   │
│                                             │
│  (LangChain + Groq LLM)                     │
└──────────────────┬──────────────────────────┘
                   │  tool calls
        ┌──────────┼──────────────┐
        ▼          ▼              ▼
 github_tool  code_parser   pr_tool
 diff_gen     test_executor
        │
        │  clone / commit / push / PR
        ▼
 GitHub API (PyGitHub + GitPython)