$(document).ready(function() {
	app.init();
});

var app = {
	init: function () {
		if ($('#protocol').is(':visible')) {
			this.initProtocol();
		} else {
			this.initConfig();
			this.initGlobals();
			this.initIpad();
			this.initPreloader();
			this.initTooltips();
			this.initValues();
			this.initLNavi();
			this.showPage('p1');
		}
	},
	initValues: function () {
		this.currentPage = 'p1';
	},
	initIpad: function () {
		var isiPad = navigator.platform.indexOf("iP");
		if(isiPad != -1) { 
			globals.isIpad = true;
			// Externes Script für besseres Touch-Feeling
			initPad();
		}
	},
	initTooltips: function () {
		$('.tooltip, .tooltipsimple, #contact').hover(function(e) {
			var tiptext = $(this).attr('rel');
			$('#tooltipbox').html(tiptext);
			if(e.pageX > 420) { var posleft = e.pageX - 220; }
			else { var posleft = e.pageX + 10; }
			$('#tooltipbox').css('left',posleft).css('top',e.pageY).show();
		}, function() {
			$('#tooltipbox').hide();
		});
		$('#contact').click(function(){$('#tooltipbox').hide();});
	},
	initLNavi: function () {
		$('#lnavi li').hover(function() {$(this).toggleClass('hover');}, function() {$(this).toggleClass('hover');});
		$('#lnavi .l_1').click(function () {app.showPage('p4');});
		$('#lnavi .l_2').click(function () {app.showPage('p6');});
		$('#lnavi .l_3').click(function () {app.showPage('p20');});
		$('#lnavi .l_4').click(function () {app.showPage('p26');});
		$('#lnavi .l_m').click(function () {app.showPage('p1');});
	},
	initPreloader: function () {
		var Images = new Array();
		for (i = 0; i < config.imagesList.length; i++) {
		   	Images[i] = new Image();
		    Images[i].src = config.imagesList[i];
		}
	},
	initGlobals: function () {
		globals.init();
	},
	initConfig: function () {
		config.init();
		if (config.version == 'offline') {
			$('#wrapper').addClass('offline');	
		} else {
			$('#wrapper').addClass('online');
		}
	},
	
	showProtocolWindow: function () {
		druckfenster = window.open('protokoll.html', 'Druckansicht', 'width=650, height=400, location=no, status=no, scrollbars=yes')
		druckfenster.focus();
	},
	
	initProtocol: function () {
		// Datenaufbereitung
		var globals = window.opener.globals;
		var config = window.opener.config;

		if (config.version == 'offline') {
			$('#protocol').addClass('offline');	
		} else {
			$('#protocol').addClass('online');
		}
			// Daten für Box 1
		var bedarf_1 = 0;
		var bedarf_2 = 0;
		var bedarf_3 = 0;
		
		if (globals.fsumme_bedarfstyp == 1) {
			bedarf_1 = globals.fsumme_kaufen_1_sum;
			bedarf_2 = globals.fsumme_kaufen_2_sum;
			bedarf_3 = globals.fsumme_kaufen_3_used;
		} else if (globals.fsumme_bedarfstyp == 2) {
			bedarf_1 = globals.fsumme_bauen_1_sum;
			bedarf_2 = globals.fsumme_bauen_2_sum;
			bedarf_3 = globals.fsumme_bauen_3_used;
		} else if (globals.fsumme_bedarfstyp == 3) {
			bedarf_1 = globals.fsumme_anschluss_1_sum;
			bedarf_2 = globals.fsumme_anschluss_2_sum;
			bedarf_3 = globals.fsumme_anschluss_3_used;
		} else if (globals.fsumme_bedarfstyp == 4) {
			bedarf_1 = globals.fsumme_modernisieren_1_sum;
			bedarf_3 = globals.fsumme_modernisieren_2_used;
		}
		
		var fix =  (globals.leistungsCase == 'a') ? 1 : 0;
		var premium = (globals.paketSicher && globals.paketFlex) ? 1 : 0;
		var flex = (globals.paketFlex) ? 1 : 0;
		
		// Datumsausgabe
		var Datum = new Date();
		var Tag = (Datum.getDate() > 9) ? Datum.getDate() : '0' + Datum.getDate();
		var Month = Datum.getMonth() + 1;
		var Monat = (Month > 9) ? Month : '0' + Month;
		var Jahr = Datum.getFullYear();
		var Stunden = (Datum.getHours() > 9) ? Datum.getHours() : Datum.getHours();
		var ampm = 'AM'; 
		if (Stunden > 12){
			Stunden = Stunden - 12;
			ampm = 'PM';
		}
		var Minuten = (Datum.getMinutes() > 9) ? Datum.getMinutes() : '0' + Datum.getMinutes();	
		var DatumString = Monat + '/' + Tag + '/' + Jahr + ' – ' +  Stunden + ':' + Minuten + ' ' + ampm;
		$('#datum').text(DatumString);
		
		// Box1
		if (globals.fsumme_bedarfstyp == 3) { // Anschluss
			$('#c1').text('Residual debt');
			
		} else if (globals.fsumme_bedarfstyp == 4) { // Modernisieren
			$('#wk').hide();
		}
		$('#v1').text('$' + app.addTSeparator(bedarf_1));
		$('#v2').text('$' + app.addTSeparator(bedarf_2));
		$('#v3').text('$' + app.addTSeparator(bedarf_3));
		$('#v4').text('$' + (app.addTSeparator(Number(bedarf_1) + Number(bedarf_2) - Number(bedarf_3))));
		
		// Box 2
		$('#v5').text('$' + app.addTSeparator(globals.fsumme_raten_1_sum));
		$('#v6').text('$' + app.addTSeparator(globals.fsumme_raten_2_sum));
		$('#v7').text('$' + app.addTSeparator(globals.fsumme_raten_3_sum));		
		$('#v8').text('$' + app.addTSeparator(globals.ratenpotenzial));
	
		// Box 3
		$('#v9').text('$' + app.addTSeparator(globals.ratenpotenzial));
		$('#v10').text('$' + app.addTSeparator(globals.darlehensrate));
		
		$('#v11').text('$' + app.addTSeparator(globals.mbkcspielraum));
		// Box 3 MBKC
		if (globals.mbkc_status == 'yes') {
			$('#mbkc').attr('src','images/protocol_mbkc2.png');
		} else if (globals.mbkc_status == 'ok') {
			$('#mbkc').attr('src','images/protocol_mbkc3.png');
		}
		
		// Häkchen
		var imgOn = 'images/protocol_radio-on.png';
		if (fix == 1 ) $('#r1').attr('src', imgOn );
		if (fix == 0 ) $('#r2').attr('src', imgOn );
		if (flex == 1 ) {$('#r3').attr('src', imgOn ); $('#r3-t').addClass("active"); }
		if (flex == 0 ) {$('#r4').attr('src', imgOn ); $('#r4-t').addClass('active'); }
		if (globals.hyposchutz == 1 ) {$('#r5').attr('src', imgOn ); $('#r5-ton').addClass('active'); $('#r5-toff').removeClass('active'); }
		if (globals.prohaus == 1 ) {$('#r6').attr('src', imgOn ); $('#r6-ton').addClass('active'); $('#r6-toff').removeClass('active'); }
		if (globals.risikolv == 1 ) {$('#r7').attr('src', imgOn ); $('#r7-ton').addClass('active'); $('#r7-toff').removeClass('active'); }
		if (globals.indsachv == 1 ) {$('#r8').attr('src', imgOn ); $('#r8-ton').addClass('active'); $('#r8-toff').removeClass('active'); }
		if (premium == 1 ) {$('#r9').attr('src', imgOn ); $('#r9-t').addClass('active'); }
		if (premium == 0 ) {$('#r10').attr('src', imgOn ); $('#r10-t').addClass('active'); }
		
		// Darlehenszusammensetzung
		var sdarlehen = (window.opener.globals.leistungspaket == '------') ? '' : ' ' + window.opener.globals.leistungspaket;
		var darlehen = Array();
		if (globals.darlehen_sk == 1) darlehen.push('„Sparkassen“ Loan' + sdarlehen);
		if (globals.darlehen_lbs== 1) darlehen.push('LBS');
		if (globals.darlehen_hand == 1) darlehen.push('“Handshake”-Loan');
		if (globals.darlehen_kfw == 1) darlehen.push('Gov. subsidies');
		if (globals.darlehen_sonstiges == 1) darlehen.push(window.opener.globals.darlehen_sonstigesDesc);

		darlehen = darlehen.join(' + ');
		if (darlehen.length < 1) darlehen = '--------------------'
		$('#e1').text(darlehen);
		
		// Fußnote
		var trate = String(globals.tilgungsrateprojahr/10);
		$('.tilgungssatz').text(trate.replace('.', ','));

		if (config.version == 'online') {
			// ONLINE
			znom = config.zinsen[10];
			znom = String(znom);
			$('.znominal').text(znom.replace('.', ','));
			
			var zeff = config.zinsenEffektiv[10];
			zeff = String(zeff);
			$('#zeffektiv').text(zeff.replace('.', ','));
		} else {
			// Offline/Berater
			znom = String(Math.round((globals.zinsSatz + globals.flexpreis) * 100) / 100);
			$('.znominal').text(znom.replace('.', ','));
			
			if (globals.anteilVar == 0 || globals.zinsSatzSpezial != false) {
				$('#mixinfo').hide();	
			} else {
				$('#anteilVar').text(globals.anteilVar);
				$('#anteilFest').text(globals.anteilFest);
				var aufpreis = globals.aufpreis + globals.flexpreis;
				var zinsFest = config.zinsen[globals.bindung];
				zinsFest = String(Math.round((zinsFest + aufpreis) * 100) / 100);
				var zinsVar = config.zinsen[0];
				zinsVar = String(Math.round((zinsVar + aufpreis) * 100) / 100);
				$('#zinsFest').text(zinsFest.replace('.', ','));
				$('#zinsVar').text(zinsVar.replace('.', ','));
			}			
		}

		
		// Anhang
		
		var boxc = (globals.fsumme_bedarfstyp == 0) ? 1 : globals.fsumme_bedarfstyp;
		
		$('#box7-' + boxc).addClass('current');
		$('.box7 td, #box8 td').each(function(index, value) { 
			if($(value).attr('id')) {
				var sum = 0;
				var id = $(value).attr('id')
				eval("if(typeof globals.fsumme_" + id +" == 'number' || typeof globals.fsumme_" + id +" == 'string') sum = globals.fsumme_" + id);
				$(value).text('$' + app.addTSeparator(sum));
			}
		});

		$('.box7 .comment, #box8 .comment').each(function(index, value) { 
			if($(value).attr('id')) {
				var text = '';
				var id = $(value).attr('id')
				eval("if(typeof globals.fsumme_" + id +" == 'string') text = globals.fsumme_" + id);
				if (text != '') {
					$(value).text(text);
				}
			}
		});
		
		// Drucken
		setTimeout('print();', 1000);
	},

	// Standardprozess zum "Seiten"-Anzeigen
	showPage: function (page) {
		$('#wrapper').removeClass(this.currentPage);
		$('#' + this.currentPage).removeClass('current');
		$('#' + this.currentPage + ' a').unbind('click');
		$('#' + this.currentPage + ' div').unbind('click');
		$('#' + page).addClass('current');
		$('#wrapper').addClass(page);
		this.currentPage = page;
		eval("if(typeof "+page + " == 'object')if(typeof "+page + ".init == 'function')"+page + ".init()");
		return false;
	},
	
	// Bestimmte Falldarstellung anzeigen
	showCase: function (casetype) {
		$('#' + this.currentPage + ' .case_a').removeClass('current');
		$('#' + this.currentPage + ' .case_b').removeClass('current');
		$('#' + this.currentPage + ' .case_c').removeClass('current');
		$('#' + this.currentPage + ' .case_' + casetype).addClass('current');	
	},

	// Bestimmtes Fieldset der FSummen-Berechnung anzeigen
	showFsummeFieldset: function (id) {
		$('#' + this.currentPage + ' .field').removeClass('current');
		$('#' + this.currentPage + ' .fsumme_fieldset').removeClass('current');
		$('#' + this.currentPage + ' .field_' + id).addClass('current');
		$('#' + this.currentPage + ' .fieldset_' + id).addClass('current');
		globals.fsumme_currentFieldset = id;
	},
	
	// Getrenntes Inputfeld auslesen
	readSepInput: function (inputId, length) {
		var value = '';
		var tmpVal;
		var i = 0;
		for (i = 1; i<= length; i++) {
			tmpVal = $('#' + inputId + '_' + i).val()
			if(isNaN(tmpVal)) {
				alert('Please enter only digits.');
				return 0;
			}
			value = value + tmpVal.toString();
		}
		return Number(value);
	},
	
	autoclearSepInput: function(inputId, length) {
		var i = 0;
		var tmpVal = '';
		for (i = 1; i<= length; i++) {
			$('#' + inputId + '_' + i).bind('focus', function () {
				tmpVal = $(this).val();
				$(this).val('');
			}).bind('blur', function () {
				if ($(this).val().replace(/\D/g, "") == '') {
					$(this).val(tmpVal);
				}
			}).bind('keyup', function () {
				if ($(this).val().replace(/\D/g, "") == '') {
					$(this).val(tmpVal);
				}
				var next = $(this).next();
				if (next.hasClass('sep')) {
					$(this).change();
					next.next().focus(); }
				else if (next.hasClass('curr')) {
					$(this).blur();
					$(this).change();
				}
				else {
					$(this).change();
					if (globals.isIpad == false) {
						next.focus();
					} else {
						$(this).blur();
						$(this).change();
					}
				}
			});
		}	
	},
	
	// Getrenntes Inputfeld beschreiben
	writeSepInput: function(inputId, length, value) {
		var stringval  = value.toString();
		var len = stringval.length;
		var i = 0;
		for (i = 1; i<= length; i++) {
			$('#' + inputId + '_' + i).val(Number(stringval.substring(len-length+i-1,len-length+i)));
		}	
	},
	
	// Getrenntes Inputfeld erhöhen
	increaseSepInput: function (inputId, length, change, max) {
		var value = this.readSepInput(inputId, length) + change;
		if (value > max && max > 0) {
			value = max;
		}		
		this.writeSepInput(inputId, length, value);
		return value;
	},
	
	// Getrenntes Inputfeld erniedrigen
	decreaseSepInput: function (inputId, length, change, min) {
		var value = this.readSepInput(inputId, length) - change;
		if (value < min) {
			value = min;
		}
		this.writeSepInput(inputId, length, value);
		return value;
	},
	
	// Fsummen-Variablen aus den Feldern Lesen und speichern
	readFsummeVars: function (prefix, end) {
		var i = 0;
		var value = 0;
		var sum = 0;
		for (i = 1; i<= end; i++) {
			value = Number(app.removeTSeparator($('#' + prefix + '_' + i).val()));
			eval("globals.fsumme_" + prefix + "_" + i + " = value");
			sum = sum + value;
			if (value == 0) {
				value = '';
			}
			$('#' + prefix + '_' + i).val(app.addTSeparator(value));
		}
		eval("globals.fsumme_" + prefix + "_sum = sum");
	},
	
	// Fsummen-Variablen in die Felder Schreiben
	writeFsummeVars: function (prefix, end) {
		var i = 0;
		var value = 0;
		var sum = 0;
		for (i = 1; i<= end; i++) {
			eval("value = globals.fsumme_" + prefix + "_" + i);
			if (value == 0) {
				value = '';
			}
			$('#' + prefix + '_' + i).val(app.addTSeparator(value));
		}
		eval("sum = globals.fsumme_" + prefix + "_sum");
		if (sum == 0) {
			sum = '';
		}
		$('#' + prefix + '_sum').val(app.addTSeparator(sum));		
	},
	
	// Summe aktualisieren
	updateFsummeFieldset: function (prefix, end) {
		var sum = 0;
		this.readFsummeVars(prefix, end);
		eval("sum = globals.fsumme_" + prefix + "_sum");
		if (sum == 0) {
			sum = '';
		}
		$('#' + prefix + '_sum').val(app.addTSeparator(sum));
	},

	// Darlehensrate berechnen	
	calcDarlehensrateGeneral: function(tilgungsrate) {
		var rate = 0;
		var tilgung = tilgungsrate / 10;
		var zins = config.zinsen[10];
		
		// Nur in der Offline-Berater-Version Aufpreis
		if (config.version == 'offline') {
			var zins = globals.zinsSatz;
			if (zins == 0) {
				zins = config.zinsen[10];
				// BWA und < 50k Aufpreis
				zins = zins + app.calcAufpreis();
			}
			// Flexaufpreis
			zins = zins + app.getFlexAufpreis();
		}
		
		rate = (globals.finanzierungssumme * (tilgung + zins)) / 1200;
		return Math.round(rate);
	},
	
	getFlexAufpreis: function () {
		if (globals.paketFlex) {
			globals.flexpreis = config.flexpreis;
		}
		else {
			globals.flexpreis = 0;
		}
		return globals.flexpreis;
	},

	calcDarlehensrate: function () {
		globals.darlehensrate = app.calcDarlehensrateGeneral(globals.tilgungsrateprojahr);
		return globals.darlehensrate;
	},

	calcSimDarlehensrate: function () {
		globals.darlehensrate_sim = app.calcDarlehensrateGeneral(globals.tilgungsrateprojahr_sim);
		return globals.darlehensrate_sim;
	},
	// Bewertungsauslauf
	calcBwa: function () {
		var eigenmittel = 0;
		globals.bwa = 0;
		if (globals.fsumme_bedarfstyp == 1) {
			eigenmittel = globals.fsumme_kaufen_3_used;
		} else if (globals.fsumme_bedarfstyp == 2) {
			eigenmittel = globals.fsumme_bauen_3_used;
		} else if (globals.fsumme_bedarfstyp == 3) {
			eigenmittel = globals.fsumme_anschluss_3_used;
		} else if (globals.fsumme_bedarfstyp == 4) {
			eigenmittel = globals.fsumme_modernisieren_2_used;
		}
		var teiler = globals.finanzierungssumme + Number(eigenmittel);
		if (teiler > 0) {
			globals.bwa = globals.finanzierungssumme / teiler;
		}
		// 2 Dezimalstellen runden
		globals.bwa = globals.bwa * 100;
		globals.bwa = Math.round(globals.bwa * Math.pow(10, 2)) / Math.pow(10, 2);
		
		return globals.bwa;
	},
	
	calcBwaPreis: function () {
		var bwa = app.calcBwa();
		var preis = 0;
		if (globals.zinsSatzSpezial == false) {
			if (bwa <= 60) { preis = config.bwapreise[0]; }
			else if (bwa > 60 && bwa <= 80) { preis = config.bwapreise[1];}
			else if (bwa > 80 && bwa <= 90) { preis = config.bwapreise[2]; }
			else if (bwa > 90) { preis = config.bwapreise[3]; }
		}
		globals.bwapreis = preis;
		return preis;
	},
	
	calcAufpreis: function () {
		globals.aufpreis = app.calcBwaPreis();
		if (globals.finanzierungssumme < 50000 && globals.zinsSatzSpezial == false) {
			globals.aufpreis = globals.aufpreis + config.minderaufschlag;
		}
		return globals.aufpreis;
	},
	
	// Tausendertrenner hinzufügen
	addTSeparator: function (number) {
		if (number < 0) {
			var size = 4;}
		else {
			var size = 3;}
		number = '' + number;
		if (number.length > size) {
			var mod = number.length % 3;
			var output = (mod > 0 ? (number.substring(0,mod)) : '');
			for (i=0 ; i < Math.floor(number.length / 3); i++) {
				if ((mod == 0) && (i == 0))						
					output += number.substring(mod+ 3 * i, mod + 3 * i + 3);
				else
					output+= ',' + number.substring(mod + 3 * i, mod + 3 * i + 3);
			}
			return (output);
		}
		else return number;
	},
	
	// Tausendertrenner entfernen
	removeTSeparator: function (numberstring) {
		var numstr = numberstring.toString();
		output = numstr.replace(/\D/g, "");
		return Number(output);
	},		
	
	// Sicherheitspaket gewählt?
	checkSecure: function () {
		if (globals.hyposchutz == 0 && globals.risikolv == 0 && globals.prohaus == 0 && globals.indsachv == 0) {
			globals.paketSicher = false;
		} else {
			globals.paketSicher = true;
		}
		return globals.paketSicher;
	},
	
	refreshMbkc: function () {
		if (globals.mbkc_status != 0) {
			p1.mbkcRecalc();
			p1.setMbkcStatus();
		}
	},
	
	// Paketempfehlung generieren
	checkPacketSuggestion: function () {
		this.checkSecure();
		var sugg = ''
		if (globals.box3_status == 0) {
			sugg = '------';
		} else {
			if (!globals.paketSicher && !globals.paketFlex) {
				sugg = 'Classic '; }
			else if (globals.paketSicher && globals.paketFlex) {
				sugg = 'Premium '; }
			else if (globals.paketSicher) {
				sugg = 'Secure '; }
			else {
				sugg = 'Flexible ';}
			if (globals.leistungsCase == 'a') {
				sugg = sugg + 'Fixed'; }
			else {
				sugg = sugg + 'Mixed'; }
		}
		globals.leistungspaket = sugg;
		return sugg;
	},
	
	// Darlehensempfehlung generieren
	checkDarlehenSuggestion: function () {
       	var count = globals.darlehen_sk + globals.darlehen_hand + globals.darlehen_lbs + globals.darlehen_kfw + globals.darlehen_sonstiges;
       	if (count > 2) {
       		sugg = 'Combi ' + count;
       	} else if (count == 2) {
       		sugg = 'Combi ';
       		if (globals.darlehen_sk && globals.darlehen_lbs) {
       			sugg = sugg + 'LBS';
       		}
       		else if (globals.darlehen_sk && globals.darlehen_kfw) {
       			sugg = sugg + 'Gov. subs.';
       		}
       		else if (globals.darlehen_sk && globals.darlehen_sonstiges) {
       			sugg = sugg + 'Other';
       		}
       		else if (globals.darlehen_lbs && globals.darlehen_sonstiges) {
       			sugg = 'LBS + Other';
       		}
       		else if (globals.darlehen_lbs && globals.darlehen_kfw) {
       			sugg = 'Gov. subs. + LBS';
       		}
       		else if (globals.darlehen_sonstiges && globals.darlehen_kfw) {
       			sugg = 'Gov. subs. + Other';
       		}
       	} else if (count == 1) {
       		if (globals.darlehen_sk) {
				sugg = 'Loan <span class="ico_turm"></span>';		
       		} else if (globals.darlehen_hand) {
				sugg = 'Loan <span class="ico_handschlag"></span>';		
       		} else if (globals.darlehen_lbs) {
       			sugg = 'Lbs-Loan';
       		} else if (globals.darlehen_kfw) {
       			sugg = 'Gov. subs.'
       		} else if (globals.darlehen_sonstiges) {
       			sugg = 'Other Loan'
       		}
       	} else {
       		globals.box4_status = 0;
       		sugg = '------';
       	}
       	globals.strukturierung = sugg;
       	return sugg;
	}
}

