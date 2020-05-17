from setuptools import setup


setup(name='political-predictor',
      version='0.1',
      description='Predict political orientation and sentiment of a text',
      url='https://github.com/piotrgajdzica/political-predictor',
      author='Piotr Gajdzica',
      author_email='piotr.gajdzica@wp.pl',
      license='MIT',
      packages=['political_predictor'],
      install_requires=[
          'flair', 'requests'
      ],
      zip_safe=False)
