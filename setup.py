import setuptools

longdescription = """Identical to the tkSimpleDialog module, except the widgets used are ttk themed widgets.
Here is an example of how to use it::

    from ttkSimpleDialog import ttkSimpleDialog

    user_response = ttkSimpleDialog.askinteger(title="hello", prompt="Enter a number")

Please note you must call it using the "from __ import __" syntax!"""

setuptools.setup(
    name="ttkSimpleDialog",
    version="1.2.1",
    description="ttk themed version of ttkSimpleDialog",
    author="Tyler Holmes",
    author_email="tyler@holmesengineering.com",
    url="https://github.com/TDHolmes/ttkSimpleDialog",
    # Name the folder where your packages live:
    # (If you have other packages (dirs) or modules (py files) then
    # put them into the package directory - they will be found
    # recursively.)
    packages=['ttkSimpleDialog'],
    # 'package' package must contain files (see list above)
    # I called the package 'package' thus cleverly confusing the whole issue...
    # This dict maps the package name== directories
    # It says, package *needs* these files.
    package_data={'ttkSimpleDialog': []},
    # 'runner' is in the root.
    scripts=["runner"],
    long_description=longdescription,
    #
    # This next part it for the Cheese Shop, look a little down the page.
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Topic :: Software Development :: User Interfaces',
    ]
)
