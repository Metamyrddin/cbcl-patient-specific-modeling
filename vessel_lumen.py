"""From-scratch vessel lumen regression. Pure PyTorch, Windows-friendly."""
import torch
import torch.nn as nn
import numpy as np

class VesselLumenNet(nn.Module):
    def __init__(self, n_points=32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(64*64, 512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU(),
            nn.Linear(256, n_points)
        )
    def forward(self, x):
        return self.net(x.view(x.size(0), -1))

def generate_synthetic_vessel(batch=4, size=64, n_points=32):
    images, radii = [], []
    angles = np.linspace(0, 2*np.pi, n_points, endpoint=False)
    for _ in range(batch):
        center = size//2 + np.random.randint(-4,5)
        base_r = np.random.uniform(12, 18)
        r = base_r + 2*np.sin(2*angles) + np.random.randn(n_points)*0.5
        img = np.zeros((size, size))
        yy, xx = np.ogrid[:size, :size]
        dist = np.sqrt((yy-center)**2 + (xx-center)**2)
        img[dist < base_r*0.7] = 1.0
        images.append(img)
        radii.append(r)
    return torch.tensor(images, dtype=torch.float32).unsqueeze(1), torch.tensor(radii, dtype=torch.float32)

if __name__ == '__main__':
    m = VesselLumenNet()
    imgs, rads = generate_synthetic_vessel()
    print(imgs.shape, m(imgs).shape)
    print('Vessel lumen module ready')
