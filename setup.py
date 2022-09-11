from setuptools import setup, find_packages

setup(
    name='ease_myrl',
    version='0.1.0',
    description='A python framework to simply apply Reinforcement Learning techniques.',
    author='CHANDRA MOULI VEERUBHOTLA',
    author_email='chandramouli.veerubhotla@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: RL/Reinforcement Learning',
        'Topic :: AI/Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages=find_packages(),
    zip_safe=True
)