:- use_module(database).

:- use_module(library(http/http_server)).
:- use_module(library(http/http_json)).
:- use_module(library(http/http_cors)).

:- http_handler('/fibb',сервис1(M), [method(M),methods([get,post]),time_limit(10000)]).
:- http_handler('/answer',сервис2(M), [method(M),methods([get,post]),time_limit(10000)]).

:- set_setting(http:cors, [*]).

сервер :- http_server(http_dispatch, [port(8080)]).






сервис2(get,_) :- cors_enable, форма(X),ответить(X).
сервис2(post,Запрос) :-
  cors_enable,
  http_parameters(Запрос,[(Число,[integer])]),
  обсчитать(Число).
















фиббоначи(_F, F1, N, N, F1) :- !.
фиббоначи(F0, F1, I, N, F) :-
        F2 is F0+F1,
        I2 is I + 1,
        !,фиббоначи(F1, F2, I2, N, F).

обсчитать(Число):-
  Число > 0,
  фиббоначи(0,1,1,Число,Ответ),форма(X),
  format(atom(Строка),'~w число Фиббоначи равно ~w<br/>~w',[Число,Ответ,X]),
  ответить(Строка).

обсчитать(Число):-
  форма(X),
  format(atom(Строка),'заданное число ~w меньше 0<br/>~w',[Число,X]),
  ответить(Строка).

ответить(Вставка):-
 format('Content-type: text/html~n~n
 <html><body>Вычисление чисел Фиббоначчи<br/>
 ~w
 </body></html>~n', [Вставка]).

форма('<form method="POST"><input name="val"/></form>').

сервис1(get,_) :- cors_enable, форма(X),ответить(X).
сервис1(post,Запрос) :-
  cors_enable,
  http_parameters(Запрос,[val(Число,[integer])]),
  обсчитать(Число).










