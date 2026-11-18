# Research Notebooks

This directory contains Jupyter notebooks supporting the numerical investigations presented in the manuscript:

**Trust-Mediated Vaccination Feedback and the Saddle-Node Elimination of Endemic Equilibria in an Epidemic Model**

## Notebook descriptions

### 1. `equilibrium_bifurcation_analysis.ipynb`

Contains numerical calculations related to endemic equilibria and bifurcation behavior, including:

- Computation of positive endemic equilibria.
- Analysis of the saddle-node bifurcation.
- Exploration of the behavioral-feedback parameter plane.
- Numerical equilibrium-count verification and visualization of the saddle-node boundary.

### 2. `epidemic_model_analysis.ipynb`

Contains additional mathematical and numerical investigations of the trust-mediated vaccination model, including equilibrium and model sensitivity analyses.

### 3. `epidemic_simulations.ipynb`

Contains numerical simulations of the epidemic model and visualization of its dynamical behavior under different parameter settings.

## Running the notebooks

The notebooks can be executed using Google Colab or a local Jupyter environment.

For Google Colab:

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload the desired `.ipynb` file.
3. Select **Runtime → Run all**.
4. Examine the generated figures and numerical outputs.

The notebooks may require different execution times depending on the numerical calculations performed.

## Dependencies

The required Python packages are listed in the `requirements.txt` file in the repository's root directory.

## Reproducibility

The notebooks provide computational implementations supporting the manuscript's numerical analyses. The equilibrium and bifurcation calculations include numerical verification procedures.

Some analyses may require additional computational time or further validation. Complete independent reproduction of every manuscript result has not yet been established.
