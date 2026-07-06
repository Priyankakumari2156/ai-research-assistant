from app.services.chat_service import ChatService
from app.services.prompt_service import PromptService


class LiteratureService:

    def __init__(self):
        self.chat_service = ChatService()

    def generate(self, document_ids):

        prompt = PromptService.get_prompt("literature_review")

        return self.chat_service.ask(
            question=prompt,
            action=None,
            document_ids=document_ids
        )