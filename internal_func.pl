:- module(internal_func, [ache/3])
:- consult(kbase_symplists).

ache(Category, Num, Symptoms):-
    s_list(Category, List),
    nth0(Num, List, Element),
    member(Element, Symptoms).

