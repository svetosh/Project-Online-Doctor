s_list("ноги", ["расширение поверхностных вен нижних конечностей у пациента или в семейном намнезе","отек на ноге","отек на двух ногах"]).
s_list("ССС",["гипертония"]).
s_list("голова",["отёчность_лица"]).

ache(Category, Num, Symptoms):-
    s_list(Category, List),
    nth0(Num, List, Element),
    member(Element, Symptoms).

dclass("аллергия",Symptoms):-
    ache("голова", 0, Symptoms),
    \+ ache("ноги", 0, Symptoms),
    \+ ache("ноги", 1, Symptoms).
dclass("к",Symptoms):-
    ache("ССС", 0, Symptoms);
    ache("ноги", 2, Symptoms).

doctor(Symptoms, "аллерголог"):-
	dclass("аллергия",Symptoms).

doctor(Symptoms, "кардиолог"):-
    dclass("к",Symptoms).

delete_doubles([], []):-!.
delete_doubles([X|Xs], Ys):-
      member(X, Xs),
      !, delete_doubles(Xs, Ys).
delete_doubles([X|Xs], [X|Ys]):-
      !, delete_doubles(Xs, Ys).

find_doctor(Symptoms,Doctors):-
    findall(Doctor, doctor(Symptoms, Doctor), Doctors_raw),
    delete_doubles(Doctors_raw, Doctors).
