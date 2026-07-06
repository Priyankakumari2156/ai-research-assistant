from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
from app.services.workspace_service import WorkspaceService


class ChatService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_service = VectorService()
        self.llm_service = LLMService()

    def ask(self,question=None,action=None,document_ids=None):

        # If user selected a predefined research action,
        # replace the question with the corresponding prompt.
        if action:

            question = PromptService.get_prompt(action)

            if question is None:
                return {
                    "error": f"Unknown action: {action}"
                }

        # Create embedding for question
        query_embedding = self.embedding_service.model.encode(
            question,
            convert_to_numpy=True
        )

        # Retrieve relevant chunks
        results = self.vector_service.search(query_embedding,document_ids=document_ids)

        # Build context
        # Build context
        context_parts = []

        for i, result in enumerate(results, start=1):

            context_parts.append(
                f"""
        Document ID: {result.payload["document_id"]}

        Chunk: {result.payload["chunk_id"]}

        Text:

        {result.payload["text"]}

        ----------------------------------------
        """
            )

        context = "\n".join(context_parts)


        # Generate answer
        try:

            answer = self.llm_service.generate_answer(
                question,
                context
            )

            WorkspaceService.add_chat(question,answer)
            
            if action:

                WorkspaceService.update(action,answer)

        except Exception as e:

            return {
                "question": question,
                "answer": "⚠ Gemini is temporarily unavailable. Please try again in a few moments.",
                "sources": [
                    {
                        "document_id": r.payload["document_id"],
                        "chunk_id": r.payload["chunk_id"],
                        "filename": r.payload["filename"],
                        "text": r.payload["text"],
                        "word_count": r.payload["word_count"],
                        "score": float(r.score)
                    }
                    for r in results
                ],
                "error": str(e)
            }

        return {
            "question": question,
            "answer": answer,
            "sources": [
                {
                    "document_id": r.payload["document_id"],
                    "chunk_id": r.payload["chunk_id"],
                    "filename": r.payload["filename"],
                    "text": r.payload["text"],
                    "word_count": r.payload["word_count"],
                    "score": float(r.score)
                }
                for r in results
            ]
        }