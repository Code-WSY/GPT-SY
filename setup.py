from setuptools import setup, find_packages
setup(
    name='GPT_SY',
    version='1.0.0',
    description='GPT_SY',
    author='Wang Suyun',
    long_description=open('README.md', encoding='utf-8').read(),
    packages=find_packages(),
    package_data={
        'Config.py': ['../data/Model.json', '../data/prompts.json'],
    },
    install_requires=[
        'openai',
    ],
    url='https://github.com/Code-WSY/GPT-SY',
    license='MIT',
    author_email='912745072@qq.com',
    keywords='GPT-GUI',
)
