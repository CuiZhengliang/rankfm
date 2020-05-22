from setuptools import setup

setup(
    name='rankfm',
    version='0.1.0',
    description='a python implementation of the generic factorization machines model class '
                'adapted for collaborative filtering recommendation/ranking problems '
                'with implicit feedback user-item interaction data',
    author='Eric Lundquist',
    author_email='e.t.lundquist@gmail.com',
    url='https://github.com/etlundquist/rankfm',
    keywords=['machine', 'learning', 'recommendation', 'factorization', 'machines', 'implicit'],
    license='GNU General Public License v3.0',
    packages=['rankfm'],
    python_requires='>=3.6',
    install_requires=['numpy>=1.15', 'pandas>=0.24', 'numba>=0.49.1']
)

