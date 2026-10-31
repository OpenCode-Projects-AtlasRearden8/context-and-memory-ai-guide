#!/usr/bin/env bash
# Build the Context & Memory AI Guide site (and optionally run its tests).
#
#   ./build.sh            build site/ from docs/
#   ./build.sh --check    build, then run the test suite
#
# Zero dependencies beyond Python 3. Everything is local.

set -euo pipefail
cd "$(dirname "$0")"

python3 build.py "$@"

if [[ "${1:-}" == "--check" ]]; then
  python3 tests/run_tests.py
fi
