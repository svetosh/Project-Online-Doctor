:- consult(kbase_symplists).
catlist(List):-
    findall(Cat, s_list(Cat, _Symptoms), List).

