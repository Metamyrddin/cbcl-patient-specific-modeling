# From-Scratch Patient-Specific Modeling on Windows

Pure Python implementations of key concepts from Stanford CBCL patient-specific modeling research: neural network-based template mesh deformation for heart reconstruction and vessel lumen segmentation/regression.

Completely from scratch, no SimVascular dependency. Runs natively on Windows with standard PyTorch/NumPy.

## Contents

- `mesh_deformation.py`: Simple template mesh deformation using PyTorch (inspired by MeshDeformNet / HeartDeformNets)
- `vessel_lumen.py`: Neural network for vessel lumen regression from 2D cross-sections
- `demo_data.py`: Synthetic data generators
- `requirements.txt`

See individual files for usage.
