import os

from google import genai


class GeminiClient:
    """Gemini API 클라이언트 클래스"""

    _api_key = os.getenv("GEMINI_API_KEY", "AIzaSyD7njri5rYS6-J6KkGhxGPoR8aeov6CX0g")
    
    
    _model_id = "gemini-2.5-flash-preview-05-20"
    
    @classmethod
    def _create_client(cls):
        """새로운 Gemini 클라이언트 인스턴스 생성"""
        return genai.Client(
            api_key=cls._api_key,
        )