from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='my project',
    url='',
    author='Volodymyr Karban',
    author_email='volodymyrkarban@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:to_check_the_folder_path']}
)
