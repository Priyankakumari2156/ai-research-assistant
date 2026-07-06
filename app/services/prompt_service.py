class PromptService:

    PROMPTS = {

        "summary": """
You are an expert research assistant.

Summarize the research paper using the following sections:

1. Objective
2. Methodology
3. Dataset
4. Results
5. Conclusion

Keep it concise and use bullet points.
""",

        "methodology": """
Explain the methodology used in this research paper.

Include:

- Workflow
- Algorithms
- Models
- Experimental setup
- Evaluation strategy
""",

        "contributions": """
List the major contributions of this paper.

Explain each contribution in simple language.
""",

        "limitations": """
Identify the limitations of this research.

Include both:

- Limitations mentioned by the authors
- Possible practical limitations
""",

        "future_work": """
Identify the future work suggested in this paper.

Also recommend additional future research directions.
""",

        "applications": """
Explain the practical applications of this research.

Mention:

- Industries
- Real-world use cases
- Benefits
""",

        "compare": """
You are an expert research assistant.

Compare the selected research papers.

Generate a comparison table with the following columns:

1. Research Objective
2. Methodology
3. Dataset
4. Model/Algorithm
5. Results
6. Strengths
7. Limitations
8. Future Work

After the table, provide:

- Key similarities
- Key differences
- Which paper performs best and why
- Research gaps
- Recommendations for future research

Base your comparison only on the provided document context.
""",

        "literature_review": """
You are an expert research assistant.

Generate a comprehensive literature review using the selected research papers.

Structure the review with the following sections:

1. Introduction
2. Existing Research
3. Comparison of Methods
4. Research Gap
5. Future Research Directions
6. Conclusion

Write in an academic style suitable for a journal or thesis.

Do not invent information. Base your review only on the provided document context.
"""
    }

    @classmethod
    def get_prompt(cls, action):
        return cls.PROMPTS.get(action)