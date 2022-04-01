var config = {
	init: function () {
		this.zinsen = [
			2.22, // Variabel
			2.00, // 1 Jahr
			2.10, // 2 Jahre
			2.20, // 3 Jahre
			2.40, // 4 Jahre
			2.55, // 5 Jahre
			2.70, // 6 Jahre
			2.75, // 7 Jahre
			2.80, // 8 Jahre
			2.85, // 9 Jahre
			2.89 // 10 Jahre
		];
		this.zinsenEffektiv = [
			2.24, // Variabel
			2.23, // 1 Jahr
			2.23, // 2 Jahre
			2.24, // 3 Jahre
			2.29, // 4 Jahre
			2.35, // 5 Jahre
			2.42, // 6 Jahre
			2.47, // 7 Jahre
			2.52, // 8 Jahre
			2.57, // 9 Jahre
			2.63 // 10 Jahre
		];
		this.version = 'online'; // online vs offline - unterschiedliche Darstellung/Berechnung
		this.grunderwerbsteuer = 5.00;
		this.maklerprovision = 3.57;
		this.notarprovision = 1.50;
		this.flexpreis = 0.19; // Aufpreis für Flex
		this.minderaufschlag = 0.30; // Aufpreis bei < 50 000
		this.bwapreise = [
			0, 		// Wenn BWA <= 60,00%, dann um 0% erhöhter Zins
			0.19,	// Wenn BWA zwischen 60,01% und 80,00%, dann um 0,19% erhöhter Zins
			0.39,	// Wenn BWA zwischen 80,01% und 90,00%, dann um 0,39% erhöhter Zins
			0.59	// Wenn BWA >90,00%, dann um 0,59% erhöhter Zins
		],
		this.personenzahl = 2;
		this.autozahl = 1;
		this.absicherungprozent = 70;
		this.einnahmen = 2000; // nur als Preset für Lebenshaltungskosten
		this.lebenshaltung = [
		//EK 500    , 750    , 1000   , 1250   , 1500   , 1750   , 2000   , 2250   , 2500   , 2750   , 3000   , 3250   , 3500   , 3750   , 4000   , 4250   , 4500   , 4750   , 5000    
			[350    , 350    , 350    , 350    , 360    , 374    , 387    , 401    , 414    , 428    , 441    , 468    , 486    , 514    , 531    , 558    , 576    , 603    , 630  ], // 1 Person
			[700    , 700    , 700    , 700    , 710    , 724    , 737    , 750    , 764    , 778    , 791    , 832    , 864    , 912    , 944    , 992    , 1024   , 1072   , 1120 ], // 2 Personen
			[910    , 910    , 910    , 910    , 920    , 934    , 952    , 973    , 994    , 1015   , 1036   , 1092   , 1134   , 1197   , 1239   , 1302   , 1344   , 1407   , 1470 ], // 3 Personen
			[1120   , 1120   , 1120   , 1120   , 1130   , 1144   , 1167   , 1196   , 1224   , 1253   , 1281   , 1352   , 1404   , 1482   , 1534   , 1612   , 1664   , 1742   , 1820 ], // 4 Personen
			[1330   , 1330   , 1330   , 1330   , 1340   , 1354   , 1382   , 1418   , 1454   , 1490   , 1526   , 1613   , 1674   , 1767   , 1829   , 1922   , 1984   , 2077   , 2170 ], // 5 Personen
			[1540   , 1540   , 1540   , 1540   , 1550   , 1564   , 1597   , 1641   , 1684   , 1728   , 1771   , 1872   , 1944   , 2052   , 2124   , 2232   , 2304   , 2412   , 2520 ], // 6 Personen
			[1750   , 1750   , 1750   , 1750   , 1760   , 1774   , 1812   , 1863   , 1914   , 1965   , 2016   , 2132   , 2214   , 2337   , 2419   , 2542   , 2624   , 2747   , 2870 ]  // 7 Personen
		];
		this.imagesList = [ // Nicht verändern, nur für den Preloader
			'images/arrow_down.png',
			'images/arrow_up.png',
			'images/bg_fsumme.jpg',
			'images/bg_header_finanzierung.jpg',
			'images/bg_header_flexibilitaet.jpg',
			'images/bg_header_fsumme_anschluss.jpg',
			'images/bg_header_fsumme_kaufenbauen.jpg',
			'images/bg_header_fsumme_modern.jpg',
			'images/bg_header_fsumme_raten.jpg',
			'images/bg_header_premium.jpg',
			'images/bg_header_sicherheit.jpg',
			'images/bg_machbarkeitscheck.png',
			'images/button_back.png',
			'images/buttons.png',
			'images/buttons_phasen.png',
			'images/checkbox.png',
			'images/fsumme_header_active.png',
			'images/fsumme_header_value.png',
			'images/ico_s.png',
			'images/input_large.png',
			'images/input_single.png',
			'images/mbkc_status.png',
			'images/p10_bottom.jpg',
			'images/p11_aufpreis.jpg',
			'images/p11_bottom.jpg',
			'images/p14_bottom.jpg',
			'images/p14_siminactive.png',
			'images/p1_bg.jpg',
			'images/p1_button.png',
			'images/p1_status.png',
			'images/p20_bottom.jpg',
			'images/p21_bottom.jpg',
			'images/p22_bottom.jpg',
			'images/p23_fotos.jpg',
			'images/p24_fotos.jpg',
			'images/p25_bottom.jpg',
			'images/p26_bottom.jpg',
			'images/p26_box.jpg',
			'images/p29_bottom.jpg',
			'images/p30_bg.jpg',
			'images/p30_button.png',
			'images/p3_bg.jpg',
			'images/p48_bg.jpg',
			'images/p48_hover.png',
			'images/p48_kfw.png',
			'images/p48_lbs.png',
			'images/p48_phasen.png',
			'images/p4_bottom.jpg',
			'images/p5_bottom.jpg',
			'images/p6_bottom.jpg',
			'images/p7_bottom.jpg',
			'images/p8_bottom.jpg',
			'images/p9_bottom.jpg',
			'images/slider_handle-horiz.png',
			'images/slider_small-handle.png',
			'images/tooltip.png'
		];
	}
}