#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
import sys
import os
from pathlib import Path

cxc_build_path = Path(sys.argv[0]).resolve()


if (cxc_build_path.parent / 'cxc_build').is_dir():
	sys.path.insert(0, str(cxc_build_path.parent))

from cxc_build import main

if __name__ == '__main__':
	sys.exit(main())


