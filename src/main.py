"""
RAG System Main Application
Entry point for the RAG application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Dict

# Import our components
from api.router import router
from shared.config.settings import settings
from shared.utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

# Create FastAPI application
app = FastAPI(
    title="Enterprise RAG System",
    description="Retrieval Augmented Generation System for Enterprise Documentation",
    version="1.0.0",
    docs_url="/api/docs",      # Swagger UI endpoint
    openapi_url="/api/openapi.json"
)

# Add CORS middleware for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only - restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include our API router
app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root() -> Dict:
    """Root endpoint - system information"""
    return {
        "system": "Enterprise RAG System",
        "version": "1.0.0",
        "status": "operational",
        "environment": settings.ENVIRONMENT
    }

@app.get("/health")
async def health() -> Dict:
    """Health check endpoint"""
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT
    }

if __name__ == "__main__":
    # Run application with uvicorn when script is run directly
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )