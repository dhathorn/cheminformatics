function hy = chempredict(T, hX)

hy = eval(T, hX);
hy = int32(hy)
hy = dec2hex(hy)