var globals = {
	init: function () {
		this.isIpad = false;
		
		// Auswahl des Richtigen Leistungspakets
		this.finanzierungssumme = 0;
		this.anteilVar = 0;
		this.anteilFest = 100;
		this.bindung = 10;
		this.zinsSatz = 0;
		this.zinsSatzSpezial = false;
		this.aufpreis = 0; // Aufpreis auf Zinssatz
		this.flexpreis = 0; // Flexaufpreis
		this.zinsSatzEffektiv = 0;
		this.leistungsCase = 'a';  //Fix vs Mix
		this.sondertilgungsrecht = 0;
		this.darlehensoption = 0;
		this.darlehensrate = 0;	// Echte Darlehensrate
		this.darlehensrate_sim = 0; // Darlehensrate auf 10Jahresbindung
		this.tilgungsrateprojahr = 20; // durch 10!
		this.tilgungsrateprojahr_sim = 20; // durch 10!
		this.zinslimit = Math.round(config.zinsen[10] * 100) + 10;
		this.sicherPrio = 'a';
		this.absicherungprozent = config.absicherungprozent;
		this.einnahmen = 0; // 
		this.ausgaben = 0; // 
		this.sonderausgaben = 0;
		this.mbkcspielraum = 0;
		
		this.grunderwerbsteuer = Math.round(config.grunderwerbsteuer * 100);

		this.bwa = 0;
		this.bwaPreis = 0;
		
		// Ermittlung der Finanzierungssumme
		this.fsumme_currentFieldset = 1;		
		
		this.fsumme_kaufen_1_1 = 0; // Kaufpreis
		this.fsumme_kaufen_1_2 = 0; // Erwerbsnebenkosten
		this.fsumme_kaufen_1_p_3 = Math.round(config.maklerprovision * 100); // Maklerkosten Prozentsatz
		this.fsumme_kaufen_1_p_4 = Math.round(config.notarprovision * 100); // Notarkosten Prozentsatz
		this.fsumme_kaufen_1_sum = 0; // Summe

		this.fsumme_kaufen_2_1 = 0; // Bäder
		this.fsumme_kaufen_2_2 = 0; // Küche
		this.fsumme_kaufen_2_3 = 0; // Malerkosten
		this.fsumme_kaufen_2_4 = 0; // Heizung
		this.fsumme_kaufen_2_5 = 0; // Wärmedämmung
		this.fsumme_kaufen_2_6 = 0; // Solaranlage
		this.fsumme_kaufen_2_7 = 0; // Dach
		this.fsumme_kaufen_2_8 = 0; // Elektriker
		this.fsumme_kaufen_2_9 = 0; // Außenanlagen
		this.fsumme_kaufen_2_10 = 0; // Sonstiges
		this.fsumme_kaufen_2_sum = 0; // Summe
		this.fsumme_kaufen_2_kommentar = ''; // Kommentar

		this.fsumme_kaufen_3_1 = 0; // Barmittel
		this.fsumme_kaufen_3_2 = 0; // Sparguthaben
		this.fsumme_kaufen_3_3 = 0; // Wertpapiere
		this.fsumme_kaufen_3_4 = 0; // Lebensversicherung
		this.fsumme_kaufen_3_5 = 0; // Bausparguthaben
		this.fsumme_kaufen_3_6 = 0; // Bezahltes Grundstück
		this.fsumme_kaufen_3_7 = 0; // Eigenleistungen
		this.fsumme_kaufen_3_8 = 0; // Sonstiges
		this.fsumme_kaufen_3_sum = 0; // Summe
		this.fsumme_kaufen_3_used = 0; // Verwendet
		this.fsumme_kaufen_2_kommentar = ''; // Kommentar

		this.fsumme_bauen_1_1 = 0; // Grundstückspreis
		this.fsumme_bauen_1_2 = 0; // Erwerbsnebenkosten
		this.fsumme_bauen_1_p_3 = Math.round(config.maklerprovision * 100); // Maklerkosten Prozentsatz
		this.fsumme_bauen_1_p_4 = Math.round(config.notarprovision * 100); // Notarkosten Prozentsatz
		this.fsumme_bauen_1_sum = 0; // Summe

		this.fsumme_bauen_2_1 = 0; // Erschließung
		this.fsumme_bauen_2_2 = 0; // Architekt
		this.fsumme_bauen_2_3 = 0; // Erdarbeiten
		this.fsumme_bauen_2_4 = 0; // Rohbau
		this.fsumme_bauen_2_5 = 0; // Dach
		this.fsumme_bauen_2_6 = 0; // Innenausbau
		this.fsumme_bauen_2_7 = 0; // Garage
		this.fsumme_bauen_2_8 = 0; // Außenanlagen
		this.fsumme_bauen_2_9 = 0; // Sonstiges
		this.fsumme_bauen_2_10 = 0; // Gesamtbaukosten
		this.fsumme_bauen_2_11 = 0; // Baunebenkosten
		this.fsumme_bauen_2_sum = 0; // Summe
		this.fsumme_bauen_2_kommentar = ''; // Kommentar

		this.fsumme_bauen_3_1 = 0; // Barmittel
		this.fsumme_bauen_3_2 = 0; // Sparguthaben
		this.fsumme_bauen_3_3 = 0; // Wertpapiere
		this.fsumme_bauen_3_4 = 0; // Lebensversicherung
		this.fsumme_bauen_3_5 = 0; // Bausparguthaben
		this.fsumme_bauen_3_6 = 0; // Bezahltes Grundstück
		this.fsumme_bauen_3_7 = 0; // Eigenleistungen
		this.fsumme_bauen_3_8 = 0; // Sonstiges
		this.fsumme_bauen_3_sum = 0; // Summe
		this.fsumme_bauen_3_used = 0; // Verwendet
		this.fsumme_bauen_3_kommentar = ''; // Kommentar

		this.fsumme_modernisieren_1_1 = 0; // Solaranlage
		this.fsumme_modernisieren_1_2 = 0; // Energiemaßnahmen
		this.fsumme_modernisieren_1_3 = 0; // Dachsanierung
		this.fsumme_modernisieren_1_4 = 0; // Heizung/ Sanitär
		this.fsumme_modernisieren_1_5 = 0; // Küche/ Bäder
		this.fsumme_modernisieren_1_6 = 0; // Wohnräume
		this.fsumme_modernisieren_1_7 = 0; // Sonstiges
		this.fsumme_modernisieren_1_sum = 0; // Summe
		this.fsumme_modernisieren_1_kommentar = ''; // Kommentar

		this.fsumme_modernisieren_2_1 = 0; // Barmittel
		this.fsumme_modernisieren_2_2 = 0; // Sparguthaben
		this.fsumme_modernisieren_2_3 = 0; // Wertpapiere
		this.fsumme_modernisieren_2_4 = 0; // Lebensversicherung
		this.fsumme_modernisieren_2_5 = 0; // Bausparguthaben
		this.fsumme_modernisieren_2_6 = 0; // Bezahltes Grundstück
		this.fsumme_modernisieren_2_7 = 0; // Eigenleistungen
		this.fsumme_modernisieren_2_8 = 0; // Sonstiges
		this.fsumme_modernisieren_2_sum = 0; // Summe
		this.fsumme_modernisieren_2_used = 0; // Verwendet
		this.fsumme_modernisieren_2_kommentar = ''; // Kommentar

		this.fsumme_anschluss_1_1 = 0; // Restschuld
		this.fsumme_anschluss_1_sum = 0; // Summe
		
		this.fsumme_anschluss_fsumme = 0;
		this.fsumme_anschluss_drate = 0;
		this.fsumme_anschluss_zinssatz = 0;
		this.fsumme_anschluss_dauer = 0;

		this.fsumme_anschluss_2_1 = 0; // Erschließung
		this.fsumme_anschluss_2_2 = 0; // Architekt
		this.fsumme_anschluss_2_3 = 0; // Erdarbeiten
		this.fsumme_anschluss_2_4 = 0; // Rohbau
		this.fsumme_anschluss_2_5 = 0; // Dach
		this.fsumme_anschluss_2_6 = 0; // Innenausbau
		this.fsumme_anschluss_2_7 = 0; // Garage
		this.fsumme_anschluss_2_8 = 0; // Außenanlagen
		this.fsumme_anschluss_2_9 = 0; 
		this.fsumme_anschluss_2_10 = 0;// Sonstiges
		this.fsumme_anschluss_2_sum = 0; // Summe
		this.fsumme_anschluss_2_kommentar = ''; // Kommentar

		this.fsumme_anschluss_3_1 = 0; // Sparmittel
		this.fsumme_anschluss_3_2 = 0; // Sparguthaben
		this.fsumme_anschluss_3_3 = 0; // Wertpapiere
		this.fsumme_anschluss_3_4 = 0; // Bausparguthaben
		this.fsumme_anschluss_3_5 = 0; // Lebensversicherung
		this.fsumme_anschluss_3_6 = 0; // Sonstiges
		this.fsumme_anschluss_3_sum = 0; // Summe
		this.fsumme_anschluss_3_used = 0; // Verwendet
		this.fsumme_anschluss_3_kommentar = ''; // Kommentar
				
		this.fsumme_raten_1_1 = 0; // Gehaltseingang
		this.fsumme_raten_1_2 = 0; // Gehaltseingang Partner
		this.fsumme_raten_1_3 = 0; // Kindergeld
		this.fsumme_raten_1_4 = 0; // Sonstige Einnahmen				
		this.fsumme_raten_1_sum = 0; // Summe
		this.fsumme_raten_1_kommentar = ''; // Kommentar

		this.fsumme_raten_2_1 = 0; // Lebenshaltungskosten
		this.fsumme_raten_2_2 = 0; // Kosten fürs Auto
		this.fsumme_raten_2_3 = 0; // Künftige Nebenkosten der Immobilie
		this.fsumme_raten_2_4 = 0; // Versicherungen / Sparraten / Altersvorsorge		
		this.fsumme_raten_2_5 = 0; // Bestehende Darlehen
		this.fsumme_raten_2_6 = 0; // Sonstige Ausgaben
		this.fsumme_raten_2_sum = 0; // Summe
		this.fsumme_raten_2_personen = config.personenzahl;
		this.fsumme_raten_2_autos = config.autozahl;
		
		this.fsumme_raten_3_1 = 0; // Monatlicher Sicherheitspuffer
		this.fsumme_raten_3_sum = 0; // Summe
			
		this.fsumme_bedarfstyp = 0; // Typ des letzten ausgewählten Bedarfs (Anschluss, Modernisierung,...)	
			
		this.box1_status = 0;
		this.box2_status = 0;
		this.box3_status = 0;
		this.box4_status = 0;
		this.mbkc_status = 0;
		
		this.hyposchutz = 0;
		this.risikolv = 0;
		this.prohaus = 0;
		this.indsachv = 0;
		
		this.hyposchutz_seen = 0; // wird erst nach dem sehen der auswahl aktiviert für defaultwert 1
		this.risikolv_seen = 0;
		this.prohaus_seen = 0;
		
		this.paketFlex = false;
		this.paketSicher = false;
		
       	this.darlehen_sk = 0;
       	this.darlehen_sk_seen = 0;
       	this.darlehen_lbs = 0;
       	this.darlehen_hand = 0;
       	this.darlehen_kfw = 0;
       	this.darlehen_sonstiges = 0;
       	this.darlehen_sonstigesDesc = 'Other';
		
		this.leistungspaket = '------';
		this.ratenpotenzial = 0;
		this.strukturierung = '------';
	}	
}


