from setuptools import setup, find_packages

setup(name='flatconfig',
      version='0.0.1a',
      description='Flattened dict-based configuration',
      url='http://github.com/wpeixoto/flatcofig',
      author='wpeixoto',
      author_email='carlos.peixoto@camara.leg.br',
      license='MIT',
      # packages=['weighted_tree'],
      packages=find_packages(exclude=['tests']),
      zip_safe=False)
