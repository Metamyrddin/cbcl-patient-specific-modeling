# Stanford CBCL Patient-Specific Modeling

This repository recreates and collects resources related to the patient-specific modeling research at the Cardiovascular Biomechanics Computation Lab (CBCL) at Stanford University, led by Prof. Alison Marsden.

Source overview: https://cbcl.stanford.edu/research-overview/computational-methods/patient-specific-modeling

## Overview

Cardiovascular simulations require patient-specific geometries. Generating 3D models from medical images is time-consuming. The lab develops methods for:

- **Automated segmentation** with minimal user interaction using neural networks:
  - Blood vessel segmentation (pathline-based lumen identification)
  - Heart segmentation (direct mesh reconstruction by deforming templates)

- **Interactive mesh morphing** for efficient exploration of surgical scenarios (e.g., stenoses, grafting in Fontan, aneurysms).

Related open-source software: [SimVascular](http://simvascular.org/) (full pipeline from images to simulation) and [Vascular Model Repository](https://vascularmodel.com/).

## Key Papers and Code

### Heart Segmentation / Mesh Reconstruction
- Kong, F., Wilson, N., Shadden, S.C. (2021). A deep-learning approach for direct whole-heart mesh reconstruction. *Medical Image Analysis*. Code: https://github.com/fkong7/MeshDeformNet (arXiv:2102.07899)
- Kong, F., Shadden, S.C. (2022). Learning Whole Heart Mesh Generation From Patient Images For Computational Simulations. Code: https://github.com/fkong7/HeartDeformNets (arXiv:2203.10517)
- Kong, F., Shadden, S.C. (2021). Whole Heart Mesh Generation For Image-Based Computational Simulations By Learning Free-Form Deformations. Code: https://github.com/fkong7/HeartFFDNet (arXiv:2107.10839)
- Kong et al. SDF4CHD: Generative Modeling of Cardiac Anatomies with Congenital Heart Defects (arXiv:2311.00332). Code: https://github.com/fkong7/SDF4CHD

### Vessel Segmentation
- Maher, G. et al. (2020). Neural Network Vessel Lumen Regression for Automated Lumen Cross-Section Segmentation in Cardiovascular Image-Based Modeling. *Cardiovasc Eng Technol*. PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7785699/
- Maher, G. et al. (2019). Accelerating cardiovascular model building with convolutional neural networks. *Med Biol Eng Comput*.

### Surgical Planning / Mesh Morphing
- Pham, J. et al. (2022). svMorph: Interactive geometry-editing tools for virtual patient-specific vascular anatomies. (arXiv:2210.07087). Code: https://github.com/SimVascular/svMorph
- Pham, J. et al. (2024). Virtual Shape-Editing of Patient-Specific Vascular Models Using Regularized Kelvinlets. *IEEE Trans Biomed Eng*. PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11138343/

Open-access PDFs (where available) are in the `papers/` directory or linked above.

## How to Recreate

1. Start with SimVascular for traditional pipeline.
2. For automated heart meshes: clone and run MeshDeformNet or HeartDeformNets on CT/MR data.
3. For morphing: use svMorph or Kelvinlets methods to edit geometries for virtual surgery.
4. Couple to reduced-order models (0D/1D) for full circulatory simulation.

Contributions and extensions welcome!
