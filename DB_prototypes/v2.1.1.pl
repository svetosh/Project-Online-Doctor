% s_list(category, num, symptom).
s_list("head", 0, "head_ache").
s_list("head", 1, "tongue_ache").
s_list("body", 0, "back_hurt").

ache(Category, Num, Symptoms):-
    s_list(Category, Num, Element),
    member(Element, Symptoms).

% ache_type(Symptoms):-
%     .. ache(category, num, ListOfSymptoms)[;,.]
%     *
brain_ache(Symptoms):-
    ache("head", 0, Symptoms).
tongue_ache(Symptoms):-
    ache("head", 1, Symptoms),
    \+ ache("body", 0, Symptoms).
back_ache(Symptoms):-
	ache("body", 0, Symptoms).

% doctor(Symptoms, doctor_spec):-
%     .. ache_type(Symptoms)[;,.]
%     *
doctor(Symptoms, "head_doctor"):-
    brain_ache(Symptoms);
    tongue_ache(Symptoms).
doctor(Symptoms, "body_doctor"):-
    back_ache(Symptoms).

delete_doubles([], []):-!.
delete_doubles([X|Xs], Ys):-
      member(X, Xs),
      !, delete_doubles(Xs, Ys).
delete_doubles([X|Xs], [X|Ys]):-
      !, delete_doubles(Xs, Ys).
find_doctor(Symptoms,Doctors):-
    findall(Doctor, doctor(Symptoms, Doctor), Doctors_raw),
    delete_doubles(Doctors_raw, Doctors).

