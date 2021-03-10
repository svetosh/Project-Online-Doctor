:- module(kbase_handler, [find_doctor/2]).

:- use_module(kbase_doctors).


delete_doubles([], []):-!.
delete_doubles([X|Xs], Ys):-
      member(X, Xs),
      !, delete_doubles(Xs, Ys).
delete_doubles([X|Xs], [X|Ys]):-
      !, delete_doubles(Xs, Ys).
      
find_doctor(Symptoms,Doctors):-
    findall(Doctor, doctor(Symptoms, Doctor), Doctors_raw),
    delete_doubles(Doctors_raw, Doctors).
