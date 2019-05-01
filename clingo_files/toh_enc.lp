% Generate
{ move(T,D,P) : disk(D), peg(P) } = 1 :- moves(M),  T = 1..M.
% schema move(TIME, DISK)
% temporal move(T,_)
% schema move(TIME, DISK, PEG)
% temporal move(T,_,_)
% schema on(TIME, DISK, PEG)
% temporal on(T,_,_)
% schema blocked(TIME, DISK, PEG)
% temporal blocked(T,_,_)
move(T,D)   :- move(T,D,_).
on(0,D,P)   :- init_on(D,P).
on(T,D,P)   :- move(T,D,P).
on(T+1,D,P) :- on(T,D,P), not move(T+1,D), not moves(T).
blocked(T+1,D-1,P) :- on(T,D,P), not moves(T).
blocked(T,D-1,P)   :- blocked(T,D,P), disk(D).
% Test
:- move(T,D,P), blocked(T,D-1,P).
:- move(T,D), on(T-1,D,P), blocked(T,D,P).
:- goal_on(D,P), not on(M,D,P), moves(M).
:- { on(T,D,P) } != 1, disk(D), moves(M), T = 1..M.
%% % Display
%% #show move/3.
