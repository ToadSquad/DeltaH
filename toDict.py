from bs4 import BeautifulSoup
import requests
import re

#HTML SOURCE IS https://www2.chem.wisc.edu/deptfiles/genchem/netorial/modules/thermodynamics/tableData.htm
html = '''<html><head>
<title></title>
<link href="../../stylesheets/biostyles.css" rel="stylesheet" type="text/css">
</head>
<body data-new-gr-c-s-check-loaded="14.1026.0" data-gr-ext-installed="">
<table border="" cellspacing="1" cellpadding="3" width="417">
<tbody><tr><td width="21%" valign="TOP" height="20">
Aluminum</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Al(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">28.3</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
AlCl<sub>3</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-704.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">110.67</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-628.8</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Al<sub>2</sub>O<sub>3</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1675.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">50.92</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1582.3</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Aqueous Solutions</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Ca<sup>2+</sup>(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-542.96</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">-55.2</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-553.04</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CO<sub>3</sub><sup>2-</sup>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-676.26</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">-53.1</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-528.1</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CO<sub>2</sub>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-413.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">117.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-386.0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Cl<sup>-</sup>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-167.16</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">56.5</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-131.26</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
H<sup>+</sup>(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
HCO<sub>2</sub><sup>-</sup>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-410</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">91.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-335</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
HCO<sub>2</sub>H(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-410</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">164</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-356</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
HCO<sub>3</sub><sup>-</sup>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-691.11</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">95</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-587.06</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
H<sub>2</sub>CO<sub>3</sub>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-698.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">191</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-623.42</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NH<sub>3</sub>(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-80.29</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">111</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-26.6</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
OH<sup>-</sup>(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-229.94</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">-10.54</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-157.3</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Ag<sup>-</sup>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">105.58</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">72.68</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">77.124</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Barium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
BaCl<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-858.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">123.68</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-810.4</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
BaCl<sub>2</sub> • 2 H<sub>2</sub>O (s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1460.1</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">203</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1296.5</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
BaO(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-553.5</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">70.42</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-525.1</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Ba(OH)<sub>2</sub> • 8 H<sub>2</sub>O (s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-3342</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">427</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-2793</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
BaSO<sub>4</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1473.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">132.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1362.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Beryllium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Be(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">9.5</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Be(OH)<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-902.5</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">51.9</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-815</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Bromine</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Br(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">111.884</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">175.022</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">82.396</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Br<sub>2</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">152.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Br<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">30.907</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">245.463</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">3.11</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
BrF<sub>3</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-255.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">292.53</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-229.43</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
HBr(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-36.4</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">198.695</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-53.45</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Calcium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Ca(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">41.42</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Ca(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">178.2</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">158.884</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">144.3</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Ca<sup>2+</sup>(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">1925.9</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CaC<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-59.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">69.96</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-64.9</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CaCO<sub>3
</sub>(s; calcite)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1206.92</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">92.9</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1128.79</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CaCl<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-795.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">104.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-748.1</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CaF<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1219.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">68.87</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1167.3</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CaH<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-186.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">42</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-147.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
CaO(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-635.09</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">39.75</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-604.03</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
CaS(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-482.4</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">56.5</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-477.4</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Ca(OH)<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-986.09</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">83.39</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-898.49</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Ca(OH)<sub>2</sub>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1002.82</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">-74.5</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-868.07</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CaSO<sub>4</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1434.11</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">106.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1321.79</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Carbon</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
C(s, graphite)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">5.74</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
C(s, diamond)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">1.895</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">2.377</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">2.9</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
C(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">716.682</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">158.096</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">671.257</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CCl<sub>4</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-135.44</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">216.4</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-65.21</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CCl<sub>4</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-102.9</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">309.85</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-60.59</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CHCl<sub>3</sub>(liq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-134.47</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">201.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-73.66</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CHCl<sub>3</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-103.14</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">295.71</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-70.34</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CH<sub>4
</sub>(g, methane)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-74.81</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">186.264</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-50.72</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>2</sub>H<sub>2
</sub>(g, ethyne)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">226.73</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">200.94</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">209.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>2</sub>H<sub>4
</sub>(g,ethene)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">52.26</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">219.56</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">68.15</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>2</sub>H<sub>6
</sub>(g, ethane)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-84.68</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">229.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-32.82</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>3</sub>H<sub>8
</sub>(g, propane)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-103.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">269.9</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-23.49</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>4</sub>H<sub>10
</sub>(g, butane)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-888.0</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">&nbsp;</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">&nbsp;</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>6</sub>H<sub>6
</sub>(<font face="MT Extra">l</font>, benzene)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">49.03</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">172.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">124.5</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>6</sub>H<sub>14</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-198.782</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">296.018</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-4.035</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>8</sub>H<sub>18</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-249.952</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">361.205</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">6.707</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CH<sub>3</sub>OH(<font face="MT Extra">l</font>, methanol)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-238.66</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">126.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-166.27</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CH<sub>3</sub>OH(g, methanol)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-200.66</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">239.81</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-161.96</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>2</sub>H<sub>5</sub>OH(<font face="MT Extra">l</font>, ethanol)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-277.69</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">160.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-174.78</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
C<sub>2</sub>H<sub>5</sub>OH(g, ethanol)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-235.1</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">282.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-168.49</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CH<sub>3</sub>COOH(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-276.981</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">160.666</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-173.991</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CO(NH<sub>2</sub>)<sub>2</sub>(s, urea)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-333.5</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">104.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-197.4</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
CO(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-110.525</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">197.674</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-137.168</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CO<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-393.509</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">213.74</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-394.359</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CS<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">117.36</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">237.84</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">67.12</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
COCl<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-218.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">283.53</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-204.6</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Cesium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Cs(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">85.23</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Cs<sup>+</sup>(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">457.964</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
CsCl(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-443.04</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">101.17</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-414.53</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Chlorine</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Cl(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">121.679</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">165.198</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">105.68</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Cl<sup>-</sup>(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-233.13</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Cl<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">223.066</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
HCl(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-92.307</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">186.908</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-95.299</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
HCl(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-167.159</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">56.5</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-131.228</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Chromium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Cr(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">23.77</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Cr<sub>2</sub>O<sub>3</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1139.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">81.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1058.1</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CrCl<sub>3</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-556.5</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">123</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-486.1</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Copper</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Cu(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">33.15</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
CuO(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-157.3</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">42.63</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-129.7</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
CuCl<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-220.1</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">108.07</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-175.7</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Fluorine</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
F<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">202.78</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
F(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">78.99</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">158.754</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">61.91</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
F<sup>-</sup>(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-255.39</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
F<sup>-</sup>(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-332.63</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">-13.8</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-278.79</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
HF(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-271.1</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">173.779</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-273.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
HF(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-332.63</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">-13.8</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-278.79</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Hydrogen</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
H<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">130.684</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
H(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">217.965</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">114.713</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">203.247</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
H<sup>+</sup>(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">1536.202</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
H<sub>2</sub>O(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-285.83</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">69.91</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-237.129</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
H<sub>2</sub>O(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-241.818</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">188.825</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-228.572</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
H<sub>2</sub>O<sub>2</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-187.78</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">109.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-120.35</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Iodine</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
I<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">116.135</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
I<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">62.438</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">260.69</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">19.327</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
I(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">106.838</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">180.791</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">70.25</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
I<sup>-</sup>(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-197</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
ICl(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">17.78</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">247.551</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-5.46</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Iron</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Fe(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">27.78</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
FeO(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-272</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Fe<sub>2</sub>O<sub>3</sub>(s, hematite)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-824.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">87.4</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-742.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Fe<sub>3</sub>O<sub>4</sub>(s, magnetite)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1118.4</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">146.4</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1015.4</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
FeCl<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-341.79</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">117.95</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-302.3</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
FeCl<sub>3</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-399.49</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">142.3</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-344</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
FeS<sub>2</sub>(s, pyrite)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-178.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">52.93</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-166.9</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Fe(CO)<sub>5</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-774</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">338.1</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-705.3</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Lead</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Pb(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">64.81</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
PbCl<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-359.41</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">136</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-314.1</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
PbO(s, yellow)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-217.32</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">68.7</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-187.89</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
PbS(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-100.4</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">91.2</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-98.7</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Lithium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Li(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">29.12</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Li<sup>+</sup>(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">685.783</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
LiOH(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-484.93</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">42.8</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-438.95</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
LiOH(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-508.48</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">2.8</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-450.58</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
LiCl(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-408.701</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">59.33</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-384.37</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Magnesium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Mg(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">32.68</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
MgCl<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-641.32</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">89.62</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-591.79</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
MgO(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-601.7</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">26.94</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-569.43</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Mg(OH)<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-924.54</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">63.18</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-833.51</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
MgS(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-346</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">50.33</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-341.8</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Mercury</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Hg(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">29.87</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
HgCl<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-224.3</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">146</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-178.6</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
HgO(s, red)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-90.83</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">70.29</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-58.539</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
HgS(s, red)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-58.2</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">82.4</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-50.6</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Nickel</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Ni(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">29.87</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NiO(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-239.7</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">37.99</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-211.7</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
NiCl<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-305.332</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">97.65</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-259.032</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Nitrogen</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
N<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">191.61</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
N(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">472.704</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">153.298</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">455.563</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
NH<sub>3</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-46.11</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">192.45</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-16.45</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
N<sub>2</sub>H<sub>4</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">50.63</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">121.21</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">149.34</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
NH<sub>4</sub>Cl(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-314.43</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">94.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-202.87</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
NH<sub>4</sub>Cl(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-299.66</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">169.9</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-210.52</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
NH<sub>4</sub>NO<sub>3</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-365.56</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">151.08</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-183.87</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
NH<sub>4</sub>NO<sub>3</sub>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-339.87</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">259.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-190.56</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NO(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">90.25</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">210.76</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">86.55</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
NO<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">33.18</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">240.06</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">51.31</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
N<sub>2</sub>O(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">82.05</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">219.85</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">104.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
N<sub>2</sub>O<sub>4</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">9.16</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">304.29</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">97.89</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NOCl(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">51.71</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">261.69</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">66.08</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
HNO<sub>3</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-174.1</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">155.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-80.71</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
HNO<sub>3</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-135.06</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">266.38</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-74.72</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
HNO<sub>3</sub>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-207.36</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">146.4</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-111.25</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Oxygen</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
O<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">205.138</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
O(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">249.17</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">161.055</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">231.731</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
O<sub>3</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">142.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">238.93</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">163.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Phosphorus</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
P<sub>4</sub>(s, white)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">164.36</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
P<sub>4</sub>(s, red)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-70.4</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">91.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-48.4</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
P(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">314.64</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">163.193</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">278.25</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
PH<sub>3</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">5.4</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">310.23</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">13.4</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
PCl<sub>3</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-287</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">311.78</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-267.8</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
P<sub>4</sub>O<sub>10</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-2984</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">228.86</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-2697.7</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
H<sub>3</sub>PO<sub>4</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1279</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">110.5</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1119.1</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Potassium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
K(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">64.18</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
KCl(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-436.747</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">82.59</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-409.14</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
KClO<sub>3</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-397.73</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">143.1</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-296.25</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
KI(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-327.9</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">106.32</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-324.892</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
KOH(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-424.764</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">78.9</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-379.08</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
KOH(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-482.37</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">91.6</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-440.5</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Silicon</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Si(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">18.83</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SiBr<sub>4</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-457.3</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">277.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-443.8</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
SiC(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-65.3</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">16.61</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-62.8</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SiCl<sub>4</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-657.01</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">330.73</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-616.98</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SiH<sub>4</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">34.3</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">204.62</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">56.9</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SiF<sub>4</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1614.94</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">282.49</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1572.65</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SiO<sub>2</sub>(s, quartz)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-910.94</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">41.84</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-856.64</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Silver</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Ag(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">42.55</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Ag<sub>2</sub>O(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-31.05</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">121.3</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-11.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
AgCl(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-127.068</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">96.2</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-109.789</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
AgNO<sub>3</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-124.39</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">140.92</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-33.41</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Sodium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Na(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">51.21</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Na(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">107.32</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">153.712</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">76.761</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Na<sup>+</sup>(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">609.358</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NaBr(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-361.062</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">86.82</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-348.983</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NaCl(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-411.153</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">72.13</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-384.138</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NaCl(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-176.65</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">229.81</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-196.66</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NaCl(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-407.27</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">115.5</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-393.133</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NaOH(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-425.609</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">64.455</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-379.484</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
NaOH(aq)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-470.114</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">48.1</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-419.15</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
Na<sub>2</sub>CO<sub>3</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-1130.68</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">134.98</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1044.44</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Sulfur</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
S(s, rhombic)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">31.8</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
S(g)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">278.805</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">167.821</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">238.25</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
S<sub>2</sub>Cl<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-18.4</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">331.5</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-31.8</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SF<sub>6</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">1209</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">291.82</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-1105.3</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
H<sub>2</sub>S(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-20.63</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">205.79</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-33.56</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SO<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-296.83</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">248.22</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-300.194</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SO<sub>3</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-395.72</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">256.76</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-371.06</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SOCl<sub>2</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-212.5</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">309.77</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-198.3</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
H<sub>2</sub>SO<sub>4</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-813.989</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">156.904</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-690.003</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
H<sub>2</sub>SO<sub>4</sub>(aq)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-909.27</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">20.1</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-744.53</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Tin</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Sn(s, white)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">51.55</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Sn(s, gray)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-2.09</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">44.14</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0.13</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SnCl<sub>4</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-511.3</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">248.6</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-440.1</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SnCl<sub>4</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-471.5</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">365.8</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-432.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
SnO<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-580.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">52.3</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-519.6</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Titanium</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Ti(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">30.63</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
TiCl<sub>4</sub>(<font face="MT Extra">l</font>)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-804.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">252.34</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-737.2</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
TiCl<sub>4</sub>(g)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-763.2</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">354.9</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-726.7</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
TiO<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-939.7</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">49.92</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-884.5</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20">
Zinc</td>
<td width="27%" valign="TOP" height="20">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">&nbsp;</td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">&nbsp;</td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
Zn(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">0</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">41.63</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">0</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="22"></td>
<td width="27%" valign="TOP" height="22">
ZnCl<sub>2</sub>(s)</td>
<td width="17%" valign="TOP" height="22" bgcolor="F7BDDE">
<p align="RIGHT">-415.05</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6B5DE">
<p align="RIGHT">111.46</p></td>
<td width="17%" valign="TOP" height="22" bgcolor="C6EFF7">
<p align="RIGHT">-369.398</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
ZnO(s)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-348.28</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">43.64</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-318.3</p></td>
</tr>
<tr><td width="21%" valign="TOP" height="20"></td>
<td width="27%" valign="TOP" height="20">
ZnS(s, sphalerite)</td>
<td width="17%" valign="TOP" height="20" bgcolor="F7BDDE">
<p align="RIGHT">-205.98</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6B5DE">
<p align="RIGHT">57.7</p></td>
<td width="17%" valign="TOP" height="20" bgcolor="C6EFF7">
<p align="RIGHT">-201.29</p></td>
</tr>
<tr><td valign="TOP" colspan="5" height="17">
<font size="2">*Taken from "The NBS Tables of Chemical Thermodynamic Properties" (1982) and "CRC Handbook of Chemistry and Physics", 1st Student Edition (1988)</font></td>
</tr>
</tbody></table>


</body><grammarly-desktop-integration data-grammarly-shadow-root="true"></grammarly-desktop-integration></html>'''

#print(html.text)

soup = BeautifulSoup(html, 'html.parser')

res = soup.findAll('tr')

ethalpy = {}

counter = 0
symbol = ""
for result in res:
    try:
        text = result.text
        text = text.replace('\n','')
        data = text.split(')')
        if(data[1][0]=="0"):
            number = '0'
            ethalpy[data[0]+')'] = float(number)
        else:
            number = data[1].split('.')
            ethalpy[data[0]+')'] = float(number[0] + '.' + number[1][0])
        
    except:
        print('not write column')

print(ethalpy)


'''try:
        if(type(ethalpy[symbol])=="float"):
            continue
    except:
        print()
    try:
        ethalpy[symbol] = float(text)
    except:
        symbol = text'''