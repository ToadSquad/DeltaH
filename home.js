// API Reference: https://www.wix.com/velo/reference/api-overview/introduction
// “Hello, World!” Example: https://learn-code.wix.com/en/article/1-hello-world
var dictOrginal = {'Al(s)': 0.0, 'AlCl3(s)': -704.2, 'Al2O3(s)': -1675.7, 'Ca2+(aq)': -542.9, 'CO32-(aq)': -676.2, 'CO2(aq)': -413.8, 'Cl-(aq)': -167.1, 'H+(aq)': 0.0, 'HCO2-(aq)': -41091.6, 'HCO3-(aq)': -691.1, 'H2CO3(aq)': -698.7, 'NH3(aq)': -80.2, 'OH-(aq)': -229.9, 'Ag-(aq)': 105.5, 'BaCl2(s)': -858.6, 'BaCl2 • 2 H2O (s)': -1460.1, 'BaO(s)': -553.5, 'BaSO4(s)': -1473.2, 'Be(s)': 0.0, 'Br(g)': 111.8, 'Br2(l)': 0.0, 'Br2(g)': 30.9, 'BrF3(g)': -255.6, 'HBr(g)': -36.4, 'Ca(s)': 0.0, 'Ca(g)': 178.2, 'Ca2+(g)': 1925.9, 'CaC2(s)': -59.8, 'CaCO3(s; calcite)': -1206.9, 'CaCl2(s)': -795.8, 'CaF2(s)': -1219.6, 'CaH2(s)': -186.2, 'CaO(s)': -635.0, 'CaS(s)': -482.4, 'CaSO4(s)': -1434.1, 
'C(s, graphite)': 0.0, 'C(s, diamond)': 1.8, 'C(g)': 716.6, 'CCl4(l)': -135.4, 'CCl4(g)': -102.9, 'CHCl3(liq)': -134.4, 'CHCl3(g)': -103.1, 'CH4(g, methane)': -74.8, 'C2H2(g, ethyne)': 226.7, 'C2H4(g,ethene)': 52.2, 'C2H6(g, ethane)': -84.6, 'C3H8(g, propane)': -103.8, 'C4H10(g, butane)': -888.0, 'C6H6(l, benzene)': 49.0, 'C6H14(l)': -198.7, 'C8H18(l)': -249.9, 'CH3OH(l, methanol)': -238.6, 'CH3OH(g, methanol)': -200.6, 'C2H5OH(l, ethanol)': 
-277.6, 'C2H5OH(g, ethanol)': -235.1, 'CH3COOH(l)': -276.9, 'CO(g)': -110.5, 'CO2(g)': -393.5, 'CS2(g)': 117.3, 'COCl2(g)': -218.8, 'Cs(s)': 0.0, 'Cs+(g)': 457.9, 'CsCl(s)': -443.0, 'Cl(g)': 121.6, 'Cl-(g)': -233.1, 'Cl2(g)': 0.0, 'HCl(g)': -92.3, 'HCl(aq)': -167.1, 'Cr(s)': 0.0, 'Cr2O3(s)': -1139.7, 'CrCl3(s)': -556.5, 'Cu(s)': 0.0, 'CuO(s)': -157.3, 'CuCl2(s)': -220.1, 'F2(g)': 0.0, 'F(g)': 78.9, 'F-(g)': -255.3, 'F-(aq)': -332.6, 'HF(g)': 
-271.1, 'HF(aq)': -332.6, 'H2(g)': 0.0, 'H(g)': 217.9, 'H+(g)': 1536.2, 'H2O(l)': -285.8, 'H2O(g)': -241.8, 'H2O2(l)': -187.7, 'I2(s)': 0.0, 'I2(g)': 62.4, 'I(g)': 106.8, 'ICl(g)': 17.7, 'Fe(s)': 0.0, 'Fe2O3(s, hematite)': 
-824.2, 'Fe3O4(s, magnetite)': -1118.4, 'FeCl2(s)': -341.7, 'FeCl3(s)': -399.4, 'FeS2(s, pyrite)': -178.2, 'Pb(s)': 0.0, 'PbCl2(s)': -359.4, 'PbO(s, yellow)': -217.3, 'PbS(s)': -100.4, 'Li(s)': 0.0, 'Li+(g)': 685.7, 'LiOH(s)': -484.9, 'LiOH(aq)': -508.4, 'LiCl(s)': -408.7, 'Mg(s)': 0.0, 'MgCl2(g)': -641.3, 'MgO(s)': -601.7, 'MgS(s)': -34650.3, 'Hg(l)': 0.0, 'HgCl2(s)': -224.3, 'HgO(s, red)': -90.8, 'HgS(s, red)': -58.2, 'Ni(s)': 0.0, 'NiO(s)': -239.7, 'NiCl2(s)': -305.3, 'N2(g)': 0.0, 'N(g)': 472.7, 'NH3(g)': -46.1, 'N2H4(l)': 50.6, 'NH4Cl(s)': -314.4, 'NH4Cl(aq)': -299.6, 'NH4NO3(s)': -365.5, 'NH4NO3(aq)': -339.8, 'NO(g)': 90.2, 'NO2(g)': 33.1, 'N2O(g)': 82.0, 'N2O4(g)': 9.1, 'NOCl(g)': 51.7, 'HNO3(l)': -174.1, 'HNO3(g)': -135.0, 'HNO3(aq)': -207.3, 'O2(g)': 0.0, 'O(g)': 249.1, 'O3(g)': 142.7, 'P4(s, white)': 0.0, 'P4(s, red)': -70.4, 'P(g)': 314.6, 'PH3(g)': 5.4, 'PCl3(g)': -287311.7, 'P4O10(s)': -2984228.8, 'H3PO4(s)': -1279110.5, 'K(s)': 0.0, 'KCl(s)': -436.7, 'KClO3(s)': -397.7, 'KI(s)': -327.9, 'KOH(s)': -424.7, 'KOH(aq)': -482.3, 'Si(s)': 0.0, 'SiBr4(l)': -457.3, 'SiC(s)': -65.3, 'SiCl4(g)': -657.0, 'SiH4(g)': 34.3, 'SiF4(g)': -1614.9, 'SiO2(s, quartz)': -910.9, 'Ag(s)': 0.0, 'Ag2O(s)': -31.0, 'AgCl(s)': -127.0, 'AgNO3(s)': -124.3, 'Na(s)': 0.0, 'Na(g)': 107.3, 'Na+(g)': 609.3, 'NaBr(s)': -361.0, 'NaCl(s)': -411.1, 'NaCl(g)': -176.6, 'NaCl(aq)': -407.2, 'NaOH(s)': -425.6, 'NaOH(aq)': -470.1, 'Na2CO3(s)': -1130.6, 'S(s, rhombic)': 0.0, 'S(g)': 278.8, 'S2Cl2(g)': -18.4, 'SF6(g)': 1209291.8, 'H2S(g)': -20.6, 'SO2(g)': -296.8, 'SO3(g)': -395.7, 'SOCl2(g)': -212.5, 'H2SO4(l)': -813.9, 'H2SO4(aq)': -909.2, 'Sn(s, white)': 0.0, 'Sn(s, gray)': -2.0, 'SnCl4(l)': -511.3, 'SnCl4(g)': -471.5, 'SnO2(s)': -580.7, 'Ti(s)': 0.0, 'TiCl4(l)': -804.2, 'TiCl4(g)': -763.2, 'TiO2(s)': -939.7, 'Zn(s)': 0.0, 'ZnCl2(s)': -415.0, 'ZnO(s)': -348.2, 'ZnS(s, sphalerite)': -205.9}
var dict = {'Al(s)': 0.0, 'AlCl3(s)': -704.2, 'Al2O3(s)': -1675.7, 'Ca2+(aq)': -542.9, 'CO32-(aq)': -676.2, 'CO2(aq)': -413.8, 'Cl-(aq)': -167.1, 'H+(aq)': 0.0, 'HCO2-(aq)': -41091.6, 'HCO3-(aq)': -691.1, 'H2CO3(aq)': -698.7, 'NH3(aq)': -80.2, 'OH-(aq)': -229.9, 'Ag-(aq)': 105.5, 'BaCl2(s)': -858.6, 'BaCl2 • 2 H2O (s)': -1460.1, 'BaO(s)': -553.5, 'BaSO4(s)': -1473.2, 'Be(s)': 0.0, 'Br(g)': 111.8, 'Br2(l)': 0.0, 'Br2(g)': 30.9, 'BrF3(g)': -255.6, 'HBr(g)': -36.4, 'Ca(s)': 0.0, 'Ca(g)': 178.2, 'Ca2+(g)': 1925.9, 'CaC2(s)': -59.8, 'CaCO3(s; calcite)': -1206.9, 'CaCl2(s)': -795.8, 'CaF2(s)': -1219.6, 'CaH2(s)': -186.2, 'CaO(s)': -635.0, 'CaS(s)': -482.4, 'CaSO4(s)': -1434.1, 
'C(s, graphite)': 0.0, 'C(s, diamond)': 1.8, 'C(g)': 716.6, 'CCl4(l)': -135.4, 'CCl4(g)': -102.9, 'CHCl3(liq)': -134.4, 'CHCl3(g)': -103.1, 'CH4(g, methane)': -74.8, 'C2H2(g, ethyne)': 226.7, 'C2H4(g,ethene)': 52.2, 'C2H6(g, ethane)': -84.6, 'C3H8(g, propane)': -103.8, 'C4H10(g, butane)': -888.0, 'C6H6(l, benzene)': 49.0, 'C6H14(l)': -198.7, 'C8H18(l)': -249.9, 'CH3OH(l, methanol)': -238.6, 'CH3OH(g, methanol)': -200.6, 'C2H5OH(l, ethanol)': 
-277.6, 'C2H5OH(g, ethanol)': -235.1, 'CH3COOH(l)': -276.9, 'CO(g)': -110.5, 'CO2(g)': -393.5, 'CS2(g)': 117.3, 'COCl2(g)': -218.8, 'Cs(s)': 0.0, 'Cs+(g)': 457.9, 'CsCl(s)': -443.0, 'Cl(g)': 121.6, 'Cl-(g)': -233.1, 'Cl2(g)': 0.0, 'HCl(g)': -92.3, 'HCl(aq)': -167.1, 'Cr(s)': 0.0, 'Cr2O3(s)': -1139.7, 'CrCl3(s)': -556.5, 'Cu(s)': 0.0, 'CuO(s)': -157.3, 'CuCl2(s)': -220.1, 'F2(g)': 0.0, 'F(g)': 78.9, 'F-(g)': -255.3, 'F-(aq)': -332.6, 'HF(g)': 
-271.1, 'HF(aq)': -332.6, 'H2(g)': 0.0, 'H(g)': 217.9, 'H+(g)': 1536.2, 'H2O(l)': -285.8, 'H2O(g)': -241.8, 'H2O2(l)': -187.7, 'I2(s)': 0.0, 'I2(g)': 62.4, 'I(g)': 106.8, 'ICl(g)': 17.7, 'Fe(s)': 0.0, 'Fe2O3(s, hematite)': 
-824.2, 'Fe3O4(s, magnetite)': -1118.4, 'FeCl2(s)': -341.7, 'FeCl3(s)': -399.4, 'FeS2(s, pyrite)': -178.2, 'Pb(s)': 0.0, 'PbCl2(s)': -359.4, 'PbO(s, yellow)': -217.3, 'PbS(s)': -100.4, 'Li(s)': 0.0, 'Li+(g)': 685.7, 'LiOH(s)': -484.9, 'LiOH(aq)': -508.4, 'LiCl(s)': -408.7, 'Mg(s)': 0.0, 'MgCl2(g)': -641.3, 'MgO(s)': -601.7, 'MgS(s)': -34650.3, 'Hg(l)': 0.0, 'HgCl2(s)': -224.3, 'HgO(s, red)': -90.8, 'HgS(s, red)': -58.2, 'Ni(s)': 0.0, 'NiO(s)': -239.7, 'NiCl2(s)': -305.3, 'N2(g)': 0.0, 'N(g)': 472.7, 'NH3(g)': -46.1, 'N2H4(l)': 50.6, 'NH4Cl(s)': -314.4, 'NH4Cl(aq)': -299.6, 'NH4NO3(s)': -365.5, 'NH4NO3(aq)': -339.8, 'NO(g)': 90.2, 'NO2(g)': 33.1, 'N2O(g)': 82.0, 'N2O4(g)': 9.1, 'NOCl(g)': 51.7, 'HNO3(l)': -174.1, 'HNO3(g)': -135.0, 'HNO3(aq)': -207.3, 'O2(g)': 0.0, 'O(g)': 249.1, 'O3(g)': 142.7, 'P4(s, white)': 0.0, 'P4(s, red)': -70.4, 'P(g)': 314.6, 'PH3(g)': 5.4, 'PCl3(g)': -287311.7, 'P4O10(s)': -2984228.8, 'H3PO4(s)': -1279110.5, 'K(s)': 0.0, 'KCl(s)': -436.7, 'KClO3(s)': -397.7, 'KI(s)': -327.9, 'KOH(s)': -424.7, 'KOH(aq)': -482.3, 'Si(s)': 0.0, 'SiBr4(l)': -457.3, 'SiC(s)': -65.3, 'SiCl4(g)': -657.0, 'SiH4(g)': 34.3, 'SiF4(g)': -1614.9, 'SiO2(s, quartz)': -910.9, 'Ag(s)': 0.0, 'Ag2O(s)': -31.0, 'AgCl(s)': -127.0, 'AgNO3(s)': -124.3, 'Na(s)': 0.0, 'Na(g)': 107.3, 'Na+(g)': 609.3, 'NaBr(s)': -361.0, 'NaCl(s)': -411.1, 'NaCl(g)': -176.6, 'NaCl(aq)': -407.2, 'NaOH(s)': -425.6, 'NaOH(aq)': -470.1, 'Na2CO3(s)': -1130.6, 'S(s, rhombic)': 0.0, 'S(g)': 278.8, 'S2Cl2(g)': -18.4, 'SF6(g)': 1209291.8, 'H2S(g)': -20.6, 'SO2(g)': -296.8, 'SO3(g)': -395.7, 'SOCl2(g)': -212.5, 'H2SO4(l)': -813.9, 'H2SO4(aq)': -909.2, 'Sn(s, white)': 0.0, 'Sn(s, gray)': -2.0, 'SnCl4(l)': -511.3, 'SnCl4(g)': -471.5, 'SnO2(s)': -580.7, 'Ti(s)': 0.0, 'TiCl4(l)': -804.2, 'TiCl4(g)': -763.2, 'TiO2(s)': -939.7, 'Zn(s)': 0.0, 'ZnCl2(s)': -415.0, 'ZnO(s)': -348.2, 'ZnS(s, sphalerite)': -205.9}
$w.onReady(function () {
	// Write your JavaScript here
	// To select an element by ID use: $w("#elementID")
	modifyTable()
	// Click "Preview" to run your code
	
});

