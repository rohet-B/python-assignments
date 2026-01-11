# This Phase is all about Data processing.
### For this we need Anaconda: 
- Anaconda is a free software distribution that provides Python along with many pre-installed libraries and tools, mainly for data science and scientific computing.
- Software distribution is a method of delivering software as a complete, installable package. Example: MS Office → Word, Excel, PowerPoint together
- It Comes with python already installed.
- Includes 300 popular libraries like: 
    - NumPy, Pandas, Matplotlib, SciPy
- Provided Jupyter Notebook for writing and running python code easily.
- Helps manage packages and environements without errors.

### To install anaconda go to [Anaconda Website](https://www.anaconda.com/download)
- Before downloading, signup first
- You can use this [video as reference](https://youtu.be/mg6cMkz9Q0c?si=5BmsgzkHkopcXwAg)
- Open AnaConda Navigator

### When we install Anaconda, By default Command line utility of Anaconda known as Conda also installed in our system.
- Conda is basically a package that manages environment so we can say that it is a environment management system.
- Conda allows - A single Operating System to work with multiple environments.
- An environment in python is a separate workspace that contains a specific python project along with specific python versions and installed libraries. For example: Environment A -> Python 3.8, Django 3.2 and Environment B -> Python 3.11, Django 5.0 (Conda keeps different projects isolated)
- Both environments can exist on same computer without conflicts and allows easy switching between environments.
- For windows OS student, we write Conda commands on `Anaconda Prompt`
- `Anaconda Prompt` works similar like cmd or cli, so you can use normal cd,mkdir etc commands on it.

### Conda Commands:
- To see built-in commands type conda in `Anaconda Prompt`
- `conda activate` - Activate a base conda environment + we can activate base environment from any different directory.
- `conda --version` - To check conda version
- `conda list` - Give a list of available packages in environment
- `conda env list` - Gives a list of different environments
- `conda create -n env_name` - Creates a new environment
- `conda activate env_name` - Activates the created environment
- `conda deactivate` - Deactivates the current environment you are inside of it.
- `conda env remove -n env_name` OR `conda remove -n env_name --all` - To delete an environment (2 prompts are given) but before deleting an environment we have to deactivate it. + We don't delete base conda environment we just deactivate it.

### base environment
- When Anaconda is installed, Conda creates a base environment.
- It allows Conda to work properly.
- It manages: Creating new environment + Installing packages + Updating Conda
- We should not use base enviroment for projects.

### Installing Jupyter Notebook
- Go to desktop in `Anaconda Prompt` using cd command and make different directory to understand the concept.
- `conda install jupyter`
- Now run this command (after conda install jupyter) `jupyter notebook` 
- Jupyter notebook will now open
- Go to File tab > New, create a `new notebook`
- Jupyter Notebook is a browser based code editor used to write and run code in cells + It is best suited for data science + Earlier, in VS Code, we used to write code in different files (like `.py` files), but in Jupyter Notebook, code is written in different notebooks with the `.ipynb` file format + Code in jupyter notebook are written in chunks called `cells`, Writing code in cells allows you to run the program step by step, so you don’t need to execute the entire code at once. You can run one cell at a time, check the output immediately, and this makes the code easier to debug and understand. It also supports easy experimentation, because you can change a small part of the code, re-run only that specific cell, and quickly test new ideas, which is very useful in data analysis and machine learning tasks + We can download a jupyter notebook and it will get saved (download) inside the system (folder). Don't think that, since jupyter notebook is running in the browser it will get saved in cloud storage - NO.

### Installing JupyterLab
- JupyterLab is the next-generation or advanced interface of Jupyter Notebook. It is More advanced, More flexible and More powerful.
- JupyterLab allows to work with Multiple notebooks, Multiple folders and Multiple Data's.
- To install jupyterLab `conda install jupyterlab` once done write below prompt
- `jupyter lab`