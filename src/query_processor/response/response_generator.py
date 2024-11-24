"""
Response Generator Component
Generates responses using Vertex AI LLM
"""

from typing import Dict, List
import vertexai
from vertexai.language_models import TextGenerationModel
from ...shared.utils.logger import get_logger

logger = get_logger(__name__)

class ResponseGenerator:
    """Handles generation of responses using LLM"""
    
    def __init__(self, model_name: str = "text-bison@latest"):
        """Initialize response generator"""
        self.model = TextGenerationModel.from_pretrained(model_name)
        
    async def generate_response(self, prompt: str) -> Dict:
        """
        Generate response using LLM
        Args:
            prompt: Formatted prompt with context
        Returns:
            Dictionary containing response and metadata
        """
        try:
            response = self.model.predict(
                prompt,
                temperature=0.3,
                max_output_tokens=1024,
                top_k=40,
                top_p=0.8,
            )
            
            return {
                "response": response.text,
                "metadata": {
                    "model": self.model.model_name,
                    "confidence": response.prediction_response.safety_attributes.scores
                }
            }
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            raise