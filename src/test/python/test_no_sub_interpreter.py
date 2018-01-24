import unittest
import sys
from jep_pipe import jep_pipe
from jep_pipe import build_java_process_cmd

@unittest.skipIf(sys.platform.startswith("win"), "subprocess complications on Windows")
class TestNoSubInterpreter(unittest.TestCase):

    def test_no_sub_interpreter(self):
        jep_pipe(build_java_process_cmd('jep.test.TestNoSubInterpreter'))

