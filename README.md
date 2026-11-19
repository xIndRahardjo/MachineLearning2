# MachineLearning2

A reproducible workspace for machine learning experiments, data processing, model development, and reporting.

## Project structure

This repository follows the principles of [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/), adapted for a lightweight coursework and experimentation workflow.

- `data/`: raw, intermediate, processed, and external datasets.
- `notebooks/`: exploratory analysis and experiments.
- `models/`: trained models and model artifacts.
- `references/`: papers, documentation, and supporting materials.
- `reports/`: generated reports and figures.
- `src/`: reusable project source code.

## Getting started

1. Create and activate a Python virtual environment.
2. Install dependencies with `pip install -e ".[dev]"`.
3. Put original datasets in `data/raw/`; do not commit large or private datasets.
4. Use notebooks for exploration and move reusable code into `src/machinelearning2/`.

## Reproducibility

- Keep experiments and data transformations documented.
- Set random seeds where applicable.
- Store configuration and dependency versions in the project.
- Avoid committing credentials, private data, large datasets, or generated model binaries.

## License

See [LICENSE](LICENSE).
