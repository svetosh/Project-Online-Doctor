:- use_module(library(http/json_convert)).
:- use_module(kbase_handler).

setListXY(X,Y) :-
    assert(myListXYZ([X,Y])).
check(JIN,Jout):-
    setListXY(JIN, PLIN),
	json_to_prolog(JIN, PLIN),
	назначить(PLIN,PLOUT),
	prolog_to_json(PLOUT,Jout).
	
