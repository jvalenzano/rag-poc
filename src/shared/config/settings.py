"""
Application Configuration
Central configuration management for the RAG system
"""

import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    # GCP Configuration
    GCP_PROJECT_ID: str
    GCP_LOCATION: str = "us-east4"
    
    # Vertex AI Settings
    VERTEX_AI_MODEL: str = "text-bison@latest"
    EMBEDDING_MODEL: str = "textembedding-gecko@latest"
    
    # Storage Configuration
    BUCKET_NAME: str
    
    # Application Settings
    LOG_LEVEL: str = "INFO"
    ENVIRONMENT: str = "development"
    API_VERSION: str = "v1"
    
    # Vector Search Settings
    VECTOR_DIMENSION: int = 768
    SIMILARITY_THRESHOLD: float = 0.7
    MAX_RESULTS: int = 5
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()