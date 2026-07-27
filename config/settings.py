"""
config/settings.py

Pydantic BaseSettings for RepoMind.

Supports only Groq backend with API Key Rotation support.
Multiple keys can be provided separated by commas to avoid 429 Rate Limits.
"""

from __future__ import annotations

import threading
from functools import lru_cache

from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ── LLM — Groq (primary, free, fast) ─────────────────────────────────────
    # Can be a single key, or multiple keys separated by commas for rotation
    groq_api_key: str
    llm_model: str  = "llama-3.3-70b-versatile"

    # ── Plan limits ───────────────────────────────────────────────────────────
    max_plan_steps: int = 10

    # ── GitHub ────────────────────────────────────────────────────────────────
    github_token: str = ""
    github_username: str = ""

    # ── App ───────────────────────────────────────────────────────────────────
    app_env: str = "development"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        extra = "ignore"

    @property
    def parsed_groq_keys(self) -> list[str]:
        """Parse comma-separated keys into a list for rotation."""
        return [k.strip() for k in self.groq_api_key.split(",") if k.strip()]

    @model_validator(mode="after")
    def check_groq_key(self) -> "Settings":
        """Fail fast at startup if no Groq backend is configured."""
        if not self.parsed_groq_keys:
            raise ValueError("GROQ_API_KEY must be set in your environment variables. You can provide multiple keys separated by commas.")
        return self

    @property
    def active_llm_model(self) -> str:
        """Return the model name appropriate for the active backend."""
        return self.llm_model

    @property
    def is_production(self) -> bool:
        return self.app_env.lower() == "production"


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance (parsed once per process)."""
    return Settings()


# --- API Key Rotation Helper ---

class GroqKeyRotator:
    """
    Thread-safe key rotator for handling 429 Rate Limits.
    Cycles through all available keys provided in GROQ_API_KEY.
    """
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._index = 0
        self._keys: list[str] | None = None

    def get_key(self) -> str:
        """Get the next available Groq API Key."""
        with self._lock:
            if self._keys is None:
                # Load keys lazily on first request
                self._keys = get_settings().parsed_groq_keys
            
            key = self._keys[self._index]
            # Move to the next key for the next request (Round-robin)
            self._index = (self._index + 1) % len(self._keys)
            return key

# Global instance to be used by the agent/LLM initialisation layer
groq_key_rotator = GroqKeyRotator()