function modifyTable(){
	let rows = []
	for(const [key, value] of Object.entries(dict)){
		let dict = {}
		dict["name"] = key
		dict["age"] = value
		rows.push(dict)
		
	}
	console.log($w("#table1").columns)
	console.log($w("#table1").rows)
	console.log(rows)
	$w("#table1").rows = rows
}
/**
 *	Adds an event handler that runs when the element is clicked.
 *	 @param {$w.MouseEvent} event
 */
export function button1_click(event) {
	// This function was added from the Properties & Events panel. To learn more, visit http://wix.to/UcBnC-4
	// Add your code for this event here: 
	
	
	
	
	let myElement = $w("TextInput");

	let formula = myElement[0].value.split("=")

	let reactionMolecules = formula[0].replace(" ","").split("+")
	let productMolecules = formula[1].replace(" ","").split("+")

	

	console.log(reactionMolecules)
	console.log(productMolecules)

	//checkBalanced(reactionMolecules, productMolecules)
	let ethalpy = calcEthalpy(reactionMolecules,productMolecules,dict)
}

function calcEthalpy(reactionMolecules,productMolecules,dict){
	let reactantsEthalpy = 0
	for(let molecule in reactionMolecules){
		let count = 1
		let curSymbol = ""
		if(!isNaN(reactionMolecules[molecule][0]) || reactionMolecules[molecule][0]=="."){
			console.log("TRUE"+reactionMolecules[molecule])
			count = reactionMolecules[molecule].match(/\.*[0-9]+/)
			console.log("COUNT:"+count)
			curSymbol = reactionMolecules[molecule].replace(count,'')
			count = Number(count)
		}
		else{
			curSymbol = reactionMolecules[molecule]
		}
		if(dict[curSymbol]==undefined){
			console.log("ERROR SYMBOL NOT FOUND IN TABLE "+curSymbol)
			$w("#input1").value = $w("#input1").value.replace(curSymbol,"UNDEFINED")
		}
		console.log("68: "+reactionMolecules[molecule][0])
		console.log(curSymbol)
		reactantsEthalpy += count * dict[curSymbol]
		console.log(dict[curSymbol])
	}
	let productEthalpy = 0
	for(let molecule in productMolecules){
		let count = 1
		let curSymbol = ""
		if(!isNaN(productMolecules[molecule][0])|| productMolecules[molecule][0]=="."){
			count = productMolecules[molecule].match(/\.*[0-9]+/)
			console.log(count)
			curSymbol = productMolecules[molecule].replace(count,'')
			count = Number(count)
		}
		else{
			curSymbol = productMolecules[molecule]
		}
		if(dict[curSymbol]==undefined){
			console.log("ERROR SYMBOL NOT FOUND IN TABLE "+curSymbol)
			$w("#input1").value = $w("#input1").value.replace(curSymbol,"UNDEFINED")
		}
		console.log("68: "+productMolecules[molecule][0])
		console.log(curSymbol)
		productEthalpy += count * dict[curSymbol]
		console.log(dict[curSymbol])
	}
	$w("#text2").text = String(productEthalpy.toFixed(1))
	$w("#text3").text = String(reactantsEthalpy.toFixed(1))
	$w("#text6").text = String((productEthalpy-reactantsEthalpy).toFixed(1))
	return productEthalpy-reactantsEthalpy
}
function checkBalanced(reactionMolecules, productMolecules){
	console.log("checking balanced")
	let reactionCounts = {}
	for(let molecule in reactionMolecules){
		console.log(reactionMolecules[molecule])
		let number = reactionMolecules[molecule].match(/[0-9]+/g)
		console.log("number: "+number)
		let symbols = reactionMolecules[molecule].match(/[A-Z][a-z]*/g)
		console.log("symbols: "+symbols)
		for(let symbol in symbols){
			try{
				reactionCounts[symbols[symbol]] = number[symbol]
			}
			catch(error){
				reactionCounts[symbols[symbol]] = 1
			}
		}
	}
	let productCounts = {}
	for(let molecule in productMolecules){
		console.log(productMolecules[molecule])
		let number = productMolecules[molecule].match(/[0-9]+/g)
		console.log("number: "+number)
		let symbols = productMolecules[molecule].match(/[A-Z]/g)
		console.log("symbols: "+symbols)
		console.log(symbols)
		for(let symbol in symbols){
			try{
				productCounts[symbols[symbol]] = number[symbol]
			}
			catch(error){
				productCounts[symbols[symbol]] = 1
			}
		}
	}
	console.log(reactionCounts) 
	console.log(productCounts)
}

/**
 *	Adds an event handler that runs when the element is clicked.
 *	 @param {$w.MouseEvent} event
 */
export function button2_click(event) {
	// This function was added from the Properties & Events panel. To learn more, visit http://wix.to/UcBnC-4
	// Add your code for this event here: 
	let text = $w("#input2").value.replace(" ","")
	let textArr = text.split("=")
	let key = textArr[0]
	let value = textArr[1]
	dict[key] = value
	modifyTable()
}

/**
 *	Adds an event handler that runs when the element is clicked.
 *	 @param {$w.MouseEvent} event
 */
export function button3_click(event) {
	// This function was added from the Properties & Events panel. To learn more, visit http://wix.to/UcBnC-4
	// Add your code for this event here: 
	dict = dictOrginal
	modifyTable()
}