"""From-scratch template mesh deformation. Pure PyTorch, Windows-friendly."""
import torch
import torch.nn as nn
import numpy as np

class MeshDeformNet(nn.Module):
    def __init__(self, n_vertices=80):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 8, 3, padding=1), nn.ReLU(),
            nn.AdaptiveAvgPool2d(4), nn.Flatten(),
            nn.Linear(8*16, 64), nn.ReLU(),
            nn.Linear(64, n_vertices*3)
        )
    def forward(self, image, template):
        offsets = self.encoder(image).view(-1, template.size(1), 3)
        return template + 0.1 * offsets  # small offsets

def generate_sphere(n=80, radius=1.0):
    phi = np.random.uniform(0, np.pi, n)
    theta = np.random.uniform(0, 2*np.pi, n)
    pts = np.stack([
        radius * np.sin(phi) * np.cos(theta),
        radius * np.sin(phi) * np.sin(theta),
        radius * np.cos(phi)
    ], axis=1)
    return torch.tensor(pts, dtype=torch.float32)

if __name__ == '__main__':
    m = MeshDeformNet()
    template = generate_sphere().unsqueeze(0)
    img = torch.rand(1, 1, 64, 64)
    out = m(img, template)
    print(out.shape)
    print('Mesh deformation module ready')
