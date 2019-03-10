% -*- Mode: Prolog -*-

#const num_disks=3.
% define peg(PEG)
peg(a;b;c).
% define disk(DISK)
disk(1..num_disks).
% define init_on(DISK, PEG)
init_on(1..num_disks,a).
% define goal_on(DISK, PEG)
goal_on(1..num_disks,c).
moves(7).
