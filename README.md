# Introduction To Python

## For students

Hi, everyone!

For those of you who are new to all this, welcome to GitHub! GitHub is a place where people, sometimes from all corners of the world, come together and collaborate on programming projects. Here in this repository, are Jupyter Notebooks that can be launched through Binder. All of this is open source, and can be accessible almost anywhere, anytime. 

### Jupyter Notebooks

The Notebooks will give you a brief tutorial into Python, designed for physics undergrads that have little to no experience in programming. Just press the Binder link and let it launch. Learn, enjoy, explore!

|Notebook|Open|Contributor|
|:--|:--|:--|
|Intro To Python|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/afyqazraei/IntroToPythonPERFUM/master?filepath=Intro_To_Python.ipynb)|Afiq Azraei|
|Basketball Shot Kinematics|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/afyqazraei/IntroToPythonPERFUM/master?filepath=BasketballKinematics.ipynb)|Zaim Hakimie|
|Random Walk|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/afyqazraei/IntroToPythonPERFUM/master?filepath=RandomWalk.ipynb)|Harith Zulfaizal|
|Simple Harmonic Motion|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/afyqazraei/IntroToPythonPERFUM/master?filepath=SHM.ipynb)|Yao Feng|

### Python Code Camp

Some of the notes from the previous Python Code Camp are available in the CodeCampNotes directory. They offer more details on the stuff you learnt in the Jupyter Notebooks.

## For contributors

### 1. Get a Linux terminal.

One can either use a proper UNIX machine, a dual boot for a Linux OS, a virtual machine or even the Windows Linux subsystem built into Windows 10. Find one that suits your needs.

### 2. Install Anaconda (preferable) or Miniconda (a run-down version). Later, install Jupyter.

Follow the steps here:

https://docs.anaconda.com/anaconda/install/linux/

and here:

https://jupyter.org/install

Check your .bashrc file for the following script, if non-existent then paste this:

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

### 3. Checkout the repository.

```bash
git clone git@github.com:afyqazraei/IntroToPythonPERFUM.git 
```

### 4. Launch the Jupyter Notebook.

```bash
jupyter-notebook IntroToPythonPERFUM/
```

When initialized, copy the localhost link and paste it in a web browser. Then, you are all set and ready to go!

