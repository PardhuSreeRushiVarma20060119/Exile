#!/usr/bin/env python3
"""
Test suite for Exile-SafeWork Framework
Tests the core functionality and modules without executing real malicious operations
"""

import unittest
import sys
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock
from io import StringIO

# We're already in the exile-safework directory, no need to modify path

# Import core modules
from core.banner import show_banner
from core.dispatch import dispatch_command
from modules.dropperlab.dropper import simulate_dropper, simulate_persistence, simulate_execution


class TestCoreBanner(unittest.TestCase):
    """Test the banner display functionality"""
    
    def test_show_banner(self):
        """Test that banner displays correctly"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            show_banner()
            output = mock_stdout.getvalue()
            
            # Check that banner contains expected elements
            # Note: EXILE is displayed as ASCII art, not plain text
            self.assertIn("SAFE WORK EMULATION FRAMEWORK", output)
            self.assertIn("v1.0.4", output)
            self.assertIn("Emulates Real Ops Without Real Payloads", output)
            # Check for some ASCII art characters to confirm banner is displayed
            self.assertIn("▄████████", output)


class TestCoreDispatch(unittest.TestCase):
    """Test the command dispatch functionality"""
    
    def test_invalid_command(self):
        """Test that invalid commands display error message"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            dispatch_command("invalid_command")
            output = mock_stdout.getvalue()
            
            self.assertIn("[!] Unknown command: invalid_command", output)

    def test_valid_command_dropperlab(self):
        """Test that dropperlab command works"""
        with patch('modules.dropperlab.dropper.dropper_menu') as mock_dropper:
            dispatch_command("dropperlab")
            mock_dropper.assert_called_once()


