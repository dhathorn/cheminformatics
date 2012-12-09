
A = importdata('Compound_000000001_000025000.out', ',', 1);
X = A.data(:, 2:21);
y = A.data(:, 1);
T = classregtree(X, y, 'splitmin', 1);
