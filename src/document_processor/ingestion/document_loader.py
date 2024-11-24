"""
Document Loader Component
Handles ingestion of various document formats into the RAG system.
"""

from typing import BinaryIO, Dict, List
from google.cloud import storage
from ...shared.utils.logger import get_logger

logger = get_logger(__name__)

class DocumentLoader:
    """Handles document loading and initial preprocessing"""
    
    def __init__(self, bucket_name: str):
        """Initialize document loader"""
        self.storage_client = storage.Client()
        self.bucket_name = bucket_name
        
    async def load_document(self, file_path: str) -> Dict:
        """
        Load document from storage
        Args:
            file_path: Path to document in Cloud Storage
        Returns:
            Dict containing document content and metadata
        """
        try:
            bucket = self.storage_client.bucket(self.bucket_name)
            blob = bucket.blob(file_path)
            content = blob.download_as_text()
            
            return {
                "content": content,
                "metadata": {
                    "source": file_path,
                    "type": self._get_document_type(file_path),
                    "timestamp": blob.time_created
                }
            }
        except Exception as e:
            logger.error(f"Error loading document {file_path}: {str(e)}")
            raise
    
    def _get_document_type(self, file_path: str) -> str:
        """Determine document type from file extension"""
        extension = file_path.split(".")[-1].lower()
        return {
            "pdf": "application/pdf",
            "docx": "application/docx",
            "txt": "text/plain"
        }.get(extension, "application/octet-stream")