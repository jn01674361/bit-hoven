

nur=0:length(uniqenotesreadysong)-1;
%A = [0 0 1 1 1 0 0 0 0 NaN NaN 1 0 0 0 1 0 1 0 1 0 0 0 1 1 1 1];
C = categorical(VarName1,nur,uniqenotesreadysong);
histogram(C)