import os, subprocess, shutil

def run(cmd):
    subprocess.run(cmd, check=True)

try:
    shutil.rmtree(".conan2")
except:
    pass


# SETUP, creation of packages

run("conan profile detect")

os.chdir("repos")

for pkg in ("mathlib", "ai", "graphics", "engine", "game", "mapviewer"):
    run(f"git clone git@github.com:memsharded/conanci_{pkg}")
    run(f"conan create conanci_{pkg}")


run("conan list")

os.chdir("..")



# SimpleWS

os.chdir("simplews")

run("conan workspace open")
run("conan workspace build")
run("game/build/Release/game.exe")
# modify engine, see that it works


# SimpleWS

os.chdir("../monows")

run("conan workspace open")
run("conan workspace super-install")
run("cmake --build --preset conan-release")
# modify engine, see that it works

# FullWS
