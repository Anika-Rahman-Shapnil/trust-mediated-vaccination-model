# Manuscript figure-to-code guide

**Manuscript:** *Trust-Mediated Vaccination Feedback and the Saddle-Node Elimination of Endemic Equilibria in an Epidemic Model*

This index links the figures in the 44-page manuscript to their corresponding Python notebook cells. The mapping follows the scientific content of the panels, not the filenames of exported images. Cell numbers are **1-based** and refer to the supplied notebook versions.

## Figure index

| Manuscript figure | Content | Notebook | Cell |
|:--|:--|:--|--:|
| 2 | Backward bifurcation in the no-feedback model | `epidemic_model_analysis.ipynb` | 19 |
| 3 | Disease-free and endemic bistability for different initial conditions | `epidemic_model_analysis.ipynb` | 27 |
| 4 | Endemic-equilibrium branches and saddle-node bifurcation | `equilibrium_bifurcation_analysis.ipynb` | 15 |
| 5 | Long-term infection dynamics at λ = 30 and 31 | `equilibrium_bifurcation_analysis.ipynb` | 12 |
| 6 | Near-fold transient and long-term dynamics at λ = 31, 31.12, 31.2 and 32 | `equilibrium_bifurcation_analysis.ipynb` | 13 |
| 7 | Behavioral state and vaccination preference near the saddle-node | `equilibrium_bifurcation_analysis.ipynb` | 14 |
| 8 | Global and enlarged equilibrium maps in the (Θ, Tc) plane | `equilibrium_bifurcation_analysis.ipynb` | 6 |
| 9 | Equilibrium branches under direct vaccine waning | `epidemic_model_analysis.ipynb` | 19 |
| 10 | Infection dynamics with and without direct vaccine waning | `epidemic_model_analysis.ipynb` | 18 |
| 11 | Initial-condition-dependent epidemic trajectories | `epidemic_simulations.ipynb` | 3 |
| 12 | Epidemic dynamics with and without infection-driven feedback | `equilibrium_bifurcation_analysis.ipynb` | 7 |
| 13 | Sensitivity to the initial behavioral state | `epidemic_model_analysis.ipynb` | 17 |
| 14 | Baseline epidemic and behavioral dynamics | `epidemic_simulations.ipynb` | 1 |
| 15 | Epidemic trajectories in four parameter scenarios | `epidemic_simulations.ipynb` | 1 |
| 16(a) | Full behavior-driven time series | `epidemic_model_analysis.ipynb` | 12 |
| 16(b) | Zoomed post-outbreak behavior-driven time series | `epidemic_model_analysis.ipynb` | 14 |
| 16(c) | Instantaneous social payoff under BDO and CVO | `epidemic_model_analysis.ipynb` | 15 |
| 17 | Social Efficiency Deficit (SED) across (λ, μ) | `epidemic_model_analysis.ipynb` | 5 |
| 18(a) | Cumulative Social Payoff (CSP) under BDO across (λ, μ) | `epidemic_model_analysis.ipynb` | 5 |
| 18(b) | Cumulative Social Payoff (CSP) at CVO across (λ, μ) | `epidemic_model_analysis.ipynb` | 5 |
| 19 | Economic sensitivity to infection and vaccination cost weights | `epidemic_model_analysis.ipynb` | 5 |

## Computational conventions

The manuscript distinguishes the **instantaneous social payoff rate**

\[
\Pi(t)=-C_I\frac{I(t)}{N}-C_V\frac{\phi x(t)S(t)}{N}
\]

from the **cumulative social payoff** over the simulation horizon,

\[
\mathrm{CSP}=\int_0^{T}\Pi(t)\,dt.
\]

The Social Efficiency Deficit is defined as \(\mathrm{SED}=\mathrm{CSP}_{\mathrm{CVO}}-\mathrm{CSP}_{\mathrm{BDO}}\).

**BDO** is the Behavior-Driven Outcome from the coupled model. **CVO** is the Constant Vaccination Optimum, found by comparing 101 uniformly spaced *constant* vaccination preferences in [0, 1]. CVO is therefore an optimum within the tested constant-preference grid, not a claim of optimality among unrestricted time-dependent policies.

## Reproducing the figures

1. Install the dependencies listed in [`requirements.txt`](requirements.txt).
2. Open the relevant notebook in [`notebooks/`](notebooks/) and run its prerequisite cells before the indicated plotting cell.
3. For Figures **17–19**, the heatmap plotting cell uses precomputed convergence results: it reads an existing `results[1e-9]` entry or loads `convergence_rtol_1e-09.npz`. Generate or provide those results before running the heatmap cell.
4. Compare the generated panel, parameters and axis labels with the manuscript. Some notebook cells generate more than one plot, including exploratory outputs not used in the manuscript.

The compartmental schematic (Figure 1) and numerical tables are outside the scope of this figure index. The source-cell mapping is based on inspection of the supplied manuscript, notebook code and stored outputs; it is not a claim that every notebook has been executed successfully from a clean environment.
