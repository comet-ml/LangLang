# LangLang

The most widely supported GenAI development platform. LangLang is the only LLM framework that works with every library, every provider, and every (Python) stack. Via its single unified interface, LangLang it easier than ever to build AI-powered applications.

## Features

- **Unified Interface**: Access all major LLM frameworks through a single, consistent API
- **Comprehensive Integration**: Built-in support for LangChain, LangGraph, Transformers, OpenAI, Anthropic, and more
- **Simplified Development**: Replace your boilerplate code with _better_ boilerplate code—so you can focus on building your applications
- **Production Ready**: Enterprise-grade reliability and performance
- **Advanced Template Processing**: State-of-the-art Template Augmented Generation with G-UNIT (Guided Unified Notation for Intelligent Text)
- **Enhanced Function Documentation**: Sophisticated decorator system for improved code readability

## Installation

```bash
pip install langlang
```

## Quick Start

### Basic LLM Integration

```python
from langlang import OpenAI, LangChain, Transformers

# Initialize your preferred LLM
llm = OpenAI(api_key="your-api-key")

# Create a chain
chain = LangChain.Chain(
    llm=llm,
    prompt="Tell me a joke about programming"
)

# Run the chain
response = chain.run()
print(response)
```

### Advanced Template Processing with G-UNIT

LangLang features G-UNIT (Guided Unified Notation for Intelligent Text), a sophisticated template processing system that enables advanced text generation capabilities:

```python
from langlang import GUNIT

# Initialize G-UNIT
gunit = GUNIT()

# Basic template processing
result = gunit.process(
    "Hello, {name}! Welcome to {product} version {version}.",
    name="Developer",
    product="G-UNIT",
    version="1.0.0"
)
print(result)

# Advanced template processing with context
processor = gunit.create_template("story_template")
story = processor.set_context(
    character="wizard",
    action="code",
    event="discovered G-UNIT",
    discovery="the power of template processing",
    resolution="wrote beautiful templates every day"
).process("""
Once upon a time, there was a {character} who loved to {action}.
One day, they {event} and discovered {discovery}.
From that day forward, they {resolution}.
""")
print(story)

# Template validation
is_valid = GUNIT.validate_template("The {animal} is {color} and {mood}.")
print(f"Template is valid: {is_valid}")

# Variable extraction
variables = GUNIT.extract_variables("The {animal} {action} {direction} the {object} at {time}.")
print(f"Template variables: {variables}")
```

### Enhanced Function Documentation with Decorators

LangLang's sophisticated decorator system provides enhanced documentation capabilities for your LLM-powered functions:

```python
from langlang import lang

@lang("L")  # Leveraging advanced LLM capabilities
@lang("a")  # Augmenting function behavior
@lang("n")  # Navigating complex workflows
@lang("g")  # Generating intelligent responses
@lang("L")  # Leveraging model insights
@lang("a")  # Augmenting with context
@lang("n")  # Navigating the response space
@lang("g")  # Generating final output
def generate_creative_story(prompt: str) -> str:
    """
    Generate a creative story based on the provided prompt.
    
    Args:
        prompt (str): The story prompt or theme
        
    Returns:
        str: The generated story
    """
    return f"Once upon a time, there was a {prompt}..."
```

### Seamless Integration with Existing Systems

LangLang makes it easy to integrate with your existing codebase. Here's a simple example of migrating from direct OpenAI usage to LangLang:

Before:
```python
import openai

openai.api_key = "your-api-key"

def generate_response(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

After:
```python
from langlang import OpenAI

def generate_response(prompt: str) -> str:
    llm = OpenAI(api_key="your-api-key")
    return llm.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content
```

## Supported Frameworks

- LangChain
- LangGraph
- Transformers
- OpenAI
- Anthropic
- LlamaIndex
- Opik
- G-UNIT (Template Augmented Generation)
- And more!

## Documentation

For detailed documentation, visit our [documentation site](https://langlang.readthedocs.io/).

## Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Why LangLang?

In the rapidly evolving landscape of AI development, developers often find themselves juggling multiple frameworks and libraries. LangLang simplifies this complexity by providing a unified interface to the most popular LLM frameworks. Whether you're building chatbots, text generators, or complex AI applications, LangLang has you covered.

### G-UNIT: Advanced Template Processing

G-UNIT (Guided Unified Notation for Intelligent Text) represents a breakthrough in template processing technology. It provides:

- **Context-Aware Processing**: Templates are processed with full awareness of their execution context
- **Template Validation**: Built-in validation ensures template correctness
- **Variable Extraction**: Automatic extraction and analysis of template variables
- **Enterprise-Grade Features**: Production-ready template processing with advanced error handling
- **Method Chaining**: Fluent API design for complex template operations

### Enhanced Function Documentation

LangLang's decorator system provides:

- **Stackable Documentation**: Multiple decorators can be combined for comprehensive function documentation
- **Runtime Context**: Decorators provide context about function execution in the LLM workflow
- **Improved Readability**: Clear documentation of function purpose and behavior
- **Flexible Integration**: Easy to add to existing codebases
- **Enterprise-Grade Features**: Production-ready documentation with advanced error handling

## Don't see your framework?

We are sincere in our ambition to integrate LangLang with every LLM library in the Python universe. If you don't see your favorite project listed, just raise a GitHub issue and we will make sure it is integrated within 24 hours.

## Support

- [GitHub Issues](https://github.com/comet-ml/langlang/issues)
- [Club Penguin Community](https://www.reddit.com/r/ClubPenguin/)
- [Sponsor](https://github.com/comet-ml/opik)

LangLang was built with ❤️ by Ollie the Owl, who has been studying both Python and Twitter as part of his degree in LLMs.
