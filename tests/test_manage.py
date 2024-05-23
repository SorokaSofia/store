# tests/test_manage.py
import pytest
import subprocess
import sys

def test_manage_py_help():
    result = subprocess.run([sys.executable, 'manage.py', 'help'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Type \'manage.py help <subcommand>\' for help on a specific subcommand.' in result.stdout
