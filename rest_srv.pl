:- use_module(kbase_symplists).
:- use_module(kbase_sympcat).
:- use_module(kbase_handler).

:- use_module(library(http/http_server)).
:- use_module(library(http/http_json)).
:- use_module(library(http/json_convert)).


:- http_handler('/categories',service1(M), [method(M),methods([post,get]),time_limit(10000)]).
:- http_handler('/symptoms',service2(M), [method(M),methods([post,get,options]),time_limit(10000)]).
:- http_handler('/answer',service2(M), [method(M),methods([post,get,options]),time_limit(10000)]).


servstart(Port) :- http_server(http_dispatch, [port(Port)]).

service1(get, _Request) :-
    catlist(PrologOut),
    prolog_to_json(PrologOut, JSONOut),
    reply_json(JSONOut).

service2(post,Request) :-
    http_read_json_dict(Request, JSONIn),
    json_to_prolog(JSONIn, PrologIn),
    s_list(PrologIn, PrologOut),
    prolog_to_json(PrologOut, JSONOut),
    reply_json(JSONOut).
    
service3(post,Request) :-
    http_read_json_dict(Request, JSONIn),
    json_to_prolog(JSONIn, PrologIn),
    find_doctor(PrologIn, PrologOut),
    prolog_to_json(PrologOut, JSONOut),
    reply_json(JSONOut).

servstop(Port) :-
    http_stop_server(Port,_).