var p1 = {
	init: function () {
		this.writeValues();
		this.bindLinks();
		app.refreshMbkc();
	},
	writeValues: function () {
		if (globals.finanzierungssumme > 0) {
			$('#p1_box1 p').html('$' + app.addTSeparator(globals.finanzierungssumme)); }
		else {
			$('#p1_box1 p').html('$000,000'); }
		
		if (globals.ratenpotenzial > 0) {
			$('#p1_box2 p').html('$' + app.addTSeparator(globals.ratenpotenzial));
		}
		else {
			$('#p1_box2 p').html('$0,000');
		}			
		$('#p1_box3 p').html(app.checkPacketSuggestion());	
		$('#p1_box4 p').html(app.checkDarlehenSuggestion());
		$('#p1 .status').removeClass('completed');
		if (globals.box1_status == 1) $('#p1_box1 .status').addClass('completed');
		if (globals.box2_status == 1) $('#p1_box2 .status').addClass('completed');
		if (globals.box3_status == 1) $('#p1_box3 .status').addClass('completed');
		if (globals.box4_status == 1) $('#p1_box4 .status').addClass('completed');
		this.setMbkcStatus();
	},
	setMbkcStatus: function () {
 		$('#mbkc_status').removeClass('yes');
 		$('#mbkc_status').removeClass('no');
  		$('#mbkc_status').removeClass('ok');		
		if (globals.mbkc_status != 0) $('#mbkc_status').addClass(globals.mbkc_status);
	},
	bindLinks: function () {
		$('#p1 .p1_box').hover(
		  function () {
		    $(this).addClass("hover");
		  },
		  function () {
		    $(this).removeClass("hover");
		  }			
		);
		$('#p1_box1').click(function () {app.showPage('p30');});
		$('#p1_box2').click(function () {app.showPage('p50');});
		$('#p1_box3').click(function () {app.showPage('p3');});
		$('#p1_box4').click(function () {app.showPage('p48');});
		$('#p1_mbkc').mouseenter(function(){$('#p1_mbkc').addClass('hover')}).mouseleave(function(){$('#p1_mbkc').removeClass('hover')});
		$('#mbkc_status').mouseenter(function(){$('#p1_mbkc').addClass('hover')}).mouseleave(function(){$('#p1_mbkc').removeClass('hover')});
		$('#mbkc_status').click(function () {p1.showMbkc(); return false;});
		$('#p1_mbkc').click(function (){p1.showMbkc(); return false;});
		$('#mbkc_btnclose, #mbkc_btntakeover').click(function (){p1.hideMbkc(); p1.setMbkcStatus(); return false;});
		$('#p1_f3 a').click(function () {window.location.reload(); return false;});		
		$('#p1_f4 a').click(function () {app.showProtocolWindow(); return false;});	
		$('#p1_f1 a').click(function () {app.showPage('p51'); return false;});	
	},
	initMbkc: function () {
		$("#mbkc_slider1").slider({
			orientation: "horizontal",
			range: 'min',
			min: 10,
			value: globals.tilgungsrateprojahr,
			max: 100,
			step: 5,
			slide:  function(event, ui) {
				globals.tilgungsrateprojahr = ui.value;
			},
			change: function() {
				p1.mbkcWrite();
			}
		});
		this.mbkcWrite();
	},
	mbkcRecalc: function () {
		app.calcDarlehensrate();
		globals.mbkcspielraum = globals.ratenpotenzial - globals.darlehensrate;
		
		if (globals.mbkcspielraum >= 0) {
			if (globals.tilgungsrateprojahr < 20) {
				globals.mbkc_status = 'ok';
			} else {
				globals.mbkc_status = 'yes';
			}
		}
		else {
			globals.mbkc_status = 'no';
		}
	},
	mbkcWrite: function() {
		this.mbkcRecalc();
		app.writeSepInput('mbkc_i1', 4, globals.ratenpotenzial);
		app.writeSepInput('mbkc_i2', 4, globals.darlehensrate);
		$('#mbkc_box-right').removeClass('ok').removeClass('yes').removeClass('no');
		$('#mbkc_box-right').addClass(globals.mbkc_status);
		$('#mbkc_box-right .value').html('$' + app.addTSeparator(globals.mbkcspielraum));
				
		if (globals.mbkc_status == 'ok') {
			$('#mbkc_tooltip').attr('rel','The mortgage pay-back installments cover less than 2% of the total mortgage value per year. Hence the total pay-back period will be significantly longer than usual pay-back periods.');
		} else if (globals.mbkc_status == 'yes') {
			$('#mbkc_tooltip').attr('rel','Your financial plans do not exceed your budget. Your project is feasible.');
		} else {
			$('#mbkc_tooltip').attr('rel','The possible monthly payments are lower than the approximate required monthly payments. Please contact your financial advisor in order to discuss the feasibility of your project.');
		}
	},
	showMbkc: function () {
		if(!$('#machbarkeitscheck').is(':visible')) {
			$('#machbarkeitscheck').fadeIn('slow');
			p1.initMbkc();
		}
	},
	hideMbkc: function () {
		$('#machbarkeitscheck').fadeOut('slow');
	}
}

var p2 = {
	init: function () {
	}
}

var p3 = {
	init: function () {
		$('#p3').click(function (event) {app.showPage('p4'); event.preventDefault();});
	}
}

