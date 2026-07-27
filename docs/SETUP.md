# RepoMind — Setup, Testing & Upgrade Guide

> Complete local development guide for Windows (MSYS2/MinGW), macOS, and Linux.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Clone the Repository](#2-clone-the-repository)
3. [Create a Virtual Environment](#3-create-a-virtual-environment)
4. [Install Dependencies](#4-install-dependencies)
5. [Configure Environment Variables](#5-configure-environment-variables)
6. [Run the API Server](#6-run-the-api-server)
7. [Running Tests](#7-running-tests)
8. [Upgrading Dependencies](#8-upgrading-dependencies)
9. [Known Issues & Fixes](#9-known-issues--fixes)
10. [Project Structure Reference](#10-project-structure-reference)

---

## 1. Prerequisites

| Tool          | Minimum Version | Check                                                             |
| ------------- | --------------- | ----------------------------------------------------------------- |
| Python        | 3.11+           | `python --version`                                                |
| pip           | 23+             | `pip --version`                                                   |
| Git           | Any recent      | `git --version`                                                   |
| Groq API Key  | —               | [console.groq.com](https://console.groq.com)                      |
| GitHub PAT    | —               | [github.com/settings/tokens](https://github.com/settings/tokens) |

> **Windows / MSYS2 users:** You are running Python inside an MSYS2-managed environment, which blocks system-wide `pip install`. You **must** use a virtual environment — see Section 3 for the exact commands.

---

## 2. Clone the Repository

```bash
git clone [https://github.com/your-org/repomind.git](https://github.com/your-org/repomind.git)
cd repomind