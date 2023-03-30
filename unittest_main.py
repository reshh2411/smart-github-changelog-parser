#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""unittest_main.py: unit testing to check if the function performs as expected"""

__author__ = "Reshhmaa B"
__date__ = "March 31, 2023"
__status__ = "Development"

import unittest
import main


class UnitTestFunction(unittest.TestCase):
    """
    Functions compare sample test strings with true and false using .assertTrue() and .assertFalse()
    return: True/False
    """

    def test_regex_true(self):
        testcase_list_true_py = ['{+# new comment+}', '[-# removed comment-]', '# comment [-old-]{+new+}',
                                 '# comment [-old-]{+new+}', '# take input[-from the user-]',
                                 '# take input {+from the user+}', 'temp = num  {+# new comment here+}',
                                 'temp = num  [-# new comment here-]', 'temp = num  # new comment [-here-]{+test+}',
                                 'if num == sum:  # comment[-here-]',  '{+hello world # new comment+}',
                                 '[-hello world # new comment-]']

        regex1 = r'.*[#].*[+]}|[#].*[-]]'
        regex2 = r'{[+[#]+}|[[]-#-]'
        result_true = main.true_false_regex(regex1, regex2, testcase_list_true_py)
        self.assertTrue(result_true)

    def test_regex_false(self):
        testcase_list_false_py = ['temp = number[-#-] new comment test', 'temp = [-num-]{+number+} # new comment test',
                                  '[-while temp > 0:-]', '{+while temp > 0:+}', '{+# new comment+', '{+#+} sum = 0']

        regex1 = r'.*[#].*[+]}|[#].*[-]]'
        regex2 = r'{[+[#]+}|[[]-#-]'
        result_false = main.true_false_regex(regex1, regex2, testcase_list_false_py)
        self.assertFalse(result_false)

    def test_regex_false2(self):
        testcase_list_false2_py = ['{+# new comment+}', 'temp = [-num-]{+number+} # new comment test']

        regex1 = r'.*[#].*[+]}|[#].*[-]]'
        regex2 = r'{[+[#]+}|[[]-#-]'
        result_false2 = main.true_false_regex(regex1, regex2, testcase_list_false2_py)
        self.assertFalse(result_false2)

    def test_regex_false3(self):
        testcase_list_false3_py = ['temp = number[-#-] new comment test', '{+#+} sum = 0']

        regex1 = r'.*[#].*[+]}|[#].*[-]]'
        regex2 = r'{[+[#]+}|[[]-#-]'
        result_false3 = main.true_false_regex(regex1, regex2, testcase_list_false3_py)
        self.assertFalse(result_false3)

    def test_regex_true_c(self):
        testcase_list_true_ccpp = ['{+// new comment+}', '[-// removed comment-]', '// comment [-old-]{+new+}',
                                   '// comment [-old-]{+new+}', '// take input[-from the user-]',
                                   '// take input {+from the user+}', 'temp = num  {+// new comment here+}',
                                   'temp = num  [-// new comment here-]', 'temp = num  // new comment [-here-]{+test+}',
                                   'if num == sum:  // comment[-here-]', '{+hello world // new comment+}',
                                   '[-hello world // new comment-]']

        regex1 = r'.*[\/\/].*[+]}|[\/\/].*[-]]'
        regex2 = r'{[+]\/\/[+]}|[[]-\/\/-]'
        result_true = main.true_false_regex(regex1, regex2, testcase_list_true_ccpp)
        self.assertTrue(result_true)

    def test_regex_false_ccpp(self):
        testcase_list_false_ccpp = ['temp = number[-//-] new comment test',
                                    'temp = [-num-]{+number+} // new comment test', '[-while temp > 0:-]',
                                    '{+while temp > 0:+}', '{+// new comment+', '{+//+} sum = 0']

        regex1 = r'.*[\/\/].*[+]}|[\/\/].*[-]]'
        regex2 = r'{[+]\/\/[+]}|[[]-\/\/-]'
        result_false = main.true_false_regex(regex1, regex2, testcase_list_false_ccpp)
        self.assertFalse(result_false)

    def test_regex_false2_ccpp(self):
        testcase_list_false2_ccpp = ['{+// new comment+}', 'temp = [-num-]{+number+} // new comment test']

        regex1 = r'.*[\/\/].*[+]}|[\/\/].*[-]]'
        regex2 = r'{[+]\/\/[+]}|[[]-\/\/-]'
        result_false2 = main.true_false_regex(regex1, regex2, testcase_list_false2_ccpp)
        self.assertFalse(result_false2)

    def test_regex_false3_ccpp(self):
        testcase_list_false3_ccpp = ['temp = number[-//-] new comment test', '{+//+} sum = 0']

        regex1 = r'.*[\/\/].*[+]}|[\/\/].*[-]]'
        regex2 = r'{[+]\/\/[+]}|[[]-\/\/-]'
        result_false3 = main.true_false_regex(regex1, regex2, testcase_list_false3_ccpp)
        self.assertFalse(result_false3)


if __name__ == '__main__':
    unittest.main()



