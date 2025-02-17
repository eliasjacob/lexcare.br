# Evaluating LLMs for Healthcare-Related Named Entity Recognition in Brazilian Judicial Decisions

This repository contains the LexCare.BR dataset and the minimal code required to generate Few-Shot NER. The study evaluates state-of-the-art large language models (LLMs) for extracting healthcare-related named entities from Brazilian judicial decisions.

## Repository Structure

- **dataset/**
  - `lexcare_br.json`: The LexCare.BR dataset, containing 1,200 manually annotated legal rulings. (Due to its large size, manual inspection is not recommended.)
  
- **paper_submission.pdf**
  - The full paper detailing the methodology, experiments, results, and conclusions.
  
- **example_use.ipynb**
  - A Jupyter Notebook demonstrating the experimental workflow. This notebook includes:
    - Few-shot prompt generation for Named Entity Recognition (NER) using the `generate_few_shot_ner_prompts` function.
    - An experiment using `ChatOpenAI` with the “gpt-4o-mini” model to extract structured healthcare entities from legal texts.
    - Usage of a schema (imported as `Saude` from `tools.schema`) to parse and output the recognized entities.
  
- **tools/**
  - Python modules supporting the experiments:
    - `prompt.py`: Contains functions for generating few-shot Named Entity Recognition prompts.
    - `fewshot.py`: Provides helper functions to construct and refine few-shot prompts.
    - `schema.py`: Defines the "Saude" schema used to structure and validate the output from the NER extraction.
  
- **pyproject.toml** and **poetry.lock**
  - Configuration files for dependency management via Poetry.

## Overview

The paper investigates the performance of both open-source and proprietary LLMs for extracting healthcare-related entities such as diseases, pharmaceutical ingredients, and medical procedures from unstructured legal texts. Key insights include:

- **Dataset:** LexCare.BR is a gold-standard dataset compiled from 1,200 legal rulings.
- **Methodology:** The experiments leverage few-shot function calling. In `example_use.ipynb`, a few-shot prompt is generated from an input legal text, and the ChatOpenAI extractor (using the gpt-4o-mini model) is used to perform NER based on a defined schema.
- **Findings:** Larger models tend to achieve higher overall F1-scores, with robust precision in extracting complex healthcare entities.
- **Implications:** Automating the extraction process can support real-time healthcare policy analysis and judicial decision-making.

## Reproducibility

- All experiments use a fixed random seed (`271828`) to ensure reproducibility.
- The project is set up with Poetry; simply run `poetry install` to set up the environment.

## Getting Started

1. **Clone the Repository**  
   Clone the repository using your preferred method.

2. **Install Dependencies**  
   This project uses Poetry for dependency management. Install the dependencies by running:
   ```bash
   poetry install
   ```

3. **Run the Example Notebook**  
   Open `example_use.ipynb` in Jupyter Notebook or VSCode’s Notebook interface. The notebook shows:
   - Generating few-shot NER prompts.
   - Using the ChatOpenAI extractor configured with the “gpt-4o-mini” model.
   - Extracting and displaying structured healthcare entity data.

## License

[MIT License](https://choosealicense.com/licenses/mit/)
