# Triangles

- Setup: `pip install -r requirements.txt`
- Run tests: `python -m pytest -q`
- Static analysis: `pylint triangles.py tests/test_triangles.py`
- Coverage:
    ```bash
    coverage erase
    coverage run -m pytest
    coverage report -m
    coverage html
    ```
