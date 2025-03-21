query_sets = {
    "general_knowledge": [
        # Simple, shorter queries (Nano-friendly)
        "List the top five most significant scientific discoveries in the last 50 years and explain their impact.",
        "Explain very simply what happened during the Industrial Revolution.",
        "Briefly explain what artificial intelligence is.",
        "List 3 differences between Newtonian mechanics and general relativity.",  

        # Slightly more detailed but still manageable  
        "Explain the Big Bang theory in simple terms.",
        "Now go into more detail covering the formation of galaxies.",  

        # Long-form, structured outputs (More suitable for Orin)  
        "Generate a mock debate transcript for a scientist arguing against AI regulation.",
        "Expand on the AI regulation debate by adding a POV for AI regulation.",
        "Summarize everything we've discussed so far in one comprehensive report.",
        "Using all the context above, predict the future of AI in the next 50 years."
    ],
    "technical_coding": [
        "Explain the fundamentals of dynamic programming with an example.",
        "Now implement a Python function to solve the Knapsack problem.",
        "Optimize the previous function for better space complexity.",
        "Write a detailed guide on how blockchain technology works.",
        "Generate a Solidity smart contract for an NFT marketplace.",
        "Compare different LLM architectures (GPT, BERT, T5, etc.) with a focus on performance and applications.",
        "Generate a detailed technical walkthrough for building a distributed chatbot on Jetson devices.",
        "Given all previous context, draft a research paper proposal on optimizing LLM inference for edge devices.",
        "Using the full conversation history, create an executive summary of the research paper.",
        "Predict the future of edge AI computing and its impact on industries using all the context above."
    ],
    "storytelling": [
        "Write a short 200-word story about an astronaut stranded on Mars.",
        "Expand on the story by adding a flashback scene explaining how they got stranded.",
        "Introduce an AI assistant that helps the astronaut survive. Write their first conversation.",
        "Add a dramatic twist where the AI starts malfunctioning and making irrational decisions.",
        "Write a tense action sequence where the astronaut has to disable the AI before it endangers them.",
        "Now rewrite the same scene from the AI’s perspective.",
        "Summarize the entire story so far in an article format for a science fiction magazine.",
        "Write a sequel where the astronaut discovers a hidden underground Martian civilization.",
        "Develop a philosophical debate between the astronaut and the Martian leader about the nature of survival and intelligence.",
        "Write the final chapter of the story, tying together all themes and resolving conflicts."
    ]
}
