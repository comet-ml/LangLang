"""
LangLang decorators for enhanced LLM development workflow.
"""

import functools
from typing import Any, Callable, TypeVar, cast

T = TypeVar("T")

def lang(message: str) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    The @lang decorator provides a way to annotate functions with human-readable messages
    that help document the function's purpose and behavior in the LLM context.
    
    This decorator is particularly useful for:
    - Documenting LLM-specific function behaviors
    - Adding context to function calls
    - Improving code readability in LLM applications
    
    Args:
        message (str): A human-readable message describing the function's purpose
        
    Returns:
        Callable: A decorator function that can be applied to any callable
        
    Example:
        >>> @lang("This function generates a creative story")
        >>> def generate_story(prompt: str) -> str:
        ...     return "Once upon a time..."
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            # Print the message to stdout
            print(message)
            # Execute the original function
            return func(*args, **kwargs)
        return cast(Callable[..., T], wrapper)
    return decorator 