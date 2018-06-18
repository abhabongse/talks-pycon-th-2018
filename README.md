# Talks in PyCon Thailand 2018

A collection of talks given at PyCon Thailand 2018.

## Environment Setup

From inside a presentation directory,

1. Install packages via [`pipenv`](https://docs.pipenv.org/):
    ```bash
    $ pipenv install
    ```

2. Run post-installation script to enable RISE extension in Jupyter notebooks:
    ```bash
    $ pipenv run post-install
    ```

3. Start a new Jupyter notebook session:
    ```bash
    $ pipenv run jupyter notebook
    ```

4. **Viewing the presentation:** Browse for a notebook to view and press `Alt-R` to start (or end) the presentation.

    Use `Space` and `Shift-Space` to navigate between elements inside the presentation. Other Jupyter notebook-specific commands should still work.

## Development Setup

Assuming that the first three steps from [Environment Setup](#environment-setup) are followed, here is how to create a new presentation with RISE:

1. Create a new notebook.
2. Show the presentation toolbar by clicking the top-bar menu: `View > Cell Toolbar > Slideshow`.
3. Go rogue!

