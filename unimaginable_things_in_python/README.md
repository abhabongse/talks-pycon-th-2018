# Unimaginable Things in Python

A talk given by Watcharapol Watcharawisetkul and Abhabongse Janthong at
PyCon Thailand 2018.

## Notes about RISE presentation

- The `black` theme is set via notebook metadata (accessible via
  `Edit > Edit Notebook Metadata` menu).
- The stylesheet with the same name as the presentation is provided for
  look-and-feel customization.

## Errata

These corrections have not yet been made into the presentation file.

- There are **more than 3 ways** a new variable is introduced in functional
  scope (all except the first 3 were not yet mentioned in the presentation).

  Assuming that `nonlocal` or `global` declarations are not present for
  these variables, `UnboundLocalError` will be raised if variables are
  accessed before assignments within the function.

    1. Function arguments
        ```python
        def foo(bar):  # bar is a new variable in foo
            ...
        ```

    2. Variable assignments
        ```python
        def foo():
            ...
            bar = 'new value'  # bar is a new variable in foo
            ...
        ```

    3. Type annotations
        ```python
        def foo():
            bar: int  # bar is a new variable in foo
            ...
        ```

    4. For-statements (not including for-loops in comprehensions)
        ```python
        def foo():
            ...
            for bar in range(10):  # bar is a new variable in foo
                pass
            ...
        ```

    5. With-statements
        ```python
        def foo():
            ...
            with open('input.txt') as bar:  # bar is a new variable
                pass
            ...
        ```
