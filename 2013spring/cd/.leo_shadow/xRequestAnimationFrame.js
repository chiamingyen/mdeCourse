//@+leo-ver=4-thin
//@+node:amd_yen.20130418193628.2126:@shadow cd/RequestAnimationFrame.js
/**
 * Provides requestAnimationFrame in a cross browser way.
 * http://paulirish.com/2011/requestanimationframe-for-smart-animating/
 */

if ( !window.requestAnimationFrame ) {

	window.requestAnimationFrame = ( function() {

		return window.webkitRequestAnimationFrame ||
		window.mozRequestAnimationFrame ||
		window.oRequestAnimationFrame ||
		window.msRequestAnimationFrame ||
		function( /* function FrameRequestCallback */ callback, /* DOMElement Element */ element ) {

			window.setTimeout( callback, 1000 / 60 );

		};

	} )();

}
//@-node:amd_yen.20130418193628.2126:@shadow cd/RequestAnimationFrame.js
//@-leo
