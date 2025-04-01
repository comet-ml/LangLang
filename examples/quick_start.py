"""
Quick start example demonstrating LangLang's unified interface.
"""

from langlang import OpenAI, LangChain, Transformers

def main():
    # Initialize OpenAI
    llm = OpenAI(api_key="your-api-key")
    
    # Create a simple chain
    chain = LangChain.Chain(
        llm=llm,
        prompt="Write a haiku about programming"
    )
    
    # Run the chain
    response = chain.run()
    print("OpenAI Response:")
    print(response)
    
    # Initialize Transformers
    model = Transformers.AutoModelForCausalLM.from_pretrained("gpt2")
    tokenizer = Transformers.AutoTokenizer.from_pretrained("gpt2")
    
    # Generate text
    inputs = tokenizer("Write a short story about", return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    print("\nTransformers Response:")
    print(text)

if __name__ == "__main__":
    main() 