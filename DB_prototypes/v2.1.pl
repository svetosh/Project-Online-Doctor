s_list("head", ["head_ache","tongue_ache"]).
s_list("body",["back_hurt"]).

ache(Category, Num, Symptoms):-
    s_list(Category, List),
    nth0(Num, List, Element),
    member(Element, Symptoms).

brain_ache(Symptoms):-
    ache("head", 0, Symptoms).
tongue_ache(Symptoms):-
    ache("head", 1, Symptoms).
back_ache(Symptoms):-
    ache("body", 0, Symptoms).

doc(Symptoms, "head_doctor"):-
    brain_ache(Symptoms);
    tongue_ache(Symptoms).
doc(Symptoms, "body_doctor"):-
    back_ache(Symptoms).

delete_doubles([], []):-!.
delete_doubles([X|Xs], Ys):-
      member(X, Xs),
      !, delete_doubles(Xs, Ys).
delete_doubles([X|Xs], [X|Ys]):-
      !, delete_doubles(Xs, Ys).
find_doctor(Symptoms,Doctors):-
    findall(Doctor, doc(Symptoms, Doctor), Doctors_raw),
    delete_doubles(Doctors_raw, Doctors).
    
