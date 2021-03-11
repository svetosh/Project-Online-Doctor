:-module(kbase_sympcat, [catlist/1]).

:- use_module(kbase_symplists).

catlist(List):-
    findall(Cat, s_list(Cat, _Symptoms), List).

