import os, sys, subprocess

# read the owdir

p = subprocess.Popen(["owdir"], stdout=subprocess.PIPE)
(names,errcode) = p.communicate()
print(names)
