"""
Embedding Generator Component
Generates embeddings for document chunks using Vertex AI
"""

from typing import List
import vertexai
from vertexai.language_models import TextEmbeddingModel
from ...shared.utils.logger import get_logger

logger = get_logger(__name__)

class EmbeddingGenerator:
    """Handles generation of embeddings for text chunks"""
    
    def __init__(self):
        """Initialize embedding generator"""
        self.model = TextEmbeddingModel.from_pretrained("textembedding-gecko@latest")
        
    async def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of text chunks
        Args:
            texts: List of text chunks to embed
        Returns:
            List of embedding vectors
        """
        try:
            embeddings = []
            for text in texts:
                embedding = self.model.get_embeddings([text])[0]
                embeddings.append(embedding.values)
            return embeddings
        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            raise