var p4 = {
	init: function () {
		var zSpezial = globals.zinsSatzSpezial;
		this.writeFsumme();
		this.initSlider();
		this.initLinks();
		this.sliderCallback();
		globals.zinsSatzSpezial = zSpezial;
		this.enablezinsSatzSpezial();
	},
	enablezinsSatzSpezial: function () {
		if (config.version == 'offline') {
			$('#p4_zsatz input').removeAttr('readonly');
			if (globals.zinsSatzSpezial != false) {
				globals.zinsSatz = globals.zinsSatzSpezial;
				app.writeSepInput('p4_i2', 3, Math.round(globals.zinsSatzSpezial * 100));
				globals.zinsSatz = globals.zinsSatzSpezial;
				$('#p4_zsatz').addClass('spezial');
			} else {
				$('#p4_zsatz').removeClass('spezial');	
			}
			
			$('#p4_zsatz input').attr('disabled', '');
			app.autoclearSepInput('p4_i2', 3);
			$('#p4_zsatz input').bind('keyup', function () {
				globals.zinsSatzSpezial = app.readSepInput('p4_i2', 3);
				globals.zinsSatzSpezial = globals.zinsSatzSpezial / 100;
				globals.zinsSatz = globals.zinsSatzSpezial;
				$('#p4_zsatz').addClass('spezial');
			});	
		}
	},
	setSliderRange: function () {
		if (globals.finanzierungssumme < 50000) {
			this.slider2Max = 100;
			this.slider2Min = 100;		
			this.slider1Max = 0;
			this.slider1Min = 0;
		}
		else if (globals.finanzierungssumme < 70000 ) {
			this.slider2Max = 80;
			this.slider2Min = 25;		
			this.slider1Max = 75;
			this.slider1Min = 20;		
		}
		else if (globals.finanzierungssumme < 10000) {
			this.slider2Max = 85;
			this.slider2Min = 25;		
			this.slider1Max = 75;
			this.slider1Min = 15;		
		}
		else {
			this.slider2Max = 90;
			this.slider2Min = 25;		
			this.slider1Max = 75;
			this.slider1Min = 10;		
		}
		this.correctValueToRange();
	},
	correctValueToRange : function () {
		if ($("#p4_slider1").slider("value") > this.slider1Max) {
			$("#p4_slider1").slider("value", this.slider1Max);
		}
		if ($("#p4_slider1").slider("value") < this.slider1Min && $("#p4_slider1").slider("value") != 0) {
			$("#p4_slider1").slider("value", this.slider1Min);
		}
		if ($("#p4_slider2").slider("value") > this.slider2Max && $("#p4_slider2").slider("value") != 100) {
			$("#p4_slider2").slider("value", this.slider2Max);
		}
		if ($("#p4_slider2").slider("value") < this.slider2Min) {
			$("#p4_slider2").slider("value", this.slider2Min);
		}
	},
	getSliderValues: function () {
		globals.anteilVar =  Number($("#p4_slider1").slider("value"));
		globals.anteilFest =  Number($("#p4_slider2").slider("value"));
		globals.bindung = Number($("#p4_slider3").slider("value"));
	},
	readFsumme: function () {
		globals.finanzierungssumme = app.readSepInput('p4_i1', 6);
		globals.sondertilgungsrecht = Math.round(globals.finanzierungssumme * globals.anteilFest / 1000);
	},
	writeFsumme: function () {
		app.writeSepInput('p4_i1', 6, globals.finanzierungssumme);
	},
	writeTilgung: function () {
		app.writeSepInput('p4_i3', 2, globals.sondertilgung);
	},
	writeZins: function () {
		var zins = Math.round(globals.zinsSatz * 100);
		app.writeSepInput('p4_i2', 3, zins);
		var	zinsE = Math.round(globals.zinsSatzEffektiv * 100);
		app.writeSepInput('p4_i4', 3, zinsE);
		
		var	zinsFixE = Math.round(this.zinsFestEffektiv * 100);
		app.writeSepInput('p4_i5', 3, zinsFixE);	
		var	zinsFixN = Math.round(this.zinsFest * 100);
		app.writeSepInput('p4_i6', 3, zinsFixN);
		var	zinsVarE = Math.round(this.zinsVarEffektiv * 100);
		app.writeSepInput('p4_i7', 3, zinsVarE);	
		var	zinsVarN = Math.round(this.zinsVar * 100);
		app.writeSepInput('p4_i8', 3, zinsVarN);
	},
	calcZins: function () {
		// Nominal
		this.zinsFest = config.zinsen[globals.bindung];
		this.zinsVar = config.zinsen[0];
		
		globals.sondertilgung = globals.anteilVar;
		if (globals.anteilVar == 0) globals.sondertilgung = 2;
		globals.zinsSatz = ((globals.anteilFest * this.zinsFest) + (globals.anteilVar * this.zinsVar)) / 100;
		if (config.version == 'offline') {
			globals.zinsSatz = globals.zinsSatz + app.calcAufpreis();
		}
		globals.zinsSatz = Math.round(globals.zinsSatz * 100) / 100;
		
		//Effektiv
		this.zinsFestEffektiv = config.zinsenEffektiv[globals.bindung];
		this.zinsVarEffektiv = config.zinsenEffektiv[0];
		globals.zinsSatzEffektiv = ((globals.anteilFest * this.zinsFestEffektiv) + (globals.anteilVar * this.zinsVarEffektiv)) / 100;
		globals.zinsSatzEffektiv = Math.round(globals.zinsSatzEffektiv * 100) / 100;
		
		globals.zinsSatzSpezial = false;
		$('#p4_zsatz').removeClass('spezial');
	},
	sliderCallback: function () {
		this.readFsumme();
		this.setSliderRange();
		this.getSliderValues();
		this.calcZins();
		this.writeTilgung();
		this.writeZins();
		risiko = globals.anteilFest * 1.7;
		$('#p4_risiko').css('height',risiko + 'px');
	},	
	increaseZins: function () {
		changed = false;
		oldZins = globals.zinsSatz;
		if ((this.zinsFest > this.zinsVar && globals.anteilVar > 0) || (this.zinsFest < this.zinsVar && globals.anteilVar < this.slider1Max)) {	
			if (this.zinsFest > this.zinsVar) {
				this.decreaseVar();
				changed = true;
			}
			else if (this.zinsFest < this.zinsVar){
				this.increaseVar();
				changed = true;
			}
			/*else if (globals.bindung < 10) {
				globals.bindung = globals.bindung + 1;
				changed = true;
			}*/	
		}/* else if (globals.bindung < 10) {
			globals.bindung = globals.bindung + 1;
			changed = true;
		}*/
		this.calcZins();
		if(changed == true && oldZins == globals.zinsSatz) {
			this.increaseZins();
		}
		else {
			this.writeSliderValues();
		}
	},
	decreaseZins: function () {
		changed = false;
		oldZins = globals.zinsSatz;
		if ((this.zinsFest > this.zinsVar && globals.anteilVar < this.slider1Max) || (this.zinsFest < this.zinsVar && globals.anteilVar > 0)) {
			if (this.zinsFest > this.zinsVar) {
				this.increaseVar();				
				changed = true;
			}
			else if(this.zinsFest < this.zinsVar) {
				this.decreaseVar();
				changed = true;
			}
		}
		this.calcZins();
		if(changed == true && oldZins == globals.zinsSatz) {
			this.decreaseZins();
		}
		else {
			this.writeSliderValues();
		}
	},
	increaseVar: function () {
		globals.anteilVar = globals.anteilVar + 5;
		globals.anteilFest = globals.anteilFest - 5;
		if (globals.anteilVar >= this.slider1Max) {
			globals.anteilVar = this.slider1Max;
			globals.anteilFest = 100 - this.slider1Max;
		}
	},
	decreaseVar: function () {
		globals.anteilVar = globals.anteilVar - 5;
		globals.anteilFest = globals.anteilFest + 5;
		if (globals.anteilVar <= this.slider1Min) {
			globals.anteilVar = 0;
			globals.anteilFest = 100;
		}
	},
	writeSliderValues: function () {
		tmp_var =  globals.anteilVar;
		tmp_fest =  globals.anteilFest;
		tmp_bindung =  globals.bindung;
		$("#p4_slider1").slider("value", tmp_var);
		$("#p4_slider2").slider("value", tmp_fest);
		$("#p4_slider3").slider("value", tmp_bindung);
	},
	initLinks: function () {
		app.autoclearSepInput('p4_i1', 6);
		$("#p4_fup").click(function () {
			globals.finanzierungssumme = app.increaseSepInput('p4_i1', 6, 1000, 999999);
			p4.sliderCallback();
		});
		$("#p4_fdown").click(function () {
			globals.finanzierungssumme = app.decreaseSepInput('p4_i1', 6, 1000, 0);
			p4.sliderCallback();
		});
		$("#p4_tup").click(function () {
			p4.increaseVar();
			p4.writeSliderValues();
			p4.sliderCallback();
		});
		$("#p4_tdown").click(function () {
			p4.decreaseVar();
			p4.writeSliderValues();
			p4.sliderCallback();
		});
		$("#p4_zup").click(function () {
			p4.increaseZins();
		});
		$("#p4_zdown").click(function () {
			p4.decreaseZins();
		});
		$("#p4_zeup").click(function () {
			p4.increaseZins();
		});
		$("#p4_zedown").click(function () {
			p4.decreaseZins();
		});
		$("#p4_fvolumen input").bind('change', function() {p4.sliderCallback();});
		$("#p4_btnnext").click(function (event) {
			app.showPage('p5'); event.preventDefault();
		});
	},
	initSlider: function () {
		$("#p4_slider1").slider({
			orientation: "vertical",
			range: 'min',
			min: 0,
			max: 100,
			value: globals.anteilVar,
			step: 5,
			slide: function(event, ui) {
				var slider1 = $(this);
				if(ui.value <= p4.slider1Max && ui.value >= p4.slider1Min || ui.value == 0) {
					slider1.slider("value", ui.value);
					$('#value').text(ui.value);
					$('#p4_slider2').slider("value",100 - ui.value);
					return false;
				}
				else {
					$('#value').text(ui.value);
				}
				return false;
			},
			change: function() {
				p4.sliderCallback();
			}
		});
		
		$( "#p4_slider2").slider({
			orientation: "vertical",
			range: 'min',
			min: 0,
			max: 100,
			value: globals.anteilFest,
			step: 5,
			slide: function(event, ui) {
				var slider2 = $(this);
				if(ui.value <= p4.slider2Max && ui.value >= p4.slider2Min  || ui.value == 100) {
					slider2.slider("value", ui.value);
					$('#value').text(ui.value);
					$('#p4_slider1').slider("value",100 - ui.value);
					return false;
				}
				else {
					$('#value').text(ui.value);
				}
				return false;
			},
			change: function() {
				p4.sliderCallback();
			}
		});
		$( "#p4_slider3").slider({
			orientation: "vertical",
			range: 'min',
			min: 1,
			max: 10,
			value: globals.bindung,
			slide: function(event, ui) {
			},
			change: function() {
				p4.sliderCallback();
			}
		});
	}
}

var p5 = {
	init: function () {
		if (globals.anteilVar > 0) {
			globals.leistungsCase = 'b';}
		else {
			globals.leistungsCase = 'a';}
		app.showCase(globals.leistungsCase);
		$('#p5_btnnext').click(function (event) {app.showPage('p6'); event.preventDefault();});
		$('#p5_btnprev').click(function (event) {app.showPage('p4'); event.preventDefault();});
	}
}

var p6 = {
	init: function () {
		if (globals.anteilVar > 0) {
			globals.leistungsCase = 'b';}
		else {
			globals.leistungsCase = 'a';}
		app.showCase(globals.leistungsCase);		
		
		if (globals.leistungsCase == 'b') {
			$('#p6_btnnext').click(function (event) {app.showPage('p14'); event.preventDefault();});
		}
		else {
			$('#p6_btnnext').click(function (event) {app.showPage('p7'); event.preventDefault();});			
		}
		$('#p6_btnprev').click(function (event) {app.showPage('p5'); event.preventDefault();});	
	}
}

var p7 = {
	init: function () {
		app.showCase(globals.leistungsCase);
		$('#p7_btnnext').click(function (event) {app.showPage('p8'); event.preventDefault();});
		$('#p7_btnprev').click(function (event) {app.showPage('p6'); event.preventDefault();});	
		app.writeSepInput('p7_i1', 6, Math.round(globals.finanzierungssumme * globals.anteilFest / 100));
		app.writeSepInput('p7_i2', 5, globals.sondertilgungsrecht);
	}
}

