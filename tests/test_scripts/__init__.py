import os

from tests.utils.dirutils import make_and_clear_directory

testscriptsdir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
testscriptstempdir = os.path.join(testscriptsdir, 'temp')

if not os.path.exists(testscriptstempdir):
    make_and_clear_directory(testscriptstempdir)