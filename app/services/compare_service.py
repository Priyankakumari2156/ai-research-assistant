from app.services.chat_service import ChatService
from app.services.prompt_service import PromptService


class CompareService:

    def __init__(self):
        self.chat_service = ChatService()

    def compare(self, document_ids):

        prompt = PromptService.get_prompt("compare")

        return self.chat_service.ask(
            question=prompt,
            action=None,
            document_ids=document_ids
        )