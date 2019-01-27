import os


def make_and_clear_directory(dirbase: str) -> None:
    """ Make dirbase if necessary and then clear generated files """
    import shutil

    safety_file = os.path.join(dirbase, "generated")
    if os.path.exists(dirbase):
        if not os.path.exists(safety_file):
            raise FileNotFoundError("'generated' guard file not found in {}".format(safety_file))
        shutil.rmtree(dirbase)
    os.makedirs(dirbase)
    with open(os.path.join(dirbase, "generated"), "w") as f:
        f.write("Generated for safety.  Directory will not be cleared if this file is not present")
