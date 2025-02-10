generator_prompt = """Given the following summary of a discussion or content:

{summary}

Generate 5 high-quality question-answer pairs that test deep understanding of the key concepts. For each pair:

1. Create a complex, thought-provoking question that requires analysis
2. Provide detailed step-by-step reasoning to arrive at the answer
3. Give a clear, concise final answer

Format each QA pair as a JSON object with these fields:
- "question": The complex question you generated
- "reasoning": Your step-by-step chain of thought analysis
- "answer": The final concise answer

Ensure the questions cover different aspects of the content and require critical thinking rather than just fact recall.

Return the 5 QA pairs formatted as a JSON array."""