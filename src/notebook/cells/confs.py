import os
import sys

ROOT = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
SRC = os.path.abspath(os.path.join(ROOT, "src"))
sys.path.append(ROOT)
sys.path.append(SRC)
