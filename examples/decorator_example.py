"""
Example demonstrating the use of LangLang's @lang decorator for enhanced LLM function documentation.
"""

from langlang import lang

@lang("Initializing the story generation pipeline")
@lang("Loading creative writing parameters")
@lang("Configuring narrative structure")
def generate_story(prompt: str) -> str:
    """
    Generate a creative story based on the provided prompt.
    
    Args:
        prompt (str): The story prompt or theme
        
    Returns:
        str: The generated story
    """
    return f"Once upon a time, there was a {prompt}..."

@lang("Initializing the code generation system")
@lang("Loading programming language templates")
@lang("Configuring code style parameters")
def generate_code(description: str) -> str:
    """
    Generate code based on a natural language description.
    
    Args:
        description (str): The code description
        
    Returns:
        str: The generated code
    """
    return f"def {description.lower().replace(' ', '_')}():\n    pass"

def main():
    # Example 1: Story Generation
    print("\nGenerating a story...")
    story = generate_story("magical AI assistant")
    print(f"Generated story: {story}")
    
    # Example 2: Code Generation
    print("\nGenerating code...")
    code = generate_code("Create a function that sorts numbers")
    print(f"Generated code:\n{code}")

if __name__ == "__main__":
    main() 