function touchHandler(event)
{
    var touches = event.changedTouches,
        first = touches[0],
        node = first.target,
        type = "";
        
        var klassen = node.className.split(' ');

		if(klassen[0] == 'ui-slider-handle' || klassen[0] == 'arrow') {
			switch(event.type) {
				case "touchstart": type = "mousedown"; break;
				case "touchmove":  type="mousemove"; break;        
				case "touchend":   type="mouseup"; break;
				default: return;
			}

			//initMouseEvent(type, canBubble, cancelable, view, clickCount, 
			//           screenX, screenY, clientX, clientY, ctrlKey, 
		    //           altKey, shiftKey, metaKey, button, relatedTarget);
		    
		    var simulatedEvent = document.createEvent("MouseEvent");
		    simulatedEvent.initMouseEvent(type, true, true, window, 1, 
		                              first.screenX, first.screenY, 
		                              first.clientX, first.clientY, false, 
		                              false, false, false, 0/*left*/, null);
		
			first.target.dispatchEvent(simulatedEvent);
		    event.preventDefault();
		}
}

function initPad() 
{
	if ($.browser.webkit) {
    	document.addEventListener("touchstart", touchHandler, true);
    	document.addEventListener("touchmove", touchHandler, true);
    	document.addEventListener("touchend", touchHandler, true);
    	document.addEventListener("touchcancel", touchHandler, true);
	}
}