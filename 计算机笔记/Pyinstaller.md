# Pyinstaller

- 官方文档 - https://pyinstaller.readthedocs.io/en/stable/index.html
- 安装`pip3 install pyinstaller`

- 打包`pyinstaller Name.py`
- 支持` Windows, Mac OS X, and GNU/Linux`

## 工作原理

- PyInstaller reads a Python script written by you. It analyzes your code to discover every other module and library your script needs in order to execute. Then it collects copies of all those files – including the active Python interpreter! – and puts them with your script in a single folder, or optionally in a single executable file.（PyInstaller读取您编写的 Python 脚本。它会分析您的代码以发现您的脚本需要执行的所有其他模块和库。然后它收集所有这些文件的副本——包括活动的 Python 解释器！– 并将它们与您的脚本放在一个文件夹中，或者可以选择放在一个可执行文件中。）
-  finds all the `import` statements in your script. It finds the imported modules and looks in them for `import` statements, and so on recursively, until it has a complete list of modules your script may use.
- If your script imports a module from an “egg”, PyInstaller adds the egg and its dependencies to the set of needed files.
- PyInstaller also knows about many major Python packages, including the GUI packages [Qt](http://www.qt-project.org/) (imported via [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/intro) or [PySide](http://qt-project.org/wiki/About-PySide)), [WxPython](http://www.wxpython.org/), [TkInter](http://wiki.python.org/moin/TkInter), [Django](https://www.djangoproject.com/)。Some Python scripts import modules in ways that PyInstaller cannot detect: for example, by using the [`__import__()`](https://docs.python.org/3/library/functions.html#__import__) function with variable data, using [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module), or manipulating the [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path) value at run time. If your script requires files that PyInstaller does not know about, you must help it:
- If your program depends on access to certain data files, you can tell PyInstaller to include them in the bundle as well. You do this by modifying the spec file.
- PyInstaller并*没有*包括应该在这个操作系统的任何安装存在库。例如，在 GNU/Linux 中，它不会捆绑来自`/lib`或 的任何文件`/usr/lib`，假设这些文件可以在每个系统中找到。
- It is easy to debug problems that occur when building the app when you use one-folder mode. You can see exactly what files PyInstaller collected into the folder.
- When you change your code, as long as it imports exactly the same set of dependencies, you could send out only the updated `myscript` executable. That is typically much smaller than the entire folder. 
- A bundled program always starts execution in the PyInstaller bootloader. This is the heart of the `myscript` executable in the folder.
- The PyInstaller bootloader is a binary executable program for the active platform (Windows, GNU/Linux, Mac OS X, etc.). When the user launches your program, it is the bootloader that runs. The bootloader creates a temporary Python environment such that the Python interpreter will find all imported modules and libraries in the `myscript` folder.
- The bootloader starts a copy of the Python interpreter to execute your script. Everything follows normally from there, provided that all the necessary support files were included.
- Bundling to One File.The advantage is that your users get something they understand, a single executable to launch. A disadvantage is that any related files such as a README must be distributed separately. Also, the single executable is a little slower to start up than the one-folder bundle.Before you attempt to bundle to one file, make sure your app works correctly when bundled to one folder. It is is *much* easier to diagnose problems in one-folder mode.
- The bootloader is the heart of the one-file bundle also. When started it creates a temporary folder in the appropriate temp-folder location for this OS. The one executable file contains an embedded archive of all the Python modules used by your script, as well as compressed copies of any non-Python support files (e.g. `.so` files). The bootloader uncompresses the support files and writes copies into the the temporary folder. This can take a little time. That is why a one-file app is a little slower to start than a one-folder app.
- After creating the temporary folder, the bootloader proceeds exactly as for the one-folder bundle, in the context of the temporary folder. When the bundled code terminates, the bootloader deletes the temporary folder.
- 因为程序制作了一个具有唯一名称的临时文件夹，您可以运行该应用程序的多个副本；他们不会互相干扰。然而，运行多个副本在磁盘空间上是昂贵的，因为没有任何东西是共享的。
- The `_MEI*xxxxxx*` folder is not removed if the program crashes or is killed (kill -9 on Unix, killed by the Task Manager on Windows, “Force Quit” on Mac OS). Thus if your app crashes frequently, your users will lose disk space to multiple `_MEI*xxxxxx*` temporary folders.It is possible to control the location of the `_MEI*xxxxxx*` folder by using the [`--runtime-tmpdir`](https://pyinstaller.readthedocs.io/en/stable/usage.html#cmdoption-runtime-tmpdir) command line option. Do *not* give administrator privileges to a one-file executable.

## 命令

- https://pyinstaller.readthedocs.io/en/stable/usage.html

## 示例

```bash
pyinstaller  --distpath pkg/dist -F --clean -n spec_file --workpath pkg/build --specpath pkg source.py
```