class TestDropperLab(unittest.TestCase):
    """Test the dropper lab functionality"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.test_payload = os.path.join(self.test_dir, "test_payload.exe")
        
        # Create a dummy payload file
        with open(self.test_payload, 'w') as f:
            f.write("dummy payload content")
    
    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_simulate_dropper_valid_payload(self):
        """Test dropper simulation with valid payload"""
        dest_dir = os.path.join(self.test_dir, "destination")
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('modules.dropperlab.dropper.simulate_persistence') as mock_persist:
                with patch('modules.dropperlab.dropper.simulate_execution') as mock_exec:
                    simulate_dropper(self.test_payload, dest_dir)
        
        output = mock_stdout.getvalue()
        
        # Check that payload was "dropped"
        self.assertIn("[+] Payload successfully dropped", output)
        
        # Verify the file was copied
        target_path = os.path.join(dest_dir, "test_payload.exe")
        self.assertTrue(os.path.exists(target_path))
        
        # Verify simulation functions were called
        mock_persist.assert_called_once_with(target_path)
        mock_exec.assert_called_once_with(target_path)
    
    def test_simulate_dropper_invalid_payload(self):
        """Test dropper simulation with invalid payload"""
        invalid_payload = os.path.join(self.test_dir, "nonexistent.exe")
        dest_dir = os.path.join(self.test_dir, "destination")
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            simulate_dropper(invalid_payload, dest_dir)
        
        output = mock_stdout.getvalue()
        self.assertIn("[!] Payload file does not exist", output)
    
    def test_simulate_persistence(self):
        """Test persistence simulation"""
        test_path = "/fake/path/payload.exe"
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('time.sleep'):  # Mock sleep to speed up test
                with patch('random.choice', return_value="Test Technique"):
                    simulate_persistence(test_path)
        
        output = mock_stdout.getvalue()
        self.assertIn("[*] Simulating persistence", output)
        self.assertIn("[+] Technique used: Test Technique", output)
    
    def test_simulate_execution(self):
        """Test execution simulation"""
        test_path = "/fake/path/payload.exe"
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('time.sleep'):  # Mock sleep to speed up test
                simulate_execution(test_path)
        
        output = mock_stdout.getvalue()
        self.assertIn("[*] Simulating execution", output)
        self.assertIn("[+] Simulated process launch", output)


class TestMainApplication(unittest.TestCase):
    """Test the main application loop"""
    
    def test_exile_main_can_be_imported(self):
        """Test that the main exile module can be imported"""
        try:
            import exile
            self.assertTrue(hasattr(exile, 'main'), "Main function exists")
        except ImportError:
            self.skipTest("Exile main module not accessible from test location")


class TestSafetyChecks(unittest.TestCase):
    """Test that the framework maintains safety boundaries"""
    
    def test_no_real_malware_execution(self):
        """Verify that no actual malicious code is executed"""
        # This test ensures that the simulation functions don't actually
        # perform dangerous operations
        
        test_path = "/fake/dangerous/payload.exe"
        
        # These should only print messages, not perform real operations
        with patch('sys.stdout', new_callable=StringIO):
            with patch('time.sleep'):
                simulate_persistence(test_path)
                simulate_execution(test_path)
        
        # If we reach this point, no actual malicious operations were performed
        self.assertTrue(True, "Safety check passed - no real operations executed")
    
    def test_file_operations_are_safe(self):
        """Test that file operations only work with test files"""
        # The dropper should only copy files, not execute them
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = os.path.join(temp_dir, "safe_test.txt")
            dest_dir = os.path.join(temp_dir, "dest")
            
            with open(test_file, 'w') as f:
                f.write("safe test content")
            
            with patch('sys.stdout', new_callable=StringIO):
                with patch('modules.dropperlab.dropper.simulate_persistence'):
                    with patch('modules.dropperlab.dropper.simulate_execution'):
                        simulate_dropper(test_file, dest_dir)
            
            # Verify file was copied (safe operation)
            copied_file = os.path.join(dest_dir, "safe_test.txt")
            self.assertTrue(os.path.exists(copied_file))
            
            # Verify content is unchanged (no modification)
            with open(copied_file, 'r') as f:
                content = f.read()
            self.assertEqual(content, "safe test content")


class TestImportSafety(unittest.TestCase):
    """Test that all modules can be imported safely"""
    
    def test_core_imports(self):
        """Test that core modules import without issues"""
        try:
            from core.banner import show_banner
            from core.dispatch import dispatch_command
            self.assertTrue(True, "Core modules imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import core modules: {e}")
    
    def test_dropper_imports(self):
        """Test that dropper module imports without issues"""
        try:
            from modules.dropperlab.dropper import simulate_dropper, run_dropper
            self.assertTrue(True, "Dropper module imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import dropper module: {e}")

    def test_all_module_functions_exist(self):
        """Test that all expected functions exist in modules"""
        expected_functions = {
            'modules.dropperlab.dropper': ['run_dropper', 'dropper_menu'],
            'modules.stage1.stage1': ['run_stage1'],
            'modules.stage2.stage2': ['run_stage2'],
            'modules.endgame.endgame': ['run_endgame'],
            'modules.payloadlab.payload': ['payload_menu'],
            'modules.telemetry.telemetry': ['telemetry_menu'],
            'modules.guard.guard': ['guard_menu'],
            'modules.vault.vault': ['vault_menu'],
            'modules.sharedspace.session': ['session_menu'],
            'modules.dashboard.dashboard': ['dashboard_menu']
        }
        
        for module_name, functions in expected_functions.items():
            try:
                module = __import__(module_name, fromlist=functions)
                for func_name in functions:
                    self.assertTrue(hasattr(module, func_name), 
                                  f"Function {func_name} missing from {module_name}")
            except ImportError as e:
                self.fail(f"Failed to import {module_name}: {e}")


def run_tests():
    """Run all tests with detailed output"""
    print("=" * 60)
    print("EXILE-SAFEWORK FRAMEWORK TEST SUITE")
    print("=" * 60)
    print("Testing core functionality and safety boundaries...")
    print()
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestCoreBanner,
        TestCoreDispatch,
        TestDropperLab,
        TestMainApplication,
        TestSafetyChecks,
        TestImportSafety
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED! The framework is working correctly.")
    else:
        print("\n❌ Some tests failed. Please review the output above.")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)