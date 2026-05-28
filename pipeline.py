import os
os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"

from src.extract_frames import extract_frames
from src.mesh_pipeline import run_pipeline

VIDEO_PATH = "data/360_ear.mp4"
FRAMES_DIR = "data/frames"

def main():

    print("1. Extract frames")
    extract_frames(VIDEO_PATH, FRAMES_DIR, fps_skip=5)

    print("2. Run full 3D pipeline")
    run_pipeline()

    print("DONE")

if __name__ == "__main__":
    main()