import os
import re
import unittest
from typing import Optional, Callable, Dict

from rdflib import Graph, Namespace, OWL

from biolinkml import METAMODEL_NAMESPACE
from biolinkml.utils.generator import Generator
from tests.utils.test_environment import TestEnvironment

BIOLINK_NS = Namespace("https://w3id.org/biolink/vocab/")


class GeneratorTestCase(unittest.TestCase):
    model_name: str = None              # yaml name (sans '.yaml')
    output_name: str = None             # If different than model name
    importmap: Dict[str, str] = None    # Location of the import mappings if any

    @staticmethod
    def _print_triples(g: Graph):
        """ Pretty print the contents of g, removing the prefix declarations """
        g.bind('BIOLINK', BIOLINK_NS)
        g.bind('meta', METAMODEL_NAMESPACE)
        g.bind('owl', OWL)
        g_text = re.sub(r'@prefix.*\n', '', g.serialize(format="turtle").decode())
        print(g_text)

    def single_file_generator(self,
                              env: TestEnvironment,
                              suffix: str,
                              gen: type(Generator), *,
                              format: Optional[str] = None,
                              generator_args: Optional[dict] = None,
                              serialize_args: Optional[dict] = None,
                              filtr: Optional[Callable[[str], str]] = None,
                              comparator: Callable[[str, str], str] = None) -> None:
        """ Invoke generator specified in gen

        :param env: Input environment
        :param suffix: File suffix (without '.')
        :param gen: Generator to invoke
        :param format: Generator format argument
        :param generator_args: Additional arguments to the generator
        :param serialize_args: Arguments to serializer.
        :param filtr: Filter to remove metadata specific info from the output.  Default: identity
        :param comparator: Comparison method to use.  Default: GeneratorTestCase._default_comparator
        """
        if serialize_args is None:
            serialize_args = {}
        if generator_args is None:
            generator_args = {}
        if format:
            generator_args["format"] = format
        if self.importmap is not None and 'importmap' not in generator_args:
            generator_args['importmap'] = self.importmap
        yaml_file = env.input_path(self.model_name + '.yaml')
        output_base = self.output_name if self.output_name is not None else self.model_name

        env.generate_single_file(output_base + ('.' if output_base else '') + suffix,
                                 lambda: gen(yaml_file, **generator_args).serialize(**serialize_args),
                                 filtr=filtr, comparator=comparator, value_is_returned=True)


    def directory_generator(self, dirname: str, gen: type(Generator), gen_args: Optional[dict] = None,
                            serialize_args: Optional[dict] = None, skip_compare_step: bool = False) -> None:
        """
        Generate an output directory using the appropriate command and then compare the target with the source
        :param dirname: name of output directory (e.g. gengraphviz)
        :param gen: generator to use
        :param gen_args: arguments to the generator constructor
        :param serialize_args: arguments to the generator serializer
        :param skip_compare_step: True means just generate -- don't compare
        """
        if gen_args is None:
            gen_args = {}
        if serialize_args is None:
            serialize_args = {}
        if self.importmap is not None and 'importmap' not in gen_args:
            gen_args['importmap'] = self.importmap
        source_dir = os.path.join(self.source_path, dirname)
        if not os.path.exists(source_dir) or skip_compare_step:
            make_and_clear_directory(source_dir)
            target_dir = source_dir
        else:
            target_dir = os.path.join(self.target_path, dirname)
            make_and_clear_directory(target_dir)
        yaml_file = os.path.join(self.model_path, self.model_name + '.yaml')
        gen(yaml_file, **gen_args).serialize(directory=target_dir, **serialize_args)
        if source_dir == target_dir:
            if skip_compare_step:
                print(f"Output generated in {dirname} -- you may want to check it manually")
                return
            else:
                self.fail(f"{dirname} created - rerun test")
        diffs = are_dir_trees_equal(target_dir, source_dir)
        if diffs:
            print(diffs)
            self.assertTrue(False, f"{dirname} mismatch")
        make_and_clear_directory(target_dir)
