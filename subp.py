import subprocess
print("Working on creating CSV...")

subprocess.call(["python3","tora.py"])

print("Finished creating CSV...")

print("Working on creating map...")

subprocess.call(["python3","map_maker.py"])

print("Finished creating map...")