var p8 = {
	init: function () {
		$('#p8_btnnext').click(function (event) {app.showPage('p9'); event.preventDefault();});
		$('#p8_btnprev').click(function (event) {app.showPage('p7'); event.preventDefault();});	
		app.writeSepInput('p8_i1', 4, app.calcSimDarlehensrate());
		app.writeSepInput('p8_i2', 2, globals.tilgungsrateprojahr_sim);
		$('#p8_i2_up').click(function () {
			globals.tilgungsrateprojahr_sim = app.increaseSepInput('p8_i2', 2, 5, 50);
			app.writeSepInput('p8_i1', 4, app.calcSimDarlehensrate());
		});
		$('#p8_i2_down').click(function () {
			globals.tilgungsrateprojahr_sim = app.decreaseSepInput('p8_i2', 2, 5, 20);
			app.writeSepInput('p8_i1', 4, app.calcSimDarlehensrate());
		});
	}
}
var p9 = {
	init: function () {
		$('#p9_btnnext').click(function (event) {app.showPage('p10'); event.preventDefault();});
		$('#p9_btnprev').click(function (event) {app.showPage('p8'); event.preventDefault();});
		
		app.writeSepInput('p9_i1', 4, globals.einnahmen);// Einnahmen
		app.writeSepInput('p9_i2', 4, globals.ausgaben + globals.darlehensrate);// Ausgaben
		app.writeSepInput('p9_i3', 4, globals.sonderausgaben);// Ausgaben

		app.autoclearSepInput('p9_i1', 4);
		$('#p9_i1 input').bind('change', function () {globals.einnahmen = app.readSepInput('p9_i1', 4); p9.calcDifference();});	
					
		app.autoclearSepInput('p9_i2', 4);
		$('#p9_i2 input').bind('change', function () {var inpdata = app.readSepInput('p9_i2', 4); globals.ausgaben = inpdata - globals.darlehensrate; p9.calcDifference();});

		app.autoclearSepInput('p9_i3', 4);
		$('#p9_i3 input').bind('change', function () {globals.sonderausgaben = app.readSepInput('p9_i3', 4); p9.calcDifference();});	
		
		this.calcDifference();
		
		$('#p9_i3_up').click(function () {globals.sonderausgaben = app.increaseSepInput('p9_i3', 4, 100, 9999); p9.calcDifference();});
		$('#p9_i3_down').click(function () {globals.sonderausgaben = app.decreaseSepInput('p9_i3', 4, 100, 0); p9.calcDifference();});
	},
	calcDifference: function () {
		var diff = 0;
		diff = globals.einnahmen - globals.ausgaben - globals.darlehensrate - globals.sonderausgaben;
		$('#p9 .box-right .value').text('$' + app.addTSeparator(diff))
	}
}
var p10 = {
	init: function () {
		$('#p10_btnnext').click(function (event) {app.showPage('p11'); event.preventDefault();});
		$('#p10_btnprev').click(function (event) {app.showPage('p9'); event.preventDefault();});	
		app.writeSepInput('p10_i1', 6, globals.finanzierungssumme);
		globals.darlehensoption = globals.finanzierungssumme; 
		if (globals.darlehensoption > 50000) globals.darlehensoption = 50000;
		app.writeSepInput('p10_i2', 6, globals.darlehensoption);
	}
}
var p11 = {
	init: function () {
		$('#p11_btnprev').click(function (event) {app.showPage('p10'); event.preventDefault();});	
		app.showCase(globals.leistungsCase);
		$('#p11_btnyes').click(function (event) {
			globals.paketFlex = true;
			app.showPage('p20'); event.preventDefault();
		});
		$('#p11_btnno').click(function (event) {
			globals.paketFlex = false;
			app.showPage('p20'); event.preventDefault();
		});
	}
}
// p12 = p5b
// p13 = p6 
var p14 = {
	init: function () {
		this.simDirection = 'up';
		app.writeSepInput('p14_i1', 3, Math.round(config.zinsen[0] * 100));
		app.writeSepInput('p14_i2', 3, Math.round(config.zinsen[10] * 100));	
		app.writeSepInput('p14_i3', 3, globals.zinslimit);
		setTimeout("p14.simulation()", 5000);
	
		$('#p14_btnprev').click(function (event) {app.showPage('p6'); event.preventDefault();});	
		$('#p14_btnnext').click(function (event) {app.showPage('p7'); event.preventDefault();});
		$('#p14_i3_up').click(function () {globals.zinslimit = app.increaseSepInput('p14_i3', 3, 10, 999); p14.showStatus();});
		$('#p14_i3_down').click(function () {globals.zinslimit = app.decreaseSepInput('p14_i3', 3, 10, 0); p14.showStatus();});
	},
	showStatus: function () {
		if (Math.round(config.zinsen[10] * 100) <= globals.zinslimit) {
			this.simDirection = 'up';
		} else {
			this.simDirection = 'down';
		}
		
		if(this.zinsFix != Math.round(config.zinsen[10] * 100)) {
			//Sim aktiv
			$('#simulation').addClass('active');
		}
		else {
			//Sim inaktiv	
			$('#simulation').removeClass('active');
		}
		if((this.zinsFix >= globals.zinslimit && this.simDirection == 'up') || (this.zinsFix <= globals.zinslimit && this.simDirection == 'down') ){
			//Limit erreicht
			$('#simulation').addClass('limit');
		} else {
			$('#simulation').removeClass('limit');
		}
	},
	simulation: function () {
		this.zinsVar = Math.round(config.zinsen[0] * 100);
		this.zinsFix = Math.round(config.zinsen[10] * 100);
		this.increaseSimulation();
	},
	increaseSimulation: function () {
		this.showStatus();
		if ((this.zinsFix < globals.zinslimit && this.simDirection == 'up') || 
			(this.zinsFix < Math.round(config.zinsen[10] * 100) && this.simDirection == 'down')) {
			this.zinsFix++;
			this.zinsVar++;
			app.writeSepInput('p14_i1', 3, (this.zinsVar > 0) ? this.zinsVar : 0 );
			app.writeSepInput('p14_i2', 3, this.zinsFix);
			setTimeout("p14.increaseSimulation()", 50);
		}
		else {
			setTimeout("p14.decreaseSimulation()", 5000);
		}
	},
	decreaseSimulation: function () {
		this.showStatus();
		if ((this.zinsFix > Math.round(config.zinsen[10] * 100) && this.simDirection == 'up') || 
			(this.zinsFix > globals.zinslimit && this.simDirection == 'down')){
		this.zinsFix--;
		this.zinsVar--;
			app.writeSepInput('p14_i1', 3, (this.zinsVar > 0) ? this.zinsVar : 0 );
			app.writeSepInput('p14_i2', 3, this.zinsFix);
			setTimeout("p14.decreaseSimulation()", 50);
		}
		else {
			setTimeout("p14.increaseSimulation()", 5000);
		}
	}
}
// p15 = p7b
// p16 = p8
// p17 = p9
// p18 = p10
// p19 = p11b
var p20 = {
	init: function () {
		$('#p20 p').mouseover(function (event) {$(this).addClass('hover')}).mouseout(function (event) {$(this).removeClass('hover')});
		$('#p20_btna').click(function (event) {
			globals.sicherPrio = 'a';
			app.showPage('p21'); event.preventDefault();
		});
		$('#p20_btnb').click(function (event) {
			globals.sicherPrio = 'b';
			app.showPage('p25'); event.preventDefault();
		});
		$('#p20_btnprev').click(function (event) {app.showPage('p11'); event.preventDefault();});	
	}
}
var p21 = {
	init: function () {
		app.writeSepInput('p21_i1', 4, globals.einnahmen);
		app.writeSepInput('p21_i2', 4, globals.ausgaben);
		app.writeSepInput('p21_i3', 4, globals.darlehensrate);
		app.writeSepInput('p21_i4', 3, globals.absicherungprozent);

		app.autoclearSepInput('p21_i1', 4);
		$('#p21_i1 input').bind('change', function () {globals.einnahmen = app.readSepInput('p21_i1', 4); p21.calcDifference();});	
	
		app.autoclearSepInput('p21_i2', 4);
		$('#p21_i2 input').bind('change', function () {globals.ausgaben = app.readSepInput('p21_i2', 4); p21.calcDifference();});

		app.autoclearSepInput('p21_i4', 3);
		$('#p21_i4 input').bind('change', function () {globals.absicherungprozent = app.readSepInput('p21_i4', 4); p21.calcDifference();});	
				
		this.calcDifference();
		
		$('#p21_i1_up').click(function () {globals.einnahmen = app.increaseSepInput('p21_i1', 4, 100, 9999); p21.calcDifference();});
		$('#p21_i1_down').click(function () {globals.einnahmen = app.decreaseSepInput('p21_i1', 4, 100, 0); p21.calcDifference();});
		$('#p21_i2_up').click(function () {globals.ausgaben = app.increaseSepInput('p21_i2', 4, 100, 9999); p21.calcDifference();});
		$('#p21_i2_down').click(function () {globals.ausgaben = app.decreaseSepInput('p21_i2', 4, 100, 0); p21.calcDifference();});
		$('#p21_i4_up').click(function () {globals.absicherungprozent = app.increaseSepInput('p21_i4', 3, 10, 100); p21.calcDifference();});
		$('#p21_i4_down').click(function () {globals.absicherungprozent = app.decreaseSepInput('p21_i4', 3, 10, 0); p21.calcDifference();});
		

		
		$('#p21_btnprev').click(function (event) {
			if (globals.sicherPrio == 'a') {
				app.showPage('p20'); event.preventDefault();
			}
			else {
				app.showPage('p22'); event.preventDefault();	
			}
		});
		$('#p21_btnnext').click(function (event) {
			app.showPage('p22'); event.preventDefault();
		});
	},
	calcDifference: function () {
		var difference = Math.round(globals.einnahmen - globals.ausgaben - globals.darlehensrate - (globals.einnahmen * globals.absicherungprozent / 100));
		if (difference < 0) {
			$('#p21 .box-right').addClass('negative');	
		} else {
			$('#p21 .box-right').removeClass('negative');
		}
		$('#p21 .box-right .value').text('$' + app.addTSeparator(difference))
	}
}
var p22 = {
	init: function () {
		$('#p22_btnprev').click(function (event) {
			app.showPage('p21'); event.preventDefault();
		});
		$('#p22_btnnext').click(function (event) {
			if (globals.sicherPrio == 'a') {
				app.showPage('p25'); event.preventDefault();
			}
			else {
				app.showPage('p26'); event.preventDefault();	
			}
		});
		
		if(!globals.hyposchutz_seen) {
			globals.hyposchutz_seen = 1; globals.hyposchutz = 1;
		}
		
		if (globals.hyposchutz == 1) {
			$('input:radio[name=p22_i1]').filter('[value=1]').attr('checked', true);
		} else {
			$('input:radio[name=p22_i1]').filter('[value=0]').attr('checked', true);
		}		
		$('input:radio[name=p22_i1]').bind('change',function () {
			globals.hyposchutz = Number($(this).val());
			app.checkSecure();
		})

		if(!globals.risikolv_seen) {
			globals.risikolv_seen = 1; globals.risikolv = 1;
		}
		
		if (globals.risikolv == 1) {
			$('input:radio[name=p22_i2]').filter('[value=1]').attr('checked', true);
		} else {
			$('input:radio[name=p22_i2]').filter('[value=0]').attr('checked', true);
		}
		$('input:radio[name=p22_i2]').bind('change',function () {
			globals.risikolv = Number($(this).val());
			app.checkSecure();
		})
		
	}
}
var p23 = {
	init: function () {
		$('#p23_btnprev').click(function (event) {
			if (globals.sicherPrio == 'a') {
				app.showPage('p22'); event.preventDefault();
			}
			else {
				app.showPage('p20'); event.preventDefault();
			}
		});
		$('#p23_btnnext').click(function (event) {
			app.showPage('p24'); event.preventDefault();	
		});
	}
}

var p24 = {
	init: function () {
		$('#p24_btnprev').click(function (event) {
			app.showPage('p23'); event.preventDefault();
		});
		$('#p24_btnnext').click(function (event) {
			app.showPage('p25'); event.preventDefault();	
		});
	}
}

var p25 = {
	init: function () {
		$('#p25_btnprev').click(function (event) {
			app.showPage('p22'); event.preventDefault();
		});
		$('#p25_btnnext').click(function (event) {
			if (globals.sicherPrio == 'a') {
				app.showPage('p26'); event.preventDefault();
			}
			else {
				app.showPage('p21'); event.preventDefault();	
			}	
		});
		
		if(!globals.prohaus_seen) {
			globals.prohaus_seen = 1; globals.prohaus = 1;
		}
		
		if (globals.prohaus == 1) {
			$('input:radio[name=p25_i1]').filter('[value=1]').attr('checked', true);
		} else {
			$('input:radio[name=p25_i1]').filter('[value=0]').attr('checked', true);
		}		
		$('input:radio[name=p25_i1]').bind('change',function () {
			globals.prohaus = Number($(this).val());
			app.checkSecure();
		})
		
		if (globals.indsachv == 1) {
			$('input:radio[name=p25_i2]').filter('[value=1]').attr('checked', true);
		} else {
			$('input:radio[name=p25_i2]').filter('[value=0]').attr('checked', true);
		}
		$('input:radio[name=p25_i2]').bind('change',function () {
			globals.indsachv = Number($(this).val());
			app.checkSecure();
		})	
	}
}

var p26 = {
	init: function () {
		app.checkSecure();
		globals.box3_status = 1;
		if (globals.paketSicher && globals.paketFlex) {
			app.showCase('a');
		} else if (!globals.paketSicher && globals.paketFlex) {
			app.showCase('b');			
		} else if (globals.paketSicher && !globals.paketFlex) {
			app.showCase('c');			
		}
		else {
			app.showPage('p29');
		}
		$('#p26_btnnext').click(function (event) {
			app.showPage('p1');
		});
		$('#p26_btnp2').click(function (event) {
			app.showPage('p6');
		});
		$('#p26_btnp3').click(function (event) {
			app.showPage('p20');
		});
		$('#p26_btnprev').click(function (event) {
			if (globals.sicherPrio == 'a') {
				app.showPage('p25'); event.preventDefault();
			}
			else {
				app.showPage('p22'); event.preventDefault();	
			}	
		});
	}
}

var p29 = {
	init: function () {
		$('#p29_btnyes').click(function (event) {
			app.showPage('p6');
		});
		$('#p29_btnnext').click(function (event) {
			app.showPage('p1');
		});
		$('#p29_btnprev').click(function (event) {
			if (globals.sicherPrio == 'a') {
				app.showPage('p25'); event.preventDefault();
			}
			else {
				app.showPage('p22'); event.preventDefault();	
			}	
		});
	}
}

var p30 = {
	init: function () {
		this.bindLinks();
	},
	bindLinks: function () {
		$('#p30 .p30_box').hover(
		  function () {
		    $(this).addClass("hover");
		  },
		  function () {
		    $(this).removeClass("hover");
		  }
		);
		$('#p30_box1').click(function (event) {app.showPage('p31'); event.preventDefault();});
		$('#p30_box2').click(function (event) {app.showPage('p37'); event.preventDefault();});
		$('#p30_box3').click(function (event) {app.showPage('p46'); event.preventDefault();});
		$('#p30_box4').click(function (event) {app.showPage('p42'); event.preventDefault();});
		$('#p30_btnprev').click(function (event) {app.showPage('p1'); event.preventDefault();});
	}
}

