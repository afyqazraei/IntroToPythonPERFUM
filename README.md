### Introduction To Python

## For students

Hi, everyone!

For those of you who are new to all this, welcome to GitHub! GitHub is a place where people, sometimes from all corners of the world, come together and collaborate on programming projects. Here in this repository, are Jupyter Notebooks that can be launched through Binder. All of this is open source, and can be accessible almost anywhere, anytime. 

The Notebooks will give you a brief tutorial into Python, designed for physics undergrads that have little to no experience in programming. Just press the Binder link and let it launch. Learn, enjoy, explore!

|Notebook|Open|
|:--|:--|
|Intro To Python|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/afyqazraei/IntroToPythonPERFUM/master?filepath=Intro_To_Python.ipynb)|

## For developers

# 1. Get a Linux terminal.

There are multiple ways to use a Linux terminal. First, using a proper Linux OS. Second, using a Virtual Machine. Third, if you are using Windows 10, use the Windows Linux Subsystem. Fourth, MacOS is already a proper UNIX terminal.

# 2. Install Anaconda (preferable) or Miniconda (a run-down version). Later, install Jupyter.

Follow the steps here:

https://docs.anaconda.com/anaconda/install/linux/

and here:

https://jupyter.org/install

Check your .bashrc file for the following script, if non-existant then paste it.

```bash
export DISPLAY=localhost:0.0

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/afyqazraei/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/afyqazraei/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/afyqazraei/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/afyqazraei/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

```

When done, source the file:

```
source .bashrc
```

# 3. Checkout the repository.

```bash
git clone git@github.com:afyqazraei/IntroToPythonPERFUM.git 
```

# 4. Launch the Jupyter Notebook.

```bash
jupyter-notebook IntroToPythonPERFUM/
```

When initialized, copy the localhost link and paste it in a web browser. Then, you are all set and ready to go!

## Developers

|Module|Developer|
|:--|:--|
|Intro To Python| Afiq Azraei |
| Project 1 | Harith Zulfaizal |
| Project 2 | Zaim Hakimie |
| Project 3 | Yao Feng |
