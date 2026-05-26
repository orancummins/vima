"""Pydantic data models for configuration and runtime artifacts."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, field_validator


Environment = Literal["sandbox", "production"]


class ApiSpec(BaseModel):
    """An API to be attached to a project."""

    name: str
    version: str = "v1"

    @field_validator("name")
    @classmethod
    def _lowercase(cls, v: str) -> str:
        return v.strip().lower()


class ProjectSpec(BaseModel):
    name: str
    description: str = ""
    apis: list[str | ApiSpec] = Field(default_factory=list)

    def normalised_apis(self) -> list[ApiSpec]:
        out: list[ApiSpec] = []
        for a in self.apis:
            out.append(ApiSpec(name=a) if isinstance(a, str) else a)
        return out


class AppConfig(BaseModel):
    environment: Environment
    organization: str = "mastercard"
    login_url: str = "https://developer.mastercard.com/account/log-in"
    dashboard_url_pattern: str = "**/dashboard**"
    projects: list[ProjectSpec] = Field(default_factory=list)

    @field_validator("projects")
    @classmethod
    def _unique_project_names(cls, v: list[ProjectSpec]) -> list[ProjectSpec]:
        names = [p.name.lower() for p in v]
        dupes = {n for n in names if names.count(n) > 1}
        if dupes:
            raise ValueError(f"Duplicate project names: {sorted(dupes)}")
        return v


class DownloadedArtifact(BaseModel):
    """A single downloaded key or certificate file."""

    alias: str
    filename: str
    path: str
    sha256: str
    kind: Literal["p12", "pem", "crt", "key", "other"]
    project: str
    api: str