var p31 = {
	init: function () {
		this.showFieldset(1);
		this.bindLinks();
		this.writeHeader();
		$('#kaufen_2_kommentar').val(globals.fsumme_kaufen_2_kommentar);
		$('#kaufen_3_kommentar').val(globals.fsumme_kaufen_3_kommentar);
	},
	calcNebenkosten: function () {
		var nebenkosten = 0;
		var preis = globals.fsumme_kaufen_1_1;
		var makler = globals.fsumme_kaufen_1_p_3 / 100;
		var notar = globals.fsumme_kaufen_1_p_4 / 100;
		var steuer = globals.grunderwerbsteuer / 100;
		nebenkosten = Math.round(((preis * makler) + (preis * notar) + (preis * steuer)) / 100);
		if (nebenkosten == 0) nebenkosten = '';
		$('#kaufen_1_2').val(nebenkosten);
		app.updateFsummeFieldset('kaufen_1', 2);
		p31.writeHeader();
	},
	
	showFieldset: function (nr) {
  		$('#p31_btnnext').show();
    	$('#p31_btnprev').show();
		switch (nr) {
   			case 1:
        		$('#p31_btnprev').hide();
   				app.showFsummeFieldset(1);
  				app.writeFsummeVars('kaufen_1', 2);
  				$('#p31 .fieldset_1 #kaufen_1_1').bind('keyup', function (event) {
  					globals.fsumme_kaufen_1_1 = app.removeTSeparator($('#kaufen_1_1').val());
  					p31.calcNebenkosten();
  				});
  				$('#p31 .fieldlist_1 .sepInputs input').bind('keyup', function (event) {
  					globals.fsumme_kaufen_1_p_3 = app.readSepInput('p31_i1', 3);
  					globals.fsumme_kaufen_1_p_4 = app.readSepInput('p31_i2', 3);
  					globals.grunderwerbsteuer = app.readSepInput('p31_i3', 3);
  					p31.calcNebenkosten();
  				});
  				 app.autoclearSepInput('p31_i1', 3);
  				 app.autoclearSepInput('p31_i2', 3);
  				 app.autoclearSepInput('p31_i3', 3);
   				$('#p31 .fieldset_1 #kaufen_1_2').bind('keyup', function (event) {
  					app.updateFsummeFieldset('kaufen_1', 2);
					p31.writeHeader();
  				});	
  				app.writeSepInput('p31_i3', 3, globals.grunderwerbsteuer);
  				app.writeSepInput('p31_i1', 3, globals.fsumme_kaufen_1_p_3);
  				app.writeSepInput('p31_i2', 3, globals.fsumme_kaufen_1_p_4);
   			break;
   			case 2:
   				app.showFsummeFieldset(2);
  				app.writeFsummeVars('kaufen_2', 10);
  				$('#p31 .fieldset_2 input').not('#kaufen_2_sum').bind('keyup', function (event) {app.updateFsummeFieldset('kaufen_2', 10); p31.writeHeader();});
  				$('#kaufen_2_sum').bind('keyup', function (event) {
  					globals.fsumme_kaufen_2_sum = app.removeTSeparator($('#kaufen_2_sum').val());
  					var sum = app.addTSeparator(globals.fsumme_kaufen_2_sum);
  					if (sum == 0) sum = '';
  					$('#kaufen_2_sum').val(sum);
  					p31.writeHeader();
  				});
   			break;
   			case 3:
        		$('#p31_btnnext').hide();
   				app.showFsummeFieldset(3);
  				app.writeFsummeVars('kaufen_3', 8);
  				$('#p31 .fieldset_3 input').bind('keyup', function (event) {app.updateFsummeFieldset('kaufen_3', 8); p31.writeHeader();});
  					var used = app.addTSeparator(globals.fsumme_kaufen_3_used);
  					if (used == 0) used = '';
  					$('#kaufen_3_used').val(used);
  				$('#kaufen_3_used').bind('keyup', function (event) {
  					globals.fsumme_kaufen_3_used = app.removeTSeparator($('#kaufen_3_used').val());
  					var used = app.addTSeparator(globals.fsumme_kaufen_3_used);
  					if (used == 0) used = '';
  					$('#kaufen_3_used').val(used);
  					p31.writeHeader();
  				});
   			break;
   			default:
   				this.takeOver();
   			break;		
			
		}
		$('input.comment').unbind('change').unbind('keyup');	
	},
	writeHeader: function () {
		$('#fsumme_kaufen_header .field_1 .value').html(app.addTSeparator(globals.fsumme_kaufen_1_sum));
		$('#fsumme_kaufen_header .field_2 .value').html(app.addTSeparator(globals.fsumme_kaufen_2_sum));
		$('#fsumme_kaufen_header .field_3 .value').html(app.addTSeparator(globals.fsumme_kaufen_3_used));
		$('#fsumme_kaufen_header .field_4 .value').html(app.addTSeparator(p31.sumFieldsets()));
	},
	sumFieldsets: function () {
		var sum = 0;
		sum = globals.fsumme_kaufen_1_sum + globals.fsumme_kaufen_2_sum - globals.fsumme_kaufen_3_used;
		return sum;
	},
	takeOver: function () {
		globals.finanzierungssumme = this.sumFieldsets();
		globals.box1_status = 1;
		globals.fsumme_bedarfstyp = 1
		globals.fsumme_kaufen_2_kommentar = $('#kaufen_2_kommentar').val();
		globals.fsumme_kaufen_3_kommentar = $('#kaufen_3_kommentar').val();
		app.showPage('p1');
	},
	showNextFieldset: function () {
		var next = globals.fsumme_currentFieldset + 1;
		this.showFieldset(next);
	},
	showPrevFieldset: function () {
		var next = globals.fsumme_currentFieldset - 1;
		this.showFieldset(next);
	},
	bindLinks: function () {
		$('#p31 .field_1').click(function (event) {p31.showFieldset(1);});
		$('#p31 .field_2').click(function (event) {p31.showFieldset(2);});
		$('#p31 .field_3').click(function (event) {p31.showFieldset(3);});
		$('#p31 .field').mouseover(function (event) {$(this).addClass('hover')});
		$('#p31 .field').mouseout(function (event) {$(this).removeClass('hover')});
		$('#p31 .field_4').unbind('click').unbind('mouseover');
		$('#p31_btnprev').click(function (event) {p31.showPrevFieldset(); event.preventDefault();});	
		$('#p31_btnnext').click(function (event) {p31.showNextFieldset(); event.preventDefault();});		
		$('#p31_btnabort').click(function (event) {app.showPage('p1'); event.preventDefault();});				
		$('#p31_btntakeover').click(function (event) {p31.takeOver(); event.preventDefault();});
		$('#p31_i1_up').click(function () {
			globals.fsumme_kaufen_1_p_3 = app.increaseSepInput('p31_i1', 3, 10, 999);
			p31.calcNebenkosten();
		});
		$('#p31_i1_down').click(function () {
			globals.fsumme_kaufen_1_p_3 = app.decreaseSepInput('p31_i1', 3, 10, 0);
			p31.calcNebenkosten();
		});
		$('#p31_i2_up').click(function () {
			globals.fsumme_kaufen_1_p_4 = app.increaseSepInput('p31_i2', 3, 10, 999);
			p31.calcNebenkosten();
		});
		$('#p31_i2_down').click(function () {
			globals.fsumme_kaufen_1_p_4 = app.decreaseSepInput('p31_i2', 3, 10, 0);
			p31.calcNebenkosten();
		});
		$('#p31_i3_up').click(function () {
			globals.grunderwerbsteuer = app.increaseSepInput('p31_i3', 3, 10, 999);
			p31.calcNebenkosten();
		});
		$('#p31_i3_down').click(function () {
			globals.grunderwerbsteuer = app.decreaseSepInput('p31_i3', 3, 10, 0);
			p31.calcNebenkosten();
		});
	}
}

var p37 = {
	init: function () {
		this.showFieldset(1);
		this.bindLinks();
		this.writeHeader();
		$('#bauen_2_kommentar').val(globals.fsumme_bauen_2_kommentar);
		$('#bauen_3_kommentar').val(globals.fsumme_bauen_3_kommentar);
	},
	calcNebenkosten: function () {
		var nebenkosten = 0;
		var preis = globals.fsumme_bauen_1_1;
		var makler = globals.fsumme_bauen_1_p_3 / 100;
		var notar = globals.fsumme_bauen_1_p_4 / 100;
		steuer  = globals.grunderwerbsteuer / 100;
		nebenkosten = Math.round(((preis * makler) + (preis * notar) + (preis * steuer)) / 100);
		if (nebenkosten == 0) nebenkosten = '';
		$('#bauen_1_2').val(nebenkosten);
		app.updateFsummeFieldset('bauen_1', 2);
  		p37.writeHeader();
	},
	showFieldset: function (nr) {
  		$('#p37_btnnext').show();
    	$('#p37_btnprev').show();
		switch (nr) {
   			case 1:
       			$('#p37_btnprev').hide();
   				app.showFsummeFieldset(1);
  				app.writeFsummeVars('bauen_1', 2);
  				$('#p37 .fieldset_1 #bauen_1_1').bind('keyup', function (event) {
  					globals.fsumme_bauen_1_1 = app.removeTSeparator($('#bauen_1_1').val());
  					p37.calcNebenkosten();
  				});
   				$('#p37 .fieldlist_1 .sepInputs input').bind('keyup', function (event) {
  					globals.fsumme_bauen_1_p_3 = app.readSepInput('p37_i1', 3);
  					globals.fsumme_bauen_1_p_4 = app.readSepInput('p37_i2', 3);
  					globals.grunderwerbsteuer = app.readSepInput('p37_i3', 3);
  					p37.calcNebenkosten();
  				});
  				 app.autoclearSepInput('p37_i1', 3);
  				 app.autoclearSepInput('p37_i2', 3);
  				 app.autoclearSepInput('p37_i3', 3);
   				$('#p37 .fieldset_1 #bauen_1_2').bind('keyup', function (event) {
  					app.updateFsummeFieldset('bauen_1', 2);
  					p37.writeHeader();
  				});	
  				app.writeSepInput('p37_i3', 3, globals.grunderwerbsteuer);
  				app.writeSepInput('p37_i1', 3, globals.fsumme_bauen_1_p_3);
  				app.writeSepInput('p37_i2', 3, globals.fsumme_bauen_1_p_4); 
  			break;
   			case 2:
   				app.showFsummeFieldset(2);
  				app.writeFsummeVars('bauen_2', 11);
  				$('#p37 .fieldset_2 input').not('#bauen_2_sum').bind('keyup', function (event) {app.updateFsummeFieldset('bauen_2', 11); p37.writeHeader();});
  				$('#bauen_2_sum').bind('keyup', function (event) {
  					globals.fsumme_bauen_2_sum = app.removeTSeparator($('#bauen_2_sum').val());
  					var sum = app.addTSeparator(globals.fsumme_bauen_2_sum);
  					if (sum == 0) sum = '';
  					$('#bauen_2_sum').val(sum);
  					p37.writeHeader();
  				});
   			break;
   			case 3:
       			$('#p37_btnnext').hide();
   				app.showFsummeFieldset(3);
  				app.writeFsummeVars('bauen_3', 8);
  				$('#p37 .fieldset_3 input').bind('keyup', function (event) {app.updateFsummeFieldset('bauen_3', 8); p37.writeHeader();});
   					var used = app.addTSeparator(globals.fsumme_bauen_3_used);
  					if (used == 0) used = '';
  					$('#bauen_3_used').val(used);
  				$('#bauen_3_used').bind('keyup', function (event) {
  					globals.fsumme_bauen_3_used = app.removeTSeparator($('#bauen_3_used').val());
   					var used = app.addTSeparator(globals.fsumme_bauen_3_used);
  					if (used == 0) used = '';
  					$('#bauen_3_used').val(used);
  					p37.writeHeader();
  				});
   			break;
   			default:
   				this.takeOver();
   			break;			
		}
		$('input.comment').unbind('change').unbind('keyup');		
	},
	writeHeader: function () {
		$('#fsumme_bauen_header .field_1 .value').html(app.addTSeparator(globals.fsumme_bauen_1_sum));
		$('#fsumme_bauen_header .field_2 .value').html(app.addTSeparator(globals.fsumme_bauen_2_sum));
		$('#fsumme_bauen_header .field_3 .value').html(app.addTSeparator(globals.fsumme_bauen_3_used));
		$('#fsumme_bauen_header .field_4 .value').html(app.addTSeparator(p37.sumFieldsets()));
	},
	sumFieldsets: function () {
		var sum = 0;
		sum = globals.fsumme_bauen_1_sum + globals.fsumme_bauen_2_sum - globals.fsumme_bauen_3_used;
		return sum;
	},
	takeOver: function () {
		globals.finanzierungssumme = this.sumFieldsets();
		globals.box1_status = 1;
		globals.fsumme_bedarfstyp = 2;
		globals.fsumme_bauen_2_kommentar = $('#bauen_2_kommentar').val();
		globals.fsumme_bauen_3_kommentar = $('#bauen_3_kommentar').val();
		app.showPage('p1');
	},
	showNextFieldset: function () {
		var next = globals.fsumme_currentFieldset + 1;
		this.showFieldset(next);
	},
	showPrevFieldset: function () {
		var next = globals.fsumme_currentFieldset - 1;
		this.showFieldset(next);
	},
	bindLinks: function () {
		$('#p37 .field_1').click(function (event) {p37.showFieldset(1);});
		$('#p37 .field_2').click(function (event) {p37.showFieldset(2);});
		$('#p37 .field_3').click(function (event) {p37.showFieldset(3);});
		$('#p37 .field').mouseover(function (event) {$(this).addClass('hover')});
		$('#p37 .field').mouseout(function (event) {$(this).removeClass('hover')});
		$('#p37 .field_4').unbind('click').unbind('mouseover');
		$('#p37_btnabort').click(function (event) {app.showPage('p31'); event.preventDefault();});				
		$('#p37_btntakeover').click(function (event) {p37.takeOver(); event.preventDefault();});							
		$('#p37_btnprev').click(function (event) {p37.showPrevFieldset(); event.preventDefault();});
		$('#p37_btnnext').click(function (event) {p37.showNextFieldset(); event.preventDefault();});
		$('#p37_i1_up').click(function () {
			globals.fsumme_bauen_1_p_3 = app.increaseSepInput('p37_i1', 3, 10, 999);
			p37.calcNebenkosten();
			p37.writeHeader();
		});
		$('#p37_i1_down').click(function () {
			globals.fsumme_bauen_1_p_3 = app.decreaseSepInput('p37_i1', 3, 10, 0);
			p37.calcNebenkosten();
			p37.writeHeader();
		});
		$('#p37_i2_up').click(function () {
			globals.fsumme_bauen_1_p_4 = app.increaseSepInput('p37_i2', 3, 10, 999);
			p37.calcNebenkosten();
			p37.writeHeader();
		});
		$('#p37_i2_down').click(function () {
			globals.fsumme_bauen_1_p_4 = app.decreaseSepInput('p37_i2', 3, 10, 0);
			p37.calcNebenkosten();
			p37.writeHeader();
		});
		$('#p37_i3_up').click(function () {
			globals.grunderwerbsteuer = app.increaseSepInput('p37_i3', 3, 10, 999);
			p37.calcNebenkosten();
		});
		$('#p37_i3_down').click(function () {
			globals.grunderwerbsteuer = app.decreaseSepInput('p37_i3', 3, 10, 0);
			p37.calcNebenkosten();
		});
	}
}

