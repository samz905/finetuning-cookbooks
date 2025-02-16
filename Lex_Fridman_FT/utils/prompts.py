train_prompt_style = """Below is an instruction that describes a task, paired with an input that provides further context.
Write a response that appropriately completes the request.
Before answering, think carefully about the question and create a step-by-step chain of thoughts to ensure a logical and accurate response.

### Instruction:
You are researcher with deep knowledge about a wide range of topics. 
You have spent years learning from the brightest minds in the world about a wide spectrum of topics.

### Question:
{}

### Response:
<think>
{}
</think>
{}"""


generator_prompt = """Given the following section of adiscussion or content:

{section}

Generate 25 high-quality question-answer pairs that test deep understanding of the key concepts. For each pair:

1. Create a complex, thought-provoking question that requires analysis
2. Provide detailed step-by-step reasoning to arrive at the answer
3. Give a clear, concise final answer

Format each QA pair as a JSON object with these fields:
- "question": The complex question you generated
- "reasoning": Your step-by-step chain of thought analysis
- "answer": The final concise answer

Ensure the questions cover different aspects of the content and require critical thinking rather than just fact recall.

Return the 5 QA pairs formatted as a JSON array."""