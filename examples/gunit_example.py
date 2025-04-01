"""
Example demonstrating the advanced capabilities of G-UNIT (Guided Unified Notation for Intelligent Text).
"""

from langlang import GUNIT, lang

@lang("Initializing G-UNIT framework")
def demonstrate_gunit():
    # Create a G-UNIT instance
    gunit = GUNIT()
    
    # Example 1: Basic template processing
    print("\nBasic Template Processing:")
    template = "Hello, {name}! Welcome to {product} version {version}."
    result = gunit.process(
        template,
        name="Developer",
        product="G-UNIT",
        version="1.0.0"
    )
    print(f"Template: {template}")
    print(f"Result: {result}")
    
    # Example 2: Template validation
    print("\nTemplate Validation:")
    valid_template = "The {animal} is {color} and {mood}."
    invalid_template = "The {animal is {color} and {mood}."
    
    print(f"Valid template: {GUNIT.validate_template(valid_template)}")
    print(f"Invalid template: {GUNIT.validate_template(invalid_template)}")
    
    # Example 3: Variable extraction
    print("\nVariable Extraction:")
    complex_template = "The {animal} {action} {direction} the {object} at {time}."
    variables = GUNIT.extract_variables(complex_template)
    print(f"Template: {complex_template}")
    print(f"Variables: {variables}")
    
    # Example 4: Advanced template processing with context
    print("\nAdvanced Template Processing:")
    processor = gunit.create_template("story_template")
    story_template = """
    Once upon a time, there was a {character} who loved to {action}.
    One day, they {event} and discovered {discovery}.
    From that day forward, they {resolution}.
    """
    
    # Validate the template
    if GUNIT.validate_template(story_template):
        # Process with context
        result = processor.set_context(
            character="wizard",
            action="code",
            event="stumbled upon G-UNIT",
            discovery="the power of template processing",
            resolution="wrote beautiful templates every day"
        ).process(story_template)
        
        print("Generated Story:")
        print(result)
    else:
        print("Invalid template!")

if __name__ == "__main__":
    demonstrate_gunit() 