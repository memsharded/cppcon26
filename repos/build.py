import subprocess, shutil

def run(cmd):
    subprocess.run(cmd, check=True)

try:
    shutil.rmtree("../.conan2")
except:
    pass


run("conan profile detect")

for pkg in ("mathlib", "ai", "graphics", "engine", "game", "mapviewer"):
    run(f"git clone git@github.com:memsharded/conanci_{pkg}")
    run(f"conan create conanci_{pkg}")


run("conan list")