import os
import unittest
import yaml
from tests.test_issues.environment import env
from tests.utils.test_environment import TestEnvironmentTestCase


from biolinkml.generators.infer_model import infer_model

class Issue371TestCase(TestEnvironmentTestCase):
    env = env

    def header(self, txt: str) -> str:
        return '\n' + ("=" * 20) + f" {txt} " + ("=" * 20)

    def test_issue_371(self):
        """ Infer a model from a CSV """
        CLS = 'my_class'
        obj = infer_model(env.input_path('issue_371.csv'), sep=',', class_name=CLS)
        print(yaml.dump(obj))
        assert len(obj['classes'][CLS]['slots']) == 4
        assert obj['slots']['age']['range'] == 'integer'
        assert obj['slots']['name']['range'] == 'string'



if __name__ == '__main__':
    unittest.main()
