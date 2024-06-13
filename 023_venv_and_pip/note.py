# pip: preffred installer program (pip installe packages) like npm -> global install by default, update package globally!!!

# install certain version: pip install requests==2.30.0 (try pp3, python3 -m pip...)
# update: python3 -m pip install -U requests(newset version)
# uninstall: python3 -m pip uninstall requests 
# check list of package installed    python3 -m pip list   (give every package installed in machine)


# venv: python virtual environment (since pip install package globally, virtual envirment will create a seperate enviroment for diferent version of package) 
# py -m venv .venv (create a virtual environment 'folder')
# source .venv/bin/activate   (activate virtual environment) -> it will end with (.venv) at terminal (run this everytime want enter this project)
# after it activate, global package are gone, can run (pip list) instead of (python3 -m pip list), same as other commands( pip install ...)

# deactivate : deactivate  (deactivate virtual enviroment)
# show detail of a package    python3 -m pip show requests

### check packages availiable (like node package manager web): pypi.org

# create a text file list all packages required():  python3 -m pip freeze > requirements.txt
# create .gitignore and list .venv in .gitignore -> so .venv wont upload to github
#################  .venv is like _module folder, requirement.txt it's like package.json  ####################