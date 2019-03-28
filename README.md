# Defer

Add a simple golang-esque deferral system for python.

# Usage

```
@defer.with_defer
def example_function(defer):
    print("Hello")
    defer(print, "!")
    print("World")
    
example_function()
> Hello
> World
> !
```