var p42 = {
	init: function () {
		this.showFieldset(1);
		this.bindLinks();
		this.writeHeader();
		$('#modernisieren_1_kommentar').val(globals.fsumme_modernisieren_1_kommentar);
		$('#modernisieren_2_kommentar').val(globals.fsumme_modernisieren_2_kommentar);
	},
	showFieldset: function (nr) {
  		$('#p42_btnnext').show();
    	$('#p42_btnprev').show();
		switch (nr) {
   			case 1:
       			$('#p42_btnprev').hide();
   				app.showFsummeFieldset(1);
   				
   				var sum = app.addTSeparator(globals.fsumme_modernisieren_1_sum);
  				p42.writeHeader();	
  				app.writeFsummeVars('modernisieren_1', 7);
  				$('#p42 .fieldset_1 input').not('#modernisieren_1_sum').bind('keyup', function (event) {app.updateFsummeFieldset('modernisieren_1', 7); p42.writeHeader();});
  				if (sum != 0) $('#modernisieren_1_sum').val(sum);
			
  				$('#modernisieren_1_sum').bind('keyup', function (event) {
  					globals.fsumme_modernisieren_1_sum = app.removeTSeparator($('#modernisieren_1_sum').val());
   					var sum = app.addTSeparator(globals.fsumme_modernisieren_1_sum);
  					if (sum == 0) sum = '';
  					$('#modernisieren_1_sum').val(sum);
  					p42.writeHeader();
  				});
   			break;
   			case 2:
       			$('#p42_btnnext').hide();
   				app.showFsummeFieldset(2);
  				app.writeFsummeVars('modernisieren_2', 8);
  				$('#p42 .fieldset_2 input').bind('keyup', function (event) {app.updateFsummeFieldset('modernisieren_2', 8); p42.writeHeader();});
   					var used = app.addTSeparator(globals.fsumme_modernisieren_2_used);
  					if (used == 0) used = '';
  					$('#modernisieren_2_used').val(used);
  				$('#modernisieren_2_used').bind('keyup', function (event) {
  					globals.fsumme_modernisieren_2_used = app.removeTSeparator($('#modernisieren_2_used').val());
   					var used = app.addTSeparator(globals.fsumme_modernisieren_2_used);
  					if (used == 0) used = '';
  					$('#modernisieren_2_used').val(used);
  					p42.writeHeader();
  				});
   			break;
   			default:
   				this.takeOver();
   			break;
		}
		$('input.comment').unbind('change').unbind('keyup');
	},
	writeHeader: function () {
		$('#fsumme_modernisieren_header .field_1 .value').html(app.addTSeparator(globals.fsumme_modernisieren_1_sum));
		$('#fsumme_modernisieren_header .field_2 .value').html(app.addTSeparator(globals.fsumme_modernisieren_2_used));
		$('#fsumme_modernisieren_header .field_3 .value').html(app.addTSeparator(p42.sumFieldsets()));
	},
	sumFieldsets: function () {
		var sum = 0;
		sum = globals.fsumme_modernisieren_1_sum - globals.fsumme_modernisieren_2_used;
		return sum;
	},
	takeOver: function () {
		globals.finanzierungssumme = this.sumFieldsets();
		globals.box1_status = 1;
		globals.fsumme_bedarfstyp = 4;
		globals.fsumme_modernisieren_1_kommentar = $('#modernisieren_1_kommentar').val();
		globals.fsumme_modernisieren_2_kommentar = $('#modernisieren_2_kommentar').val();
		app.showPage('p1');
	},
	showNextFieldset: function () {
		var next = globals.fsumme_currentFieldset + 1;
		this.showFieldset(next);
	},
	showPrevFieldset: function () {
		var next = globals.fsumme_currentFieldset - 1;
		this.showFieldset(next);
	},
	bindLinks: function () {
		$('#p42 .field_1').click(function (event) {p42.showFieldset(1);});
		$('#p42 .field_2').click(function (event) {p42.showFieldset(2);});
		$('#p42 .field').mouseover(function (event) {$(this).addClass('hover')});
		$('#p42 .field').mouseout(function (event) {$(this).removeClass('hover')});
		$('#p42 .field_3').unbind('click').unbind('mouseover');
		$('#p42_btnabort').click(function (event) {app.showPage('p1'); event.preventDefault();});				
		$('#p42_btntakeover').click(function (event) {p42.takeOver(); event.preventDefault();});
		$('#p42_btnprev').click(function (event) {p42.showPrevFieldset(); event.preventDefault();});
		$('#p42_btnnext').click(function (event) {p42.showNextFieldset(); event.preventDefault();});
	}
}

var p46 = {
	init: function () {
		this.showFieldset(1);
		this.bindLinks();
		this.writeHeader();
		$('#anschluss_2_kommentar').val(globals.fsumme_anschluss_2_kommentar);
		$('#anschluss_3_kommentar').val(globals.fsumme_anschluss_3_kommentar);
	},
	calcRestschuld: function () {
		var rs = 0;
		
		var fs = globals.fsumme_anschluss_fsumme;
		var i = globals.fsumme_anschluss_zinssatz / 10000 / 12;
		var i_b = i+1;
		var n = globals.fsumme_anschluss_dauer * 12;
		var D = globals.fsumme_anschluss_drate;
		
		if (i_b == 1) {
			rs = 0;
		}
		else {
			rs = fs * Math.pow(i_b, n) - D * ((1 - Math.pow(i_b, n)) / (1 - i_b ));
		}
		if (rs < 0) rs = 0;
		rs = Math.round(rs);
		globals.fsumme_anschluss_1_1 = rs;
		globals.fsumme_anschluss_1_sum = rs;
		app.writeFsummeVars('anschluss_1', 1);
		return rs;
	},
	showFieldset: function (nr) {
  		$('#p46_btnnext').show();
    	$('#p46_btnprev').show();
		switch (nr) {
   			case 1:
       			$('#p46_btnprev').hide();
   				app.showFsummeFieldset(1);
  				app.writeFsummeVars('anschluss_1', 1);

   					var fs = app.addTSeparator(globals.fsumme_anschluss_fsumme);
  					if (fs == 0) fs = '';
  					$('#anschluss_fs').val(fs);
  					
   					var dr = app.addTSeparator(globals.fsumme_anschluss_drate);
  					if (dr == 0) dr = '';
  					$('#anschluss_dr').val(dr);
  					
  				
  				$('#p46 .fieldset_1 input').bind('keyup', function (event) {app.updateFsummeFieldset('anschluss_1', 1); p46.writeHeader();});
  				$('#anschluss_fs').bind('keyup', function (event) {
  					globals.fsumme_anschluss_fsumme = app.removeTSeparator($('#anschluss_fs').val());
   					var fs = app.addTSeparator(globals.fsumme_anschluss_fsumme);
  					if (fs == 0) fs = '';
  					$('#anschluss_fs').val(fs);
  					p46.calcRestschuld();
  				});
  				$('#anschluss_dr').bind('keyup', function (event) {
  					globals.fsumme_anschluss_drate = app.removeTSeparator($('#anschluss_dr').val());
   					var dr = app.addTSeparator(globals.fsumme_anschluss_drate);
  					if (dr == 0) dr = '';
  					$('#anschluss_dr').val(dr);
  					p46.calcRestschuld();
  				});
				$('#p46_i1 input').bind('keyup', function () {
					globals.fsumme_anschluss_zinssatz = app.readSepInput('p46_i1', 3);
					p46.calcRestschuld();
				});
				$('#p46_i2 input').bind('keyup', function () {
					globals.fsumme_anschluss_dauer = app.readSepInput('p46_i2', 2);
					p46.calcRestschuld();
				});
 				app.autoclearSepInput('p46_i1', 2);
 				app.autoclearSepInput('p46_i2', 2);
   			break;
   			case 2:
   				app.showFsummeFieldset(2);
  				app.writeFsummeVars('anschluss_2', 10);
  				$('#p46 .fieldset_2 input').not('#anschluss_2_sum').bind('keyup', function (event) {app.updateFsummeFieldset('anschluss_2', 10); p46.writeHeader();});
  				$('#anschluss_2_sum').bind('keyup', function (event) {
  					globals.fsumme_anschluss_2_sum = app.removeTSeparator($('#anschluss_2_sum').val());
  					var sum = app.addTSeparator(globals.fsumme_anschluss_2_sum);
  					if (sum == 0) sum = '';
  					$('#anschluss_2_sum').val(sum);
  					p46.writeHeader();
  				});
   			break;
   			case 3:
       			$('#p46_btnnext').hide();
   				app.showFsummeFieldset(3);
  				app.writeFsummeVars('anschluss_3', 6);
  				$('#p46 .fieldset_3 input').bind('keyup', function (event) {app.updateFsummeFieldset('anschluss_3', 6); p46.writeHeader();});
   					var used = app.addTSeparator(globals.fsumme_anschluss_3_used);
  					if (used == 0) used = '';
  					$('#anschluss_3_used').val(used);
  				$('#anschluss_3_used').bind('keyup', function (event) {
  					globals.fsumme_anschluss_3_used = app.removeTSeparator($('#anschluss_3_used').val());
   					var used = app.addTSeparator(globals.fsumme_anschluss_3_used);
  					if (used == 0) used = '';
  					$('#anschluss_3_used').val(used);
  					p46.writeHeader();
  				});
   			break;
   			default:
   				this.takeOver();
   			break;	
		}		
		$('input.comment').unbind('change').unbind('keyup');
	},
	writeHeader: function () {
		$('#fsumme_anschluss_header .field_1 .value').html(app.addTSeparator(globals.fsumme_anschluss_1_sum));
		$('#fsumme_anschluss_header .field_2 .value').html(app.addTSeparator(globals.fsumme_anschluss_2_sum));
		$('#fsumme_anschluss_header .field_3 .value').html(app.addTSeparator(globals.fsumme_anschluss_3_used));
		$('#fsumme_anschluss_header .field_4 .value').html(app.addTSeparator(p46.sumFieldsets()));
	},
	sumFieldsets: function () {
		var sum = 0;
		sum = globals.fsumme_anschluss_1_sum + globals.fsumme_anschluss_2_sum - globals.fsumme_anschluss_3_used;
		return sum;
	},
	takeOver: function () {
		globals.finanzierungssumme = this.sumFieldsets();
		globals.box1_status = 1;
		globals.fsumme_bedarfstyp = 3;
		globals.fsumme_anschluss_2_kommentar = $('#anschluss_2_kommentar').val();
		globals.fsumme_anschluss_3_kommentar = $('#anschluss_3_kommentar').val();
		app.showPage('p1');
	},
	showNextFieldset: function () {
		var next = globals.fsumme_currentFieldset + 1;
		this.showFieldset(next);
	},
	showPrevFieldset: function () {
		var next = globals.fsumme_currentFieldset - 1;
		this.showFieldset(next);
	},
	bindLinks: function () {
		$('#p46_i1_up').click(function () {
			globals.fsumme_anschluss_zinssatz = app.increaseSepInput('p46_i1', 3, 1, 999);
			p46.calcRestschuld();
		});
		$('#p46_i1_down').click(function () {
			globals.fsumme_anschluss_zinssatz = app.decreaseSepInput('p46_i1', 3, 1, 0);
			p46.calcRestschuld();
		});
		$('#p46_i2_up').click(function () {
			globals.fsumme_anschluss_dauer = app.increaseSepInput('p46_i2', 2, 1, 99);
			p46.calcRestschuld();
		});
		$('#p46_i2_down').click(function () {
			globals.fsumme_anschluss_dauer = app.decreaseSepInput('p46_i2', 2, 1, 0);
			p46.calcRestschuld();
		});
		$('#p46 .field_1').click(function (event) {p46.showFieldset(1);});
		$('#p46 .field_2').click(function (event) {p46.showFieldset(2);});
		$('#p46 .field_3').click(function (event) {p46.showFieldset(3);});
		$('#p46 .field').mouseover(function (event) {$(this).addClass('hover')});
		$('#p46 .field').mouseout(function (event) {$(this).removeClass('hover')});
		$('#p46 .field_4').unbind('click').unbind('mouseover');
		$('#p46_btnabort').click(function (event) {app.showPage('p1'); event.preventDefault();});				
		$('#p46_btntakeover').click(function (event) {p46.takeOver(); event.preventDefault();});
		$('#p46_btnprev').click(function (event) {p46.showPrevFieldset(); event.preventDefault();});
		$('#p46_btnnext').click(function (event) {p46.showNextFieldset(); event.preventDefault();});
	}
}

