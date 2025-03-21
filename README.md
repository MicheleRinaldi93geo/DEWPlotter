## DEWPlotter

## Info
Script author: ENKI  
Library author: Michele Rinaldi  
Contacts:rinaldim@tcd.ie  

**DEWPlotter** is a Python package for plotting data from EQ6 package of the Deep Earth 
Water Model (http://www.dewcommunity.org). It contains an executable that runs in the same 
way as EQ6 (i.e., ./DEWPlotter) and a python library to be used into a python routine.  



### Installation

You can just download the executable to use it. You'll find it into the zip file attached 
to the release. No further work is needed.  

To install the python version through your terminal:  
1) Install Python: https://www.python.org and https://realpython.com/installing-python/.  
2) Instal pip: https://packaging.python.org/en/latest/tutorials/installing-packages/.  
3) Install DEWPlotter: pip install git+https://github.com/MicheleRinaldi93geo/DEWPlotter.git  



### To run

Place the executable into the folder with your output files. Then, run it with ./DEWPlotter    

The python version requires the library to be imported first, and then you can run the only
function available [.analise(directory of the folder with the output files).] 
See the example among the files provided.  



### Mandatory files

All the output files from the EQ6 package must be there (output, tab, tabx)



### Notes

Please not that the library is not fully automated, and it may not find all the aqueous species
in the output file. If you spot a non-analysed species, please send me an email and I'll add it
to the library.

### Logfile
v 1.0.0 - Library created
v 1.1.0 - Fixed problem with PSAT