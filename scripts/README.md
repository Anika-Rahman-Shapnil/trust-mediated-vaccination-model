
# Validation Scripts

This folder contains standalone Python scripts used to validate numerical results reported in the manuscript.

## Recovery-allocation validation

`validate_recovery_allocation.py` compares the original vaccination-preference-based recovery allocation with an alternative infection-origin-based allocation.

The script calculates endemic equilibria, Jacobian eigenvalues, and saddle-node coordinates.

Run from the repository root:

```bash
python scripts/validate_recovery_allocation.py
```
