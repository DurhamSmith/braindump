#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3 ninja

import glob
from pathlib import Path

files = glob.glob("/home/dd/org/Notes/*.org")
#files.append(glob.glob("/home/dd/org/Notes/Lit/*.org"))
#files = glob.glob("/home/dd/org/daily/*.org")
#files = files.append(glob.glob("/home/dd/org/daily/*.org"))
#files = ["/home/dd/org/Notes/dey21_dna_origam.org"]
#files = ["/home/dd/org/Notes/test.org", "/home/dd/org/Notes/nanotech.org"]


print(files)

# with open('build.ninja', 'w') as ninja_file:
#     ninja_file.write("""
# rule org2md
#   command = emacs --batch -l ~/.emacs.d/init.el -l publish.el --eval \"(jethro/publish \\"$in\\")"
#   description = org2md $in
# """)
with open('build.ninja', 'w') as ninja_file:
    ninja_file.write("""
rule org2md
  command = emacs --batch -l ~/.emacs.d/init.el -l publish.el --eval \"(jethro/publish \\"$in\\")"
  description = org2md $in
    """)
    
    for f in files:
        path = Path(f)
        output_file = f"/home/dd/org/braindump/content/posts/{path.with_suffix('.md').name}"
        print(f"STREETLIHTS: {output_file}  \n PATH: {path}")
        ninja_file.write(f"""
build {output_file}: org2md {path}
""")

import subprocess
subprocess.call(["ninja"])



files = glob.glob("/home/dd/org/Notes/Lit/*.org")
with open('build.ninja', 'w') as ninja_file:
    ninja_file.write("""
rule org2md
  command = emacs --batch -l ~/.emacs.d/init.el -l publish.el --eval \"(jethro/publish \\"$in\\")"
  description = org2md $in
    """)

    for f in files:
        path = Path(f)
        output_file = f"/home/dd/org/braindump/content/posts/{path.with_suffix('.md').name}"
        print(f"STREETLIHTS: {output_file}  \n PATH: {path}")
        ninja_file.write(f"""
build {output_file}: org2md {path}
""")

import subprocess
subprocess.call(["ninja"])
