# My modern Python coding set-up

# Intro
I'm introducing this repo as a playground to test a modern Python set-up.

## Overview
| 🔨 Tool                | Role                        | Benefit                                 |
|---------------------|-----------------------------|-----------------------------------------|
| Git                 | Version control             | Track, revert, and collaborate          |
| uv                  | Virtual env & dependency management        | Fast, reproducible, isolated installs   |
| Cursor              | IDE              | Smarter, faster coding                  |
| Ruff                | Linting & formatting        | Fast, consistent, high-quality code, production ready?     |
| Weights & Biases    | ML experiment tracking      | Track, visualize, and share experiments |

## Way of working with uv
1. Create a new project directory and enter it.
2. Run `uv venv` to create a virtual environment.
3. Activate the environment.
4. Install packages as needed with `uv pip add ...`.
5. (Optional) Run `uv init` to set project metadata if you want.
6. Commit `pyproject.toml` and `uv.lock` to git.
7. Others can clone the repo, run `uv venv`, activate the environment and `uv sync` to get the same environment.


## Way of working for IEEE competition
1. Use and promote modern Python coding set-up (Cursor, Git, Weights and Biases, Nixtla, EDA automation)
2. 