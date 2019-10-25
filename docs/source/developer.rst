######################
**Developer Manual**
######################

*Software Requirements*
========================

The following softwares are needed to be installed:

* Python3

 * tkinter
 * openepyxl

* Sphinx

.. code-block:: python

    sudo apt-get install python3
    sudo apt-get install python3-tk
    pip install openepyxl

Sphinx installation in needed in case you want to work on the documentation

.. code-block:: python

    pip install sphinx

Note that to compile the changes made to the documentation you have to move to the docs folder and compile your changes

.. code-block:: python 

    cd docs/
    make html

The file will be changes in the *build/html* folder

For more information on working with sphinx you can refer: 
https://www.sphinx-doc.org/en/master/index.html

*Bug Reports and Feature Requests*
===================================

If you have encontered a problem with the application or have an idea for a new feature, please submit it as an issue tracker on Github.

After getting approval from a moderator, you may make a pull requests to the repository.

*Contributing on the Project*
===============================
The recommended way for new contributors to submit code to Sphinx is to fork the repository on GitHub and then submit a pull request after committing the changes. The pull request will then need to be approved by one of the core developers before it is merged into the main repository.

1. Clone the Repository
2. Working on any of the given modules:

 * GUI#1
 * GUI#2
 * Documentation

Clone the Repository
---------------------

These are the basic steps needed to start developing on the application.

1. Got to the given link
    https://github.com/PS-Ddevil/Time-table-assist-tool

2. Click on the fork option to make a copy of the repo on your profile

.. image:: img/Fork1.png
    :width: 80%
    :align: center

3. Go to a desired location on you local system(PC).
4. Open the terminal by pressing *Alt+Ctrl+T*
5. Run the command

.. code-block:: python

    git clone https://github.com/<git-username>/Time-table-assist-tool.git

Where <git-username> refers to the Username of your Github Profile

Working on GUI#1
-----------------
1. Move to the cloned the folder

    .. code-block:: python

        cd Time-table-assist-tool

2. Open the *prob1.py* file.

    Open the *prob1.py* file in any text editor of your choice

    For Sublime Editor:

    .. code-block:: python
        
        subl prob1.py

    For Atom Editor:

    .. code-block:: python
        
        atom prob1.py

    For Visual Studio Code:

    .. code-block:: python
        
        code prob1.py

3. There are three broad sections in the code 

 * GUI Development 
 * Slot management algorithm section
 * Slot rendering section

SECTION 1:

.. code-block:: python
    
    # DEFINING THE GUI ELEMENTS
    Label(master, text='').grid(row=0)
    Label(master, text='8:00 - 8:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=1)
    Label(master, text='9:00 - 9:50',border......

SECTION 2:

.. code-block:: python

    # THIS SECTION DEFINES THE ALGORITHM TO UPDATE THE OPTIONS IN THE GUI
    def update_options(var, row_val):
        cr = cr_vars[var].get()
        if(old_var[var] == cr):
            return 0
        if match[row_val][ord(cr)-65] == True:
            cr_vars[var].set("SLOT")
            messagebox.showerror("Erro....

SECTION 3:

.. code-block:: python

    # THIS SECTION DEFINES THE RENDERING OF THE SLOTS IN THE GUI'S TIMETABLE MATRIX
    for i in range(1,6):
        for j in range(1,10):
            cr_vars.append(StringVar(master))
            cr_vars[z].set("SLOT")
            old_var.append("SLOT")
            left_course = ['A', 'B'...

4. Modify the code accordingly and commit changes when necessary.

Working on GUI#2
-----------------
1. Move to the cloned the folder

    .. code-block:: python

        cd Time-table-assist-tool

2. Open the *prob1.py* file.

    Open the *prob1.py* file in any text editor of your choice

    For Sublime Editor:

    .. code-block:: python
        
        subl prob1.py

    For Atom Editor:

    .. code-block:: python
        
        atom prob1.py

    For Visual Studio Code:

    .. code-block:: python
        
        code prob1.py

3. There are Three broad section for the GUI#2

 * DropDown Function
 * ConstraintCheck Function
 * Display GUI
 * DialogBOX 

SECTION 1:

.. code-block:: python

    def DropDown():
        global lists,v
        v.set("Select File")
        w = OptionMenu(frame1, v, *lists)
        w.grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
        w.config(width=45)
        v.trace("w", DisplayGUI)

SECTION 2:

.. code-block:: python

    def ConstraintCheck(var,i,name,focus,*args):
        global file_path
        wb = openpyxl.load_workbook(str(os.path.join(file_path, v.get())))
        ws = wb.active
        j=0
        for j in range(2,ws.max_row+1):
            c1=ws.cell(j,5)
            if i==j:
                continue
            if c1.value==var.get():
                messagebox.showerror("Err...

SECTION 3:

.. code-block:: python

    def DisplayGUI(*args):
        global file_path
        for widget in frame2.winfo_children():
            widget.destroy()
        wb = openpyxl.load_workbook(str(os.path.join(file_path, v.get())))
        ws = wb.active
        slots=['Slot A','Slot B','Slot C','Slo...

SECTION 4:

.. code-block:: python

    def DialogBox():
       global file_path
       file_path=filedialog.askdirectory()
       global lists, v
       a=str(os.path.join(file_path, "track.xlsx"))
       wb = openpyxl.load_workb....

4. Include the required packages in the top of the file

.. code-block:: python

    # Include your packages here
    from tkinter import *
    from tkinter import messagebox
    import os
    import openpyxl
    from tkinter import filedialog

*Core Developers*
==================

The core developers of the application have write access to the main repository. They can commit changes, accept/reject pull requests, and manage items on the issue tracker.

You do not need to be a core developer or have write access to be involved in the development of the application. You can submit patches or create pull requests from forked repositories and have a core developer add the changes for you.

The following are some general guidelines for core developers:

    * Questionable or extensive changes should be submitted as a pull request instead of being committed directly to the main repository. The pull request should be reviewed by another core developer before it is merged.

    * Trivial changes can be committed directly but be sure to keep the repository in a good working state and that all tests pass before pushing your changes.

    * When committing code written by someone else, please attribute the original author in the commit message and any relevant CHANGES entry.


*Brach Model*
==============

The branch are made when a new major portion is added into the application. Only minor changes and bug removal in the branch would be appretiated.

Conventions
------------

master:
^^^^^^^^

The is the most recent branch and the one which is currently deployed for the consumer.

X.Y:
^^^^^

Where X.Y stands for the MAJOR.MINOR release. 

X.Y.Z: 
^^^^^^^

Where X.Y.Z stands for MAJOR.MINOR.PATCH release.