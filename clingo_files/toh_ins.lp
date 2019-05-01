#const num_disks=3.
% schema peg(PEG)
peg(a;b;c).
% schema disk(DISK)
disk(1..num_disks).
% schema init_on(DISK, PEG)
init_on(1..num_disks,a).
% schema goal_on(DISK, PEG)
goal_on(1..num_disks,c).
moves(7).
