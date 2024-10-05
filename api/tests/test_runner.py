from dotenv import load_dotenv
load_dotenv()

import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='Apis')

    runner = unittest.TextTestRunner()
    runner.run(suite)

