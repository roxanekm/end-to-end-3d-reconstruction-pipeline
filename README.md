# End-to-End 3D Reconstruction Pipeline

Pipeline de reconstruction 3D à partir d’une vidéo monoculaire.

## Pipeline

Video
Frames
Depth (MiDaS)
Point Cloud
Fusion
Mesh (Poisson)

## Installation

pip install -r requirements.txt

## Run

python pipeline.py

## Outputs

data/global_cloud.ply  
data/clean_cloud.ply  
data/mesh.ply  

## Stack

Python  
PyTorch  
MiDaS  
Open3D  
OpenCV  

## Structure

src/ modules pipeline  
data/ inputs et outputs  
pipeline.py entry point