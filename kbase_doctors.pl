:- module(kbase_doctors, [doctor/2]).
:- consult(kbase_deseases).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% База знаний "врач - класс заболевания"


doctor(Symptoms, "аллерголог"):-
	dclass("аллергия",Symptoms).

doctor(Symptoms, "кардиолог"):-
    dclass("к",Symptoms).

/**
doctor(Symptoms, "терапевт"):-
    орви(Symptoms);
	заболевание_для_терапевта(Symptoms).

doctor(Symptoms, "нефролог"):-
	заболевание_для_нефролога(Symptoms).

doctor(Symptoms, "флеболог"):-
	заболевание_для_флеболога_или_хирурга(Symptoms).

doctor(Symptoms, "хирург"):-
	заболевание_для_флеболога_или_хирурга(Symptoms).

doctor(Symptoms, "гастроэнтеролог"):-
	заболевание_для_гастроэнтеролога(Symptoms).

doctor(Symptoms, "гинеколог"):-
	заболевание_для_гинеколога(Symptoms).

doctor(Symptoms, "уролог"):-
	заболевание_для_уролога(Symptoms).

doctor(Symptoms, "скорая помощь"):-
	срочно_в_больницу(Symptoms).
*/
