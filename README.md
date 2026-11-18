# Trust-Mediated Vaccination Feedback and Endemic Equilibria

This repository contains Python code supporting the manuscript:

**Trust-Mediated Vaccination Feedback and the Saddle-Node Elimination of Endemic Equilibria in an Epidemic Model**

Authors: Anika Rahman Shapnil and Md. Mamun-Ur-Rashid Khan


## Overview

The study investigates a compartmental epidemic model with vaccination, waning immunity, and a trust-related behavioral state that influences vaccination preference.

The analysis examines pre-existing endemic bistability, backward bifurcation in the no-feedback model, and the modification and eventual elimination of endemic equilibria through a saddle-node bifurcation as behavioral feedback increases.


## Repository Contents

- `notebooks/equilibrium_bifurcation_analysis.ipynb` — Equilibrium analysis, stability calculations, and bifurcation investigations.
- `notebooks/epidemic_model_analysis.ipynb` — Epidemic model analysis, numerical simulations, and additional computational investigations.
- `notebooks/epidemic_simulations.ipynb` — Epidemic simulations and parameter-sensitivity analyses.
- `scripts/validate_recovery_allocation.py` — Equilibrium, stability, and saddle-node validation under alternative recovery-allocation assumptions.

## Installation

Python 3.10 or newer is recommended.

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the code

Open the notebooks in Jupyter Notebook or Google Colab and run the relevant cells.

To run the recovery-allocation validation script from the repository root:

```bash
python scripts/validate_recovery_allocation.py
```

Some analyses may require additional runtime or separate validation files. Full end-to-end reproduction of every manuscript result has not yet been verified.

## Numerical methods

The notebooks contain numerical integration, equilibrium calculations, and sensitivity analyses. Solver tolerances vary according to the calculations performed.

The final heatmap convergence analysis uses tighter numerical tolerances than the preliminary simulations.

## Code availability

The repository is being prepared to support reproducibility of the manuscript's numerical analyses.