var p48 = {
	init: function () {
		this.phase = 1;
		this.phaseCallback();
		this.bindLinks();
		if (!globals.darlehen_sk_seen) {
			globals.darlehen_sk = 1;
			globals.darlehen_sk_seen = 1;
		}
		this.setCb('p48_cb_1', globals.darlehen_sk);
		this.setCb('p48_cb_2', globals.darlehen_hand);
		this.setCb('p48_cb_3', globals.darlehen_lbs);
		this.setCb('p48_cb_4', globals.darlehen_kfw);
		this.setCb('p48_cb_5', globals.darlehen_sonstiges);
	},
	bindLinks: function () {
		$('#p48_i1_1').val(globals.darlehen_sonstigesDesc);
		$('#p48_i1_1').bind('change', function() {globals.darlehen_sonstigesDesc = $(this).val()});
		$('#p48_i1_1').bind('focus', function () {if ($(this).val() == 'Other') $(this).val('');}).bind('blur', function () {if ($(this).val() == '') $(this).val('Other');});
		$('#p48 .checkbox').click(function () {
			$(this).toggleClass('checked');
			if ($(this).attr('id') == 'p48_cb_2' && $(this).hasClass('checked')) {
				p48.setCb('p48_cb_1', 0);
				p48.setCb('p48_cb_2', 1);
				p48.setCb('p48_cb_3', 0);
				p48.setCb('p48_cb_4', 0);
				p48.setCbVar('p48_cb_5', 0);
				p48.setCbVar('p48_cb_1', 0);
				p48.setCbVar('p48_cb_2', 1);
				p48.setCbVar('p48_cb_3', 0);
				p48.setCbVar('p48_cb_4', 0);
				p48.setCbVar('p48_cb_5', 0);
			} else {
				p48.setCbVar('p48_cb_2', 0);
				p48.setCb('p48_cb_2', 0);
				p48.setCbVar($(this).attr('id'), $(this).hasClass('checked'));
			}
		});
		$('#p48_btnprev').click(function (event) {globals.box4_status = 1; app.showPage('p1'); event.preventDefault();});
		$('#p48_btntakeover').click(function (event) {globals.box4_status = 1; app.showPage('p1'); event.preventDefault();});
		$('#p48_btnlbs').hover(function (){$(this).toggleClass('hover');});	
		$('#p48_btnkfw').hover(function (){$(this).toggleClass('hover');});	
		$('#p48_btnhand').hover(function (){$(this).toggleClass('hover');});
		$('#p48_btnhand').click(function (event) {p48.showHand();});	
		$('#p48_btnlbs').click(function (event) {p48.showLbs();});	
		$('#p48_btnkfw').click(function (event) {p48.showKfw();});
		$('#p48 .p48_pleft').click(function (event) {p48.prevPhase(); event.preventDefault();});
		$('#p48 .p48_pright').click(function (event) {p48.nextPhase(); event.preventDefault();});
		$('#p48_kfw_btnclose').click(function (event) {p48.hideKfw(); event.preventDefault();});
		$('#p48_lbs_btnclose').click(function (event) {p48.hideLbs(); event.preventDefault();});
		$('#p48_hand_btnclose').click(function (event) {p48.hideHand(); event.preventDefault();});
	},
	nextPhase: function() {
		this.phase = this.phase + 1;
		$('.p48_pwrap').animate({
		    left: '-=503'
		}, 300, function() {
			 p48.phaseCallback();
		});
  	},
	prevPhase: function () {
		this.phase = this.phase - 1;
		$('.p48_pwrap').animate({
		    left: '+=503'
		}, 300, function() {
			 p48.phaseCallback();
		});
	},
	phaseCallback: function () {
		if (this.phase <= 1) {
			$('.p48_pleft').hide();
		} else {
			$('.p48_pleft').show();			
		}
		if ((this.phase >= 3 && !$('#p48_popup_hand').is(':visible')) || this.phase >= 5) {
			$('.p48_pright').hide();
		} else {
			$('.p48_pright').show();			
		}
	},
	setCbVar: function (id, value) {
		if (value == true) value = 1;
		else value = 0;
		switch (id) {
   			case 'p48_cb_1':
       			globals.darlehen_sk = value;
       			break;
       		case 'p48_cb_2':
       			globals.darlehen_hand = value;
       			break;
       		case 'p48_cb_3':
       			globals.darlehen_lbs = value;
       			break;
       		case 'p48_cb_4':
       			globals.darlehen_kfw = value;
       			break;
       		case 'p48_cb_5':
       			globals.darlehen_sonstiges = value;
   				break;
   		}	
	},
	setCb: function (id, value) {
		if (value) {
			$('#' + id).addClass('checked');
		} else {
			$('#' + id).removeClass('checked');			
		}
	},
	showLbs: function () {
		if(!$('#p48_popup_lbs').is(':visible')) {
			if($('#p48_popup_kfw').is(':visible')) {this.hideKfw();}
			if($('#p48_popup_hand').is(':visible')) {this.hideHand();}
			$('#p48_popup_lbs').fadeIn('slow');
		}
	},
	hideLbs: function () {
		$('#p48_popup_lbs').fadeOut('slow');
		$('#p48 .p48_pwrap').css('left', '0');
		this.phase = 1;
		this.phaseCallback();
	},
	showHand: function () {
		if(!$('#p48_popup_hand').is(':visible')) {
			if($('#p48_popup_kfw').is(':visible')) {this.hideKfw();}
			if($('#p48_popup_lbs').is(':visible')) {this.hideLbs();}
			$('#p48_popup_hand').fadeIn('slow');
		}
	},
	hideHand: function () {
		$('#p48_popup_hand').fadeOut('slow');
		$('#p48 .p48_pwrap').css('left', '0');
		this.phase = 1;
		this.phaseCallback();
	},
	showKfw: function () {
		if(!$('#p48_popup_kfw').is(':visible')) {
			if($('#p48_popup_lbs').is(':visible')) {this.hideLbs();}
			if($('#p48_popup_hand').is(':visible')) {this.hideHand();}
			$('#p48_popup_kfw').fadeIn('slow');
		}
	},
	hideKfw: function () {
		$('#p48_popup_kfw').fadeOut('slow');
	}
		
}

var p50 = {
	init: function () {
		this.showFieldset(1);
		this.bindLinks();
		this.writeHeader();
		$('#raten_1_kommentar').val(globals.fsumme_raten_1_kommentar);
	},
	showFieldset: function (nr) {
  		$('#p50_btnnext').show();
    	$('#p50_btnprev').show();
		switch (nr) {
   			case 1:
       			$('#p50_btnprev').hide();
   				app.showFsummeFieldset(1);
  				app.writeFsummeVars('raten_1', 4);
  				$('#p50 .fieldset_1 input').not('#raten_1_sum').bind('keyup', function (event) {app.updateFsummeFieldset('raten_1', 4); p50.writeHeader();});
  				$('#raten_1_sum').bind('keyup', function (event) {
  					globals.fsumme_raten_1_sum = app.removeTSeparator($('#raten_1_sum').val());
  					var sum = app.addTSeparator(globals.fsumme_raten_1_sum);
  					if (sum == 0) sum = '';
  					$('#raten_1_sum').val(sum);
  					p50.writeHeader();
  				});
   			break;
   			case 2:
   				app.showFsummeFieldset(2);
  				app.writeFsummeVars('raten_2', 6);
  				$('#p50 .fieldset_2 input').not('#raten_2_sum').bind('keyup', function (event) {app.updateFsummeFieldset('raten_2', 6); p50.writeHeader();});
				if ($('#raten_2_1').val() == '') this.calcLebenshaltungskosten();
				if ($('#raten_2_2').val() == '') this.calcAutokosten();
				if ($('#raten_2_3').val() == '') this.calcImmobilienkosten();
  				$('#raten_2_sum').bind('keyup', function (event) {
  					globals.fsumme_raten_2_sum = app.removeTSeparator($('#raten_2_sum').val());
  					var sum = app.addTSeparator(globals.fsumme_raten_2_sum);
  					if (sum == 0) sum = '';
  					$('#raten_2_sum').val(sum);
  					p50.writeHeader();
  				});
   			break;
   			case 3:
       			$('#p50_btnnext').hide();
   				app.showFsummeFieldset(3);
  				app.writeFsummeVars('raten_3', 1);
  				$('#p50 .fieldset_3 input').bind('keyup', function (event) {app.updateFsummeFieldset('raten_3', 1); p50.writeHeader();});
   			break;
   			default:
   				this.takeOver();
   			break;	
		}
		$('input.comment').unbind('change').unbind('keyup');
	},
	writeHeader: function () {
		$('#fsumme_raten_header .field_1 .value').html(app.addTSeparator(globals.fsumme_raten_1_sum));
		$('#fsumme_raten_header .field_2 .value').html(app.addTSeparator(globals.fsumme_raten_2_sum));
		$('#fsumme_raten_header .field_3 .value').html(app.addTSeparator(globals.fsumme_raten_3_sum));
		$('#fsumme_raten_header .field_4 .value').html(app.addTSeparator(p50.sumFieldsets()));
	},
	sumFieldsets: function () {
		var sum = 0;
		sum = globals.fsumme_raten_1_sum - globals.fsumme_raten_2_sum - globals.fsumme_raten_3_sum;
		return sum;
	},
	takeOver: function () {
		globals.ratenpotenzial = this.sumFieldsets();
		globals.einnahmen = globals.fsumme_raten_1_sum;
		globals.ausgaben = globals.fsumme_raten_2_sum;
		globals.box2_status = 1;
		globals.fsumme_raten_1_kommentar = $('#raten_1_kommentar').val();
		app.showPage('p1');
	},
	showNextFieldset: function () {
		var next = globals.fsumme_currentFieldset + 1;
		this.showFieldset(next);
	},
	showPrevFieldset: function () {
		var next = globals.fsumme_currentFieldset - 1;
		this.showFieldset(next);
	},
	calcLebenshaltungskosten: function () {
		var row = globals.fsumme_raten_2_personen - 1;
		if (row < 0) {
			var kosten = 0;
		} else {			
			var einnahmen = (globals.fsumme_raten_1_sum > 0) ? globals.fsumme_raten_1_sum : config.einnahmen;
			var col = Math.floor(einnahmen / 250) - 2;
			col = (col < 0) ? 0 : col;
			col = (col > 18) ? 18 : col;
			
			var kosten = config.lebenshaltung[row][col];
		}
		
		$('#raten_2_1').val(kosten);
		$('#raten_2_1').keyup();	
		return kosten
	},
	calcAutokosten: function () {
		var kosten = Math.round(globals.fsumme_raten_2_autos * 300);
		$('#raten_2_2').val(kosten);
		$('#raten_2_2').keyup();
		return kosten;
	},
	calcImmobilienkosten: function () {
		var kosten = Math.round((globals.fsumme_raten_2_personen -1) * 20 * 2.5 + (70 * 2.5));
		$('#raten_2_3').val(kosten);
		$('#raten_2_3').keyup();
		return kosten;
	},
	bindLinks: function () {
		app.writeSepInput('p50_i1', 1, globals.fsumme_raten_2_personen);
		app.writeSepInput('p50_i2', 1, globals.fsumme_raten_2_autos);		
		$('#p50_i1_up').click(function () {
			globals.fsumme_raten_2_personen = app.increaseSepInput('p50_i1', 1, 1, 7);
			p50.calcLebenshaltungskosten();
			p50.calcImmobilienkosten();
		});
		$('#p50_i1_down').click(function () {
			globals.fsumme_raten_2_personen = app.decreaseSepInput('p50_i1', 1, 1, 0);
			p50.calcLebenshaltungskosten();
			p50.calcImmobilienkosten();
		});
		$('#p50_i2_up').click(function () {
			globals.fsumme_raten_2_autos = app.increaseSepInput('p50_i2', 1, 1, 9);
			p50.calcAutokosten();
		});
		$('#p50_i2_down').click(function () {
			globals.fsumme_raten_2_autos = app.decreaseSepInput('p50_i2', 1, 1, 0);
			p50.calcAutokosten();
		});
		$('#p50 .field_1').click(function (event) {p50.showFieldset(1);});
		$('#p50 .field_2').click(function (event) {p50.showFieldset(2);});
		$('#p50 .field_3').click(function (event) {p50.showFieldset(3);});
		$('#p50 .field').mouseover(function (event) {$(this).addClass('hover')});
		$('#p50 .field').mouseout(function (event) {$(this).removeClass('hover')});
		$('#p50 .field_4').unbind('click').unbind('mouseover');
		$('#p50_btnabort').click(function (event) {app.showPage('p1'); event.preventDefault();});
		$('#p50_btntakeover').click(function (event) {p50.takeOver(); event.preventDefault();});
		$('#p50_btnprev').click(function (event) {p50.showPrevFieldset(); event.preventDefault();});
		$('#p50_btnnext').click(function (event) {p50.showNextFieldset(); event.preventDefault();});
	}
}

var p51 = {
	init: function () {
		$('#p51 .el.current').fadeIn();
		$('#p51 .ela').mouseover(function (event) {$(this).addClass('hover')});
		$('#p51 .ela').mouseout(function (event) {$(this).removeClass('hover')});
		$('#p51 .ela').click(function (event) {$('#p51 .ela').removeClass('current'); $(this).addClass('current'); $('#p51 .el').hide();  $('#' + $(this).attr('rel')).fadeIn(); event.preventDefault();});
		$('#p51_btnprev').click(function (event) {app.showPage('p1'); event.preventDefault();});
	}
}

