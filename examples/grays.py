import pathlib

from hatched import hatched

if __name__ == "__main__":
    image_path = pathlib.Path(__file__).parent / "grays.png"
    hatched.hatch(str(image_path), hatch_pitch=1)
