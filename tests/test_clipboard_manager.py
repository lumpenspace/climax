
import unittest
from unittest.mock import patch, MagicMock
from clipboard_maximizer.clipboard_manager import copy_to_clipboard
import platform
import subprocess
import os

scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'clipboard_maximizer'))

class TestClipboardManager(unittest.TestCase):
    @patch('platform.system')
    def test_copy_to_clipboard_macos(self, mock_platform):
        mock_platform.return_value = 'Darwin'
        with patch('subprocess.run') as mock_run:
            copy_to_clipboard(['testfile.txt'])
            mock_run.assert_called_with(['osascript', os.path.join(scripts_dir, 'copy-macos.applescript'), 'testfile.txt'], check=True)

    @patch('platform.system')
    def test_copy_to_clipboard_linux(self, mock_platform):
        mock_platform.return_value = 'Linux'
        with patch('subprocess.run') as mock_run:
            copy_to_clipboard(['testfile.txt'])
            mock_run.assert_called_with([os.path.join(scripts_dir, 'copy-linux-xclip.sh'), 'testfile.txt'], check=True)

    @patch('platform.system')
    def test_copy_to_clipboard_windows(self, mock_platform):
        mock_platform.return_value = 'Windows'
        with patch('subprocess.run') as mock_run:
            copy_to_clipboard(['testfile.txt'])
            mock_run.assert_called_with([
                'powershell',
                '-ExecutionPolicy', 'Bypass', 
                '-File', os.path.join(scripts_dir, 'copy-windows.ps1'),
                'testfile.txt'
            ], check=True)

    @patch('platform.system')
    def test_copy_to_clipboard_unsupported_os(self, mock_platform):
        mock_platform.return_value = 'UnsupportedOS'
        with self.assertRaises(SystemExit) as cm:
            copy_to_clipboard(['testfile.txt'])
        self.assertEqual(cm.exception.code, 1)

    @patch('subprocess.run')
    def test_copy_to_clipboard_osascript_not_installed(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, 'osascript')
        with self.assertRaises(SystemExit) as cm:
            copy_to_clipboard(['testfile.txt'], 'Darwin')
        self.assertEqual(cm.exception.code, 1)

    # Additional tests can be written for error handling in Linux and Windows environments

if __name__ == '__main__':
    unittest.main()
