:- module(ache_term, [ache/3]).
:- use_module(kbase_symptlists).

ache(Category, Num, Symptoms):-
    s_list(Category, List),
    nth0(Num, List, Element),
    member(Element, Symptoms).

