# DeltaH
The Webpage: https://justinp101234.wixsite.com/ethalpy

Data Sourcing:
Data was sourced from: https://www2.chem.wisc.edu/deptfiles/genchem/netorial/modules/thermodynamics/tableData.htm
![alt text](https://i.imgur.com/CsmDmtU.png)

The Data was converted into a dictionary format using python: toDict.py
![alt text](https://i.imgur.com/DZJWU2U.png)

The website was built using wix:

![alt text](https://i.imgur.com/rIqB3A3.png)

Key Parts of Coding: home.js

The main problem for creating this calculator involves data parsing

![alt text](https://i.imgur.com/Cv01nVy.png)

This formats the data so we now have reactionMolecules = ['H2(g)','.5O2(g)'] and productMolecules = ['H2O(l)']

We than have to parse the symbols to determine if they start with an XH2(g) number where X is we will do this using regex so we can capture multi digit and decimal numbers

![alt text](https://i.imgur.com/dgsXzZO.png)

Ehtalpy is than summed up using the value found in the dictionary:

![alt text](https://i.imgur.com/65YNyoj.png)

If Value Not Found:

![alt text](https://i.imgur.com/oYeIMyb.png)

The corresponding not found value is changed to UNDEFINED in the calculation bar

Fixing the issue, the issue is either a user error for not following the guidelines or the value is not in the table if so there is a function to add values to the table via:

![alt text](https://i.imgur.com/2JJ1ziM.png)

Integrating components with Wix:

Every component has an id that can be accessed

![alt text](https://i.imgur.com/AHLUq7g.png)

using $w("#ELEMENTID")

![alt text](https://i.imgur.com/O4oWHED.png)

With specific event handler functions that can be added to the script:

![alt text](https://i.imgur.com/N0Nk8Ez.png)





