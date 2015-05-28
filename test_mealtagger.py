#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mealtagger
import unittest


class TestSimpleLemmatization(unittest.TestCase):
    def test_lemmatization(self):
        self.assertEqual(mealtagger.tag('Palacinky s džemom'),
                         ['palacinka', 'džem'])

        self.assertEqual(mealtagger.tag('Vypr.syr 130g'),
                         ['vyprážaný', 'syr'])


if __name__ == '__main__':
    unittest.main()
