/*
Uh ok so I'm bad at JS but this is how'd I implement it. T
his is greatly inspired by PYJS!
*/

// Events given by Python 
var Events

// The all encompassing handler, loads our functions and what not
var __handler = {
  _locale: [
    '_Reload',
    '_Init'
  ],
  _ret: {},
  _onEvent: function( Event ){
    if ( this._locale.includes(Event) ){
      console.log('[pjec] Code called a locale function')
    } else {
    	console.log('[pjec] Assuming non inherent function, checking user defined funcs', this._locale)
    }
  }
}

// Initialize the handler
__handler._onEvent('_Init')

// Code-appeneded below, no touchy!
__handler._ret.Clicked = function( _Arg){
	console.log('Clicked!')
}