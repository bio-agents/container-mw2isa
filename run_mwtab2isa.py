import sys
import os
mwtab_study_id = sys.argv[1]
target_dir = sys.argv[2]
try:
    from isaagents.convert import mw2isa
    mw2isa(mwtab_study_id, target_dir)
except ImportError as e:
    raise RuntimeError("Could not import isaagents package")

