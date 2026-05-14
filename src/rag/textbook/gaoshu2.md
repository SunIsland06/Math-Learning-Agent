又由于 $F(x)$ 是 $F'(x)$ 的原函数, 所以

$$
\int F ^ {\prime} (x) \mathrm{d} x = F (x) + C,
$$

或记作

$$
\int \mathrm{d} F (x) = F (x) + C. \tag {1-2}
$$

由此可见,微分运算(以记号 d 表示)与求不定积分的运算(简称积分运算,以记号 $\int$ 表示)是互逆的.当记号 $\int$ 与 d 连在一起时,或者抵消,或者抵消后差一个常数.

# 二、基本积分表

既然积分运算是微分运算的逆运算,那么很自然地可以从导数公式得到相应的积分公式.

例如, 因为 $\left(\frac{x^{\mu+1}}{\mu+1}\right)^{\prime}=x^{\mu}$ , 所以 $\frac{x^{\mu+1}}{\mu+1}$ 是 $x^{\mu}$ 的一个原函数, 于是

$$
\int x ^ {\mu} \mathrm{d} x = \frac {x ^ {\mu + 1}}{\mu + 1} + C \quad (\mu \neq - 1).
$$

类似地可以得到其他积分公式.下面我们把一些基本的积分公式列成一个表,这个表通常叫做基本积分表.

① $\int kdx=kx+C$ （k 是常数），

② $\int x^{\mu}\mathrm{d}x = \frac{x^{\mu + 1}}{\mu + 1} +C$ （ $\mu \neq -1$ ） 

③ $\int \frac{\mathrm{d}x}{x} = \ln |x| + C,$ 

④ $\int\frac{dx}{1+x^{2}}=\arctan x+C,$ 

⑤ $\int \frac{\mathrm{d}x}{\sqrt{1 - x^2}} = \arcsin x + C,$ 

⑥ $\int \cos x dx = \sin x + C,$ 

⑦ $\int \sin x\mathrm{d}x = -\cos x + C,$ 

⑧ $\int \frac{\mathrm{d}x}{\cos^2 x} = \int \sec^2 x\mathrm{d}x = \tan x + C,$ 

⑨ $\int \frac{\mathrm{d}x}{\sin^2 x} = \int \csc^2 x \mathrm{d}x = -\cot x + C,$ 

⑩ $\int \sec x\tan x\mathrm{d}x = \sec x + C,$ 

⑪ $\int \csc x\cot x\mathrm{d}x = -\csc x + C,$ 

⑫ $\int \mathrm{e}^{x}\mathrm{d}x = \mathrm{e}^{x} + C,$ 

⑬ $\int a^{x} \mathrm{d} x = \frac{a^{x}}{\ln a} + C (a > 0$ 且 $a \neq 1$ ).

以上十三个基本积分公式是求不定积分的基础,必须熟记,下面举几个应用幂函数的积分公式②的例子.

例5 求 $\int \frac{\mathrm{d}x}{x^3}$ .

解 $\int \frac{\mathrm{d}x}{x^3} = \int x^{-3}\mathrm{d}x = \frac{x^{-3 + 1}}{-3 + 1} +C = -\frac{1}{2x^2} +C.$ 

例6 求 $\int x^2\sqrt{x}\mathrm{d}x.$ 

解 $\int x^2\sqrt{x}\mathrm{d}x = \int x^{\frac{5}{2}}\mathrm{d}x = \frac{x^{\frac{5}{2} + 1}}{\frac{5}{2} + 1} +C = \frac{2}{7} x^{\frac{7}{2}} + C = \frac{2}{7} x^3\sqrt{x} +C.$ 

例 7 求 $\int\frac{dx}{x\sqrt[3]{x}}$ .

解 $\int \frac{\mathrm{d}x}{x\sqrt[3]{x}} = \int x^{-\frac{4}{3}}\mathrm{d}x = \frac{x^{-\frac{4}{3} + 1}}{-\frac{4}{3} + 1} +C = -3x^{-\frac{1}{3}} + C = -\frac{3}{\sqrt[3]{x}} +C.$ 

上面三个例子表明,有时被积函数实际是幂函数,但用分式或根式表示.遇此情形,应先把它化为 $x^{\mu}$ 的形式,然后应用幂函数的积分公式②来求不定积分.

# 三、不定积分的性质

根据不定积分的定义,可以推得它有如下两个性质:

性质1 设函数 $f(x)$ 及 $g(x)$ 的原函数存在, 则

$$
\int [ f (x) + g (x) ] \mathrm{d} x = \int f (x) \mathrm{d} x + \int g (x) \mathrm{d} x. \tag {1-3}
$$

证 将(1-3)式右端求导,得

$$
\left[ \int f (x) \mathrm{d} x + \int g (x) \mathrm{d} x \right] ^ {\prime} = \left[ \int f (x) \mathrm{d} x \right] ^ {\prime} + \left[ \int g (x) \mathrm{d} x \right] ^ {\prime} = f (x) + g (x).
$$

这表示，(1-3)式右端是 $f(x)+g(x)$ 的原函数，又(1-3)式右端有两个积分记号，形式上含两个任意常数，由于任意常数之和仍为任意常数，故实际上含一个任意常数，因此(1-3)式右端是 $f(x)+g(x)$ 的不定积分.

性质 1 对于有限个函数都是成立的.

类似地可以证明不定积分的第二个性质.

性质2 设函数 $f(x)$ 的原函数存在， $k$ 为非零常数，则

$$
\int k f (x) \mathrm{d} x = k \int f (x) \mathrm{d} x.
$$

利用基本积分表以及不定积分的这两个性质,可以求出一些简单函数的不定积分.

例8 求 $\int \sqrt{x} (x^2 - 5) \, \mathrm{d}x$ .

解 $\int \sqrt{x} (x^2 - 5) \, \mathrm{d}x = \int (x^{\frac{5}{2}} - 5x^{\frac{1}{2}}) \, \mathrm{d}x = \int x^{\frac{5}{2}} \, \mathrm{d}x - \int 5x^{\frac{1}{2}} \, \mathrm{d}x$ 

$$
= \int x ^ {\frac {5}{2}} d x - 5 \int x ^ {\frac {1}{2}} d x = \frac {2}{7} x ^ {\frac {7}{2}} - 5 \cdot \frac {2}{3} x ^ {\frac {3}{2}} + C
$$

$$
= \frac {2}{7} x ^ {3} \sqrt {x} - \frac {1 0}{3} x \sqrt {x} + C.
$$

注意 检验积分结果是否正确, 只要对结果求导, 看它的导数是否等于被积函数, 相等时结果是正确的, 否则结果是错误的. 如就例 8 的结果来看, 由于

$$
\left(\frac {2}{7} x ^ {3} \sqrt {x} - \frac {1 0}{3} x \sqrt {x} + C\right) ^ {\prime} = \left(\frac {2}{7} x ^ {\frac {7}{2}} - \frac {1 0}{3} x ^ {\frac {3}{2}} + C\right) ^ {\prime} = x ^ {\frac {5}{2}} - 5 x ^ {\frac {1}{2}} = \sqrt {x} (x ^ {2} - 5),
$$

所以结果是正确的.

例9 求 $\int \frac{(x - 1)^3}{x^2} \mathrm{d}x.$ 

解 $\int \frac{(x - 1)^3}{x^2}\mathrm{d}x = \int \frac{x^3 - 3x^2 + 3x - 1}{x^2}\mathrm{d}x = \int \left(x - 3 + \frac{3}{x} -\frac{1}{x^2}\right)\mathrm{d}x$ 

$$
= \int x \mathrm{d} x - 3 \int \mathrm{d} x + 3 \int \frac {\mathrm{d} x}{x} - \int \frac {\mathrm{d} x}{x ^ {2}} = \frac {x ^ {2}}{2} - 3 x + 3 \ln | x | + \frac {1}{x} + C.
$$

例10 求 $\int (\mathrm{e}^x - 3\cos x)\mathrm{d}x.$ 

解 $\int (\mathrm{e}^{x} - 3\cos x)\mathrm{d}x = \int \mathrm{e}^{x}\mathrm{d}x - 3\int \cos x\mathrm{d}x = \mathrm{e}^{x} - 3\sin x + C.$ 

例11 求 $\int 2^{x}\mathrm{e}^{x}\mathrm{d}x.$ 

解 因为

$$
2 ^ {x} \mathrm{e} ^ {x} = (2 \mathrm{e}) ^ {x},
$$

所以可把 2e 看作 a, 并利用积分公式⑬, 便得

$$
\int 2 ^ {x} \mathrm{e} ^ {x} \mathrm{d} x = \int (2 \mathrm{e}) ^ {x} \mathrm{d} x = \frac {(2 \mathrm{e}) ^ {x}}{\ln (2 \mathrm{e})} + C = \frac {2 ^ {x} \mathrm{e} ^ {x}}{1 + \ln 2} + C.
$$

例12 求 $\int \tan^2 x\mathrm{d}x.$ 

解 基本积分表中没有这种类型的积分,先利用三角恒等式化成表中所列类型的积分,然后再逐项求积分.

$$
\int \tan^ {2} x \mathrm{d} x = \int (\sec^ {2} x - 1) \mathrm{d} x = \int \sec^ {2} x \mathrm{d} x - \int \mathrm{d} x = \tan x - x + C.
$$

例13 求 $\int \sin^2\frac{x}{2}\mathrm{d}x.$ 

解 基本积分表中也没有这种类型的积分, 同上例一样, 可以先利用三角恒等式变形, 然后再逐项求积分.

$$
\begin{array}{l} \int \sin^ {2} \frac {x}{2} d x = \int \frac {1}{2} (1 - \cos x) d x = \frac {1}{2} \int (1 - \cos x) d x \\ = \frac {1}{2} \left(\int \mathrm{d} x - \int \cos x \mathrm{d} x\right) = \frac {1}{2} (x - \sin x) + C. \\ \end{array}
$$

例14 求 $\int \frac{1}{\sin^2\frac{x}{2}\cos^2\frac{x}{2}}\mathrm{d}x.$ 

解 同上例一样,先利用三角恒等式变形,然后再求积分.

$$
\int \frac {1}{\sin^ {2} \frac {x}{2} \cos^ {2} \frac {x}{2}} \mathrm{d} x = \int \frac {1}{\left(\frac {\sin x}{2}\right) ^ {2}} \mathrm{d} x = 4 \int \csc^ {2} x \mathrm{d} x = - 4 \cot x + C.
$$

例15 求 $\int \frac{2x^4 + x^2 + 3}{x^2 + 1} \mathrm{d}x.$ 

解 被积函数的分子和分母都是多项式,通过多项式的除法,可以把它化成基本积分表中所列类型的积分,然后再逐项求积分.

$$
\begin{array}{l} \int \frac {2 x ^ {4} + x ^ {2} + 3}{x ^ {2} + 1} d x = \int \left(2 x ^ {2} - 1 + \frac {4}{x ^ {2} + 1}\right) d x \\ = 2 \int x ^ {2} \mathrm{d} x - \int 1 \mathrm{d} x + 4 \int \frac {1}{x ^ {2} + 1} \mathrm{d} x = \frac {2}{3} x ^ {3} - x + 4 \arctan x + C. \\ \end{array}
$$

# 习题4-1

1. 利用求导运算验证下列等式：

(1) $\int \frac{1}{\sqrt{x^2 + 1}} \mathrm{d}x = \ln (x + \sqrt{x^2 + 1}) + C;$ 

(2) $\int \frac{1}{x^2\sqrt{x^2 - 1}}\mathrm{d}x = \frac{\sqrt{x^2 - 1}}{x} + C;$ 

(3) $\int \frac{2x}{(x^2 + 1)(x + 1)^2} \, \mathrm{d}x = \arctan x + \frac{1}{x + 1} + C;$ 

(4) $\int \sec x\mathrm{d}x = \ln |\tan x + \sec x| + C;$ 

(5) $\int x\cos x\mathrm{d}x = x\sin x + \cos x + C;$ 

(6) $\int \mathrm{e}^{x}\sin x\mathrm{d}x = \frac{1}{2}\mathrm{e}^{x}(\sin x - \cos x) + C.$ 

2. 求下列不定积分：

(1) $\int \frac{\mathrm{d}x}{x^2}$ ; 

(2) $\int x\sqrt{x}\mathrm{d}x;$ 

(3) $\int \frac{\mathrm{d}x}{\sqrt{x}};$ 

(4) $\int x^{2\sqrt[3]{x}}\mathrm{d}x;$ 

(5) $\int \frac{\mathrm{d}x}{x^2\sqrt{x}};$ 

(6) $\int \sqrt[m]{x^n}\mathrm{d}x;$ 

(7) $\int 5x^{3}\mathrm{d}x;$ 

(8) $\int (x^2 - 3x + 2)\mathrm{d}x$ ; 

(9) $\int \frac{\mathrm{d}h}{\sqrt{2gh}}$ ( $g$ 是常数);

(10) $\int (x^{2} + 1)^{2}\mathrm{d}x;$ 

(11) $\int (\sqrt{x} + 1)(\sqrt{x^3} - 1)\mathrm{d}x;$ 

(12) $\int \frac{(1 - x)^2}{\sqrt{x}} \, \mathrm{d}x$ ; 

(13) $\int \left(2\mathrm{e}^{x} + \frac{3}{x}\right)\mathrm{d}x;$ 

(14) $\int \left(\frac{3}{1 + x^2} -\frac{2}{\sqrt{1 - x^2}}\right)\mathrm{d}x;$ 

(15) $\int \mathrm{e}^{x}\left(1 - \frac{\mathrm{e}^{-x}}{\sqrt{x}}\right)\mathrm{d}x;$ 

(16) $\int 3^{x} e^{x} \, dx$ ; 

(17) $\int \frac{2 \cdot 3^x - 5 \cdot 2^x}{3^x} \, \mathrm{d}x$ ; 

(18) $\int \sec x (\sec x - \tan x) \, \mathrm{d}x$ ; 

(19) $\int \cos^2\frac{x}{2}\mathrm{d}x;$ 

(20) $\int \frac{\mathrm{d}x}{1 + \cos 2x}$ ; 

(21) $\int \frac{\cos 2x}{\cos x - \sin x} \, \mathrm{d}x;$ 

(22) $\int \frac{\cos 2x}{\cos^2 x \sin^2 x} \, \mathrm{d}x;$ 

(23) $\int \cot^2 x \, \mathrm{d}x$ ; 

(24) $\int \cos \theta (\tan \theta +\sec \theta)\mathrm{d}\theta ;$ 

(25) $\int \frac{x^2}{x^2 + 1} \, \mathrm{d}x$ ; 

(26) $\int \frac{3x^4 + 2x^2}{x^2 + 1}\mathrm{d}x.$ 

3. 含有未知函数的导数的方程称为微分方程, 例如方程 $\frac{\mathrm{dy}}{\mathrm{dx}} = f(x)$ , 其中 $\frac{\mathrm{dy}}{\mathrm{dx}}$ 为未知函数的导数, $f(x)$ 为已知函数. 如果将函数 $y = \varphi(x)$ 代入微分方程, 使微分方程成为恒等式, 那么函数 $y = \varphi(x)$ 就称为该微分方程的解. 求下列微分方程满足所给条件的解:

(1) $\frac{\mathrm{dy}}{\mathrm{dx}} = (x - 2)^2, y|_{x=2} = 0;$ 

(2) $\frac{\mathrm{d}^2x}{\mathrm{d}t^2} = \frac{2}{t^3}, \quad \frac{\mathrm{d}x}{\mathrm{d}t}\bigg|_{t=1} = 1, x \big|_{t=1} = 1.$ 

4. 汽车以 20 m/s 的速度沿直线行驶, 刹车后匀减速行驶了 50 m 停住, 求刹车加速度. 可执行下列步骤:

（1）求微分方程 $\frac{\mathrm{d}^2s}{\mathrm{d}t^2} = -k$ 满足条件 $\frac{\mathrm{d}s}{\mathrm{d}t}\bigg|_{t = 0} = 20$ 及 $s\mid_{t = 0} = 0$ 的解；

(2) 求使 $\frac{ds}{dt}=0$ 的t值及相应的s值；

(3) 求使 s=50 的 k 值.

5. 一曲线通过点 $(e^{2},3)$ ，且在任一点处的切线的斜率等于该点横坐标的倒数，求该曲线的方程.

6. 一物体沿直线由静止开始运动, 经 $t \mathrm{~s}$ 后的速度是 $3 t^{2} \mathrm{~m} / \mathrm{s}$ , 问

(1) 3 s 后物体离开出发点的距离是多少?

(2) 物体走完 360 m 需要多少时间?

7. 证明 $\arcsin(2x-1)$ , $\arccos(1-2x)$ 和 $2\arctan\sqrt{\frac{x}{1-x}}$ 都是 $\frac{1}{\sqrt{x-x^2}}$ 的原函数.

# 第二节 换元积分法

利用基本积分表与积分的性质,所能计算的不定积分是非常有限的.因此,有必要进一步来研究不定积分的求法.本节把复合函数的微分法反过来用于求不定积分,利用中间变量的代换,得到复合函数的积分法,称为换元积分法,简称换元法.换元法通常分成两类,下面先讲第一类换元法.

# 一、第一类换元法

设 $f(u)$ 具有原函数 $F(u)$ ，即

$$
F ^ {\prime} (u) = f (u), \quad \int f (u) \mathrm{d} u = F (u) + C.
$$

如果 $u$ 是中间变量： $u = \varphi (x)$ ，且设 $\varphi (x)$ 可微，那么，根据复合函数微分法，有

$$
\mathrm{d} F [ \varphi (x) ] = f [ \varphi (x) ] \varphi^ {\prime} (x) \mathrm{d} x,
$$

从而根据不定积分的定义就得

$$
\int f [ \varphi (x) ] \varphi^ {\prime} (x) \mathrm{d} x = F [ \varphi (x) ] + C = \left[ \int f (u) \mathrm{d} u \right] _ {u = \varphi (x)}.
$$

于是有下述定理：

定理1 设 $f(u)$ 具有原函数, $u = \varphi(x)$ 可导, 则有换元公式

$$
\int f [ \varphi (x) ] \varphi^ {\prime} (x) \mathrm{d} x = \left[ \int f (u) \mathrm{d} u \right] _ {u = \varphi (x)}. \tag {2-1}
$$

由此定理可见,虽然 $\int f[\varphi(x)]\varphi'(x)\mathrm{d}x$ 是一个整体的记号,但从形式上看,被积表达式中的 dx 也可当作变量 x 的微分来对待,从而微分等式 $\varphi'(x)\mathrm{d}x=\mathrm{d}u$ 可以方便地应用到被积表达式中来,我们在上节第一目中已经这样用了,那里把积分 $\int F'(x)\mathrm{d}x$ 记作 $\int\mathrm{d}F(x)$ , 就是按微分 $F'(x)\mathrm{d}x=\mathrm{d}F(x)$ , 把被积表达式 $F'(x)\mathrm{d}x$ 记作 $\mathrm{d}F(x)$ .

如何应用公式(2-1)来求不定积分？设要求 $\int g(x)\mathrm{d}x$ ，如果函数 $g(x)$ 可以化为 $g(x) = f[\varphi (x)]\varphi '(x)$ 的形式，那么

$$
\int g (x) \mathrm{d} x = \int f [ \varphi (x) ] \varphi^ {\prime} (x) \mathrm{d} x = \left[ \int f (u) \mathrm{d} u \right] _ {u = \varphi (x)},
$$

这样, 函数 $g(x)$ 的积分即转化为函数 $f(u)$ 的积分. 如果能求得 $f(u)$ 的原函数, 那么也就得到了 $g(x)$ 的原函数.

例1 求 $\int 2\cos 2x\mathrm{d}x.$ 

解 被积函数中, $\cos 2x$ 是一个由 $\cos 2x = \cos u, u = 2x$ 复合而成的复合函数, 常数因子恰好是中间变量 u 的导数. 因此, 作变换 u = 2x, 便有

$$
\int 2 \cos 2 x \mathrm{d} x = \int \cos 2 x \cdot 2 \mathrm{d} x = \int \cos 2 x \cdot (2 x) ^ {\prime} \mathrm{d} x = \int \cos u \mathrm{d} u = \sin u + C,
$$

再以 u=2x 代入, 即得

$$
\int 2 \cos 2 x \mathrm{d} x = \sin 2 x + C.
$$

例2 求 $\int \frac{1}{3 + 2x}\mathrm{d}x.$ 

解 被积函数 $\frac{1}{3 + 2x} = \frac{1}{u}, u = 3 + 2x.$ 这里缺少 $\frac{\mathrm{d}u}{\mathrm{d}x} = 2$ 这样一个因子，但由于 $\frac{\mathrm{d}u}{\mathrm{d}x}$ 是个常数，故可改变系数凑出这个因子：

$$
\frac {1}{3 + 2 x} = \frac {1}{2} \cdot \frac {1}{3 + 2 x} \cdot 2 = \frac {1}{2} \cdot \frac {1}{3 + 2 x} (3 + 2 x) ^ {\prime},
$$

从而令 $u = 3 + 2x$ ，便有

$$
\begin{array}{l} \int \frac {1}{3 + 2 x} \mathrm{d} x = \int \frac {1}{2} \cdot \frac {1}{3 + 2 x} (3 + 2 x) ^ {\prime} \mathrm{d} x = \int \frac {1}{2} \cdot \frac {1}{u} \mathrm{d} u \\ = \frac {1}{2} \ln | u | + C = \frac {1}{2} \ln | 3 + 2 x | + C. \\ \end{array}
$$

一般地，对于积分 $\int f(ax + b)\mathrm{d}x$ （ $a\neq 0$ )，总可作变换 $u = ax + b$ ，把它化为

$$
\int f (a x + b) \mathrm{d} x = \int \frac {1}{a} f (a x + b) \mathrm{d} (a x + b) = \frac {1}{a} \left[ \int f (u) \mathrm{d} u \right] _ {u = a x + b},
$$

例3 求 $\int \frac{x^2}{(x + 2)^3} \mathrm{d}x.$ 

解 令 $u = x + 2$ ，则 $x = u - 2, \mathrm{d}x = \mathrm{d}u$ ，于是

$$
\begin{array}{l} \int \frac {x ^ {2}}{(x + 2) ^ {3}} \mathrm{d} x = \int \frac {(u - 2) ^ {2}}{u ^ {3}} \mathrm{d} u = \int (u ^ {2} - 4 u + 4) u ^ {- 3} \mathrm{d} u \\ = \int (u ^ {- 1} - 4 u ^ {- 2} + 4 u ^ {- 3}) d u = \ln | u | + 4 u ^ {- 1} - 2 u ^ {- 2} + C \\ = \ln | x + 2 | + \frac {4}{x + 2} - \frac {2}{(x + 2) ^ {2}} + C. \\ \end{array}
$$

例4 求 $\int 2x\mathrm{e}^{x^2}\mathrm{d}x.$ 

解 被积函数中的一个因子为 $\mathrm{e}^{x^2} = \mathrm{e}^u, u = x^2$ ，剩下的因子 $2x$ 恰好是中间变量 $u = x^2$ 的导数，于是有

$$
\int 2 x \mathrm{e} ^ {x ^ {2}} \mathrm{d} x = \int \mathrm{e} ^ {x ^ {2}} \mathrm{d} (x ^ {2}) = \int \mathrm{e} ^ {u} \mathrm{d} u = \mathrm{e} ^ {u} + C = \mathrm{e} ^ {x ^ {2}} + C.
$$

例5 求 $\int x\sqrt{1 - x^2}\mathrm{d}x.$ 

解 设 $u = 1 - x^2$ ，则 $\mathrm{d}u = -2x\mathrm{d}x$ ，即 $-\frac{1}{2}\mathrm{d}u = x\mathrm{d}x$ ，因此，

$$
\int x \sqrt {1 - x ^ {2}} \mathrm{d} x = \int u ^ {\frac {1}{2}} \cdot \left(- \frac {1}{2}\right) \mathrm{d} u = - \frac {1}{2} \frac {u ^ {\frac {3}{2}}}{\frac {3}{2}} + C = - \frac {1}{3} u ^ {\frac {3}{2}} + C = - \frac {1}{3} (1 - x ^ {2}) ^ {\frac {3}{2}} + C.
$$

在对变量代换比较熟练以后,就不一定写出中间变量 u.

例6 求 $\int \frac{1}{a^2 + x^2} \mathrm{d}x (a \neq 0)$ .

解 $\int \frac{1}{a^2 + x^2}\mathrm{d}x = \int \frac{1}{a^2}\cdot \frac{1}{1 + \left(\frac{x}{a}\right)^2}\mathrm{d}x = \frac{1}{a}\int \frac{1}{1 + \left(\frac{x}{a}\right)^2}\mathrm{d}\frac{x}{a} = \frac{1}{a}\arctan \frac{x}{a} +C.$ 

在上例中,我们实际上已经用了变量代换 $u=\frac{x}{a}$ ，并在求出积分 $\frac{1}{a}\int\frac{1}{1+u^{2}}du$ 之后，代回了原积分变量 x，只是没有把这些步骤写出来而已.

例7 求 $\int \frac{\mathrm{d}x}{\sqrt{a^2 - x^2}} (a > 0)$ .

解 $\int \frac{\mathrm{d}x}{\sqrt{a^2 - x^2}} = \int \frac{1}{a}\cdot \frac{\mathrm{d}x}{\sqrt{1 - \left(\frac{x}{a}\right)^2}} = \int \frac{\mathrm{d}\frac{x}{a}}{\sqrt{1 - \left(\frac{x}{a}\right)^2}} = \arcsin \frac{x}{a} +C.$ 

例8 求 $\int \frac{1}{x^2 - a^2} \mathrm{d}x (a \neq 0)$ .

解 由于

$$
\frac {1}{x ^ {2} - a ^ {2}} = \frac {1}{2 a} \left(\frac {1}{x - a} - \frac {1}{x + a}\right),
$$

所以

$$
\begin{array}{l} \int \frac {1}{x ^ {2} - a ^ {2}} \mathrm{d} x = \frac {1}{2 a} \int \left(\frac {1}{x - a} - \frac {1}{x + a}\right) \mathrm{d} x = \frac {1}{2 a} \left(\int \frac {1}{x - a} \mathrm{d} x - \int \frac {1}{x + a} \mathrm{d} x\right) \\ = \frac {1}{2 a} \left[ \int \frac {1}{x - a} d (x - a) - \int \frac {1}{x + a} d (x + a) \right] \\ = \frac {1}{2 a} (\ln | x - a | - \ln | x + a |) + C = \frac {1}{2 a} \ln \left| \frac {x - a}{x + a} \right| + C. \\ \end{array}
$$

例9 求 $\int \frac{\mathrm{d}x}{x(1 + 2\ln x)}.$ 

解 $\int \frac{\mathrm{d}x}{x(1 + 2\ln x)} = \int \frac{\mathrm{d}(\ln x)}{1 + 2\ln x} = \frac{1}{2}\int \frac{\mathrm{d}(1 + 2\ln x)}{1 + 2\ln x} = \frac{1}{2}\ln |1 + 2\ln x| + C.$ 

例10 求 $\int \frac{\mathrm{e}^{\sqrt[3]{x}}}{\sqrt{x}}\mathrm{d}x.$ 

解 由于 $\mathrm{d}\sqrt{x} = \frac{1}{2}\frac{\mathrm{d}x}{\sqrt{x}}$ ，因此，

$$
\int \frac {\mathrm{e} ^ {3 \sqrt {x}}}{\sqrt {x}} \mathrm{d} x = 2 \int \mathrm{e} ^ {3 \sqrt {x}} \mathrm{d} \sqrt {x} = \frac {2}{3} \int \mathrm{e} ^ {3 \sqrt {x}} \mathrm{d} (3 \sqrt {x}) = \frac {2}{3} \mathrm{e} ^ {3 \sqrt {x}} + C.
$$

下面再举一些积分的例子,它们的被积函数中含有三角函数,在计算这种积分的过程中,往往要用到一些三角恒等式.

例11 求 $\int \sin^3 x\mathrm{d}x.$ 

解 $\int \sin^3 x\mathrm{d}x = \int \sin^2 x\sin x\mathrm{d}x = -\int (1 - \cos^2 x)\mathrm{d}(\cos x) = -\cos x + \frac{1}{3}\cos^3 x + C.$ 

例12 求 $\int \sin^2 x\cos^5 x\mathrm{d}x.$ 

$$
\begin{array}{l} = \int \left(\sin^ {2} x - 2 \sin^ {4} x + \sin^ {6} x\right) d (\sin x) \\ = \frac {1}{3} \sin^ {3} x - \frac {2}{5} \sin^ {5} x + \frac {1}{7} \sin^ {7} x + C. \\ \end{array}
$$

解 $\int \sin^2 x\cos^5 x\mathrm{d}x = \int \sin^2 x\cos^4 x\cos x\mathrm{d}x = \int \sin^2 x(1 - \sin^2 x)^2\mathrm{d}(\sin x)$ 

一般地,对于 $\sin^{2k+1}x\cos^{n}x$ 或 $\sin^{n}x\cos^{2k+1}x$ （其中 $k\in N$ ）型函数的积分,总可依次作变换 $u=\cos x$ 或 $u=\sin x$ ,求得结果.

例13 求 $\int \tan x\mathrm{d}x.$ 

解 $\int \tan x\mathrm{d}x = \int \frac{\sin x}{\cos x}\mathrm{d}x = -\int \frac{1}{\cos x}\mathrm{d}(\cos x) = -\ln |\cos x| + C.$ 

类似地可得

$$
\int \cot x \mathrm{d} x = \ln | \sin x | + C.
$$

例14 求 $\int \cos^2 x\mathrm{d}x.$ 

解 $\int \cos^2 x\mathrm{d}x = \int \frac{1 + \cos 2x}{2}\mathrm{d}x = \frac{1}{2}\left(\int \mathrm{d}x + \int \cos 2x\mathrm{d}x\right)$ 

$$
= \frac {1}{2} \int \mathrm{d} x + \frac {1}{4} \int \cos 2 x \mathrm{d} (2 x) = \frac {x}{2} + \frac {\sin 2 x}{4} + C.
$$

例15 求 $\int \sin^2 x\cos^4 x\mathrm{d}x$ 

$$
\begin{array}{l} = \frac {1}{8} \int (1 + \cos 2 x - \cos^ {2} 2 x - \cos^ {3} 2 x) d x \\ = \frac {1}{8} \int (\cos 2 x - \cos^ {3} 2 x) d x + \frac {1}{8} \int (1 - \cos^ {2} 2 x) d x \\ = \frac {1}{8} \int \sin^ {2} 2 x \cdot \frac {1}{2} d (\sin 2 x) + \frac {1}{8} \int \frac {1}{2} (1 - \cos 4 x) d x \\ = \frac {1}{4 8} \sin^ {3} 2 x + \frac {x}{1 6} - \frac {1}{6 4} \sin 4 x + C. \\ \end{array}
$$

解 $\int \sin^2 x\cos^4 x\mathrm{d}x = \frac{1}{8}\int (1 - \cos 2x)(1 + \cos 2x)^2\mathrm{d}x$ 

一般地, 对于 $\sin^{2k} x \cos^{2l} x (k, l \in \mathbb{N})$ 型函数, 总可利用三角恒等式: $\sin^2 x = \frac{1}{2} (1 - \cos 2x), \cos^2 x = \frac{1}{2} (1 + \cos 2x)$ 化成 $\cos 2x$ 的多项式, 然后采用例 15 中所用的方法求得积分的结果.

例 16 求 $\int \sec^{6} x dx$ .

解 $\int \sec^6 x\mathrm{d}x = \int (\sec^2 x)^2\sec^2 x\mathrm{d}x = \int (1 + \tan^2 x)^2\mathrm{d}(\tan x)$ 

$$
= \int (1 + 2 \tan^ {2} x + \tan^ {4} x) d (\tan x) = \tan x + \frac {2}{3} \tan^ {3} x + \frac {1}{5} \tan^ {5} x + C.
$$

例 17 求 $\int \tan^{5} x \sec^{3} x dx.$ 

解 $\int \tan^5 x\sec^3 x\mathrm{d}x$ 

$$
\begin{array}{l} = \int \tan^ {4} x \sec^ {2} x \sec x \tan x d x = \int (\sec^ {2} x - 1) ^ {2} \sec^ {2} x d (\sec x) \\ = \int (\sec^ {6} x - 2 \sec^ {4} x + \sec^ {2} x) d (\sec x) = \frac {1}{7} \sec^ {7} x - \frac {2}{5} \sec^ {5} x + \frac {1}{3} \sec^ {3} x + C. \\ \end{array}
$$

一般地,对于 $\tan^{n}x\sec^{2k}x$ 或 $\tan^{2k-1}x\sec^{n}x$ ( $n,k\in N_{+}$ ) 型函数的积分,可依次作变换 $u=\tan x$ 或 $u=\sec x$ ,求得结果.

例 18 求 $\int \csc x dx.$ 

解 $\int \csc x\mathrm{d}x = \int \frac{\mathrm{d}x}{\sin x} = \int \frac{\mathrm{d}x}{2\sin\frac{x}{2}\cos\frac{x}{2}}$ 

$$
= \int \frac {\mathrm{d} \left(\frac {x}{2}\right)}{\tan \frac {x}{2} \cos^ {2} \frac {x}{2}} = \int \frac {\mathrm{d} \left(\tan \frac {x}{2}\right)}{\tan \frac {x}{2}} = \ln \left| \tan \frac {x}{2} \right| + C.
$$

因为

$$
\tan \frac {x}{2} = \frac {\sin \frac {x}{2}}{\cos \frac {x}{2}} = \frac {2 \sin^ {2} \frac {x}{2}}{\sin x} = \frac {1 - \cos x}{\sin x} = \csc x - \cot x,
$$

所以上述不定积分又可表示为

$$
\int \csc x \mathrm{d} x = \ln | \csc x - \cot x | + C.
$$

例19 求 $\int \sec x\mathrm{d}x.$ 

解 利用上例的结果,有

$$
\begin{array}{l} \int \sec x d x = \int \csc \left(x + \frac {\pi}{2}\right) d \left(x + \frac {\pi}{2}\right) \\ = \ln \left| \csc \left(x + \frac {\pi}{2}\right) - \cot \left(x + \frac {\pi}{2}\right) \right| + C = \ln | \sec x + \tan x | + C. \\ \end{array}
$$

例 20 求 $\int \cos 3x \cos 2x dx$ .

解 利用三角函数的积化和差公式

$$
\cos A \cos B = \frac {1}{2} [ \cos (A - B) + \cos (A + B) ]
$$

得

$$
\cos 3 x \cos 2 x = \frac {1}{2} (\cos x + \cos 5 x),
$$

于是

$$
\begin{array}{l} \int \cos 3 x \cos 2 x d x = \frac {1}{2} \int (\cos x + \cos 5 x) d x \\ = \frac {1}{2} \left[ \int \cos x d x + \frac {1}{5} \int \cos 5 x d (5 x) \right] \\ = \frac {1}{2} \sin x + \frac {1}{1 0} \sin 5 x + C. \\ \end{array}
$$

上面所举的例子, 可以使我们认识到公式(2-1)在求不定积分中所起的作用. 像复合函数的求导法则在微分学中一样, 公式(2-1)在积分学中也是经常使用的. 但利用公式(2-1)来求不定积分, 一般却比利用复合函数的求导法则求函数的导数要来得困难, 因为其中需要一定的技巧, 而且如何适当地选择变量代换 $u = \varphi(x)$ 没有一般规律可循, 因此要掌握换元法, 除了熟悉一些典型的例子外, 还要做较多的练习才行.

上述各例用的都是第一类换元法, 即形如 $u = \varphi(x)$ 的变量代换. 下面介绍另一种形式的变量代换 $x = \psi(t)$ , 即所谓第二类换元法.

# 二、第二类换元法

上面介绍的第一类换元法是通过变量代换 $u = \varphi(x)$ , 将积分 $\int f[\varphi(x)] \cdot \varphi'(x) \, \mathrm{d}x$ 化为积分 $\int f(u) \, \mathrm{d}u$ .

下面将介绍的第二类换元法是:适当地选择变量代换 $x=\psi(t)$ ，将积分 $\int f(x)\mathrm{d}x$ 化为积分 $\int f[\psi(t)]\psi'(t)\mathrm{d}t.$ 这是另一种形式的变量代换，换元公式可表达为

$$
\int f (x) \mathrm{d} x = \int f [ \psi (t) ] \psi^ {\prime} (t) \mathrm{d} t.
$$

这公式的成立是需要一定条件的. 首先, 等式右边的不定积分要存在, 即 $f[\psi(t)]\psi'(t)$ 有原函数; 其次, $\int f[\psi(t)]\psi'(t)dt$ 求出后必须用 $x = \psi(t)$ 的反函数 $t = \psi^{-1}(x)$ 代回去, 为了保证这反函数存在而且是可导的, 我们假定直接函数 $x = \psi(t)$ 在 $t$ 的某一个区间 (这区间和所考虑的 $x$ 的积分区间相对应) 上是单调的、可导的, 并且 $\psi'(t) \neq 0$ .

归纳上述,我们给出下面的定理:

定理2 设 $x = \psi(t)$ 是单调的可导函数, 并且 $\psi'(t) \neq 0$ . 又设 $f[\psi(t)]\psi'(t)$ 具有原函数, 则有换元公式

$$
\int f (x) \mathrm{d} x = \left[ \int f [ \psi (t) ] \psi^ {\prime} (t) \mathrm{d} t \right] _ {t = \psi^ {- 1} (x)}, \tag {2-2}
$$

其中 $\psi^{-1}(x)$ 是 $x=\psi(t)$ 的反函数.

证 设 $f[\psi(t)]\psi'(t)$ 的原函数为 $\Phi(t)$ , 记 $\Phi[\psi^{-1}(x)] = F(x)$ , 利用复合函数及反函数的求导法则, 得到

$$
F ^ {\prime} (x) = \frac {\mathrm{d} \Phi}{\mathrm{d} t} \cdot \frac {\mathrm{d} t}{\mathrm{d} x} = f [ \psi (t) ] \psi^ {\prime} (t) \cdot \frac {1}{\psi^ {\prime} (t)} = f [ \psi (t) ] = f (x),
$$

即 $F(x)$ 是 $f(x)$ 的原函数. 所以有

$$
\int f (x) \mathrm{d} x = F (x) + C = \Phi [ \psi^ {- 1} (x) ] + C = \left[ \int f [ \psi (t) ] \psi^ {\prime} (t) \mathrm{d} t \right] _ {t = \psi^ {- 1} (x)},
$$

这就证明了公式(2-2).

下面举例说明换元公式(2-2)的应用.

例21 求 $\int \sqrt{a^2 - x^2} \, \mathrm{d}x$ （ $a > 0$ ).

解 求这个积分的困难在于有根式 $\sqrt{a^2 - x^2}$ , 但我们可以利用三角函数公式

$$
\sin^ {2} t + \cos^ {2} t = 1
$$

来化去根式.

设 $x = a\sin t, -\frac{\pi}{2} < t < \frac{\pi}{2}$ , 则 $\sqrt{a^2 - x^2} = \sqrt{a^2 - a^2\sin^2t} = a\cos t, dx = a\cos tdt$ , 于是根式化成了三角式, 所求积分化为

$$
\int \sqrt {a ^ {2} - x ^ {2}} \mathrm{d} x = \int a \cos t \cdot a \cos t \mathrm{d} t = a ^ {2} \int \cos^ {2} t \mathrm{d} t.
$$

利用例 14 的结果得

$$
\int \sqrt {a ^ {2} - x ^ {2}} \mathrm{d} x = a ^ {2} \left(\frac {t}{2} + \frac {\sin 2 t}{4}\right) + C = \frac {a ^ {2}}{2} t + \frac {a ^ {2}}{2} \sin t \cos t + C.
$$

由于 $x = a\sin t, -\frac{\pi}{2} < t < \frac{\pi}{2}$ , 所以

$$
t = \arcsin \frac {x}{a},
$$

$$
\cos t = \sqrt {1 - \sin^ {2} t} = \sqrt {1 - \left(\frac {x}{a}\right) ^ {2}} = \frac {\sqrt {a ^ {2} - x ^ {2}}}{a},
$$

于是所求积分为

$$
\int \sqrt {a ^ {2} - x ^ {2}} \mathrm{d} x = \frac {a ^ {2}}{2} \arcsin \frac {x}{a} + \frac {1}{2} x \sqrt {a ^ {2} - x ^ {2}} + C.
$$

例22 求 $\int \frac{\mathrm{d}x}{\sqrt{x^2 + a^2}} (a > 0)$ .

解 和上例类似,可以利用三角函数公式

$$
1 + \tan^ {2} t = \sec^ {2} t
$$

来化去根式.

设 $x = a\tan t\left(-\frac{\pi}{2} < t < \frac{\pi}{2}\right)$ ，则

$$
\sqrt {x ^ {2} + a ^ {2}} = \sqrt {a ^ {2} \tan^ {2} t + a ^ {2}} = a \sqrt {\tan^ {2} t + 1} = a \sec t, \quad \mathrm{d} x = a \sec^ {2} t \mathrm{d} t,
$$

于是

$$
\int \frac {\mathrm{d} x}{\sqrt {x ^ {2} + a ^ {2}}} = \int \frac {a \sec^ {2} t}{a \sec t} \mathrm{d} t = \int \sec t \mathrm{d} t.
$$

利用例 19 的结果得

$$
\int \frac {\mathrm{d} x}{\sqrt {x ^ {2} + a ^ {2}}} = \ln | \sec t + \tan t | + C.
$$

为了要把 $\sec t$ 及 $\tan t$ 换成 $x$ 的函数, 可以根据 $\tan t = \frac{x}{a}$ 作辅助三角形 (图4-3), 便有

$$
\sec t = \frac {\sqrt {x ^ {2} + a ^ {2}}}{a},
$$

且 $\sec t + \tan t > 0$ ，因此，

$$
\begin{array}{l} \int \frac {\mathrm{d} x}{\sqrt {x ^ {2} + a ^ {2}}} = \ln \left(\frac {x}{a} + \frac {\sqrt {x ^ {2} + a ^ {2}}}{a}\right) + C \\ = \ln (x + \sqrt {x ^ {2} + a ^ {2}}) + C _ {1}, \\ \end{array}
$$

a. 

例23 求 $\int \frac{\mathrm{d}x}{\sqrt{x^2 - a^2}} (a > 0)$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/d08a78083761af84250f82ddda04f847e90343d64c18d539ac2ff84bbd403eeb.jpg)



图4-3


解 和以上两例类似,可以利用公式

$$
\sec^ {2} t - 1 = \tan^ {2} t
$$

来化去根式.注意到被积函数的定义域是 $x > a$ 和 $x < -a$ 两个区间,我们在两个区间内分别求不定积分.

当 $x > a$ 时，设 $x = a\sec t\left(0 < t < \frac{\pi}{2}\right)$ ，则

$$
\sqrt {x ^ {2} - a ^ {2}} = \sqrt {a ^ {2} \sec^ {2} t - a ^ {2}} = a \sqrt {\sec^ {2} t - 1} = a \tan t,
$$

$$
\mathrm{d} x = a \sec t \tan t \mathrm{d} t,
$$

于是

$$
\int \frac {\mathrm{d} x}{\sqrt {x ^ {2} - a ^ {2}}} = \int \frac {a \sec t \tan t}{a \tan t} \mathrm{d} t = \int \sec t \mathrm{d} t = \ln (\sec t + \tan t) + C.
$$

为了把 $\sec t$ 及 $\tan t$ 换成 $x$ 的函数, 我们根据 $\sec t = \frac{x}{a}$ 作辅助三角形 (图4-4), 得到

$$
\tan t = \frac {\sqrt {x ^ {2} - a ^ {2}}}{a},
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/2c2b2126f4032137d59167e871750284066ddb07a75a4374b3251df3689ff9be.jpg)



图4-4


因此

$$
\int \frac {\mathrm{d} x}{\sqrt {x ^ {2} - a ^ {2}}} = \ln \left(\frac {x}{a} + \frac {\sqrt {x ^ {2} - a ^ {2}}}{a}\right) + C = \ln (x + \sqrt {x ^ {2} - a ^ {2}}) + C _ {1},
$$

其中 $C_1 = C - \ln a$ .

当 $x < -a$ 时，令 $x = -u$ ，那么 $u > a$ .由上段结果，有

$$
\begin{array}{l} \int \frac {\mathrm{d} x}{\sqrt {x ^ {2} - a ^ {2}}} = - \int \frac {\mathrm{d} u}{\sqrt {u ^ {2} - a ^ {2}}} = - \ln (u + \sqrt {u ^ {2} - a ^ {2}}) + C \\ = - \ln (- x + \sqrt {x ^ {2} - a ^ {2}}) + C = \ln \frac {- x - \sqrt {x ^ {2} - a ^ {2}}}{a ^ {2}} + C \\ = \ln (- x - \sqrt {x ^ {2} - a ^ {2}}) + C _ {1}, \\ \end{array}
$$

其中 $C_{1}=C-2\ln a.$ 

把在 $x > a$ 及 $x < -a$ 内的结果合起来, 可写作

$$
\int \frac {\mathrm{d} x}{\sqrt {x ^ {2} - a ^ {2}}} = \ln \left| x + \sqrt {x ^ {2} - a ^ {2}} \right| + C.
$$

从上面的三个例子可以看出:如果被积函数含有 $\sqrt{a^{2}-x^{2}}$ ,可以作代换 $x=a\sin t$ 化去根式;如果被积函数含有 $\sqrt{x^{2}+a^{2}}$ ,可以作代换 $x=atan t$ 化去根式;如果被积函数含有 $\sqrt{x^{2}-a^{2}}$ ,可以作代换 $x=\pm a\sec t$ 化去根式.但具体解题时要分析被积函数的具体情况,选取尽可能简捷的代换,不要拘泥于上述的变量代换(如例5、例7).

当被积函数含有 $\sqrt{x^2\pm a^2}$ 时，为了化去根式，除采用三角代换 $x = a\tan t$ 或 $x = \pm a\sec t$ 外，还可利用公式

$$
\mathrm{ch} ^ {2} t - \mathrm{sh} ^ {2} t = 1,
$$

采用双曲代换 $x = a \operatorname{sh} t, x = \pm a \operatorname{ch} t$ 来化去根式.

例如,在例 22 中,可设x=ash t,则

$$
\sqrt {x ^ {2} + a ^ {2}} = \sqrt {a ^ {2} \mathrm{sh} ^ {2} t + a ^ {2}} = a \mathrm{ch} t, \quad \mathrm{d} x = a \mathrm{ch} t \mathrm{d} t,
$$

于是

$$
\begin{array}{l} \int \frac {\mathrm{d} x}{\sqrt {x ^ {2} + a ^ {2}}} = \int \frac {a \operatorname{ch} t}{a \operatorname{ch} t} \mathrm{d} t = \int \mathrm{d} t = t + C = \operatorname{arsh} \frac {x}{a} + C \\ = \ln \left[ \frac {x}{a} + \sqrt {\left(\frac {x}{a}\right) ^ {2} + 1} \right] + C = \ln (x + \sqrt {x ^ {2} + a ^ {2}}) + C _ {1}, \\ \end{array}
$$

其中 $C_{1}=C-\ln a.$ 

在例 23 中, 当 x > a 时, 可设 x = a ch t (t > 0), 则

$$
\sqrt {x ^ {2} - a ^ {2}} = \sqrt {a ^ {2} \operatorname{ch} ^ {2} t - a ^ {2}} = a \operatorname{sh} t, \quad \mathrm{d} x = a \operatorname{sh} t \mathrm{d} t,
$$

于是当 $x > a$ 时，

$$
\begin{array}{l} \int \frac {\mathrm{d} x}{\sqrt {x ^ {2} - a ^ {2}}} = \int \frac {a \mathrm{sh} t}{a \mathrm{sh} t} \mathrm{d} t = \int \mathrm{d} t = t + C = \operatorname{arch} \frac {x}{a} + C \\ = \ln \left[ \frac {x}{a} + \sqrt {\left(\frac {x}{a}\right) ^ {2} - 1} \right] + C = \ln \left(x + \sqrt {x ^ {2} - a ^ {2}}\right) + C _ {1}, \\ \end{array}
$$

其中 $C_1 = C - \ln a$ .

当 $x < -a$ 时，令 $x = -a\operatorname{ch}t(t > 0)$ ，类似可得

$$
\int \frac {\mathrm{d} x}{\sqrt {x ^ {2} - a ^ {2}}} = \ln (- x - \sqrt {x ^ {2} - a ^ {2}}) + C _ {1}.
$$

上节所列基本积分表中没有双曲函数的积分公式,现添加两个常用的双曲函数积分公式:

⑭ $\int \mathrm{sh} x\mathrm{d}x = \mathrm{ch} x + C,$ 

⑮ $\int ch x dx = sh x + C.$ 

下面我们通过例子来介绍一种也很有用的代换——倒代换,利用它常可消去被积函数的分母中的变量因子 x.

例24 求 $\int \frac{\sqrt{a^2 - x^2}}{x^4}\mathrm{d}x (a\neq 0).$ 

解 设 $x = \frac{1}{t}$ , 则 $\mathrm{d}x = -\frac{\mathrm{d}t}{t^2}$ , 于是

$$
\int \frac {\sqrt {a ^ {2} - x ^ {2}}}{x ^ {4}} \mathrm{d} x = \int \frac {\sqrt {a ^ {2} - \frac {1}{t ^ {2}}} \cdot \left(- \frac {\mathrm{d} t}{t ^ {2}}\right)}{\frac {1}{t ^ {4}}} = - \int (a ^ {2} t ^ {2} - 1) ^ {\frac {1}{2}} | t | \mathrm{d} t,
$$

当 $x > 0$ 时，有

$$
\int \frac {\sqrt {a ^ {2} - x ^ {2}}}{x ^ {4}} \mathrm{d} x = - \frac {1}{2 a ^ {2}} \int (a ^ {2} t ^ {2} - 1) ^ {\frac {1}{2}} \mathrm{d} (a ^ {2} t ^ {2} - 1)
$$

$$
= - \frac {\left(a ^ {2} t ^ {2} - 1\right) ^ {\frac {3}{2}}}{3 a ^ {2}} + C = - \frac {\left(a ^ {2} - x ^ {2}\right) ^ {\frac {3}{2}}}{3 a ^ {2} x ^ {3}} + C,
$$

当 x<0 时,有相同的结果.

在本节的例题中,有几个积分是以后经常会遇到的,所以它们通常也被当作公式使用.这样,常用的积分公式,除了基本积分表中的几个外,再添加下面几个(其中常数a>0):

⑯ $\int \tan x\mathrm{d}x = -\ln |\cos x| + C,$ 

⑰ $\int \cot x\mathrm{d}x = \ln |\sin x| + C,$ 

⑱ $\int \sec x dx = \ln | \sec x + \tan x | + C,$ 

⑲ $\int \csc x dx = \ln | \csc x - \cot x | + C,$ 

②0 $\int \frac{\mathrm{d}x}{a^2 + x^2} = \frac{1}{a}\arctan \frac{x}{a} +C,$ 

②1 $\int \frac{\mathrm{d}x}{x^2 - a^2} = \frac{1}{2a}\ln \left|\frac{x - a}{x + a}\right| + C,$ 

② $\int \frac{\mathrm{d}x}{\sqrt{a^2 - x^2}} = \arcsin \frac{x}{a} + C,$ 

②3 $\int \frac{\mathrm{d}x}{\sqrt{x^2 + a^2}} = \ln (x + \sqrt{x^2 + a^2}) + C,$ 

②4 $\int \frac{\mathrm{d}x}{\sqrt{x^2 - a^2}} = \ln |x + \sqrt{x^2 - a^2}| + C.$ 

例25 求 $\int \frac{\mathrm{d}x}{\sqrt{4x^2 + 9}}.$ 

解 $\int \frac{\mathrm{d}x}{\sqrt{4x^2 + 9}} = \int \frac{\mathrm{d}x}{\sqrt{(2x)^2 + 3^2}} = \frac{1}{2}\int \frac{\mathrm{d}(2x)}{\sqrt{(2x)^2 + 3^2}},$ 

利用公式②3,便得

$$
\int \frac {\mathrm{d} x}{\sqrt {4 x ^ {2} + 9}} = \frac {1}{2} \ln (2 x + \sqrt {4 x ^ {2} + 9}) + C.
$$

例26 求 $\int \frac{\mathrm{d}x}{\sqrt{1 + x - x^2}}.$ 

解 $\int \frac{\mathrm{d}x}{\sqrt{1 + x - x^2}} = \int \frac{\mathrm{d}\left(x - \frac{1}{2}\right)}{\sqrt{\left(\frac{\sqrt{5}}{2}\right)^2 - \left(x - \frac{1}{2}\right)^2}},$ 

利用公式②2,便得

$$
\int \frac {\mathrm{d} x}{\sqrt {1 + x - x ^ {2}}} = \arcsin \frac {2 x - 1}{\sqrt {5}} + C.
$$

在例 22 中, 我们用变换 $x = a \tan t$ 消去被积函数中的根式 $\sqrt{x^{2} + a^{2}}$ , 这个变换还能消去被积函数分母中的 $(x^{2} + a^{2})$ 的高次幂. 请看下例.

例27 求 $\int \frac{x^3}{(x^2 - 2x + 2)^2} \mathrm{d}x.$ 

解 分母是二次质因式的平方, 把二次质因式配方成 $(x-1)^{2}+1$ , 令 $x-1=\tan t\left(-\frac{\pi}{2}<t<\frac{\pi}{2}\right)$ , 则

$$
x ^ {2} - 2 x + 2 = \sec^ {2} t, \quad \mathrm{d} x = \sec^ {2} t \mathrm{d} t.
$$

于是

$$
\begin{array}{l} \int \frac {x ^ {3}}{\left(x ^ {2} - 2 x + 2\right) ^ {2}} \mathrm{d} x \\ = \int \frac {(\tan t + 1) ^ {3}}{\sec^ {4} t} \cdot \sec^ {2} t d t \\ = \int \left(\sin^ {3} t \cos^ {- 1} t + 3 \sin^ {2} t + 3 \sin t \cos t + \cos^ {2} t\right) d t \\ = \int (\sin^ {2} t \cos^ {- 1} t + 3 \cos t) \sin t d t + \int (3 \sin^ {2} t + \cos^ {2} t) d t \\ \end{array}
$$

$$
\begin{array}{l} = \int [ (1 - \cos^ {2} t) \cos^ {- 1} t + 3 \cos t ] [ - d (\cos t) ] + \int (2 - \cos 2 t) d t \\ = - \int (\cos^ {- 1} t + 2 \cos t) d (\cos t) + 2 t - \frac {1}{2} \sin 2 t \\ = - \ln \cos t - \cos^ {2} t + 2 t - \sin t \cos t + C, \\ \end{array}
$$

按 $\tan t = x - 1$ 作辅助三角形(图 4-5)，便有

$$
\cos t = \frac {1}{\sqrt {x ^ {2} - 2 x + 2}}, \quad \sin t = \frac {x - 1}{\sqrt {x ^ {2} - 2 x + 2}},
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/bd5bc84bfd8cd13d6fd846a9450a154dc3ebac35ff2d66e151c013a3f79f7f32.jpg)



图4-5


于是

$$
\begin{array}{l} \int \frac {x ^ {3}}{\left(x ^ {2} - 2 x + 2\right) ^ {2}} \mathrm{d} x \\ = \frac {1}{2} \ln (x ^ {2} - 2 x + 2) + 2 \arctan (x - 1) - \frac {x}{x ^ {2} - 2 x + 2} + C. \\ \end{array}
$$

# 习题4-2

1. 在下列各式等号右端的横线处填入适当的系数,使等式成立(例如: $\mathrm{d}x=\frac{1}{4}\mathrm{d}(4x+7)$ ):

(1) $\mathrm{dx} = \_ \mathrm{d}(ax)(a \neq 0)$ ; 

(2) $\mathrm{dx} = \_ \mathrm{d}(7x - 3)$ ; 

(3) $x \, dx = \_\_ d(x^{2})$ ; 

(4) $x\mathrm{d}x = \_\mathrm{d}(5x^2)$ ; 

(5) $x \, dx = \_\_ d(1 - x^{2})$ ; 

(6) $x^{3}\mathrm{d}x = \_\mathrm{d}(3x^{4} - 2)$ ; 

(7) $e^{2x}dx=$ d(e $^{2x}$ ); 

(8) $e^{-\frac{x}{2}}dx= \_d(1+e^{-\frac{x}{2}})$ ; 

(9) $\sin\frac{3}{2}xdx=$ d $\left(\cos\frac{3}{2}x\right)$ ; 

(10) $\frac{\mathrm{d}x}{x} = \_ \mathrm{d}(5\ln |x|)$ ; 

(11) $\frac{\mathrm{d}x}{x} = \_ \mathrm{d}(3 - 5\ln |x|)$ ; 

(12) $\frac{\mathrm{d}x}{1 + 9x^2} = -\mathrm{d}(\arctan 3x)$ ; 

(13) $\frac{\mathrm{d}x}{\sqrt{1 - x^2}} = -\mathrm{d}(1 - \arcsin x)$ ; 

(14) $\frac{x\mathrm{d}x}{\sqrt{1 - x^2}} = -\mathrm{d}\left(\sqrt{1 - x^2}\right).$ 

2. 求下列不定积分(其中 $a, b, \omega, \varphi$ 均为常数):

(1) $\int \mathrm{e}^{5t}\mathrm{d}t;$ 

(2) $\int (3 - 2x)^{3} \mathrm{d}x$ ; 

(3) $\int\frac{dx}{1-2x};$ 

(4) $\int \frac{\mathrm{d}x}{\sqrt[3]{2 - 3x}};$ 

(5) $\int (\sin ax - e^{\frac{x}{b}})dx;$ 

(6) $\int \frac{\sin\sqrt{t}}{\sqrt{t}}\mathrm{d}t;$ 

(7) $\int x\mathrm{e}^{-x^2}\mathrm{d}x;$ 

(8) $\int x\cos (x^2)\mathrm{d}x;$ 

(9) $\int \frac{x}{\sqrt{2 - 3x^2}}\mathrm{d}x;$ 

(10) $\int \frac{3x^3}{1 - x^4}\mathrm{d}x;$ 

(11) $\int \frac{x + 1}{x^2 + 2x + 5} \, \mathrm{d}x$ ; 

(12) $\int \cos^2 (\omega t + \varphi)\sin (\omega t + \varphi)\mathrm{d}t;$ 

(13) $\int \frac{\sin x}{\cos^3 x} \, \mathrm{d}x$ ; 

(14) $\int \frac{\sin x + \cos x}{\sqrt[3]{\sin x - \cos x}}\mathrm{d}x;$ 

(15) $\int \tan^{10} x \cdot \sec^2 x \, \mathrm{d}x$ ; 

(16) $\int \frac{\mathrm{d}x}{x\ln x\ln\ln x};$ 

(17) $\int \frac{\mathrm{d}x}{(\arcsin x)^2\sqrt{1 - x^2}};$ 

(18) $\int \frac{10^{2\arccos x}}{\sqrt{1 - x^2}}\mathrm{d}x;$ 

(19) $\int \tan \sqrt{1 + x^2} \cdot \frac{x \, \mathrm{d}x}{\sqrt{1 + x^2}};$ 

(20) $\int \frac{\arctan\sqrt{x}}{\sqrt{x}(1 + x)}\mathrm{d}x;$ 

(21) $\int \frac{1 + \ln x}{(x\ln x)^2}\mathrm{d}x;$ 

(22) $\int \frac{\mathrm{d}x}{\sin x\cos x}$ ; 

(23) $\int \frac{\ln \tan x}{\cos x \sin x} \, \mathrm{d}x$ ; 

(24) $\int \cos^3 x\mathrm{d}x;$ 

(25) $\int \cos^2 (\omega t + \varphi)\mathrm{d}t;$ 

(26) $\int \sin 2x\cos 3x\mathrm{d}x;$ 

(27) $\int \cos x\cos \frac{x}{2}\mathrm{d}x;$ 

(28) $\int \sin 5x\sin 7x\mathrm{d}x;$ 

(29) $\int \tan^3 x\sec x\mathrm{d}x;$ 

(30) $\int \frac{\mathrm{d}x}{\mathrm{e}^x + \mathrm{e}^{-x}};$ 

(31) $\int \frac{1 - x}{\sqrt{9 - 4x^2}}\mathrm{d}x;$ 

(32) $\int \frac{x^3}{9 + x^2} \, \mathrm{d}x$ ; 

(33) $\int \frac{\mathrm{d}x}{2x^2 - 1}$ ; 

(34) $\int \frac{\mathrm{d}x}{(x + 1)(x - 2)};$ 

(35) $\int \frac{x}{x^2 - x - 2} \, \mathrm{d}x$ ; 

(36) $\int \frac{x^2\mathrm{d}x}{\sqrt{a^2 - x^2}} (a > 0)$ ; 

(37) $\int \frac{\mathrm{d}x}{x\sqrt{x^2 - 1}};$ 

(38) $\int \frac{\mathrm{d}x}{\sqrt{(x^2 + 1)^3}};$ 

(39) $\int \frac{\sqrt{x^2 - 9}}{x} \, \mathrm{d}x$ ; 

(40) $\int \frac{\mathrm{d}x}{1 + \sqrt{2x}};$ 

(41) $\int \frac{\mathrm{d}x}{1 + \sqrt{1 - x^2}};$ 

(42) $\int \frac{\mathrm{d}x}{x + \sqrt{1 - x^2}};$ 

(43) $\int \frac{x - 1}{x^2 + 2x + 3} \, \mathrm{d}x$ ; 

(44) $\int \frac{x^3 + 1}{(x^2 + 1)^2} \, \mathrm{d}x.$ 

# 第三节 分部积分法

前面我们在复合函数求导法则的基础上,得到了换元积分法.现在我们利用两个函数乘积的求导法则,来推得另一个求积分的基本方法——分部积分法.

设函数 $u = u(x)$ 及 $v = v(x)$ 具有连续导数，则两个函数乘积的导数公式为

$$
(u v) ^ {\prime} = u ^ {\prime} v + u v ^ {\prime},
$$

移项,得

$$
u v ^ {\prime} = (u v) ^ {\prime} - u ^ {\prime} v.
$$

对这个等式两边求不定积分,得

$$
\int u v ^ {\prime} \mathrm{d} x = u v - \int u ^ {\prime} v \mathrm{d} x. \tag {3-1}
$$

公式(3-1)称为分部积分公式.如果求 $\int uv' \mathrm{d}x$ 有困难,而求 $\int u' v \mathrm{d}x$ 比较容易时,分部积分公式就可以发挥作用了.

为简便起见,也可把公式(3-1)写成下面的形式:

$$
\int u \mathrm{d} v = u v - \int v \mathrm{d} u. \tag {3-2}
$$

现在通过例子说明如何运用这个重要公式.

例1 求 $\int x\cos x\mathrm{d}x.$ 

解 这个积分用换元积分法不易求得结果, 现在试用分部积分法来求它. 但是怎样选取 u 和 dv 呢? 如果设 u = x, dv = cos x dx, 则 du = dx, v = sin x, 代入分部积分公式 (3-2), 得

$$
\int x \cos x \mathrm{d} x = x \sin x - \int \sin x \mathrm{d} x,
$$

而 $\int v\mathrm{d}u = \int \sin x\mathrm{d}x$ 容易积出，所以

$$
\int x \cos x \mathrm{d} x = x \sin x + \cos x + C.
$$

求这个积分时,如果设 $u=\cos x$ , dv=xdx, 则

$$
\mathrm{d} u = - \sin x \mathrm{d} x, \quad v = \frac {x ^ {2}}{2}.
$$

于是

$$
\int x \cos x \mathrm{d} x = \frac {x ^ {2}}{2} \cos x + \int \frac {x ^ {2}}{2} \sin x \mathrm{d} x.
$$

上式右端的积分比原积分更不容易求出.

由此可见,如果 u 和 dv 选取不当,就求不出结果,所以应用分部积分法时,恰当选取 u 和 dv 是一个关键.选取 u 和 dv 一般要考虑下面两点:

(1) v 要容易求得;

(2) $\int vdu$ 要比 $\int udv$ 容易积出.

例2 求 $\int x\mathrm{e}^{x}\mathrm{d}x.$ 

解 设 $u = x, \mathrm{d}v = \mathrm{e}^x\mathrm{d}x$ ，则 $\mathrm{d}u = \mathrm{d}x, v = \mathrm{e}^x$ 。于是

$$
\int x \mathrm{e} ^ {x} \mathrm{d} x = x \mathrm{e} ^ {x} - \int \mathrm{e} ^ {x} \mathrm{d} x = x \mathrm{e} ^ {x} - \mathrm{e} ^ {x} + C = \mathrm{e} ^ {x} (x - 1) + C.
$$

运用分部积分公式(3-2)的形式,例1、例2的求解过程也可表述为

$$
\begin{array}{l} \int x \cos x \mathrm{d} x = \int x \mathrm{d} (\sin x) = x \sin x - \int \sin x \mathrm{d} x = x \sin x + \cos x + C. \\ \int x \mathrm{e} ^ {x} \mathrm{d} x = \int x \mathrm{d} (\mathrm{e} ^ {x}) = x \mathrm{e} ^ {x} - \int \mathrm{e} ^ {x} \mathrm{d} x = x \mathrm{e} ^ {x} - \mathrm{e} ^ {x} + C = (x - 1) \mathrm{e} ^ {x} + C. \\ \end{array}
$$

例3 求 $\int x^{2}\mathrm{e}^{x}\mathrm{d}x.$ 

解 设 $u = x^2, \mathrm{d}v = \mathrm{e}^x\mathrm{d}x = \mathrm{d}\left(\mathrm{e}^x\right)$ ，则

$$
\int x ^ {2} \mathrm{e} ^ {x} \mathrm{d} x = \int x ^ {2} \mathrm{d} (\mathrm{e} ^ {x}) = x ^ {2} \mathrm{e} ^ {x} - \int \mathrm{e} ^ {x} \mathrm{d} (x ^ {2}) = x ^ {2} \mathrm{e} ^ {x} - 2 \int x \mathrm{e} ^ {x} \mathrm{d} x.
$$

这里 $\int x\mathrm{e}^x\mathrm{d}x$ 比 $\int x^{2}\mathrm{e}^{x}\mathrm{d}x$ 容易积出，因为被积函数中 $x$ 的幂次前者比后者降低了一次.由例2可知，对 $\int x\mathrm{e}^x\mathrm{d}x$ 再使用一次分部积分法就可以了.于是

$$
\begin{array}{l} \int x ^ {2} \mathrm{e} ^ {x} \mathrm{d} x = x ^ {2} \mathrm{e} ^ {x} - 2 \int x \mathrm{e} ^ {x} \mathrm{d} x = x ^ {2} \mathrm{e} ^ {x} - 2 \int x \mathrm{d} (\mathrm{e} ^ {x}) \\ = x ^ {2} \mathrm{e} ^ {x} - 2 (x \mathrm{e} ^ {x} - \mathrm{e} ^ {x}) + C = \mathrm{e} ^ {x} (x ^ {2} - 2 x + 2) + C. \\ \end{array}
$$

总结上面三个例子可以知道,如果被积函数是幂函数和正(余)弦函数或幂函数和指数函数的乘积,就可以考虑用分部积分法,并设幂函数为 u. 这样用一次分部积分法就可以使幂函数的幂次降低一次.这里假定幂指数是正整数.

例4 求 $\int x\ln x\mathrm{d}x.$ 

解 设 $u = \ln x, \mathrm{d}v = x\mathrm{d}x$ ，则

$$
\begin{array}{l} \int x \ln x \mathrm{d} x = \int \ln x \mathrm{d} \left(\frac {x ^ {2}}{2}\right) = \frac {x ^ {2}}{2} \ln x - \int \frac {x ^ {2}}{2} \mathrm{d} (\ln x) \\ = \frac {x ^ {2}}{2} \ln x - \frac {1}{2} \int x \mathrm{d} x = \frac {x ^ {2}}{2} \ln x - \frac {x ^ {2}}{4} + C. \\ \end{array}
$$

例 5 求 $\int \arccos x dx$ .

解 设 $u = \arccos x, \mathrm{d}v = \mathrm{d}x$ ，则

$$
\begin{array}{l} \int \arccos x \mathrm{d} x = x \arccos x - \int x \mathrm{d} (\arccos x) = x \arccos x + \int \frac {x}{\sqrt {1 - x ^ {2}}} \mathrm{d} x \\ = x \arccos x - \frac {1}{2} \int \frac {1}{(1 - x ^ {2}) ^ {\frac {1}{2}}} d (1 - x ^ {2}) = x \arccos x - \sqrt {1 - x ^ {2}} + C. \\ \end{array}
$$

在分部积分法运用比较熟练以后,就不必再写出哪一部分选作 u, 哪一部分选作 dv. 只要把被积表达式凑成 $\varphi(x)\mathrm{d}\psi(x)$ 的形式, 便可使用分部积分公式.

例6 求 $\int x\arctan x\mathrm{d}x.$ 

$$
\begin{array}{l} = \frac {x ^ {2}}{2} \arctan x - \frac {1}{2} \int \frac {1 + x ^ {2} - 1}{1 + x ^ {2}} d x = \frac {x ^ {2}}{2} \arctan x - \frac {1}{2} \int \left(1 - \frac {1}{1 + x ^ {2}}\right) d x \\ = \frac {x ^ {2}}{2} \arctan x - \frac {1}{2} (x - \arctan x) + C = \frac {1}{2} (x ^ {2} + 1) \arctan x - \frac {1}{2} x + C. \\ \end{array}
$$

解 $\int x\arctan x\mathrm{d}x=\frac{1}{2}\int\arctan x\mathrm{d}(x^{2})=\frac{x^{2}}{2}\arctan x-\frac{1}{2}\int\frac{x^{2}}{1+x^{2}}\mathrm{d}x$ 

总结上面三个例子可以知道,如果被积函数是幂函数和对数函数或幂函数和反三角函数的乘积,就可以考虑用分部积分法,并设对数函数或反三角函数为 u.

下面几个例子中所用的方法也是比较典型的.

例7 求 $\int \mathrm{e}^{x}\sin x\mathrm{d}x.$ 

解 $\int \mathrm{e}^{x}\sin x\mathrm{d}x = \int \sin x\mathrm{d}(e^{x}) = e^{x}\sin x - \int e^{x}\cos x\mathrm{d}x,$ 

等式右端的积分与等式左端的积分是同一类型的,对右端的积分再用一次分部积分法,得

$$
\int \mathrm{e} ^ {x} \sin x \mathrm{d} x = \mathrm{e} ^ {x} \sin x - \int \cos x \mathrm{d} (\mathrm{e} ^ {x}) = \mathrm{e} ^ {x} \sin x - \mathrm{e} ^ {x} \cos x - \int \mathrm{e} ^ {x} \sin x \mathrm{d} x,
$$

由于上式右端的第三项就是所求的积分 $\int \mathrm{e}^x\sin x\mathrm{d}x$ ，把它移到等号左端去，等式两端再同除以2，便得

$$
\int \mathrm{e} ^ {x} \sin x \mathrm{d} x = \frac {1}{2} \mathrm{e} ^ {x} (\sin x - \cos x) + C.
$$

因上式右端已不包含积分项,所以必须加上任意常数 C.

例 8 求 $\int \sec^{3} x dx$ .

解 $\int \sec^3 x\mathrm{d}x = \int \sec x\mathrm{d}(\tan x)$ 

$$
= \sec x \tan x - \int \sec x \tan^ {2} x d x
$$

$$
= \sec x \tan x - \int \sec x (\sec^ {2} x - 1) d x
$$

$$
= \sec x \tan x - \int \sec^ {3} x \mathrm{d} x + \int \sec x \mathrm{d} x
$$

$$
= \sec x \tan x + \ln | \sec x + \tan x | - \int \sec^ {3} x d x.
$$

由于上式右端的第三项就是所求的积分 $\int \sec^3 x\mathrm{d}x$ ，把它移到等号左端去，等式两端再同时除以2，便得

$$
\int \sec^ {3} x \mathrm{d} x = \frac {1}{2} (\sec x \tan x + \ln | \sec x + \tan x |) + C.
$$

在积分的过程中往往要兼用换元法与分部积分法,如例5,下面再来举一个例子.

例9 求 $\int \mathrm{e}^{\sqrt{x}}\mathrm{d}x.$ 

解 令 $\sqrt{x} = t$ ，则 $x = t^2, \mathrm{d}x = 2t\mathrm{d}t.$ 于是

$$
\int \mathrm{e} ^ {\sqrt {x}} \mathrm{d} x = 2 \int t \mathrm{e} ^ {t} \mathrm{d} t.
$$

利用例 2 的结果, 并用 $t=\sqrt{x}$ 代回, 便得所求积分:

$$
\int \mathrm{e} ^ {\sqrt {x}} \mathrm{d} x = 2 \int t \mathrm{e} ^ {t} \mathrm{d} t = 2 \mathrm{e} ^ {t} (t - 1) + C = 2 \mathrm{e} ^ {\sqrt {x}} (\sqrt {x} - 1) + C.
$$

# 习题4-3

求下列不定积分：

1. $\int x\sin x\mathrm{d}x.$ 

2. $\int \ln x\mathrm{d}x.$ 

3. $\int \arcsin x\mathrm{d}x.$ 

4. $\int x\mathrm{e}^{-x}\mathrm{d}x.$ 

5. $\int x^{2}\ln x\mathrm{d}x.$ 

6. $\int \mathrm{e}^{-x}\cos x\mathrm{d}x.$ 

7. $\int \mathrm{e}^{-2x}\sin \frac{x}{2}\mathrm{d}x.$ 

8. $\int x\cos \frac{x}{2}\mathrm{d}x.$ 

9. $\int x^{2}\arctan x\mathrm{d}x.$ 

10. $\int x\tan^2 x\mathrm{d}x.$ 

11. $\int x^{2}\cos x\mathrm{d}x.$ 

12. $\int t\mathrm{e}^{-2t}\mathrm{d}t.$ 

13. $\int \ln^{2} x dx.$ 

14. $\int x\sin x\cos x\mathrm{d}x.$ 

15. $\int x^{2}\cos^{2}\frac{x}{2}\mathrm{d}x.$ 

16. $\int x\ln (x - 1)\mathrm{d}x.$ 

17. $\int (x^{2} - 1)\sin 2x\mathrm{d}x.$ 

18. $\int \frac{\ln^3 x}{x^2} \, \mathrm{d}x$ . 

19. $\int \mathrm{e}^{\sqrt[3]{x}}\mathrm{d}x.$ 

20. $\int \cos \ln x\mathrm{d}x.$ 

21. $\int (\arcsin x)^{2} \mathrm{d}x$ . 

22. $\int \mathrm{e}^{x}\sin^{2}x\mathrm{d}x.$ 

23. $\int x\ln^2 x\mathrm{d}x.$ 

24. $\int \mathrm{e}^{\sqrt{3x + 9}}\mathrm{d}x.$ 

# 第四节 有理函数的积分

前面已经介绍了求不定积分的两个基本方法——换元积分法和分部积分法，下面简要地介绍有理函数的积分及可化为有理函数的积分.

# 一、有理函数的积分

两个多项式的商 $\frac{P(x)}{Q(x)}$ 称为有理函数,又称有理分式.我们总假定分子多项式 $P(x)$ 与分母多项式 $Q(x)$ 之间没有公因式.当分子多项式 $P(x)$ 的次数小于分母多项式 $Q(x)$ 的次数时,称这有理函数为真分式,否则称为假分式.

利用多项式的除法, 总可以将一个假分式化成一个多项式与一个真分式之和的形式, 例如第一节例 15 中的被积函数

$$
\frac {2 x ^ {4} + x ^ {2} + 3}{x ^ {2} + 1} = 2 x ^ {2} - 1 + \frac {4}{x ^ {2} + 1}.
$$

对于真分式 $\frac{P(x)}{Q(x)}$ ，如果分母可分解为两个多项式的乘积

$$
Q (x) = Q _ {1} (x) Q _ {2} (x),
$$

且 $Q_{1}(x)$ 与 $Q_{2}(x)$ 没有公因式，那么它可分拆成两个真分式之和

$$
\frac {P (x)}{Q (x)} = \frac {P _ {1} (x)}{Q _ {1} (x)} + \frac {P _ {2} (x)}{Q _ {2} (x)},
$$

上述步骤称为把真分式化成部分分式之和.如果 $Q_{1}(x)$ 或 $Q_{2}(x)$ 还能再分解成两个没有公因式的多项式的乘积,那么就可再分拆成更简单的部分分式.最后,有理函数的分解式中只出现多项式、 $\frac{P_{1}(x)}{(x-a)^{k}}$ 、 $\frac{P_{2}(x)}{(x^{2}+px+q)^{l}}$ 等三类函数(这里 $p^{2}-4q<0$ , $P_{1}(x)$ 为小于 k 次的多项式, $P_{2}(x)$ 为小于 2l 次的多项式).多项式的积分容易求得,后两类真分式的积分可参看第二节例 3 和例 27.

下面举几个真分式的积分的例子.

例1 求 $\int \frac{x + 1}{x^2 - 5x + 6}\mathrm{d}x.$ 

解 被积函数的分母分解成 $(x - 3)(x - 2)$ , 故可设

$$
\frac {x + 1}{x ^ {2} - 5 x + 6} = \frac {A}{x - 3} + \frac {B}{x - 2},
$$

其中 A, B 为待定系数. 上式两端去分母后, 得

$$
x + 1 = A (x - 2) + B (x - 3),
$$

即

$$
x + 1 = (A + B) x - 2 A - 3 B.
$$

比较上式两端同次幂的系数,即有

$$
\left\{ \begin{array}{l} A + B = 1, \\ 2 A + 3 B = - 1, \end{array} \right.
$$

从而解得 A=4, B=-3. 于是

$$
\int \frac {x + 1}{x ^ {2} - 5 x + 6} \mathrm{d} x = \int \left(\frac {4}{x - 3} - \frac {3}{x - 2}\right) \mathrm{d} x = 4 \ln | x - 3 | - 3 \ln | x - 2 | + C.
$$

例2 求 $\int \frac{x + 2}{(2x + 1)(x^2 + x + 1)}\mathrm{d}x.$ 

解 设 $\frac{x + 2}{(2x + 1)(x^2 + x + 1)} = \frac{A}{2x + 1} + \frac{Bx + D}{x^2 + x + 1}$ , 则

$$
x + 2 = A \left(x ^ {2} + x + 1\right) + (B x + D) (2 x + 1),
$$

即

$$
x + 2 = (A + 2 B) x ^ {2} + (A + B + 2 D) x + A + D,
$$

比较上式两端同次幂的系数,即有

$$
\left\{ \begin{array}{l} A + 2 B = 0, \\ A + B + 2 D = 1, \\ A + D = 2, \end{array} \right.
$$

从而解得 $\left\{\begin{aligned}A&=2,\\ B&=-1,\\ D&=0.\end{aligned}\right.$ 于是

$$
\begin{array}{l} \int \frac {x + 2}{(2 x + 1) (x ^ {2} + x + 1)} d x \\ = \int \left(\frac {2}{2 x + 1} - \frac {x}{x ^ {2} + x + 1}\right) d x = \ln | 2 x + 1 | - \frac {1}{2} \int \frac {(2 x + 1) - 1}{x ^ {2} + x + 1} d x \\ = \ln | 2 x + 1 | - \frac {1}{2} \int \frac {\mathrm{d} (x ^ {2} + x + 1)}{x ^ {2} + x + 1} + \frac {1}{2} \int \frac {\mathrm{d} x}{\left(x + \frac {1}{2}\right) ^ {2} + \frac {3}{4}} \\ = \ln | 2 x + 1 | - \frac {1}{2} \ln (x ^ {2} + x + 1) + \frac {1}{\sqrt {3}} \arctan \frac {2 x + 1}{\sqrt {3}} + C. \\ \end{array}
$$

例3 求 $\int \frac{x - 3}{(x - 1)(x^2 - 1)}\mathrm{d}x.$ 

解 被积函数分母的两个因式 $x - 1$ 与 $x^{2} - 1$ 有公因式, 故需再分解成 $(x - 1)^{2}(x + 1)$ . 设

$$
\frac {x - 3}{(x - 1) ^ {2} (x + 1)} = \frac {A x + B}{(x - 1) ^ {2}} + \frac {D}{x + 1},
$$

则

$$
x - 3 = (A x + B) (x + 1) + D (x - 1) ^ {2},
$$

即

$$
x - 3 = (A + D) x ^ {2} + (A + B - 2 D) x + B + D,
$$

比较上式两端同次幂的系数,即有

$$
\left\{ \begin{array}{l} A + D = 0, \\ A + B - 2 D = 1, \\ B + D = - 3, \end{array} \right.
$$

从而解得 $\left\{\begin{aligned}A&=1,\\ B&=-2,\\ D&=-1.\end{aligned}\right.$ 于是

$$
\begin{array}{l} \int \frac {x - 3}{(x - 1) (x ^ {2} - 1)} \mathrm{d} x \\ = \int \frac {x - 3}{(x - 1) ^ {2} (x + 1)} d x = \int \left[ \frac {x - 2}{(x - 1) ^ {2}} - \frac {1}{x + 1} \right] d x \\ = \int \frac {x - 1 - 1}{(x - 1) ^ {2}} d x - \ln | x + 1 | \\ = \ln | x - 1 | + \frac {1}{x - 1} - \ln | x + 1 | + C. \\ \end{array}
$$

# 二、可化为有理函数的积分举例

例4 求 $\int \frac{1 + \sin x}{\sin x(1 + \cos x)}\mathrm{d}x.$ 

解 由三角函数公式知道, $\sin x$ 与 $\cos x$ 都可以用 $\tan\frac{x}{2}$ 的有理式表示,即

$$
\sin x = 2 \sin \frac {x}{2} \cos \frac {x}{2} = \frac {2 \tan \frac {x}{2}}{\sec^ {2} \frac {x}{2}} = \frac {2 \tan \frac {x}{2}}{1 + \tan^ {2} \frac {x}{2}},
$$

$$
\cos x = \cos^ {2} \frac {x}{2} - \sin^ {2} \frac {x}{2} = \frac {1 - \tan^ {2} \frac {x}{2}}{\sec^ {2} \frac {x}{2}} = \frac {1 - \tan^ {2} \frac {x}{2}}{1 + \tan^ {2} \frac {x}{2}}.
$$

如果作代换 $u = \tan \frac{x}{2} (-\pi < x < \pi)$ ①, 那么

$$
\sin x = \frac {2 u}{1 + u ^ {2}}, \quad \cos x = \frac {1 - u ^ {2}}{1 + u ^ {2}},
$$

而 $x=2\arctan u$ ，从而

$$
\mathrm{d} x = \frac {2}{1 + u ^ {2}} \mathrm{d} u.
$$

于是

$$
\begin{array}{l} \int \frac {1 + \sin x}{\sin x (1 + \cos x)} d x \\ = \int \frac {\left(1 + \frac {2 u}{1 + u ^ {2}}\right) \frac {2 \mathrm{d} u}{1 + u ^ {2}}}{\frac {2 u}{1 + u ^ {2}} \left(1 + \frac {1 - u ^ {2}}{1 + u ^ {2}}\right)} = \frac {1}{2} \int \left(u + 2 + \frac {1}{u}\right) \mathrm{d} u \\ = \frac {1}{2} \left(\frac {u ^ {2}}{2} + 2 u + \ln | u |\right) + C = \frac {1}{4} \tan^ {2} \frac {x}{2} + \tan \frac {x}{2} + \frac {1}{2} \ln \left| \tan \frac {x}{2} \right| + C. \\ \end{array}
$$

本例所用的变量代换 $u=\tan\frac{x}{2}$ 对三角函数有理式的积分都可以应用.

① 当 $x \in ((2k - 1)\pi, (2k + 1)\pi), k \in \mathbb{Z}$ 时，作代换 $u = \tan \frac{x - 2k\pi}{2} = \tan \frac{x}{2}, x = 2k\pi + 2\arctan u$ ，以下所得结果相同.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/2ad6497a32abb7b39161be00af2dacd8aeb3ab8a3eab48f2437b91e5c28161bb.jpg)


释疑解难

4-4 

例5 求 $\int \frac{\sqrt{x - 1}}{x}\mathrm{d}x.$ 

解 为了去掉根号, 可以设 $\sqrt{x-1}=u$ , 于是 $x=u^{2}+1$ , dx=2u du, 从而所求积分为

$$
\begin{array}{l} \int \frac {\sqrt {x - 1}}{x} \mathrm{d} x = \int \frac {u}{u ^ {2} + 1} \cdot 2 u \mathrm{d} u = 2 \int \frac {u ^ {2}}{u ^ {2} + 1} \mathrm{d} u \\ = 2 \int \left(1 - \frac {1}{1 + u ^ {2}}\right) d u = 2 (u - \arctan u) + C \\ = 2 (\sqrt {x - 1} - \arctan \sqrt {x - 1}) + C. \\ \end{array}
$$

例6 求 $\int \frac{\mathrm{d}x}{1 + \sqrt[3]{x + 2}}.$ 

解 为了去掉根号, 可以设 $\sqrt[3]{x+2}=u$ . 于是 $x=u^{3}-2, dx=3u^{2}du$ , 从而所求积分为

$$
\begin{array}{l} \int \frac {\mathrm{d} x}{1 + \sqrt [ 3 ]{x + 2}} = \int \frac {3 u ^ {2}}{1 + u} \mathrm{d} u \\ = 3 \int \left(u - 1 + \frac {1}{1 + u}\right) d u = 3 \left(\frac {u ^ {2}}{2} - u + \ln | 1 + u |\right) + C \\ = \frac {3}{2} \sqrt [ 3 ]{(x + 2) ^ {2}} - 3 \sqrt [ 3 ]{x + 2} + 3 \ln | 1 + \sqrt [ 3 ]{x + 2} | + C. \\ \end{array}
$$

例7 求 $\int \frac{\mathrm{d}x}{(1 + \sqrt[3]{x})\sqrt{x}}.$ 

解 被积函数中出现了两个根式 $\sqrt{x}$ 及 $\sqrt[3]{x}$ , 为了能同时消去这两个根式, 可令 $x = u^6$ , 于是 $\mathrm{d}x = 6u^5\mathrm{d}u$ , 从而所求积分为

$$
\begin{array}{l} \int \frac {\mathrm{d} x}{(1 + \sqrt [ 3 ]{x}) \sqrt {x}} = \int \frac {6 u ^ {5}}{(1 + u ^ {2}) u ^ {3}} \mathrm{d} u = 6 \int \frac {u ^ {2}}{1 + u ^ {2}} \mathrm{d} u \\ = 6 \int \left(1 - \frac {1}{1 + u ^ {2}}\right) d u = 6 (u - \arctan u) + C \\ = 6 \left(\sqrt [ 6 ]{x} - \arctan \sqrt [ 6 ]{x}\right) + C. \\ \end{array}
$$

例8 求 $\int \frac{1}{x} \sqrt{\frac{1 + x}{x}} \, \mathrm{d}x$ .

解 为了去掉根号, 可以设 $\sqrt{\frac{1+x}{x}} = u$ , 于是 $\frac{1+x}{x} = u^{2}$ , $x = \frac{1}{u^{2}-1}$ , $\mathrm{d}x = -\frac{2u\mathrm{d}u}{(u^{2}-1)^{2}}$ , 从而所求积分为

$$
\int \frac {1}{x} \sqrt {\frac {1 + x}{x}} \mathrm{d} x = \int (u ^ {2} - 1) u \cdot \frac {- 2 u}{(u ^ {2} - 1) ^ {2}} \mathrm{d} u = - 2 \int \frac {u ^ {2}}{u ^ {2} - 1} \mathrm{d} u
$$

$$
\begin{array}{l} = - 2 \int \left(1 + \frac {1}{u ^ {2} - 1}\right) d u = - 2 u - \ln \left| \frac {u - 1}{u + 1} \right| + C \\ = - 2 u + 2 \ln (u + 1) - \ln | u ^ {2} - 1 | + C \\ = - 2 \sqrt {\frac {1 + x}{x}} + 2 \ln \left(\sqrt {\frac {1 + x}{x}} + 1\right) + \ln | x | + C. \\ \end{array}
$$

以上四个例子表明,如果被积函数中含有简单根式 $\sqrt[n]{ax+b}$ 或 $\sqrt[n]{\frac{ax+b}{cx+d}}$ ,可以令这个简单根式为u.由于这样的变换具有反函数,且反函数是u的有理函数,因此原积分即可化为有理函数的积分.

# 习题4- 4

求下列不定积分：

1. $\int \frac{x^3}{x + 3}\mathrm{d}x.$ 

2. $\int \frac{2x + 3}{x^2 + 3x - 10}\mathrm{d}x.$ 

3. $\int\frac{x+1}{x^{2}-2x+5}dx.$ 

4. $\int\frac{dx}{x(x^{2}+1)}$ . 

5. $\int\frac{3}{x^{3}+1}dx.$ 

6. $\int\frac{x^{2}+1}{(x+1)^{2}(x-1)}dx.$ 

7. $\int \frac{x\mathrm{d}x}{(x + 1)(x + 2)(x + 3)}.$ 

8. $\int \frac{x^5 + x^4 - 8}{x^3 - x} \, \mathrm{d}x.$ 

9. $\int \frac{\mathrm{d}x}{(x^2 + 1)(x^2 + x)}.$ 

10. $\int \frac{1}{x^4 - 1} \, \mathrm{d}x.$ 

11. $\int \frac{\mathrm{d}x}{(x^2 + 1)(x^2 + x + 1)}.$ 

12. $\int \frac{(x + 1)^2}{(x^2 + 1)^2} \, \mathrm{d}x.$ 

13. $\int\frac{-x^{2}-2}{(x^{2}+x+1)^{2}}dx.$ 

14. $\int \frac{\mathrm{d}x}{3 + \sin^2 x}$ 

15. $\int\frac{dx}{3+\cos x}.$ 

16. $\int\frac{dx}{2+\sin x}.$ 

17. $\int \frac{\mathrm{d}x}{1 + \sin x + \cos x}$ . 

18. $\int \frac{\mathrm{d}x}{2\sin x - \cos x + 5}$ . 

19. $\int\frac{dx}{1+\sqrt[3]{x+1}}.$ 

20. $\int \frac{(\sqrt{x})^3 - 1}{\sqrt{x} + 1}\mathrm{d}x.$ 

21. $\int \frac{\sqrt{x + 1} - 1}{\sqrt{x + 1} + 1}\mathrm{d}x.$ 

22. $\int \frac{\mathrm{d}x}{\sqrt{x} + \sqrt[4]{x}}.$ 

23. $\int \sqrt{\frac{1 - x}{1 + x}}\frac{\mathrm{d}x}{x}.$ 

24. $\int \frac{\mathrm{d}x}{\sqrt[3]{(x + 1)^2(x - 1)^4}}.$ 

# 第五节 积分表的使用

通过前面的讨论可以看出,积分的计算要比导数的计算来得灵活、复杂.为了实用的方便,往往把常用的积分公式汇集成表,这种表叫做积分表.积分表是按照被积函数的类型来排列的.求积分时,可根据被积函数的类型直接地或经过简单的变形后,在表

内查得所需的结果.

本书末附录IV有一个简单的积分表,以供查阅.

我们先举几个可以直接从积分表中查得结果的积分例子.

例1 求 $\int \frac{x}{(3x + 4)^2} \mathrm{d}x.$ 

解 被积函数含有 $ax + b$ ，在积分表(一)中查得公式7

$$
\int \frac {x}{(a x + b) ^ {2}} \mathrm{d} x = \frac {1}{a ^ {2}} \left(\ln | a x + b | + \frac {b}{a x + b}\right) + C.
$$

现在 $a = 3, b = 4$ ，于是

$$
\int \frac {x}{(3 x + 4) ^ {2}} \mathrm{d} x = \frac {1}{9} \left(\ln | 3 x + 4 | + \frac {4}{3 x + 4}\right) + C.
$$

例2 求 $\int \frac{\mathrm{d}x}{5 - 4\cos x}$ .

解 被积函数含有三角函数, 在积分表(十一)中查得关于积分 $\int \frac{dx}{a+b\cos x}$ 的公式, 但是公式有两个, 要看 $a^{2}>b^{2}$ 或 $a^{2}<b^{2}$ 而决定采用哪一个.

现在 $a = 5, b = -4, a^2 > b^2$ ，所以用公式105

$$
\int \frac {\mathrm{d} x}{a + b \cos x} = \frac {2}{a + b} \sqrt {\frac {a + b}{a - b}} \arctan \left(\sqrt {\frac {a - b}{a + b}} \tan \frac {x}{2}\right) + C \quad (a ^ {2} > b ^ {2}).
$$

于是

$$
\begin{array}{l} \int \frac {\mathrm{d} x}{5 - 4 \cos x} = \frac {2}{5 + (- 4)} \sqrt {\frac {5 + (- 4)}{5 - (- 4)}} \arctan \left(\sqrt {\frac {5 - (- 4)}{5 + (- 4)}} \tan \frac {x}{2}\right) + C \\ = \frac {2}{3} \arctan \left(3 \tan \frac {x}{2}\right) + C. \\ \end{array}
$$

下面再举一个需要先进行变量代换,然后再查表求积分的例子.

例3 求 $\int \frac{\mathrm{d}x}{x\sqrt{4x^2 + 9}}.$ 

解 这个积分不能在表中直接查到,需要先进行变量代换.

令 $2x = u$ ，那么 $\sqrt{4x^2 + 9} = \sqrt{u^2 + 3^2}, x = \frac{u}{2}, \mathrm{d}x = \frac{1}{2}\mathrm{d}u.$ 于是

$$
\int \frac {\mathrm{d} x}{x \sqrt {4 x ^ {2} + 9}} = \int \frac {\frac {1}{2} \mathrm{d} u}{\frac {u}{2} \sqrt {u ^ {2} + 3 ^ {2}}} = \int \frac {\mathrm{d} u}{u \sqrt {u ^ {2} + 3 ^ {2}}}.
$$

被积函数中含有 $\sqrt{u^2 + 3^2}$ ，在积分表(六)中查到公式37

$$
\int \frac {\mathrm{d} x}{x \sqrt {x ^ {2} + a ^ {2}}} = \frac {1}{a} \ln \frac {\sqrt {x ^ {2} + a ^ {2}} - a}{| x |} + C.
$$

现在 $a = 3, x$ 相当于 $u$ , 于是

$$
\int \frac {\mathrm{d} u}{u \sqrt {u ^ {2} + 3 ^ {2}}} = \frac {1}{3} \ln \frac {\sqrt {u ^ {2} + 3 ^ {2}} - 3}{| u |} + C.
$$

再把 u=2x 代入, 最后得到

$$
\int \frac {\mathrm{d} x}{x \sqrt {4 x ^ {2} + 9}} = \int \frac {\mathrm{d} u}{u \sqrt {u ^ {2} + 3 ^ {2}}} = \frac {1}{3} \ln \frac {\sqrt {u ^ {2} + 3 ^ {2}} - 3}{| u |} + C = \frac {1}{3} \ln \frac {\sqrt {4 x ^ {2} + 9} - 3}{2 | x |} + C.
$$

最后,举一个用递推公式求积分的例子.

例4 求 $\int \sin^4 x\mathrm{d}x.$ 

解 在积分表(十一)中查到公式 95

$$
\int \sin^ {n} x \mathrm{d} x = - \frac {\sin^ {n - 1} x \cos x}{n} + \frac {n - 1}{n} \int \sin^ {n - 2} x \mathrm{d} x.
$$

利用这个公式可以使被积函数中正弦的幂次减少2次, 只要重复使用这个公式, 可以使正弦的幂次继续减少, 直到求出最后结果为止, 这种公式叫做递推公式.

现在 $n = 4$ ，于是

$$
\int \sin^ {4} x \mathrm{d} x = - \frac {\sin^ {3} x \cos x}{4} + \frac {3}{4} \int \sin^ {2} x \mathrm{d} x.
$$

对积分 $\int \sin^2 x\mathrm{d}x$ 用公式93

$$
\int \sin^ {2} x \mathrm{d} x = \frac {x}{2} - \frac {1}{4} \sin 2 x + C,
$$

从而所求积分为

$$
\int \sin^ {4} x \mathrm{d} x = - \frac {\sin^ {3} x \cos x}{4} + \frac {3}{4} \left(\frac {x}{2} - \frac {1}{4} \sin 2 x\right) + C.
$$

一般说来,查积分表可以节省计算积分的时间,但是,只有掌握了前面学过的基本积分方法才能灵活地使用积分表,而且对一些比较简单的积分,应用基本积分方法来计算比查表更快些,例如,对 $\int \sin^2 x\cos^3 x\mathrm{d}x$ ,用代换 $u = \sin x$ 很快就可得到结果.所以,求积分时究竟是直接计算,还是查表,或是两者结合使用,应该作具体分析,不能一概而论.

在本章结束之前,我们还要指出:对初等函数来说,在其定义区间上,它的原函数一定存在,但原函数不一定都是初等函数,如

$$
\int \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x, \quad \int \frac {\sin x}{x} \mathrm{d} x, \quad \int \frac {\mathrm{d} x}{\ln x}, \quad \int \frac {\mathrm{d} x}{\sqrt {1 + x ^ {4}}},
$$

等等,它们的原函数就都不是初等函数.

# 习题4- 5

利用积分表计算下列不定积分：

1. $\int \frac{\mathrm{d}x}{\sqrt{4x^2 - 9}}.$ 

2. $\int \frac{1}{x^2 + 2x + 5}\mathrm{d}x.$ 

3. $\int \frac{\mathrm{d}x}{\sqrt{5 - 4x + x^2}}.$ 

4. $\int \sqrt{2x^2 + 9} \, \mathrm{d}x.$ 

5. $\int \sqrt{3x^2 - 2} \, \mathrm{d}x.$ 

6. $\int e^{2x}\cos xdx.$ 

7. $\int x\arcsin \frac{x}{2}\mathrm{d}x.$ 

8. $\int \frac{\mathrm{d}x}{(x^2 + 9)^2}$ . 

9. $\int \frac{\mathrm{d}x}{\sin^3 x}$ . 

10. $\int \mathrm{e}^{-2x}\sin 3x\mathrm{d}x.$ 

11. $\int \sin 3x\sin 5x dx.$ 

12. $\int \ln^3 x\mathrm{d}x.$ 

13. $\int \frac{1}{x^2(1 - x)}\mathrm{d}x.$ 

14. $\int \frac{\sqrt{x - 1}}{x}\mathrm{d}x.$ 

15. $\int \frac{1}{(1 + x^2)^2} \, \mathrm{d}x.$ 

16. $\int \frac{1}{x\sqrt{x^2 - 1}}\mathrm{d}x.$ 

17. $\int \frac{x}{(2 + 3x)^2} \mathrm{d}x.$ 

18. $\int \cos^6 x\mathrm{d}x.$ 

19. $\int x^{2}\sqrt{x^{2} - 2}\mathrm{d}x.$ 

20. $\int \frac{1}{2 + 5\cos x}\mathrm{d}x.$ 

21. $\int \frac{\mathrm{d}x}{x^2\sqrt{2x - 1}}.$ 

22. $\int \sqrt{\frac{1 - x}{1 + x}}\mathrm{d}x.$ 

23. $\int \frac{x + 5}{x^2 - 2x - 1} \, \mathrm{d}x.$ 

24. $\int \frac{x\mathrm{d}x}{\sqrt{1 + x - x^2}}.$ 

25. $\int \frac{x^4}{25 + 4x^2}\mathrm{d}x.$ 

# 总习题四

1. 填空：

(1) $\int x^{3}e^{x}dx =$ 

(2) $\int \frac{x + 5}{x^2 - 6x + 13} \mathrm{d}x =$ 

2. 以下两题中给出了四个结论,从中选出一个正确的结论:

(1) 已知 $f'(x)=\frac{1}{x(1+2\ln x)}$ ，且 $f(1)=1$ ，则 $f(x)$ 等于（）；

(A) $\ln(1+2\ln x)+1$ 

(B) $\frac{1}{2}\ln (1 + 2\ln x) + 1$ 

(C) $\frac{1}{2}\ln(1+2\ln x)+\frac{1}{2}$ 

(D) $2\ln (1 + 2\ln x) + 1$ 

(2) 在下列等式中, 正确的结果是().

(A) $\int f'(x) \, \mathrm{d}x = f(x)$ 

(B) $\int \mathrm{d}f(x) = f(x)$ 

(C) $\frac{\mathrm{d}}{\mathrm{d}x}\int f(x)\mathrm{d}x = f(x)$ 

(D) $\mathrm{d}\int f(x)\mathrm{d}x = f(x)$ 

3. 已知 $\frac{\sin x}{x}$ 是 $f(x)$ 的一个原函数, 求 $\int x^3 f'(x) \mathrm{d}x$ .

4. 求下列不定积分(其中 a, b 为常数):

(1) $\int \frac{\mathrm{d}x}{\mathrm{e}^x - \mathrm{e}^{-x}};$ 

(2) $\int \frac{x}{(1 - x)^3} \mathrm{d}x$ ; 

(3) $\int \frac{x^2}{a^6 - x^6} \, \mathrm{d}x (a > 0)$ ; 

(4) $\int \frac{1 + \cos x}{x + \sin x} \, \mathrm{d}x$ ; 

(5) $\int \frac{\ln \ln x}{x} \, \mathrm{d}x$ ; 

(6) $\int \frac{\sin x \cos x}{1 + \sin^4 x} \, \mathrm{d}x$ ; 

(7) $\int \tan^4 x\mathrm{d}x;$ 

(8) $\int \sin x\sin 2x\sin 3x\mathrm{d}x;$ 

(9) $\int \frac{\mathrm{d}x}{x(x^6 + 4)};$ 

(10) $\int \sqrt{\frac{a + x}{a - x}}\mathrm{d}x (a > 0)$ ; 

(11) $\int \frac{\mathrm{d}x}{\sqrt{x(1 + x)}};$ 

(12) $\int x\cos^2 x\mathrm{d}x;$ 

(13) $\int \mathrm{e}^{ax}\cos bx\mathrm{d}x;$ 

(14) $\int \frac{\mathrm{d}x}{\sqrt{1 + \mathrm{e}^x}};$ 

(15) $\int \frac{\mathrm{d}x}{x^2\sqrt{x^2 - 1}};$ 

(16) $\int \frac{\mathrm{d}x}{\left(a^2 - x^2\right)^{5 / 2}};$ 

(17) $\int \frac{\mathrm{d}x}{x^4\sqrt{1 + x^2}};$ 

(18) $\int \sqrt{x} \sin \sqrt{x} \, \mathrm{d}x$ ; 

(19) $\int \ln(1+x^{2})\mathrm{d}x;$ 

(20) $\int \frac{\sin^2 x}{\cos^3 x} \, \mathrm{d}x$ ; 

(21) $\int \arctan\sqrt{x} dx;$ 

(22) $\int \frac{\sqrt{1 + \cos x}}{\sin x} \, \mathrm{d}x$ ; 

(23) $\int \frac{x^3}{(1 + x^8)^2} \, \mathrm{d}x$ ; 

(24) $\int \frac{x^{11}}{x^8 + 3x^4 + 2} \, \mathrm{d}x$ ; 

(25) $\int \frac{\mathrm{d}x}{16 - x^4};$ 

(26) $\int \frac{\sin x}{1 + \sin x} \, \mathrm{d}x$ ; 

(27) $\int \frac{x + \sin x}{1 + \cos x} \, \mathrm{d}x$ ; 

(28) $\int \mathrm{e}^{\sin x}\frac{x\cos^3x - \sin x}{\cos^2x}\mathrm{d}x;$ 

(29) $\int \frac{\sqrt[3]{x}}{x(\sqrt{x} + \sqrt[3]{x})}\mathrm{d}x;$ 

(30) $\int \frac{\mathrm{d}x}{(1 + \mathrm{e}^x)^2};$ 

(31) $\int \frac{\mathrm{e}^{3x} + \mathrm{e}^x}{\mathrm{e}^{4x} - \mathrm{e}^{2x} + 1}\mathrm{d}x;$ 

(32) $\int \frac{x\mathrm{e}^x}{(\mathrm{e}^x + 1)^2}\mathrm{d}x;$ 

(33) $\int \ln^2 (x + \sqrt{1 + x^2})\mathrm{d}x;$ 

(34) $\int \frac{\ln x}{(1 + x^2)^{\frac{3}{2}}} \, \mathrm{d}x$ ; 

(35) $\int \sqrt{1 - x^2} \arcsin x \, \mathrm{d}x$ ; 

(36) $\int \frac{x^3\arccos x}{\sqrt{1 - x^2}}\mathrm{d}x;$ 

(37) $\int \frac{\cot x}{1 + \sin x} \, \mathrm{d}x$ ; 

(38) $\int \frac{\mathrm{d}x}{\sin^3 x \cos x}$ ; 

(39) $\int \frac{\mathrm{d}x}{(2 + \cos x)\sin x};$ 

(40) $\int \frac{\sin x \cos x}{\sin x + \cos x} \, \mathrm{d}x.$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/d7d77867f4c71f057591f2fede11cf10ee809e60ea5650214b66f91e99adeb9e.jpg)



第四章释疑解难


# 第五章

# 定积分

本章讨论积分学的另一个基本问题——定积分问题.我们先从几何与力学问题出发引进定积分的定义,然后讨论它的性质与计算方法.关于定积分的应用,将在第六章讨论.

# 第一节 定积分的概念与性质

# 一、定积分问题举例

# 1. 曲边梯形的面积

设 $y = f(x)$ 在区间 $[a, b]$ 上非负、连续. 由直线 $x = a, x = b, y = 0$ 及曲线 $y = f(x)$ 所围成的图形(图 5-1)称为曲边梯形,其中曲线弧称为曲边.

我们知道,已知矩形的高和底,它的面积可按公式

$$
\mathrm{矩形面积} = \mathrm{高} \times \mathrm{底}
$$

来定义和计算.而曲边梯形在底边上各点处的高 $f(x)$ 在区间 $[a,b]$ 上是变动的,故它的面积不能直接按上述公式来定义和计算.然而,由于曲边梯形的高 $f(x)$ 在区间 $[a,b]$ 上是连续变化的,在很小一段区间上它的变化很小,近似于不变.因此,如果把区间 $[a,b]$ 划分为许多小区间,在每个小区间上用其中某一点处的高来近似代替同一个小区间上的窄曲边梯形的变高,那么,每个窄曲边梯形就可近似地看成这样得到的窄矩形.我们就以所有这些窄矩形面积之和作为曲边梯形面积的近似值,并把区间 $[a,b]$ 无限细分下去,即使每个小区间的长度都趋于零,这时所有窄矩形面积之和的极限就可定义为曲边梯形的面积.这个定义同时也给出了计算曲边梯形面积的方法,现详述于下:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/603cd0a374cde93ce1b4510fcae33418a5084e148296913ea6c9542a76a56d00.jpg)



图5-1


在区间 $[a, b]$ 中任意插入 $n - 1$ 个分点

$$
a = x _ {0} <   x _ {1} <   x _ {2} <   \dots <   x _ {n - 1} <   x _ {n} = b,
$$

把 $[a,b]$ 分成 $n$ 个小区间

$$
\left[ x _ {0}, x _ {1} \right], \quad \left[ x _ {1}, x _ {2} \right], \quad \dots , \quad \left[ x _ {n - 1}, x _ {n} \right],
$$

它们的长度依次为

$$
\Delta x _ {1} = x _ {1} - x _ {0}, \quad \Delta x _ {2} = x _ {2} - x _ {1}, \quad \dots , \quad \Delta x _ {n} = x _ {n} - x _ {n - 1}.
$$

经过每一个分点作平行于 y 轴的直线段, 把曲边梯形分成 n 个窄曲边梯形. 在每个小区间 $\left[x_{i-1}, x_{i}\right]$ 上任取一点 $\xi_{i}$ , 以 $\left[x_{i-1}, x_{i}\right]$ 为底、 $f(\xi_{i})$ 为高的窄矩形近似替代第 i 个窄曲边梯形 $(i=1,2,\cdots,n)$ , 把这样得到的 n 个窄矩形面积之和作为所求曲边梯形面积 A 的近似值, 即

$$
A \approx f (\xi_ {1}) \Delta x _ {1} + f (\xi_ {2}) \Delta x _ {2} + \dots + f (\xi_ {n}) \Delta x _ {n} = \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i}.
$$

为了保证所有小区间的长度都无限缩小,我们要求小区间长度中的最大者趋于零,如记 $\lambda=\max\left\{\Delta x_{1},\Delta x_{2},\cdots,\Delta x_{n}\right\}$ ，则上述条件可表示为 $\lambda\to0$ 。当 $\lambda\to0$ 时(这时分段数 n 无限增多,即 $n\to\infty$ )，取上述和式的极限,便得曲边梯形的面积

$$
A = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i}.
$$

# 2. 变速直线运动的路程

设某物体做直线运动,已知速度 $v=v(t)$ 是时间间隔 $\left[T_{1},T_{2}\right]$ 上 t 的连续函数,且 $v(t)\geqslant0$ , 计算在这段时间内物体所经过的路程 s.

我们知道,对于等速直线运动,有公式

路程 $=$ 速度 $\times$ 时间.

但是,在现在讨论的问题中,速度不是常量而是随时间变化的变量,因此,所求路程s不能直接按等速直线运动的路程公式来计算.然而,物体运动的速度函数 $v=v(t)$ 是连续变化的,在很短一段时间内,速度的变化很小,近似于等速.因此,如果把时间间隔分小,在小段时间内,以等速运动代替变速运动,那么,就可算出部分路程的近似值;再求和,得到整个路程的近似值;最后,通过对时间间隔无限细分的极限过程,这时所有部分路程的近似值之和的极限,就是所求变速直线运动的路程的精确值.

具体计算步骤如下：

在时间间隔 $[T_1, T_2]$ 内任意插入若干个分点

$$
T _ {1} = t _ {0} <   t _ {1} <   t _ {2} <   \dots <   t _ {n - 1} <   t _ {n} = T _ {2},
$$

把 $[T_1, T_2]$ 分成 $n$ 个小时段

$$
\left[ t _ {0}, t _ {1} \right], \quad \left[ t _ {1}, t _ {2} \right], \quad \dots , \quad \left[ t _ {n - 1}, t _ {n} \right],
$$

各小时段时间的长依次为

$$
\Delta t _ {1} = t _ {1} - t _ {0}, \quad \Delta t _ {2} = t _ {2} - t _ {1}, \quad \dots , \quad \Delta t _ {n} = t _ {n} - t _ {n - 1}.
$$

相应地,在各段时间内物体经过的路程依次为

$$
\Delta s _ {1}, \quad \Delta s _ {2}, \quad \dots , \quad \Delta s _ {n}.
$$

在时间间隔 $[t_{i - 1}, t_i]$ 上任取一个时刻 $\tau_i$ ( $t_{i - 1} \leqslant \tau_i \leqslant t_i$ ), 以 $\tau_i$ 时的速度 $v(\tau_i)$ 来代替 $[t_{i - 1}, t_i]$ 上各个时刻的速度, 得到部分路程 $\Delta s_i$ 的近似值, 即

$$
\Delta s _ {i} \approx v (\tau_ {i}) \Delta t _ {i} (i = 1, 2, \dots , n).
$$

于是这 n 段部分路程的近似值之和就是所求变速直线运动路程 s 的近似值, 即

$$
s \approx v (\tau_ {1}) \Delta t _ {1} + v (\tau_ {2}) \Delta t _ {2} + \dots + v (\tau_ {n}) \Delta t _ {n} = \sum_ {i = 1} ^ {n} v (\tau_ {i}) \Delta t _ {i}.
$$

记 $\lambda=\max\left\{\Delta t_{1},\Delta t_{2},\cdots,\Delta t_{n}\right\}$ ，当 $\lambda\to0$ 时，取上述和式的极限，即得变速直线运动的路程

$$
s = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} v (\tau_ {i}) \Delta t _ {i}.
$$

# 二、定积分的定义

从上面两个例子可以看到:所要计算的量,即曲边梯形的面积 A 及变速直线运动的路程 s 的实际意义虽然不同,前者是几何量,后者是物理量,但是它们都由一个函数及其自变量的变化区间所决定,如:

曲边梯形的高度 $y=f(x)$ 及其底边上的点 x 的变化区间 $[a,b]$ ,

直线运动的速度 $v=v(t)$ 及时间 t 的变化区间 $[T_{1}, T_{2}]$ .

其次,计算这些量的方法与步骤都是相同的,并且它们都归结为具有相同结构的一种特定和的极限,如

面积 $A = \lim_{\lambda \to 0}\sum_{i = 1}^{n}f(\xi_i)\Delta x_i$ 

路程 $s=\lim_{\lambda\to0}\sum_{i=1}^{n}v(\tau_{i})\Delta t_{i}.$ 

抛开这些问题的具体意义,抓住它们在数量关系上共同的本质与特性加以概括,我们就可以抽象出下述定积分的定义:

定义 设函数 $f(x)$ 在 $[a, b]$ 上有界，在 $[a, b]$ 中任意插入若干个分点

$$
a = x _ {0} <   x _ {1} <   x _ {2} <   \dots <   x _ {n - 1} <   x _ {n} = b,
$$

把区间 $[a, b]$ 分成 $n$ 个小区间

$$
\left[ x _ {0}, x _ {1} \right], \quad \left[ x _ {1}, x _ {2} \right], \quad \dots , \quad \left[ x _ {n - 1}, x _ {n} \right],
$$

各个小区间的长度依次为

$$
\Delta x _ {1} = x _ {1} - x _ {0}, \quad \Delta x _ {2} = x _ {2} - x _ {1}, \quad \dots , \quad \Delta x _ {n} = x _ {n} - x _ {n - 1}.
$$

在每个小区间 $\left[x_{i-1},x_{i}\right]$ 上任取一点 $\xi_{i}\left(x_{i-1}\leqslant\xi_{i}\leqslant x_{i}\right)$ ，作函数值 $f(\xi_{i})$ 与小区间长度 $\Delta x_{i}$ 的乘积 $f(\xi_{i})\Delta x_{i}(i=1,2,\cdots,n)$ ，并作出和

$$
S = \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i}. \tag {1-1}
$$

记 $\lambda=\max\left\{\Delta x_{1},\Delta x_{2},\cdots,\Delta x_{n}\right\}$ ，如果当 $\lambda\to0$ 时，这和的极限总存在，且与闭区间 $[a,b]$ 的分法及点 $\xi_{i}$ 的取法无关，那么称这个极限 I 为函数 $f(x)$ 在区间 $[a,b]$ 上的定积分（简称积分），记作 $\int_{a}^{b}f(x)\mathrm{d}x$ ，即

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = I = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i}, \tag {1-2}
$$

其中 $f(x)$ 叫做被积函数, $f(x)\mathrm{d}x$ 叫做被积表达式, x 叫做积分变量, a 叫做积分下限, b 叫做积分上限, $[a,b]$ 叫做积分区间.

利用“ $\varepsilon-\delta$ ”的说法,上述定积分的定义可以表述如下:

设有常数 I，如果对于任意给定的正数 $\varepsilon$ ，总存在一个正数 $\delta$ ，使得对于区间 $[a, b]$ 的任何分法，不论 $\xi_{i}$ 在 $[x_{i-1}, x_{i}]$ 中怎样选取，只要 $\lambda = \max\{\Delta x_{1}, \Delta x_{2}, \cdots, \Delta x_{n}\} < \delta$ ，总有

$$
\left| \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} - I \right| <   \varepsilon
$$

成立,那么称 I 是 $f(x)$ 在区间 $[a,b]$ 上的定积分,记作 $\int_{a}^{b}f(x)\mathrm{d}x$ .

注意 当和式 $\sum_{i=1}^{n} f(\xi_i) \Delta x_i$ 的极限存在时, 其极限 $I$ 仅与被积函数 $f(x)$ 及积分区间 $[a, b]$ 有关. 如果既不改变被积函数 $f$ , 也不改变积分区间 $[a, b]$ , 而只把积分变量 $x$ 改写成其他字母, 例如 $t$ 或 $u$ , 那么, 这时和的极限 $I$ 不变, 也就是定积分的值不变, 即

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {b} f (t) \mathrm{d} t = \int_ {a} ^ {b} f (u) \mathrm{d} u.
$$

这就是说,定积分的值只与被积函数及积分区间有关,而与积分变量的记法无关.

和式 $\sum_{i=1}^{n} f(\xi_i) \Delta x_i$ 通常称为 $f(x)$ 的积分和. 如果 $f(x)$ 在 $[a, b]$ 上的定积分存在, 那么就说 $f(x)$ 在 $[a, b]$ 上可积.

对于定积分,有这样一个重要问题:函数 $f(x)$ 在 $[a,b]$ 上满足怎样的条件, $f(x)$ 在 $[a,b]$ 上一定可积?这个问题我们不作深入讨论,而只给出以下两个充分条件:

定理1 设 $f(x)$ 在区间 $[a, b]$ 上连续，则 $f(x)$ 在 $[a, b]$ 上可积.

定理2 设 $f(x)$ 在区间 $[a, b]$ 上有界，且只有有限个间断点，则 $f(x)$ 在 $[a, b]$ 上可积.

利用定积分的定义,前面所讨论的两个实际问题可以分别表述如下:

曲线 $y = f(x)$ ( $f(x) \geqslant 0$ )、 $x$ 轴及两条直线 $x = a, x = b$ 所围成的曲边梯形的面积 $A$ 等于函数 $f(x)$ 在区间 $[a, b]$ 上的定积分，即

$$
A = \int_ {a} ^ {b} f (x) \mathrm{d} x.
$$

物体以变速 $v = v(t)(v(t)\geqslant 0)$ 做直线运动，从时刻 $t = T_{1}$ 到时刻 $t = T_{2}$ ，这物体经过的路程 $s$ 等于函数 $v(t)$ 在区间 $[T_1,T_2]$ 上的定积分，即

$$
s = \int_ {T _ {1}} ^ {T _ {2}} v (t) \mathrm{d} t.
$$

下面讨论定积分的几何意义. 在 $[a, b]$ 上 $f(x) \geqslant 0$ 时, 我们已经知道, 定积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 表示由曲线 $y = f(x)$ , 两条直线 $x = a, x = b$ 与 $x$ 轴所围成的曲边梯形的面积; 在 $[a, b]$ 上 $f(x) \leqslant 0$ 时, 由曲线 $y = f(x)$ , 两条直线 $x = a, x = b$ 与 $x$ 轴所围成的曲边梯形位于 $x$ 轴的下方, 定积分

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x
$$

表示上述曲边梯形面积的负值；在 $[a, b]$ 上 $f(x)$ 既取得正值又取得负值时，函数 $f(x)$ 的图形某些部分在 $x$ 轴的上方，而其他部分在 $x$ 轴下方（图5-2），此时定积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 表示 $x$ 轴上方图形面积减去 $x$ 轴下方图形面积所得之差.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/3d82bf8e133de47d49bd6a823fbf1c8a703fa15fffeb2b417b60231da4a91b46.jpg)



图5-2


最后,举一个按定义计算定积分的例子.

例1 利用定义计算定积分 $\int_0^1 x^2\mathrm{d}x.$ 

解 因为被积函数 $f(x) = x^2$ 在积分区间[0,1]上连续，而连续函数是可积的，所以积分与区间[0,1]的分法及点 $\xi_i$ 的取法无关。因此，为了便于计算，不妨把区间[0,1]分成 $n$ 等份，分点为 $x_i = \frac{i}{n}, i = 1,2,\dots ,n - 1$ 。这样，每个小区间 $[x_{i-1},x_i]$ 的长度 $\Delta x_i = \frac{1}{n}$ ， $i = 1,2,\dots ,n$ 。取 $\xi_i = x_i, i = 1,2,\dots ,n$ 。于是，得和式

$$
\sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} = \sum_ {i = 1} ^ {n} \xi_ {i} ^ {2} \Delta x _ {i} = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} \Delta x _ {i} = \sum_ {i = 1} ^ {n} \left(\frac {i}{n}\right) ^ {2} \cdot \frac {1}{n} = \frac {1}{n ^ {3}} \sum_ {i = 1} ^ {n} i ^ {2}
$$

$$
= \frac {1}{n ^ {3}} \cdot \frac {1}{6} n (n + 1) (2 n + 1) ① = \frac {1}{6} \left(1 + \frac {1}{n}\right) \left(2 + \frac {1}{n}\right).
$$

当 $\lambda \to 0$ 即 $n\to \infty$ 时，取上式右端的极限.由定积分的定义，即得所要计算的积分为

$$
\int_ {0} ^ {1} x ^ {2} \mathrm{d} x = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} \xi_ {i} ^ {2} \Delta x _ {i} = \lim _ {n \rightarrow \infty} \frac {1}{6} \left(1 + \frac {1}{n}\right)\left(2 + \frac {1}{n}\right) = \frac {1}{3}.
$$

# 三、定积分的近似计算

从例 1 的计算过程中可以看到,对于任一确定的正整数 n,积分和

$$
\sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} = \frac {1}{6} \left(1 + \frac {1}{n}\right) \left(2 + \frac {1}{n}\right)
$$

都是定积分 $\int_0^1 x^2\mathrm{d}x$ 的近似值.当 $n$ 取不同值时，可得到定积分 $\int_0^1 x^2\mathrm{d}x$ 精度不同的近似值.一般说来， $n$ 取得越大，近似程度越好.

下面就一般情形,讨论定积分的近似计算问题.设 $f(x)$ 在 $[a,b]$ 上连续,这时定积分 $\int_{a}^{b}f(x)\mathrm{d}x$ 存在.如同例1,采取把区间 $[a,b]$ 等分的分法,即用分点 $a=x_{0},x_{1},x_{2},\cdots,x_{n}=b$ 将 $[a,b]$ 分成n个长度相等的小区间,每个小区间的长为

$$
\Delta x = \frac {b - a}{n},
$$

在小区间 $[x_{i - 1},x_i]$ 上，取 $\xi_{i} = x_{i - 1}$ ，应有

① 利用恒等式 $(n + 1)^{3} = n^{3} + 3n^{2} + 3n + 1$ ，得

$$
\left\{ \begin{array}{l} (n + 1) ^ {3} - n ^ {3} = 3 n ^ {2} + 3 n + 1, \\ n ^ {3} - (n - 1) ^ {3} = 3 (n - 1) ^ {2} + 3 (n - 1) + 1, \\ \dots \dots \\ 3 ^ {3} - 2 ^ {3} = 3 \times 2 ^ {2} + 3 \times 2 + 1, \\ 2 ^ {3} - 1 ^ {3} = 3 \times 1 ^ {2} + 3 \times 1 + 1. \end{array} \right.
$$

把这 n 个等式两端分别相加, 得

$$
(n + 1) ^ {3} - 1 = 3 \left(1 ^ {2} + 2 ^ {2} + \dots + n ^ {2}\right) + 3 (1 + 2 + \dots + n) + n.
$$

由于 $1+2+\cdots+n=\frac{1}{2}n(n+1)$ ，代入上式，得

$$
n ^ {3} + 3 n ^ {2} + 3 n = 3 \left(1 ^ {2} + 2 ^ {2} + \dots + n ^ {2}\right) + \frac {3}{2} n (n + 1) + n.
$$

整理后,得

$$
1 ^ {2} + 2 ^ {2} + \dots + n ^ {2} = \frac {1}{6} n (n + 1) (2 n + 1).
$$

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \lim _ {n \rightarrow \infty} \frac {b - a}{n} \sum_ {i = 1} ^ {n} f (x _ {i - 1}),
$$

从而对于任一确定的正整数 n, 有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x \approx \frac {b - a}{n} \sum_ {i = 1} ^ {n} f (x _ {i - 1}).
$$

记 $f(x_{i})=y_{i}\quad(i=0,1,2,\cdots,n)$ ，上式可记作

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x \approx \frac {b - a}{n} (y _ {0} + y _ {1} + \dots + y _ {n - 1}). \tag {1-3}
$$

如果取 $\xi_{i} = x_{i}$ ，则可得近似公式

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x \approx \frac {b - a}{n} (y _ {1} + y _ {2} + \dots + y _ {n}). \tag {1-4}
$$

以上求定积分近似值的方法称为矩形法,公式(1-3)、(1-4)称为矩形法公式.

矩形法的几何意义是:用窄条矩形的面积作为窄条曲边梯形面积的近似值.整体上用台阶形的面积作为曲边梯形面积的近似值.如图5-3所示.

求定积分近似值的方法,常用的还有梯形法和抛物线法(又称辛普森(Simpson)法),简单介绍如下:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/972029ad0ec66e2884ab3ee9ee68130ea5d9b56cd6b0bf12c6d182a62e7d1dd7.jpg)



图5-3


和矩形法一样, 将区间 $[a, b]$ n 等分. 设 $f(x_{i}) = y_{i}$ , 曲线 $y = f(x)$ 上的点 $(x_{i}, y_{i})$ 记作 $M_{i}$ $(i = 0, 1, 2, \cdots, n)$ .

梯形法的原理是: 将曲线 $y=f(x)$ 上的小弧段 $\widehat{M_{i-1}M_i}$ 用直线段 $\overline{M_{i-1}M_i}$ 代替, 也就是把窄条曲边梯形用窄条梯形代替 (图 5-4(a)), 由此得到定积分的近似值为

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) \mathrm{d} x \approx \frac {b - a}{n} \left(\frac {y _ {0} + y _ {1}}{2} + \frac {y _ {1} + y _ {2}}{2} + \dots + \frac {y _ {n - 1} + y _ {n}}{2}\right) \\ = \frac {b - a}{n} \left(\frac {y _ {0} + y _ {n}}{2} + y _ {1} + y _ {2} + \dots + y _ {n - 1}\right). \tag {1-5} \\ \end{array}
$$

显然,梯形法公式(1-5)所得近似值就是矩形法公式(1-3)和(1-4)所得两个近似值的平均值.

抛物线法的原理是: 将曲线 $y=f(x)$ 上的两个小弧段 $\widehat{M_{i-1}M_i}$ 和 $\widehat{M_iM_{i+1}}$ 合起来, 用过 $M_{i-1}, M_i, M_{i+1}$ 三点的抛物线 $y=px^2+qx+r (p\neq0)$ 代替(图 5-4(b)). 经推导可得, 以此抛物线弧段为曲边、以 $[x_{i-1}, x_{i+1}]$ 为底的曲边梯形面积为

$$
\frac {1}{6} (y _ {i - 1} + 4 y _ {i} + y _ {i + 1}) \cdot 2 \Delta x = \frac {b - a}{3 n} (y _ {i - 1} + 4 y _ {i} + y _ {i + 1}).
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/003766ee0944cca31d0ffb5bf558fb50dd81901d1d0752c2a9d15095aa64fa21.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/fd44ab3f3bb1a3313872745e01e6d1f3bee216cdd72e5267897899268024be11.jpg)



(b)



图5-4


取 n 为偶数, 得到定积分的近似值为

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) \mathrm{d} x \approx \frac {b - a}{3 n} \left[ \left(y _ {0} + 4 y _ {1} + y _ {2}\right) + \left(y _ {2} + 4 y _ {3} + y _ {4}\right) + \dots + \left(y _ {n - 2} + 4 y _ {n - 1} + y _ {n}\right) \right] \\ = \frac {b - a}{3 n} [ y _ {0} + y _ {n} + 4 (y _ {1} + y _ {3} + \dots + y _ {n - 1}) + 2 (y _ {2} + y _ {4} + \dots + y _ {n - 2}) ]. \tag {1-6} \\ \end{array}
$$

例 2 按梯形法公式(1-5)和抛物线法公式(1-6)计算定积分 $\int_{0}^{1}\frac{4}{1+x^{2}}dx$ 的近似值(取 n=10, 计算时取 5 位小数).

解 计算 $y_{i}$ 并列表：

<table><tr><td>i</td><td><eq>x_i</eq></td><td><eq>y_i</eq></td></tr><tr><td>0</td><td>0.0</td><td>4.000 00</td></tr><tr><td>1</td><td>0.1</td><td>3.960 40</td></tr><tr><td>2</td><td>0.2</td><td>3.846 15</td></tr><tr><td>3</td><td>0.3</td><td>3.669 72</td></tr><tr><td>4</td><td>0.4</td><td>3.448 28</td></tr><tr><td>5</td><td>0.5</td><td>3.200 00</td></tr><tr><td>6</td><td>0.6</td><td>2.941 18</td></tr><tr><td>7</td><td>0.7</td><td>2.684 56</td></tr><tr><td>8</td><td>0.8</td><td>2.439 02</td></tr><tr><td>9</td><td>0.9</td><td>2.209 94</td></tr><tr><td>10</td><td>1.0</td><td>2.000 00</td></tr></table>

按梯形法公式(1-5)求得近似值为

$$
S _ {1} = 3. 1 3 9 9 3,
$$

按抛物线法公式(1-6)求得近似值为

$$
S _ {2} = 3. 1 4 1 5 9.
$$

本例所给积分的精确值为

$$
\int_ {0} ^ {1} \frac {4}{1 + x ^ {2}} \mathrm{d} x = \pi = 3. 1 4 1 5 9 2 6 \dots ,
$$

用 $S_{2}$ 作为所给积分的近似值,误差小于 $10^{-5}$ .

计算定积分的近似值的方法很多,这里不再作介绍.随着计算机应用的普及,定积分的近似计算已变得更为方便,现在已有很多现成的数学软件可用于定积分的近似计算.

# 四、定积分的性质

为了以后计算及应用方便起见,对定积分作以下两点补充规定:

(1) 当 b=a 时， $\int_{a}^{a}f(x)\mathrm{d}x=0;$ 

(2) 当 a > b 时， $\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx,$ 

由上式可知,交换定积分的上、下限时,定积分的绝对值不变而符号相反.

下面讨论定积分的性质.下列各性质中积分上、下限的大小,如不特别指明,均不加限制,并假定各性质中所出现的被积函数在积分区间上都是可积的.

性质1 设 $\alpha$ 与 $\beta$ 均为常数, 则

$$
\int_ {a} ^ {b} [ \alpha f (x) + \beta g (x) ] d x = \alpha \int_ {a} ^ {b} f (x) d x + \beta \int_ {a} ^ {b} g (x) d x.
$$

证 $\int_{a}^{b}\left[\alpha f(x) + \beta g(x)\right]\mathrm{d}x = \lim_{\lambda \to 0}\sum_{i = 1}^{n}\left[\alpha f(\xi_i) + \beta g(\xi_i)\right]\Delta x_i$ 

$$
= \lim _ {\lambda \rightarrow 0} \alpha \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} + \lim _ {\lambda \rightarrow 0} \beta \sum_ {i = 1} ^ {n} g (\xi_ {i}) \Delta x _ {i}
$$

$$
= \alpha \int_ {a} ^ {b} f (x) \mathrm{d} x + \beta \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

性质 1 对于任意有限个函数的线性组合也是成立的.

性质2 设 $a < c < b$ ，则

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x.
$$

证 因为函数 $f(x)$ 在区间 $[a, b]$ 上可积，所以不论把 $[a, b]$ 怎样分，积分和的极限总是不变的。因此，在分区间时，可以使 $c$ 永远是个分点。那么， $[a, b]$ 上的积分和等于 $[a, c]$ 上的积分和加 $[c, b]$ 上的积分和，记为

$$
\sum_ {[ a, b ]} f (\xi_ {i}) \Delta x _ {i} = \sum_ {[ a, c ]} f (\xi_ {i}) \Delta x _ {i} + \sum_ {[ c, b ]} f (\xi_ {i}) \Delta x _ {i}.
$$

令 $\lambda\rightarrow0$ , 上式两端同时取极限, 即得

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x.
$$

这个性质表明定积分对于积分区间具有可加性.

按定积分的补充规定,我们有:不论 a, b, c 的相对位置如何,总有等式

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x
$$

成立.例如,当a<b<c时,由于

$$
\int_ {a} ^ {c} f (x) \mathrm{d} x = \int_ {a} ^ {b} f (x) \mathrm{d} x + \int_ {b} ^ {c} f (x) \mathrm{d} x,
$$

于是得

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {c} f (x) \mathrm{d} x - \int_ {b} ^ {c} f (x) \mathrm{d} x = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x.
$$

性质3 如果在区间 $[a, b]$ 上 $f(x) \equiv 1$ ，那么

$$
\int_ {a} ^ {b} 1 \mathrm{d} x = \int_ {a} ^ {b} \mathrm{d} x = b - a.
$$

这个性质的证明请读者自己完成.

性质4 如果在区间 $[a, b]$ 上 $f(x) \geqslant 0$ ，那么

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x \geqslant 0 \quad (a <   b).
$$

证 因为 $f(x)\geqslant 0$ ，所以

$$
f (\xi_ {i}) \geqslant 0 (i = 1, 2, \dots , n).
$$

又由于 $\Delta x_{i} \geqslant 0 (i = 1, 2, \cdots, n)$ ，因此

$$
\sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} \geqslant 0,
$$

令 $\lambda=\max\left\{\Delta x_{1},\Delta x_{2},\cdots,\Delta x_{n}\right\}\rightarrow0$ ,便得要证的不等式.

推论1 如果在区间 $[a, b]$ 上 $f(x) \leqslant g(x)$ , 那么.

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x \leqslant \int_ {a} ^ {b} g (x) \mathrm{d} x \quad (a <   b).
$$

证 因为 $g(x) - f(x)\geqslant 0$ ，由性质4得

$$
\int_ {a} ^ {b} \left[ g (x) - f (x) \right] \mathrm{d} x \geqslant 0.
$$

再利用性质 1, 便得要证的不等式.

推论2 $\left|\int_{a}^{b}f(x)\mathrm{d}x\right| \leqslant \int_{a}^{b}|f(x)|\mathrm{d}x (a < b).$ 

证 因为

$$
- | f (x) | \leqslant f (x) \leqslant | f (x) |,
$$

所以由推论 1 及性质 1 可得

$$
- \int_ {a} ^ {b} | f (x) | \mathrm{d} x \leqslant \int_ {a} ^ {b} f (x) \mathrm{d} x \leqslant \int_ {a} ^ {b} | f (x) | \mathrm{d} x,
$$

即

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x \right| \leqslant \int_ {a} ^ {b} | f (x) | \mathrm{d} x.
$$

性质5 设 $M$ 及 $m$ 分别是函数 $f(x)$ 在区间 $[a, b]$ 上的最大值及最小值，则

$$
m (b - a) \leqslant \int_ {a} ^ {b} f (x) \mathrm{d} x \leqslant M (b - a) \quad (a <   b).
$$

证 因为 $m \leqslant f(x) \leqslant M$ ，所以由性质4的推论1，得

$$
\int_ {a} ^ {b} m \mathrm{d} x \leqslant \int_ {a} ^ {b} f (x) \mathrm{d} x \leqslant \int_ {a} ^ {b} M \mathrm{d} x.
$$

再由性质 1 及性质 3, 即得所要证的不等式.

这个性质说明,由被积函数在积分区间上的最大值及最小值,可以估计积分值的大致范围.例如,定积分 $\int_{\frac{1}{2}}^{1}x^{4}\mathrm{d}x$ ,它的被积函数 $f(x)=x^{4}$ 在积分区间 $\left[\frac{1}{2},1\right]$ 上是单调增加的,于是有最小值 $m=\left(\frac{1}{2}\right)^{4}=\frac{1}{16}$ 、最大值 $M=(1)^{4}=1$ .由性质5,得

$$
\frac {1}{1 6} \times \left(1 - \frac {1}{2}\right) \leqslant \int_ {\frac {1}{2}} ^ {1} x ^ {4} \mathrm{d} x \leqslant 1 \times \left(1 - \frac {1}{2}\right),
$$

即

$$
\frac {1}{3 2} \leqslant \int_ {\frac {1}{2}} ^ {1} x ^ {4} \mathrm{d} x \leqslant \frac {1}{2}.
$$

性质6(定积分中值定理) 如果函数 $f(x)$ 在积分区间 $[a, b]$ 上连续, 那么在 $[a, b]$ 上至少存在一个点 $\xi$ , 使下式成立:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = f (\xi) (b - a) \quad (a \leqslant \xi \leqslant b).
$$

这个公式叫做积分中值公式①.

证 把性质 5 中的不等式各边除以 b-a, 得

$$
m \leqslant \frac {1}{b - a} \int_ {a} ^ {b} f (x) \mathrm{d} x \leqslant M.
$$

这表明,确定的数值 $\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x\in[m,M]$ .根据闭区间上连续函数的介值定理(第一章第十节定理3)的推论,在 $[a,b]$ 上至少存在一点 $\xi$ ,使得函数 $f(x)$ 在点 $\xi$ 处的值与这个确定的数值相等,即应有

$$
\frac {1}{b - a} \int_ {a} ^ {b} f (x) \mathrm{d} x = f (\xi) \quad (a \leqslant \xi \leqslant b).
$$

两端各乘 $b - a$ ，即得所要证的等式

显然,积分中值公式

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = f (\xi) (b - a) (\xi \text {在} a \text {与} b \text {之间})
$$

不论 $a < b$ 或 $a > b$ 都是成立的.

积分中值公式有如下的几何解释: 在区间 $[a, b]$ 上至少存在一点 $\xi$ ，使得以区间 $[a, b]$ 为底边、以曲线 $y = f(x)$ 为曲边的曲边梯形的面积等于同一底边而高为 $f(\xi)$ 的一个矩形的面积（图 5-5）.

按积分中值公式所得

$$
f (\xi) = \frac {1}{b - a} \int_ {a} ^ {b} f (x) \mathrm{d} x
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/d3f899d07e5650fc4c25c741f60f9a8793163a4e2191ca9761990e5b8424e97f.jpg)



图5-5


称为函数 $f(x)$ 在区间 $[a, b]$ 上的平均值. 例如按图5-5, $f(\xi)$ 可看作图中曲边梯形的平均高度. 又如物体以变速 $v(t)$ 做直线运动, 在时间区间 $[T_1, T_2]$ 上经过的路程为 $\int_{T_1}^{T_2} v(t) \mathrm{d}t$ , 因此,

$$
v (\xi) = \frac {1}{T _ {2} - T _ {1}} \int_ {T _ {1}} ^ {T _ {2}} v (t) \mathrm{d} t, \quad \xi \in [ T _ {1}, T _ {2} ]
$$

便是运动物体在 $[T_1, T_2]$ 这段时间内的平均速度.

# 习题5-1

*1. 利用定积分的定义计算由抛物线 $y = x^2 + 1$ 、两直线 $x = a, x = b (b > a)$ 及 $x$ 轴所围成的图形的面积.

*2. 利用定积分的定义计算下列积分：

(1) $\int_{a}^{b} x \, \mathrm{d}x (a < b)$ ; 

(2) $\int_{0}^{1}\mathrm{e}^{x}\mathrm{d}x.$ 

3. 利用定积分的几何意义,证明下列等式:

(1) $\int_0^1 2x\mathrm{d}x = 1;$ 

(2) $\int_0^1\sqrt{1 - x^2}\mathrm{d}x = \frac{\pi}{4};$ 

(3) $\int_{-\pi}^{\pi}\sin x\mathrm{d}x = 0;$ 

(4) $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\cos x\mathrm{d}x = 2\int_{0}^{\frac{\pi}{2}}\cos x\mathrm{d}x.$ 

4. 利用定积分的几何意义, 求下列积分:

(1) $\int_{0}^{t} x \, \mathrm{d}x (t > 0)$ ; 

(2) $\int_{-2}^{4}\left(\frac{x}{2} + 3\right)\mathrm{d}x;$ 

(3) $\int_{-1}^{2}|x|\mathrm{d}x;$ 

(4) $\int_{-3}^{3}\sqrt{9 - x^2}\mathrm{d}x.$ 

5. 设 $a < b$ ，问 $a, b$ 取什么值时，积分 $\int_{a}^{b} (x - x^2) \mathrm{d}x$ 取得最大值？

6. 试从定积分的几何意义,说明以下等式成立:

$$
\int_ {1} ^ {\mathrm{e}} \ln x \mathrm{d} x + \int_ {0} ^ {1} \mathrm{e} ^ {x} \mathrm{d} x = \mathrm{e}.
$$

7. 已知 $\ln 2 = \int_{0}^{1} \frac{1}{1 + x} \mathrm{d}x$ ，试用抛物线法公式(1-6)，求出 $\ln 2$ 的近似值（取 $n = 10$ ，计算时取4位小数）.

8. 设 $\int_{-1}^{1} 3f(x) \mathrm{d}x = 18, \int_{-1}^{3} f(x) \mathrm{d}x = 4, \int_{-1}^{3} g(x) \mathrm{d}x = 3.$ 求：

(1) $\int_{-1}^{1} f(x) \, \mathrm{d}x$ ; 

(2) $\int_{1}^{3} f(x) \, \mathrm{d}x$ ; 

(3) $\int_{3}^{-1} g(x) \, \mathrm{d}x$ ; 

(4) $\int_{-1}^{3}\frac{1}{5}[4f(x) + 3g(x)]\mathrm{d}x.$ 

9. 证明定积分的性质：

(1) $\int_{a}^{b} kf(x) \mathrm{d}x = k\int_{a}^{b} f(x) \mathrm{d}x$ ( $k$ 是常数);

(2) $\int_{a}^{b} 1 \cdot \mathrm{d}x = \int_{a}^{b} \mathrm{d}x = b - a.$ 

10. 估计下列各积分的值：

(1) $\int_{1}^{4}(x^{2} + 1)\mathrm{d}x;$ 

(2) $\int_{\frac{\pi}{4}}^{\frac{5}{4}\pi}(1 + \sin^2 x)\mathrm{d}x;$ 

(3) $\int_{\frac{1}{\sqrt{3}}}^{\sqrt{3}} x \arctan x \, \mathrm{d}x$ ; 

(4) $\int_{2}^{0}\mathrm{e}^{x^{2} - x}\mathrm{d}x.$ 

11. 设 $f(x)$ 在 $[0,1]$ 上连续，证明 $\int_0^1 f^2 (x)\mathrm{d}x\geqslant \left[\int_0^1 f(x)\mathrm{d}x\right]^2.$ 

12. 设 $f(x)$ 及 $g(x)$ 在 $[a, b]$ 上连续，证明：

(1) 若在 $[a,b]$ 上， $f(x)\geqslant0$ ，且 $f(x)\neq0$ ，则 $\int_{a}^{b}f(x)\mathrm{d}x>0;$ 

(2) 若在 $[a, b]$ 上， $f(x) \geqslant 0$ ，且 $\int_{a}^{b} f(x) \mathrm{d}x = 0$ ，则在 $[a, b]$ 上 $f(x) \equiv 0$ ；

(3) 若在 $[a, b]$ 上， $f(x) \leqslant g(x)$ ，且 $\int_{a}^{b} f(x) \mathrm{d}x = \int_{a}^{b} g(x) \mathrm{d}x$ ，则在 $[a, b]$ 上 $f(x) \equiv g(x)$ .

13. 根据定积分的性质及第 12 题的结论,说明下列各对积分中哪一个的值较大:

(1) $\int_{0}^{1}x^{2}dx$ 还是 $\int_{0}^{1}x^{3}dx?$ 

(2) $\int_{1}^{2}x^{2}dx$ 还是 $\int_{1}^{2}x^{3}dx?$ 

(3) $\int_{1}^{2}\ln x\mathrm{d}x$ 还是 $\int_1^2 (\ln x)^2\mathrm{d}x?$ 

(4) $\int_{0}^{1}x\mathrm{d}x$ 还是 $\int_{0}^{1}\ln(1+x)\mathrm{d}x?$ 

(5) $\int_{0}^{1}e^{x}dx$ 还是 $\int_{0}^{1}(1+x)dx?$ 

# 第二节 微积分基本公式

在第一节中有一个应用定积分的定义计算积分的例子.从这个例子我们看到,被积函数虽然是简单的幂函数 $f(x)=x^{2}$ ,但直接按定义来计算它的定积分已经不是很容易的事.如果被积函数是其他复杂的函数,其困难就更大了.因此,我们必须寻求计算定积分的新方法.

下面先从实际问题中寻找解决问题的线索.为此,我们对变速直线运动中遇到的位置函数 $s(t)$ 及速度函数 $v(t)$ 之间的联系作进一步的研究.

# 一、变速直线运动中位置函数与速度函数之间的联系

有一物体在一直线上运动.在这直线上取定原点、正方向及长度单位,使它成一数轴.设时刻 t 时物体所在位置为 $s(t)$ , 速度为 $v(t)$ (为了讨论方便起见, 可以设 $v(t) \geqslant 0$ ).

从第一节知道: 物体在时间间隔 $\left[T_{1}, T_{2}\right]$ 内经过的路程可以用速度函数 $v(t)$ 在 $\left[T_{1}, T_{2}\right]$ 上的定积分

$$
\int_ {T _ {1}} ^ {T _ {2}} v (t) \mathrm{d} t
$$

来表达;另一方面,这段路程又可以通过位置函数 $s(t)$ 在区间 $[T_{1},T_{2}]$ 上的增量

$$
s \left(T _ {2}\right) - s \left(T _ {1}\right)
$$

来表达.由此可见,位置函数 $s(t)$ 与速度函数 $v(t)$ 之间有如下关系:

$$
\int_ {T _ {1}} ^ {T _ {2}} v (t) \mathrm{d} t = s (T _ {2}) - s (T _ {1}). \tag {2-1}
$$

因为 $s'(t) = v(t)$ ，即位置函数 $s(t)$ 是速度函数 $v(t)$ 的原函数，所以关系式(2-1)表示，速度函数 $v(t)$ 在区间 $[T_1, T_2]$ 上的定积分等于 $v(t)$ 的原函数 $s(t)$ 在区间 $[T_1, T_2]$ 上的增量

$$
s \left(T _ {2}\right) - s \left(T _ {1}\right).
$$

上述从变速直线运动的路程这个特殊问题中得出来的关系,在一定条件下具有普遍性.事实上,我们将在第三目中证明,如果函数 $f(x)$ 在区间 $[a,b]$ 上连续,那么, $f(x)$ 在区间 $[a,b]$ 上的定积分就等于 $f(x)$ 的原函数(设为 $F(x)$ )在区间 $[a,b]$ 上的增量

$$
F (b) - F (a).
$$

# 二、积分上限的函数及其导数

设函数 $f(x)$ 在区间 $[a, b]$ 上可积，并且设 $x$ 为 $[a, b]$ 上的一点。我们来考察 $f(x)$ 在

部分区间 $[a, x]$ 上的定积分

$$
\int_ {a} ^ {x} f (x) \mathrm{d} x.
$$

首先,由于 $f(x)$ 在 $[a,x]$ 上仍旧可积,因此这个定积分存在.这里,x既表示定积分的上限,又表示积分变量.因为定积分与积分变量的记法无关,所以,为了明确起见,可以把积分变量改用其他符号,例如用t表示,则上面的定积分可以写成

$$
\int_ {a} ^ {x} f (t) \mathrm{d} t.
$$

如果上限 $x$ 在区间 $[a, b]$ 上任意变动, 那么对于每一个取定的 $x$ 值, 定积分有一个对应值, 所以它在 $[a, b]$ 上定义了一个函数, 记作 $\Phi(x)$ :

$$
\Phi (x) = \int_ {a} ^ {x} f (t) \mathrm{d} t \quad (a \leqslant x \leqslant b).
$$

这个函数 $\Phi(x)$ 具有下面定理 1 所指出的重要性质.

定理 1 如果函数 $f(x)$ 在区间 $[a, b]$ 上连续, 那么积分上限的函数

$$
\Phi (x) = \int_ {a} ^ {x} f (t) \mathrm{d} t
$$

在 $[a,b]$ 上可导，并且它的导数

$$
\Phi^ {\prime} (x) = \frac {\mathrm{d}}{\mathrm{d} x} \int_ {a} ^ {x} f (t) \mathrm{d} t = f (x) \quad (a \leqslant x \leqslant b). \tag {2-2}
$$

证 若 $x \in (a, b)$ , 设 $x$ 获得增量 $\Delta x$ , 其绝对值足够地小, 使得 $x + \Delta x \in (a, b)$ , 则 $\Phi(x)$ (图5-6, 图中 $\Delta x > 0$ ) 在 $x + \Delta x$ 处的函数值为

$$
\Phi (x + \Delta x) = \int_ {a} ^ {x + \Delta x} f (t) \mathrm{d} t.
$$

由此得函数的增量

$$
\begin{array}{l} \Delta \Phi = \Phi (x + \Delta x) - \Phi (x) \\ = \int_ {a} ^ {x + \Delta x} f (t) \mathrm{d} t - \int_ {a} ^ {x} f (t) \mathrm{d} t \\ = \int_ {a} ^ {x} f (t) \mathrm{d} t + \int_ {x} ^ {x + \Delta x} f (t) \mathrm{d} t - \int_ {a} ^ {x} f (t) \mathrm{d} t \\ = \int_ {x} ^ {x + \Delta x} f (t) \mathrm{d} t. \\ \end{array}
$$

再应用积分中值定理,即有等式

$$
\Delta \Phi = f (\xi) \Delta x,
$$

这里, $\xi$ 在x与 $x+\Delta x$ 之间.把上式两端各除以 $\Delta x$ ,得函数增量与自变量增量的比值

$$
\frac {\Delta \Phi}{\Delta x} = f (\xi).
$$

由于假设 $f(x)$ 在 $[a,b]$ 上连续，而 $\Delta x\to 0$ 时， $\xi \rightarrow x$ ，因此 $\lim_{\Delta x\to 0}f(\xi) = f(x)$ .于是，令$\Delta x \to 0$ 对上式两端取极限时, 左端的极限也应该存在且等于 $f(x)$ . 这就是说, 函数 $\Phi(x)$ 的导数存在, 并且

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/8d11385e271de88725cf88ecf68ecf8f4860825b53605e97981e0bbdd1796c9e.jpg)



图5-6


$$
\Phi^ {\prime} (x) = f (x).
$$

若 $x = a$ ，取 $\Delta x > 0$ ，则同理可证 $\Phi_{+}^{\prime}(a) = f(a)$ ；若 $x = b$ ，取 $\Delta x < 0$ ，则同理可证 $\Phi_{-}^{\prime}(b) = f(b)$ 

定理 1 证毕.

这个定理指出了一个重要结论:连续函数 $f(x)$ 取变上限x的定积分然后求导,其结果还原为 $f(x)$ 本身.联想到原函数的定义,就可以从定理1推知 $\Phi(x)$ 是连续函数 $f(x)$ 的一个原函数.因此,我们引出如下的原函数存在定理:

定理2 如果函数 $f(x)$ 在区间 $[a, b]$ 上连续，那么函数

$$
\Phi (x) = \int_ {a} ^ {x} f (t) \mathrm{d} t \tag {2-3}
$$

就是 $f(x)$ 在 $[a, b]$ 上的一个原函数.

这个定理的重要意义是:一方面肯定了连续函数的原函数是存在的,另一方面初步地揭示了积分学中的定积分与原函数之间的联系.因此,我们就有可能通过原函数来计算定积分.

# 三、牛顿-莱布尼茨公式

现在我们根据定理 2 来证明一个重要定理——微积分基本定理, 它给出了用原函数计算定积分的公式.

定理3（微积分基本定理）如果函数 $F(x)$ 是连续函数 $f(x)$ 在区间 $[a, b]$ 上的一个原函数，那么

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - F (a). \tag {2-4}
$$

证 已知函数 $F(x)$ 是连续函数 $f(x)$ 的一个原函数, 又根据定理2知道, 积分上限的函数

$$
\Phi (x) = \int_ {a} ^ {x} f (t) \mathrm{d} t
$$

也是 $f(x)$ 的一个原函数.于是这两个原函数之差 $F(x) - \Phi (x)$ 在 $[a,b]$ 上必定是某一个常数 $C$ （第四章第一节），即

$$
F (x) - \Phi (x) = C \quad (a \leqslant x \leqslant b). \tag {2-5}
$$

在上式中令 $x = a$ ，得 $F(a) - \Phi (a) = C.$ 又由 $\Phi (x)$ 的定义式(2-3)及上节定积分的补充规定(1)可知 $\Phi (a) = 0$ ，因此， $C = F(a)$ .以 $F(a)$ 代入(2-5)式中的 $C$ ，以 $\int_{a}^{x}f(t)\mathrm{d}t$ 代入(2-5)式中的 $\Phi (x)$ ，可得

$$
\int_ {a} ^ {x} f (t) \mathrm{d} t = F (x) - F (a).
$$

在上式中令 x=b，就得到所要证明的公式(2-4).

由上节定积分的补充规定(2)可知，(2-4)式对a>b的情形同样成立.

为了方便起见,以后把 $F(b)-F(a)$ 记成 $[F(x)]_{a}^{b}$ ,于是(2-4)式又可写成

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = [ F (x) ] _ {a} ^ {b}.
$$

公式(2-4)叫做牛顿(Newton)-莱布尼茨(Leibniz)公式①,也叫做微积分基本公式.这个公式进一步揭示了定积分与被积函数的原函数或不定积分之间的联系.它表明:一个连续函数在区间 $[a,b]$ 上的定积分等于它的任一个原函数在区间 $[a,b]$ 上的增量.这就给定积分提供了一个有效而简便的计算方法,大大简化了定积分的计算步骤.

下面我们举几个应用公式(2-4)来计算定积分的简单例子.

例1 计算第一节中的定积分 $\int_0^1 x^2\mathrm{d}x.$ 

解 由于 $\frac{x^3}{3}$ 是 $x^2$ 的一个原函数, 所以按牛顿-莱布尼茨公式, 有

$$
\int_ {0} ^ {1} x ^ {2} \mathrm{d} x = \left[ \frac {x ^ {3}}{3} \right] _ {0} ^ {1} = \frac {1 ^ {3}}{3} - \frac {0 ^ {3}}{3} = \frac {1}{3} - 0 = \frac {1}{3}.
$$

例2 计算 $\int_{-1}^{\sqrt{3}}\frac{\mathrm{d}x}{1 + x^2}.$ 

解 由于 $\arctan x$ 是 $\frac{1}{1 + x^2}$ 的一个原函数, 所以

$$
\int_ {- 1} ^ {\sqrt {3}} \frac {\mathrm{d} x}{1 + x ^ {2}} = [ \arctan x ] _ {- 1} ^ {\sqrt {3}} = \arctan \sqrt {3} - \arctan (- 1) = \frac {\pi}{3} - \left(- \frac {\pi}{4}\right) = \frac {7}{1 2} \pi .
$$

例3 计算 $\int_{-2}^{-1}\frac{\mathrm{d}x}{x}$ 

解 当 $x < 0$ 时, $\frac{1}{x}$ 的一个原函数是 $\ln |x|$ , 现在积分区间是 $[-2, -1]$ , 所以按牛顿-莱布尼茨公式, 有

$$
\int_ {- 2} ^ {- 1} \frac {\mathrm{d} x}{x} = [ \ln | x | ] _ {- 2} ^ {- 1} = \ln 1 - \ln 2 = - \ln 2.
$$

通过例 3, 我们应该特别注意: 公式(2-4)中的函数 $F(x)$ 必须是 $f(x)$ 在该积分区间 $[a, b]$ 上的原函数.

例4 计算正弦曲线 $y = \sin x$ 在 $[0, \pi]$ 上与 $x$ 轴所围成的平面图形（图5-7）的面积.

解 这图形是曲边梯形的一个特例. 它的面积

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/1cb56d1809ca75e89140dc0ea475b14cd172367604f7359139f0f810ab8deb36.jpg)



图5-7


$$
A = \int_ {0} ^ {\pi} \sin x \mathrm{d} x.
$$

由于- $\cos x$ 是 $\sin x$ 的一个原函数,所以

$$
A = \int_ {0} ^ {\pi} \sin x \mathrm{d} x = [ - \cos x ] _ {0} ^ {\pi} = - (- 1) - (- 1) = 2.
$$

例 5 汽车以 36 km/h 速度沿直线行驶, 到某处需要减速停车. 设汽车以等加速度 $a = -5 \, m/s^{2}$ 刹车. 问从开始刹车到停车, 汽车驶过了多少距离?

解 首先要算出从开始刹车到停车经过的时间. 设开始刹车的时刻为 t=0, 此时汽车速度

$$
v _ {0} = 3 6 \mathrm{km/h} = \frac {3 6 \times 1 0 0 0}{3 6 0 0} \mathrm{m/s} = 1 0 \mathrm{m/s}.
$$

刹车后汽车减速行驶,其速度为

$$
v (t) = v _ {0} + a t = 1 0 - 5 t.
$$

当汽车停住时,速度 $v(t)=0$ , 故从

$$
v (t) = 1 0 - 5 t = 0
$$

解得

$$
t = \frac {1 0}{5} = 2 (\mathrm{s}).
$$

于是在这段时间内,汽车所驶过的距离为

$$
s = \int_ {0} ^ {2} v (t) \mathrm{d} t = \int_ {0} ^ {2} (1 0 - 5 t) \mathrm{d} t = \left[ 1 0 t - 5 \times \frac {t ^ {2}}{2} \right] _ {0} ^ {2} = 1 0 (\mathrm{m}),
$$

即在刹车后,汽车需驶过 $10 \, m$ 才能停住.

例6 证明积分中值定理: 若函数 $f(x)$ 在闭区间 $[a, b]$ 上连续, 则在开区间 $(a, b)$ 内至少存在一点 $\xi$ , 使

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = f (\xi) (b - a) (a <   \xi <   b).
$$

证 因 $f(x)$ 连续, 故它的原函数存在, 设为 $F(x)$ , 即设在 $[a, b]$ 上 $F'(x) = f(x)$ . 根据牛顿-莱布尼茨公式, 有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - F (a).
$$

显然函数 $F(x)$ 在区间 $[a, b]$ 上满足微分中值定理的条件, 因此按微分中值定理, 在开区间 $(a, b)$ 内至少存在一点 $\xi$ , 使

$$
F (b) - F (a) = F ^ {\prime} (\xi) (b - a), \quad \xi \in (a, b),
$$

故

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = f (\xi) (b - a), \quad \xi \in (a, b).
$$

本例的结论是上一节所述积分中值定理的改进.从本例的证明中不难看出积分中值定理与微分中值定理的联系.

下面再举几个应用公式(2-2)的例子.

例7 设 $f(x)$ 在 $[0, +\infty)$ 内连续且 $f(x) > 0$ . 证明函数

$$
F (x) = \frac {\int_ {0} ^ {x} t f (t) \mathrm{d} t}{\int_ {0} ^ {x} f (t) \mathrm{d} t}
$$

在 $(0,+\infty)$ 内为单调增加函数.

证 由公式(2-2)，得

$$
\frac {\mathrm{d}}{\mathrm{d} x} \int_ {0} ^ {x} t f (t) \mathrm{d} t = x f (x), \quad \frac {\mathrm{d}}{\mathrm{d} x} \int_ {0} ^ {x} f (t) \mathrm{d} t = f (x).
$$

故

$$
F ^ {\prime} (x) = \frac {x f (x) \int_ {0} ^ {x} f (t) \mathrm{d} t - f (x) \int_ {0} ^ {x} t f (t) \mathrm{d} t}{\left[ \int_ {0} ^ {x} f (t) \mathrm{d} t \right] ^ {2}} = \frac {f (x) \int_ {0} ^ {x} (x - t) f (t) \mathrm{d} t}{\left[ \int_ {0} ^ {x} f (t) \mathrm{d} t \right] ^ {2}}.
$$

按假设, 当 0 < t < x 时 $f(t) > 0$ , $(x - t)f(t) > 0$ , 按例 6 所述积分中值定理可知

$$
\int_ {0} ^ {x} f (t) \mathrm{d} t > 0, \quad \int_ {0} ^ {x} (x - t) f (t) \mathrm{d} t > 0,
$$

所以 $F'(x)>0$ (x>0)，从而 $F(x)$ 在 $(0,+\infty)$ 内为单调增加函数.

例8 求 $\lim_{x\to 0}\frac{\int_{\cos x}^{1}\mathrm{e}^{-t^2}\mathrm{d}t}{x^2}.$ 

解 易知这是一个 $\frac{0}{0}$ 型的未定式, 我们利用洛必达法则来计算. 分子可写成

$$
- \int_ {1} ^ {\cos x} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t,
$$

它是以 $\cos x$ 为上限的积分,作为 x 的函数可看成是以 $u=\cos x$ 为中间变量的复合函数,故由公式(2-2)有

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/00d590efe40095ea7e5e4018e4fbc352b93a92c77a7828ef468fc86800a5ca95.jpg)


释疑解难

5-1 

$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} x} \int_ {\cos x} ^ {1} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t = - \frac {\mathrm{d}}{\mathrm{d} x} \int_ {1} ^ {\cos x} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t = - \frac {\mathrm{d}}{\mathrm{d} u} \int_ {1} ^ {u} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t \Bigg | _ {u = \cos x} \cdot (\cos x) ^ {\prime} \\ = - \mathrm{e} ^ {- \cos^ {2} x} \cdot (- \sin x) = \sin x \mathrm{e} ^ {- \cos^ {2} x}. \\ \frac {\mathrm{d}}{\mathrm{d} x} \int_ {\cos x} ^ {1} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t = - \frac {\mathrm{d}}{\mathrm{d} x} \int_ {1} ^ {\cos x} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t = - \frac {\mathrm{d}}{\mathrm{d} u} \int_ {1} ^ {u} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t \Bigg | _ {u = \cos x} \cdot (\cos x) ^ {\prime} \\ \end{array}
$$

$$
\lim _ {x \rightarrow 0} \frac {\int_ {\cos x} ^ {1} e ^ {- t ^ {2}} d t}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\sin x e ^ {- \cos^ {2} x}}{2 x} = \frac {1}{2 e}.
$$

因此

# 习题5-2

1. 试求函数 $y = \int_0^x \sin t \, \mathrm{d}t$ 当 $x = 0$ 及 $x = \frac{\pi}{4}$ 时的导数.

2. 求由参数表达式 $x = \int_{0}^{t} \sin u du, y = \int_{0}^{t} \cos u du$ 所确定的函数对 x 的导数 $\frac{dy}{dx}$ .

3. 求由 $\int_{0}^{y} e^{t} dt + \int_{0}^{x} \cos t dt = 0$ 所确定的隐函数对 x 的导数 $\frac{dy}{dx}$ .

4. 当 $x$ 为何值时, 函数 $I(x) = \int_{0}^{x} t \mathrm{e}^{-t^2} \mathrm{d}t$ 有极值?

5. 计算下列各导数：

(1) $\frac{\mathrm{d}}{\mathrm{d}x}\int_{0}^{x^{2}}\sqrt{1 + t^{2}}\mathrm{d}t;$ 

(2) $\frac{\mathrm{d}}{\mathrm{d}x}\int_{x^2}^{x^3}\frac{\mathrm{d}t}{\sqrt{1 + t^4}};$ 

(3) $\frac{\mathrm{d}}{\mathrm{d}x}\int_{\sin x}^{\cos x}\cos (\pi t^2)\mathrm{d}t.$ 

6. 证明 $f(x) = \int_{1}^{x} \sqrt{1 + t^3} \, \mathrm{d}t$ 在 $[-1, +\infty)$ 上是单调增加函数，并求 $(f^{-1})'(0)$ .

7. 设 $f(x) = \int_{0}^{x} \left( \int_{\sin t}^{1} \sqrt{1 + u^4} \, \mathrm{d}u \right) \, \mathrm{d}t$ ，求 $f''\left( \frac{\pi}{3} \right)$ .

8. 设 $f(x)$ 具有三阶连续导数, $y = f(x)$ 的图形如图5-8所示. 问下列积分中的哪一个积分值为负?

(A) $\int_{-1}^{3} f(x) \, \mathrm{d}x$ 

(B) $\int_{-1}^{3} f'(x) \, \mathrm{d}x$ 

(C) $\int_{-1}^{3}f''(x)\mathrm{d}x$ 

(D) $\int_{-1}^{3} f'''(x) \, \mathrm{d}x$ 

9. 计算下列各定积分：

(1) $\int_0^a (3x^2 - x + 1)\mathrm{d}x;$ 

(2) $\int_{1}^{2}\left(x^{2} + \frac{1}{x^{4}}\right)\mathrm{d}x;$ 

(3) $\int_{4}^{9}\sqrt{x}(1 + \sqrt{x})\mathrm{d}x;$ 

(4) $\int_{\frac{1}{\sqrt{3}}}^{\sqrt{3}} \frac{\mathrm{d}x}{1 + x^2}$ ; 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/586d9401cfec14e29d6db0f454fcf6afb89a4ebd9aeb8b63009c2bb1166cca21.jpg)



图5-8


(5) $\int_{-\frac{1}{2}}^{\frac{1}{2}}\frac{\mathrm{d}x}{\sqrt{1 - x^2}};$ 

(6) $\int_{0}^{\sqrt{3}a}\frac{\mathrm{d}x}{a^{2} + x^{2}};$ 

(7) $\int_0^1\frac{\mathrm{d}x}{\sqrt{4 - x^2}};$ 

(8) $\int_{-1}^{0} \frac{3x^4 + 3x^2 + 1}{x^2 + 1} \, \mathrm{d}x$ ; 

(9) $\int_{-e - 1}^{-2}\frac{\mathrm{d}x}{1 + x};$ 

(10) $\int_{0}^{\frac{\pi}{4}}\tan^{2}\theta \mathrm{d}\theta ;$ 

(11) $\int_{0}^{2\pi}|\sin x|\mathrm{d}x;$ 

(12) $\int_0^2 f(x)\mathrm{d}x$ ，其中 $f(x) = \left\{ \begin{array}{ll}x + 1, & x\leqslant 1,\\ \frac{1}{2} x^2, & x > 1. \end{array} \right.$ 

10. 设 $k \in \mathbb{N}_{+}$ . 试证下列各题：

(1) $\int_{-\pi}^{\pi}\cos kx\mathrm{d}x = 0;$ 

(2) $\int_{-\pi}^{\pi}\sin kx\mathrm{d}x = 0;$ 

(3) $\int_{-\pi}^{\pi}\cos^{2}kx\mathrm{d}x = \pi ;$ 

(4) $\int_{-\pi}^{\pi}\sin^{2}kx\mathrm{d}x = \pi .$ 

11. 设 $k, l \in \mathbb{N}_{+}$ , 且 $k \neq l$ . 证明:

(1) $\int_{-\pi}^{\pi}\cos kx\sin lxdx = 0;$ 

(2) $\int_{-\pi}^{\pi}\cos kx\cos lxdx = 0;$ 

(3) $\int_{-\pi}^{\pi}\sin kx\sin lxdx=0.$ 

12. 求下列极限：

(1) $\lim_{x\to 0}\frac{\int_0^x\cos t^2\mathrm{d}t}{x};$ 

(2) $\lim_{x\to 0}\frac{\left(\int_0^x\mathrm{e}^{t^2}\mathrm{d}t\right)^2}{\int_0^x t\mathrm{e}^{2t^2}\mathrm{d}t}.$ 

13. 设

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2}, & x \in [ 0, 1), \\ x, & x \in [ 1, 2 ]. \end{array} \right.
$$

求 $\Phi(x) = \int_{0}^{x} f(t) \, \mathrm{d}t$ 在 $[0,2]$ 上的表达式，并讨论 $\Phi(x)$ 在 $(0,2)$ 内的连续性.

14. 设

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{2} \sin x, & 0 \leqslant x \leqslant \pi , \\ 0, & x <   0 \text {或} x > \pi . \end{array} \right.
$$

求 $\Phi(x)=\int_{0}^{x}f(t)\mathrm{d}t$ 在 $(-∞,+∞)$ 内的表达式.

15. 设 $f(x)$ 在 $[a, b]$ 上连续，在 $(a, b)$ 内可导且 $f'(x) \leqslant 0$ ，

$$
F (x) = \frac {1}{x - a} \int_ {a} ^ {x} f (t) \mathrm{d} t.
$$

证明在 $(a,b)$ 内有 $F'(x)\leqslant0.$ 

16. 以下积分上限的函数：

$$
S (x) = \int_ {0} ^ {x} \sin \frac {\pi t ^ {2}}{2} \mathrm{d} t, x \in (- \infty , + \infty)
$$

称为菲涅耳(Fresnel)积分,在光学中有重要应用.

(1) 证明: $S(x)$ 为奇函数;

(2) 求出 $S(x)$ 的极小值点.

17. 设 $f(x)$ 在 $[0, +\infty)$ 内连续，且 $\lim_{x \to +\infty} f(x) = 1$ 。证明函数

$$
\gamma = \mathrm{e} ^ {- x} \int_ {0} ^ {x} \mathrm{e} ^ {t} f (t) \mathrm{d} t
$$

满足方程 $\frac{dy}{dx}+y=f(x)$ ，并求 $\lim_{x\to+\infty}y(x)$ .

# 第三节 定积分的换元法和分部积分法

由上节结果知道,计算定积分 $\int_{a}^{b}f(x)\mathrm{d}x$ 的简便方法是把它转化为求 $f(x)$ 的原函数的增量.在第四章中,我们知道用换元积分法和分部积分法可以求出一些函数的原函数.因此,在一定条件下,可以用换元积分法和分部积分法来计算定积分.下面就来讨论定积分的这两种计算方法.

# 一、定积分的换元法

为了说明如何用换元法来计算定积分,先证明下面的定理:

定理 设函数 $f(x)$ 在区间 $[a, b]$ 上连续，函数 $x = \varphi(t)$ 满足条件：

(1) $\varphi(\alpha)=a,\varphi(\beta)=b;$ 

(2) $\varphi(t)$ 在 $[\alpha, \beta]$ （或 $[\beta, \alpha]$ ）上具有连续导数，且其值域 $R_{\varphi} = [a, b]$ ①，则有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {\alpha} ^ {\beta} f [ \varphi (t) ] \varphi^ {\prime} (t) \mathrm{d} t. \tag {3-1}
$$

公式(3-1)叫做定积分的换元公式.

证 由假设可以知道,上式两端的被积函数都是连续的,因此不仅上式两端的定积分都存在,而且由上节的定理2知道,被积函数的原函数也都存在.所以,(3-1)式两端的定积分都可应用牛顿-莱布尼茨公式.假设 $F(x)$ 是 $f(x)$ 的一个原函数,则

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - F (a).
$$

另一方面, 记 $\Phi(t) = F[\varphi(t)]$ , 它是由 $F(x)$ 与 $x = \varphi(t)$ 复合而成的函数. 由复合函数求导法则, 得

$$
\Phi^ {\prime} (t) = \frac {\mathrm{d} F}{\mathrm{d} x} \cdot \frac {\mathrm{d} x}{\mathrm{d} t} = f (x) \varphi^ {\prime} (t) = f [ \varphi (t) ] \varphi^ {\prime} (t).
$$

这表明 $\Phi(t)$ 是 $f[\varphi(t)]\varphi'(t)$ 的一个原函数. 因此有

$$
\int_ {\alpha} ^ {\beta} f [ \varphi (t) ] \varphi^ {\prime} (t) \mathrm{d} t = \Phi (\beta) - \Phi (\alpha).
$$

又由 $\Phi(t) = F[\varphi(t)]$ 及 $\varphi(\alpha) = a, \varphi(\beta) = b$ 可知

$$
\Phi (\beta) - \Phi (\alpha) = F [ \varphi (\beta) ] - F [ \varphi (\alpha) ] = F (b) - F (a).
$$

所以

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - F (a) = \Phi (\beta) - \Phi (\alpha) = \int_ {\alpha} ^ {\beta} f [ \varphi (t) ] \varphi^ {\prime} (t) \mathrm{d} t.
$$

这就证明了换元公式.

在定积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 中的 $\mathrm{d}x$ , 本来是整个定积分记号中不可分割的一部分, 但由上述定理可知, 在一定条件下, 它确实可以作为微分记号来对待. 这就是说, 应用换元公式时, 如果把 $\int_{a}^{b} f(x) \mathrm{d}x$ 中的 $x$ 换成 $\varphi(t)$ , 那么 $\mathrm{d}x$ 就换成 $\varphi'(t) \mathrm{d}t$ , 这正好是 $x = \varphi(t)$ 的微分 $\mathrm{d}x$ .

应用换元公式时有两点值得注意: (1) 用 $x = \varphi(t)$ 把原来变量 $x$ 代换成新变量 $t$ 时, 积分限也要换成相应于新变量 $t$ 的积分限; (2) 求出 $f[\varphi(t)]\varphi'(t)$ 的一个原函数 $\Phi(t)$ 后, 不必像计算不定积分那样再要把 $\Phi(t)$ 变换成原来变量 $x$ 的函数, 而只要把新变量 $t$ 的上、下限分别代入 $\Phi(t)$ 中然后相减就行了.

例1 计算 $\int_0^a\sqrt{a^2 - x^2}\mathrm{d}x (a > 0).$ 

解 设 $x = a\sin t$ ，则 $\mathrm{d}x = a\cos t\mathrm{d}t$ 

当 $x = 0$ 时，取 $t = 0$ ；当 $x = a$ 时，取 $t = \frac{\pi}{2}$ .

于是

$$
\begin{array}{l} \int_ {0} ^ {a} \sqrt {a ^ {2} - x ^ {2}} \mathrm{d} x = a ^ {2} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} t \mathrm{d} t = \frac {a ^ {2}}{2} \int_ {0} ^ {\frac {\pi}{2}} (1 + \cos 2 t) \mathrm{d} t \\ = \frac {a ^ {2}}{2} \left[ t + \frac {1}{2} \sin 2 t \right] _ {0} ^ {\frac {\pi}{2}} = \frac {\pi a ^ {2}}{4}. \\ \end{array}
$$

换元公式也可反过来使用.为使用方便起见,把换元公式中左、右两端对调位置,同时把t改记为x,而x改记为t,得

$$
\int_ {a} ^ {b} f [ \varphi (x) ] \varphi^ {\prime} (x) \mathrm{d} x = \int_ {\alpha} ^ {\beta} f (t) \mathrm{d} t.
$$

这样,我们可用 $t=\varphi(x)$ 来引入新变量 t, 而 $\alpha=\varphi(a)$ , $\beta=\varphi(b)$ .

例2 计算 $\int_0^{\frac{\pi}{2}}\cos^5 x\sin x\mathrm{d}x.$ 

解 设 $t = \cos x$ ，则 $\mathrm{dt} = -\sin x\mathrm{dx}$ ，且

当 $x = 0$ 时， $t = 1$ ；当 $x = \frac{\pi}{2}$ 时， $t = 0$ .

于是

$$
\int_ {0} ^ {\frac {\pi}{2}} \cos^ {5} x \sin x \mathrm{d} x = - \int_ {1} ^ {0} t ^ {5} \mathrm{d} t = \int_ {0} ^ {1} t ^ {5} \mathrm{d} t = \left[ \frac {t ^ {6}}{6} \right] _ {0} ^ {1} = \frac {1}{6}.
$$

在例 2 中, 如果我们不明显地写出新变量 t, 那么定积分的上、下限就不要变更. 现在用这种记法写出计算过程如下:

$$
\int_ {0} ^ {\frac {\pi}{2}} \cos^ {5} x \sin x \mathrm{d} x = - \int_ {0} ^ {\frac {\pi}{2}} \cos^ {5} x \mathrm{d} (\cos x) = - \left[ \frac {\cos^ {6} x}{6} \right] _ {0} ^ {\frac {\pi}{2}} = - \left(0 - \frac {1}{6}\right) = \frac {1}{6}.
$$

例3 计算 $\int_0^\pi \sqrt{\sin^3 x - \sin^5 x} \, \mathrm{d}x.$ 

解 由于 $\sqrt{\sin^3 x - \sin^5 x} = \sqrt{\sin^3 x(1 - \sin^2 x)} = \sin^{\frac{3}{2}}x\cdot |\cos x|$ ，在 $\left[0,\frac{\pi}{2}\right]$ 上， $|\cos x| = \cos x$ ；在 $\left[\frac{\pi}{2},\pi \right]$ 上， $|\cos x| = -\cos x$ ，所以

$$
\begin{array}{l} \int_ {0} ^ {\pi} \sqrt {\sin^ {3} x - \sin^ {5} x} d x = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {\frac {3}{2}} x \cos x d x + \int_ {\frac {\pi}{2}} ^ {\pi} \sin^ {\frac {3}{2}} x (- \cos x) d x \\ = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {\frac {3}{2}} x \mathrm{d} (\sin x) - \int_ {\frac {\pi}{2}} ^ {\pi} \sin^ {\frac {3}{2}} x \mathrm{d} (\sin x) \\ = \left[ \frac {2}{5} \sin^ {\frac {5}{2}} x \right] _ {0} ^ {\frac {\pi}{2}} - \left[ \frac {2}{5} \sin^ {\frac {5}{2}} x \right] _ {\frac {\pi}{2}} ^ {\pi} \\ = \frac {2}{5} - \left(- \frac {2}{5}\right) = \frac {4}{5}. \\ \end{array}
$$

注意 如果忽略 $\cos x$ 在 $\left[\frac{\pi}{2},\pi\right]$ 上非正，而按 $\sqrt{\sin^3 x - \sin^5 x} = \sin^{\frac{3}{2}}x\cos x$ 计算，将导致错误.

例4 计算 $\int_0^4\frac{x + 2}{\sqrt{2x + 1}}\mathrm{d}x.$ 

解 设 $\sqrt{2x + 1} = t$ ，则 $x = \frac{t^2 - 1}{2}, \mathrm{d}x = t\mathrm{d}t$ ，且

当 x=0 时, t=1; 当 x=4 时, t=3.

于是

$$
\begin{array}{l} \int_ {0} ^ {4} \frac {x + 2}{\sqrt {2 x + 1}} \mathrm{d} x = \int_ {1} ^ {3} \frac {\frac {t ^ {2} - 1}{2} + 2}{t} t \mathrm{d} t = \frac {1}{2} \int_ {1} ^ {3} (t ^ {2} + 3) \mathrm{d} t \\ = \frac {1}{2} \left[ \frac {t ^ {3}}{3} + 3 t \right] _ {1} ^ {3} = \frac {1}{2} \left[ \left(\frac {2 7}{3} + 9\right) - \left(\frac {1}{3} + 3\right) \right] = \frac {2 2}{3}. \\ \end{array}
$$

例5 证明：

(1) 若 $f(x)$ 在 $[-a, a]$ 上连续且为偶函数，则

$$
\int_ {- a} ^ {a} f (x) \mathrm{d} x = 2 \int_ {0} ^ {a} f (x) \mathrm{d} x;
$$

(2) 若 $f(x)$ 在 $[-a, a]$ 上连续且为奇函数，则

$$
\int_ {- a} ^ {a} f (x) \mathrm{d} x = 0.
$$

证 因为

$$
\int_ {- a} ^ {a} f (x) \mathrm{d} x = \int_ {- a} ^ {0} f (x) \mathrm{d} x + \int_ {0} ^ {a} f (x) \mathrm{d} x,
$$

对积分 $\int_{-a}^{0}f(x)\mathrm{d}x$ 作代换 $x = -t$ ，则得

$$
\int_ {- a} ^ {0} f (x) \mathrm{d} x = - \int_ {a} ^ {0} f (- t) \mathrm{d} t = \int_ {0} ^ {a} f (- t) \mathrm{d} t = \int_ {0} ^ {a} f (- x) \mathrm{d} x,
$$

于是

$$
\int_ {- a} ^ {a} f (x) \mathrm{d} x = \int_ {0} ^ {a} f (- x) \mathrm{d} x + \int_ {0} ^ {a} f (x) \mathrm{d} x = \int_ {0} ^ {a} [ f (x) + f (- x) ] \mathrm{d} x.
$$

(1) 若 $f(x)$ 为偶函数, 则

$$
f (x) + f (- x) = 2 f (x),
$$

从而

$$
\int_ {- a} ^ {a} f (x) \mathrm{d} x = 2 \int_ {0} ^ {a} f (x) \mathrm{d} x.
$$

(2) 若 $f(x)$ 为奇函数, 则

$$
f (x) + f (- x) = 0,
$$

从而

$$
\int_ {- a} ^ {a} f (x) \mathrm{d} x = 0.
$$

利用例 5 的结论, 常可简化计算偶函数、奇函数在对称于原点的区间上的定积分.

例 6 设 $f(x)$ 在 $[0,1]$ 上连续, 证明:

(1) $\int_{0}^{\frac{\pi}{2}} f(\sin x) \, \mathrm{d}x = \int_{0}^{\frac{\pi}{2}} f(\cos x) \, \mathrm{d}x$ ; 

(2) $\int_0^\pi xf(\sin x)\mathrm{d}x = \frac{\pi}{2}\int_0^\pi f(\sin x)\mathrm{d}x$ ，由此计算

$$
\int_ {0} ^ {\pi} \frac {x \sin x}{1 + \cos^ {2} x} d x.
$$

证（1）设 $x = \frac{\pi}{2} - t$ ，则 $\mathrm{dx} = -\mathrm{dt}$ ，且

当 $x = 0$ 时， $t = \frac{\pi}{2}$ ；当 $x = \frac{\pi}{2}$ 时， $t = 0$ .

于是

$$
\int_ {0} ^ {\frac {\pi}{2}} f (\sin x) \mathrm{d} x = - \int_ {\frac {\pi}{2}} ^ {0} f \left[ \sin \left(\frac {\pi}{2} - t\right) \right] \mathrm{d} t = \int_ {0} ^ {\frac {\pi}{2}} f (\cos t) \mathrm{d} t = \int_ {0} ^ {\frac {\pi}{2}} f (\cos x) \mathrm{d} x.
$$

(2) 设 $x = \pi - t$ ，则 dx = -dt，且

当 $x = 0$ 时， $t = \pi$ ；当 $x = \pi$ 时， $t = 0$ .

于是

$$
\begin{array}{l} \int_ {0} ^ {\pi} x f (\sin x) \mathrm{d} x = - \int_ {\pi} ^ {0} (\pi - t) f [ \sin (\pi - t) ] \mathrm{d} t = \int_ {0} ^ {\pi} (\pi - t) f (\sin t) \mathrm{d} t \\ = \pi \int_ {0} ^ {\pi} f (\sin t) \mathrm{d} t - \int_ {0} ^ {\pi} t f (\sin t) \mathrm{d} t = \pi \int_ {0} ^ {\pi} f (\sin x) \mathrm{d} x - \int_ {0} ^ {\pi} x f (\sin x) \mathrm{d} x, \\ \end{array}
$$

所以

$$
\int_ {0} ^ {\pi} x f (\sin x) \mathrm{d} x = \frac {\pi}{2} \int_ {0} ^ {\pi} f (\sin x) \mathrm{d} x.
$$

利用上述结论,即得

$$
\begin{array}{l} \int_ {0} ^ {\pi} \frac {x \sin x}{1 + \cos^ {2} x} \mathrm{d} x = \frac {\pi}{2} \int_ {0} ^ {\pi} \frac {\sin x}{1 + \cos^ {2} x} \mathrm{d} x = - \frac {\pi}{2} \int_ {0} ^ {\pi} \frac {\mathrm{d} (\cos x)}{1 + \cos^ {2} x} \\ = - \frac {\pi}{2} [ \arctan (\cos x) ] _ {0} ^ {\pi} = - \frac {\pi}{2} \left(- \frac {\pi}{4} - \frac {\pi}{4}\right) = \frac {\pi^ {2}}{4}. \\ \end{array}
$$

例 7 设 $f(x)$ 是连续的周期函数, 周期为 T, 证明:

(1) $\int_{a}^{a + T}f(x)\mathrm{d}x = \int_{0}^{T}f(x)\mathrm{d}x;$ 

(2) $\int_{a}^{a + nT}f(x)\mathrm{d}x = n\int_{0}^{T}f(x)\mathrm{d}x (n\in \mathbf{N})$ ，由此计算

$$
\int_ {0} ^ {n \pi} \sqrt {1 + \sin 2 x} d x.
$$

证 (1) 记 $\Phi(a) = \int_{a}^{a + T} f(x) \, \mathrm{d}x$ ，则

$$
\Phi^ {\prime} (a) = \left[ \int_ {0} ^ {a + T} f (x) \mathrm{d} x - \int_ {0} ^ {a} f (x) \mathrm{d} x \right] ^ {\prime} = f (a + T) - f (a) = 0,
$$

知 $\Phi(a)$ 与 $a$ 无关, 因此 $\Phi(a)=\Phi(0)$ , 即

$$
\int_ {a} ^ {a + T} f (x) \mathrm{d} x = \int_ {0} ^ {T} f (x) \mathrm{d} x.
$$

(2) $\int_{a}^{a + nT}f(x)\mathrm{d}x = \sum_{k = 0}^{n - 1}\int_{a + kT}^{a + kT + T}f(x)\mathrm{d}x,$ 由（1）知

$$
\int_ {a + k T} ^ {a + k T + T} f (x) \mathrm{d} x = \int_ {0} ^ {T} f (x) \mathrm{d} x,
$$

因此

$$
\int_ {a} ^ {a + n T} f (x) \mathrm{d} x = n \int_ {0} ^ {T} f (x) \mathrm{d} x.
$$

由于 $\sqrt{1 + \sin 2x}$ 是以 $\pi$ 为周期的周期函数，利用上述结论，有

$$
\begin{array}{l} \int_ {0} ^ {n \pi} \sqrt {1 + \sin 2 x} \mathrm{d} x = n \int_ {0} ^ {\pi} \sqrt {1 + \sin 2 x} \mathrm{d} x = n \int_ {0} ^ {\pi} | \sin x + \cos x | \mathrm{d} x \\ = \sqrt {2} n \int_ {0} ^ {\pi} \left| \sin \left(x + \frac {\pi}{4}\right) \right| d x = \sqrt {2} n \int_ {\frac {\pi}{4}} ^ {\frac {5 \pi}{4}} | \sin t | d t \\ = \sqrt {2} n \int_ {0} ^ {\pi} | \sin t | \mathrm{d} t = \sqrt {2} n \int_ {0} ^ {\pi} \sin t \mathrm{d} t = 2 \sqrt {2} n. \\ \end{array}
$$

例8 计算 $\int_0^3\frac{x^2}{(x^2 - 3x + 3)^2}\mathrm{d}x.$ 

解 因 $x^{2} - 3x + 3 = \left(x - \frac{3}{2}\right)^{2} + \frac{3}{4}$ , 令 $x - \frac{3}{2} = \frac{\sqrt{3}}{2}\tan u\left(|u| < \frac{\pi}{2}\right)$ , 则

$$
\left(x ^ {2} - 3 x + 3\right) ^ {2} = \left(\frac {3}{4} \sec^ {2} u\right) ^ {2} = \frac {9}{1 6} \sec^ {4} u, \mathrm{d} x = \frac {\sqrt {3}}{2} \sec^ {2} u \mathrm{d} u.
$$

当 $x = 0$ 时， $u = -\frac{\pi}{3}$ ； $x = 3$ 时， $u = \frac{\pi}{3}$ .

于是

$$
\begin{array}{l} \int_ {0} ^ {3} \frac {x ^ {2}}{\left(x ^ {2} - 3 x + 3\right) ^ {2}} \mathrm{d} x = \int_ {- \frac {\pi}{3}} ^ {\frac {\pi}{3}} \left(\frac {3}{4} \tan^ {2} u + \frac {3 \sqrt {3}}{2} \tan u + \frac {9}{4}\right) \cdot \frac {1 6}{9} \cdot \frac {\sqrt {3}}{2} \cos^ {2} u \mathrm{d} u \\ = \frac {8}{3 \sqrt {3}} \cdot 2 \int_ {0} ^ {\frac {\pi}{3}} \left(\frac {3}{4} \tan^ {2} u + \frac {9}{4}\right) \cos^ {2} u d u \\ = \frac {4}{\sqrt {3}} \int_ {0} ^ {\frac {\pi}{3}} (\sin^ {2} u + 3 \cos^ {2} u) d u = \frac {4}{\sqrt {3}} \int_ {0} ^ {\frac {\pi}{3}} (2 + \cos 2 u) d u \\ = \frac {4}{\sqrt {3}} \left[ 2 u + \frac {1}{2} \sin 2 u \right] _ {0} ^ {\frac {\pi}{3}} = \frac {8 \pi}{3 \sqrt {3}} + 1. \\ \end{array}
$$

例9 设函数

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{1 + \cos x}, & - \pi <   x <   0, \\ x \mathrm{e} ^ {- x ^ {2}}, & x \geqslant 0, \end{array} \right.
$$

计算 $\int_{1}^{4}f(x - 2)\mathrm{d}x.$ 

解 设 $x - 2 = t$ ，则 $\mathrm{dx} = \mathrm{dt}$ ，且

当 $x = 1$ 时， $t = -1$ ；当 $x = 4$ 时， $t = 2$ .

于是

$$
\begin{array}{l} \int_ {1} ^ {4} f (x - 2) \mathrm{d} x = \int_ {- 1} ^ {2} f (t) \mathrm{d} t = \int_ {- 1} ^ {0} \frac {\mathrm{d} t}{1 + \cos t} + \int_ {0} ^ {2} t \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t \\ = \left[ \tan \frac {t}{2} \right] _ {- 1} ^ {0} - \left[ \frac {1}{2} e ^ {- t ^ {2}} \right] _ {0} ^ {2} = \tan \frac {1}{2} - \frac {1}{2} e ^ {- 4} + \frac {1}{2}. \\ \end{array}
$$

# 二、定积分的分部积分法

依据不定积分的分部积分法, 若 $u(x)$ , $v(x)$ 在 $[a, b]$ 上具有连续导数, 则

$$
\begin{array}{l} \int_ {a} ^ {b} u (x) v ^ {\prime} (x) \mathrm{d} x = \left[ \int u (x) v ^ {\prime} (x) \mathrm{d} x \right] _ {a} ^ {b} = \left[ u (x) v (x) - \int v (x) u ^ {\prime} (x) \mathrm{d} x \right] _ {a} ^ {b} \\ = [ u (x) v (x) ] _ {a} ^ {b} - \int_ {a} ^ {b} v (x) u ^ {\prime} (x) \mathrm{d} x, \tag {3-2} \\ \end{array}
$$

简记作

$$
\int_ {a} ^ {b} u v ^ {\prime} \mathrm{d} x = [ u v ] _ {a} ^ {b} - \int_ {a} ^ {b} v u ^ {\prime} \mathrm{d} x,
$$

或

$$
\int_ {a} ^ {b} u \mathrm{d} v = [ u v ] _ {a} ^ {b} - \int_ {a} ^ {b} v \mathrm{d} u.
$$

公式(3-2)叫做定积分的分部积分公式.公式表明原函数已经积出的部分可以先用上、下限代入.

例10 计算 $\int_0^{\frac{1}{2}}\arcsin x\mathrm{d}x.$ 

解 $\int_0^{\frac{1}{2}}\arcsin x\mathrm{d}x = [x\arcsin x]_{0}^{\frac{1}{2}} - \int_0^{\frac{1}{2}}\frac{x}{\sqrt{1 - x^2}}\mathrm{d}x$ 

$$
= \frac {1}{2} \cdot \frac {\pi}{6} + \left[ \sqrt {1 - x ^ {2}} \right] _ {0} ^ {\frac {1}{2}} = \frac {\pi}{1 2} + \frac {\sqrt {3}}{2} - 1.
$$

例11 计算 $\int_0^1\mathrm{e}^{\sqrt{x}}\mathrm{d}x.$ 

解 先用换元法. 令 $\sqrt{x} = t$ , 则 $x = t^2, \mathrm{d}x = 2t\mathrm{d}t$ , 且

当 x=0 时, t=0; 当 x=1 时, t=1.

于是

$$
\begin{array}{l} \int_ {0} ^ {1} \mathrm{e} ^ {\sqrt {x}} \mathrm{d} x = 2 \int_ {0} ^ {1} t \mathrm{e} ^ {t} \mathrm{d} t = 2 \int_ {0} ^ {1} t \mathrm{d} (\mathrm{e} ^ {t}) = 2 \left(\left[ t \mathrm{e} ^ {t} \right] _ {0} ^ {1} - \int_ {0} ^ {1} \mathrm{e} ^ {t} \mathrm{d} t\right) \\ = 2 \left(\mathrm{e} - \left[ \mathrm{e} ^ {t} \right] _ {0} ^ {1}\right) = 2 \left[ \mathrm{e} - (\dot {\mathrm{e}} - 1) \right] = 2. \\ \end{array}
$$

例 12 证明定积分公式(见附录Ⅳ积分表公式 147):

$$
I _ {n} = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} x \mathrm{d} x \left(= \int_ {0} ^ {\frac {\pi}{2}} \cos^ {n} x \mathrm{d} x\right)
$$

$$
= \left\{ \begin{array}{l l} \frac {n - 1}{n} \cdot \frac {n - 3}{n - 2} \cdot \dots \cdot \frac {3}{4} \cdot \frac {1}{2} \cdot \frac {\pi}{2}, & n \text {为正偶数,} \\ \frac {n - 1}{n} \cdot \frac {n - 3}{n - 2} \cdot \dots \cdot \frac {4}{5} \cdot \frac {2}{3}, & n \text {为大于1的正奇数.} \end{array} \right.
$$

证 $I_{n} = -\int_{0}^{\frac{\pi}{2}}\sin^{n - 1}x\mathrm{d}(\cos x)$ 

$$
= \left[ - \cos x \sin^ {n - 1} x \right] _ {0} ^ {\frac {\pi}{2}} + (n - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 2} x \cos^ {2} x d x.
$$

右端第一项等于零;将第二项里的 $\cos^{2}x$ 写成 $1-\sin^{2}x$ , 并把积分分成两个, 得

$$
I _ {n} = (n - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 2} x \mathrm{d} x - (n - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} x \mathrm{d} x = (n - 1) I _ {n - 2} - (n - 1) I _ {n},
$$

由此得

$$
I _ {n} = \frac {n - 1}{n} I _ {n - 2}.
$$

这个等式叫做积分 $I_{n}$ 关于下标的递推公式.

如果把 $n$ 换成 $n - 2$ ，那么得

$$
I _ {n - 2} = \frac {n - 3}{n - 2} I _ {n - 4}.
$$

同样地依次进行下去,直到 $I_{n}$ 的下标递减到0或1为止.于是,

$$
I _ {2 m} = \frac {2 m - 1}{2 m} \cdot \frac {2 m - 3}{2 m - 2} \cdot \dots \cdot \frac {5}{6} \cdot \frac {3}{4} \cdot \frac {1}{2} I _ {0},
$$

$$
I _ {2 m + 1} = \frac {2 m}{2 m + 1} \cdot \frac {2 m - 2}{2 m - 1} \cdot \dots \cdot \frac {6}{7} \cdot \frac {4}{5} \cdot \frac {2}{3} I _ {1} (m = 1, 2, \dots),
$$

而

$$
I _ {0} = \int_ {0} ^ {\frac {\pi}{2}} \mathrm{d} x = \frac {\pi}{2}, I _ {1} = \int_ {0} ^ {\frac {\pi}{2}} \sin x \mathrm{d} x = 1,
$$

因此

$$
I _ {2 m} = \frac {2 m - 1}{2 m} \cdot \frac {2 m - 3}{2 m - 2} \cdot \dots \cdot \frac {5}{6} \cdot \frac {3}{4} \cdot \frac {1}{2} \cdot \frac {\pi}{2},
$$

$$
I _ {2 m + 1} = \frac {2 m}{2 m + 1} \cdot \frac {2 m - 2}{2 m - 1} \cdot \dots \cdot \frac {6}{7} \cdot \frac {4}{5} \cdot \frac {2}{3} (m = 1, 2, \dots).
$$

至于定积分 $\int_0^{\frac{\pi}{2}}\cos^n x\mathrm{d}x$ 与 $\int_0^{\frac{\pi}{2}}\sin^n x\mathrm{d}x$ 相等，由本节例6(1）即可知道，证毕.

# 习题5-3

1. 计算下列定积分：

(1) $\int_{\frac{\pi}{3}}^{\pi}\sin \left(x + \frac{\pi}{3}\right)\mathrm{d}x;$ 

(2) $\int_{-2}^{1}\frac{\mathrm{d}x}{(11 + 5x)^3};$ 

(3) $\int_{0}^{\frac{\pi}{2}}\sin \varphi \cos^{3}\varphi \mathrm{d}\varphi ;$ 

(4) $\int_{0}^{\pi}(1 - \sin^{3}\theta)\mathrm{d}\theta ;$ 

(5) $\int_{\frac{\pi}{6}}^{\frac{\pi}{2}}\cos^{2}u\mathrm{d}u;$ 

(6) $\int_{0}^{\sqrt{2}}\sqrt{2 - x^{2}}\mathrm{d}x;$ 

(7) $\int_{-\sqrt{2}}^{\sqrt{2}}\sqrt{8 - 2y^2}\mathrm{d}y;$ 

(8) $\int_{\frac{1}{\sqrt{2}}}^{1}\frac{\sqrt{1-x^{2}}}{x^{2}}dx;$ 

(9) $\int_{0}^{a}x^{2}\sqrt{a^{2}-x^{2}}dx(a>0);$ 

(10) $\int_{1}^{\sqrt{3}}\frac{\mathrm{d}x}{x^{2}\sqrt{1 + x^{2}}};$ 

(11) $\int_{-1}^{1}\frac{xdx}{\sqrt{5-4x}};$ 

(12) $\int_{1}^{4}\frac{dx}{1+\sqrt{x}};$ 

(13) $\int_{\frac{3}{4}}^{1}\frac{\mathrm{d}x}{\sqrt{1 - x} - 1};$ 

(14) $\int_0^{\sqrt{2} a}\frac{x\mathrm{d}x}{\sqrt{3a^2 - x^2}} (a > 0)$ 

(15) $\int_{0}^{1} t \mathrm{e}^{-\frac{t^2}{2}} \, \mathrm{d}t$ ; 

(16) $\int_{1}^{\mathrm{e}^{2}}\frac{\mathrm{d}x}{x\sqrt{1 + \ln x}};$ 

(17) $\int_{-2}^{0} \frac{(x + 2) \mathrm{d}x}{x^2 + 2x + 2}$ ; 

(18) $\int_0^2\frac{x\mathrm{d}x}{(x^2 - 2x + 2)^2};$ 

(19) $\int_{-\pi}^{\pi} x^{4} \sin x \, \mathrm{d}x$ ; 

(20) $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} 4\cos^{4}\theta \mathrm{d}\theta$ ; 

(21) $\int_{-\frac{1}{2}}^{\frac{1}{2}}\frac{(\arcsin x)^2}{\sqrt{1 - x^2}}\mathrm{d}x;$ 

(22) $\int_{-5}^{5}\frac{x^3\sin^2x}{x^4 + 2x^2 + 1}\mathrm{d}x;$ 

(23) $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\cos x\cos 2x\mathrm{d}x;$ 

(24) $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{\cos x - \cos^3 x}\mathrm{d}x;$ 

(25) $\int_0^\pi \sqrt{1 + \cos 2x} \, \mathrm{d}x$ ; 

(26) $\int_{0}^{2\pi}|\sin (x + 1)|\mathrm{d}x.$ 

2. 设 $f(x)$ 在 $[a, b]$ 上连续，证明：

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {b} f (a + b - x) \mathrm{d} x.
$$

3. 证明： $\int_{x}^{1}\frac{\mathrm{d}t}{1 + t^2} = \int_{1}^{\frac{1}{x}}\frac{\mathrm{d}t}{1 + t^2}$ （ $x > 0$ ）.

4. 证明： $\int_0^1 x^m (1 - x)^n\mathrm{d}x = \int_0^1 x^n (1 - x)^m\mathrm{d}x$ （ $m,n\in \mathbf{N}$ 

5. 设 $f(x)$ 在 $[0,1]$ 上连续， $n \in \mathbf{Z}$ ，证明：

$$
\int_ {\frac {n}{2} \pi} ^ {\frac {n + 1}{2} \pi} f (\mid \sin x \mid) \mathrm{d} x = \int_ {\frac {n}{2} \pi} ^ {\frac {n + 1}{2} \pi} f (\mid \cos x \mid) \mathrm{d} x = \int_ {0} ^ {\frac {\pi}{2}} f (\sin x) \mathrm{d} x.
$$

6. 若 $f(t)$ 是连续的奇函数, 证明 $\int_{0}^{x}f(t)\mathrm{d}t$ 是偶函数; 若 $f(t)$ 是连续的偶函数, 证明 $\int_{0}^{x}f(t)\mathrm{d}t$ 是奇函数.

7. 设 $x = \varphi(y)$ 是单调函数 $y = x\mathrm{e}^{x^2}$ 的反函数, 求 $\int_0^e \varphi(y)\mathrm{d}y$ .

8. 计算下列定积分：

(1) $\int_{0}^{1} x \mathrm{e}^{-x} \mathrm{d}x$ ; 

(2) $\int_{1}^{\mathrm{e}} x \ln x \, \mathrm{d}x$ ; 

(3) $\int_{0}^{\frac{2\pi}{\omega}}t\sin\omega tdt(\omega$ 为常数 $)$ ;

(4) $\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \frac{x}{\sin^2 x} \, \mathrm{d}x$ ; 

(5) $\int_{1}^{4}\frac{\ln x}{\sqrt{x}}\mathrm{d}x;$ 

(6) $\int_{0}^{1} x \arctan x \, \mathrm{d}x$ ; 

(7) $\int_{0}^{\frac{\pi}{2}}\mathrm{e}^{2x}\cos x\mathrm{d}x;$ 

(8) $\int_{1}^{2} x \log_{2} x \, \mathrm{d}x$ ; 

(9) $\int_{0}^{\pi}(x\sin x)^{2}\mathrm{d}x;$ 

(10) $\int_{1}^{\infty}\sin (\ln x)\mathrm{d}x;$ 

(11) $\int_{\frac{1}{e}}^{e}|\ln x|\mathrm{d}x;$ 

(12) $\int_0^1 (1 - x^2)^{\frac{m}{2}}\mathrm{d}x$ ( $m \in \mathbf{N}_+$ ); 

(13) $J_{m} = \int_{0}^{\pi}x\sin^{m}x\mathrm{d}x (m\in \mathbf{N}_{+}).$ 

# 第四节 反常积分

在一些实际问题中,常会遇到积分区间为无穷区间,或者被积函数为无界函数的积分,它们已经不属于前面所说的定积分了.因此,我们对定积分作如下两种推广,从而形成反常积分的概念.

# 一、无穷限的反常积分

设函数 $f(x)$ 在区间 $[a, +\infty)$ 上连续，任取 $t > a$ ，作定积分 $\int_{a}^{t} f(x) \, \mathrm{d}x$ ，再求极限：

$$
\lim _ {t \to + \infty} \int_ {a} ^ {t} f (x)   \mathrm{d} x, \tag {4-1}
$$

这个对变上限定积分的算式(4-1)称为函数 $f(x)$ 在无穷区间 $[a,+\infty)$ 上的反常积分，记为 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ ，即

$$
\int_ {a} ^ {+ \infty} f (x) \mathrm{d} x = \lim _ {t \rightarrow + \infty} \int_ {a} ^ {t} f (x) \mathrm{d} x, \tag {$4-1^{\prime$}}
$$

根据算式(4-1)的结果是否存在,可引入反常积分 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 收敛与发散的定义如下:

定义1（1）设函数 $f(x)$ 在区间 $[a, +\infty)$ 上连续，如果极限(4-1)存在，那么称反常积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 收敛，并称此极限为该反常积分的值；如果极限(4-1)不存在，那么称反常积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 发散.

类似地,设函数 $f(x)$ 在区间 $(-∞,b]$ 上连续,任取t<b,算式

$$
\lim _ {t \rightarrow - \infty} \int_ {t} ^ {b} f (x) \mathrm{d} x \tag {4-2}
$$

称为函数 $f(x)$ 在无穷区间 $(- \infty, b]$ 上的反常积分，记为 $\int_{-\infty}^{b} f(x) \mathrm{d}x$ ，即

$$
\int_ {- \infty} ^ {b} f (x) \mathrm{d} x = \lim _ {t \rightarrow - \infty} \int_ {t} ^ {b} f (x) \mathrm{d} x. \tag {$4-2^{\prime$}}
$$

于是有

（2）设函数 $f(x)$ 在区间 $(- \infty, b]$ 上连续，如果极限(4-2)存在，那么称反常积分 $\int_{-\infty}^{b} f(x) \mathrm{d}x$ 收敛，并称此极限为该反常积分的值；如果极限(4-2)不存在，那么称反常积分 $\int_{-\infty}^{b} f(x) \mathrm{d}x$ 发散.

设函数 $f(x)$ 在区间 $(- \infty, + \infty)$ 上连续，反常积分 $\int_{-\infty}^{0} f(x) \mathrm{d}x$ 与反常积分 $\int_{0}^{+\infty} f(x) \mathrm{d}x$ 之和称为函数 $f(x)$ 在无穷区间 $(- \infty, + \infty)$ 上的反常积分，记为 $\int_{-\infty}^{+\infty} f(x) \mathrm{d}x$ 即

$$
\int_ {- \infty} ^ {+ \infty} f (x) \mathrm{d} x = \int_ {- \infty} ^ {0} f (x) \mathrm{d} x + \int_ {0} ^ {+ \infty} f (x) \mathrm{d} x. \tag {4-3}
$$

（3）设函数 $f(x)$ 在区间 $(-\infty, +\infty)$ 上连续，如果反常积分 $\int_{-\infty}^{0} f(x) \mathrm{d}x$ 与反常积分 $\int_{0}^{+\infty} f(x) \mathrm{d}x$ 均收敛，那么称反常积分 $\int_{-\infty}^{+\infty} f(x) \mathrm{d}x$ 收敛，并称反常积分 $\int_{-\infty}^{0} f(x) \mathrm{d}x$ 的值与反常积分 $\int_{0}^{+\infty} f(x) \mathrm{d}x$ 的值之和为反常积分 $\int_{-\infty}^{+\infty} f(x) \mathrm{d}x$ 的值，否则就称反常积分 $\int_{-\infty}^{+\infty} f(x) \mathrm{d}x$ 发散.

上述反常积分统称为无穷限的反常积分.

由上述定义及牛顿-莱布尼茨公式,可得如下结果:

设 $F(x)$ 为 $f(x)$ 在 $[a, +\infty)$ 上的一个原函数，若 $\lim_{x \to +\infty} F(x)$ 存在，则反常积分

$$
\int_ {a} ^ {+ \infty} f (x) \mathrm{d} x = \lim _ {x \rightarrow + \infty} F (x) - F (a);
$$

若 $\lim_{x\to +\infty}F(x)$ 不存在，则反常积分 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 发散.

若记 $F(+\infty) = \lim_{x\to +\infty}F(x),[F(x)]_a^{+\infty} = F(+\infty) - F(a)$ ，则当 $F(+\infty)$ 存在时，

$$
\int_ {a} ^ {+ \infty} f (x) \mathrm{d} x = [ F (x) ] _ {a} ^ {+ \infty};
$$

当 $F(+\infty)$ 不存在时，反常积分 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 发散.

类似地，若在 $(- \infty, b]$ 上 $F'(x) = f(x)$ ，则当 $F(-\infty)$ 存在时，

$$
\int_ {- \infty} ^ {b} f (x) \mathrm{d} x = [ F (x) ] _ {- \infty} ^ {b};
$$

当 $F(-\infty)$ 不存在时，反常积分 $\int_{-\infty}^{b}f(x)\mathrm{d}x$ 发散.

若在 $(- \infty, + \infty)$ 内 $F^{\prime}(x) = f(x)$ ，则当 $F(-\infty)$ 与 $F(+\infty)$ 都存在时，

$$
\int_ {- \infty} ^ {+ \infty} f (x) \mathrm{d} x = [ F (x) ] _ {- \infty} ^ {+ \infty};
$$

当 $F(-\infty)$ 与 $F(+\infty)$ 有一个不存在时，反常积分 $\int_{-\infty}^{+\infty}f(x)\mathrm{d}x$ 发散.

例1 计算反常积分 $\int_{-\infty}^{+\infty}\frac{\mathrm{d}x}{1 + x^2}.$ 

解 $\int_{-\infty}^{+\infty}\frac{\mathrm{d}x}{1 + x^2} = [\arctan x]_{-\infty}^{+\infty} = \lim_{x\to +\infty}\arctan x - \lim_{x\to -\infty}\arctan x = \frac{\pi}{2} -\left(-\frac{\pi}{2}\right) = \pi .$ 

这个反常积分值的几何意义是: 当 $a \to -\infty$ , $b \to +\infty$ 时, 虽然图 5-9 中阴影部分向左、右无限延伸, 但其面积却有极限值 $\pi$ . 简单地说, 它是位于曲线 $y = \frac{1}{1 + x^{2}}$ 的下方, x 轴上方的图形面积.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/c68c3c4c06e0dbeab8aef6e87562a04f9079f3b1f04df09a5c2f1c320a9c2c6e.jpg)



图5-9


例 2 计算反常积分 $\int_{0}^{+\infty} t e^{-pt} dt$ ，其中 p 是常数，且 p > 0.

解 $\int_0^{+\infty}t\mathrm{e}^{-pt}\mathrm{d}t = \left[\int t\mathrm{e}^{-pt}\mathrm{d}t\right]_0^{+\infty} = \left[-\frac{1}{p}\int t\mathrm{d}\left(\mathrm{e}^{-pt}\right)\right]_0^{+\infty}$ 

$$
= \left[ - \frac {t}{p} \mathrm{e} ^ {- p t} + \frac {1}{p} \int \mathrm{e} ^ {- p t} \mathrm{d} t \right] _ {0} ^ {+ \infty} = \left[ - \frac {t}{p} \mathrm{e} ^ {- p t} \right] _ {0} ^ {+ \infty} - \left[ \frac {1}{p ^ {2}} \mathrm{e} ^ {- p t} \right] _ {0} ^ {+ \infty}
$$

$$
= - \frac {1}{p} \lim _ {t \rightarrow + \infty} t e ^ {- p t} - 0 - \frac {1}{p ^ {2}} (0 - 1) = \frac {1}{p ^ {2}}.
$$

[Non-Text] 

释疑解难

5-2 

注意,上式中的极限 $\lim_{t\to+\infty}te^{-pt}$ 是未定式,可用洛必达法则确定.

例3 证明反常积分 $\int_{a}^{+\infty}\frac{\mathrm{d}x}{x^p}$ （ $a > 0$ )当 $p > 1$ 时收敛，当 $p\leqslant 1$ 时发散.

证 当 $p = 1$ 时，

$$
\int_ {a} ^ {+ \infty} \frac {\mathrm{d} x}{x ^ {p}} = \int_ {a} ^ {+ \infty} \frac {\mathrm{d} x}{x} = [ \ln x ] _ {a} ^ {+ \infty} = + \infty ,
$$

当 $p \neq 1$ 时，

$$
\int_ {a} ^ {+ \infty} \frac {\mathrm{d} x}{x ^ {p}} = \left[ \frac {x ^ {1 - p}}{1 - p} \right] _ {a} ^ {+ \infty} = \left\{ \begin{array}{l l} + \infty , & p <   1, \\ \frac {a ^ {1 - p}}{p - 1}, & p > 1. \end{array} \right.
$$

因此，当 $p > 1$ 时，这反常积分收敛，其值为 $\frac{a^{1 - p}}{p - 1}$ ；当 $p \leqslant 1$ 时，这反常积分发散.

# 二、无界函数的反常积分

现在我们把定积分推广到被积函数为无界函数的情形.

如果函数 $f(x)$ 在点 $a$ 的任一邻域内都无界, 那么点 $a$ 称为函数 $f(x)$ 的瑕点 (也称为无界间断点). 无界函数的反常积分又称为瑕积分.

设函数 $f(x)$ 在区间 $(a, b]$ 上连续，点 $a$ 为 $f(x)$ 的瑕点。任取 $t > a$ ，作定积分 $\int_{t}^{b} f(x) \mathrm{d}x$ ，再求极限

$$
\lim _ {t \rightarrow a ^ {+}} \int_ {t} ^ {b} f (x) \mathrm{d} x, \tag {4-4}
$$

这个对变下限的定积分求极限的算式(4-4)称为函数 $f(x)$ 在区间 $(a,b]$ 上的反常积分,仍然记为 $\int_{a}^{b}f(x)\mathrm{d}x$ ,即

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \lim _ {t \rightarrow a ^ {+}} \int_ {t} ^ {b} f (x) \mathrm{d} x. \tag {$4-4^{\prime$}}
$$

根据算式(4-4)的结果是否存在,可引入反常积分 $\int_{a}^{b}f(x)\mathrm{d}x$ 收敛与发散的定义如下:

定义2（1）设函数 $f(x)$ 在区间 $(a, b]$ 上连续，点 $a$ 为 $f(x)$ 的瑕点，如果极限(4-4)存在，那么称反常积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 收敛，并称此极限为该反常积分的值；如果极限(4-4)不存在，那么称反常积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 发散.

类似地, 设函数 $f(x)$ 在区间 $[a, b)$ 上连续, 点 b 为 $f(x)$ 的瑕点. 任取 t < b, 算式

$$
\lim _ {t \rightarrow b ^ {-}} \int_ {a} ^ {t} f (x) \mathrm{d} x \tag {4-5}
$$

称为函数 $f(x)$ 在区间 $[a, b)$ 上的反常积分，仍然记为 $\int_{a}^{b} f(x) \mathrm{d}x$ ，即

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \lim _ {t \rightarrow b ^ {-}} \int_ {a} ^ {t} f (x) \mathrm{d} x. \tag {$4-5^{\prime$}}
$$

于是有

(2) 设函数 $f(x)$ 在区间 $[a, b)$ 上连续, 点 $b$ 为 $f(x)$ 的瑕点, 如果极限 (4-5) 存在, 那么称反常积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 收敛, 并称此极限为该反常积分的值; 如果极限 (4-5) 不存在, 那么称反常积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 发散.

设函数 $f(x)$ 在区间 $[a, c)$ 及区间 $(c, b]$ 上连续，点 $c$ 为 $f(x)$ 的瑕点。反常积分 $\int_{a}^{c} f(x) \mathrm{d}x$ 与反常积分 $\int_{c}^{b} f(x) \mathrm{d}x$ 之和称为函数 $f(x)$ 在区间 $[a, b]$ 上的反常积分，仍然记为 $\int_{a}^{b} f(x) \mathrm{d}x$ ，即

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x. \tag {4-6}
$$

（3）设函数 $f(x)$ 在区间 $[a, c)$ 及区间 $(c, b]$ 上连续，点 $c$ 为 $f(x)$ 的瑕点。如果反常积分 $\int_{a}^{c} f(x) \mathrm{d}x$ 与反常积分 $\int_{c}^{b} f(x) \mathrm{d}x$ 均收敛，那么称反常积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 收敛，并称反常积分 $\int_{a}^{c} f(x) \mathrm{d}x$ 的值与反常积分 $\int_{c}^{b} f(x) \mathrm{d}x$ 的值之和为反常积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 的值；否则，就称反常积分 $\int_{a}^{b} f(x) \mathrm{d}x$ 发散。

计算无界函数的反常积分,也可借助于牛顿-莱布尼茨公式.

设 $x = a$ 为 $f(x)$ 的瑕点，在 $(a,b]$ 上 $F^{\prime}(x) = f(x)$ ，如果极限 $\lim_{x\to a^{+}}F(x)$ 存在，那么反常积分

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - \lim _ {x \rightarrow a ^ {+}} F (x) = F (b) - F \left(a ^ {+}\right);
$$

如果 $\lim_{x\to a^{+}}F(x)$ 不存在，那么反常积分 $\int_{a}^{b}f(x)\mathrm{d}x$ 发散.

我们仍用记号 $[F(x)]_a^b$ 来表示 $F(b) - F(a^{+})$ ，从而形式上仍有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = [ F (x) ] _ {a} ^ {b}.
$$

对于 $f(x)$ 在 $[a, b)$ 上连续， $b$ 为瑕点的反常积分，也有类似的计算公式，这里不再详述.

例4 计算反常积分

$$
\int_ {0} ^ {a} \frac {\mathrm{d} x}{\sqrt {a ^ {2} - x ^ {2}}} \quad (a > 0),
$$

解 因为

$$
\lim _ {x \rightarrow a ^ {-}} \frac {1}{\sqrt {a ^ {2} - x ^ {2}}} = + \infty ,
$$

所以点 a 是瑕点, 于是

$$
\int_ {0} ^ {a} \frac {\mathrm{d} x}{\sqrt {a ^ {2} - x ^ {2}}} = \left[ \arcsin \frac {x}{a} \right] _ {0} ^ {a} = \lim _ {x \rightarrow a ^ {-}} \arcsin \frac {x}{a} - 0 = \frac {\pi}{2}.
$$

这个反常积分值的几何意义是:位于曲线 $y=\frac{1}{\sqrt{a^{2}-x^{2}}}$ 之下,x 轴之上,直线 x=0 与 x=a 之间的图形面积(图 5-10).

例 5 讨论反常积分 $\int_{-1}^{1}\frac{dx}{x^{2}}$ 的收敛性.

解 被积函数 $f(x) = \frac{1}{x^2}$ 在积分区间 $[-1, 1]$ 上除 $x = 0$ 外连续，且 $\lim_{x \to 0} \frac{1}{x^2} = \infty$ 。由于

$$
\int_ {- 1} ^ {0} \frac {\mathrm{d} x}{x ^ {2}} = \left[ - \frac {1}{x} \right] _ {- 1} ^ {0} = \lim _ {x \to 0 ^ {-}} \left(- \frac {1}{x}\right) - 1 = + \infty ,
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/dd4e5fb633ce69a67ca282f8ed3e6f45b4166e0a3fbe4a54372772fd48b61d32.jpg)



图5-10


即反常积分 $\int_{-1}^{0}\frac{\mathrm{d}x}{x^2}$ 发散，所以反常积分 $\int_{-1}^{1}\frac{\mathrm{d}x}{x^2}$ 发散.

注意 如果疏忽了 x=0 是被积函数的瑕点, 就会得到以下的错误结果:

$$
\int_ {- 1} ^ {1} \frac {\mathrm{d} x}{x ^ {2}} = \left[ - \frac {1}{x} \right] _ {- 1} ^ {1} = - 1 - 1 = - 2.
$$

例6 证明反常积分 $\int_{a}^{b}\frac{\mathrm{d}x}{(x - a)^q}$ 当 $0 < q < 1$ 时收敛，当 $q \geqslant 1$ 时发散.

证 当 $q = 1$ 时，

$$
\int_ {a} ^ {b} \frac {\mathrm{d} x}{(x - a) ^ {q}} = \int_ {a} ^ {b} \frac {\mathrm{d} x}{x - a} = [ \ln (x - a) ] _ {a} ^ {b} = \ln (b - a) - \lim _ {x \rightarrow a ^ {+}} \ln (x - a) = + \infty .
$$

当 $q \neq 1$ 时，

$$
\int_ {a} ^ {b} \frac {\mathrm{d} x}{(x - a) ^ {q}} = \left[ \frac {(x - a) ^ {1 - q}}{1 - q} \right] _ {a} ^ {b} = \left\{ \begin{array}{l l} \frac {(b - a) ^ {1 - q}}{1 - q}, & 0 <   q <   1, \\ + \infty , & q > 1. \end{array} \right.
$$

因此, 当 0 < q < 1 时, 该反常积分收敛, 其值为 $\frac{(b-a)^{1-q}}{1-q}$ ; 当 $q \geqslant 1$ 时, 该反常积分

发散.

设有反常积分 $\int_{a}^{b} f(x) \mathrm{d}x$ ，其中 $f(x)$ 在开区间 $(a, b)$ 内连续， $a$ 可以是 $-\infty, b$ 可以是 $+\infty, a, b$ 也可以是 $f(x)$ 的瑕点。对于这样的反常积分，在另加换元函数单调的假定下，可以像定积分一样作换元。

例7 求反常积分 $\int_0^{+\infty}\frac{\mathrm{d}x}{\sqrt{x(x + 1)^3}}.$ 

解 这里,积分上限为 $+\infty$ ,且下限x=0为被积函数的瑕点.

令 $\sqrt{x} = t$ ，则 $x = t^2$ ，当 $x\to 0^{+}$ 时 $t\to 0$ ；当 $x\rightarrow +\infty$ 时 $t\rightarrow +\infty$ .于是

$$
\int_ {0} ^ {+ \infty} \frac {\mathrm{d} x}{\sqrt {x (x + 1) ^ {3}}} = \int_ {0} ^ {+ \infty} \frac {2 t \mathrm{d} t}{t (t ^ {2} + 1) ^ {3 / 2}} = 2 \int_ {0} ^ {+ \infty} \frac {\mathrm{d} t}{(t ^ {2} + 1) ^ {3 / 2}}.
$$

再令 $t = \tan u$ ，则 $u = \arctan t$ ，当 $t = 0$ 时 $u = 0$ ；当 $t\to +\infty$ 时 $u\to \frac{\pi}{2}$ .于是

$$
\int_ {0} ^ {+ \infty} \frac {\mathrm{d} x}{\sqrt {x (x + 1) ^ {3}}} = 2 \int_ {0} ^ {\frac {\pi}{2}} \frac {\sec^ {2} u \mathrm{d} u}{\sec^ {3} u} = 2 \int_ {0} ^ {\frac {\pi}{2}} \cos u \mathrm{d} u = 2.
$$

本例如用代换 $\frac{1}{x} = t$ 或 $\frac{1}{x + 1} = t$ ，计算会更简单些，读者可自行解之.

# 习题5-4

1. 判定下列各反常积分的收敛性,如果收敛,计算反常积分的值:

(1) $\int_{1}^{+\infty}\frac{\mathrm{d}x}{x^4};$ 

(2) $\int_{1}^{+\infty}\frac{dx}{\sqrt{x}};$ 

(3) $\int_{0}^{+\infty}\mathrm{e}^{-ax}\mathrm{d}x (a > 0)$ ; 

(4) $\int_{0}^{+\infty}\frac{dx}{(1+x)(1+x^{2})};$ 

(5) $\int_{0}^{+\infty}\mathrm{e}^{-pt}\sin\omega t\mathrm{d}t\quad(p>0,\omega>0);$ 

(6) $\int_{-\infty}^{+\infty}\frac{dx}{x^{2}+2x+2};$ 

(7) $\int_{0}^{1}\frac{x\mathrm{d}x}{\sqrt{1-x^{2}}};$ 

(8) $\int_{0}^{2}\frac{dx}{(1-x)^{2}};$ 

(9) $\int_{1}^{2}\frac{x\mathrm{d}x}{\sqrt{x-1}};$ 

(10) $\int_{1}^{e}\frac{\mathrm{d}x}{x\sqrt{1 - (\ln x)^2}}.$ 

2. 求由曲线 $y=\frac{1}{4x^{2}-1}$ 、x 轴和直线 x=1 所围成的向右无限延伸的图形的面积.

3. 当 k 为何值时, 反常积分 $\int_{2}^{+\infty}\frac{\mathrm{d}x}{x(\ln x)^{k}}$ 收敛? 当 k 为何值时, 该反常积分发散? 又当 k 为何值时, 该反常积分取得最小值?

4. 利用递推公式计算反常积分 $I_{n} = \int_{0}^{+\infty} x^{n} \mathrm{e}^{-x} \, \mathrm{d}x (n \in \mathbb{N})$ .

5. 计算反常积分 $\int_{0}^{1}\ln xdx$ .

# * 第五节 反常积分的审敛法 Γ函数

反常积分的收敛性,可以通过求被积函数的原函数,然后按定义取极限,根据极限的存在与否来判定.本节中我们来建立不通过被积函数的原函数判定反常积分收敛性的判定法.

# 一、无穷限反常积分的审敛法

定理1 设函数 $f(x)$ 在区间 $[a, +\infty)$ 上连续，且 $f(x) \geqslant 0$ . 若函数

$$
F (x) = \int_ {a} ^ {x} f (t) \mathrm{d} t
$$

在 $[a, +\infty)$ 上有上界，则反常积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 收敛.

事实上, 因为 $f(x) \geqslant 0, F(x)$ 在 $[a, +\infty)$ 上单调增加, 又 $F(x)$ 在 $[a, +\infty)$ 上有上界, 故 $F(x)$ 在 $[a, +\infty)$ 上是单调有界的函数. 按照“ $[a, +\infty)$ 上的单调有界函数 $F(x)$ 必有极限 $\lim_{x \to +\infty} F(x)$ ”的准则, 就可知道极限

$$
\lim _ {x \rightarrow + \infty} \int_ {a} ^ {x} f (t) d t
$$

存在,即反常积分 $\int_{a}^{+\infty}f(x)dx$ 收敛.

根据定理 1, 对于非负函数的无穷限的反常积分, 有以下的比较审敛原理:

定理2（比较审敛原理）设函数 $f(x), g(x)$ 在区间 $[a, +\infty)$ 上连续. 如果 $0 \leqslant f(x) \leqslant g(x) (a \leqslant x < +\infty)$ ，并且 $\int_{a}^{+\infty} g(x) \mathrm{d}x$ 收敛，那么 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 也收敛；如果 $0 \leqslant g(x) \leqslant f(x) (a \leqslant x < +\infty)$ ，并且 $\int_{a}^{+\infty} g(x) \mathrm{d}x$ 发散，那么 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 也发散.

证 设 $a < t < +\infty$ ，由 $0 \leqslant f(x) \leqslant g(x)$ 及 $\int_{a}^{+\infty} g(x) \, \mathrm{d}x$ 收敛，得

$$
\int_ {a} ^ {t} f (x) \mathrm{d} x \leqslant \int_ {a} ^ {t} g (x) \mathrm{d} x \leqslant \int_ {a} ^ {+ \infty} g (x) \mathrm{d} x.
$$

这表明作为积分上限 $t$ 的函数

$$
F (t) = \int_ {a} ^ {t} f (x) \mathrm{d} x
$$

在 $[a, +\infty)$ 上有上界. 由定理1即知反常积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 收敛.

如果 $0 \leqslant g(x) \leqslant f(x)$ , 且 $\int_{a}^{+\infty} g(x) \mathrm{d}x$ 发散, 那么 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 必定发散. 因为如果 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 收敛, 由定理的第一部分即知 $\int_{a}^{+\infty} g(x) \mathrm{d}x$ 也收敛, 这与假设相矛盾. 证毕.

由上节例3知道,反常积分 $\int_{a}^{+\infty}\frac{\mathrm{d}x}{x^{p}}(a>0)$ 当p>1时收敛,当 $p\leqslant1$ 时发散.因此,取 $g(x)=\frac{A}{x^{p}}(A>0)$ ,立即可得下面的反常积分的比较审敛法.

定理3（比较审敛法1）设函数 $f(x)$ 在区间 $[a, +\infty)$ （ $a > 0$ ）上连续，且 $f(x) \geqslant 0$ 。如果存在常数 $M > 0$ 及 $p > 1$ ，使得 $f(x) \leqslant \frac{M}{x^p}$ （ $a \leqslant x < +\infty$ ），那么反常积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 收敛；如果存在常数 $N > 0$ ，使得 $f(x) \geqslant \frac{N}{x}$ （ $a \leqslant x < +\infty$ ），那么反常积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 发散。

例1 判定反常积分 $\int_{1}^{+\infty}\frac{\mathrm{d}x}{\sqrt[3]{x^4 + 1}}$ 的收敛性.

解 由于

$$
0 <   \frac {1}{\sqrt [ 3 ]{x ^ {4} + 1}} <   \frac {1}{\sqrt [ 3 ]{x ^ {4}}} = \frac {1}{x ^ {\frac {4}{3}}},
$$

根据比较审敛法1,这个反常积分收敛.

以比较审敛法 1 为基础, 可以得到在应用上较为方便的极限审敛法.

定理4（极限审敛法1）设函数 $f(x)$ 在区间 $[a, +\infty)$ 上连续，且 $f(x) \geqslant 0$ 。如果存在常数 $p > 1$ ，使得 $\lim_{x \to +\infty} x^p f(x) = c < +\infty$ ，那么反常积分 $\int_{a}^{+\infty} f(x) \, \mathrm{d}x$ 收敛；如果 $\lim_{x \to +\infty} x f(x) = d > 0$ （或 $\lim_{x \to +\infty} x f(x) = +\infty$ ），那么反常积分 $\int_{a}^{+\infty} f(x) \, \mathrm{d}x$ 发散。

证 由假设 $\lim_{x\to +\infty}x^p f(x) = c(p > 1)$ . 根据极限的定义, 存在充分大的 $x_{1}(x_{1}\geqslant a,x_{1} > 0)$ , 当 $x > x_{1}$ 时, 必有

$$
\mid x ^ {p} f (x) - c \mid <   1,
$$

由此得

$$
0 \leqslant x ^ {p} f (x) <   1 + c.
$$

令 $1 + c = M > 0$ ，于是在区间 $(x_{1}, + \infty)$ 内不等式 $0\leqslant f(x) <   \frac{M}{x^p}$ 成立.由比较审敛法1知

$\int_{x_1}^{+\infty}f(x)\mathrm{d}x$ 收敛，而

$$
\begin{array}{l} \int_ {a} ^ {+ \infty} f (x) \mathrm{d} x = \lim _ {t \rightarrow + \infty} \int_ {a} ^ {t} f (x) \mathrm{d} x = \lim _ {t \rightarrow + \infty} \left[ \int_ {a} ^ {x _ {1}} f (x) \mathrm{d} x + \int_ {x _ {1}} ^ {t} f (x) \mathrm{d} x \right] \\ = \int_ {a} ^ {x _ {1}} f (x) \mathrm{d} x + \lim _ {t \rightarrow + \infty} \int_ {x _ {1}} ^ {t} f (x) \mathrm{d} x = \int_ {a} ^ {x _ {1}} f (x) \mathrm{d} x + \int_ {x _ {1}} ^ {+ \infty} f (x) \mathrm{d} x, \\ \end{array}
$$

故反常积分

$$
\int_ {a} ^ {+ \infty} f (x) \mathrm{d} x
$$

收敛.

如果 $\lim_{x\to +\infty}xf(x) = d > 0$ （或 $+\infty$ ），那么存在充分大的 $x_{1}$ ，当 $x > x_{1}$ 时，必有

$$
\left| x f (x) - d \right| <   \frac {d}{2},
$$

由此得

$$
x f (x) > \frac {d}{2}.
$$

(当 $\lim_{x\to+\infty}xf(x)=+\infty$ 时, 可取任意正数作为 d.) 令 $\frac{d}{2}=N>0$ , 于是在区间 $(x_{1},+\infty)$ 内不等式 $f(x)\geqslant\frac{N}{x}$ 成立. 根据比较审敛法 1 知 $\int_{x_{1}}^{+\infty}f(x)\mathrm{d}x$ 发散, 从而反常积分 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 发散.

例2 判定反常积分 $\int_{1}^{+\infty}\frac{\mathrm{d}x}{x\sqrt{1 + x^2}}$ 的收敛性.

解 由于

$$
\lim _ {x \rightarrow + \infty} x ^ {2} \cdot \frac {1}{x \sqrt {1 + x ^ {2}}} = \lim _ {x \rightarrow + \infty} \frac {1}{\sqrt {\frac {1}{x ^ {2}} + 1}} = 1,
$$

根据极限审敛法 1, 知所给反常积分收敛.

例3 判定反常积分 $\int_{1}^{+\infty}\frac{x^{\frac{3}{2}}}{1 + x^2}\mathrm{d}x$ 的收敛性.

解 由于

$$
\lim _ {x \rightarrow + \infty} x \frac {x ^ {\frac {3}{2}}}{1 + x ^ {2}} = \lim _ {x \rightarrow + \infty} \frac {x ^ {2} \sqrt {x}}{1 + x ^ {2}} = + \infty ,
$$

根据极限审敛法 1, 知所给反常积分发散.

例4 判定反常积分 $\int_{1}^{+\infty}\frac{\arctan x}{x}\mathrm{d}x$ 的收敛性.

解 由于

$$
\lim _ {x \rightarrow + \infty} x \frac {\arctan x}{x} = \lim _ {x \rightarrow + \infty} \arctan x = \frac {\pi}{2},
$$

根据极限审敛法 1, 知所给反常积分发散.

假定反常积分的被积函数在所讨论的区间上可取正值也可取负值,对于这类反常积分的收敛性,有如下的结论:

定理5 设函数 $f(x)$ 在区间 $[a, +\infty)$ 上连续. 如果反常积分

$$
\int_ {a} ^ {+ \infty} | f (x) | \mathrm{d} x
$$

收敛,那么反常积分

$$
\int_ {a} ^ {+ \infty} f (x) \mathrm{d} x
$$

也收敛.

证 令 $\varphi(x) = \frac{1}{2} [f(x) + |f(x)|]$ , 于是 $\varphi(x) \geqslant 0$ , 且 $\varphi(x) \leqslant |f(x)|$ , 而

$\int_{a}^{+\infty}|f(x)|\mathrm{d}x$ 收敛，由比较审敛法1即知 $\int_{a}^{+\infty}\varphi (x)\mathrm{d}x$ 也收敛.但 $f(x) = 2\varphi (x) - |f(x)|$ ，因此

$$
\int_ {a} ^ {+ \infty} f (x) \mathrm{d} x = 2 \int_ {a} ^ {+ \infty} \varphi (x) \mathrm{d} x - \int_ {a} ^ {+ \infty} | f (x) | \mathrm{d} x.
$$

可见反常积分 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 是两个收敛的反常积分的差，因此它是收敛的.证毕

通常称满足定理5条件的反常积分 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 绝对收敛.于是，定理5可简单地表达为：绝对收敛的反常积分 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 必定收敛.

例5 判定反常积分 $\int_0^{+\infty}\mathrm{e}^{-ax}\sin bx\mathrm{d}x(a,b$ 都是常数，且 $a > 0)$ 的收敛性.

解 因为 $|\mathrm{e}^{-ax}\sin bx| \leqslant \mathrm{e}^{-ax}$ , 而 $\int_0^{+\infty} \mathrm{e}^{-ax} \, \mathrm{d}x$ 收敛, 根据比较审敛法 1, 反常积分 $\int_0^{+\infty} |\mathrm{e}^{-ax}\sin bx| \, \mathrm{d}x$ 收敛. 由定理 5 可知所给反常积分收敛.

# 二、无界函数的反常积分的审敛法

对于无界函数的反常积分,也有类似的审敛法.

由上节例6知道,反常积分

$$
\int_ {a} ^ {b} \frac {\mathrm{d} x}{(x - a) ^ {q}}
$$

当 $q < 1$ 时收敛，当 $q \geqslant 1$ 时发散.于是，与定理3、定理4类似可得如下两个审敛法：

定理6（比较审敛法2）设函数 $f(x)$ 在区间 $(a,b]$ 上连续，且 $f(x)\geqslant 0,x = a$ 为 $f(x)$ 的瑕点.如果存在常数 $M > 0$ 及 $q < 1$ ，使得

$$
f (x) \leqslant \frac {M}{(x - a) ^ {q}} \quad (a <   x \leqslant b),
$$

那么反常积分 $\int_{a}^{b}f(x)\mathrm{d}x$ 收敛；如果存在常数 $N > 0$ ，使得

$$
f (x) \geqslant \frac {N}{x - a} \quad (a <   x \leqslant b),
$$

那么反常积分 $\int_{a}^{b}f(x)\mathrm{d}x$ 发散.

定理7（极限审敛法2）设函数 $f(x)$ 在区间 $(a,b]$ 上连续，且 $f(x)\geqslant 0,x = a$ 为 $f(x)$ 的瑕点.如果存在常数 $0 < q < 1$ ，使得

$$
\lim _ {x \rightarrow a ^ {+}} (x - a) ^ {q} f (x)
$$

存在,那么反常积分 $\int_{a}^{b}f(x)\mathrm{d}x$ 收敛;如果

$$
\lim _ {x \to a ^ {+}} (x - a) f (x) = d > 0 \quad (\text {或} \lim _ {x \to a ^ {+}} (x - a) f (x) = + \infty),
$$

那么反常积分 $\int_{a}^{b}f(x)\mathrm{d}x$ 发散.

例6 判定反常积分 $\int_{1}^{3}\frac{\mathrm{d}x}{\ln x}$ 的收敛性.

解 这里 $x = 1$ 是被积函数的瑕点. 由洛必达法则知

$$
\lim _ {x \to 1 ^ {+}} (x - 1) \frac {1}{\ln x} = \lim _ {x \to 1 ^ {+}} \frac {1}{\frac {1}{x}} = 1 > 0,
$$

根据极限审敛法2,所给反常积分发散.

例7 判定椭圆积分

$$
\int_ {0} ^ {1} \frac {\mathrm{d} x}{\sqrt {(1 - x ^ {2}) (1 - k ^ {2} x ^ {2})}} \quad (k ^ {2} <   1)
$$

的收敛性.

解 这里 $x = 1$ 是被积函数的瑕点.由于

$$
\lim _ {x \to 1 ^ {-}} (1 - x) ^ {\frac {1}{2}} \frac {1}{\sqrt {(1 - x ^ {2}) (1 - k ^ {2} x ^ {2})}} = \lim _ {x \to 1 ^ {-}} \frac {1}{\sqrt {(1 + x) (1 - k ^ {2} x ^ {2})}} = \frac {1}{\sqrt {2 (1 - k ^ {2})}},
$$

根据极限审敛法 2, 所给反常积分收敛.

对于无界函数的反常积分,当被积函数在所讨论的区间上可取正值也可取负值时,有与定理5相类似的结论,在此不再详述.

例8 判定反常积分 $\int_0^1\frac{1}{\sqrt{x}}\sin \frac{1}{x}\mathrm{d}x$ 的收敛性.

解 因为 $\left|\frac{1}{\sqrt{x}}\sin\frac{1}{x}\right|\leqslant\frac{1}{\sqrt{x}}$ ，而 $\int_{0}^{1}\frac{dx}{\sqrt{x}}$ 收敛，根据比较审敛法2，反常积分 $\int_{0}^{1}\left|\frac{1}{\sqrt{x}}\sin\frac{1}{x}\right|dx$ 收敛，从而反常积分 $\int_{0}^{1}\frac{1}{\sqrt{x}}\sin\frac{1}{x}dx$ 也收敛.

# 三、 $\Gamma$ 函数

下面介绍在理论上和应用上都有重要意义的 $\Gamma$ 函数.这函数的定义是

$$
\Gamma (s) = \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- x} x ^ {s - 1} \mathrm{d} x \quad (s > 0). \tag {5-1}
$$

首先,讨论(5-1)式右端积分的收敛性问题.这个积分的积分区间为无穷,又当s-1<0时x=0是被积函数的瑕点.为此,分别讨论下列两个积分

$$
I _ {1} = \int_ {0} ^ {1} \mathrm{e} ^ {- x} x ^ {s - 1} \mathrm{d} x, I _ {2} = \int_ {1} ^ {+ \infty} \mathrm{e} ^ {- x} x ^ {s - 1} \mathrm{d} x
$$

的收敛性.

先讨论 $I_{1}$ . 当 $s \geqslant 1$ 时, $I_{1}$ 是定积分; 当 0 < s < 1 时, 因为

$$
\mathrm{e} ^ {- x} \cdot x ^ {s - 1} = \frac {1}{\mathrm{e} ^ {x}} \frac {1}{x ^ {1 - s}} <   \frac {1}{x ^ {1 - s}},
$$

而 1-s<1, 根据比较审敛法 2, 反常积分 $I_{1}$ 收敛.

再讨论 $I_{2}$ .因为

$$
\lim _ {x \rightarrow + \infty} x ^ {2} \cdot \left(\mathrm{e} ^ {- x} x ^ {s - 1}\right) = \lim _ {x \rightarrow + \infty} \frac {x ^ {s + 1}}{\mathrm{e} ^ {x}} = 0,
$$

根据极限审敛法 1, $I_{2}$ 也收敛.

由以上讨论即得反常积分 $\int_0^{+\infty}\mathrm{e}^{-x}x^{s - 1}\mathrm{d}x$ 对 $s > 0$ 均收敛. $\Gamma$ 函数的图形如图5-11所示.

其次,讨论 $\Gamma$ 函数的几个重要性质.

1. 递推公式 $\Gamma(s+1)=s\Gamma(s) (s>0)$ .

证 应用分部积分法,有

$$
\Gamma (s + 1) = \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- x} x ^ {s} \mathrm{d} x = - \int_ {0} ^ {+ \infty} x ^ {s} \mathrm{d} (\mathrm{e} ^ {- x}) = [ - x ^ {s} \mathrm{e} ^ {- x} ] _ {0} ^ {+ \infty} + s \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- x} x ^ {s - 1} \mathrm{d} x = s \Gamma (s),
$$

其中 $\lim_{x\to+\infty}x^{s}e^{-x}=0$ 可由洛必达法则求得.

显然, $\Gamma(1)=\int_{0}^{+\infty}\mathrm{e}^{-x}\mathrm{d}x=1.$ 

反复运用递推公式,便有

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/009c1a3625eb9a54578afddaedb373804aa02832f86e67dd23d1b5c612c10fd8.jpg)



图5-11


$$
\begin{array}{l} \Gamma (2) = 1 \cdot \Gamma (1) = 1, \\ \Gamma (3) = 2 \cdot \Gamma (2) = 2!, \\ \Gamma (4) = 3 \cdot \Gamma (3) = 3!, \dots \\ \end{array}
$$

一般地,对任何正整数 n,有

$$
\Gamma (n + 1) = n!,
$$

所以,我们可以把 $\Gamma$ 函数看成是阶乘的推广.

2. 当 $s \to 0^{+}$ 时, $\Gamma(s) \to +\infty$ .

证 因为

$$
\Gamma (s) = \frac {\Gamma (s + 1)}{s}, \quad \Gamma (1) = 1,
$$

所以当 $s \to 0^{+}$ 时, $\Gamma(s) \to +\infty$ ①.

3. $\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin\pi s}$ (0<s<1). 

这个公式称为余元公式,在此我们不作证明.

当 $s=\frac{1}{2}$ 时,由余元公式可得

$$
\Gamma \left(\frac {1}{2}\right) = \sqrt {\pi}.
$$

4. 在 $\Gamma(s) = \int_{0}^{+\infty} \mathrm{e}^{-x} x^{s-1} \, \mathrm{d}x$ 中，作代换 $x = u^2$ ，有

$$
\Gamma (s) = 2 \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- u ^ {2}} u ^ {2 s - 1} \mathrm{d} u. \tag {5-2}
$$

再令 $2s - 1 = t$ 或 $s = \frac{1 + t}{2}$ , 便有

$$
\int_ {0} ^ {+ \infty} \mathrm{e} ^ {- u ^ {2}} u ^ {t} \mathrm{d} u = \frac {1}{2} \Gamma \left(\frac {1 + t}{2}\right) (t > - 1).
$$

上式左端是实际应用中常见的积分,它的值可以通过上式用 $\Gamma$ 函数计算出来.

在(5-2)中,令 $s=\frac{1}{2}$ ,得

$$
2 \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- u ^ {2}} \mathrm{d} u = \Gamma \left(\frac {1}{2}\right) = \sqrt {\pi}.
$$

从而

$$
\int_ {0} ^ {+ \infty} \mathrm{e} ^ {- u ^ {2}} \mathrm{d} u = \frac {\sqrt {\pi}}{2}.
$$

上式左端的积分是在概率论中常用的积分.

# *习题5-5

1. 判定下列反常积分的收敛性：

(1) $\int_{0}^{+\infty}\frac{x^{2}}{x^{4} + x^{2} + 1}\mathrm{d}x;$ 

(2) $\int_{1}^{+\infty}\frac{dx}{x\sqrt[3]{x^{2}+1}};$ 

(3) $\int_{1}^{+\infty}\sin \frac{1}{x^2}\mathrm{d}x;$ 

(4) $\int_{0}^{+\infty}\frac{\mathrm{d}x}{1 + x|\sin x|};$ 

(5) $\int_{1}^{+\infty}\frac{x\arctan x}{1 + x^3}\mathrm{d}x;$ 

(6) $\int_{1}^{2}\frac{dx}{(\ln x)^{3}};$ 

(7) $\int_{0}^{1}\frac{x^{4}}{\sqrt{1-x^{4}}}dx;$ 

(8) $\int_{1}^{2}\frac{\mathrm{d}x}{\sqrt[3]{x^2 - 3x + 2}}.$ 

2. 设反常积分 $\int_{1}^{+\infty} f^{2}(x) dx$ 收敛, 证明反常积分 $\int_{1}^{+\infty} \frac{f(x)}{x} dx$ 绝对收敛.

3. 用 $\Gamma$ 函数表示下列积分, 并指出这些积分的收敛范围:

(1) $\int_{0}^{+\infty}\mathrm{e}^{-x^{n}}\mathrm{d}x (n > 0)$ ; 

(2) $\int_{0}^{1}\left(\ln \frac{1}{x}\right)^{p}\mathrm{d}x;$ 

(3) $\int_{0}^{+\infty} x^{m} \mathrm{e}^{-x^{n}} \, \mathrm{d}x (n \neq 0)$ . 

4. 证明 $\Gamma\left(\frac{2k+1}{2}\right)=\frac{1\cdot3\cdot5\cdot\cdots\cdot(2k-1)\sqrt{\pi}}{2^k}$ , 其中 $k\in\mathbf{N}_{+}$ .

5. 证明以下各式(其中 $n \in \mathbb{N}_+$ ):

(1) $2 \cdot 4 \cdot 6 \cdot \cdots \cdot 2n = 2^{n}\Gamma(n+1)$ ; 

(2) $1 \cdot 3 \cdot 5 \cdot \cdots \cdot (2n - 1) = \frac{\Gamma(2n)}{2^{n - 1}\Gamma(n)};$ 

(3) $\sqrt{\pi}\Gamma(2n)=2^{2n-1}\Gamma(n)\Gamma\left(n+\frac{1}{2}\right)$ (勒让德(Legendre)倍量公式).

# 总习题五

1. 填空：

（1）函数 $f(x)$ 在 $[a,b]$ 上有界是 $f(x)$ 在 $[a,b]$ 上可积的____条件，而 $f(x)$ 在 $[a,b]$ 上连续是 $f(x)$ 在 $[a,b]$ 上可积的____条件；

(2) 对 $[a, +\infty)$ 上非负、连续的函数 $f(x)$ , 积分上限的函数 $\int_{a}^{x} f(t) \mathrm{d}t$ 在 $[a, +\infty)$ 上有界是反常积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 收敛的 ____ 条件;

* (3) 绝对收敛的反常积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 一定 ____；

(4) 函数 $f(x)$ 在 $[a, b]$ 上有定义且 $|f(x)|$ 在 $[a, b]$ 上可积，此时积分 $\int_{a}^{b} f(x) \, dx$ ____ 存在.

(5) 设函数 $f(x)$ 连续，则 $\frac{d}{dx}\int_{0}^{x}tf(t^{2}-x^{2})dt=$ ____.

2. 以下两题中给出了四个结论,从中选出一个正确的结论:

（1）设 $I = \int_0^1\frac{x^4}{\sqrt{1 + x}}\mathrm{d}x$ ，则估计 $I$ 值的大致范围为（ ）；

(A) $0 \leqslant I \leqslant \frac{\sqrt{2}}{10}$ 

(B) $\frac{\sqrt{2}}{10} \leqslant I \leqslant \frac{1}{5}$ 

(C) $\frac{1}{5}<I<1$ 

(D) $I \geqslant 1$ 

(2) 设 $F(x)$ 是连续函数 $f(x)$ 的一个原函数, 则必有().

(A) $F(x)$ 是偶函数 $\Leftrightarrow f(x)$ 是奇函数

(B) $F(x)$ 是奇函数 $\Leftrightarrow f(x)$ 是偶函数

(C) $F(x)$ 是周期函数 $\Leftrightarrow f(x)$ 是周期函数

(D) $F(x)$ 是单调函数 $\Leftrightarrow f(x)$ 是单调函数

3. 回答下列问题：

（1）设函数 $f(x)$ 及 $g(x)$ 在区间 $[a,b]$ 上连续，且 $f(x)\geqslant g(x)$ ，则 $\int_{a}^{b}[f(x)-g(x)]\mathrm{d}x$ 在几何上表示什么？

(2) 设函数 $f(x)$ 在区间 $[a, b]$ 上连续，且 $f(x) \geqslant 0$ ，则 $\int_{a}^{b} \pi f^{2}(x) \, dx$ 在几何上表示什么？

（3）如果在时刻 t 以 $\varphi(t)$ 的流量（单位时间内流过的流体的体积或质量）向一水池注水，那么 $\int_{t_{1}}^{t_{2}}\varphi(t)\mathrm{d}t$ 表示什么？

(4) 如果某国人口增长的速率为 $u(t)$ ，那么 $\int_{T_{1}}^{T_{2}} u(t) \, dt$ 表示什么？

(5) 如果一公司经营某种产品的边际利润函数为 $P'(x)$ ，那么 $\int_{1000}^{2000} P'(x) \, dx$ 表示什么？

*4. 利用定积分的定义计算下列极限：

(1) $\lim_{n\to \infty}\frac{1}{n}\sum_{i = 1}^{n}\sqrt{1 + \frac{i}{n}};$ 

(2) $\lim_{n\to \infty}\frac{1^p + 2^p + \cdots + n^p}{n^{p + 1}} (p > 0).$ 

5. 求下列极限：

(1) $\lim_{x\to a}\frac{x}{x - a}\int_{a}^{x}f(t)\mathrm{d}t$ ，其中 $f(x)$ 连续；

(2) $\lim_{x\to +\infty}\frac{\int_0^x(\arctan t)^2dt}{\sqrt{x^2 + 1}}.$ 

6. 下列计算是否正确,试说明理由:

(1) $\int_{-1}^{1}\frac{\mathrm{d}x}{1 + x^2} = -\int_{-1}^{1}\frac{\mathrm{d}\left(\frac{1}{x}\right)}{1 + \left(\frac{1}{x}\right)^2} = \left[-\arctan \frac{1}{x}\right]_{-1}^{1} = -\frac{\pi}{2};$ 

(2) 因为 $\int_{-1}^{1}\frac{dx}{x^{2}+x+1}=\frac{x=\frac{1}{t}}{t}=\int_{-1}^{1}\frac{dt}{t^{2}+t+1}$ ，所以 $\int_{-1}^{1}\frac{dx}{x^{2}+x+1}=0.$ 

7. 设 $x > 0$ ，证明： $\int_{0}^{x} \frac{1}{1 + t^2} \mathrm{d}t + \int_{0}^{\frac{1}{x}} \frac{1}{1 + t^2} \mathrm{d}t = \frac{\pi}{2}$ .

8. 设 p > 0，证明： $\frac{p}{p+1} < \int_{0}^{1} \frac{dx}{1 + x^{p}} < 1.$ 

9. 设 $f(x)$ , $g(x)$ 在区间 $[a, b]$ 上均连续, 证明:

(1) $\left[\int_{a}^{b}f(x)g(x)\mathrm{d}x\right]^{2}\leqslant \int_{a}^{b}f^{2}(x)\mathrm{d}x\cdot \int_{a}^{b}g^{2}(x)\mathrm{d}x$ （柯西-施瓦茨不等式）；

(2) $\left\{\int_{a}^{b}[f(x) + g(x)]^{2}\mathrm{d}x\right\}^{\frac{1}{2}}\leqslant \left[\int_{a}^{b}f^{2}(x)\mathrm{d}x\right]^{\frac{1}{2}} + \left[\int_{a}^{b}g^{2}(x)\mathrm{d}x\right]^{\frac{1}{2}}$ （闵可夫斯基不等式）.

10. 设 $f(x)$ 在区间 $[a, b]$ 上连续，且 $f(x) > 0$ . 证明： $\int_{a}^{b} f(x) \mathrm{d}x \cdot \int_{a}^{b} \frac{\mathrm{d}x}{f(x)} \geqslant (b - a)^2$ .

11. 计算下列积分：

(1) $\int_{0}^{\frac{\pi}{2}}\frac{x + \sin x}{1 + \cos x}\mathrm{d}x;$ 

(2) $\int_{0}^{\frac{\pi}{4}}\ln (1 + \tan x)\mathrm{d}x;$ 

(3) $\int_{0}^{a}\frac{\mathrm{d}x}{x + \sqrt{a^2 - x^2}} (a > 0)$ ; 

(4) $\int_{0}^{\frac{\pi}{2}}\sqrt{1 - \sin 2x}\mathrm{d}x;$ 

(5) $\int_{0}^{\frac{\pi}{2}}\frac{\mathrm{d}x}{1 + \cos^2x};$ 

(6) $\int_{0}^{\pi} x \sqrt{\cos^{2} x - \cos^{4} x} \, \mathrm{d}x$ ; 

(7) $\int_{0}^{\pi} x^{2} \mid \cos x \, \mathrm{d}x$ ; 

(8) $\int_{0}^{+\infty}\frac{\mathrm{d}x}{\mathrm{e}^{x + 1} + \mathrm{e}^{3 - x}};$ 

(9) $\int_{\frac{1}{2}}^{\frac{3}{2}}\frac{\mathrm{d}x}{\sqrt{|x^2 - x|}};$ 

(10) $\int_0^x\max \{t^3,t^2,1\} \mathrm{d}t.$ 

12. 设 $f(x)$ 为连续函数, 证明: $\int_{0}^{x}f(t)(x - t)\mathrm{d}t = \int_{0}^{x}\left[\int_{0}^{t}f(u)\mathrm{d}u\right]\mathrm{d}t.$ 

13. 设 $f(x)$ 在区间 $[a, b]$ 上连续，且 $f(x) > 0$ ，

$$
F (x) = \int_ {a} ^ {x} f (t) \mathrm{d} t + \int_ {b} ^ {x} \frac {\mathrm{d} t}{f (t)}, \quad x \in [ a, b ].
$$

证明：

(1) $F'(x) \geqslant 2;$ 

(2) 方程 $F(x)=0$ 在区间 $(a,b)$ 内有且仅有一个根.

14. 求 $\int_{0}^{2}f(x-1)\mathrm{d}x$ , 其中

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{1 + \mathrm{e} ^ {x}}, & x <   0, \\ \frac {1}{1 + x}, & x \geqslant 0. \end{array} \right.
$$

15. 设 $f'(x)$ 在 $[- \pi, \pi]$ 上连续， $a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos nx \, dx (n \in \mathbb{N})$ ，证明： $\lim_{n \to \infty} a_n = 0$ 

16. 设 $f(x)$ 在区间 $[a, b]$ 上连续, $g(x)$ 在区间 $[a, b]$ 上连续且不变号. 证明: 至少存在一点 $\xi \in [a, b]$ , 使下式成立:

$$
\int_ {a} ^ {b} f (x) g (x) \mathrm{d} x = f (\xi) \int_ {a} ^ {b} g (x) \mathrm{d} x \quad (\text {积分第一中值定理}).
$$

* 17. 证明: $\int_{0}^{+\infty} x^{n} \mathrm{e}^{-x^{2}} \mathrm{d} x = \frac{n - 1}{2} \int_{0}^{+\infty} x^{n - 2} \mathrm{e}^{-x^{2}} \mathrm{d} x (n > 1)$ , 并用它证明

$$
\int_ {0} ^ {+ \infty} x ^ {2 n + 1} e ^ {- x ^ {2}} d x = \frac {1}{2} \Gamma (n + 1) \quad (n \in \mathbf {N}).
$$

* 18. 判定下列反常积分的收敛性：

(1) $\int_{0}^{+\infty}\frac{\sin x}{\sqrt{x^3}}\mathrm{d}x;$ 

(2) $\int_{2}^{+\infty}\frac{\mathrm{d}x}{x\cdot\sqrt[3]{x^2-3x+2}};$ 

(3) $\int_{2}^{+\infty} \frac{\cos x}{\ln x} \, \mathrm{d}x$ ; 

(4) $\int_{0}^{+\infty}\frac{\mathrm{d}x}{\sqrt[3]{x^2(x - 1)(x - 2)}}.$ 

* 19. 计算下列反常积分:

(1) $\int_{0}^{\frac{\pi}{2}}\ln \sin x\mathrm{d}x;$ 

(2) $\int_{0}^{+\infty}\frac{\mathrm{d}x}{(1 + x^2)(1 + x^\alpha)} (\alpha \geqslant 0).$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/424d4678efbecb7d35be63868899eca13d4cc12b1d531c58bef6241b3a760b3e.jpg)



第五章释疑解难


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/c0516ff6c5cda34753cfa0e5c6ba8d151099c5defd5b77f87e6798947b63982f.jpg)



第五章例题精讲


# 第六章

# 定积分的应用

本章中我们将应用前面学过的定积分理论来分析和解决一些几何、物理中的问题,其目的不仅在于建立计算这些几何、物理量的公式,更重要的还在于介绍运用元素法将一个量表达成为定积分的分析方法.

# 第一节 定积分的元素法

在定积分的应用中,经常采用所谓元素法.为了说明这种方法,我们先回顾一下第五章中讨论过的曲边梯形的面积问题.

设 $f(x)$ 在区间 $[a,b]$ 上连续且 $f(x)\geqslant0$ ，求以曲线 $y=f(x)$ 为曲边、底为 $[a,b]$ 的曲边梯形的面积A.把这个面积A表示为定积分

$$
A = \int_ {a} ^ {b} f (x) \mathrm{d} x
$$

的步骤是

(1) 用任意一组分点把区间 $[a, b]$ 分成长度为 $\Delta x_{i} (i = 1,2,\dots,n)$ 的 $n$ 个小区间，相应地把曲边梯形分成 $n$ 个窄曲边梯形，第 $i$ 个窄曲边梯形的面积设为 $\Delta A_{i}$ ，于是有

$$
A = \sum_ {i = 1} ^ {n} \Delta A _ {i};
$$

(2) 计算 $\Delta A_{i}$ 的近似值

$$
\Delta A _ {i} \approx f (\xi_ {i}) \Delta x _ {i} \quad (x _ {i - 1} \leqslant \xi_ {i} \leqslant x _ {i});
$$

(3) 求和, 得 A 的近似值

$$
A \approx \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i};
$$

(4) 求极限, 记 $\lambda = \max\left\{\Delta x_{1}, \Delta x_{2}, \cdots, \Delta x_{n}\right\}$ , 得

$$
A = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} = \int_ {a} ^ {b} f (x) \mathrm{d} x.
$$

在上述问题中我们注意到,所求量(即面积 A)与区间 $[a,b]$ 有关.如果把区间 $[a,b]$ 分成许多部分区间,那么所求量相应地分成许多部分量(即 $\Delta A_{i}$ ),而所求量等于所有部分量之和(即 $A=\sum_{i=1}^{n}\Delta A_{i}$ ),这一性质称为所求量对于区间 $[a,b]$ 具有可加性.此外,以 $f(\xi_{i})\Delta x_{i}$ 近似代替部分量 $\Delta A_{i}$ 时,要求它们只相差一个比 $\Delta x_{i}$ 高阶的无穷小,以使和式 $\sum_{i=1}^{n}f(\xi_{i})\Delta x_{i}$ 的极限是 A 的精确值,从而 A 可以表示为定积分

$$
A = \int_ {a} ^ {b} f (x) \mathrm{d} x.
$$

在引出 $A$ 的积分表达式的四个步骤中，主要的是第二步，这一步是要确定 $\Delta A_{i}$ 的近似值 $f(\xi_i)\Delta x_i$ ，使得

$$
A = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} = \int_ {a} ^ {b} f (x) \mathrm{d} x.
$$

在实用上,为了简便起见,省略下标 i,用 $\Delta A$ 表示任一小区间 $[x,x+dx]$ 上的窄曲边梯形的面积,这样,

$$
A = \sum \Delta A.
$$

取 $[x,x+\mathrm{d}x]$ 的左端点x为 $\xi$ ，以点x处的函数值 $f(x)$ 为高、dx为底的矩形的面积 $f(x)\mathrm{d}x$ 为 $\Delta A$ 的近似值（如图6-1阴影部分所示），即

$$
\Delta A \approx f (x) \mathrm{d} x.
$$

上式右端 $f(x)\mathrm{d}x$ 叫做面积元素, 记为 $\mathrm{d}A=f(x)\mathrm{d}x$ . 于是

$$
A \approx \sum f (x) \mathrm{d} x,
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/9a3bbff414f33df64aa51e3a97168de1425a39904c45e50ba0ac5917bed503dc.jpg)



图6-1


因此

$$
A = \lim \sum f (x) \mathrm{d} x = \int_ {a} ^ {b} f (x) \mathrm{d} x.
$$

一般地,如果某一实际问题中的所求量 U 符合下列条件:

(1) U 是与一个变量 x 的变化区间 $[a, b]$ 有关的量；

(2) U 对于区间 $[a, b]$ 具有可加性, 就是说, 如果把区间 $[a, b]$ 分成许多部分区间, 那么 U 相应地分成许多部分量, 而 U 等于所有部分量之和;

(3) 部分量 $\Delta U_{i}$ 的近似值可表示为 $f(\xi_{i})\Delta x_{i}$ ,

那么就可考虑用定积分来表达这个量 U. 通常写出这个量 U 的积分表达式的步骤是

1）根据问题的具体情况,选取一个变量例如 x 为积分变量,并确定它的变化区间

$[a,b]$ 

2）设想把区间 $[a,b]$ 分成 $n$ 个小区间，取其中任一小区间并记作 $[x,x + \mathrm{d}x]$ ，求出相应于这个小区间的部分量 $\Delta U$ 的近似值。如果 $\Delta U$ 能近似地表示为 $[a,b]$ 上的一个连续函数在 $x$ 处的值 $f(x)$ 与 $\mathrm{d}x$ 的乘积①，就把 $f(x)\mathrm{d}x$ 称为量 $U$ 的元素且记作 $\mathrm{d}U$ ，即

$$
\mathrm{d} U = f (x) \mathrm{d} x;
$$

3）以所求量 $U$ 的元素 $f(x)\mathrm{d}x$ 为被积表达式，在区间 $[a,b]$ 上作定积分，得

$$
U = \int_ {a} ^ {b} f (x) \mathrm{d} x.
$$

这就是所求量 U 的积分表达式.

这个方法通常叫做元素法.下面两节中我们将应用这个方法来讨论几何、物理中的一些问题.

# 第二节 定积分在几何学上的应用

# 一、平面图形的面积

# 1. 直角坐标情形

在第五章中我们已经知道,由曲线 $y=f(x)$ ( $f(x)\geqslant0$ ) 及直线 x=a, x=b (a<b) 与 x 轴所围成的曲边梯形的面积 A 是定积分

$$
A = \int_ {a} ^ {b} f (x) \mathrm{d} x,
$$

其中被积表达式 $f(x)\mathrm{d}x$ 就是直角坐标下的面积元素,它表示高为 $f(x)$ 、底为dx的一个矩形面积.

应用定积分,不但可以计算曲边梯形面积,还可以计算一些比较复杂的平面图形的面积.

例 1 计算由两条抛物线: $y^{2}=x, y=x^{2}$ 所围成的图形的面积.

解 这两条抛物线所围成的图形如图 6-2 所示.为了具体定出图形的所在范围,先求出这两条抛物线的交点.为此,解方程组

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/dbef2ed7d665eecd4332384db80bb80164fbf89ef86fe72dca9491ff1f75bbd8.jpg)



图6-2


$$
\left\{ \begin{array}{l} y ^ {2} = x, \\ y = x ^ {2}, \end{array} \right.
$$

得到两个解

$$
x = 0, y = 0 \quad {\text {及}} \quad x = 1, y = 1.
$$

即这两抛物线的交点为(0,0)及(1,1)，从而知道这图形在直线x=0与x=1之间.

取横坐标 $x$ 为积分变量, 它的变化区间为 $[0,1]$ . 相应于 $[0,1]$ 上的任一小区间 $[x, x + \mathrm{d}x]$ 的窄条的面积近似于高为 $\sqrt{x} - x^2$ 、底为 $\mathrm{d}x$ 的窄矩形的面积, 从而得到面积元素

$$
\mathrm{d} A = (\sqrt {x} - x ^ {2}) \mathrm{d} x.
$$

以 $(\sqrt{x}-x^{2})\mathrm{d}x$ 为被积表达式,在闭区间[0,1]上作定积分,便得所求面积为

$$
A = \int_ {0} ^ {1} (\sqrt {x} - x ^ {2}) \mathrm{d} x = \left[ \frac {2}{3} x ^ {\frac {3}{2}} - \frac {x ^ {3}}{3} \right] _ {0} ^ {1} = \frac {1}{3}.
$$

例 2 计算抛物线 $y^{2}=2x$ 与直线 y=x-4 所围成的图形的面积.

解 这个图形如图 6-3 所示.为了定出这图形所在的范围,先求出所给抛物线和直线的交点.解方程组

$$
\left\{ \begin{array}{l} y ^ {2} = 2 x, \\ y = x - 4, \end{array} \right.
$$

得交点 $(2,-2)$ 和 $(8,4)$ ，从而知道这图形在直线y=-2及y=4之间.

现在,选取纵坐标 y 为积分变量,它的变化区间为 $[-2,4]$ (读者可以思考一下,取横坐标 x 为积分变量,有什么不方便的地方).相应于 $[-2,4]$ 上任一小区间 $[y,y+dy]$ 的窄条面积近似于高为dy、底为 $(y+4)-\frac{1}{2}y^{2}$ 的窄矩形的面积,从而得到面积元素

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/41d2c16521620b4f791c7fb08c32a05d8aad402ece1cc554d9e9e20409203ea2.jpg)



图6-3


$$
\mathrm{d} A = \left(y + 4 - \frac {1}{2} y ^ {2}\right) \mathrm{d} y.
$$

以 $\left(y + 4 - \frac{1}{2} y^2\right)\mathrm{d}y$ 为被积表达式，在闭区间[-2,4]上作定积分，便得所求的面积为

$$
A = \int_ {- 2} ^ {4} \left(y + 4 - \frac {1}{2} y ^ {2}\right) d y = \left[ \frac {y ^ {2}}{2} + 4 y - \frac {y ^ {3}}{6} \right] _ {- 2} ^ {4} = 1 8.
$$

由例 2 可以看到,积分变量选得适当,可使计算方便.

例3 求椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ 所围成的图形的面积.

解 该椭圆关于两坐标轴都对称(图6-4),所以椭圆所围成的图形的面积为

$$
A = 4 A _ {1},
$$

其中 $A_{1}$ 为该椭圆在第一象限部分与两坐标轴所围图形的面积, 因此

$$
A = 4 A _ {1} = 4 \int_ {0} ^ {a} y \mathrm{d} x.
$$

利用椭圆的参数方程

$$
\left\{ \begin{array}{l l} x = a \cos t, \\ y = b \sin t \end{array} \right. \quad \left(0 \leqslant t \leqslant \frac {\pi}{2}\right),
$$

应用定积分换元法, 令 $x = a \cos t$ , 则

$$
y = b \sin t, \quad \mathrm{d} x = - a \sin t \mathrm{d} t.
$$

当 $x$ 由0变到 $a$ 时， $t$ 由 $\frac{\pi}{2}$ 变到0，所以

$$
\begin{array}{l} A = 4 \int_ {\frac {\pi}{2}} ^ {0} b \sin t (- a \sin t) \mathrm{d} t = - 4 a b \int_ {\frac {\pi}{2}} ^ {0} \sin^ {2} t \mathrm{d} t \\ = 4 a b \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} t \mathrm{d} t = 4 a b \cdot \frac {1}{2} \cdot \frac {\pi}{2} = \pi a b. \\ \end{array}
$$

当 a=b 时, 就得到大家所熟悉的圆面积的公式 $A=\pi a^{2}$ .

# 2. 极坐标情形

某些平面图形,用极坐标来计算它们的面积比较方便.

设由曲线 $\rho=\rho(\theta)$ 及射线 $\theta=\alpha,\theta=\beta$ 围成一图形（简称为曲边扇形），现在要计算它的面积（图 6-5）。这里， $\rho(\theta)$ 在 $[\alpha,\beta]$ 上连续，且 $\rho(\theta)\geqslant0,0<\beta-\alpha\leqslant2\pi.$ 

由于当 $\theta$ 在 $[\alpha,\beta]$ 上变动时, 极径 $\rho=\rho(\theta)$ 也随之变动, 因此所求图形的面积不能直接利用扇形面积的公式 $A=\frac{1}{2}R^{2}\theta$ 来计算.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/8df17a32589adf95fb4686d09c5fee54c9a0d1d893114179f3f064a8b427c337.jpg)



图6-4


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/b79c7c6653d3f1c389d7c06da4e94e11e055b0b8bf5066906e129ea46e8fca17.jpg)



图6-5


取极角 $\theta$ 为积分变量, 它的变化区间为 $[\alpha, \beta]$ . 相应于任一小区间 $[\theta, \theta + \mathrm{d}\theta]$ 的窄曲边扇形的面积可以用半径为 $\rho = \rho(\theta)$ 、中心角为 $\mathrm{d}\theta$ 的扇形的面积来近似代替, 从而得到这窄曲边扇形面积的近似值, 即曲边扇形的面积元素

$$
\mathrm{d} A = \frac {1}{2} [ \rho (\theta) ] ^ {2} \mathrm{d} \theta .
$$

以 $\frac{1}{2} [\rho (\theta)]^2\mathrm{d}\theta$ 为被积表达式，在闭区间 $[\alpha ,\beta ]$ 上作定积分，便得所求曲边扇形的面

积为

$$
A = \int_ {\alpha} ^ {\beta} \frac {1}{2} [ \rho (\theta) ] ^ {2} \mathrm{d} \theta .
$$

例 4 计算阿基米德螺线

$$
\rho = a \theta \quad (a > 0)
$$

上相应于 $\theta$ 从0变到 $2\pi$ 的一段弧与极轴所围成的图形(图6-6)的面积.

解 在指定的这段螺线上, $\theta$ 的变化区间为 $[0,2\pi]$ .相应于 $[0,2\pi]$ 上任一小区间 $[\theta,\theta+d\theta]$ 的窄曲边扇形的面积近似于半径为 $a\theta$ 、圆心角为 $d\theta$ 的扇形的面积,从而得到面积元素

$$
\mathrm{d} A = \frac {1}{2} (a \theta) ^ {2} \mathrm{d} \theta .
$$

于是所求面积为

$$
A = \int_ {0} ^ {2 \pi} \frac {a ^ {2}}{2} \theta^ {2} \mathrm{d} \theta = \frac {a ^ {2}}{2} \left[ \frac {\theta^ {3}}{3} \right] _ {0} ^ {2 \pi} = \frac {4}{3} a ^ {2} \pi^ {3}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/75b306b120275aa484b72722544cde897a73231ce662a918eb17d9a018a51757.jpg)



图6-6


例5 计算心形线

$$
\rho = a (1 + \cos \theta) \quad (a > 0)
$$

所围成的图形的面积.

解 心形线所围成的图形如图 6-7 所示. 这个图形对称于极轴, 因此所求图形的面积 A 是极轴以上部分图形面积 $A_{1}$ 的 2 倍.

对于极轴以上部分的图形, $\theta$ 的变化区间为 $[0,\pi]$ .相应于 $[0,\pi]$ 上任一小区间 $[\theta,\theta+d\theta]$ 的窄曲边扇形的面积近似于半径为 $a(1+\cos\theta)$ 、圆心角为 $d\theta$ 的扇形的面积.从而得到面积元素

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/fdc5bf196c29bafbc004b961c7479805f5548269a7cdf94db75c3a2506248523.jpg)



图6-7


$$
\mathrm{d} A = \frac {1}{2} a ^ {2} (1 + \cos \theta) ^ {2} \mathrm{d} \theta ,
$$

# 

例题精讲

6-1 

1 

释疑解难

6-1 

于是

$$
\begin{array}{l} A _ {1} = \int_ {0} ^ {\pi} \frac {1}{2} a ^ {2} (1 + \cos \theta) ^ {2} \mathrm{d} \theta = \frac {a ^ {2}}{2} \int_ {0} ^ {\pi} (1 + 2 \cos \theta + \cos^ {2} \theta) \mathrm{d} \theta \\ = \frac {a ^ {2}}{2} \int_ {0} ^ {\pi} \left(\frac {3}{2} + 2 \cos \theta + \frac {1}{2} \cos 2 \theta\right) d \theta \\ = \frac {a ^ {2}}{2} \left[ \frac {3}{2} \theta + 2 \sin \theta + \frac {1}{4} \sin 2 \theta \right] _ {0} ^ {\pi} = \frac {3}{4} \pi a ^ {2}, \\ \end{array}
$$

因而所求面积为

$$
A = 2 A _ {1} = \frac {3}{2} \pi a ^ {2}.
$$

# 二、体积

# 1. 旋转体的体积

旋转体就是由一个平面图形绕这平面内一条直线旋转一周而成的立体.这直线叫做旋转轴.圆柱、圆锥、圆台、球可以分别看成是由矩形绕它的一条边、直角三角形绕它的直角边、直角梯形绕它的直角腰、半圆绕它的直径旋转一周而成的立体,所以它们都是旋转体.

上述旋转体都可以看作是由连续曲线 $y=f(x)$ ，直线 x=a, x=b 及 x 轴所围成的曲边梯形绕 x 轴旋转一周而成的立体。现在我们考虑用定积分来计算这种旋转体的体积。

取横坐标 x 为积分变量, 它的变化区间为 $[a,b]$ . 相应于 $[a,b]$ 上的任一小区间 $[x,x+dx]$ 的窄曲边梯形绕 x 轴旋转而成的薄片的体积近似于以 $f(x)$ 为底半径、dx 为高的扁圆柱体的体积(图 6-8), 即体积元素

$$
\mathrm{d} V = \pi [ f (x) ] ^ {2} \mathrm{d} x.
$$

以 $\pi[f(x)]^{2}dx$ 为被积表达式, 在闭区间 $[a,b]$ 上作定积分, 便得所求旋转体体积为

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/c8f2c560308f61fa66bf8a1599998d5bb2ebfec8fd1d17f4bc535e0bc0c24e51.jpg)



图6-8


$$
V = \int_ {a} ^ {b} \pi [ f (x) ] ^ {2} \mathrm{d} x.
$$

例6 连接坐标原点 $O$ 及点 $P(h, r)$ 的直线、直线 $x = h$ 及 $x$ 轴围成一个直角三角形（图6-9). 将它绕 $x$ 轴旋转一周构成一个底半径为 $r$ 、高为 $h$ 的圆锥体. 计算这圆锥体的体积.

解 过原点 O 及点 $P(h,r)$ 的直线方程为

$$
y = \frac {r}{h} x.
$$

取横坐标 $x$ 为积分变量, 它的变化区间为 $[0, h]$ . 圆锥体中相应于 $[0, h]$ 上任一小区间 $[x, x + \mathrm{d}x]$ 的薄片的体积近似于底半径为 $\frac{r}{h} x$ 、高为 $\mathrm{d}x$ 的扁圆柱体的体积, 即体积元素

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/e03873a7a1822c66ed27e774678c41a0934760eab7ac2aadc26358e64b88075e.jpg)



图6-9


$$
\mathrm{d} V = \pi \left[ \frac {r}{h} x \right] ^ {2} \mathrm{d} x.
$$

于是所求圆锥体的体积为

$$
V = \int_ {0} ^ {h} \pi \left(\frac {r}{h} x\right) ^ {2} \mathrm{d} x = \frac {\pi r ^ {2}}{h ^ {2}} \left[ \frac {x ^ {3}}{3} \right] _ {0} ^ {h} = \frac {\pi r ^ {2} h}{3}.
$$

例7 计算由椭圆

$$
\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} = 1
$$

所围成的图形绕 x 轴旋转一周而成的旋转体(叫做旋转椭球体)的体积.

解 这个旋转椭球体也可以看作是由半个椭圆

$$
y = \frac {b}{a} \sqrt {a ^ {2} - x ^ {2}}
$$

及 x 轴围成的图形绕 x 轴旋转一周而成的立体.

取 $x$ 为积分变量, 它的变化区间为 $[-a, a]$ . 旋转椭球体中相应于 $[-a, a]$ 上任一小区间 $[x, x + \mathrm{d}x]$ 的薄片的体积, 近似于底半径为 $\frac{b}{a} \sqrt{a^2 - x^2}$ , 高为 $\mathrm{d}x$ 的扁圆柱体的体积

(图 6-10), 即体积元素

$$
\mathrm{d} V = \frac {\pi b ^ {2}}{a ^ {2}} (a ^ {2} - x ^ {2}) \mathrm{d} x.
$$

于是所求旋转椭球体的体积为

$$
\begin{array}{l} V = \int_ {- a} ^ {a} \pi \frac {b ^ {2}}{a ^ {2}} (a ^ {2} - x ^ {2}) \mathrm{d} x = \frac {2 \pi b ^ {2}}{a ^ {2}} \int_ {0} ^ {a} (a ^ {2} - x ^ {2}) \mathrm{d} x \\ = 2 \pi \frac {b ^ {2}}{a ^ {2}} \left[ a ^ {2} x - \frac {x ^ {3}}{3} \right] _ {0} ^ {a} = \frac {4}{3} \pi a b ^ {2}. \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/be24d81533897d0f1ebda9cafb756fa6512c8e80bb9f00879634804f95375b54.jpg)



图6-10


当 a=b 时,旋转椭球体就成为半径为 a 的球,它的体积为 $\frac{4}{3}\pi a^{3}$ .

用与上面类似的方法可以推出:由曲线 $x=\varphi(y)$ ，直线 y=c, y=d (c<d) 与 y 轴所围成的曲边梯形，绕 y 轴旋转一周而成的旋转体(图 6-11) 的体积为

$$
V = \pi \int_ {c} ^ {d} [ \varphi (y) ] ^ {2} d y,
$$

例8 计算由摆线 $x = a(t - \sin t), y = a(1 - \cos t)$ 相应于 $0 \leqslant t \leqslant 2\pi$ 的一拱与直线 $y = 0$ 所围成的图形分别绕 $x$ 轴、 $y$ 轴旋转而成的旋转体的体积.

解 按旋转体的体积公式,所述图形绕 x 轴旋转而成的旋转体的体积为

$$
V _ {x} = \int_ {0} ^ {2 \pi a} \pi y ^ {2} (x) \mathrm{d} x = \pi \int_ {0} ^ {2 \pi} a ^ {2} (1 - \cos t) ^ {2} \cdot a (1 - \cos t) \mathrm{d} t
$$

$$
= \pi a ^ {3} \int_ {0} ^ {2 \pi} (1 - 3 \cos t + 3 \cos^ {2} t - \cos^ {3} t) d t = 5 \pi^ {2} a ^ {3}.
$$

所述图形绕 y 轴旋转而成的旋转体的体积可看成平面图形 OABC 与 OBC（图 6-12）分别绕 y 轴旋转而成的旋转体的体积之差。因此所求的体积为

$$
\begin{array}{l} V _ {y} = \int_ {0} ^ {2 a} \pi x _ {2} ^ {2} (y) \mathrm{d} y - \int_ {0} ^ {2 a} \pi x _ {1} ^ {2} (y) \mathrm{d} y \\ = \pi \int_ {2 \pi} ^ {\pi} a ^ {2} (t - \sin t) ^ {2} \cdot a \sin t d t - \pi \int_ {0} ^ {\pi} a ^ {2} (t - \sin t) ^ {2} \cdot a \sin t d t \\ = - \pi a ^ {3} \int_ {0} ^ {2 \pi} (t - \sin t) ^ {2} \sin t d t = 6 \pi^ {3} a ^ {3}. \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/6b46ab22a31d7532e8883316fb8b509ccbc6ba054abffe0501aaf0e0cc33248d.jpg)



图6-11


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/8ac2f3cab53b5ba4cc443f1667118e1936fd1f851f79e99a30d232fa40d3e296.jpg)



图6-12


# 2. 平行截面面积为已知的立体的体积

从计算旋转体体积的过程中可以看出:如果一个立体不是旋转体,但却知道该立体上垂直于一定轴的各个截面的面积,那么,这个立体的体积也可以用定积分来计算.

如图 6-13 所示, 取上述定轴为 x 轴, 并设该立体在过点 x=a, x=b 且垂直于 x 轴的两个平面之间. 以 $A(x)$ 表示过点 x 且垂直于 x 轴的截面面积. 假定 $A(x)$ 为已知的 x 的连续函数. 这时, 取 x 为积分变量, 它的变化区间为 $[a, b]$ ; 立体中相应于 $[a, b]$ 上任一小区间 $[x, x + dx]$ 的一薄片的体积, 近似于底面积为 $A(x)$ 、高为 dx 的扁柱体的体积, 即体积元素

$$
\mathrm{d} V = A (x) \mathrm{d} x.
$$

以 $A(x)\mathrm{d}x$ 为被积表达式, 在闭区间 $[a,b]$ 上作定积分, 便得所求立体的体积

$$
V = \int_ {a} ^ {b} A (x) \mathrm{d} x.
$$

例9 一平面经过半径为 $R$ 的圆柱体的底圆中心, 并与底面交成角 $\alpha$ (图6-14). 计算这平面截圆柱体所得立体的体积.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/d4f5142316ae0f0ba8a6a88abc34f49824c559597870db5af56c7a172810cf46.jpg)



图6-13


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/a8f4bdcf5bd8dd809aebe75b5a663c02b1b44ffb6023435ff1c832605897b8bd.jpg)



图6-14


解 取这平面与圆柱体的底面的交线为 $x$ 轴，底面上过圆中心、且垂直于 $x$ 轴的直线为 $y$ 轴.那么，底圆的方程为 $x^{2} + y^{2} = R^{2}$ .立体中过 $x$ 轴上的点 $x$ 且垂直于 $x$ 轴的截面是一个直角三角形.它的两条直角边的长分别为 $y$ 及 $y\tan \alpha$ ，即 $\sqrt{R^2 - x^2}$ 及 $\sqrt{R^2 - x^2}\tan \alpha.$ 因而截面积为 $A(x) = \frac{1}{2} (R^2 -x^2)\tan \alpha$ ，于是所求立体体积为

$$
\begin{array}{l} V = \int_ {- R} ^ {R} \frac {1}{2} (R ^ {2} - x ^ {2}) \tan \alpha \mathrm{d} x = \int_ {0} ^ {R} (R ^ {2} - x ^ {2}) \tan \alpha \mathrm{d} x \\ = \tan \alpha \left[ R ^ {2} x - \frac {1}{3} x ^ {3} \right] _ {0} ^ {R} = \frac {2}{3} R ^ {3} \tan \alpha . \\ \end{array}
$$

例 10 求以半径为 R 的圆为底、平行且等于底圆直径的线段为顶、高为 h 的正劈锥体的体积.

解 取底圆所在的平面为 $xOy$ 平面, 圆心 $O$ 为原点, 并使 $x$ 轴与正劈锥的顶平行 (图6-15). 底圆的方程为 $x^{2} + y^{2} = R^{2}$ . 过 $x$ 轴上的点 $x (-R \leqslant x \leqslant R)$ 作垂直于 $x$ 轴的平面, 截正劈锥体得等腰三角形. 这截面的面积为

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/dcf28dfb03271e00965098d45567fe291df68cc1c0c23da603e2e75e7aa9d3d4.jpg)



图6-15


$$
A (x) = h y = h \sqrt {R ^ {2} - x ^ {2}},
$$

于是所求正劈锥体的体积为

$$
\begin{array}{l} V = \int_ {- R} ^ {R} A (x) \mathrm{d} x = h \int_ {- R} ^ {R} \sqrt {R ^ {2} - x ^ {2}} \mathrm{d} x = 2 h \int_ {0} ^ {R} \sqrt {R ^ {2} - x ^ {2}} \mathrm{d} x \\ = 2 R ^ {2} h \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} \theta \mathrm{d} \theta = \frac {\pi R ^ {2} h}{2}. \\ \end{array}
$$

由此可知正劈锥体的体积等于同底同高的圆柱体体积的一半.

# 三、平面曲线的弧长

我们知道,圆的周长可以利用圆的内接正多边形的周长当边数无限增多时的极限来确定.现在用类似的方法来建立平面的连续曲线弧长的概念,从而应用定积分来计

算弧长.

设 A, B 是曲线弧的两个端点. 在弧 $\widehat{AB}$ 上依次任取分点 $A = M_{0}, M_{1}, M_{2}, \cdots, M_{i-1}$ ,

$M_{i},\cdots,M_{n-1},M_{n}=B$ ,并依次连接相邻的分点得一折线(图6-16).当分点的数目无限增加且每个小段 $\widehat{M_{i-1}M_{i}}$ 都缩向一点时,如果此折线的长 $\sum_{i=1}^{n}|M_{i-1}M_{i}|$ 的极限存在,那么称此极限为曲线弧 $\widehat{AB}$ 的弧长,并称此曲线弧 $\widehat{AB}$ 是可求长的.

对光滑的曲线弧(参看第165页上的脚注),有如下结论:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/95e84c8710323e9a280724cb454109bf62ece4f07958d6c4f9f56d21b2ee4412.jpg)



图6-16


定理 光滑曲线弧是可求长的.

这个定理我们不加证明.由于光滑曲线弧是可求长的,故可应用定积分来计算弧长.下面我们利用定积分的元素法来讨论平面光滑曲线弧长的计算公式.

设曲线弧由参数方程

$$
\left\{ \begin{array}{l l} x = \varphi (t), \\ y = \psi (t) \end{array} \right. (\alpha \leqslant t \leqslant \beta)
$$

给出,其中 $\varphi(t),\psi(t)$ 在 $[\alpha,\beta]$ 上具有连续导数,且 $\varphi'(t),\psi'(t)$ 不同时为零.现在来计算这曲线弧的长度.

取参数 t 为积分变量, 它的变化区间为 $[\alpha, \beta]$ . 相应于 $[\alpha, \beta]$ 上任一小区间 $[t, t + dt]$ 的小弧段的长度 $\Delta s$ 近似等于对应的弦的长度 $\sqrt{(\Delta x)^{2} + (\Delta y)^{2}}$ , 因为

$$
\Delta x = \varphi (t + \mathrm{d} t) - \varphi (t) \approx \mathrm{d} x = \varphi^ {\prime} (t) \mathrm{d} t,
$$

$$
\Delta y = \psi (t + \mathrm{d} t) - \psi (t) \approx \mathrm{d} y = \psi^ {\prime} (t) \mathrm{d} t,
$$

所以, $\Delta s$ 的近似值(弧微分)即弧长元素为

$$
\mathrm{d} s = \sqrt {(\mathrm{d} x) ^ {2} + (\mathrm{d} y) ^ {2}} = \sqrt {\varphi^ {\prime 2} (t) (\mathrm{d} t) ^ {2} + \psi^ {\prime 2} (t) (\mathrm{d} t) ^ {2}} = \sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)} \mathrm{d} t.
$$

于是所求弧长为

$$
s = \int_ {\alpha} ^ {\beta} \sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)} \mathrm{d} t.
$$

当曲线弧由直角坐标方程

$$
y = f (x) \quad (a \leqslant x \leqslant b)
$$

给出,其中 $f(x)$ 在 $[a,b]$ 上具有一阶连续导数,这时曲线弧有参数方程

$$
\left\{ \begin{array}{l l} x = x, \\ y = f (x) \end{array} \right. \quad (a \leqslant x \leqslant b),
$$

从而所求的弧长为

$$
s = \int_ {a} ^ {b} \sqrt {1 + y ^ {\prime 2}} \mathrm{d} x.
$$

当曲线弧由极坐标方程

$$
\rho = \rho (\theta) \quad (\alpha \leqslant \theta \leqslant \beta)
$$

给出,其中 $\rho(\theta)$ 在 $[\alpha,\beta]$ 上具有连续导数,则由直角坐标与极坐标的关系可得

$$
\left\{ \begin{array}{l l} x = x (\theta) = \rho (\theta) \cos \theta , \\ y = y (\theta) = \rho (\theta) \sin \theta \end{array} \right. (\alpha \leqslant \theta \leqslant \beta),
$$

这就是以极角 $\theta$ 为参数的曲线弧的参数方程.于是,弧长元素为

$$
\mathrm{d} s = \sqrt {x ^ {\prime 2} (\theta) + y ^ {\prime 2} (\theta)} \mathrm{d} \theta = \sqrt {\rho^ {2} (\theta) + \rho^ {\prime 2} (\theta)} \mathrm{d} \theta ,
$$

从而所求弧长为

$$
s = \int_ {\alpha} ^ {\beta} \sqrt {\rho^ {2} (\theta) + \rho^ {\prime 2} (\theta)} d \theta .
$$

例11 计算曲线 $y = \frac{2}{3} x^{\frac{3}{2}}$ 上相应于 $a \leqslant x \leqslant b$ 的一段弧（图6-17）的长度.

解 因 $y' = x^{\frac{1}{2}}$ ，从而弧长元素

$$
\mathrm{d} s = \sqrt {1 + \left(x ^ {\frac {1}{2}}\right) ^ {2}} \mathrm{d} x = \sqrt {1 + x} \mathrm{d} x.
$$

因此,所求弧长为

$$
s = \int_ {a} ^ {b} \sqrt {1 + x} \mathrm{d} x = \left[ \frac {2}{3} (1 + x) ^ {\frac {3}{2}} \right] _ {a} ^ {b} = \frac {2}{3} \left[ (1 + b) ^ {\frac {3}{2}} - (1 + a) ^ {\frac {3}{2}} \right].
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/278d1502c5d4f9b5f41253d457419017c6c8f6320b4ede7be879d3e81b2a664c.jpg)



图6-17


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/63cc3f02c3ae8cb8623981b24b2a73a89374237e046a197fb9971a0a1c55301c.jpg)



图6-18


例 12 计算摆线(图 6-18)

$$
\left\{ \begin{array}{l} x = a (\theta - \sin \theta), \\ y = a (1 - \cos \theta) \end{array} \right.
$$

的一拱 $(0 \leqslant \theta \leqslant 2\pi)$ 的长度.

解 弧长元素为

$$
\begin{array}{l} \mathrm{d} s = \sqrt {a ^ {2} (1 - \cos \theta) ^ {2} + a ^ {2} \sin^ {2} \theta} \mathrm{d} \theta \\ = a \sqrt {2 (1 - \cos \theta)} \mathrm{d} \theta = 2 a \sin \frac {\theta}{2} \mathrm{d} \theta . \\ \end{array}
$$

从而,所求弧长

$$
s = \int_ {0} ^ {2 \pi} 2 a \sin \frac {\theta}{2} \mathrm{d} \theta = 2 a \left[ - 2 \cos \frac {\theta}{2} \right] _ {0} ^ {2 \pi} = 8 a.
$$

例 13 求阿基米德螺线 $\rho = a\theta (a > 0)$ 相应于 $0 \leqslant \theta \leqslant 2\pi$ 一段(图 6-19)的弧长.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/fb283a927e7b360992b5ea029a2881641440208c43ec4896df7b2a5a8a363c11.jpg)



图6-19


解 弧长元素为

$$
\mathrm{d} s = \sqrt {a ^ {2} \theta^ {2} + a ^ {2}} \mathrm{d} \theta = a \sqrt {1 + \theta^ {2}} \mathrm{d} \theta ,
$$

于是所求弧长为

$$
s = a \int_ {0} ^ {2 \pi} \sqrt {1 + \theta^ {2}} \mathrm{d} \theta = \frac {a}{2} [ 2 \pi \sqrt {1 + 4 \pi^ {2}} + \ln (2 \pi + \sqrt {1 + 4 \pi^ {2}}) ].
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/a323bb8e6c8ef666032668f0f7a3076c9c5028f2f8bf97fe0b72b8b2af7f1348.jpg)


例题精讲

6-3 

# 习题6-2

1. 求图 6-20 中各阴影部分的面积.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/84e32f1c130a18581fae87b3cea22df3857a6af0fe39114c3db776643d9af0f7.jpg)



(1)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/e90027d8ac162f5256fbbf8339ac9efa08633139f87ad84c51a680c9b7d5e458.jpg)



(2)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/1534bd87704c7ed37172a4d1acc9ac811f53893dd7db59115b5707054e928126.jpg)



(3)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/3db355b5331b1cf829972b1fe92e34c2c33500d0f1d1ba360f7101bd3780d0a5.jpg)



(4)



图6-20


2. 求由下列各组曲线所围成的图形的面积：

(1) $y=\frac{1}{2}x^{2}$ 与 $x^{2}+y^{2}=8$ （两部分都要计算）；

(2) $y=\frac{1}{x}$ 与直线y=x及x=2;

(3) $y=e^{x},y=e^{-x}$ 与直线x=1;

(4) $y=\ln x,y$ 轴与直线 $y=\ln a,y=\ln b(b>a>0)$ .

3. 求抛物线 $y = -x^{2} + 4x - 3$ 及其在点 $(0, -3)$ 和 $(3, 0)$ 处的切线所围成的图形的面积.

4. 求抛物线 $y^{2}=2px$ 及其在点 $\left(\frac{p}{2},p\right)$ 处的法线所围成的图形的面积.

5. 试求 $a, b$ 的值, 使得由曲线 $y = \cos x \left(0 \leqslant x \leqslant \frac{\pi}{2}\right)$ 与两坐标轴所围成的图形的面积被曲线 $y = a \sin x$ 与 $y = b \sin x$ 三等分.

6. 求由下列各曲线所围成的图形的面积：

(1) $\rho = 2a\cos \theta$ ; 

(2) $x = a\cos^3 t, y = a\sin^3 t;$ 

(3) $\rho = 2a(2 + \cos \theta)$ . 

7. 求由摆线 $x=a(t-\sin t)$ , $y=a(1-\cos t)$ 的一拱 $(0\leqslant t\leqslant2\pi)$ 与横轴所围成的图形的面积.

8. 求对数螺线 $\rho = ae^{\theta} (-\pi \leqslant \theta \leqslant \pi)$ 及射线 $\theta = \pi$ 所围成的图形的面积.

9. 求下列各曲线所围成图形的公共部分的面积：

(1) $\rho=3\cos\theta$ 及 $\rho=1+\cos\theta;$ 

(2) $\rho = \sqrt{2}\sin \theta$ 及 $\rho^2 = \cos 2\theta$ .

10. 求位于曲线 $y=e^{x}$ 下方、该曲线过原点的切线的左方以及 x 轴上方之间的图形的面积.

11. 在区间 $[1, e]$ 上求一点 $\xi$ ，使得图6-21中所示的阴影部分的面积最小。

12. 已知抛物线 $y = px^{2} + qx$ （其中 p < 0, q > 0）在第一象限内与直线 $x + y = 5$ 相切，且此抛物线与 x 轴所围成的图形的面积为 A。问 p 和 q 为何值时，A 达到最大值，并求出此最大值。

13. 由 $y=x^{3}, x=2, y=0$ 所围成的图形分别绕 x 轴及 y 轴旋转，计算所得两个旋转体的体积.

14. 把星形线 $x^{2/3} + y^{2/3} = a^{2/3}$ 所围成的图形绕 x 轴旋转（图6-22），计算所得旋转体的体积.

15. 用积分方法证明图 6-23 中球缺的体积为

$$
V = \pi H ^ {2} \left(R - \frac {H}{3}\right).
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/6961529fa62628b3574e64c40cffa8442a33d5ec27d32a3c2dcd1f186ffa7b3f.jpg)



图6-21


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/7db4d2d3be1fbf91f218d18276cad67562eeeafeb34fa3584e69c20392f783b1.jpg)



图6-22


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/872fed28fcf075d2e374cca4761dd76300be0312a072fbc7baa4b871cce7b009.jpg)



图6-23


16. 求下列已知曲线所围成的图形按指定的轴旋转所产生的旋转体的体积:

(1) $y=x^{2},x=y^{2}$ ，绕y轴；

(2) $y = \arcsin x, x = 1, y = 0$ , 绕 x 轴;

(3) $x^{2}+(y-5)^{2}=16$ , 绕 x 轴;

(4) 摆线 $x=a(t-\sin t)$ , $y=a(1-\cos t)$ 的一拱, y=0, 绕直线 y=2a.

17. 求圆盘 $x^{2} + y^{2} \leqslant a^{2}$ 绕 $x = -b (b > a > 0)$ 旋转所成旋转体的体积.

18. 设有一截锥体, 其高为 $h$ , 上、下底均为椭圆, 椭圆的轴长分别为 $2a, 2b$ 和 $2A, 2B$ , 求这截锥体的体积.

19. 计算底面是半径为 R 的圆, 而垂直于底面上一条固定直径的所有截面都是等边三角形的立体体积(图6-24).

20. 证明:由平面图形 $0 \leqslant a \leqslant x \leqslant b, 0 \leqslant y \leqslant f(x)$ 绕 $y$ 轴旋转所成的旋转体的体积为

$$
V = 2 \pi \int_ {a} ^ {b} x f (x) \mathrm{d} x.
$$

21. 利用题 20 的结论和方法, 计算曲线 $y = \sin x (0 \leqslant x \leqslant \pi)$ 和 x 轴所围成的图形按下列方式所得旋转体的体积:

(1) 绕 y 轴旋转;

(2) 绕直线 $x = -\pi$ 旋转.

22. 设由抛物线 $y = 2x^{2}$ 和直线 $x = a, x = 2$ 及 $y = 0$ 所围成的平面图形为 $D_{1}$ ，由抛物线 $y = 2x^{2}$ 和直线 $x = a$ 及 $y = 0$ 所围成的平面图形为 $D_{2}$ ，其中 $0 < a < 2$ （图6-25）.

（1）试求 $D_{1}$ 绕 $\pmb{x}$ 轴旋转而成的旋转体体积 $V_{1}, D_{2}$ 绕 $\gamma$ 轴旋转而成的旋转体体积 $V_{2}$ 

(2) 问当 a 为何值时, $V_{1}+V_{2}$ 取得最大值? 试求此最大值.

23. 计算曲线 $y=\ln x$ 上相应于 $\sqrt{3}\leqslant x\leqslant2\sqrt{2}$ 的一段弧的长度.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/0e0c97fd4356e1e0d14a29898600958761a2da60f9736aefeca17d6b76492cf5.jpg)



图6-24


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/fe560eb82cefc510a0cb577ca521228a54c1d3c83e2073924df9eae78c3daf06.jpg)



图6-25


24. 计算半立方抛物线 $y^{2}=\frac{2}{3}(x-1)^{3}$ 被抛物线 $y^{2}=\frac{x}{3}$ 截得的一段弧的长度.

25. 计算抛物线 $y^{2}=2px$ (p>0) 从顶点到这曲线上的一点 $M(x,y)$ 的弧长.

26. 计算星形线 $x = a \cos^{3} t, y = a \sin^{3} t$ （图 6-26）的全长.

27. 将绕在圆(半径为 a)上的细线放开拉直,使细线与圆周始终相切(图 6-27),细线端点画出的轨迹叫做圆的渐伸线,它的方程为

$$
x = a (\cos t + t \sin t), y = a (\sin t - t \cos t).
$$

计算该曲线上相应于 $0 \leqslant t \leqslant \pi$ 的一段弧的长度.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/b329a8b1862ebf0fe598449246be3f59dee33de4062dc7d4c07bb2d3ec36d732.jpg)



图6-26


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/be513edc4601c1274d2563c3167f793d13610ef2c3bd79a9af062875bd8d5291.jpg)



图6-27


28. 在摆线 $x=a(t-\sin t)$ , $y=a(1-\cos t)$ 上求分摆线第一拱成 1:3 的点的坐标.

29. 求对数螺线 $\rho = \mathrm{e}^{\alpha \theta}$ 相应于 $0 \leqslant \theta \leqslant \varphi$ 的一段弧长.

30. 求曲线 $\rho\theta=1$ 相应于 $\frac{3}{4}\leqslant\theta\leqslant\frac{4}{3}$ 的一段弧长.

# 第三节 定积分在物理学上的应用

# 一、变力沿直线所做的功

从物理学知道,如果物体在做直线运动的过程中有一个不变的力 F 作用在该物体上,且这力的方向与物体运动的方向一致,那么,在物体移动了距离 s 时,力 F 对物体所做的功为

$$
W = F \cdot s.
$$

如果物体在运动过程中所受到的力是变化的, 这就会遇到变力对物体做功的问题. 下面通过具体例子说明如何计算变力所做的功.

例 1 把一个带电荷量 +q 的点电荷放在 r 轴上坐标原点 O 处, 它产生一个电场. 这个电场对周围的电荷有作用力. 由物理学知道, 如果有一个单位正电荷放在这个电场中距离原点 O 为 r 的地方, 那么电场对它的作用力的大小为

$$
F = k \frac {q}{r ^ {2}} (k \text {是常数}).
$$

见图 6-28, 当这个单位正电荷在电场中从 r=a 处沿 r 轴移动到 r=b (a<b) 处时, 计算电场力 F 对它所做的功.

解 在上述移动过程中,电场对这单位正电荷的作用力是变的.取 r 为积分变量,它的变化区间为 $[a,b]$ .设$[r, r + \mathrm{d}r]$ 为 $[a, b]$ 上的任一小区间. 当单位正电荷从 $r$ 移动到 $r + \mathrm{d}r$ 时, 电场力对它所做的功近似于 $\frac{kq}{r^2}\mathrm{d}r$ , 即功元素为

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/db1bddd4f8bc44908f255d4789b9f408c34bd0e94a0525156b60c6820a48c5b7.jpg)



图6-28


$$
\mathrm{d} W = \frac {k q}{r ^ {2}} \mathrm{d} r,
$$

于是所求的功为

$$
W = \int_ {a} ^ {b} \frac {k q}{r ^ {2}} \mathrm{d} r = k q \left[ - \frac {1}{r} \right] _ {a} ^ {b} = k q \left(\frac {1}{a} - \frac {1}{b}\right).
$$

在计算静电场中某点的电位时,要考虑将单位正电荷从该点处 $(r=a)$ 移到无穷远处时电场力所做的功W.此时,电场力对单位正电荷所做的功就是反常积分

$$
W = \int_ {a} ^ {+ \infty} \frac {k q}{r ^ {2}} \mathrm{d} r = \left[ - \frac {k q}{r} \right] _ {a} ^ {+ \infty} = \frac {k q}{a}.
$$

例 2 在底面积为 S 的圆柱形容器中存有一定量的气体. 在等温条件下, 由于气体的膨胀, 把容器中的一个活塞(面积为 S)从点 a 处推移到点 b 处(图 6-29). 计算在移动过程中, 气体压力所做的功.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/189237b4e2c653d4dbcd1d9acc85acec574b6ae0aa949b270e55481c51587eff.jpg)



图6-29


解 取坐标系如图 6-29 所示. 活塞的位置可以

用坐标 x 来表示. 由物理学知道, 一定量的气体在等温条件下, 压强 p 与体积 V 的乘积是常数 k, 即

$$
p V = k \quad \text {或} \quad p = \frac {k}{V}  .
$$

因为 V = xS，所以

$$
p = \frac {k}{x S}.
$$

于是,作用在活塞上的力

$$
F = p \cdot S = \frac {k}{x S} \cdot S = \frac {k}{x}.
$$

在气体膨胀过程中,体积 V 是变化的,因而 x 也是变化的,所以作用在活塞上的力也是变化的.

取 $x$ 为积分变量, 它的变化区间为 $[a, b]$ . 设 $[x, x + \mathrm{d}x]$ 为 $[a, b]$ 上任一小区间, 当活塞从 $x$ 移动到 $x + \mathrm{d}x$ 时, 变力 $F$ 所做的功近似于 $\frac{k}{x} \mathrm{d}x$ , 即功元素为

$$
\mathrm{d} W = \frac {k}{x} \mathrm{d} x,
$$

于是所求的功为

$$
W = \int_ {a} ^ {b} \frac {k}{x} \mathrm{d} x = k [ \ln x ] _ {a} ^ {b} = k \ln \frac {b}{a}.
$$

下面再举一个计算功的例子,它虽不是一个变力做功问题,但也可用积分来计算.

例 3 一圆柱形的贮水桶高为 5 m, 底圆半径为 3 m, 桶内盛满了水. 试问要把桶内的水全部吸出需做多少功?

解 作 x 轴如图 6-30 所示. 取深度 x （单位为 m）为积分变量, 它的变化区间为 [0,5]. 相应于 [0,5] 上任一小区间 $[x, x + dx]$ 的一薄层水的高度为 dx, 若重力加速度 g 取 $9.8 \, m/s^{2}$ , 则这薄层水所受重力为 $9.8\pi \cdot 3^{2} \, dx \, kN$ . 把这薄层水吸出桶外需做的功近似地为

$$
\mathrm{d} W = 8 8. 2 \pi x \mathrm{d} x,
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/eb3fd70e8b4b618b38031d5f5e34c12c226d1e69f9515de4f5efb4c9afcebf10.jpg)



图6-30


此即功元素.于是所求的功为

$$
W = \int_ {0} ^ {5} 8 8. 2 \pi x \mathrm{d} x = 8 8. 2 \pi \left[ \frac {x ^ {2}}{2} \right] _ {0} ^ {5} = 8 8. 2 \pi \cdot \frac {2 5}{2} \approx 3 4 6 2 (\mathrm{kJ}).
$$

# 二、水压力

从物理学知道,在水深为 h 处的压强为 $p=\rho gh$ , 这里 $\rho$ 是水的密度, g 是重力加速度. 如果有一面积为 A 的平板水平地放置在水深为 h 处, 那么, 平板一侧所受的水压力为

$$
P = p \cdot A.
$$

如果平板铅直放置在水中,那么,由于水深不同的点处压强 p 不相等,平板一侧所受的水压力就不能用上述方法计算.下面举例说明它的计算方法.

例 4 一个横放着的圆柱形水桶, 桶内盛有半桶水(图 6-31(a)). 设桶的底半径为 R, 水的密度为 $\rho$ , 计算桶的一个端面上所受的压力.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/35d67889c0677c6ea977f073b6035f9527b1c03620dcd3dca209c57fd9fed425.jpg)



图6-31


解 桶的一个端面是圆片,所以现在要计算的是当水平面通过圆心时,铅直放置的一个半圆片的一侧所受到的水压力.

如图 6-31(b)，在这个圆片上取过圆心且铅直向下的直线为 x 轴，过圆心的水平线为 y 轴。对这个坐标系来讲，所讨论的半圆的方程为 $x^{2} + y^{2} = R^{2}$ （ $0 \leqslant x \leqslant R$ ）。取 x 为积分变量，它的变化区间为 $[0, R]$ 。设 $[x, x + dx]$ 为 $[0, R]$ 上的任一小区间，半圆片上相应于 $[x, x + dx]$ 的窄条上各点处的压强近似于 $\rho g x$ ，这窄条的面积近似于 $2\sqrt{R^{2} - x^{2}} dx$ 。因此，这窄条一侧所受水压力的近似值，即压力元素为

$$
\mathrm{d} P = 2 \rho g x \sqrt {R ^ {2} - x ^ {2}} \mathrm{d} x.
$$

于是所求压力为

$$
\begin{array}{l} P = \int_ {0} ^ {R} 2 \rho g x \sqrt {R ^ {2} - x ^ {2}} \mathrm{d} x = - \rho g \int_ {0} ^ {R} (R ^ {2} - x ^ {2}) ^ {\frac {1}{2}} \mathrm{d} (R ^ {2} - x ^ {2}) \\ = - \rho g \left[ \frac {2}{3} \left(R ^ {2} - x ^ {2}\right) ^ {\frac {3}{2}} \right] _ {0} ^ {R} = \frac {2 \rho g}{3} R ^ {3}. \\ \end{array}
$$

# 三、引力

从物理学知道,质量分别为 $m_{1}, m_{2}$ , 相距为 r 的两质点间的引力的大小为

$$
F = G \frac {m _ {1} m _ {2}}{r ^ {2}},
$$

其中 G 为引力常量, 引力的方向沿着两质点的连线方向.

如要计算一根细棒对一个质点的引力,那么,由于细棒上各点与该质点的距离是变化的,且各点对该质点的引力的方向也是变化的,因此就不能用上述公式来计算.下面举例说明它的计算方法.

例 5 设有一长度为 l、线密度为 $\mu$ 的均匀细直棒，在其中垂线上距棒 a 单位处有一质量为 m 的质点 M。试计算该棒对质点 M 的引力。

解 取坐标系如图 6-32 所示, 使棒位于 y 轴上, 质点 M 位于 x 轴上, 棒的中点为原点 O. 取 y 为积分变量, 它的变化区间为 $\left[-\frac{l}{2}, \frac{l}{2}\right]$ . 设 $[y, y + dy]$ 为 $\left[-\frac{l}{2}, \frac{l}{2}\right]$ 上任一小区间, 把细直棒上相应于 $[y, y + dy]$ 的一小段近似地看成质点, 其质量为 $\mu dy$ , 与 M 相距 $r = \sqrt{a^{2} + y^{2}}$ . 因此可以按照两质点间的引力计算公式求出这小段细直棒对质点 M 的引力 $\Delta F$ 的大小为

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/27e521b28f35476512ab7213ca049d142b7a9e056c05da4f6d2c8077163434e1.jpg)



图6-32


$$
\Delta F \approx G \frac {m \mu \mathrm{d} y}{a ^ {2} + y ^ {2}},
$$

从而求出 $\Delta F$ 在水平方向分力 $\Delta F_{x}$ 的近似值, 即细直棒对质点 M 的引力在水平方向分力 $F_{x}$ 的元素为

$$
\mathrm{d} F _ {x} = - G \frac {a m \mu \mathrm{d} y}{\left(a ^ {2} + y ^ {2}\right) ^ {\frac {3}{2}}}.
$$

于是得引力在水平方向分力为

$$
F _ {x} = - \int_ {- \frac {l}{2}} ^ {\frac {l}{2}} \frac {G a m \mu}{\left(a ^ {2} + y ^ {2}\right) ^ {\frac {3}{2}}} \mathrm{d} y = - \frac {2 G m \mu l}{a} \cdot \frac {1}{\sqrt {4 a ^ {2} + l ^ {2}}}.
$$

由对称性知,引力在铅直方向分力为 $F_{y}=0$ .

当细直棒的长度 l 很大时, 可视 l 趋于无穷. 此时, 引力的大小为 $\frac{2Gm\mu}{a}$ , 方向与细直棒垂直且由 M 指向细直棒.

# 习题6-3

1. 由实验知道, 弹簧在拉伸过程中, 需要的力 F (单位: N) 与伸长量 s (单位: cm) 成正比, 即
F = k s （k 是弹性系数）.

如果把弹簧由原长拉伸 $6 \, cm$ ，计算所做的功.

2. 直径为 20 cm、高为 80 cm 的圆筒内充满压强为 $10 \, N/cm^{2}$ 的蒸汽。设温度保持不变，要使蒸汽体积缩小一半，问需要做多少功？

3.（1）证明：把质量为 m 的物体从地球表面升高到 h 处所做的功是

$$
W = \frac {m g R h}{R + h},
$$

其中 g 是重力加速度, R 是地球的半径;

(2) 一颗人造地球卫星的质量为 $173 \mathrm{~kg}$ , 在高于地面 $630 \mathrm{~km}$ 处进入轨道. 问把这颗卫星从地面送到 $630 \mathrm{~km}$ 的高空处, 克服地球引力要做多少功? 已知 $g = 9.8 \mathrm{~m} / \mathrm{s}^{2}$ , 地球半径 $R = 6370 \mathrm{~km}$ .

4. 一物体按规律 $x = ct^3$ 做直线运动, 介质的阻力与速度的平方成正比. 计算物体由 $x = 0$ 移至 $x = a$ 时, 克服介质阻力所做的功.

5. 用铁锤将一铁钉击入木板, 设木板对铁钉的阻力与铁钉被击入木板的深度成正比, 在锤击第一次时, 将铁钉击入木板 1 cm. 如果铁锤每次锤击铁钉所做的功相等, 问锤击第二次时, 铁钉又被击入木板多少?

6. 设一圆锥形贮水池, 深 15 m, 口径 20 m, 盛满水, 今以泵将水吸尽, 问要做多少功?

7. 有一铅直放置的矩形闸门, 它的顶端与水面相平, 一条对角线将闸门分成两个三角形区域. 试证: 其中一个三角形区域上所受的水压力是另一个三角形区域上所受水压力的 2 倍.

8. 有一等腰梯形闸门, 它的两条底边各长 $10 \mathrm{~m}$ 和 $6 \mathrm{~m}$ , 高为 $20 \mathrm{~m}$ . 较长的底边与水面相齐. 计算闸门的一侧所受的水压力.

9. 一底为 8 cm、高为 6 cm 的等腰三角形片, 铅直地沉没在水中, 顶在上, 底在下且与水面平行, 而顶离水面 3 cm, 试求它每面所受的压力.

10. 设有一长度为 $l$ 、线密度为 $\mu$ 的均匀细直棒，在与棒的一端垂直距离为 $a$ 单位处有一质量为

m 的质点 M, 试求这细棒对质点 M 的引力.

11. 设有一半径为 R、圆心角为 $\varphi$ 的圆弧形细棒，其线密度为常数 $\mu_{n}$ 在圆心处有一质量为 m 的质点 M。试求这细棒对质点 M 的引力。

# 总习题六

1. 填空：

(1) 曲线 $y=x^{3}-5x^{2}+6x$ 与 x 轴所围成的图形的面积 A= ____；

(2) 曲线 $y=\frac{\sqrt{x}}{3}(3-x)$ 上相应于 $1 \leqslant x \leqslant 3$ 的一段弧的长度 s= ____.

2. 以下三题中均给出了四个结论,从中选出一个正确的结论:

（1）设 x 轴上有一长度为 l、线密度为常数 $\mu$ 的细棒，在与细棒右端的距离为 a 处有一质量为 m 的质点 M（图 6-33），已知引力常量为 G，则质点 M 与细棒之间的引力的大小为（）；

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/bac400ad4ffcb142912ad3f0c765ad8f600be5a5e920f3fb2cdbb7ce4fce4543.jpg)



图6-33


(A) $\int_{-l}^{0}\frac{Gm\mu}{(a - x)^2}\mathrm{d}x$ 

(B) $\int_0^l\frac{Gm\mu}{(a - x)^2}\mathrm{d}x$ 

(C) $2\int_{-\frac{l}{2}}^{0}\frac{Gm\mu}{(a - x)^{2}}\mathrm{d}x$ 

(D) $2\int_{0}^{\frac{l}{2}}\frac{Gm\mu}{(a - x)^{2}}\mathrm{d}x$ 

（2）设在区间 $[a,b]$ 上， $f(x) > 0, f'(x) > 0, f''(x) < 0.$ 令 $A_{1} = \int_{a}^{b} f(x) \mathrm{d}x, A_{2} = f(a)(b - a), A_{3} = \frac{1}{2} [f(a) + f(b)] (b - a)$ ，则有（ ）；

(A) $A_{1}<A_{2}<A_{3}$ 

(B) $A_{2}<A_{1}<A_{3}$ 

(C) $A_{3}<A_{1}<A_{2}$ 

(D) $A_{2} < A_{3} < A_{1}$ 

（3）有半径不相等的两个木质球体，分别在中间钻出一个以球体直径为轴的圆柱形洞，使得剩下的两个环状立体的高都等于 $h$ （图6-34).假设对应木质球半径较大的环状立体为 $P$ ，另一个为 $Q.$ 通过计算，正确的结论是( ).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/dd902af5f4dc8dca59208e59672c165fa8df89f948e07e23c68811a98f022599.jpg)



图6-34


(A) P 的体积大于 Q 的体积

(B) P 的体积等于 Q 的体积

(C) P 的体积小于 Q 的体积

(D) 在 h 的不同取值范围, P 与 Q 的体积有不同的大小关系

3. 一金属棒长 $3 \mathrm{~m}$ , 离棒左端 $x \mathrm{~m}$ 处的线密度为 $\mu(x) = \frac{1}{\sqrt{x + 1}} \mathrm{~kg} / \mathrm{m}$ . 问 $x$ 为何值时, $[0, x]$ 一段的质量为全棒质量的一半?

4. 求由曲线 $\rho = a \sin \theta, \rho = a (\cos \theta + \sin \theta) (a > 0)$ 所围图形公共部分的面积.

5. 如图 6-35 所示, 从下到上依次有三条曲线: $y = x^2$ , $y = 2x^2$ 和 C. 假设对曲线 $y = 2x^2$ 上的任一点

P,所对应的面积A和B恒相等,求曲线C的方程.

6. 设抛物线 $y=ax^{2}+bx+c$ ( $a\neq0$ ) 通过点 $(0,0)$ ，且当 $x\in[0,1]$ 时， $y\geqslant0$ 。试确定 a, b, c 的值，使得抛物线 $y=ax^{2}+bx+c$ 与直线 x=1，y=0 所围图形的面积为 $\frac{4}{9}$ ，且使该图形绕 x 轴旋转而成的旋转体的体积最小。

7. 过坐标原点作曲线 $y=\ln x$ 的切线, 该切线与曲线 $y=\ln x$ 及 x 轴围成平面图形 D.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/c046cba35894a4bb225371e2b0c62f443f7c32b476c595be2ae256adbfa8194a.jpg)



图6-35


(1) 求平面图形 D 的面积 A;

(2) 求平面图形 D 绕直线 x=e 旋转一周所得旋转体的体积 V.

8. 设曲线 $C$ 为函数 $y = x\mathrm{e}^{-x}$ ( $x \geqslant 0$ ) 的图形, $M(x_0, y_0)$ 为 $C$ 上的一个拐点, $MT$ 为曲线 $C$ 在点 $M$ 处的切线. 求由曲线 $C$ 、切线 $MT$ 和 $x$ 轴所围的向右无限延伸的平面图形的面积.

9. 求由曲线 $y=x^{\frac{3}{2}}$ ，直线 x=4 及 x 轴所围图形绕 y 轴旋转而成的旋转体的体积.

10. 求圆盘 $(x-2)^{2}+y^{2}\leqslant1$ 绕 y 轴旋转而成的旋转体的体积.

11. 求抛物线 $y=\frac{1}{2}x^{2}$ 被圆 $x^{2}+y^{2}=3$ 所截下的有限部分的弧长.

12. 半径为 r 的球沉入水中, 球的上部与水面相切, 球的密度与水相同, 现将球从水中取出, 需做多少功?

13. 边长为 a 和 b 的矩形薄板, 与液面成 $\alpha$ 角斜沉于液体内, 长边平行于液面而位于深 h 处, 设 a > b, 液体的密度为 $\rho$ , 试求薄板每面所受的压力.

14. 设星形线 $x = a \cos^{3} t, y = a \sin^{3} t$ 上每一点处的线密度的大小等于该点到原点距离的立方，在原点 O 处有一单位质点，求星形线在第一象限的弧段对这质点的引力.

15. 某建筑工程打地基时,需用汽锤将桩打进土层.汽锤每次击打,都要克服土层对桩的阻力做功.设土层对桩的阻力的大小与桩被打进地下的深度成正比(比例系数为 k,k>0).汽锤第一次击打将桩打进地下 a m.根据设计方案,要求汽锤每次击打桩时所做的功与前一次击打时所做的功之比为常数 r (0<r<1).问

(1) 汽锤击打桩 3 次后, 可将桩打进地下多深?

(2) 若击打次数不限,则汽锤至多能将桩打进地下多深?

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/c114bddb040e16016eb96b979de349687b1ed912a49fda14558a8bd7079bf21b.jpg)



第六章释疑解难


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/1d9fc87337a3b9694de0e1c7acbb438b2b87bf1da4a6dfa8cd4c192298fd5f08.jpg)



第六章例题精讲


# 第七章

# 微分方程

函数是客观事物的内部联系在数量方面的反映,利用函数关系又可以对客观事物的规律性进行研究.因此如何寻求函数关系,在实践中具有重要意义.在许多问题中,往往不能直接找出所需要的函数关系,但是根据问题所提供的情况,有时可以列出含有要找的函数及其导数的关系式.这样的关系式就是所谓微分方程.微分方程建立以后,对它进行研究,求出未知函数,这就是解微分方程.本章主要介绍微分方程的一些基本概念和几种常用的微分方程的解法.

# 第一节 微分方程的基本概念

下面我们通过几何、力学及物理学中的几个具体例题来说明微分方程的基本概念.

例 1 一曲线通过点 $(1,2)$ ，且在该曲线上任一点 $M(x,y)$ 处的切线的斜率为 2x，求这曲线的方程.

解 设所求曲线的方程为 $y=\varphi(x)$ . 根据导数的几何意义, 可知未知函数 $y=\varphi(x)$ 应满足关系式

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = 2 x. \tag {1-1}
$$

此外,未知函数 $y=\varphi(x)$ 还应满足下列条件:

$$
x = 1 \text {   时,   } y = 2. \tag {1-2}
$$

把(1-1)式两端积分, 得 $y = \int 2x dx$ 即

$$
y = x ^ {2} + C, \tag {1-3}
$$

其中 C 是任意常数.

把条件“x=1 时, y=2”代入(1-3)式, 得

$$
2 = 1 ^ {2} + C,
$$

由此定出 C=1. 把 C=1 代入 $(1-3)$ 式, 即得所求曲线方程

$$
y = x ^ {2} + 1. \tag {1-4}
$$

例 2 列车沿直线以 20 m/s（相当于 72 km/h）的速度行驶，当制动时列车获得加速度 $-0.4 \, m/s^{2}$ . 问开始制动后多少时间列车才能停住以及列车在这段时间里行驶了多少路程？

解 设列车在开始制动后 t s 时行驶了 s m. 根据题意, 反映制动阶段列车运动规律的函数 $s = s(t)$ 应满足关系式

$$
\frac {\mathrm{d} ^ {2} s}{\mathrm{d} t ^ {2}} = - 0. 4. \tag {1-5}
$$

此外,未知函数 $s=s(t)$ 还应满足下列条件:

$$
t = 0 \text {   时,   } s = 0, v = \frac {\mathrm{d} s}{\mathrm{d} t} = 2 0. \tag {1-6}
$$

把(1-5)式两端积分一次,得

$$
v = \frac {\mathrm{d} s}{\mathrm{d} t} = - 0. 4 t + C _ {1}, \tag {1-7}
$$

再积分一次,得

$$
s = - 0. 2 t ^ {2} + C _ {1} t + C _ {2}, \tag {1-8}
$$

这里 $C_{1}, C_{2}$ 都是任意常数.

把条件“t=0 时, v=20”代入(1-7)式, 得

$$
2 0 = C _ {1},
$$

把条件“t=0 时, s=0”代入(1-8)式, 得

$$
0 = C _ {2}.
$$

把 $C_{1}, C_{2}$ 的值代入(1-7)及(1-8)式, 得

$$
v = - 0. 4 t + 2 0, \tag {1-9}
$$

$$
s = - 0. 2 t ^ {2} + 2 0 t. \tag {1-10}
$$

在(1-9)式中令 v=0，得到列车从开始制动到完全停住所需的时间

$$
t = \frac {2 0}{0 . 4} = 5 0 (\mathrm{s}).
$$

再把 t=50 代入(1-10)式, 得到列车在制动阶段行驶的路程

$$
s = - 0. 2 \times 5 0 ^ {2} + 2 0 \times 5 0 = 5 0 0 (\mathrm{m}).
$$

上述两个例子中的关系式(1-1)和(1-5)都含有未知函数的导数,它们都是微分方程.一般地,凡表示未知函数、未知函数的导数与自变量之间的关系的方程,叫做微

分方程,有时也简称方程.

微分方程中所出现的未知函数的最高阶导数的阶数,叫做微分方程的阶.例如,方程(1-1)是一阶微分方程,方程(1-5)是二阶微分方程.又如,方程

$$
x ^ {3} y ^ {\prime \prime \prime} + x ^ {2} y ^ {\prime \prime} - 4 x y ^ {\prime} = 3 x ^ {2}
$$

是三阶微分方程,方程

$$
y ^ {(4)} - 4 y ^ {\prime \prime \prime} + 1 0 y ^ {\prime \prime} - 1 2 y ^ {\prime} + 5 y = \sin 2 x
$$

是四阶微分方程.

一般地， $n$ 阶微分方程的形式是

$$
F (x, y, y ^ {\prime}, \dots , y ^ {(n)}) = 0. \tag {1-11}
$$

这里必须指出,在方程(1-11)中, $y^{(n)}$ 是必须出现的,而 $x,y,y',\cdots,y^{(n-1)}$ 等则可以不出现.例如n阶微分方程

$$
y ^ {(n)} + 1 = 0
$$

中,除 $y^{(n)}$ 外,y 的其他阶导数和自变量 x 都没有出现.

如果能从方程(1-11)中解出最高阶导数,那么可得微分方程

$$
y ^ {(n)} = f (x, y, y ^ {\prime}, \dots , y ^ {(n - 1)}). \tag {1-12}
$$

以后我们讨论的微分方程都是已解出最高阶导数的方程或能解出最高阶导数的方程.

由前面的例子我们看到,在研究某些实际问题时,首先要建立微分方程,然后找出满足微分方程的函数(解微分方程),就是说,找出这样的函数,把这函数代入微分方程能使该方程成为恒等式.这个函数就叫做该微分方程的解.确切地说,设函数 $y=\varphi(x)$ 在区间 I 上有 n 阶连续导数,如果在区间 I 上,

$$
f [ x, \varphi (x), \varphi^ {\prime} (x), \dots , \varphi^ {(n)} (x) ] \equiv 0,
$$

那么函数 $y=\varphi(x)$ 就叫做微分方程(1-11)在区间 I 上的解.

例如,函数(1-3)和(1-4)都是微分方程(1-1)的解,函数(1-8)和(1-10)都是微分方程(1-5)的解.

如果微分方程的解中含有任意常数,且任意常数的个数与微分方程的阶数相同①,这样的解叫做微分方程的通解.例如,函数(1-3)是方程(1-1)的解,它含有1个任意常数,而方程(1-1)是一阶的,所以函数(1-3)是方程(1-1)的通解.又如,函数(1-8)是方程(1-5)的解,它含有2个任意常数,而方程(1-5)是二阶的,所以函数(1-8)是方程(1-5)的通解.

由于通解中含有任意常数,所以它还不能完全确定地反映函数所代表的某一个客观事物的规律性.要完全确定地反映客观事物的规律性,必须确定这些常数的值.为

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/7249c5ec8d62000bbecfb80c5b2377a2d195fb958502a9242eb3a3da9ab28f60.jpg)


释疑解难

7-1 

此,要根据问题的实际情况,提出确定这些常数的条件.例如,例1中的条件(1-2)及例2中的条件(1-6)便是这样的条件.

设微分方程中的未知函数为 $y=\varphi(x)$ ，如果微分方程是一阶的，通常用来确定任意常数的条件是

$$
x = x _ {0} \text {时}, \quad y = y _ {0},
$$

或写成

$$
y \mid_ {x = x _ {0}} = y _ {0},
$$

其中 $x_0, y_0$ 都是给定的值；如果微分方程是二阶的，通常用来确定任意常数的条件是

$$
x = x _ {0} \text {时}, \quad y = y _ {0}, \quad y ^ {\prime} = y _ {0} ^ {\prime},
$$

或写成

$$
y \mid_ {x = x _ {0}} = y _ {0}, \quad y ^ {\prime} \mid_ {x = x _ {0}} = y _ {0} ^ {\prime},
$$

其中 $x_{0}, y_{0}$ 和 $y_{0}^{\prime}$ 都是给定的值. 上述这种条件叫做初值条件.

确定了通解中的任意常数以后, 就得到微分方程的特解. 例如 (1-4) 式是方程 (1-1) 满足条件 (1-2) 的特解, (1-10) 式是方程 (1-5) 满足条件 (1-6) 的特解.

求微分方程 $y' = f(x, y)$ 满足初值条件 $y \mid_{x = x_0} = y_0$ 的特解这样一个问题，叫做一阶微分方程的初值问题，记作

$$
\left\{ \begin{array}{l} y ^ {\prime} = f (x, y), \\ y \mid_ {x = x _ {0}} = y _ {0}. \end{array} \right. \tag {1-13}
$$

微分方程的解的图形是一条曲线,叫做微分方程的积分曲线.初值问题(1-13)的几何意义,就是求微分方程的通过点 $(x_{0},y_{0})$ 的那条积分曲线.二阶微分方程的初值问题

$$
\left\{ \begin{array}{l} y ^ {\prime \prime} = f (x, y, y ^ {\prime}), \\ y \mid_ {x = x _ {0}} = y _ {0}, y ^ {\prime} \mid_ {x = x _ {0}} = y _ {0} ^ {\prime} \end{array} \right.
$$

的几何意义,是求微分方程的通过点 $(x_{0},y_{0})$ 且在该点处的切线斜率为 $y_{0}^{\prime}$ 的那条积分曲线.

例 3 验证: 函数

$$
x = C _ {1} \cos k t + C _ {2} \sin k t \tag {1-14}
$$

是微分方程

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} + k ^ {2} x = 0 \tag {1-15}
$$

的解.

解 求出所给函数(1-14)的导数

$$
\frac {\mathrm{d} x}{\mathrm{d} t} = - k C _ {1} \sin k t + k C _ {2} \cos k t, \tag {1-16}
$$

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} = - k ^ {2} C _ {1} \cos k t - k ^ {2} C _ {2} \sin k t = - k ^ {2} (C _ {1} \cos k t + C _ {2} \sin k t).
$$

把 $\frac{\mathrm{d}^2x}{\mathrm{d}t^2}$ 及 $x$ 的表达式代入方程(1-15)，得

$$
- k ^ {2} \left(C _ {1} \cos k t + C _ {2} \sin k t\right) + k ^ {2} \left(C _ {1} \cos k t + C _ {2} \sin k t\right) \equiv 0.
$$

函数(1-14)及其二阶导数代入方程(1-15)后成为一个恒等式,因此函数(1-14)是微分方程(1-15)的解.

例 4 已知函数(1-14)当 $k \neq 0$ 时是微分方程(1-15)的通解, 求满足初值条件

$$
x \mid_ {t = 0} = A, \quad \frac {\mathrm{d} x}{\mathrm{d} t} \Big | _ {t = 0} = 0
$$

的特解.

解 将条件“t=0 时, x=A”代入(1-14)式得

$$
C _ {1} = A.
$$

将条件“t=0 时, $\frac{dx}{dt}=0$ ”代入(1-16)式,得

$$
C _ {2} = 0.
$$

把 $C_{1}, C_{2}$ 的值代入(1-14)式, 就得所求的特解

$$
x = A \cos k t.
$$

# 习题7-1

1. 试说出下列各微分方程的阶数：

(1) $x(y')^2 - 2yy' + x = 0$ ; 

(2) $x^{2}y''-xy'+y=0;$ 

(3) $xy''' + 2y'' + x^{2}y = 0;$ 

(4) $(7x-6y)\mathrm{d}x+(x+y)\mathrm{d}y=0;$ 

(5) $L\frac{d^{2}Q}{dt^{2}}+R\frac{dQ}{dt}+\frac{Q}{C}=0;$ 

(6) $\frac{\mathrm{d}\rho}{\mathrm{d}\theta} + \rho = \sin^2\theta.$ 

2. 指出下列各题中的函数是不是所给微分方程的解：

(1) $xy' = 2y, y = 5x^2;$ 

(2) $y''+y=0,y=3\sin x-4\cos x;$ 

(3) $y''-2y'+y=0,y=x^{2}e^{x};$ 

(4) $y''-(\lambda_1+\lambda_2)y'+\lambda_1\lambda_2y=0,y=C_1e^{\lambda_1x}+C_2e^{\lambda_2x}.$ 

3. 在下列各题中,验证所给二元方程所确定的函数为所给微分方程的解:

(1) $(x-2y)y'=2x-y,x^{2}-xy+y^{2}=C;$ 

(2) $(xy - x)y'' + xy'^{2} + yy' - 2y' = 0, y = \ln(xy).$ 

4. 在下列各题中, 确定函数关系式中所含的参数, 使函数满足所给的初值条件:

(1) $x^{2} - y^{2} = C, y \mid_{x=0} = 5$ ; 

(2) $y = (C_1 + C_2x)e^{2x}, y \big|_{x=0} = 0, y' \big|_{x=0} = 1;$ 

(3) $y = C_{1}\sin (x - C_{2}), y \big|_{x=\pi} = 1, y' \big|_{x=\pi} = 0.$ 

5. 写出由下列条件确定的曲线所满足的微分方程：

(1) 曲线在点 $(x,y)$ 处的切线的斜率等于该点横坐标的平方；

(2) 曲线上点 $P(x,y)$ 处的法线与 x 轴的交点为 Q，且线段 PQ 被 y 轴平分；

(3) 曲线上点 $P(x,y)$ 处的切线与 y 轴的交点为 Q，线段 PQ 的长度为 a，且曲线通过点 $(a,0)$ .

6. 用微分方程表示一物理命题: 某种气体的压强 p 对于温度 T 的变化率与压强成正比, 与温度的平方成反比.

7. 一个半球体形状的雪堆, 其体积融化率与半球面面积 A 成正比, 比例系数 k > 0. 假设在融化过程中雪堆始终保持半球体形状, 已知半径为 $r_{0}$ 的雪堆在开始融化的 3 h 内, 融化了其体积的 $\frac{7}{8}$ , 问雪堆全部融化需要多少时间?

# 第二节 可分离变量的微分方程

本节至第四节,我们讨论一阶微分方程

$$
y ^ {\prime} = f (x, y) \tag {2-1}
$$

的一些解法.

一阶微分方程有时也写成如下的对称形式：

$$
P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y = 0. \tag {2-2}
$$

在方程(2-2)中,变量 x 与 y 对称,它既可看作是以 x 为自变量 y 为因变量的方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = - \frac {P (x , y)}{Q (x , y)}
$$

(这时 $Q(x,y)\neq0$ )，也可看作是以 y 为自变量 x 为因变量的方程

$$
\frac {\mathrm{d} x}{\mathrm{d} y} = - \frac {Q (x , y)}{P (x , y)}
$$

(这时 $P(x,y) \neq 0$ ).

在第一节的例 1 中,我们遇到一阶微分方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = 2 x,
$$

或

$$
\mathrm{d} y = 2 x \mathrm{d} x.
$$

把上式两端积分就得到这个方程的通解

$$
y = x ^ {2} + C.
$$

但是并不是所有的一阶微分方程都能这样求解.例如,对于一阶微分方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = 2 x y ^ {2}, \tag {2-3}
$$

就不能像上面那样用直接对两端积分的方法求出它的通解.这是什么缘故呢？原因是方程(2-3)的右端含有与 $x$ 存在函数关系的变量 $\gamma$ ，积分

$$
\int 2 x y ^ {2} \mathrm{d} x
$$

求不出来,这是困难所在.为了解决这个困难,在方程(2-3)的两端同时乘 $\frac{dx}{y^{2}}$ ,使方程(2-3)变为

$$
\frac {\mathrm{d} y}{y ^ {2}} = 2 x \mathrm{d} x,
$$

这样, 变量 x 与 y 已分离在等式的两端, 然后两端积分得

$$
- \frac {1}{y} = x ^ {2} + C,
$$

或

$$
y = - \frac {1}{x ^ {2} + C}, \tag {2-4}
$$

其中 C 是任意常数.

可以验证,函数(2-4)确实满足一阶微分方程(2-3),且含有一个任意常数,所以它是方程(2-3)的通解.

一般地,如果一个一阶微分方程能写成

$$
g (y) \mathrm{d} y = f (x) \mathrm{d} x \tag {2-5}
$$

的形式, 就是说, 能把微分方程写成一端只含 y 的函数和 dy, 另一端只含 x 的函数和 dx, 那么原方程就称为可分离变量的微分方程.

假定方程(2-5)中的函数 $g(y)$ 和 $f(x)$ 是连续的. 设 $y = \varphi(x)$ 是方程(2-5)的解，将它代入(2-5)中得到恒等式

$$
g [ \varphi (x) ] \varphi^ {\prime} (x) \mathrm{d} x = f (x) \mathrm{d} x.
$$

将上式两端积分,并由 $y=\varphi(x)$ 引进变量 y, 得

$$
\int g (y) \mathrm{d} y = \int f (x) \mathrm{d} x.
$$

设 $G(y)$ 及 $F(x)$ 依次为 $g(y)$ 及 $f(x)$ 的原函数，于是有

$$
G (y) = F (x) + C. \tag {2-6}
$$

因此,方程(2-5)的解满足关系式(2-6).反之,如果 $y=\Phi(x)$ 是由关系式(2-6)所确定的隐函数,那么在 $g(y) \neq 0$ 的条件下, $y = \Phi(x)$ 也是方程(2-5)的解,事实上,由隐函数的求导法可知,当 $g(y) \neq 0$ 时,

$$
\Phi^ {\prime} (x) = \frac {F ^ {\prime} (x)}{G ^ {\prime} (y)} = \frac {f (x)}{g (y)},
$$

这就表示函数 $y=\Phi(x)$ 满足方程(2-5). 所以, 如果已分离变量的方程(2-5)中, $g(y)$ 和 $f(x)$ 是连续的, 且 $g(y)\neq0$ , 那么(2-5)式两端积分后得到的关系式(2-6), 就用隐式给出了方程(2-5)的解, (2-6)式就叫做微分方程(2-5)的隐式解. 又由于关系式(2-6)中含有任意常数, 因此(2-6)式所确定的隐函数是方程(2-5)的通解, 所以(2-6)式叫做微分方程(2-5)的隐式通解(当 $f(x)\neq0$ 时, (2-6)式所确定的隐函数 $x=\Psi(y)$ 也可认为是方程(2-5)的解).

例1 求微分方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = 2 x y \tag {2-7}
$$

的通解.

解 方程(2-7)是可分离变量的,分离变量后得

$$
\frac {\mathrm{d} y}{y} = 2 x \mathrm{d} x,
$$

两端积分

$$
\int \frac {\mathrm{d} y}{y} = \int 2 x \mathrm{d} x,
$$

得

$$
\ln | y | = x ^ {2} + C _ {1},
$$

从而

$$
y = \pm \mathrm{e} ^ {x ^ {2} + C _ {1}} = \pm \mathrm{e} ^ {C _ {1}} \mathrm{e} ^ {x ^ {2}}.
$$

因 $\pm \mathrm{e}^{C_1}$ 是任意非零常数，又 $y\equiv 0$ 也是方程(2-7)的解，故得方程(2-7)的通解

$$
y = C \mathrm{e} ^ {x ^ {2}},
$$

其中 C 为任意常数.

例 2 放射性元素铀由于不断地有原子放射出微粒子而变成其他元素,铀的含量就不断减少,这种现象叫做衰变.由原子物理学知道,铀的衰变速度与当时未衰变的铀原子的含量 M 成正比.已知 t=0 时铀的含量为 $M_{0}$ ,求在衰变过程中铀含量 $M(t)$ 随时间 t 变化的规律.

解 铀的衰变速度就是 $M(t)$ 对时间 t 的导数 $\frac{dM}{dt}$ . 由于铀的衰变速度与其含量成正比, 故得微分方程

$$
\frac {\mathrm{d} M}{\mathrm{d} t} = - \lambda M, \tag {2-8}
$$

其中 $\lambda (\lambda > 0)$ 是常数, 叫做衰变系数, $\lambda$ 前置负号是由于当 t 增加时 M 单调减少, 即 $\frac{dM}{dt} < 0$ 的缘故.

按题意,初值条件为

$$
M \mid_ {t = 0} = M _ {0}.
$$

方程(2-8)是可分离变量的.分离变量后得

$$
\frac {\mathrm{d} M}{M} = - \lambda \mathrm{d} t.
$$

两端积分

$$
\int \frac {\mathrm{d} M}{M} = \int (- \lambda) \mathrm{d} t,
$$

以 $\ln C$ 表示任意常数, 考虑到 M>0, 得

$$
\ln M = - \lambda t + \ln C,
$$

即

$$
M = C \mathrm{e} ^ {- \lambda t}.
$$

这就是方程(2-8)的通解.以初值条件代入上式,得

$$
M _ {0} = C \mathrm{e} ^ {0} = C,
$$

所以

$$
M = M _ {0} \mathrm{e} ^ {- \lambda t},
$$

这就是所求铀的衰变规律.由此可见,铀的含量随时间的增加而按指数规律衰减(图7-1).

例 3 跳伞人从跳伞塔跳下后, 假设降落伞同时打开, 且所受空气阻力与速度成正比, 并设降落伞离开跳伞塔时 $(t=0)$ 速度为零, 求降落伞下落速度与时间的函数关系.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/60638bf31696c00f2a306effaca32068732526fe45b25eca3f0069d5235c8f60.jpg)



图7-1


解 设降落伞下落速度为 $v(t)$ . 降落伞在空中下落
时, 同时受到重力 P 与阻力 R 的作用(图 7-2). 重力大小为 mg, 方向与 v 一致; 阻力大小为 kv (k 为比例系数), 方向与 v 相反, 从而降落伞所受外力为

$$
F = m g - k v.
$$

根据牛顿第二运动定律

$$
F = m a
$$

(其中 a 为加速度), 得函数 $v(t)$ 应满足的方程为

$$
m \frac {\mathrm{d} v}{\mathrm{d} t} = m g - k v. \tag {2-9}
$$

按题意,初值条件为

$$
v \mid_ {t = 0} = 0.
$$

方程(2-9)是可分离变量的.分离变量后得

$$
\frac {\mathrm{d} v}{m g - k v} = \frac {\mathrm{d} t}{m},
$$

两端积分

$$
\int \frac {\mathrm{d} v}{m g - k v} = \int \frac {\mathrm{d} t}{m},
$$

考虑到 $mg - kv > 0$ ，得

$$
- \frac {1}{k} \ln (m g - k v) = \frac {t}{m} + C _ {1},
$$

即

$$
m g - k v = \mathrm{e} ^ {- \frac {k}{m} t - k C _ {1}},
$$

或

$$
v = \frac {m g}{k} + C \mathrm{e} ^ {- \frac {k}{m} t} \quad \left(C = - \frac {\mathrm{e} ^ {- k C _ {1}}}{k}\right), \tag {2-10}
$$

这就是方程(2-9)的通解.

将初值条件 $v|_{t = 0} = 0$ 代入(2-10)式，得

$$
C = - \frac {m g}{k}.
$$

于是所求的特解为

$$
v = \frac {m g}{k} (1 - \mathrm{e} ^ {- \frac {k}{m} t}). \tag {2-11}
$$

由(2-11)可以看出,随着时间 t 的增大,速度 v 逐渐接近于常数 $\frac{mg}{k}$ ,且不会超过 $\frac{mg}{k}$ ,也就是说,跳伞后开始阶段是加速运动,但以后逐渐接近于等速运动.

例 4 有高为 1 m 的半球形容器, 水从它的底部小孔流出, 小孔横截面面积为 $1 \, cm^{2}$ (图 7-3). 开始时容器内盛满了水, 求水从小孔流出过程中容器里水面的高度 h (水面与孔口中心间的距离) 随时间 t 变化的规律, 并求水流完所需的时间.

解 由力学知道,水从孔口流出的流量(即通过孔口横截面的水的体积 V 对时间 t 的变化率)Q 可用下列公式计算:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/69f032dfd4a98fd0680bf2116063d5d317e457d685adb76da2e751bb6327ed36.jpg)



图7-2


$$
Q = \frac {\mathrm{d} V}{\mathrm{d} t} = k S \sqrt {2 g h}, \tag {2-12}
$$

其中 k 为流量系数,由实验测得 k=0.62,S 为孔口横截面面积,g 为重力加速度.

另一方面,设在微小时间间隔 $[t,t+dt]$ 内,水面高度由h降至 $h+dh(dh<0)$ ,则又可得到

$$
\mathrm{d} V = - \pi r ^ {2} \mathrm{d} h, \tag {2-13}
$$

其中 r 是时刻 t 时的水面半径(图 7-3)，右端置负号是由于 dh<0 而 dV>0 的缘故. 又因

$$
r = \sqrt {1 ^ {2} - (1 - h) ^ {2}} = \sqrt {2 h - h ^ {2}},
$$

所以(2-13)式变成

$$
\mathrm{d} V = - \pi (2 h - h ^ {2}) \mathrm{d} h. \tag {2-14}
$$

比较(2-12)和(2-14)两式,得

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/838c0eca6be72d4c70881b9f6dbb155688612954c2f33f18c7b94482348974f6.jpg)



图7-3


$$
k S \sqrt {2 g h} \mathrm{d} t = - \pi (2 h - h ^ {2}) \mathrm{d} h, \tag {2-15}
$$

这就是未知函数 $h=h(t)$ 应满足的微分方程.

此外,开始时容器内的水是满的,所以未知函数 $h=h(t)$ 还应满足下列初值条件:

$$
h \mid_ {t = 0} = 1. \tag {2-16}
$$

方程(2-15)是可分离变量的.分离变量后得

$$
\mathrm{d} t = - \frac {\pi}{k S \sqrt {2 g}} (2 h ^ {\frac {1}{2}} - h ^ {\frac {3}{2}}) \mathrm{d} h.
$$

两端积分,得

$$
t = - \frac {\pi}{k S \sqrt {2 g}} \left(\frac {4}{3} h ^ {\frac {3}{2}} - \frac {2}{5} h ^ {\frac {5}{2}} + C\right), \tag {2-17}
$$

其中 C 是任意常数.

把初值条件(2-16)代入(2-17)式,得

$$
C = - \frac {4}{3} + \frac {2}{5} = - \frac {1 4}{1 5}.
$$

把所得的 C 值代入(2-17)式并化简,就得

$$
t = \frac {1 4 \pi}{1 5 k S \sqrt {2 g}} \left(1 - \frac {1 0}{7} h ^ {\frac {3}{2}} + \frac {3}{7} h ^ {\frac {5}{2}}\right).
$$

以 $k = 0.62, S = 10^{-4} \mathrm{~m}^2, g = 9.8 \mathrm{~m} / \mathrm{s}^2$ 代入上式，计算后可得

$$
t = 1. 0 6 8 \times 1 0 ^ {4} \left(1 - \frac {1 0}{7} h ^ {\frac {3}{2}} + \frac {3}{7} h ^ {\frac {5}{2}}\right) \mathrm{s}.
$$

上式表达了水从小孔流出的过程中容器内水面高度 h 与时间 t 之间的函数关系. 由此可知水流完所需的时间为

$$
t = 1. 0 6 8 \times 1 0 ^ {4} \mathrm{s} = 2 \mathrm{h} 5 8 \min.
$$

[Document Icon] 

释疑解难

7-2 

这里还要指出,在例4中我们是通过对微小量dV的分析得到微分方程(2-15)的.这种微小量分析的方法,也是建立微分方程的一种常用方法.

# 习题7-2

1. 求下列微分方程的通解：

(1) $xy' - y \ln y = 0;$ 

(2) $3x^{2}+5x-5y'=0;$ 

(3) $\sqrt{1 - x^2} y' = \sqrt{1 - y^2}$ ; 

(4) $y' - xy' = a(y^2 + y')$ ; 

(5) $\sec^{2}x\tan ydx+\sec^{2}y\tan xdy=0;$ 

(6) $\frac{\mathrm{dy}}{\mathrm{dx}} = 10^{x + y}$ ; 

(7) $(\mathrm{e}^{x + y} - \mathrm{e}^x)\mathrm{d}x + (\mathrm{e}^{x + y} + \mathrm{e}^y)\mathrm{d}y = 0;$ 

(8) $\cos x \sin y dx + \sin x \cos y dy = 0;$ 

(9) $(y+1)^{2}\frac{\mathrm{d}y}{\mathrm{d}x}+x^{3}=0;$ 

(10) $y\mathrm{d}x + (x^2 - 4x)\mathrm{d}y = 0.$ 

2. 求下列微分方程满足所给初值条件的特解：

(1) $y' = e^{2x - y}, y \mid_{x=0} = 0;$ 

(2) $\cos x \sin y \, \mathrm{d}y = \cos y \sin x \, \mathrm{d}x, y \mid_{x=0} = \frac{\pi}{4}$ ; 

(3) $y'\sin x=y\ln y,y\mid_{x=\frac{\pi}{2}}=e;$ 

(4) $\cos y\mathrm{d}x + (1 + e^{-x})\sin y\mathrm{d}y = 0, y \mid_{x=0} = \frac{\pi}{4};$ 

(5) $x \, dy + 2y \, dx = 0, y \mid_{x=2} = 1;$ 

(6) $\frac{1}{\rho}\frac{\mathrm{d}\rho}{\mathrm{d}\theta} + \frac{\rho^2 + 1}{\rho^2 - 1}\cot \theta = 0, \rho \mid_{\theta = \frac{\pi}{6}} = 3;$ 

(7) $x^{2}(1 + y'^{2}) = a^{2},y\mid_{x = a} = 0$ ，其中 $a > 0$ 

3. 有一盛满了水的圆锥形漏斗, 高为 $10 \, cm$ , 顶角为 $60^{\circ}$ , 漏斗下面有面积为 $0.5 \, cm^{2}$ 的孔, 求水面高度变化的规律及水流完所需的时间.

4. 质量为 1 g 的质点受外力作用做直线运动, 这外力和时间成正比, 和质点运动的速度成反比. 在 t=10 s 时, 速度等于 50 cm/s, 外力为 $4 \, g \cdot cm/s^{2}$ , 问从运动开始经过了 1 min 后的速度是多少?

5. 镭的衰变有如下的规律: 镭的衰变速度与它的现存量 R 成正比. 由经验材料得知, 镭经过 1600 年后, 只余原始量 $R_{0}$ 的一半. 试求镭的现存量 R 与时间 t 的函数关系.

6. 一曲线通过点(2,3)，它在两坐标轴间的任一切线线段均被切点所平分，求这曲线方程.

7. 小船从河边点 O 处出发驶向对岸(两岸为平行直线). 设船速为 a, 小船航行的方向始终与河岸垂直, 又设河宽为 h, 河中任一点处的水流速度与该点到两岸距离的乘积成正比(比例系数为 k). 求小船的航行路线.

# 第三节 齐次方程

# 一、齐次方程

如果一阶微分方程可化成

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \varphi \left(\frac {y}{x}\right) \tag {3-1}
$$

的形式,那么就称这方程为齐次方程,例如

$$
(x y - y ^ {2}) \mathrm{d} x - (x ^ {2} - 2 x y) \mathrm{d} y = 0
$$

是齐次方程,因为它可化成

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {x y - y ^ {2}}{x ^ {2} - 2 x y},
$$

即

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {\frac {y}{x} - \left(\frac {y}{x}\right) ^ {2}}{1 - 2 \left(\frac {y}{x}\right)}.
$$

在齐次方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \varphi \left(\frac {y}{x}\right)
$$

中,引进新的未知函数

$$
u = \frac {y}{x}, \tag {3-2}
$$

就可把它化为可分离变量的方程.因为由(3-2)有

$$
y = u x, \quad \frac {\mathrm{d} y}{\mathrm{d} x} = u + x \frac {\mathrm{d} u}{\mathrm{d} x},
$$

代入方程(3-1)，便得方程

$$
u + x \frac {\mathrm{d} u}{\mathrm{d} x} = \varphi (u),
$$

即

$$
x \frac {\mathrm{d} u}{\mathrm{d} x} = \varphi (u) - u.
$$

分离变量,得

$$
\frac {\mathrm{d} u}{\varphi (u) - u} = \frac {\mathrm{d} x}{x}.
$$

两端积分,得

$$
\int \frac {\mathrm{d} u}{\varphi (u) - u} = \int \frac {\mathrm{d} x}{x}.
$$

求出积分后,再以 $\frac{y}{x}$ 代替u,便得所给齐次方程的通解.

例1 解方程

$$
y ^ {2} + x ^ {2} \frac {\mathrm{d} y}{\mathrm{d} x} = x y \frac {\mathrm{d} y}{\mathrm{d} x}.
$$

解 原方程可写成

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {y ^ {2}}{x y - x ^ {2}} = \frac {\left(\frac {y}{x}\right) ^ {2}}{\frac {y}{x} - 1},
$$

因此是齐次方程.令 $\frac{y}{x} = u$ ，则

$$
y = x u, \quad \frac {\mathrm{d} y}{\mathrm{d} x} = u + x \frac {\mathrm{d} u}{\mathrm{d} x},
$$

于是原方程变为

$$
u + x \frac {\mathrm{d} u}{\mathrm{d} x} = \frac {u ^ {2}}{u - 1},
$$

即

$$
x \frac {\mathrm{d} u}{\mathrm{d} x} = \frac {u}{u - 1}.
$$

分离变量,得

$$
\left(1 - \frac {1}{u}\right) \mathrm{d} u = \frac {\mathrm{d} x}{x}.
$$

两端积分,得

$$
u - \ln | u | + C _ {1} = \ln | x |,
$$

或写为

$$
\ln | x u | = u + C _ {1}.
$$

以 $\frac{y}{x}$ 代上式中的 $u$ ，便得所给方程的通解为

$$
\ln | y | = \frac {y}{x} + C _ {1} \quad \text {或} \quad y = C \mathrm{e} ^ {\frac {y}{x}} (C = \pm \mathrm{e} ^ {C _ {1}}).
$$

例 2 探照灯的聚光镜的镜面是一张旋转曲面, 它的形状由 xOy 坐标面上的一条曲线 L 绕 x 轴旋转而成. 按聚光镜性能的要求, 在其旋转轴 (x 轴) 上一点 O 处发出的一切光线, 经它反射后都与旋转轴平行. 求曲线 L 的方程.

解 将光源所在之 O 点取作坐标原点(图 7-4)，且曲线 L 位于 $y \geqslant 0$ 范围内.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/6dbc1d8c072266f4f293ccfecdbb4ed127d2b9288b06b779856f9c85fe7eeea8.jpg)



图7-4


设点 $M(x,y)$ 为 $L$ 上的任一点，点 $O$ 发出的某条光线经点 $M$ 反射后是一条与 $x$ 轴平行的直线 $MS$ . 又设过点 $M$ 的切线 $AT$ 与 $x$ 轴的夹角为 $\alpha$ . 根据题意, $\angle SMT = \alpha$ . 另一方面, $\angle OMA$ 是入射角的余角, $\angle SMT$ 是反射角的余角, 于是由光学中的反射定律有 $\angle OMA = \angle SMT = \alpha$ . 从而 $AO = OM$ , 但 $AO = AP - OP = PM \cot \alpha - OP = \frac{y}{y'} - x$ , 而 $OM = \sqrt{x^2 + y^2}$ . 于是得微分方程

$$
\frac {y}{y ^ {\prime}} - x = \sqrt {x ^ {2} + y ^ {2}}.
$$

把 $x$ 看作因变量， $y$ 看作自变量，当 $y > 0$ 时，上式即为

$$
\frac {\mathrm{d} x}{\mathrm{d} y} = \frac {x}{y} + \sqrt {\left(\frac {x}{y}\right) ^ {2} + 1},
$$

这是齐次方程.令 $\frac{x}{y} = v$ ，则 $x = yv,\frac{\mathrm{d}x}{\mathrm{d}y} = v + y\frac{\mathrm{d}v}{\mathrm{d}y}$ ，代入上式，得

$$
v + y \frac {\mathrm{d} v}{\mathrm{d} y} = v + \sqrt {v ^ {2} + 1},
$$

即

$$
y \frac {\mathrm{d} v}{\mathrm{d} y} = \sqrt {v ^ {2} + 1}.
$$

分离变量,得

$$
\frac {\mathrm{d} v}{\sqrt {v ^ {2} + 1}} = \frac {\mathrm{d} y}{y}.
$$

积分,得

$$
\ln (v + \sqrt {v ^ {2} + 1}) = \ln y - \ln C,
$$

或

$$
v + \sqrt {v ^ {2} + 1} = \frac {y}{C}.
$$

由

$$
\left(\frac {y}{C} - v\right) ^ {2} = v ^ {2} + 1,
$$

得

$$
\frac {y ^ {2}}{C ^ {2}} - \frac {2 y v}{C} = 1,
$$

以 $yv = x$ 代入上式，得

$$
y ^ {2} = 2 C \left(x + \frac {C}{2}\right).
$$

这是以 x 轴为对称轴、焦点在原点的抛物线.

# *二、可化为齐次的方程

方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {a x + b y + c}{a _ {1} x + b _ {1} y + c _ {1}} \tag {3-3}
$$

当 $c=c_{1}=0$ 时是齐次的, 否则不是齐次的. 在非齐次的情形, 可用下列变换把它化为齐次方程: 令

$$
x = X + h, \quad y = Y + k,
$$

其中 $h$ 及 $k$ 是待定的常数.于是

$$
\mathrm{d} x = \mathrm{d} X, \quad \mathrm{d} y = \mathrm{d} Y,
$$

从而方程(3-3)成为

$$
\frac {\mathrm{d} Y}{\mathrm{d} X} = \frac {a X + b Y + a h + b k + c}{a _ {1} X + b _ {1} Y + a _ {1} h + b _ {1} k + c _ {1}}.
$$

如果方程组

$$
\left\{ \begin{array}{l} a h + b k + c = 0, \\ a _ {1} h + b _ {1} k + c _ {1} = 0 \end{array} \right.
$$

的系数行列式 $\left| \begin{array}{ll}a & b\\ a_1 & b_1 \end{array} \right|\neq 0$ ，即 $\frac{a_1}{a}\neq \frac{b_1}{b}$ 那么可以定出 $h$ 及 $k$ 使它们满足上述方程组.这样，方程(3-3)便化为齐次方程

$$
\frac {\mathrm{d} Y}{\mathrm{d} X} = \frac {a X + b Y}{a _ {1} X + b _ {1} Y}.
$$

求出这齐次方程的通解后,在通解中以 x-h 代 X,y-k 代 Y,便得方程(3-3)的通解.

当 $\frac{a_1}{a} = \frac{b_1}{b}$ 时， $h$ 及 $k$ 无法求得，因此上述方法不能应用。但这时令 $\frac{a_1}{a} = \frac{b_1}{b} = \lambda$ ，从而方程(3-3)可写成

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {a x + b y + c}{\lambda (a x + b y) + c _ {1}}.
$$

引入新变量 $v=ax+by$ ，则

$$
\frac {\mathrm{d} v}{\mathrm{d} x} = a + b \frac {\mathrm{d} y}{\mathrm{d} x} \quad \text {或} \quad \frac {\mathrm{d} y}{\mathrm{d} x} = \frac {1}{b} \left(\frac {\mathrm{d} v}{\mathrm{d} x} - a\right).
$$

于是方程(3-3)成为

$$
\frac {1}{b} \left(\frac {\mathrm{d} v}{\mathrm{d} x} - a\right) = - \frac {v + c}{\lambda v + c _ {1}},
$$

这是可分离变量的方程.

以上所介绍的方法可以应用于更一般的方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = f \left(\frac {a x + b y + c}{a _ {1} x + b _ {1} y + c _ {1}}\right).
$$

例3 解方程

$$
(2 x + y - 4) \mathrm{d} x + (x + y - 1) \mathrm{d} y = 0.
$$

解 所给方程属方程(3-3)的类型. 令 $x = X + h, y = Y + k$ , 则 $\mathrm{dx} = \mathrm{d}X, \mathrm{dy} = \mathrm{d}Y$ , 代入原方程得

$$
(2 X + Y + 2 h + k - 4) \mathrm{d} X + (X + Y + h + k - 1) \mathrm{d} Y = 0.
$$

解方程组

$$
\left\{ \begin{array}{l} 2 h + k - 4 = 0, \\ h + k - 1 = 0. \end{array} \right.
$$

得 h=3, k=-2. 令 $x=X+3$ , y=Y-2, 原方程成为

$$
(2 X + Y) \mathrm{d} X + (X + Y) \mathrm{d} Y = 0,
$$

或

$$
\frac {\mathrm{d} Y}{\mathrm{d} X} = - \frac {2 X + Y}{X + Y} = - \frac {2 + \frac {Y}{X}}{1 + \frac {Y}{X}},
$$

这是齐次方程.

令 $\frac{Y}{X} = u$ ，则 $Y = Xu, \frac{\mathrm{d}Y}{\mathrm{d}X} = u + X \frac{\mathrm{d}u}{\mathrm{d}X}$ ，于是方程变为

$$
u + X \frac {\mathrm{d} u}{\mathrm{d} X} = - \frac {2 + u}{1 + u},
$$

或

$$
X \frac {\mathrm{d} u}{\mathrm{d} X} = - \frac {2 + 2 u + u ^ {2}}{1 + u}.
$$

分离变量得

$$
- \frac {u + 1}{u ^ {2} + 2 u + 2} \mathrm{d} u = \frac {\mathrm{d} X}{X}.
$$

积分得

$$
\ln C _ {1} - \frac {1}{2} \ln (u ^ {2} + 2 u + 2) = \ln | X |,
$$

于是

$$
\frac {C _ {1}}{\sqrt {u ^ {2} + 2 u + 2}} = | X |,
$$

或

$$
C _ {2} = X ^ {2} (u ^ {2} + 2 u + 2) \quad (C _ {2} = C _ {1} ^ {2}),
$$

即

$$
Y ^ {2} + 2 X Y + 2 X ^ {2} = C _ {2}.
$$

以 X=x-3, Y=y+2 代入上式并化简, 得

$$
2 x ^ {2} + 2 x y + y ^ {2} - 8 x - 2 y = C \quad (C = C _ {2} - 1 0).
$$

# 习题7-3

1. 求下列齐次方程的通解：

(1) $xy' - y - \sqrt{y^2 - x^2} = 0$ ; 

(2) $x\frac{\mathrm{dy}}{\mathrm{dx}} = y\ln \frac{y}{x};$ 

(3) $(x^{2} + y^{2})\mathrm{d}x - xy\mathrm{d}y = 0;$ 

(4) $(x^{3} + y^{3})\mathrm{d}x - 3xy^{2}\mathrm{d}y = 0;$ 

(5) $\left(2x\sin\frac{y}{x}+3y\cos\frac{y}{x}\right)\mathrm{d}x-3x\cos\frac{y}{x}\mathrm{d}y=0;$ 

(6) $(1 + 2\mathrm{e}^{x / y})\mathrm{d}x + 2\mathrm{e}^{x / y}\left(1 - \frac{x}{y}\right)\mathrm{d}y = 0.$ 

2. 求下列齐次方程满足所给初值条件的特解：

(1) $(y^{2} - 3x^{2})\mathrm{d}y + 2xy\mathrm{d}x = 0,y\mid_{x = 0} = 1;$ 

(2) $y' = \frac{x}{y} + \frac{y}{x}, y \big|_{x=1} = 2;$ 

(3) $(x^{2} + 2xy - y^{2})\mathrm{d}x + (y^{2} + 2xy - x^{2})\mathrm{d}y = 0,y\mid_{x = 1} = 1;$ 

(4) $x\frac{\mathrm{dy}}{\mathrm{dx}} = y + x\sec \frac{y}{x},y\mid_{x = 1} = \frac{\pi}{4}.$ 

3. 设有连接点 $O(0,0)$ 和 $A(1,1)$ 的一段向上凸的曲线弧 $\widehat{OA}$ , 对于 $\widehat{OA}$ 上任一点 $P(x,y)$ , 曲线弧 $\widehat{OP}$ 与直线段 $\overline{OP}$ 所围图形的面积为 $x^{2}$ , 求曲线弧 $\widehat{OA}$ 的方程.

*4. 化下列方程为齐次方程,并求出通解:

(1) $(2x - 5y + 3)\mathrm{d}x - (2x + 4y - 6)\mathrm{d}y = 0;$ 

(2) $(x-y-1)\mathrm{d}x+(4y+x-1)\mathrm{d}y=0;$ 

(3) $(3y - 7x + 7)\mathrm{d}x + (7y - 3x + 3)\mathrm{d}y = 0;$ 

(4) $(x+y)\mathrm{d}x+(3x+3y-4)\mathrm{d}y=0,$ 

# 第四节 一阶线性微分方程

# 一、线性方程

方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} + P (x) y = Q (x) \tag {4-1}
$$

叫做一阶线性微分方程,因为它对于未知函数 y 及其导数是一次方程.如果 $Q(x) \equiv 0$ , 那么方程(4-1)称为齐次的;如果 $Q(x) \neq 0$ ,那么方程(4-1)称为非齐次的.

设(4-1)为非齐次线性方程.为了求出非齐次线性方程(4-1)的解,我们先把 $Q(x)$ 换成零而写出方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} + P (x) y = 0. \tag {4-2}
$$

方程(4-2)叫做对应于非齐次线性方程(4-1)的齐次线性方程.方程(4-2)是可分离变量的,分离变量后得

$$
\frac {\mathrm{d} y}{y} = - P (x) \mathrm{d} x,
$$

两端积分,得

$$
\ln | y | = - \int P (x) \mathrm{d} x + C _ {1},
$$

或

$$
y = C \mathrm{e} ^ {- \int P (x) \mathrm{d} x} \quad (C = \pm \mathrm{e} ^ {C _ {1}}),
$$

这是对应的齐次线性方程(4-2)的通解①.

现在我们使用所谓常数变易法来求非齐次线性方程(4-1)的通解.这方法是把(4-2)的通解中的 $C$ 换成 $\pmb{x}$ 的未知函数 $u(x)$ , 即作变换

$$
y = u \mathrm{e} ^ {- \int P (x) \mathrm{d} x}, \tag {4-3}
$$

于是

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = u ^ {\prime} \mathrm{e} ^ {- \int P (x) \mathrm{d} x} - u P (x) \mathrm{e} ^ {- \int P (x) \mathrm{d} x}. \tag {4-4}
$$

将(4-3)和(4-4)代入方程(4-1)得

$$
u ^ {\prime} \mathrm{e} ^ {- \int P (x) \mathrm{d} x} - u P (x) \mathrm{e} ^ {- \int P (x) \mathrm{d} x} + P (x) u \mathrm{e} ^ {- \int P (x) \mathrm{d} x} = Q (x),
$$

即

$$
u ^ {\prime} \mathrm{e} ^ {- \int P (x) \mathrm{d} x} = Q (x), u ^ {\prime} = Q (x) \mathrm{e} ^ {\int P (x) \mathrm{d} x}.
$$

两端积分,得

$$
u = \int Q (x) \mathrm{e} ^ {\int P (x) \mathrm{d} x} \mathrm{d} x + C.
$$

把上式代入(4-3)，便得非齐次线性方程(4-1)的通解

$$
y = \mathrm{e} ^ {- \int P (x) \mathrm{d} x} \left[ \int Q (x) \mathrm{e} ^ {\int P (x) \mathrm{d} x} \mathrm{d} x + C \right]. \tag {4-5}
$$

将(4-5)式改写成两项之和

$$
y = C \mathrm{e} ^ {- \int P (x) \mathrm{d} x} + \mathrm{e} ^ {- \int P (x) \mathrm{d} x} \int Q (x) \mathrm{e} ^ {\int P (x) \mathrm{d} x} \mathrm{d} x,
$$

上式右端第一项是对应的齐次线性方程(4-2)的通解,第二项是非齐次线性方程(4-1)的一个特解(在(4-1)的通解(4-5)中取C=0便得到这个特解).由此可知,一阶非齐次线性方程的通解等于对应的齐次方程的通解与非齐次方程的一个特解之和.

例1 求方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} - \frac {2 y}{x + 1} = (x + 1) ^ {\frac {5}{2}}
$$

的通解.

解 这是一个非齐次线性方程. 先求对应的齐次方程的通解.

$$
\frac {\mathrm{d} y}{\mathrm{d} x} - \frac {2}{x + 1} y = 0,
$$

$$
\frac {\mathrm{d} y}{y} = \frac {2 \mathrm{d} x}{x + 1},
$$

$$
\ln | y | = 2 \ln | x + 1 | + C _ {1},
$$

$$
y = C (x + 1) ^ {2} \left(C = \pm e ^ {C _ {1}}\right).
$$

用常数变易法, 把 C 换成 u, 即令

$$
y = u (x + 1) ^ {2}, \tag {4-6}
$$

那么

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = u ^ {\prime} (x + 1) ^ {2} + 2 u (x + 1),
$$

代入所给非齐次方程,得

$$
u ^ {\prime} = (x + 1) ^ {\frac {1}{2}}.
$$

两端积分,得

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/a07eb1de88df998f6efb115b2a573fc150fb3706d4c50a251e36f585293bae54.jpg)


释疑解难

7-3 

$$
u = \frac {2}{3} (x + 1) ^ {\frac {3}{2}} + C.
$$

再把上式代入(4-6)式,即得所求方程的通解为

$$
y = (x + 1) ^ {2} \left[ \frac {2}{3} (x + 1) ^ {\frac {3}{2}} + C \right].
$$

例 2 有一个电路如图 7-5 所示, 其中电源电动势为 $E = E_{m} \sin \omega t$ ( $E_{m}, \omega$ 都是常量), 电阻 R 和电感 L 都是常量. 求电流 $i(t)$ .

解（i）列方程 由电学知道，当电流变化时， $L$ 上有感应电动势 $-L\frac{\mathrm{d}i}{\mathrm{d}t}$ 。由回路电压定律得出

$$
E - L \frac {\mathrm{d} i}{\mathrm{d} t} - i R = 0,
$$

即

$$
\frac {\mathrm{d} i}{\mathrm{d} t} + \frac {R}{L} i = \frac {E}{L}.
$$

把 $E=E_{m}\sin\omega t$ 代入上式, 得

$$
\frac {\mathrm{d} i}{\mathrm{d} t} + \frac {R}{L} i = \frac {E _ {\mathrm{m}}}{L} \sin \omega t. \tag {4-7}
$$

未知函数 $i(t)$ 应满足方程(4-7). 此外, 设开关 S 闭合的时刻为 $t = 0$ , 这时 $i(t)$ 还应该满足初值条件

$$
i \mid_ {t = 0} = 0. \tag {4-8}
$$

(ii) 解方程 方程(4-7)是一个非齐次线性方程. 可以先求出对应的齐次方程的通解, 然后用常数变易法求非齐次方程的通解. 但是, 也可以直接应用通解公式(4-5)

来求解.这里 $P(t) = \frac{R}{L}, Q(t) = \frac{E_{\mathrm{m}}}{L}\sin \omega t$ ，代入公式(4-5)，得

$$
i (t) = \mathrm{e} ^ {- \frac {R}{L} t} \left(\int \frac {E _ {\mathrm{m}}}{L} \mathrm{e} ^ {\frac {R}{L} t} \sin \omega t \mathrm{d} t + C\right).
$$

应用分部积分法,得

$$
\int \mathrm{e} ^ {\frac {R}{L} t} \sin \omega t \mathrm{d} t = \frac {\mathrm{e} ^ {\frac {R}{L} t}}{R ^ {2} + \omega^ {2} L ^ {2}} (R L \sin \omega t - \omega L ^ {2} \cos \omega t),
$$

将上式代入前式并化简,得方程(4-7)的通解

$$
i (t) = \frac {E _ {\mathrm{m}}}{R ^ {2} + \omega^ {2} L ^ {2}} (R \sin \omega t - \omega L \cos \omega t) + C \mathrm{e} ^ {- \frac {R}{L} t},
$$

其中 C 为任意常数.

将初值条件(4-8)代入上式,得

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/bd3dd5941944136c3478bae9e775c40e4a7467c50566048919e6a1c538238a3a.jpg)



图7-5


$$
C = \frac {\omega L E _ {\mathrm{m}}}{R ^ {2} + \omega^ {2} L ^ {2}},
$$

因此,所求函数 $i(t)$ 为

$$
i (t) = \frac {\omega L E _ {\mathrm{m}}}{R ^ {2} + \omega^ {2} L ^ {2}} \mathrm{e} ^ {- \frac {R}{L} t} + \frac {E _ {\mathrm{m}}}{R ^ {2} + \omega^ {2} L ^ {2}} (R \sin \omega t - \omega L \cos \omega t). \tag {4-9}
$$

为了便于说明(4-9)式所反映的物理现象,下面把 $i(t)$ 中第二项的形式稍加改变.令

$$
\cos \varphi = \frac {R}{\sqrt {R ^ {2} + \omega^ {2} L ^ {2}}}, \quad \sin \varphi = \frac {\omega L}{\sqrt {R ^ {2} + \omega^ {2} L ^ {2}}},
$$

于是(4-9)式可写成

$$
i (t) = \frac {\omega L E _ {\mathrm{m}}}{R ^ {2} + \omega^ {2} L ^ {2}} \mathrm{e} ^ {- \frac {R}{L} t} + \frac {E _ {\mathrm{m}}}{\sqrt {R ^ {2} + \omega^ {2} L ^ {2}}} \sin (\omega t - \varphi),
$$

其中

$$
\varphi = \arctan \frac {\omega L}{R}.
$$

当 t 增大时, 上式右端第一项(叫做暂态电流)逐渐衰减而趋于零; 第二项(叫做稳态电流)是正弦函数, 它的周期和电动势的周期相同而相角落后 $\varphi$ .

在上节中,对于齐次方程 $y' = f\left(\frac{y}{x}\right)$ ，我们通过变量代换 y = xu，把它化为变量可分离的方程，然后分离变量，经积分求得通解。在本节中，对于一阶非齐次线性方程

$$
y ^ {\prime} + P (x) y = Q (x),
$$

我们通过解对应的齐次线性方程找到变量代换

$$
y = u \mathrm{e} ^ {- \int P (x) \mathrm{d} x},
$$

利用这一代换,把非齐次线性方程化为变量可分离的方程,然后经积分求得通解.

利用变量代换(因变量的变量代换或自变量的变量代换)把一个微分方程化为变量可分离的方程,或化为已经知其求解步骤的方程,这是解微分方程最常用的方法.下面再举一个例子.

例3 解方程 $\frac{\mathrm{dy}}{\mathrm{dx}} = \frac{1}{x + y}$ .

解 若把所给方程变形为

$$
\frac {\mathrm{d} x}{\mathrm{d} y} = x + y,
$$

即为一阶线性方程,则按一阶线性方程的解法可求得通解.

也可用变量代换来解所给方程. 令 $x + y = u$ , 则 $y = u - x, \frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}u}{\mathrm{d}x} - 1$ . 代入原方程, 得

$$
\frac {\mathrm{d} u}{\mathrm{d} x} - 1 = \frac {1}{u}, \quad \frac {\mathrm{d} u}{\mathrm{d} x} = \frac {u + 1}{u}.
$$

分离变量得

$$
\frac {u}{u + 1} \mathrm{d} u = \mathrm{d} x,
$$

两端积分得

$$
u - \ln | u + 1 | = x + C _ {1}.
$$

以 $u=x+y$ 代入上式, 即得

$$
y - \ln | x + y + 1 | = C _ {1},
$$

或

$$
x = C \mathrm{e} ^ {y} - y - 1 \quad (C = \pm \mathrm{e} ^ {- C _ {1}}).
$$

在以上求解过程中, 假定了 $u + 1 \neq 0$ , 即 $x + y + 1 \neq 0$ . 事实上, $x + y + 1 = 0$ 也是方程的解. 为了补充这个失去的解, 在 $C = \pm e^{C_1} \neq 0$ 中, 补充 $C = 0$ , 即

$$
x = C \mathrm{e} ^ {y} - y - 1,
$$

其中 C 为任意常数.

# *二、伯努利方程

方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} + P (x) y = Q (x) y ^ {n} \quad (n \neq 0, 1) \tag {4-10}
$$

叫做伯努利(Bernoulli)方程.当 $n = 0$ 或 $n = 1$ 时,这是线性微分方程.当 $n \neq 0$ ,且 $n \neq 1$ 时,这方程不是线性的,但是通过变量的代换,便可把它化为线性的.事实上,以 $y^n$ 除方程(4-10)的两端,得

$$
y ^ {- n} \frac {\mathrm{d} y}{\mathrm{d} x} + P (x) y ^ {1 - n} = Q (x). \tag {4-11}
$$

容易看出,上式左端第一项与 $\frac{\mathrm{d}}{\mathrm{d}x}(y^{1-n})$ 只差一个常数因子1-n,因此我们引入新的因变量

$$
z = y ^ {1 - n},
$$

那么

$$
\frac {\mathrm{d} z}{\mathrm{d} x} = (1 - n) y ^ {- n} \frac {\mathrm{d} y}{\mathrm{d} x}.
$$

用 $(1-n)$ 乘方程 $(4-11)$ 的两端,再通过上述代换便得线性方程

$$
\frac {\mathrm{d} z}{\mathrm{d} x} + (1 - n) P (x) z = (1 - n) Q (x).
$$

求出这方程的通解后,以 $y^{1-n}$ 代换 z 便得到伯努利方程的通解.

例4 求方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} + \frac {y}{x} = a (\ln x) y ^ {2}
$$

的通解.

解 以 $y^{2}$ 除方程的两端, 得

$$
y ^ {- 2} \frac {\mathrm{d} y}{\mathrm{d} x} + \frac {1}{x} y ^ {- 1} = a \ln x,
$$

即

$$
- \frac {\mathrm{d} (y ^ {- 1})}{\mathrm{d} x} + \frac {1}{x} y ^ {- 1} = a \ln x.
$$

令 $z = y^{-1}$ ，则上述方程成为

$$
\frac {\mathrm{d} z}{\mathrm{d} x} - \frac {1}{x} z = - a \ln x.
$$

这是一个线性方程,它的通解为

$$
z = x \left[ C - \frac {a}{2} (\ln x) ^ {2} \right].
$$

以 $y^{-1}$ 代 z, 得所求方程的通解为

$$
y x \left[ C - \frac {a}{2} (\ln x) ^ {2} \right] = 1.
$$

# 习题7-4

1. 求下列微分方程的通解：

(1) $\frac{\mathrm{dy}}{\mathrm{dx}} + y = \mathrm{e}^{-x}$ ; 

(2) $xy' + y = x^2 + 3x + 2$ ; 

(3) $y' + y\cos x = e^{-\sin x}$ ; 

(4) $y' + y \tan x = \sin 2x;$ 

(5) $(x^{2}-1)y'+2xy-\cos x=0;$ 

(6) $\frac{\mathrm{d}\rho}{\mathrm{d}\theta} + 3\rho = 2;$ 

(7) $\frac{\mathrm{dy}}{\mathrm{dx}} + 2xy = 4x$ ; 

(8) $y \ln y \, dx + (x - \ln y) \, dy = 0;$ 

(9) $(x-2)\frac{\mathrm{d}y}{\mathrm{d}x}=y+2(x-2)^{3}$ ; 

(10) $(y^{2}-6x)\frac{\mathrm{d}y}{\mathrm{d}x}+2y=0.$ 

2. 求下列微分方程满足所给初值条件的特解：

(1) $\frac{\mathrm{dy}}{\mathrm{dx}} - y\tan x = \sec x, y \mid_{x=0} = 0;$ 

(2) $\frac{\mathrm{dy}}{\mathrm{dx}} + \frac{y}{x} = \frac{\sin x}{x}, y \mid_{x=\pi} = 1$ ; 

(3) $\frac{\mathrm{dy}}{\mathrm{dx}} + y\cot x = 5\mathrm{e}^{\cos x}, y \mid_{x = \frac{\pi}{2}} = -4;$ 

(4) $\frac{\mathrm{dy}}{\mathrm{dx}} + 3y = 8, y \mid_{x=0} = 2$ ; 

(5) $\frac{\mathrm{dy}}{\mathrm{dx}} + \frac{2 - 3x^2}{x^3} y = 1, y \mid_{x=1} = 0$ ; 

(6) $x(1 + x^2)y' + y = 1 + x^2, y \mid_{x=1} = 0.$ 

3. 若曲线通过原点,并且它在点 $(x,y)$ 处的切线斜率等于 $2x+y$ ,求这曲线的方程.

4. 设有一质量为 $m$ 的质点做直线运动. 从速度等于零的时刻起, 有一个与运动方向一致、大小与时间成正比 (比例系数为 $k_{1}$ ) 的力作用于它, 此外还受一与速度成正比 (比例系数为 $k_{2}$ ) 的阻力作用. 求质点运动的速度与时间的函数关系.

5. 设有一个由电阻 $R=10\ \Omega$ 、电感 $L=2\ H$ 和电源电压 $E=20\sin5t\ V$ 串联组成的电路。开关 S 合上后，电路中有电流通过。求电流 i 与时间 t 的函数关系。

6. 验证形如 $yf(xy) \, \mathrm{d}x + xg(xy) \, \mathrm{d}y = 0$ 的微分方程可经变量代换 $v = xy$ 化为可分离变量的方程，并求其通解.

7. 用适当的变量代换将下列方程化为可分离变量的方程, 然后求出通解:

(1) $\frac{\mathrm{dy}}{\mathrm{dx}} = (x + y)^2$ ; 

(2) $\frac{\mathrm{dy}}{\mathrm{dx}} = \frac{1}{x - y} + 1$ ; 

(3) $xy' + y = y (\ln x + \ln y)$ ; 

(4) $y' = y^2 + 2(\sin x - 1)y + \sin^2 x - 2\sin x - \cos x + 1;$ 

(5) $y(xy+1)\mathrm{d}x+x(1+xy+x^{2}y^{2})\mathrm{d}y=0.$ 

* 8. 求下列伯努利方程的通解：

(1) $\frac{\mathrm{dy}}{\mathrm{dx}} + y = y^2 (\cos x - \sin x)$ ; 

(2) $\frac{\mathrm{dy}}{\mathrm{dx}} - 3xy = xy^2$ ; 

(3) $\frac{dy}{dx}+\frac{1}{3}y=\frac{1}{3}(1-2x)y^{4};$ 

(4) $\frac{\mathrm{dy}}{\mathrm{dx}} - y = xy^5$ ; 

(5) $x \, dy - [y + xy^{3}(1 + \ln x)] \, dx = 0.$ 

# 第五节 可降阶的高阶微分方程

从这一节起我们将讨论二阶及二阶以上的微分方程,即所谓高阶微分方程.对于有些高阶微分方程,我们可以通过代换将它化成较低阶的方程来求解.以二阶微分方程

$$
y ^ {\prime \prime} = f (x, y, y ^ {\prime}) \tag {5-1}
$$

而论,如果我们能设法作代换把它从二阶降至一阶,那么就有可能应用前面几节中所讲的方法来求出它的解了.

下面介绍三种容易降阶的高阶微分方程的求解方法.

# 一、 $y^{(n)}=f(x)$ 型的微分方程

微分方程

$$
y ^ {(n)} = f (x) \tag {5-2}
$$

的右端仅含有自变量 $x$ . 容易看出, 只要把 $y^{(n-1)}$ 作为新的未知函数, 那么 (5-2) 式就是

新未知函数的一阶微分方程.两边积分,就得到一个n-1阶的微分方程

$$
\gamma^ {(n - 1)} = \int f (x) \mathrm{d} x + C _ {1}.
$$

同理可得

$$
\gamma^ {(n - 2)} = \int \left[ \int f (x) \mathrm{d} x + C _ {1} \right] \mathrm{d} x + C _ {2}.
$$

依此法继续进行,接连积分 n 次,便得方程(5-2)的含有 n 个任意常数的通解.

例1 求微分方程

$$
y ^ {\prime \prime \prime} = \mathrm{e} ^ {2 x} - \cos x
$$

的通解.

解 对所给方程接连积分三次, 得

$$
\begin{array}{l} y ^ {\prime \prime} = \frac {1}{2} \mathrm{e} ^ {2 x} - \sin x + C, \\ y ^ {\prime} = \frac {1}{4} \mathrm{e} ^ {2 x} + \cos x + C x + C _ {2}, \\ y = \frac {1}{8} \mathrm{e} ^ {2 x} + \sin x + C _ {1} x ^ {2} + C _ {2} x + C _ {3} \quad \left(C _ {1} = \frac {C}{2}\right), \\ \end{array}
$$

这就是所求的通解.

例 2 质量为 m 的质点受力 F 的作用沿 x 轴做直线运动. 设力 $F = F(t)$ 在开始时刻 t = 0 时 $F(0) = F_{0}$ ，随着时间 t 的增大，力 F 均匀地减小，直到 t = T 时， $F(T) = 0$ . 如果开始时质点位于原点，且初速度为零，求这质点的运动规律.

解 设 $x = x(t)$ 表示在时刻 $t$ 时质点的位置, 根据牛顿第二定律, 质点运动的微分方程为

$$
m \frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} = F (t). \tag {5-3}
$$

由题设, 力 $F(t)$ 随 t 增大而均匀地减小, 且 t=0 时, $F(0)=F_{0}$ , 所以 $F(t)=F_{0}-kt$ ; 又当 t=T 时, $F(T)=0$ , 从而

$$
F (t) = F _ {0} \left(1 - \frac {t}{T}\right).
$$

于是方程(5-3)可以写成

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} = \frac {F _ {0}}{m} \left(1 - \frac {t}{T}\right). \tag {5-4}
$$

其初值条件为

$$
x \mid_ {t = 0} = 0, \quad \frac {\mathrm{d} x}{\mathrm{d} t} \Big | _ {t = 0} = 0.
$$

把(5-4)式两端积分,得

$$
\frac {\mathrm{d} x}{\mathrm{d} t} = \frac {F _ {0}}{m} \int \left(1 - \frac {t}{T}\right) \mathrm{d} t,
$$

即

$$
\frac {\mathrm{d} x}{\mathrm{d} t} = \frac {F _ {0}}{m} \left(t - \frac {t ^ {2}}{2 T}\right) + C _ {1}. \tag {5-5}
$$

将条件 $\frac{dx}{dt}\bigg|_{t=0}=0$ 代入(5-5)式,得

$$
C _ {1} = 0,
$$

于是(5-5)式成为

$$
\frac {\mathrm{d} x}{\mathrm{d} t} = \frac {F _ {0}}{m} \left(t - \frac {t ^ {2}}{2 T}\right). \tag {5-6}
$$

把(5-6)式两端积分,得

$$
x = \frac {F _ {0}}{m} \left(\frac {t ^ {2}}{2} - \frac {t ^ {3}}{6 T}\right) + C _ {2},
$$

将条件 $x|_{t = 0} = 0$ 代入上式，得

$$
C _ {2} = 0.
$$

于是所求质点的运动规律为

$$
x = \frac {F _ {0}}{m} \left(\frac {t ^ {2}}{2} - \frac {t ^ {3}}{6 T}\right), \quad 0 \leqslant t \leqslant T.
$$

# 二、 $y''=f(x,y')$ 型的微分方程

方程

$$
y ^ {\prime \prime} = f (x, y ^ {\prime}) \tag {5-7}
$$

的右端不显含未知函数 y. 如果我们设 $y' = p$ ，那么

$$
y ^ {\prime \prime} = \frac {\mathrm{d} p}{\mathrm{d} x} = p ^ {\prime},
$$

而方程(5-7)就成为

$$
p ^ {\prime} = f (x, p).
$$

这是一个关于变量 x, p 的一阶微分方程. 设其通解为

$$
p = \varphi (x, C _ {1}),
$$

但是 $p = \frac{\mathrm{dy}}{\mathrm{dx}}$ ，因此又得到一个一阶微分方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \varphi (x, C _ {1}).
$$

对它进行积分,便得方程(5-7)的通解为

$$
y = \int \varphi (x, C _ {1}) \mathrm{d} x + C _ {2}.
$$

例3 求微分方程

$$
\left(1 + x ^ {2}\right) y ^ {\prime \prime} = 2 x y ^ {\prime}
$$

满足初值条件

$$
y \mid_ {x = 0} = 1, \quad y ^ {\prime} \mid_ {x = 0} = 3
$$

的特解.

解 所给方程是 $y''=f(x,y')$ 型的. 设 $y'=p$ , 代入方程并分离变量后, 有

$$
\frac {\mathrm{d} p}{p} = \frac {2 x}{1 + x ^ {2}} \mathrm{d} x.
$$

两端积分,得

$$
\ln | p | = \ln (1 + x ^ {2}) + C,
$$

即

$$
p = y ^ {\prime} = C _ {1} \left(1 + x ^ {2}\right) \quad \left(C _ {1} = \pm e ^ {C}\right).
$$

由条件 $y'\mid_{x=0}=3$ ，得

$$
C _ {1} = 3,
$$

所以

$$
y ^ {\prime} = 3 (1 + x ^ {2}).
$$

两端再积分,得

$$
y = x ^ {3} + 3 x + C _ {2}.
$$

又由条件 $y|_{x = 0} = 1$ ，得

$$
C _ {2} = 1,
$$

于是所求的特解为

$$
y = x ^ {3} + 3 x + 1.
$$

例 4 设有一均匀、柔软的绳索,两端固定,绳索仅受重力的作用而下垂.试问该绳索在平衡状态时是怎样的曲线?

解 设绳索的最低点为 $A$ . 取 $y$ 轴通过点 $A$ 铅直向上, 并取 $x$ 轴水平向右. 且 $|OA|$ 等于某个定值 (这个定值将在以后说明). 设绳索曲线的方程为 $y = \varphi(x)$ . 考察绳索上点 $A$ 到另一点 $M(x, y)$ 间的一段弧 $\widehat{AM}$ , 设其长为 $s$ . 假定绳索的线密度为 $\rho$ , 则弧 $\widehat{AM}$ 所受重力为 $\rho g s$ . 由于绳索是柔软的, 因而在点 $A$ 处的张力沿水平的切线方向, 其大小设为 $H$ ; 在点 $M$ 处的张力沿该点处的切线方向, 设其倾角为 $\theta$ , 其大小为 $T$ (图7-6). 因作用于弧段 $\widehat{AM}$ 的外力相互平衡, 把作用于弧 $\widehat{AM}$ 上的力沿铅直及水平两方向分解, 得

$$
T \sin \theta = \rho g s, \quad T \cos \theta = H.
$$

将此两式相除,得

$$
\tan \theta = \frac {1}{a} s \quad \left(a = \frac {H}{\rho g}\right).
$$

由于 $\tan \theta = y^{\prime}, s = \int_{0}^{x}\sqrt{1 + y'^2} \mathrm{d}x$ ，代入上式即得

$$
y ^ {\prime} = \frac {1}{a} \int_ {0} ^ {x} \sqrt {1 + y ^ {\prime 2}} \mathrm{d} x.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/d5197229336347664a20cd313e371db513ebd8f4cc39b80161052821a6f93b6a.jpg)



图7-6


将上式两端对 x 求导, 便得 $y=\varphi(x)$ 满足的微分方程

$$
y ^ {\prime \prime} = \frac {1}{a} \sqrt {1 + y ^ {\prime 2}}. \tag {5-8}
$$

取原点 O 到点 A 的距离为定值 a，即 $\left|OA\right|=a$ ，那么初值条件为

$$
y \mid_ {x = 0} = a, \quad y ^ {\prime} \mid_ {x = 0} = 0.
$$

下面来解方程(5-8).

方程(5-8)属于 $y''=f(x,y')$ 的类型. 设 $y'=p$ , 则 $y''=\frac{dp}{dx}$ , 代入方程(5-8), 并分离变量, 得

$$
\frac {\mathrm{d} p}{\sqrt {1 + p ^ {2}}} = \frac {\mathrm{d} x}{a}.
$$

两端积分,得

$$
\ln (p + \sqrt {1 + p ^ {2}}) = \frac {x}{a} + C _ {1}. \tag {5-9}
$$

把条件 $y'\mid_{x=0}=p\mid_{x=0}=0$ 代入(5-9)式, 得

$$
C _ {1} = 0,
$$

于是(5-9)式成为

$$
\ln (p + \sqrt {1 + p ^ {2}}) = \frac {x}{a},
$$

解得

$$
p = \frac {1}{2} \left(\mathrm{e} ^ {\frac {x}{a}} - \mathrm{e} ^ {- \frac {x}{a}}\right),
$$

即

$$
y ^ {\prime} = \frac {1}{2} \left(\mathrm{e} ^ {\frac {x}{a}} - \mathrm{e} ^ {- \frac {x}{a}}\right).
$$

积分上式两端,便得

$$
y = \frac {a}{2} (\mathrm{e} ^ {\frac {x}{a}} + \mathrm{e} ^ {- \frac {x}{a}}) + C _ {2}. \tag {5-10}
$$

将条件 $y \mid_{x=0}=a$ 代入(5-10)式, 得

$$
C _ {2} = 0.
$$

于是该绳索的形状可由曲线方程

$$
y = \frac {a}{2} \left(\mathrm{e} ^ {\frac {x}{a}} + \mathrm{e} ^ {- \frac {x}{a}}\right)
$$

来表示.这曲线叫做悬链线.

# 三、 $y''=f(y,y')$ 型的微分方程

方程

$$
y ^ {\prime \prime} = f (y, y ^ {\prime}) \tag {5-11}
$$

中不明显地含自变量 $x$ ，为了求出它的解。我们令 $y' = p$ ，并利用复合函数的求导法则把 $y''$ 化为对 $y$ 的导数，即

$$
y ^ {\prime \prime} = \frac {\mathrm{d} p}{\mathrm{d} x} = \frac {\mathrm{d} p}{\mathrm{d} y} \cdot \frac {\mathrm{d} y}{\mathrm{d} x} = p \frac {\mathrm{d} p}{\mathrm{d} y}.
$$

这样,方程(5-11)就成为

$$
p \frac {\mathrm{d} p}{\mathrm{d} y} = f (y, p),
$$

这是一个关于变量 y, p 的一阶微分方程. 设它的通解为

$$
y ^ {\prime} = p = \varphi (y, C _ {1}),
$$

分离变量并积分,便得方程(5-11)的通解为

$$
\int \frac {\mathrm{d} y}{\varphi (y , C _ {1})} = x + C _ {2}.
$$

例5 求微分方程

$$
y y ^ {\prime \prime} - y ^ {\prime 2} = 0 \tag {5-12}
$$

的通解.

解 方程(5-12)不明显地含自变量 x, 设

$$
y ^ {\prime} = p,
$$

则 $y''=p\frac{dp}{dy}$ ，代入方程(5-12)，得

$$
\gamma p \frac {\mathrm{d} p}{\mathrm{d} y} - p ^ {2} = 0.
$$

在 $y \neq 0, p \neq 0$ 时，约去 p 并分离变量，得

$$
\frac {\mathrm{d} p}{p} = \frac {\mathrm{d} y}{y}.
$$

两端积分,得

$$
\ln | p | = \ln | y | + C,
$$

即

$$
p = C _ {1} y \quad \text {或} \quad y ^ {\prime} = C _ {1} y \quad (C _ {1} = \pm e ^ {c}).
$$

再分离变量并两端积分,便得方程(5-12)的通解为

$$
\ln | y | = C _ {1} x + C _ {2} ^ {\prime},
$$

或

$$
y = C _ {2} \mathrm{e} ^ {C _ {1} x} \quad (C _ {2} = \pm \mathrm{e} ^ {C _ {2} ^ {\prime}}).
$$

例 6 一个离地面很高的物体, 受地球引力的作用由静止开始落向地面. 求它落到地面时的速度和所需的时间 (不计空气阻力).

解 取连接地心与该物体的直线为 y 轴, 其方向铅直向上, 取地心为原点 O (图 7-7).

设地球的半径为 R, 物体的质量为 m, 物体开始下落时与地心的距离为 $l (l > R)$ , 在时刻 t 物体所在位置为 $y = \varphi(t)$ , 于是速度为 $v(t) = \frac{\mathrm{d}y}{\mathrm{d}t}$ . 根据万有引力定律, 即得微分方程

$$
m \frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} = - \frac {G m M}{y ^ {2}},
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/2ac1b3cca6d5e0f3b67fa2de16e936d1734c7ed7b737322263039353bccf301f.jpg)



图7-7


即

$$
\frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} = - \frac {G M}{y ^ {2}}, \tag {5-13}
$$

其中 $M$ 为地球的质量, $G$ 为引力常量. 因为当 $y = R$ 时, $\frac{\mathrm{d}^2y}{\mathrm{d}t^2} = -g$ (这里置负号是由于物体运动加速度的方向与 $y$ 轴的正向相反的缘故), 所以 $g = \frac{GM}{R^2}$ , $GM = gR^2$ . 于是方程 (5-13) 成为

$$
\frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} = - \frac {g R ^ {2}}{y ^ {2}}. \tag {5-14}
$$

初值条件是

$$
\left. y \right| _ {t = 0} = l, \quad \left. y ^ {\prime} \right| _ {t = 0} = 0.
$$

先求物体到达地面时的速度.由 $\frac{\mathrm{dy}}{\mathrm{dt}} = v$ ，得

$$
\frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} = \frac {\mathrm{d} v}{\mathrm{d} t} = \frac {\mathrm{d} v}{\mathrm{d} y} \cdot \frac {\mathrm{d} y}{\mathrm{d} t} = v \frac {\mathrm{d} v}{\mathrm{d} y},
$$

代入方程(5-14)并分离变量,得

$$
v \mathrm{d} v = - \frac {g R ^ {2}}{y ^ {2}} \mathrm{d} y.
$$

两端积分,得

$$
v ^ {2} = \frac {2 g R ^ {2}}{y} + C _ {1}.
$$

把初值条件代入上式,得

$$
C _ {1} = - \frac {2 g R ^ {2}}{l},
$$

于是

$$
v ^ {2} = 2 g R ^ {2} \left(\frac {1}{y} - \frac {1}{l}\right),
$$

$$
v = - R \sqrt {2 g \left(\frac {1}{y} - \frac {1}{l}\right)}. \tag {5-15}
$$

这里取负号是由于物体运动的方向与 y 轴的正向相反的缘故. 在 $(5-15)$ 式中令 y=R，就得到物体到达地面时的速度为

$$
v = - \sqrt {\frac {2 g R (l - R)}{l}}.
$$

下面来求物体落到地面所需的时间.由(5-15)式有

$$
\frac {\mathrm{d} y}{\mathrm{d} t} = v = - R \sqrt {2 g \left(\frac {1}{y} - \frac {1}{l}\right)},
$$

分离变量得

$$
\mathrm{d} t = - \frac {1}{R} \sqrt {\frac {l}{2 g}} \sqrt {\frac {y}{l - y}} \mathrm{d} y.
$$

两端积分(对右端积分利用置换 $y=l\cos^{2}u$ )，得

$$
t = \frac {1}{R} \sqrt {\frac {l}{2 g}} \left(\sqrt {l y - y ^ {2}} + l \arccos \sqrt {\frac {y}{l}}\right) + C _ {2}. \tag {5-16}
$$

由条件 $y|_{t=0}=l$ ，得

$$
C _ {2} = 0.
$$

于是(5-16)式成为

$$
t = \frac {1}{R} \sqrt {\frac {l}{2 g}} \left(\sqrt {l y - y ^ {2}} + l \arccos \sqrt {\frac {y}{l}}\right).
$$

在上式中令 y=R，便得到物体到达地面所需的时间为

$$
t = \frac {1}{R} \sqrt {\frac {l}{2 g}} \left(\sqrt {l R - R ^ {2}} + l \arccos \sqrt {\frac {R}{l}}\right).
$$

# 习题7-5

1. 求下列各微分方程的通解：

(1) $y''=x+\sin x;$ 

(2) $y''' = xe^x$ ; 

(3) $y''=\frac{1}{1+x^{2}};$ 

(4) $y''=1+y'^{2}$ ; 

(5) $y'' = y' + x$ ; 

(6) $xy'' + y' = 0;$ 

(7) $yy'' + 2y'^2 = 0$ ; 

(8) $y^{3}y''-1=0;$ 

(9) $y''=\frac{1}{\sqrt{y}};$ 

(10) $y'' = y'^{3} + y'$ . 

2. 设 $f(x)$ 具有二阶连续导数, 满足:

$$
f ^ {\prime 2} (x) = f (x) + \int_ {0} ^ {x} [ f ^ {\prime} (t) ] ^ {3} \mathrm{d} t,
$$

且 $f'(0)=1$ ,求 $f(x)$ .

3. 求下列各微分方程满足所给初值条件的特解：

(1) $y^{3}y'' + 1 = 0, y \big|_{x=1} = 1, y' \big|_{x=1} = 0;$ 

(2) $y'' - ay'^2 = 0, y \mid_{x=0} = 0, y' \mid_{x=0} = -1;$ 

(3) $y''' = e^{ax}, y \mid_{x=1} = y' \mid_{x=1} = y'' \mid_{x=1} = 0;$ 

(4) $y'' = e^{2y}, y \mid_{x=0} = y' \mid_{x=0} = 0;$ 

(5) $y'' = 3\sqrt{y}, y \mid_{x=0} = 1, y' \mid_{x=0} = 2;$ 

(6) $y'' + y'^2 = 1, y \big|_{x=0} = 0, y' \big|_{x=0} = 0.$ 

4. 试求 $y'' = x$ 的经过点 $M(0,1)$ 且在此点与直线 $y = \frac{x}{2} + 1$ 相切的积分曲线.

5. 设有一质量为 m 的物体在空中由静止开始下落, 如果空气阻力 R = cv (其中 c 为常数, v 为物体运动的速度), 试求物体下落的距离 s 与时间 t 的函数关系.

# 第六节 高阶线性微分方程

本节和以下两节,我们将讨论在实际问题中应用得较多的所谓高阶线性微分方程.讨论时以二阶线性微分方程为主.

# 一、二阶线性微分方程举例

例 1 设有一个弹簧, 它的上端固定, 下端挂一个质量为 m 的物体. 当物体处于静止状态时, 作用在物体上的重力与弹性力大小相等、方向相反. 这个位置就是物体的平衡位置. 如图 7-8 所示, 取 x 轴铅直向下, 并取物体的平衡位置为坐标原点.

如果使物体具有一个初始速度 $v_{0} \neq 0$ ，那么物体便离开平衡位置，并在平衡位置附近做上下振动.在振动过程中,物体的位置x随时间t变化,即x与t之间存在函数关系: $x=x(t)$ .要确定物体的振动规律,就要求出函数 $x=x(t)$ .

由力学知道,弹簧使物体回到平衡位置的弹性恢复力f(它不包括在平衡位置时和重力mg相平衡的那一部分弹性力)和物体离开平衡位置的位移x成正比:

$$
f = - c x,
$$

其中 c 为弹簧的弹性系数, 负号表示弹性恢复力的方向和物体位移的方向相反.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/2a9dbb9d368efb4e4ee6af8eae37537d6cf828f57bfa5208adccbeb5d154c519.jpg)



图7-8


另外,物体在运动过程中还受到阻尼介质(如空气、油等)的阻力的作用,使得振动逐渐趋向停止.由实验知道,阻力R的方向总与运动方向相反,当运动速度不大时,其大小与物体运动的速度成正比,设比例系数为 $\mu$ ,则有

$$
R = - \mu \frac {\mathrm{d} x}{\mathrm{d} t}.
$$

根据上述关于物体受力情况的分析,由牛顿第二定律得

$$
m \frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} = - c x - \mu \frac {\mathrm{d} x}{\mathrm{d} t}.
$$

移项,并记

$$
2 n = \frac {\mu}{m}, \quad k ^ {2} = \frac {c}{m},
$$

则上式化为

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} + 2 n \frac {\mathrm{d} x}{\mathrm{d} t} + k ^ {2} x = 0. \tag {6-1}
$$

这就是在有阻尼的情况下,物体自由振动的微分方程.

如果物体在振动过程中,还受到铅直干扰力

$$
F = H \sin p t
$$

的作用,那么有

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} + 2 n \frac {\mathrm{d} x}{\mathrm{d} t} + k ^ {2} x = h \sin p t, \tag {6-2}
$$

其中 $h=\frac{H}{m}$ . 这就是强迫振动的微分方程.

例 2 设有一个由电阻 R、自感 L、电容 C 和电源 E 串联组成的电路, 其中 R, L 及 C 为常数, $E = E_{m} \sin \omega t$ , 这里 $E_{m}$ 及 $\omega$ 也是常数 (图 7-9).

设电路中的电流为 $i(t)$ , 电容器极板上的电荷量为 $q(t)$ , 两极板间的电压为 $u_{C}$ ,

自感电动势为 $E_{L}$ . 由电学知道

$$
i = \frac {\mathrm{d} q}{\mathrm{d} t}, \quad u _ {C} = \frac {q}{C}, \quad E _ {L} = - L \frac {\mathrm{d} i}{\mathrm{d} t},
$$

根据回路电压定律,得

$$
E - L \frac {\mathrm{d} i}{\mathrm{d} t} - \frac {q}{C} - R i = 0,
$$

即

$$
L C \frac {\mathrm{d} ^ {2} u _ {c}}{\mathrm{d} t ^ {2}} + R C \frac {\mathrm{d} u _ {c}}{\mathrm{d} t} + u _ {c} = E _ {\mathrm{m}} \sin \omega t,
$$

或写成

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/c0ece5c71adbebf81a1b2dc2c2799da0c59adbfb101683c0111768ded5c5ee6a.jpg)



图7-9


$$
\frac {\mathrm{d} ^ {2} u _ {c}}{\mathrm{d} t ^ {2}} + 2 \beta \frac {\mathrm{d} u _ {c}}{\mathrm{d} t} + \omega_ {0} ^ {2} u _ {c} = \frac {E _ {\mathrm{m}}}{L C} \sin \omega t. \tag {6-3}
$$

式中 $\beta=\frac{R}{2L},\omega_{0}=\frac{1}{\sqrt{LC}}$ . 这就是串联电路的振荡方程.

如果电容器经充电后撤去外电源 $(E=0)$ ，那么方程 $(6-3)$ 成为

$$
\frac {\mathrm{d} ^ {2} u _ {C}}{\mathrm{d} t ^ {2}} + 2 \beta \frac {\mathrm{d} u _ {C}}{\mathrm{d} t} + \omega_ {0} ^ {2} u _ {C} = 0. \tag {6-4}
$$

例 1 和例 2 虽然是两个不同的实际问题,但是仔细观察一下所得出的方程(6-2)和(6-3),就会发现它们可以归结为同一个形式

$$
\frac {\mathrm{d} ^ {2} y}{\mathrm{d} x ^ {2}} + P (x) \frac {\mathrm{d} y}{\mathrm{d} x} + Q (x) y = f (x), \tag {6-5}
$$

而方程(6-1)和方程(6-4)都是方程(6-5)的特殊情形: $f(x)\equiv0$ .在工程技术的其他许多问题中,也会遇到上述类型的微分方程.

方程(6-5)叫做二阶线性微分方程.当方程右端 $f(x)\equiv0$ 时,方程叫做齐次的;当 $f(x)\neq0$ 时,方程叫做非齐次的.

于是方程(6-2)、(6-3)都是二阶非齐次线性微分方程,方程(6-1)、(6-4)都是二阶齐次线性微分方程.

要进一步讨论例 1 和例 2 中的问题, 就需要解二阶线性微分方程. 为此, 下面来讨论二阶线性微分方程的解的一些性质, 这些性质可以推广到 n 阶线性方程

$$
y ^ {(n)} + a _ {1} (x) y ^ {(n - 1)} + \dots + a _ {n - 1} (x) y ^ {\prime} + a _ {n} (x) y = f (x).
$$

# 二、线性微分方程的解的结构

先讨论二阶齐次线性方程

$$
y ^ {\prime \prime} + P (x) y ^ {\prime} + Q (x) y = 0. \tag {6-6}
$$

定理1 如果函数 $y_{1}(x)$ 与 $y_{2}(x)$ 是方程(6-6)的两个解, 那么

$$
y = C _ {1} y _ {1} (x) + C _ {2} y _ {2} (x) \tag {6-7}
$$

也是(6-6)的解,其中 $C_{1}, C_{2}$ 是任意常数.

证 将(6-7)式代入(6-6)式左端,得

$$
\begin{array}{l} \left[ C _ {1} y _ {1} ^ {\prime \prime} + C _ {2} y _ {2} ^ {\prime \prime} \right] + P (x) \left[ C _ {1} y _ {1} ^ {\prime} + C _ {2} y _ {2} ^ {\prime} \right] + Q (x) \left[ C _ {1} y _ {1} + C _ {2} y _ {2} \right] \\ = C _ {1} \left[ y _ {1} ^ {\prime \prime} + P (x) y _ {1} ^ {\prime} + Q (x) y _ {1} \right] + C _ {2} \left[ y _ {2} ^ {\prime \prime} + P (x) y _ {2} ^ {\prime} + Q (x) y _ {2} \right]. \\ \end{array}
$$

由于 $y_{1}$ 与 $y_{2}$ 是方程(6-6)的解, 上式右端方括号中的表达式都恒等于零, 因而整个式子恒等于零, 所以(6-7)式是方程(6-6)的解.

解(6-7)从形式上来看含有 $C_1$ 与 $C_2$ 两个任意常数,但它不一定是方程(6-6)的通解.例如,设 $y_1(x)$ 是(6-6)的一个解,则 $y_2(x) = 2y_1(x)$ 也是(6-6)的解.这时(6-7)式成为 $y = C_1y_1(x) + 2C_2y_1(x)$ ,可以把它改写成 $y = Cy_1(x)$ ,其中 $C = C_1 + 2C_2$ .这显然不是(6-6)的通解.那么在什么情况下(6-7)式才是方程(6-6)的通解呢?要解决这个问题,还得引入一个新的概念,即所谓函数组的线性相关与线性无关.

设 $y_{1}(x)$ , $y_{2}(x)$ , $\cdots$ , $y_{n}(x)$ 为定义在区间 I 上的 n 个函数, 如果存在 n 个不全为零的常数 $k_{1}$ , $k_{2}$ , $\cdots$ , $k_{n}$ , 使得当 $x \in I$ 时有恒等式

$$
k _ {1} y _ {1} + k _ {2} y _ {2} + \dots + k _ {n} y _ {n} \equiv 0
$$

成立,那么称这 n 个函数在区间 I 上线性相关;否则称线性无关.

例如, 函数 $1, \cos^{2}x, \sin^{2}x$ 在整个数轴上是线性相关的. 因为取 $k_{1}=1, k_{2}=k_{3}=-1$ , 就有恒等式

$$
1 - \cos^ {2} x - \sin^ {2} x \equiv 0.
$$

又如,函数 $1, x, x^{2}$ 在任何区间 $(a, b)$ 内是线性无关的. 因为如果 $k_{1}, k_{2}, k_{3}$ 不全为零, 那么在该区间内至多只有两个 x 值能使二次三项式

$$
k _ {1} + k _ {2} x + k _ {3} x ^ {2}
$$

为零;要使它恒等于零,必须 $k_{1},k_{2},k_{3}$ 全为零.

应用上述概念可知,对于两个函数的情形,它们线性相关与否,只要看它们的比是否为常数:如果比为常数,那么它们就线性相关;否则就线性无关.

有了一组函数线性相关或线性无关的概念后,我们有如下关于二阶齐次线性微分方程(6-6)的通解结构的定理.

定理2 如果 $y_{1}(x)$ 与 $y_{2}(x)$ 是方程(6-6)的两个线性无关的特解, 那么

$$
y = C _ {1} y _ {1} (x) + C _ {2} y _ {2} (x) \quad (C _ {1}, C _ {2} \text {是任意常数})
$$

就是方程(6-6)的通解.

例如,方程 $y'' + y = 0$ 是二阶齐次线性方程(这里 $P(x) \equiv 0, Q(x) \equiv 1$ ). 容易验证, $y_{1} = \cos x$ 与 $y_{2} = \sin x$ 是所给方程的两个解, 且 $\frac{y_{2}}{y_{1}} = \frac{\sin x}{\cos x} = \tan x \neq$ 常数, 即它们是线性无关

的.因此方程 $y'' + y = 0$ 的通解为

$$
y = C _ {1} \cos x + C _ {2} \sin x.
$$

又如，方程 $(x-1)y''-xy'+y=0$ 也是二阶齐次线性方程（这里 $P(x)=-\frac{x}{x-1},Q(x)=\frac{1}{x-1}$ ）.容易验证 $y_{1}=x,y_{2}=e^{x}$ 是所给方程的两个解，且 $\frac{y_{2}}{y_{1}}=\frac{e^{x}}{x}\neq$ 常数，即它们是线性无关的.因此方程的通解为

$$
y = C _ {1} x + C _ {2} \mathrm{e} ^ {x}.
$$

定理 2 不难推广到 n 阶齐次线性方程.

推论 如果 $y_{1}(x)$ , $y_{2}(x)$ , $\cdots$ , $y_{n}(x)$ 是 n 阶齐次线性方程

$$
y ^ {(n)} + a _ {1} (x) y ^ {(n - 1)} + \dots + a _ {n - 1} (x) y ^ {\prime} + a _ {n} (x) y = 0
$$

的 n 个线性无关的解,那么,此方程的通解为

$$
y = C _ {1} y _ {1} (x) + C _ {2} y _ {2} (x) + \dots + C _ {n} y _ {n} (x),
$$

其中 $C_{1}, C_{2}, \cdots, C_{n}$ 为任意常数.

下面讨论二阶非齐次线性方程(6-5).我们把方程(6-6)叫做与非齐次方程(6-5)对应的齐次方程.

在第四节中我们已经看到,一阶非齐次线性微分方程的通解由两部分构成:一部分是对应的齐次方程的通解,另一部分是非齐次方程本身的一个特解.实际上,不仅一阶非齐次线性微分方程的通解具有这样的结构,而且二阶及更高阶的非齐次线性微分方程的通解也具有同样的结构.

定理3 设 $y^{*}(x)$ 是二阶非齐次线性方程

$$
y ^ {\prime \prime} + P (x) y ^ {\prime} + Q (x) y = f (x) \tag {6-5}
$$

的一个特解. $Y(x)$ 是与(6-5)对应的齐次方程(6-6)的通解,则

$$
y = Y (x) + y ^ {*} (x) \tag {6-8}
$$

是二阶非齐次线性微分方程(6-5)的通解.

证 把(6-8)式代入方程(6-5)的左端,得

$$
\begin{array}{l} \left(Y ^ {\prime \prime} + y ^ {* ^ {\prime \prime}}\right) + P (x) \left(Y ^ {\prime} + y ^ {* ^ {\prime}}\right) + Q (x) \left(Y + y ^ {*}\right) \\ = \left[ Y ^ {\prime \prime} + P (x) Y ^ {\prime} + Q (x) Y \right] + \left[ y ^ {* \prime \prime} + P (x) y ^ {* \prime} + Q (x) y ^ {*} \right], \\ \end{array}
$$

由于 Y 是方程(6-6)的解, $y^{*}$ 是(6-5)的解, 可知第一个括号内的表达式恒等于零, 第二个恒等于 $f(x)$ . 这样, $y = Y + y^{*}$ 使(6-5)的两端恒等. 即(6-8)式是方程(6-5)的解.

由于对应的齐次方程(6-6)的通解 $Y = C_{1}y_{1} + C_{2}y_{2}$ 中含有两个任意常数，所以 $y = Y + y^{*}$ 中也含有两个任意常数，从而它就是二阶非齐次线性方程(6-5)的通解.

例如, 方程 $y'' + y = x^{2}$ 是二阶非齐次线性微分方程. 已知 $Y = C_{1} \cos x + C_{2} \sin x$ 是对应的齐次方程 $y'' + y = 0$ 的通解; 又容易验证 $y^{*} = x^{2} - 2$ 是所给方程的一个特解. 因此

$$
y = C _ {1} \cos x + C _ {2} \sin x + x ^ {2} - 2
$$

是所给方程的通解.

非齐次线性微分方程(6-5)的特解有时可用下述定理来帮助求出.

定理 4 设非齐次线性方程(6-5)的右端 $f(x)$ 是两个函数之和, 即

$$
y ^ {\prime \prime} + P (x) y ^ {\prime} + Q (x) y = f _ {1} (x) + f _ {2} (x), \tag {6-9}
$$

而 $y_{1}^{*}(x)$ 与 $y_{2}^{*}(x)$ 分别是方程

$$
y ^ {\prime \prime} + P (x) y ^ {\prime} + Q (x) y = f _ {1} (x)
$$

与

$$
y ^ {\prime \prime} + P (x) y ^ {\prime} + Q (x) y = f _ {2} (x)
$$

的特解, 则 $y_{1}^{*}(x)+y_{2}^{*}(x)$ 就是原方程的特解.

证 将 $y = y_{1}^{*} + y_{2}^{*}$ 代入方程(6-9)的左端,得

$$
\begin{array}{l} \left(y _ {1} ^ {*} + y _ {2} ^ {*}\right) ^ {\prime \prime} + P (x) \left(y _ {1} ^ {*} + y _ {2} ^ {*}\right) ^ {\prime} + Q (x) \left(y _ {1} ^ {*} + y _ {2} ^ {*}\right) \\ = \left[ y _ {1} ^ {* \prime \prime} + P (x) y _ {1} ^ {* \prime} + Q (x) y _ {1} ^ {*} \right] + \left[ y _ {2} ^ {* \prime \prime} + P (x) y _ {2} ^ {* \prime} + Q (x) y _ {2} ^ {*} \right] \\ = f _ {1} (x) + f _ {2} (x). \\ \end{array}
$$

因此 $y_{1}^{*} + y_{2}^{*}$ 是方程(6-9)的一个特解.

这一定理通常称为线性微分方程的解的叠加原理.

定理 3 和定理 4 也可推广到 n 阶非齐次线性方程, 这里不再赘述.

# * 三、常数变易法

在第四节中,为解一阶非齐次线性方程,我们用了常数变易法.这方法的特点是:如果 $Cy_{1}(x)$ 是齐次线性方程的通解,那么,可以利用变换 $y=uy_{1}(x)$ (这变换是把齐次方程的通解中的任意常数 C 换成未知函数 $u(x)$ 而得到的)去解非齐次线性方程.这一方法也适用于解高阶线性方程.下面就二阶线性方程来作讨论.

如果已知齐次方程(6-6)的通解为

$$
Y (x) = C _ {1} y _ {1} (x) + C _ {2} y _ {2} (x),
$$

那么,可以用如下的常数变易法去求非齐次方程(6-5)的通解.令

$$
y = y _ {1} (x) v _ {1} + y _ {2} (x) v _ {2}, \tag {6-10}
$$

要确定未知函数 $v_{1}(x)$ 及 $v_{2}(x)$ 使 (6-10) 式所表示的函数满足非齐次方程 (6-5). 为此, 对 (6-10) 式求导, 得

$$
y ^ {\prime} = y _ {1} v _ {1} ^ {\prime} + y _ {2} v _ {2} ^ {\prime} + y _ {1} ^ {\prime} v _ {1} + y _ {2} ^ {\prime} v _ {2}.
$$

由于两个未知函数 $v_{1}, v_{2}$ 只需使(6-10)式所表示的函数满足一个关系式(6-5)，所以可规定它们再满足一个关系式。从 $y'$ 的上述表示式可看出，为了使 $y''$ 的表示式中不含 $v_{1}''$ 和 $v_{2}''$ ，可设

$$
y _ {1} v _ {1} ^ {\prime} + y _ {2} v _ {2} ^ {\prime} = 0, \tag {6-11}
$$

从而

$$
y ^ {\prime} = y _ {1} ^ {\prime} v _ {1} + y _ {2} ^ {\prime} v _ {2},
$$

再求导,得

$$
y ^ {\prime \prime} = y _ {1} ^ {\prime} v _ {1} ^ {\prime} + y _ {2} ^ {\prime} v _ {2} ^ {\prime} + y _ {1} ^ {\prime \prime} v _ {1} + y _ {2} ^ {\prime \prime} v _ {2}.
$$

把 $y, y', y''$ 代入方程(6-5)，得

$$
y _ {1} ^ {\prime} v _ {1} ^ {\prime} + y _ {2} ^ {\prime} v _ {2} ^ {\prime} + y _ {1} ^ {\prime \prime} v _ {1} + y _ {2} ^ {\prime \prime} v _ {2} + P \left(y _ {1} ^ {\prime} v _ {1} + y _ {2} ^ {\prime} v _ {2}\right) + Q \left(y _ {1} v _ {1} + y _ {2} v _ {2}\right) = f,
$$

整理得

$$
y _ {1} ^ {\prime} v _ {1} ^ {\prime} + y _ {2} ^ {\prime} v _ {2} ^ {\prime} + \left(y _ {1} ^ {\prime \prime} + P y _ {1} ^ {\prime} + Q y _ {1}\right) v _ {1} + \left(y _ {2} ^ {\prime \prime} + P y _ {2} ^ {\prime} + Q y _ {2}\right) v _ {2} = f.
$$

注意到 $y_{1}$ 及 $y_{2}$ 是齐次方程(6-6)的解, 故上式即为

$$
y _ {1} ^ {\prime} v _ {1} ^ {\prime} + y _ {2} ^ {\prime} v _ {2} ^ {\prime} = f. \tag {6-12}
$$

联立方程(6-11)与(6-12)，在系数行列式

$$
W = \left| \begin{array}{l l} y _ {1} & y _ {2} \\ y _ {1} ^ {\prime} & y _ {2} ^ {\prime} \end{array} \right| = y _ {1} y _ {2} ^ {\prime} - y _ {1} ^ {\prime} y _ {2} \neq 0
$$

时,可解得

$$
v _ {1} ^ {\prime} = - \frac {y _ {2} f}{W}, \quad v _ {2} ^ {\prime} = \frac {y _ {1} f}{W}.
$$

对上两式积分(假定 $f(x)$ 连续),得

$$
v _ {1} = C _ {1} + \int \left(- \frac {y _ {2} f}{W}\right) \mathrm{d} x, v _ {2} = C _ {2} + \int \frac {y _ {1} f}{W} \mathrm{d} x.
$$

于是得非齐次方程(6-5)的通解为

$$
y = C _ {1} y _ {1} + C _ {2} y _ {2} - y _ {1} \int \frac {y _ {2} f}{W} \mathrm{d} x + y _ {2} \int \frac {y _ {1} f}{W} \mathrm{d} x.
$$

例 3 已知齐次方程 $(x-1)y''-xy'+y=0$ 的通解为 $Y(x)=C_{1}x+C_{2}e^{x}$ ，求非齐次方程 $(x-1)y''-xy'+y=(x-1)^{2}$ 的通解.

解 把所给方程写成标准形式

$$
y ^ {\prime \prime} - \frac {x}{x - 1} y ^ {\prime} + \frac {1}{x - 1} y = x - 1.
$$

令 $y = xv_{1} + e^{x}v_{2}$ . 按照

$$
\left\{ \begin{array}{l} y _ {1} v _ {1} ^ {\prime} + y _ {2} v _ {2} ^ {\prime} = 0, \\ y _ {1} ^ {\prime} v _ {1} ^ {\prime} + y _ {2} ^ {\prime} v _ {2} ^ {\prime} = f. \end{array} \right.
$$

有

$$
\left\{ \begin{array}{l} x v _ {1} ^ {\prime} + \mathrm{e} ^ {x} v _ {2} ^ {\prime} = 0, \\ v _ {1} ^ {\prime} + \mathrm{e} ^ {x} v _ {2} ^ {\prime} = x - 1, \end{array} \right.
$$

解得

$$
v _ {1} ^ {\prime} = - 1, \quad v _ {2} ^ {\prime} = x \mathrm{e} ^ {- x}.
$$

积分,得

$$
v _ {1} = C _ {1} - x, \quad v _ {2} = C _ {2} - (x + 1) \mathrm{e} ^ {- x}.
$$

于是所求非齐次方程的通解为

$$
y = C _ {1} x + C _ {2} \mathrm{e} ^ {x} - (x ^ {2} + x + 1).
$$

如果只知齐次方程(6-6)的一个不恒为零的解 $y_{1}(x)$ ，那么，利用变换 $y = uy_{1}(x)$ ，可把非齐次方程(6-5)化为一阶线性方程.

事实上，把

$$
y = y _ {1} u, \quad y ^ {\prime} = y _ {1} u ^ {\prime} + y _ {1} ^ {\prime} u, \quad y ^ {\prime \prime} = y _ {1} u ^ {\prime \prime} + 2 y _ {1} ^ {\prime} u ^ {\prime} + y _ {1} ^ {\prime \prime} u
$$

代入方程(6-5)，得

$$
y _ {1} u ^ {\prime \prime} + 2 y _ {1} ^ {\prime} u ^ {\prime} + y _ {1} ^ {\prime \prime} u + P (y _ {1} u ^ {\prime} + y _ {1} ^ {\prime} u) + Q y _ {1} u = f,
$$

即

$$
y _ {1} u ^ {\prime \prime} + \left(2 y _ {1} ^ {\prime} + P y _ {1}\right) u ^ {\prime} + \left(y _ {1} ^ {\prime \prime} + P y _ {1} ^ {\prime} + Q y _ {1}\right) u = f,
$$

由于 $y_{1}^{\prime\prime} + Py_{1}^{\prime} + Qy_{1} \equiv 0$ ，故上式为

$$
y _ {1} u ^ {\prime \prime} + (2 y _ {1} ^ {\prime} + P y _ {1}) u ^ {\prime} = f.
$$

令 $u' = z$ ，上式即化为一阶线性方程

$$
y _ {1} z ^ {\prime} + (2 y _ {1} ^ {\prime} + P y _ {1}) z = f. \tag {6-13}
$$

把方程(6-5)化为方程(6-13)以后,按一阶线性方程的解法,设求得方程(6-13)的通解为

$$
z = C _ {2} Z (x) + z ^ {*} (x),
$$

积分得

$$
u = C _ {1} + C _ {2} U (x) + u ^ {*} (x) \quad (\text {其中} U ^ {\prime} (x) = Z (x), u ^ {* ^ {\prime}} (x) = z ^ {*} (x)),
$$

上式两端同乘 $y_{1}(x)$ ，便得方程(6-5)的通解

$$
y = C _ {1} y _ {1} (x) + C _ {2} U (x) y _ {1} (x) + u ^ {*} (x) y _ {1} (x).
$$

上述方法显然也适用于求齐次方程(6-6)的通解.

例 4 已知 $y_{1}(x)=\mathrm{e}^{x}$ 是齐次方程 $y''-2y'+y=0$ 的解, 求非齐次方程 $y''-2y'+y=\frac{1}{x}\mathrm{e}^{x}$ 的通解.

解 令 $y = \mathrm{e}^{x}u$ ，则 $y' = \mathrm{e}^{x}(u' + u), y'' = \mathrm{e}^{x}(u'' + 2u' + u)$ ，代入非齐次方程，得

$$
\mathrm{e} ^ {x} \left(u ^ {\prime \prime} + 2 u ^ {\prime} + u\right) - 2 \mathrm{e} ^ {x} \left(u ^ {\prime} + u\right) + \mathrm{e} ^ {x} u = \frac {1}{x} \mathrm{e} ^ {x},
$$

即

$$
\mathrm{e} ^ {x} u ^ {\prime \prime} = \frac {1}{x} \mathrm{e} ^ {x}, \quad u ^ {\prime \prime} = \frac {1}{x}.
$$

这里不需再作变换去化为一阶线性方程,只要直接积分,便得

$$
u ^ {\prime} = C + \ln | x |,
$$

再积分得

$$
u = C _ {1} + C x + x \ln | x | - x,
$$

即

$$
u = C _ {1} + C _ {2} x + x \ln | x | (C _ {2} = C - 1).
$$

于是所求通解为

$$
y = C _ {1} \mathrm{e} ^ {x} + C _ {2} x \mathrm{e} ^ {x} + x \mathrm{e} ^ {x} \ln | x |.
$$

# 习题7-6

1. 下列函数组在其定义区间内哪些是线性无关的？

(1) $x, x^2$ ; 

(2) $x, 2x$ ; 

(3) $\mathrm{e}^{2x}, 3\mathrm{e}^{2x}$ , 

(4) $\mathrm{e}^{-x},\mathrm{e}^{x}$ 

(5) $\cos 2x, \sin 2x$ ; 

(6) $e^{x^{2}}, xe^{x^{2}}$ ; 

(7) $\sin 2x, \cos x \sin x;$ 

(8) $e^{x}\cos2x$ , $e^{x}\sin2x$ ; 

(9) $\ln x, x \ln x$ ; 

(10) $e^{ax}, e^{bx} (a \neq b)$ . 

2. 验证 $y_{1}=\cos \omega x$ 及 $y_{2}=\sin \omega x$ 都是方程 $y''+\omega^{2}y=0$ 的解，并写出该方程的通解.

3. 验证 $y_{1} = \mathrm{e}^{x^{2}}$ 及 $y_{2} = x\mathrm{e}^{x^{2}}$ 都是方程 $y'' - 4xy' + (4x^2 - 2)y = 0$ 的解，并写出该方程的通解.

4. 验证：

(1) $y = C_1 e^x + C_2 e^{2x} + \frac{1}{12} e^{5x}$ ( $C_1, C_2$ 是任意常数) 是方程 $y'' - 3y' + 2y = e^{5x}$ 的通解；

(2) $y = C_{1} \cos 3x + C_{2} \sin 3x + \frac{1}{32} (4x \cos x + \sin x)$ ( $C_{1}, C_{2}$ 是任意常数) 是方程 $y'' + 9y = x \cos x$ 的通解；

(3) $y = C_1 x^2 + C_2 x^2 \ln x (C_1, C_2 \text{是任意常数})$ 是方程 $x^2 y'' - 3xy' + 4y = 0$ 的通解；

(4) $y = C_{1}x^{5} + \frac{C_{2}}{x} - \frac{x^{2}}{9}\ln x$ ( $C_{1}, C_{2}$ 是任意常数) 是方程 $x^{2}y'' - 3xy' - 5y = x^{2}\ln x$ 的通解；

(5) $y = \frac{1}{x} (C_1 e^x + C_2 e^{-x}) + \frac{e^x}{2} (C_1, C_2 \text{是任意常数})$ 是方程 $xy'' + 2y' - xy = e^x$ 的通解；

(6) $y = C_1 e^x + C_2 e^{-x} + C_3 \cos x + C_4 \sin x - x^2$ ( $C_1, C_2, C_3, C_4$ 是任意常数) 是方程 $y^{(4)} - y = x^2$ 的通解.

*5. 已知 $y_{1}(x) = \mathrm{e}^{x}$ 是齐次线性方程

$$
(2 x - 1) y ^ {\prime \prime} - (2 x + 1) y ^ {\prime} + 2 y = 0
$$

的一个解,求此方程的通解.

*6. 已知 $y_{1}(x) = x$ 是齐次线性方程 $x^{2}y'' - 2xy' + 2y = 0$ 的一个解, 求非齐次线性方程 $x^{2}y'' - 2xy' + 2y'$ 

$2y=2x^{3}$ 的通解.

* 7. 已知齐次线性方程 $y'' + y = 0$ 的通解为 $Y(x) = C_1\cos x + C_2\sin x$ ，求非齐次线性方程 $y'' + y = \sec x$ 的通解.

*8. 已知齐次线性方程 $x^{2}y'' - xy' + y = 0$ 的通解为 $Y(x) = C_{1}x + C_{2}x\ln |x|$ , 求非齐次线性方程 $x^{2}y'' - xy' + y = x$ 的通解.

# 第七节 常系数齐次线性微分方程

先讨论二阶常系数齐次线性微分方程的解法,再把二阶方程的解法推广到 n 阶方程.

在二阶齐次线性微分方程

$$
y ^ {\prime \prime} + P (x) y ^ {\prime} + Q (x) y = 0 \tag {7-1}
$$

中,如果 $y'$ , y 的系数 $P(x)$ , $Q(x)$ 均为常数, 即(7-1)式成为

$$
y ^ {\prime \prime} + p y ^ {\prime} + q y = 0, \tag {7-2}
$$

其中 p, q 是常数, 那么称 (7-2) 为二阶常系数齐次线性微分方程. 如果 p, q 不全为常数, 称 (7-1) 为二阶变系数齐次线性微分方程.

由上节讨论可知,要找微分方程(7-2)的通解,可以先求出它的两个解 $y_{1}, y_{2}$ , 如果它们之比不为常数, 即 $y_{1}$ 与 $y_{2}$ 线性无关, 那么 $y = C_{1}y_{1} + C_{2}y_{2}$ 就是方程(7-2)的通解.

当 r 为常数时, 指数函数 $y = e^{rx}$ 和它的各阶导数都只相差一个常数因子. 由于指数函数有这个特点, 因此我们用 $y = e^{rx}$ 来尝试, 看能否选取适当的常数 r, 使 $y = e^{rx}$ 满足方程 (7-2).

将 $y=e^{rx}$ 求导①, 得到

$$
y ^ {\prime} = r \mathrm{e} ^ {r x}, \quad y ^ {\prime \prime} = r ^ {2} \mathrm{e} ^ {r x}
$$

把 $y, y'$ 和 $y''$ 代入方程(7-2)，得

$$
\left(r ^ {2} + p r + q\right) \mathrm{e} ^ {r x} = 0.
$$

由于 $\mathrm{e}^{rx}\neq 0$ ，所以

$$
r ^ {2} + p r + q = 0. \tag {7-3}
$$

① 当 $r$ 为复数 $a + bi, x$ 为实变量时，导数公式 $\frac{\mathrm{d}}{\mathrm{d}x}\mathrm{e}^{rx} = r\mathrm{e}^{rx}$ 仍成立.事实上，对欧拉公式

$$
\mathrm{e} ^ {(a + b \mathrm{i}) x} = \mathrm{e} ^ {a x} (\cos b x + \mathrm{i} \sin b x)
$$

两端求导,得

$$
\frac {\mathrm{d}}{\mathrm{d} x} \mathrm{e} ^ {(a + b \mathrm{i}) x} = a \mathrm{e} ^ {a x} (\cos b x + \mathrm{i} \sin b x) + \mathrm{e} ^ {a x} (- b \sin b x + \mathrm{i} b \cos b x)
$$

$$
= (a + b \mathrm{i}) \mathrm{e} ^ {a x} (\cos b x + \mathrm{i} \sin b x) = (a + b \mathrm{i}) \mathrm{e} ^ {(a + b \mathrm{i}) x}.
$$

由此可见, 只要 r 满足代数方程(7-3), 函数 $y = e^{rx}$ 就是微分方程(7-2)的解, 我们把代数方程(7-3)叫做微分方程(7-2)的特征方程.

特征方程(7-3)是一个二次代数方程,其中 $r^{2}$ ,r的系数及常数项恰好依次是微分方程(7-2)中 $y''$ , $y'$ 及y的系数.

特征方程(7-3)的两个根 $r_{1}, r_{2}$ 可以用公式

$$
r _ {1, 2} = \frac {- p \pm \sqrt {p ^ {2} - 4 q}}{2}
$$

求出. 它们有三种不同的情形:

(i) 当 $p^{2}-4q>0$ 时, $r_{1}, r_{2}$ 是两个不相等的实根

$$
r _ {1} = \frac {- p + \sqrt {p ^ {2} - 4 q}}{2}, \quad r _ {2} = \frac {- p - \sqrt {p ^ {2} - 4 q}}{2};
$$

(ii) 当 $p^2 - 4q = 0$ 时, $r_1, r_2$ 是两个相等的实根

$$
r _ {1} = r _ {2} = - \frac {p}{2};
$$

(iii) 当 $p^{2}-4q<0$ 时, $r_{1}, r_{2}$ 是一对共轭复根

$$
r _ {1} = \alpha + \beta \mathrm{i}, \quad r _ {2} = \alpha - \beta \mathrm{i},
$$

其中

$$
\alpha = - \frac {p}{2}, \quad \beta = \frac {\sqrt {4 q - p ^ {2}}}{2}.
$$

相应地,微分方程(7-2)的通解也有三种不同的情形.分别讨论如下:

(i) 特征方程有两个不相等的实根: $r_{1} \neq r_{2}$ 

由上面的讨论知道, $y_{1}=e^{r_{1}x},y_{2}=e^{r_{2}x}$ 是微分方程(7-2)的两个解,并且 $\frac{y_{2}}{y_{1}}=\frac{e^{r_{2}x}}{e^{r_{1}x}}=e^{(r_{2}-r_{1})x}$ 不是常数,因此微分方程(7-2)的通解为

$$
y = C _ {1} \mathrm{e} ^ {r _ {1} x} + C _ {2} \mathrm{e} ^ {r _ {2} x}.
$$

(ii) 特征方程有两个相等的实根: $r_{1}=r_{2}$ 

这时, 只得到微分方程(7-2)的一个解

$$
y _ {1} = \mathrm{e} ^ {r _ {1} x}.
$$

为了得出微分方程(7-2)的通解, 还需求出另一个解 $y_{2}$ , 并且要求 $\frac{y_{2}}{y_{1}}$ 不是常数. 设 $\frac{y_{2}}{y_{1}} = u(x)$ , 即 $y_{2} = e^{r_{1}x} u(x)$ . 下面来求 $u(x)$ . 将 $y_{2}$ 求导, 得

$$
\begin{array}{l} y _ {2} ^ {\prime} = \mathrm{e} ^ {r _ {1} x} (u ^ {\prime} + r _ {1} u), \\ y _ {2} ^ {\prime \prime} = \mathrm{e} ^ {r _ {1} x} \left(u ^ {\prime \prime} + 2 r _ {1} u ^ {\prime} + r _ {1} ^ {2} u\right), \\ \end{array}
$$

将 $y_{2}, y_{2}^{\prime}$ 和 $y_{2}^{\prime \prime}$ 代入微分方程(7-2)，得

$$
\mathrm{e} ^ {r _ {1} x} \left[ \left(u ^ {\prime \prime} + 2 r _ {1} u ^ {\prime} + r _ {1} ^ {2} u\right) + p \left(u ^ {\prime} + r _ {1} u\right) + q u \right] = 0,
$$

约去 $\mathrm{e}^{r_1x}$ ，并合并同类项，得

$$
u ^ {\prime \prime} + (2 r _ {1} + p) u ^ {\prime} + (r _ {1} ^ {2} + p r _ {1} + q) u = 0.
$$

由于 $r_1$ 是特征方程(7-3)的二重根. 因此 $r_1^2 + pr_1 + q = 0$ , 且 $2r_1 + p = 0$ , 于是得

$$
u ^ {\prime \prime} = 0.
$$

因为这里只要得到一个不为常数的解,所以不妨选取 u=x, 由此得到微分方程(7-2)的另一个解

$$
y _ {2} = x \mathrm{e} ^ {r _ {1} x}.
$$

从而微分方程(7-2)的通解为

$$
y = C _ {1} \mathrm{e} ^ {r _ {1} x} + C _ {2} x \mathrm{e} ^ {r _ {1} x},
$$

即

$$
y = \left(C _ {1} + C _ {2} x\right) \mathrm{e} ^ {r _ {1} x}.
$$

(iii) 特征方程有一对共轭复根: $r_{1}=\alpha+\beta i, r_{2}=\alpha-\beta i (\beta \neq 0)$ 

这时, $y_{1}=e^{(\alpha+\beta i)x},y_{2}=e^{(\alpha-\beta i)x}$ 是微分方程(7-2)的两个解,但它们是复值函数形式.为了得出实值函数形式的解,先利用欧拉公式 $e^{i\theta}=\cos\theta+i\sin\theta$ 把 $y_{1},y_{2}$ 改写为

$$
y _ {1} = \mathrm{e} ^ {(\alpha + \beta \mathrm{i}) x} = \mathrm{e} ^ {\alpha x} \cdot \mathrm{e} ^ {\beta x \mathrm{i}} = \mathrm{e} ^ {\alpha x} (\cos \beta x + \mathrm{i} \sin \beta x),
$$

$$
y _ {2} = \mathrm{e} ^ {(\alpha - \beta \mathrm{i}) x} = \mathrm{e} ^ {\alpha x} \cdot \mathrm{e} ^ {- \beta x \mathrm{i}} = \mathrm{e} ^ {\alpha x} (\cos \beta x - \mathrm{i} \sin \beta x).
$$

由于复值函数 $y_{1}$ 与 $y_{2}$ 之间成共轭关系, 因此, 取它们的和除以 2 就得到它们的实部, 取它们的差除以 2i 就得到它们的虚部. 由于方程 (7-2) 的解符合叠加原理, 所以实值函数

$$
\overline {{{y}}} _ {1} = \frac {1}{2} (y _ {1} + y _ {2}) = \mathrm{e} ^ {\alpha x} \cos \beta x, \quad \overline {{{y}}} _ {2} = \frac {1}{2 \mathrm{i}} (y _ {1} - y _ {2}) = \mathrm{e} ^ {\alpha x} \sin \beta x
$$

还是微分方程(7-2)的解,且 $\frac{\overline{y}_{1}}{\overline{y}_{2}}=\frac{e^{\alpha x}\cos\beta x}{e^{\alpha x}\sin\beta x}=\cot\beta x$ 不是常数,所以微分方程(7-2)的通解为

$$
y = \mathrm{e} ^ {\alpha x} \left(C _ {1} \cos \beta x + C _ {2} \sin \beta x\right).
$$

综上所述,求二阶常系数齐次线性微分方程

$$
y ^ {\prime \prime} + p y ^ {\prime} + q y = 0 \tag {7-2}
$$

的通解的步骤如下：

第一步 写出微分方程(7-2)的特征方程

$$
r ^ {2} + p r + q = 0. \tag {7-3}
$$

第二步 求出特征方程(7-3)的两个根 $r_1, r_2$ .

第三步 根据特征方程(7-3)的两个根的不同情形,按照下列表格写出微分方程(7-2)的通解:

<table><tr><td>特征方程<eq>r^{2}+pr+q=0</eq>的两个根<eq>r_{1},r_{2}</eq></td><td>微分方程<eq>y&#x27;&#x27;+py&#x27;+qy=0</eq>的通解</td></tr><tr><td>两个不相等的实根<eq>r_{1},r_{2}</eq></td><td><eq>y=C_{1}e^{r_{1}x}+C_{2}e^{r_{2}x}</eq></td></tr><tr><td>两个相等的实根<eq>r_{1}=r_{2}</eq></td><td><eq>y=(C_{1}+C_{2}x)e^{r_{1}x}</eq></td></tr><tr><td>一对共轭复根<eq>r_{1,2}=\alpha\pm\beta i</eq></td><td><eq>y=e^{\alpha x}(C_{1}\cos\beta x+C_{2}\sin\beta x)</eq></td></tr></table>

例 1 求微分方程 $y''-2y'-3y=0$ 的通解.

解 所给微分方程的特征方程为

$$
r ^ {2} - 2 r - 3 = 0,
$$

其根 $r_1 = -1, r_2 = 3$ 是两个不相等的实根，因此所求通解为

$$
y = C _ {1} \mathrm{e} ^ {- x} + C _ {2} \mathrm{e} ^ {3 x}.
$$

例2 求方程 $\frac{\mathrm{d}^2s}{\mathrm{d}t^2} + 2\frac{\mathrm{d}s}{\mathrm{d}t} + s = 0$ 满足初值条件 $s|_{t=0} = 4, s' |_{t=0} = -2$ 的特解.

解 所给方程的特征方程为

$$
r ^ {2} + 2 r + 1 = 0,
$$

其根 $r_1 = r_2 = -1$ 是两个相等的实根，因此所求微分方程的通解为

$$
s = \left(C _ {1} + C _ {2} t\right) \mathrm{e} ^ {- t}.
$$

将条件 $s|_{t = 0} = 4$ 代入通解，得 $C_1 = 4$ ，从而

$$
s = (4 + C _ {2} t) \mathrm{e} ^ {- t}.
$$

将上式对 t 求导, 得

$$
s ^ {\prime} = \left(C _ {2} - 4 - C _ {2} t\right) \mathrm{e} ^ {- t}.
$$

再把条件 $s^{\prime}\mid_{t = 0} = -2$ 代入上式，得 $C_2 = 2.$ 于是所求特解为

$$
s = (4 + 2 t) \mathrm{e} ^ {- t}.
$$

例 3 求微分方程 $y''-2y'+5y=0$ 的通解.

解 所给方程的特征方程为

$$
r ^ {2} - 2 r + 5 = 0,
$$

其根 $r_{1,2}=1\pm2i$ 为一对共轭复根.因此所求通解为

$$
y = \mathrm{e} ^ {x} \left(C _ {1} \cos 2 x + C _ {2} \sin 2 x\right).
$$

例 4 在第六节例 1 中, 设物体只受弹性恢复力 f 的作用, 且在初始时刻 t=0 的位置为 $x=x_{0}$ , 初始速度为 $\frac{dx}{dt}\bigg|_{t=0}=v_{0}$ . 求反映物体运动规律的函数 $x=x(t)$ .

解 由于不计阻力 R，即假设 $-\mu \frac{dx}{dt}=0$ ，所以方程(6-1)成为

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} + k ^ {2} x = 0, \tag {7-4}
$$

方程(7-4)叫做无阻尼自由振动的微分方程.

反映物体运动规律的函数 $x = x(t)$ 是满足微分方程(7-4)及初值条件

$$
x \mid_ {t = 0} = x _ {0}, \frac {\mathrm{d} x}{\mathrm{d} t} \Big | _ {t = 0} = v _ {0}
$$

的特解.

方程(7-4)的特征方程为 $r^{2}+k^{2}=0$ ，其根 $r=\pm ki$ 是一对共轭复根，所以方程(7-4)的通解为

$$
x = C _ {1} \cos k t + C _ {2} \sin k t.
$$

应用初值条件,定出 $C_{1}=x_{0}, C_{2}=\frac{v_{0}}{k}$ . 因此,所求的特解为

$$
x = x _ {0} \cos k t + \frac {v _ {0}}{k} \sin k t. \tag {7-5}
$$

为了便于说明特解所反映的振动现象,我们令

$$
x _ {0} = A \sin \varphi , \quad \frac {v _ {0}}{k} = A \cos \varphi (0 \leqslant \varphi <   2 \pi),
$$

于是(7-5)式成为

$$
x = A \sin (k t + \varphi), \tag {7-6}
$$

其中

$$
A = \sqrt {x _ {0} ^ {2} + \frac {v _ {0} ^ {2}}{k ^ {2}}}, \quad \tan \varphi = \frac {k x _ {0}}{v _ {0}}.
$$

函数(7-6)的图形如图7-10所示(图中假定 $x_{0}>0,v_{0}>0$ ).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/b031bbd1a93c42f627b8b3bb076b98122a0f1547acc318620aeb690fe3dee9ae.jpg)



图7-10


函数(7-6)所反映的运动就是简谐振动.这个振动的振幅为 $A$ , 初相为 $\varphi$ , 周期为 $T = \frac{2\pi}{k}$ , 角频率为 $k$ . 由于 $k = \sqrt{\frac{c}{m}}$ (见第六节例1), 它与初值条件无关, 而完全由振动系统 (在本例中就是弹簧和物体所组成的系统) 本身所确定. 因此, $k$ 又叫做系统的固有频率. 固有频率是反映振动系统特性的一个重要参数.

例5 在第六节例1中,设物体受弹簧的恢复力f和阻力R的作用,且在初始时刻t=0的位置 $x=x_{0}$ ,初始速度 $\frac{dx}{dt}\bigg|_{t=0}=v_{0}$ ,求反映物体运动规律的函数 $x=x(t)$ .

解 这就是要找满足有阻尼的自由振动方程

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} + 2 n \frac {\mathrm{d} x}{\mathrm{d} t} + k ^ {2} x = 0 \tag {7-7}
$$

及初值条件

$$
x \mid_ {t = 0} = x _ {0}, \quad \frac {\mathrm{d} x}{\mathrm{d} t} \Big | _ {t = 0} = v _ {0}
$$

的特解.

方程(7-7)的特征方程为 $r^{2}+2nr+k^{2}=0$ ，其根为

$$
r = \frac {- 2 n \pm \sqrt {4 n ^ {2} - 4 k ^ {2}}}{2} = - n \pm \sqrt {n ^ {2} - k ^ {2}}.
$$

以下按 $n < k, n > k$ 及 $n = k$ 三种不同情形分别进行讨论.

(i) 小阻尼情形: n < k

特征方程的根 $r = -n \pm \omega i (\omega = \sqrt{k^{2} - n^{2}})$ 是一对共轭复根, 所以方程 (7-7) 的通解为

$$
x = \mathrm{e} ^ {- n t} \left(C _ {1} \cos \omega t + C _ {2} \sin \omega t\right).
$$

应用初值条件定出 $C_1 = x_0, C_2 = \frac{v_0 + nx_0}{\omega}$ , 因此所求特解为

$$
x = \mathrm{e} ^ {- n t} \left(x _ {0} \cos \omega t + \frac {v _ {0} + n x _ {0}}{\omega} \sin \omega t\right). \tag {7-8}
$$

如例 4 中所做的那样,令

$$
x _ {0} = A \sin \varphi , \quad \frac {v _ {0} + n x _ {0}}{\omega} = A \cos \varphi (0 \leqslant \varphi <   2 \pi), \tag {7-9}
$$

那么(7-8)式又可写成

$$
x = A \mathrm{e} ^ {- n t} \sin (\omega t + \varphi), \tag {7-10}
$$

其中

$$
\omega = \sqrt {k ^ {2} - n ^ {2}}, \quad A = \sqrt {x _ {0} ^ {2} + \frac {\left(v _ {0} + n x _ {0}\right) ^ {2}}{\omega^ {2}}}, \quad \tan \varphi = \frac {x _ {0} \omega}{v _ {0} + n x _ {0}}.
$$

从(7-10)式看出,物体的运动是周期为 $T=\frac{2\pi}{\omega}$ 的振动.但与简谐振动不同,它的振幅 $Ae^{-nt}$ 随时间 t 的增大而逐渐减小.因此,物体随时间 t 的增大而趋于平衡位置.

函数(7-10)的图形如图7-11所示(图中假定 $x_{0}=0,v_{0}>0$ ).

(ii) 大阻尼情形: n > k

特征方程的根 $r_1 = -n + \sqrt{n^2 - k^2}, r_2 = -n - \sqrt{n^2 - k^2}$ 是两个不相等的负实根，所以方程(7-7)的通解为

$$
x = C _ {1} \mathrm{e} ^ {- (n - \sqrt {n ^ {2} - k ^ {2}}) t} + C _ {2} \mathrm{e} ^ {- (n + \sqrt {n ^ {2} - k ^ {2}}) t}, \tag {7-11}
$$

其中任意常数 $C_1, C_2$ 可以由初值条件来确定.

从(7-11)式看出,使 x=0 的 t 值最多只有一个,即物体最多越过平衡位置一次,因此物体已不再有振动现象.又当 $t \to +\infty$ 时, $x \to 0$ . 因此,物体随时间 t 的增大而趋于平衡位置.

函数(7-11)的图形如图7-12所示(图中假定 $x_{0}>0,v_{0}>0$ ).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/f2fc087d8199845f13e062c7ddeba62376bd87f036ff0713ec9a1b8a08ca68d3.jpg)



图7-11


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/2dbaf1510bf12ae05199305e1b35bcf3277dd06e27adaa7226250e4b483f528d.jpg)



图7-12


(iii) 临界阻尼情形: n = k

特征方程的根 $r_1 = r_2 = -n$ 是两个相等的实根，所以方程(7-7)的通解为

$$
x = \mathrm{e} ^ {- n t} \left(C _ {1} + C _ {2} t\right),
$$

其中任意常数 $C_1$ 及 $C_2$ 可由初值条件来确定. 由上式可看出, 在临界阻尼情形使 $x = 0$ 的 $t$ 值也最多只有一个, 因此物体也不再有振动现象. 又由于

$$
\lim _ {t \rightarrow + \infty} t \mathrm{e} ^ {- n t} = \lim _ {t \rightarrow + \infty} \frac {t}{\mathrm{e} ^ {n t}} = \lim _ {t \rightarrow + \infty} \frac {1}{n \mathrm{e} ^ {n t}} = 0,
$$

从而可以看出, 当 $t \to +\infty$ 时, $x \to 0$ . 因此, 在临界阻尼情形, 物体也随时间 t 的增大而趋于平衡位置.

上面讨论二阶常系数齐次线性微分方程所用的方法以及方程的通解的形式,可推广到 n 阶常系数齐次线性微分方程上去,对此我们不再详细讨论,只简单地叙述于下:

n 阶常系数齐次线性微分方程的一般形式是

$$
y ^ {(n)} + p _ {1} y ^ {(n - 1)} + p _ {2} y ^ {(n - 2)} + \dots + p _ {n - 1} y ^ {\prime} + p _ {n} y = 0, \tag {7-12}
$$

其中 $p_{1}, p_{2}, \cdots, p_{n-1}, p_{n}$ 都是常数.

有时我们用记号 D（叫做微分算子）表示对 x 求导的运算 $\frac{d}{dx}$ ，把 $\frac{dy}{dx}$ 记作 Dy，把 $\frac{d^{n}y}{dx^{n}}$ 记作 $D^{n}y$ ，并把方程(7-12)记作

$$
\left(\mathrm{D} ^ {n} + p _ {1} \mathrm{D} ^ {n - 1} + \dots + p _ {n - 1} \mathrm{D} + p _ {n}\right) y = 0. \tag {7-13}
$$

记

$$
L (\mathrm{D}) = \mathrm{D} ^ {n} + p _ {1} \mathrm{D} ^ {n - 1} + \dots + p _ {n - 1} \mathrm{D} + p _ {n},
$$

$L(\mathrm{D})$ 叫做微分算子 $\mathrm{D}$ 的 $n$ 次多项式.于是方程(7-13)可记作

$$
L (\mathrm{D}) \gamma = 0.
$$

如同讨论二阶常系数齐次线性微分方程那样, 令 $y = \mathrm{e}^{rx}$ . 由于 $\mathrm{De}^{rx} = r\mathrm{e}^{rx}, \cdots, \mathrm{D}^n\mathrm{e}^{rx} = r^n\mathrm{e}^{rx}$ , 故 $L(\mathrm{D})\mathrm{e}^{rx} = L(r)\mathrm{e}^{rx}$ . 因此把 $y = \mathrm{e}^{rx}$ 代入方程 (7-13), 得

$$
L (r) \mathrm{e} ^ {r x} = 0.
$$

由此可见,如果选取 r 是 n 次代数方程 $L(r)=0$ 即

$$
r ^ {n} + p _ {1} r ^ {n - 1} + p _ {2} r ^ {n - 2} + \dots + p _ {n - 1} r + p _ {n} = 0 \tag {7-14}
$$

的根,那么作出的函数 $y=e^{rx}$ 就是方程(7-13)的一个解.

方程(7-14)叫做方程(7-13)的特征方程.

根据特征方程的根,可以写出其对应的微分方程的解如下:

<table><tr><td>特征方程的根</td><td>微分方程通解中的对应项</td></tr><tr><td>单实根r</td><td>给出一项:<eq>Ce^{rx}</eq></td></tr><tr><td>一对单复根<eq>r_{1,2}=\alpha\pm\beta i</eq></td><td>给出两项:<eq>e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)</eq></td></tr><tr><td>k重实根r</td><td>给出k项:<eq>e^{rx}(C_1+C_2x+\cdots+C_kx^{k-1})</eq></td></tr><tr><td>一对k重复根<eq>r_{1,2}=\alpha\pm\beta i</eq></td><td>给出2k项:<eq>e^{\alpha x}\left[(C_1+C_2x+\cdots+C_kx^{k-1})\cos\beta x+(D_1+D_2x+\cdots+D_kx^{k-1})\sin\beta x\right]</eq></td></tr></table>

从代数学知道, $n$ 次代数方程有 $n$ 个根(重根按重数计算), 而特征方程的每一个根都对应着通解中的一项, 且每项各含一个任意常数, 这样就得到 $n$ 阶常系数齐次线性微分方程的通解

$$
y = C _ {1} y _ {1} + C _ {2} y _ {2} + \dots + C _ {n} y _ {n}.
$$

例 6 求方程 $y^{(4)}-2y'''+5y''=0$ 的通解.

解 这里的特征方程为

$$
r ^ {4} - 2 r ^ {3} + 5 r ^ {2} = 0,
$$

即

$$
r ^ {2} (r ^ {2} - 2 r + 5) = 0.
$$

它的根是 $r_1 = r_2 = 0$ 和 $r_{3,4} = 1 \pm 2\mathrm{i}$ . 因此所给微分方程的通解为

$$
y = C _ {1} + C _ {2} x + \mathrm{e} ^ {x} \left(C _ {3} \cos 2 x + C _ {4} \sin 2 x\right).
$$

例 7 求方程 $\frac{d^{4}w}{dx^{4}}+\beta^{4}w=0$ 的通解, 其中 $\beta>0$ .

解 这里的特征方程为

$$
r ^ {4} + \beta^ {4} = 0.
$$

由于

$$
r ^ {4} + \beta^ {4} = r ^ {4} + 2 r ^ {2} \beta^ {2} + \beta^ {4} - 2 r ^ {2} \beta^ {2} = (r ^ {2} + \beta^ {2}) ^ {2} - 2 r ^ {2} \beta^ {2} = (r ^ {2} - \sqrt {2} \beta r + \beta^ {2}) (r ^ {2} + \sqrt {2} \beta r + \beta^ {2}),
$$

所以特征方程可以写为

$$
\left(r ^ {2} - \sqrt {2} \beta r + \beta^ {2}\right) \left(r ^ {2} + \sqrt {2} \beta r + \beta^ {2}\right) = 0.
$$

它的根为 $r_{1,2} = \frac{\beta}{\sqrt{2}} (1\pm \mathrm{i}), r_{3,4} = -\frac{\beta}{\sqrt{2}} (1\pm \mathrm{i})$ ，因此所给方程的通解为

$$
w = \mathrm{e} ^ {\frac {\beta}{\sqrt {2}} x} \left(C _ {1} \cos \frac {\beta}{\sqrt {2}} x + C _ {2} \sin \frac {\beta}{\sqrt {2}} x\right) + \mathrm{e} ^ {- \frac {\beta}{\sqrt {2}} x} \left(C _ {3} \cos \frac {\beta}{\sqrt {2}} x + C _ {4} \sin \frac {\beta}{\sqrt {2}} x\right).
$$

# 习题7-7

1. 下题中给出了四个结论,从中选一个正确的结论:

在下列微分方程中，以 $y=C_{1}e^{-x}+C_{2}\cos x+C_{3}\sin x$ ( $C_{1},C_{2},C_{3}$ 为任意常数) 为通解的常系数齐次线性微分方程是().

(A) $y''' + y'' - y' - y = 0$ 

(B) $y''' + y'' + y' + y = 0$ 

(C) $y'''-y''-y'+y=0$ 

(D) $y'''-y''-y'-y=0$ 

2. 求下列微分方程的通解：

(1) $y'' + y' - 2y = 0$ ; 

(2) $y''-4y'=0;$ 

(3) $y'' + y = 0;$ 

(4) $y'' + 6y' + 13y = 0$ ; 

(5) $4\frac{d^{2}x}{dt^{2}}-20\frac{dx}{dt}+25x=0;$ 

(6) $y''-4y'+5y=0;$ 

(7) $y^{(4)} - y = 0;$ 

(8) $y^{(4)}+2y''+y=0;$ 

(9) $y^{(4)}-2y'''+y''=0;$ 

(10) $y^{(4)}+5y''-36y=0.$ 

3. 求下列微分方程满足所给初值条件的特解：

(1) $y'' - 4y' + 3y = 0, y \mid_{x=0} = 6, y' \mid_{x=0} = 10;$ 

(2) $4y'' + 4y' + y = 0, y \mid_{x=0} = 2, y' \mid_{x=0} = 0$ ; 

(3) $y'' - 3y' - 4y = 0, y \mid_{x=0} = 0, y' \mid_{x=0} = -5;$ 

(4) $y'' + 4y' + 29y = 0, y \mid_{x=0} = 0, y' \mid_{x=0} = 15;$ 

(5) $y'' + 25y = 0, y \mid_{x=0} = 2, y' \mid_{x=0} = 5;$ 

(6) $y'' - 4y' + 13y = 0, y \big|_{x=0} = 0, y' \big|_{x=0} = 3.$ 

4. 一个单位质量的质点在数轴上运动, 开始时质点在原点 O 处且速度为 $v_{0}$ , 在运动过程中, 它

受到一个力的作用,这个力的大小与质点到原点的距离成正比(比例系数 $k_{1}>0$ )而方向与初速度一致.又介质的阻力与速度成正比(比例系数 $k_{2}>0$ ).求反映这质点的运动规律的函数.

5. 在图 7-13 所示的电路中先将开关 S 拨向 A，达到稳定状态后再将开关 S 拨向 B，求电压 $u_{C}(t)$ 及电流 $i(t)$ . 已知 E = 20 V, $C = 0.5 \times 10^{-6}$ F, L = 0.1 H, R = 2000 Ω.

6. 设圆柱形浮筒的底面直径为 0.5 m, 将它铅直放在水中, 当稍向下压后突然放开, 浮筒在水中上下振动的周期为 2 s, 求浮筒的质量.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/0e1a8fb097851f1032916cd0f37ac2456c7c62260b417e8169f8bc9c9a4a92e6.jpg)



图7-13


# 第八节 常系数非齐次线性微分方程

本节着重讨论二阶常系数非齐次线性微分方程的解法,并对 n 阶方程的解法作必要的说明.

二阶常系数非齐次线性微分方程的一般形式是

$$
y ^ {\prime \prime} + p y ^ {\prime} + q y = f (x), \tag {8-1}
$$

其中 p, q 是常数.

由第六节定理 3 可知, 求二阶常系数非齐次线性微分方程的通解, 归结为求对应的齐次方程

$$
y ^ {\prime \prime} + p y ^ {\prime} + q y = 0 \tag {8-2}
$$

的通解和非齐次方程(8-1)本身的一个特解.由于二阶常系数齐次线性微分方程的通解的求法已在第七节得到解决,所以这里只需讨论求二阶常系数非齐次线性微分方程的一个特解 $y^{*}$ 的方法.

本节只介绍当方程(8-1)中的 $f(x)$ 取两种常见形式时求 $y^{*}$ 的方法.这种方法的特点是不用积分就可求出 $y^{*}$ 来,它叫做待定系数法. $f(x)$ 的两种形式是

(1) $f(x)=\mathrm{e}^{\lambda x}P_{m}(x)$ ，其中 $\lambda$ 是常数， $P_{m}(x)$ 是x的一个m次多项式

$$
P _ {m} (x) = a _ {0} x ^ {m} + a _ {1} x ^ {m - 1} + \dots + a _ {m - 1} x + a _ {m};
$$

(2) $f(x) = \mathrm{e}^{\lambda x}\left[P_l(x)\cos \omega x + Q_n(x)\sin \omega x\right]$ , 其中 $\lambda, \omega$ 是常数, $\omega \neq 0, P_l(x), Q_n(x)$ 分别是 $x$ 的 $l$ 次、 $n$ 次多项式, 且仅有一个可为零.

下面分别介绍 $f(x)$ 为上述两种形式时 $y^{*}$ 的求法.

# 一、 $f(x) = \mathrm{e}^{\lambda x}P_m(x)$ 型

我们知道,方程(8-1)的特解 $y^{*}$ 是使(8-1)成为恒等式的函数.怎样的函数能使(8-1)成为恒等式呢？因为(8-1)式右端 $f(x)$ 是多项式 $P_{m}(x)$ 与指数函数 $e^{\lambda x}$ 的乘积，而多项式与指数函数乘积的导数仍然是多项式与指数函数的乘积，因此，我们推测 $y^{*}=R(x)e^{\lambda x}$ （其中 $R(x)$ 是某个多项式）可能是方程(8-1)的特解。把 $y^{*},y^{*}$ 及 $y^{*}$ 代入方程(8-1)，然后考虑能否选取适当的多项式 $R(x)$ ，使 $y^{*}=R(x)e^{\lambda x}$ 满足方程(8-1)。为此，将

$$
\begin{array}{l} y ^ {*} = R (x) \mathrm{e} ^ {\lambda x}, \\ y ^ {* \prime} = \mathrm{e} ^ {\lambda x} [ \lambda R (x) + R ^ {\prime} (x) ], \\ y ^ {* \prime \prime} = e ^ {\lambda x} \left[ \lambda^ {2} R (x) + 2 \lambda R ^ {\prime} (x) + R ^ {\prime \prime} (x) \right] \\ \end{array}
$$

代入方程(8-1)并消去 $\mathbf{e}^{\lambda x}$ , 得

$$
R ^ {\prime \prime} (x) + (2 \lambda + p) R ^ {\prime} (x) + \left(\lambda^ {2} + p \lambda + q\right) R (x) = P _ {m} (x). \tag {8-3}
$$

(i) 如果 $\lambda$ 不是(8-2)式的特征方程 $r^2 + pr + q = 0$ 的根, 即 $\lambda^2 + p\lambda + q \neq 0$ , 由于 $P_m(x)$ 是一个 $m$ 次多项式, 要使(8-3)的两端恒等, 那么可令 $R(x)$ 为另一个 $m$ 次多项式 $R_m(x)$ :

$$
R _ {m} (x) = b _ {0} x ^ {m} + b _ {1} x ^ {m - 1} + \dots + b _ {m - 1} x + b _ {m},
$$

代入(8-3)式, 比较等式两端 x 同次幂的系数, 就得到以 $b_{0}, b_{1}, \cdots, b_{m}$ 作为未知数的 $m+1$ 个方程的联立方程组. 从而可以定出这些 $b_{i} (i=0,1,\cdots,m)$ , 并得到所求的特解 $y^{*}=R_{m}(x)e^{\lambda x}$ .

（ii）如果 $\lambda$ 是特征方程 $r^2 + pr + q = 0$ 的单根，即 $\lambda^2 + p\lambda + q = 0$ ，但 $2\lambda + p \neq 0$ ，要使(8-3)的两端恒等，那么 $R'(x)$ 必须是 $m$ 次多项式.此时可令

$$
R (x) = x R _ {m} (x),
$$

并且可用同样的方法来确定 $R_{m}(x)$ 的系数 $b_{i}$ ( $i=0,1,2,\cdots,m$ ).

（iii）如果 $\lambda$ 是特征方程 $r^2 + pr + q = 0$ 的重根，即 $\lambda^2 + p\lambda + q = 0$ ，且 $2\lambda + p = 0$ ，要使(8-3)的两端恒等，那么 $R''(x)$ 必须是 $m$ 次多项式.此时可令

$$
R (x) = x ^ {2} R _ {m} (x),
$$

并用同样的方法来确定 $R_{m}(x)$ 中的系数.

综上所述,我们有如下结论:

如果 $f(x) = \mathrm{e}^{\lambda x}P_{m}(x)$ ，那么二阶常系数非齐次线性微分方程(8-1)具有形如

$$
y ^ {*} = x ^ {k} R _ {m} (x) \mathrm{e} ^ {\lambda x} \tag {8-4}
$$

的特解,其中 $R_{m}(x)$ 是与 $P_{m}(x)$ 同次(m次)的多项式,而k按 $\lambda$ 不是特征方程的根、是特征方程的单根或是特征方程的重根依次取为0,1或2.

上述结论可推广到 $n$ 阶常系数非齐次线性微分方程, 但要注意(8-4)式中的 $k$ 是特征方程含根 $\lambda$ 的重复次数 (即若 $\lambda$ 不是特征方程的根, 则 $k$ 取为0; 若 $\lambda$ 是特征方程的 $s$ 重根, 则 $k$ 取为 $s$ ).

例 1 求微分方程 $y''-2y'-3y=3x+1$ 的一个特解.

解 这是二阶常系数非齐次线性微分方程,且函数 $f(x)$ 是 $\mathrm{e}^{\lambda x}P_{m}(x)$ 型(其中 $\lambda=0, P_{m}(x)=3x+1$ ).

与所给方程对应的齐次方程为

$$
y ^ {\prime \prime} - 2 y ^ {\prime} - 3 y = 0,
$$

它的特征方程为

$$
r ^ {2} - 2 r - 3 = 0.
$$

由于这里 $\lambda=0$ 不是特征方程的根, 所以应设特解为

$$
y ^ {*} = b _ {0} x + b _ {1}.
$$

把它代入所给方程,得

$$
- 3 b _ {0} x - 2 b _ {0} - 3 b _ {1} = 3 x + 1,
$$

比较等式两端 x 同次幂的系数, 得

$$
\left\{ \begin{array}{l} - 3 b _ {0} = 3, \\ - 2 b _ {0} - 3 b _ {1} = 1. \end{array} \right.
$$

由此求得 $b_{0} = -1, b_{1} = \frac{1}{3}$ . 于是求得一个特解为

$$
y ^ {*} = - x + \frac {1}{3}.
$$

例 2 求微分方程 $y''-5y'+6y=xe^{2x}$ 的通解.

解 所给方程也是二阶常系数非齐次线性微分方程, 且 $f(x)$ 呈 $\mathrm{e}^{\lambda x} P_{m}(x)$ 型 (其中 $\lambda = 2, P_{m}(x) = x$ ).

与所给方程对应的齐次方程为

$$
y ^ {\prime \prime} - 5 y ^ {\prime} + 6 y = 0,
$$

它的特征方程

$$
r ^ {2} - 5 r + 6 = 0
$$

有两个实根 $r_1 = 2, r_2 = 3$ . 于是与所给方程对应的齐次方程的通解为

$$
Y = C _ {1} \mathrm{e} ^ {2 x} + C _ {2} \mathrm{e} ^ {3 x}.
$$

由于 $\lambda=2$ 是特征方程的单根, 所以应设 $y^{*}$ 为

$$
y ^ {*} = x \left(b _ {0} x + b _ {1}\right) \mathrm{e} ^ {2 x}.
$$

把它代入所给方程,得

$$
- 2 b _ {0} x + 2 b _ {0} - b _ {1} = x.
$$

比较等式两端 x 同次幂的系数, 得

$$
\left\{ \begin{array}{l} - 2 b _ {0} = 1, \\ 2 b _ {0} - b _ {1} = 0. \end{array} \right.
$$

解得 $b_{0} = -\frac{1}{2}, b_{1} = -1.$ 因此求得一个特解为

$$
y ^ {*} = x \left(- \frac {1}{2} x - 1\right) \mathrm{e} ^ {2 x}.
$$

从而所求的通解为

$$
y = C _ {1} \mathrm{e} ^ {2 x} + C _ {2} \mathrm{e} ^ {3 x} - \frac {1}{2} (x ^ {2} + 2 x) \mathrm{e} ^ {2 x}.
$$

# 二、 $f(x) = \mathrm{e}^{\lambda x}[P_l(x)\cos \omega x + Q_n(x)\sin \omega x]$ 型

应用欧拉公式

$$
\cos \theta = \frac {1}{2} \left(\mathrm{e} ^ {\mathrm{i} \theta} + \mathrm{e} ^ {- \mathrm{i} \theta}\right), \quad \sin \theta = \frac {1}{2 \mathrm{i}} \left(\mathrm{e} ^ {\mathrm{i} \theta} - \mathrm{e} ^ {- \mathrm{i} \theta}\right),
$$

把 $f(x)$ 表示成复变指数函数的形式,有

$$
\begin{array}{l} f (x) = \mathrm{e} ^ {\lambda x} \left(P _ {l} \cos \omega x + Q _ {n} \sin \omega x\right) = \mathrm{e} ^ {\lambda x} \left(P _ {l} \frac {\mathrm{e} ^ {\omega x \mathrm{i}} + \mathrm{e} ^ {- \omega x \mathrm{i}}}{2} + Q _ {n} \frac {\mathrm{e} ^ {\omega x \mathrm{i}} - \mathrm{e} ^ {- \omega x \mathrm{i}}}{2 \mathrm{i}}\right) \\ = \left(\frac {P _ {l}}{2} + \frac {Q _ {n}}{2 \mathrm{i}}\right) \mathrm{e} ^ {(\lambda + \omega \mathrm{i}) x} + \left(\frac {P _ {l}}{2} - \frac {Q _ {n}}{2 \mathrm{i}}\right) \mathrm{e} ^ {(\lambda - \omega \mathrm{i}) x} = P (x) \mathrm{e} ^ {(\lambda + \omega \mathrm{i}) x} + \overline {{P}} (x) \mathrm{e} ^ {(\lambda - \omega \mathrm{i}) x}, \\ \end{array}
$$

其中

$$
P (x) = \frac {P _ {l}}{2} + \frac {Q _ {n}}{2 \mathrm{i}} = \frac {P _ {l}}{2} - \frac {Q _ {n}}{2} \mathrm{i}, \quad \overline {{{P}}} (x) = \frac {P _ {l}}{2} - \frac {Q _ {n}}{2 \mathrm{i}} = \frac {P _ {l}}{2} + \frac {Q _ {n}}{2} \mathrm{i}
$$

是互成共轭的 $m$ 次多项式（即它们对应项的系数是共轭复数），而 $m = \max \{l, n\}$ .

应用上一目的结果,对于 $f(x)$ 中的第一项 $P(x)\mathrm{e}^{(\lambda+\omega\mathrm{i})x}$ , 可求出一个 m 次多项式 $R_{m}(x)$ , 使得 $y_{1}^{*}=x^{k}R_{m}\mathrm{e}^{(\lambda+\omega\mathrm{i})x}$ 为方程

$$
y ^ {\prime \prime} + p y ^ {\prime} + q y = P (x) \mathrm{e} ^ {(\lambda + \omega \mathrm{i}) x}
$$

的特解,其中 k 按 $\lambda + \omega i$ 不是特征方程的根或是特征方程的单根依次取 0 或 1. 由于 $f(x)$ 的第二项 $\overline{P}(x)e^{(\lambda - \omega i)x}$ 与第一项 $P(x)e^{(\lambda + \omega i)x}$ 成共轭,所以与 $y_{1}^{*}$ 成共轭的函数 $y_{2}^{*} = x^{k}\overline{R}_{m}e^{(\lambda - \omega i)x}$ 必然是方程

$$
y ^ {\prime \prime} + p y ^ {\prime} + q y = \overline {{{P}}} (x) e ^ {(\lambda - \omega i) x}
$$

的特解,这里 $\overline{R}_{m}$ 表示与 $R_{m}$ 成共轭的 m 次多项式.于是,根据第六节定理 4,方程(8-1)具有形如

$$
y ^ {*} = x ^ {k} R _ {m} \mathrm{e} ^ {(\lambda + \omega \mathrm{i}) x} + x ^ {k} \overline {{{R}}} _ {m} \mathrm{e} ^ {(\lambda - \omega \mathrm{i}) x}
$$

的特解.上式可写为

$$
\begin{array}{l} y ^ {*} = x ^ {k} \mathrm{e} ^ {\lambda x} \left(R _ {m} \mathrm{e} ^ {\omega x \mathrm{i}} + \overline {{{R}}} _ {m} \mathrm{e} ^ {- \omega x \mathrm{i}}\right) \\ = x ^ {k} \mathrm{e} ^ {\lambda x} \left[ R _ {m} (\cos \omega x + \mathrm{i} \sin \omega x) + \overline {{{R}}} _ {m} (\cos \omega x - \mathrm{i} \sin \omega x) \right], \\ \end{array}
$$

由于括号内的两项是互成共轭的,相加后即无虚部,所以可以写成实函数的形式

$$
y ^ {*} = x ^ {k} \mathrm{e} ^ {\lambda x} \left[ R _ {m} ^ {(1)} (x) \cos \omega x + R _ {m} ^ {(2)} (x) \sin \omega x \right].
$$

综上所述,我们有如下结论:

如果 $f(x) = \mathrm{e}^{\lambda x}\left[P_l(x)\cos \omega x + Q_n(x)\sin \omega x\right]$ ，那么二阶常系数非齐次线性微分方程(8-1)的特解可设为

$$
y ^ {*} = x ^ {k} \mathrm{e} ^ {\lambda x} \left[ R _ {m} ^ {(1)} (x) \cos \omega x + R _ {m} ^ {(2)} (x) \sin \omega x \right], \tag {8-5}
$$

其中 $R_{m}^{(1)}(x), R_{m}^{(2)}(x)$ 是 $m$ 次多项式, $m = \max \{l, n\}$ , 而 $k$ 按 $\lambda + \omega \mathrm{i}$ (或 $\lambda - \omega \mathrm{i}$ ) 不是特征方程的根或是特征方程的单根依次取 0 或 1.

上述结论可推广到 n 阶常系数非齐次线性微分方程,但要注意(8-5)式中的 k 是特征方程中含根 $\lambda + \omega i$ (或 $\lambda - \omega i$ ) 的重复次数.

例 3 求微分方程 $y'' + y = x \cos 2x$ 的一个特解.

解 所给方程是二阶常系数非齐次线性方程, 且 $f(x)$ 属于 $\mathrm{e}^{\lambda x}\left[P_l(x)\cos \omega x + Q_n(x)\sin \omega x\right]$ 型 (其中 $\lambda = 0, \omega = 2, P_l(x) = x, Q_n(x) = 0$ ).

与所给方程对应的齐次方程为

$$
y ^ {\prime \prime} + y = 0,
$$

它的特征方程为

$$
r ^ {2} + 1 = 0.
$$

由于这里 $\lambda + \omega i = 2i$ 不是特征方程的根, 所以应设特解为

$$
y ^ {*} = (a x + b) \cos 2 x + (c x + d) \sin 2 x.
$$

把它代入所给方程,得

$$
(- 3 a x - 3 b + 4 c) \cos 2 x - (3 c x + 3 d + 4 a) \sin 2 x = x \cos 2 x.
$$

比较等式两端同类项的系数,得

$$
\left\{ \begin{array}{l} - 3 a = 1, \\ - 3 b + 4 c = 0, \\ - 3 c = 0, \\ - 3 d - 4 a = 0, \end{array} \right.
$$

由此解得

$$
a = - \frac {1}{3}, \quad b = 0, \quad c = 0, \quad d = \frac {4}{9}.
$$

于是求得一个特解为

$$
y ^ {*} = - \frac {1}{3} x \cos 2 x + \frac {4}{9} \sin 2 x.
$$

例 4 求微分方程 $y''-y=e^{x}\cos2x$ 的一个特解.

解 这是二阶常系数非齐次线性方程, 且 $f(x)$ 属 $\mathrm{e}^{\lambda x}\left[P_l(x)\cos \omega x + Q_n(x)\sin \omega x\right]$ 型 (这里 $\lambda = 1, \omega = 2, P_l(x) = 1, Q_n(x) = 0$ ).

特征方程为 $r^{2}-1=0$ ，由于 $\lambda+\omega i=1+2i$ 不是特征方程的根，所以应设特解为

$$
y ^ {*} = \mathrm{e} ^ {x} (a \cos 2 x + b \sin 2 x).
$$

求导得

$$
y ^ {* \prime} = e ^ {x} [ (a + 2 b) \cos 2 x + (- 2 a + b) \sin 2 x ],
$$

$$
y ^ {* \prime \prime} = e ^ {x} [ (- 3 a + 4 b) \cos 2 x + (- 4 a - 3 b) \sin 2 x ].
$$

代入所给方程,得

$$
4 \mathrm{e} ^ {x} [ (- a + b) \cos 2 x - (a + b) \sin 2 x ] = \mathrm{e} ^ {x} \cos 2 x,
$$

比较等式两端同类项的系数,有

$$
\left\{ \begin{array}{l} - a + b = \frac {1}{4}, \\ a + b = 0, \end{array} \right.
$$

解得 $a = -\frac{1}{8}, b = \frac{1}{8}.$ 

因此所给方程的一个特解为

$$
y ^ {*} = \frac {1}{8} \mathrm{e} ^ {x} (\sin 2 x - \cos 2 x).
$$

例 5 在第六节例 1 中, 设物体受弹性恢复力 f 和铅直干扰力 F 的作用. 试求物体的运动规律.

解 这里需要求出无阻尼强迫振动方程

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} + k ^ {2} x = h \sin p t \tag {8-6}
$$

的通解.

对应的齐次微分方程(即无阻尼自由振动方程)为

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} + k ^ {2} x = 0, \tag {8-7}
$$

它的特征方程 $r^2 + k^2 = 0$ 的根为 $r = \pm k\mathrm{i}$ . 故方程(8-7)的通解为

$$
X = C _ {1} \cos k t + C _ {2} \sin k t.
$$

令 $C_1 = A\sin \varphi, C_2 = A\cos \varphi$ ，则方程(8-7)的通解又可写成

$$
X = A \sin (k t + \varphi),
$$

其中， $A,\varphi$ 为任意常数

方程(8-6)右端的函数

$$
f (t) = h \sin p t
$$

与 $f(t) = \mathrm{e}^{\lambda t}\left[P_l(t)\cos \omega t + Q_n(t)\sin \omega t\right]$ 相比较，有 $\lambda = 0, \omega = p, P_l(t) = 0, Q_n(t) = h.$ 现在分别就 $p \neq k$ 和 $p = k$ 两种情形讨论如下：

(i) 如果 $p \neq k$ , 则 $\lambda \pm \omega \mathrm{i} = \pm p \mathrm{i}$ 不是特征方程的根, 故设

$$
x ^ {*} = a _ {1} \cos p t + b _ {1} \sin p t.
$$

代入方程(8-6)求得

$$
a _ {1} = 0, \quad b _ {1} = \frac {h}{k ^ {2} - p ^ {2}},
$$

于是

$$
x ^ {*} = \frac {h}{k ^ {2} - p ^ {2}} \sin p t.
$$

从而当 $p \neq k$ 时, 方程(8-6)的通解为

$$
x = X + x ^ {*} = A \sin (k t + \varphi) + \frac {h}{k ^ {2} - p ^ {2}} \sin p t.
$$

上式表示,物体的运动由两部分组成,这两部分都是简谐振动.上式第一项表示自由振动,第二项所表示的振动叫做强迫振动.强迫振动是干扰力引起的,它的角频率即是干扰力的角频率p;当干扰力的角频率p与振动系统的固有频率k相差很小时,它的振幅 $\left|\frac{h}{k^{2}-p^{2}}\right|$ 可以很大.

（ii）如果 $p = k$ 那么 $\lambda \pm \omega \mathrm{i} = \pm p\mathrm{i}$ 是特征方程的根.故设

$$
x ^ {*} = t \left(a _ {1} \cos k t + b _ {1} \sin k t\right).
$$

代入方程(8-6)求得

$$
a _ {1} = - \frac {h}{2 k}, \quad b _ {1} = 0.
$$

于是

$$
x ^ {*} = - \frac {h}{2 k} t \cos k t.
$$

从而当 p=k 时, 方程(8-6)的通解为

$$
x = X + x ^ {*} = A \sin (k t + \varphi) - \frac {h}{2 k} t \cos k t.
$$

上式右端第二项表明,强迫振动的振幅 $\frac{h}{2k}t$ 随时间 $t$ 的增大而无限增大.这就发生所谓共振现象.为了避免共振现象,应使干扰力的角频率 $p$ 不要靠近振动系统的固有频率 $k$ .反之,如果要利用共振现象,那么应使 $p=k$ 或使 $p$ 与 $k$ 尽量靠近.

有阻尼的强迫振动问题可作类似的讨论,这里从略了.

# 习题7-8

1. 求下列各微分方程的通解：

(1) $2y'' + y' - y = 2e^x$ ; 

(2) $y'' + a^2 y = e^x$ ; 

(3) $2y'' + 5y' = 5x^2 - 2x - 1$ ; 

(4) $y'' + 3y' + 2y = 3xe^{-x}$ ; 

(5) $y''-2y'+5y=e^{x}\sin 2x;$ 

(6) $y''-6y'+9y=(x+1)e^{3x}$ ; 

(7) $y'' + 5y' + 4y = 3 - 2x$ ; 

(8) $y''+4y=x\cos x;$ 

(9) $y'' + y = e^x + \cos x;$ 

(10) $y''-y=\sin^{2}x.$ 

2. 求下列各微分方程满足已给初值条件的特解：

(1) $y'' + y + \sin 2x = 0, y \mid_{x=\pi} = 1, y' \mid_{x=\pi} = 1;$ 

(2) $y''-3y'+2y=5,y\big|_{x=0}=1,y'\big|_{x=0}=2;$ 

(3) $y''-10y'+9y=e^{2x},y\mid_{x=0}=\frac{6}{7},y'\mid_{x=0}=\frac{33}{7};$ 

(4) $y''-y=4xe^{x},y\mid_{x=0}=0,y'\mid_{x=0}=1;$ 

(5) $y''-4y'=5,y\big|_{x=0}=1,y'\big|_{x=0}=0.$ 

3. 已知二阶常系数齐次线性微分方程 $y'' + my' + ny = 0$ 的通解为 $y = (C_1 + C_2x)e^x$ ，求 $m, n$ 的值，并求非齐次方程 $y'' + my' + ny = x$ 满足初值条件 $y(0) = 2, y'(0) = 0$ 的特解.

4. 大炮以仰角 $\alpha$ 、初速度 $v_{0}$ 发射炮弹，若不计空气阻力，求弹道曲线.

5. 在 RLC 含源串联电路中, 电动势为 E 的电源对电容器 C 充电. 已知 $E = 20 \, V, C = 0.2 \, \mu F, L = 0.1 \, H, R = 1000 \, \Omega$ , 试求合上开关 S 后的电流 $i(t)$ 及电压 $u_{c}(t)$ .

6. 设函数 $\varphi(x)$ 连续, 且满足

$$
\varphi (x) = \mathrm{e} ^ {x} + \int_ {0} ^ {x} t \varphi (t) \mathrm{d} t - x \int_ {0} ^ {x} \varphi (t) \mathrm{d} t,
$$

求 $\varphi(x)$ .

# * 第九节 欧拉方程

变系数的线性微分方程,一般说来都是不容易求解的.但是有些特殊的变系数线性微分方程,则可以通过变量代换化为常系数线性微分方程,因而容易求解,欧拉方程就是其中的一种.

形如

$$
x ^ {n} y ^ {(n)} + p _ {1} x ^ {n - 1} y ^ {(n - 1)} + \dots + p _ {n - 1} x y ^ {\prime} + p _ {n} y = f (x) \tag {9-1}
$$

的方程(其中 $p_{1},p_{2},\cdots,p_{n}$ 为常数),叫做欧拉方程.

作变换 $x = \mathrm{e}^t$ 或 $t = \ln x$ ，将自变量 $x$ 换成 $t^{①}$ ，我们有

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {\mathrm{d} y}{\mathrm{d} t} \cdot \frac {\mathrm{d} t}{\mathrm{d} x} = \frac {1}{x} \frac {\mathrm{d} y}{\mathrm{d} t},
$$

$$
\frac {\mathrm{d} ^ {2} y}{\mathrm{d} x ^ {2}} = \frac {1}{x ^ {2}} \left(\frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} - \frac {\mathrm{d} y}{\mathrm{d} t}\right),
$$

$$
\frac {\mathrm{d} ^ {3} y}{\mathrm{d} x ^ {3}} = \frac {1}{x ^ {3}} \left(\frac {\mathrm{d} ^ {3} y}{\mathrm{d} t ^ {3}} - 3 \frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} + 2 \frac {\mathrm{d} y}{\mathrm{d} t}\right).
$$

如果采用记号 D 表示对 t 求导的运算 $\frac{d}{dt}$ ，那么上述计算结果可以写成

$$
x y ^ {\prime} = \mathrm{D} y,
$$

$$
x ^ {2} y ^ {\prime \prime} = \frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} - \frac {\mathrm{d} y}{\mathrm{d} t} = \left(\frac {\mathrm{d} ^ {2}}{\mathrm{d} t ^ {2}} - \frac {\mathrm{d}}{\mathrm{d} t}\right) y = (\mathrm{D} ^ {2} - \mathrm{D}) y = \mathrm{D} (\mathrm{D} - 1) y,
$$

$$
x ^ {3} y ^ {\prime \prime \prime} = \frac {\mathrm{d} ^ {3} y}{\mathrm{d} t ^ {3}} - 3 \frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} + 2 \frac {\mathrm{d} y}{\mathrm{d} t} = (\mathrm{D} ^ {3} - 3 \mathrm{D} ^ {2} + 2 \mathrm{D}) y = \mathrm{D} (\mathrm{D} - 1) (\mathrm{D} - 2) y,
$$

一般地，有

$$
x ^ {k} y ^ {(k)} = \mathrm{D} (\mathrm{D} - 1) \dots (\mathrm{D} - k + 1) y.
$$

把它代入欧拉方程(9-1)，便得一个以 $t$ 为自变量的常系数线性微分方程.在求出这个方程的解后，把 $t$ 换成 $\ln x$ ，即得原方程的解

例 求欧拉方程 $x^{3}y''' + x^{2}y'' - 4xy' = 3x^{2}$ 的通解.

解 作变换 $x = \mathrm{e}^{t}$ 或 $t = \ln x$ ，原方程化为

$$
\mathrm{D} (\mathrm{D} - 1) (\mathrm{D} - 2) y + \mathrm{D} (\mathrm{D} - 1) y - 4 \mathrm{D} y = 3 \mathrm{e} ^ {2 t},
$$

即

$$
\mathrm{D} ^ {3} y - 2 \mathrm{D} ^ {2} y - 3 \mathrm{D} y = 3 \mathrm{e} ^ {2 t},
$$

或

$$
\frac {\mathrm{d} ^ {3} y}{\mathrm{d} t ^ {3}} - 2 \frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} - 3 \frac {\mathrm{d} y}{\mathrm{d} t} = 3 \mathrm{e} ^ {2 t}. \tag {9-2}
$$

方程(9-2)所对应的齐次方程为

$$
\frac {\mathrm{d} ^ {3} y}{\mathrm{d} t ^ {3}} - 2 \frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} - 3 \frac {\mathrm{d} y}{\mathrm{d} t} = 0, \tag {9-3}
$$

其特征方程为

$$
r ^ {3} - 2 r ^ {2} - 3 r = 0,
$$

它有三个根: $r_1 = 0, r_2 = -1, r_3 = 3$ . 于是方程(9-3)的通解为

$$
Y = C _ {1} + C _ {2} \mathrm{e} ^ {- t} + C _ {3} \mathrm{e} ^ {3 t} = C _ {1} + \frac {C _ {2}}{x} + C _ {3} x ^ {3}.
$$

根据上节第一目,特解的形式为

$$
y ^ {*} = b \mathrm{e} ^ {2 t} = b x ^ {2},
$$

代入原方程,求得 $b=-\frac{1}{2}$ , 即

$$
y ^ {*} = - \frac {x ^ {2}}{2}.
$$

于是,所给欧拉方程的通解为①

$$
y = C _ {1} + \frac {C _ {2}}{x} + C _ {3} x ^ {3} - \frac {1}{2} x ^ {2}.
$$

# *习题7-9

求下列欧拉方程的通解：

1. $x^{2}y'' + xy' - y = 0.$ 

2. $y'' - \frac{y'}{x} + \frac{y}{x^2} = \frac{2}{x}$ . 

3. $x^{3}y''' + 3x^{2}y'' - 2xy' + 2y = 0.$ 

4. $x^{2}y''-2xy'+2y=\ln^{2}x-2\ln x.$ 

5. $x^{2}y^{\prime \prime} + xy^{\prime} - 4y = x^{3}$ 

6. $x^{2}y^{\prime \prime} - xy^{\prime} + 4y = x\sin (\ln x)$ . 

7. $x^{2}y''-3xy'+4y=x+x^{2}\ln x.$ 

8. $x^{3}y^{\prime \prime \prime} + 2xy^{\prime} - 2y = x^{2}\ln x + 3x.$ 

# * 第十节 常系数线性微分方程组解法举例

前面讨论的是由一个微分方程求解一个未知函数的情形,但在研究某些实际问题时,还会遇到由几个微分方程联立起来共同确定几个具有同一自变量的函数的情形.这些联立的微分方程称为微分方程组.

如果微分方程组中的每一个微分方程都是常系数线性微分方程,那么,这种微分方程组就叫做常系数线性微分方程组.

对于常系数线性微分方程组,我们可以用下述方法求它的解:

第一步 从方程组中消去一些未知函数及其各阶导数,得到只含有一个未知函数的高阶常系数线性微分方程.

第二步 解此高阶微分方程,求出满足该方程的未知函数.

第三步 把已求得的函数代入原方程组,一般说来,不必经过积分就可求出其余的未知函数.

例 1 解微分方程组

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} y}{\mathrm{d} x} = 3 y - 2 z, \\ \frac {\mathrm{d} z}{\mathrm{d} x} = 2 y - z. \end{array} \right. \tag {10-1}
$$

解 这是含有两个未知函数 $y(x), z(x)$ 的由两个一阶常系数线性方程组成的方程组.

设法消去未知函数 y. 由(10-2)式得

$$
y = \frac {1}{2} \left(\frac {\mathrm{d} z}{\mathrm{d} x} + z\right). \tag {10-3}
$$

对上式两端求导,有

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {1}{2} \left(\frac {\mathrm{d} ^ {2} z}{\mathrm{d} x ^ {2}} + \frac {\mathrm{d} z}{\mathrm{d} x}\right). \tag {10-4}
$$

把(10-3)、(10-4)两式代入(10-1)式并化简,得

$$
\frac {\mathrm{d} ^ {2} z}{\mathrm{d} x ^ {2}} - 2 \frac {\mathrm{d} z}{\mathrm{d} x} + z = 0.
$$

这是一个二阶常系数线性微分方程,它的通解是

$$
z = \left(C _ {1} + C _ {2} x\right) \mathrm{e} ^ {x}. \tag {10-5}
$$

再把(10-5)式代入(10-3)式,得

$$
y = \frac {1}{2} \left(2 C _ {1} + C _ {2} + 2 C _ {2} x\right) \mathrm{e} ^ {x}. \tag {10-6}
$$

将(10-5)、(10-6)联立起来,就得到所给方程组的通解.

如果我们要得到方程组满足初值条件

$$
y \mid_ {x = 0} = 1, \quad z \mid_ {x = 0} = 0
$$

的特解,只需将此条件代入(10-6)和(10-5)式,得

$$
\left\{ \begin{array}{l} 1 = \frac {1}{2} (2 C _ {1} + C _ {2}), \\ 0 = C _ {1}. \end{array} \right.
$$

由此求得

$$
C _ {1} = 0, \quad C _ {2} = 2.
$$

于是所给微分方程组满足上述初值条件的特解为

$$
\left\{ \begin{array}{l} y = (1 + 2 x) \mathrm{e} ^ {x}, \\ z = 2 x \mathrm{e} ^ {x}. \end{array} \right.
$$

在讨论常系数线性微分方程(或方程组)时,常采用第七节中引入的记号 D 表示对自变量 x 求导的运算 $\frac{d}{dx}$ .

例2 解微分方程组

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} + \frac {\mathrm{d} y}{\mathrm{d} t} - x = \mathrm{e} ^ {t}, \\ \frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} + \frac {\mathrm{d} x}{\mathrm{d} t} + y = 0. \end{array} \right.
$$

解 用记号 D 表示 $\frac{\mathrm{d}}{\mathrm{d}t}$ , 则方程组可记作

$$
\left\{ \begin{array}{l} (\mathrm{D} ^ {2} - 1) x + \mathrm{D} y = \mathrm{e} ^ {t}, \\ \mathrm{D} x + (\mathrm{D} ^ {2} + 1) y = 0. \end{array} \right. \tag {10-7}
$$

我们可以类似于解代数方程组那样消去一个未知数,例如为消去 x, 可作如下运算:

$$
(1 0 - 7) - \mathrm{D} (1 0 - 8): - x - \mathrm{D} ^ {3} y = \mathrm{e} ^ {t}, \tag {10-9}
$$

$$
(1 0 - 8) + D (1 0 - 9): (- D ^ {4} + D ^ {2} + 1) y = D e ^ {t},
$$

即

$$
\left(- \mathrm{D} ^ {4} + \mathrm{D} ^ {2} + 1\right) y = \mathrm{e} ^ {t}. \tag {10-10}
$$

(10-10)式为四阶非齐次线性方程,其特征方程为

$$
- r ^ {4} + r ^ {2} + 1 = 0,
$$

解得特征根为

$$
r _ {1, 2} = \pm \alpha = \pm \sqrt {\frac {1 + \sqrt {5}}{2}}, r _ {3, 4} = \pm \beta \mathrm{i} = \pm \mathrm{i} \sqrt {\frac {\sqrt {5} - 1}{2}},
$$

容易求得一个特解 $y^{*} = \mathrm{e}^{t}$ ，于是得(10-10)的通解为

$$
y = C _ {1} \mathrm{e} ^ {- \alpha t} + C _ {2} \mathrm{e} ^ {\alpha t} + C _ {3} \cos \beta t + C _ {4} \sin \beta t + \mathrm{e} ^ {t}. \tag {10-11}
$$

再求 $x$ . 由(10-9)式, 即有

$$
x = - \mathrm{D} ^ {3} y - \mathrm{e} ^ {t},
$$

以(10-11)式代入上式,即得

$$
x = \alpha^ {3} C _ {1} \mathrm{e} ^ {- \alpha t} - \alpha^ {3} C _ {2} \mathrm{e} ^ {\alpha t} - \beta^ {3} C _ {3} \sin \beta t + \beta^ {3} C _ {4} \cos \beta t - 2 \mathrm{e} ^ {t}. \tag {10-12}
$$

将(10-11)和(10-12)两个函数联立,就是所求方程组的通解.

这里要注意,在求得一个未知函数以后,再求另一个未知函数时,一般不再积分(积分就会出现新的任意常数,从(10-11)、(10-12)两式可知两式中的任意常数之间有着确定的关系).

我们也可用行列式解上述方程组.由(10-7)和(10-8),有

$$
\left| \begin{array}{c c} \mathrm{D} ^ {2} - 1 & \mathrm{D} \\ \mathrm{D} & \mathrm{D} ^ {2} + 1 \end{array} \right| y = \left| \begin{array}{c c} \mathrm{D} ^ {2} - 1 & \mathrm{e} ^ {t} \\ \mathrm{D} & 0 \end{array} \right|,
$$

即

$$
\left(\mathrm{D} ^ {4} - \mathrm{D} ^ {2} - 1\right) y = - \mathrm{e} ^ {t}.
$$

这与(10-10)式是一样的.但再求x时,不宜再次应用行列式.如再应用行列式,得

$$
\left| \begin{array}{c c} \mathrm{D} ^ {2} - 1 & \mathrm{D} \\ \mathrm{D} & \mathrm{D} ^ {2} + 1 \end{array} \right| x = \left| \begin{array}{c c} \mathrm{e} ^ {t} & \mathrm{D} \\ 0 & \mathrm{D} ^ {2} + 1 \end{array} \right|,
$$

即

$$
\left(\mathrm{D} ^ {4} - \mathrm{D} ^ {2} - 1\right) x = 2 \mathrm{e} ^ {t},
$$

解得

$$
x = A _ {1} \mathrm{e} ^ {- \alpha t} + A _ {2} \mathrm{e} ^ {\alpha t} + A _ {3} \cos \beta t + A _ {4} \sin \beta t - 2 \mathrm{e} ^ {t},
$$

则必须说明 $A_{1}, A_{2}, A_{3}, A_{4}$ 与 $C_{1}, C_{2}, C_{3}, C_{4}$ 之间的关系.

注意这里的“系数行列式”

$$
\left| \begin{array}{c c} \mathrm{D} ^ {2} - 1 & \mathrm{D} \\ \mathrm{D} & \mathrm{D} ^ {2} + 1 \end{array} \right| = \mathrm{D} ^ {4} - \mathrm{D} ^ {2} - 1
$$

是 D 的四次多项式, 这就标志着微分方程组是四阶的, 它的通解中一定恰含四个任意常数.

# *习题7-10

1. 求下列微分方程组的通解：

(1) $\left\{ \begin{array}{l} \frac{\mathrm{d}y}{\mathrm{d}x} = z, \\ \frac{\mathrm{d}z}{\mathrm{d}x} = y; \end{array} \right.$ 

(2) $\left\{ \begin{array}{l} \frac{\mathrm{d}^2x}{\mathrm{d}t^2} = y, \\ \frac{\mathrm{d}^2y}{\mathrm{d}t^2} = x; \end{array} \right.$ 

(3) $\left\{ \begin{array}{l} \frac{\mathrm{d}x}{\mathrm{d}t} + \frac{\mathrm{d}y}{\mathrm{d}t} = -x + y + 3, \\ \frac{\mathrm{d}x}{\mathrm{d}t} - \frac{\mathrm{d}y}{\mathrm{d}t} = x + y - 3; \end{array} \right.$ 

(4) $\left\{ \begin{array}{l} \frac{\mathrm{d}x}{\mathrm{d}t} + 5x + y = \mathrm{e}^t, \\ \frac{\mathrm{d}y}{\mathrm{d}t} - x - 3y = \mathrm{e}^{2t}; \end{array} \right.$ 

(5) $\left\{\begin{aligned}\frac{\mathrm{d}x}{\mathrm{d}t}+2x+\frac{\mathrm{d}y}{\mathrm{d}t}+y=t,\\5x+\frac{\mathrm{d}y}{\mathrm{d}t}+3y=t^{2};\end{aligned}\right.$ 

(6) $\left\{ \begin{array}{l} \frac{\mathrm{d}x}{\mathrm{d}t} - 3x + 2\frac{\mathrm{d}y}{\mathrm{d}t} + 4y = 2\sin t, \\ 2\frac{\mathrm{d}x}{\mathrm{d}t} + 2x + \frac{\mathrm{d}y}{\mathrm{d}t} - y = \cos t. \end{array} \right.$ 

2. 求下列微分方程组满足所给初值条件的特解：

(1) $\left\{\begin{aligned}\frac{\mathrm{d}x}{\mathrm{d}t}&=y,x\mid_{t=0}=0,\\ \frac{\mathrm{d}y}{\mathrm{d}t}&=-x,y\mid_{t=0}=1;\end{aligned}\right.$ 

(2) $\left\{ \begin{array}{l} \frac{\mathrm{d}^2x}{\mathrm{d}t^2} + 2\frac{\mathrm{d}y}{\mathrm{d}t} - x = 0, x \mid_{t=0} = 1, \\ \frac{\mathrm{d}x}{\mathrm{d}t} + y = 0, y \mid_{t=0} = 0; \end{array} \right.$ 

(3) $\left\{ \begin{array}{l} \frac{\mathrm{d}x}{\mathrm{d}t} + 3x - y = 0, x \mid_{t=0} = 1, \\ \frac{\mathrm{d}y}{\mathrm{d}t} - 8x + y = 0, y \mid_{t=0} = 4; \end{array} \right.$ 

(4) $\left\{\begin{aligned}&2\frac{\mathrm{d}x}{\mathrm{d}t}-4x+\frac{\mathrm{d}y}{\mathrm{d}t}-y=\mathrm{e}^{t},x\mid_{t=0}=\frac{3}{2},\\&\frac{\mathrm{d}x}{\mathrm{d}t}+3x+y=0,y\mid_{t=0}=0;\end{aligned}\right.$ 

(5) $\left\{\frac{\mathrm{d}x}{\mathrm{d}t}+2x-\frac{\mathrm{d}y}{\mathrm{d}t}=10\cos t,x\right|_{t=0}=2,$ $\frac{\mathrm{d}x}{\mathrm{d}t}+\frac{\mathrm{d}y}{\mathrm{d}t}+2y=4\mathrm{e}^{-2t},y\bigg|_{t=0}=0;$ 

(6) $\left\{ \begin{array}{l} \frac{\mathrm{d}x}{\mathrm{d}t} - x + \frac{\mathrm{d}y}{\mathrm{d}t} + 3y = \mathrm{e}^{-t} - 1, x \mid_{t=0} = \frac{48}{49}, \\ \frac{\mathrm{d}x}{\mathrm{d}t} + 2x + \frac{\mathrm{d}y}{\mathrm{d}t} + y = \mathrm{e}^{2t} + t, y \mid_{t=0} = \frac{95}{98}. \end{array} \right.$ 

# 总习题七

1. 填空：

(1) $xy''' + 2x^2y'^2 + x^3y = x^4 + 1$ 是 ____ 阶微分方程；

(2) 一阶线性微分方程 $y' + P(x)y = Q(x)$ 的通解为 ____；

(3) 与积分方程 $y=\int_{x_{0}}^{x}f(x,y)\mathrm{d}x$ 等价的微分方程初值问题是 ____；

(4) 已知 $y = 1,y = x,y = {x}^{2}$ 是某二阶非齐次线性微分方程的三个解,则该方程的通解为 ____.

2. 以下两题中给出了四个结论,从中选出一个正确的结论:

（1）设非齐次线性微分方程 $y' + P(x)y = Q(x)$ 有两个不同的解 $y_{1}(x)$ 与 $y_{2}(x), C$ 为任意常数，则该方程的通解是（）；

(A) $C[y_{1}(x)-y_{2}(x)]$ 

(B) $y_{1}(x)+C[y_{1}(x)-y_{2}(x)]$ 

(C) $C[y_{1}(x)+y_{2}(x)]$ 

(D) $y_{1}(x)+C[y_{1}(x)+y_{2}(x)]$ 

(2) 具有特解 $y_{1}=e^{-x}, y_{2}=2xe^{-x}, y_{3}=3e^{x}$ 的三阶常系数齐次线性微分方程是().

(A) $y'''-y''-y'+y=0$ 

(B) $y''' + y'' - y' - y = 0$ 

(C) $y'''-6y''+11y'-6y=0$ 

(D) $y'''-2y''-y'+2y=0$ 

3. 求以下列各式所表示的函数为通解的微分方程：

(1) $(x+C)^{2}+y^{2}=1$ （其中C为任意常数）；

(2) $y=C_{1}e^{x}+C_{2}e^{2x}$ （其中 $C_{1},C_{2}$ 为任意常数）.

4. 求下列微分方程的通解：

(1) $xy' + y = 2\sqrt{xy}$ ; 

(2) $xy' \ln x + y = ax (\ln x + 1)$ ; 

(3) $\frac{dy}{dx}=\frac{y}{2(\ln y-x)}$ ; 

* (4) $\frac{\mathrm{dy}}{\mathrm{dx}} + xy - x^3 y^3 = 0$ ; 

(5) $y'' + y'^{2} + 1 = 0;$ 

(6) $yy'' - y'^2 - 1 = 0$ ; 

(7) $y'' + 2y' + 5y = \sin 2x;$ 

(8) $y''' + y'' - 2y' = x(e^x + 4)$ ; 

* (9) $(y^{4} - 3x^{2})\mathrm{d}y + xy\mathrm{d}x = 0;$ 

(10) $y' + x = \sqrt{x^2 + y}$ . 

5. 求下列微分方程满足所给初值条件的特解：

* (1) $y^3 \mathrm{d}x + 2(x^2 - xy^2) \mathrm{d}y = 0, x = 1$ 时 $y = 1$ ;

(2) $y''-ay'^{2}=0,x=0$ 时 $y=0,y'=-1;$ 

(3) $2y''-\sin 2y=0,x=0$ 时 $y=\frac{\pi}{2},y'=1;$ 

(4) $y''+2y'+y=\cos x,x=0$ 时 $y=0,y'=\frac{3}{2}$ .

6. 已知某曲线经过点(1,1)，它的切线在纵轴上的截距等于切点的横坐标，求它的方程.

7. 已知某车间的容积为 $5400 \, m^{3}$ ，其中的空气含 0.12% 的 $CO_{2}$ （以容积计算）。现以含 $CO_{2}$ 0.04% 的新鲜空气输入，问每分应输入多少，才能在 30 min 后使车间空气中 $CO_{2}$ 的含量不超过 0.06%？（假定输入的新鲜空气与原有空气很快混合均匀后，以相同的流量排出。）

8. 设可导函数 $\varphi(x)$ 满足

$$
\varphi (x) \cos x + 2 \int_ {0} ^ {x} \varphi (t) \sin t \mathrm{d} t = x + 1,
$$

求 $\varphi(x)$ .

9. 设光滑曲线 $y = \varphi(x)$ 过原点, 且当 $x > 0$ 时 $\varphi(x) > 0$ . 对应于 $[0, x]$ 一段曲线的弧长为 $e^x - 1$ , 求 $\varphi(x)$ .

10. 设 $y_{1}(x)$ , $y_{2}(x)$ 是二阶齐次线性方程 $y'' + p(x)y' + q(x)y = 0$ 的两个解, 令

$$
W (x) = \left| \begin{array}{l l} y _ {1} (x) & y _ {2} (x) \\ y _ {1} ^ {\prime} (x) & y _ {2} ^ {\prime} (x) \end{array} \right| = y _ {1} (x) y _ {2} ^ {\prime} (x) - y _ {1} ^ {\prime} (x) y _ {2} (x),
$$

证明:(1) $W(x)$ 满足方程 $W' + p(x)W = 0$ ;

(2) $W(x) = W(x_0)e^{-\int_{x_0}^x p(t)dt}.$ 

* 11. 求下列欧拉方程的通解：

(1) $x^{2}y''+3xy'+y=0;$ 

(2) $x^{2}y^{\prime \prime} - 4xy^{\prime} + 6y = x.$ 

* 12. 求下列常系数线性微分方程组的通解：

(1) $\left\{ \begin{array}{l} \frac{\mathrm{d}x}{\mathrm{d}t} + 2\frac{\mathrm{d}y}{\mathrm{d}t} + y = 0, \\ 3\frac{\mathrm{d}x}{\mathrm{d}t} + 2x + 4\frac{\mathrm{d}y}{\mathrm{d}t} + 3y = t; \end{array} \right.$ 

(2) $\left\{ \begin{array}{l} \frac{\mathrm{d}^2x}{\mathrm{d}t^2} + 2\frac{\mathrm{d}x}{\mathrm{d}t} + x + \frac{\mathrm{d}y}{\mathrm{d}t} + y = 0, \\ \frac{\mathrm{d}x}{\mathrm{d}t} + x + \frac{\mathrm{d}^2y}{\mathrm{d}t^2} + 2\frac{\mathrm{d}y}{\mathrm{d}t} + y = \mathrm{e}^t. \end{array} \right.$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/e44abc6dfaa7aa6586d455acb288933223556a62c7ecfca6b31b2a5abe580f59.jpg)


第七章释疑解难

# 附录I

# 初等数学几个内容简介

# (一) 三角函数公式

1. 两角和差公式

$$
\sin (\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta
$$

$$
\sin (\alpha - \beta) = \sin \alpha \cos \beta - \cos \alpha \sin \beta
$$

$$
\cos (\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta
$$

$$
\cos (\alpha - \beta) = \cos \alpha \cos \beta + \sin \alpha \sin \beta
$$

$$
\tan (\alpha + \beta) = \frac {\tan \alpha + \tan \beta}{1 - \tan \alpha \tan \beta}
$$

$$
\tan (\alpha - \beta) = \frac {\tan \alpha - \tan \beta}{1 + \tan \alpha \tan \beta}
$$

2. 和差化积公式

$$
\sin \alpha + \sin \beta = 2 \sin \frac {\alpha + \beta}{2} \cos \frac {\alpha - \beta}{2}
$$

$$
\sin \alpha - \sin \beta = 2 \cos \frac {\alpha + \beta}{2} \sin \frac {\alpha - \beta}{2}
$$

$$
\cos \alpha + \cos \beta = 2 \cos \frac {\alpha + \beta}{2} \cos \frac {\alpha - \beta}{2}
$$

$$
\cos \alpha - \cos \beta = - 2 \sin \frac {\alpha + \beta}{2} \sin \frac {\alpha - \beta}{2}
$$

3. 积化和差公式

$$
\sin \alpha \cos \beta = \frac {1}{2} [ \sin (\alpha + \beta) + \sin (\alpha - \beta) ]
$$

$$
\cos \alpha \sin \beta = \frac {1}{2} [ \sin (\alpha + \beta) - \sin (\alpha - \beta) ]
$$

$$
\cos \alpha \cos \beta = \frac {1}{2} [ \cos (\alpha + \beta) + \cos (\alpha - \beta) ]
$$

$$
\sin \alpha \sin \beta = - \frac {1}{2} [ \cos (\alpha + \beta) - \cos (\alpha - \beta) ]
$$

4. 倍角公式

$$
\sin 2 \alpha = 2 \sin \alpha \cos \alpha = \frac {2 \tan \alpha}{1 + \tan^ {2} \alpha}
$$

$$
\cos 2 \alpha = \cos^ {2} \alpha - \sin^ {2} \alpha = 2 \cos^ {2} \alpha - 1 = 1 - 2 \sin^ {2} \alpha = \frac {1 - \tan^ {2} \alpha}{1 + \tan^ {2} \alpha}
$$

$$
\tan 2 \alpha = \frac {2 \tan \alpha}{1 - \tan^ {2} \alpha}
$$

5. 半角公式

$$
\sin \frac {\alpha}{2} = \pm \sqrt {\frac {1 - \cos \alpha}{2}}
$$

$$
\cos \frac {\alpha}{2} = \pm \sqrt {\frac {1 + \cos \alpha}{2}}
$$

$$
\tan \frac {\alpha}{2} = \frac {\sin \alpha}{1 + \cos \alpha} = \frac {1 - \cos \alpha}{\sin \alpha} = \pm \sqrt {\frac {1 - \cos \alpha}{1 + \cos \alpha}}
$$

(正、负号由 $\frac{\alpha}{2}$ 所在的象限决定.)

# (二) 反三角函数

三角函数作为一种从它们各自的定义域到值域的映射,都不是单射. 然而,如果对其定义域作某种限制,也可以使每一个三角函数都成为单射,从而就存在反函数,这样得到的反函数就是通常所说的反三角函数,它们的定义以及性质如下:

正弦函数 $y = \sin x, x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ 的反函数称为反正弦函数，记作 $y = \arcsin x$ ，即 $x = \sin y$ ，这里 $x$ 是自变量， $y$ 是因变量.

因为 $\frac{1}{2} = \sin \frac{\pi}{6}$ , 所以 $\arcsin \frac{1}{2} = \frac{\pi}{6}$ ; 类似地, 有

$$
\frac {\sqrt {2}}{2} = \sin \frac {\pi}{4} \Rightarrow \arcsin \frac {\sqrt {2}}{2} = \frac {\pi}{4};
$$

$$
\frac {\sqrt {3}}{2} = \sin \frac {\pi}{3} \Rightarrow \arcsin \frac {\sqrt {3}}{2} = \frac {\pi}{3};
$$

$$
- 1 = \sin \left(- \frac {\pi}{2}\right) \Rightarrow \arcsin (- 1) = - \frac {\pi}{2},
$$

等等. 反正弦函数 $y = \arcsin x$ 的定义域为 $[-1, 1]$ , 值域为 $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ , 它在闭区间

[-1,1]上是有界的、单调增加的，且为奇函数，函数的图形如图1(a)所示.

余弦函数 $y = \cos x, x \in [0, \pi]$ 的反函数称为反余弦函数，记作 $y = \arccos x$ ，即 $x = \cos y$ . 反余弦函数 $y = \arccos x$ 的定义域为 $[-1, 1]$ ，值域为 $[0, \pi]$ ，它在闭区间 $[-1, 1]$ 上是有界的、单调减少的，函数的图形如图1(b)所示.

正切函数 $y = \tan x, x \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ 的反函数称为反正切函数，记作 $y = \arctan x$ ，即 $x = \tan y$ . 反正切函数 $y = \arctan x$ 的定义域为 $(-\infty, +\infty)$ ，值域为 $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ ，它在 $(-\infty, +\infty)$ 内是有界的、单调增加的，且为奇函数，函数的图形如图1(c)所示.

余切函数 $y = \cot x = \frac{\cos x}{\sin x}, x \in (0, \pi)$ 的反函数称为反余切函数，记作 $y = \operatorname{arccot} x$ ，即 $x = \cot y$ . 反余切函数 $y = \operatorname{arccot} x$ 的定义域为 $(-\infty, +\infty)$ ，值域为 $(0, \pi)$ ，它在 $(-\infty, +\infty)$ 内是有界的、单调减少的，函数的图形如图1(d)所示.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/c4a6cb8907f20eea09b4b603d0e4d2853e55fc907ed64f76fbc4635a1b941488.jpg)



图1


# (三) 极坐标

在平面上取定一点 $O$ ，从点 $O$ 引一条射线 $OA$ ，再选定一个长度单位和角的正方向

（通常取逆时针方向），这样，平面上任意一点 $M$ 的位置就可用两个数 $\rho$ 和 $\theta$ 来确定，确定的方法是（图2）： $\rho = |OM|$ ，因此 $\rho \geqslant 0; \theta = \angle AOM, 0 \leqslant \theta < 2\pi.$ 这样规定的数 $\rho$ 和 $\theta$ 叫做点 $M$ 的极坐标，且以有序实数对 $(\rho, \theta)$ 表示， $\rho$ 称为点 $M$ 的极径， $\theta$ 称为点 $M$ 的极角， $O$ 称为极点， $OA$ 称为极轴. 这样建立的坐标系称为极坐标系.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/5db58b5366d3041e1d1b774d2f25c9dfbbfe3b6b14dc3834b4c05cb0075e0ada.jpg)



图2


当点 M 在极点时, 极径 $\rho = 0$ , 极角 $\theta$ 可取任意值. 在极坐标系中, 除了极点 O 以外, 平面上任一点 M 与有序实数对 $(\rho, \theta)$ 之间建立了一一对应关系. 但在实际应用中,有时为了方便起见, 在极坐标中, 允许 $\rho$ 和 $\theta$ 可取一切实数. 这时, 设有两个任意实数 $\rho$ 和 $\theta$ , 先作射线 $OP$ , 使 $\angle AOP = \theta$ , 如果 $\rho > 0$ , 在 $OP$ 上作一点 $M$ , 使 $|OM| = \rho$ ; 如果 $\rho < 0$ , 在 $P$ 向 $O$ 的延长线上, 作一点 $M$ , 使 $|OM| = |\rho|$ (图3). 这样, 对于任意一对实数 $\rho$ 和 $\theta$ , 总可以在平面上确定唯一的一点 $M, (\rho, \theta)$ 仍称为点 $M$ 的极坐标. 由此可知, 有序实数对 $(\rho, \theta)$ 与 $(\rho, \theta + 2k\pi)$ 或 $(- \rho, \theta + (2k + 1)\pi)$ 表示同一个点, 这里

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/c982773535b1b03955b984b75a63dc10b9d67b10d674d11e87e061437c76e29f.jpg)



图3


与直角坐标系一样,在极坐标系中,把曲线看作适合某种条件的点的集合,用曲线上的点的极坐标 $\rho,\theta$ 的关系式 $\varphi(\rho,\theta)=0$ 表示的方程,就是曲线的极坐标方程.

当极坐标系中的极点与直角坐标系中的原点重合,极轴与x轴正半轴重合,两种坐标系的长度单位一致时(图4)，极坐标与直角坐标可以互换.

由直角坐标到极坐标的变换公式为

$$
x = \rho \cos \theta , \quad y = \rho \sin \theta .
$$

由极坐标到直角坐标的变换公式为

$$
\rho^ {2} = x ^ {2} + y ^ {2}, \quad \tan \theta = \frac {y}{x} \quad (x \neq 0).
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/1aeec4f1d52ac5fa3a9c540bd6bade8e851fda65606b581222ede39c70276132.jpg)



图4


下面给出常用曲线的极坐标方程：

1. 圆心在极点, 半径为 r 的圆的方程为 $\rho = r$ .

2. 圆心为 $(a,0)$ ，半径为a的圆的方程为 $\rho=2a\cos\theta$ .

3. 圆心为 $\left(a, \frac{\pi}{2}\right)$ ，半径为 a 的圆的方程为 $\rho = 2a\sin\theta$ .

4. 过极点, 倾角为 $\alpha$ 的直线方程为 $\theta = \alpha (\rho \in \mathbb{R})$ .

5. 过点 $(a,0)$ 且垂直于极轴的直线方程为 $\rho\cos\theta=a$ .

6. 过点 $\left(a,\frac{\pi}{2}\right)$ 且平行于极轴的直线方程为 $\rho\sin\theta=a$ .

# (四) 参数方程

在平面直角坐标系中,如果曲线上任意一点的坐标 x,y 都是某个变量 t 的函数$\left\{ \begin{array}{l} x = \varphi(t), \\ y = \psi(t), \end{array} \right.$ 并且对于 $t$ 的每一个允许的取值，由方程组确定的点 $(x, y)$ 都在这条曲线上，那么这个方程就叫做曲线的参数方程，变量 $t$ 叫做参数.

下面给出常用曲线的参数方程：

1. 以 $(a,b)$ 为圆心，r为半径的圆的参数方程为

$$
\left\{ \begin{array}{l} x = a + r \cos \theta , \\ y = b + r \sin \theta , \end{array} \right.
$$

其中 $\theta$ 为参数.

2. 椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 (a > b > 0)$ 的参数方程为

$$
\left\{ \begin{array}{l} x = a \cos \theta , \\ y = b \sin \theta . \end{array} \right.
$$

3. 双曲线 $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 (a > b > 0)$ 的参数方程为

$$
\left\{ \begin{array}{l} x = a \sec \theta , \\ y = b \tan \theta . \end{array} \right.
$$

4. 抛物线 $y^{2}=2px$ 的参数方程为

$$
\left\{ \begin{array}{l} x = 2 p t ^ {2}, \\ y = 2 p t. \end{array} \right.
$$

# (五) 二阶和三阶行列式

给出二元线性方程组

$$
\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} = b _ {1}, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} = b _ {2}, \end{array} \right. \tag {1}
$$

求这方程组的解.

用大家熟知的消元法,分别消去方程组(1)中的 $x_{2}$ 及 $x_{1}$ ,得

$$
\left\{ \begin{array}{l} (a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1}) x _ {1} = b _ {1} a _ {2 2} - a _ {1 2} b _ {2}, \\ (a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1}) x _ {2} = a _ {1 1} b _ {2} - b _ {1} a _ {2 1}. \end{array} \right. \tag {2}
$$

下面引入二阶行列式,然后利用二阶行列式来进一步讨论上述问题.

设已知四个数排成正方形表

$$
\left( \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right),
$$

则数 $a_{11}a_{22} - a_{12}a_{21}$ 称为对应于这个表的二阶行列式, 用记号

$$
\left| \begin{array}{l l} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| \tag {3}
$$

表示,因此

$$
\left| \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| = a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1}.
$$

数 $a_{11}, a_{12}, a_{21}, a_{22}$ 叫做行列式(3)的元素, 横排叫做行, 竖排叫做列. 元素 $a_{ij}$ 中的第一个指标 $i$ 和第二个指标 $j$ 依次表示该元素所在的行数和列数. 例如, 元素 $a_{21}$ 在行列式(3)中位于第二行和第一列.

现在,方程组(2)可利用行列式来表示.设

$$
D = \left| \begin{array}{l l} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| = a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1},
$$

$$
D _ {1} = \left| \begin{array}{l l} b _ {1} & a _ {1 2} \\ b _ {2} & a _ {2 2} \end{array} \right| = b _ {1} a _ {2 2} - a _ {1 2} b _ {2},
$$

$$
D _ {2} = \left| \begin{array}{l l} a _ {1 1} & b _ {1} \\ a _ {2 1} & b _ {2} \end{array} \right| = a _ {1 1} b _ {2} - b _ {1} a _ {2 1},
$$

则方程组(2)可写成

$$
\left\{ \begin{array}{l} D x _ {1} = D _ {1}, \\ D x _ {2} = D _ {2}. \end{array} \right. \tag {$2^{\prime$}}
$$

我们注意到, D 就是方程组(1)中 $x_{1}$ 及 $x_{2}$ 的系数构成的行列式, 因此称为系数行列式, 而 $D_{1}$ 和 $D_{2}$ 分别是用方程组(1)右端的常数项代替 D 的第一列和第二列而形成的.

若 $D \neq 0$ ，则方程组(2)的解为

$$
x _ {1} = \frac {D _ {1}}{D}, \quad x _ {2} = \frac {D _ {2}}{D}. \tag {4}
$$

把(4)中 $x_{1}$ 及 $x_{2}$ 的值代入方程组(1)，便可证实 $x_{1}$ 及 $x_{2}$ 的这对值也是方程组(1)的解。另一方面，(2)是由(1)导出的，因此(1)的解一定是(2)的解。现在(2)只有一组解(4)，所以(4)是方程组(1)的唯一解。由此得出结论：

在 $D \neq 0$ 的条件下, 方程组(1)有唯一的解

$$
x _ {1} = \frac {D _ {1}}{D}, \quad x _ {2} = \frac {D _ {2}}{D}.
$$

例 1 解方程组

$$
\left\{ \begin{array}{l} 2 x + 3 y = 8, \\ x - 2 y = - 3. \end{array} \right.
$$

解 $D = \left| \begin{array}{cc}2 & 3\\ 1 & -2 \end{array} \right| = 2\times (-2) - 3\times 1 = -7,$ 

$$
D _ {1} = \left| \begin{array}{c c} 8 & 3 \\ - 3 & - 2 \end{array} \right| = 8 \times (- 2) - 3 \times (- 3) = - 7,
$$

$$
D _ {2} = \left| \begin{array}{c c} 2 & 8 \\ 1 & - 3 \end{array} \right| = 2 \times (- 3) - 8 \times 1 = - 1 4.
$$

因 $D = -7 \neq 0$ ，故所给方程组有唯一解

$$
x = \frac {D _ {1}}{D} = \frac {- 7}{- 7} = 1, \quad y = \frac {D _ {2}}{D} = \frac {- 1 4}{- 7} = 2.
$$

下面介绍三阶行列式概念.

设已知 9 个数排成正方形表

$$
\left( \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right),
$$

则数 $a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}-a_{12}a_{21}a_{33}-a_{11}a_{23}a_{32}$ 称为对应于这个表的三阶行列式,用记号

$$
\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right|
$$

表示,因此

$$
\begin{array}{l} \left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| \\ = a _ {1 1} a _ {2 2} a _ {3 3} + a _ {1 2} a _ {2 3} a _ {3 1} + a _ {1 3} a _ {2 1} a _ {3 2} - a _ {1 3} a _ {2 2} a _ {3 1} - a _ {1 2} a _ {2 1} a _ {3 3} - a _ {1 1} a _ {2 3} a _ {3 2}. \tag {5} \\ \end{array}
$$

关于三阶行列式的元素、行、列等概念，与二阶行列式的相应概念类似，不再重复.

(5)式右端相当复杂,我们可以借助图5得出它的计算法则(通常称为对角线法则):

行列式中从左上角到右下角的直线称为主对角线,从右上角到左下角的直线称为次对角线.主对角线上元素的乘积以及位于主对角线的平行线上的元素与对角上的元素的乘积,前面都取正号.次对角线上元素的乘积以及位于次对角线的平行线上的元素与对角上的元素的乘积,前面都取负号.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/acc2a8bad944ee66f1985943d16ba1c20bb03774b8edf8aa53b9af1aef90a896.jpg)



图5


例2 $\left| \begin{array}{ccc}2 & 1 & 2\\ -4 & 3 & 1\\ 2 & 3 & 5 \end{array} \right|$ 

$$
\begin{array}{l} = 2 \times 3 \times 5 + 1 \times 1 \times 2 + 2 \times (- 4) \times 3 - 2 \times 3 \times 2 - 1 \times (- 4) \times 5 - 2 \times 1 \times 3 \\ = 3 0 + 2 - 2 4 - 1 2 + 2 0 - 6 = 1 0. \\ \end{array}
$$

利用交换律及结合律,可把(5)式改写如下:

$$
\left| \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = a _ {1 1} (a _ {2 2} a _ {3 3} - a _ {2 3} a _ {3 2}) - a _ {1 2} (a _ {2 1} a _ {3 3} - a _ {2 3} a _ {3 1}) + a _ {1 3} (a _ {2 1} a _ {3 2} - a _ {2 2} a _ {3 1}).
$$

把上式右端三个括号中的式子表示为二阶行列式,则有

$$
\left| \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = a _ {1 1} \left| \begin{array}{c c} a _ {2 2} & a _ {2 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| - a _ {1 2} \left| \begin{array}{c c} a _ {2 1} & a _ {2 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right| + a _ {1 3} \left| \begin{array}{c c} a _ {2 1} & a _ {2 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right|.
$$

上式称为三阶行列式按第一行的展开式.

例 3 将例 2 中的行列式按第一行展开并计算它的值.

解 $\left|\begin{array}{ccc}2 & 1 & 2 \\ -4 & 3 & 1 \\ 2 & 3 & 5\end{array}\right|=2\left|\begin{array}{cc}3 & 1 \\ 3 & 5\end{array}\right|-\left|\begin{array}{cc} -4 & 1 \\ 2 & 5\end{array}\right|+2\left|\begin{array}{cc} -4 & 3 \\ 2 & 3\end{array}\right|$ 

$$
= 2 \times 1 2 - (- 2 2) + 2 \times (- 1 8) = 2 4 + 2 2 - 3 6 = 1 0.
$$

# 习题

1. 利用二阶行列式解下列方程组：

(1) $\left\{\begin{aligned}5x-y&=2,\\ 3x+2y&=9;\end{aligned}\right.$ 

(2) $\left\{ \begin{array}{l} 3x + 4y = 2, \\ 2x + 3y = 7. \end{array} \right.$ 

2. 利用对角线法则, 计算下列各行列式:

(1) $\left| \begin{array}{ccc}2 & 0 & 1\\ 1 & -4 & -1\\ -1 & 8 & 3 \end{array} \right|$ ; 

(2) $\left| \begin{array}{ccc}4 & -2 & 4\\ 10 & 2 & 12\\ 1 & 2 & 2 \end{array} \right|$ ; 

(3) $\left| \begin{array}{ccc}3 & 4 & 2\\ 7 & 5 & 1\\ 3 & 2 & 4 \end{array} \right|$ ; 

(4) $\left| \begin{array}{ccc}1 & 1 & 1\\ 1 & 1 + a & 1\\ 1 & 1 & 1 + b \end{array} \right|$ 

3. 将下列行列式按第一行展开并计算它们的值：

(1) $\left| \begin{array}{ccc}1 & 2 & 3\\ 3 & 1 & 2\\ 2 & 3 & 1 \end{array} \right|$ ; 

(2) $\left| \begin{array}{ccc} - 1 & 2 & 2\\ 2 & -1 & 2\\ 2 & 2 & -1 \end{array} \right|$ 

4. 证明下列等式：

(1) $\left| \begin{array}{lll}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33} \end{array} \right| = -a_{21}\left| \begin{array}{ll}a_{12} & a_{13}\\ a_{32} & a_{33} \end{array} \right| + a_{22}\left| \begin{array}{ll}a_{11} & a_{13}\\ a_{31} & a_{33} \end{array} \right| - a_{23}\left| \begin{array}{ll}a_{11} & a_{12}\\ a_{31} & a_{32} \end{array} \right|$ 

(2) $\left| \begin{array}{lll}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33} \end{array} \right| = a_{31}\left| \begin{array}{ll}a_{12} & a_{13}\\ a_{22} & a_{23} \end{array} \right| - a_{32}\left| \begin{array}{ll}a_{11} & a_{13}\\ a_{21} & a_{23} \end{array} \right| + a_{33}\left| \begin{array}{ll}a_{11} & a_{12}\\ a_{21} & a_{22} \end{array} \right|.$ 

注:上面这两个等式分别称为三阶行列式按第二行和按第三行的展开式.

# 答 案

1. (1) x=1, y=3; (2) x=-22, y=17. 

2. (1) -4; (2) 8; (3) -48; (4) ab. 

3. (1) 18; (2) 27. 

4. 略.

# 附录Ⅱ

# 基本初等函数的图形


幂函数


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/93753b09c9603ef9d907b7e20ca9e56fdfcd784cbaa92fa55de5b10e6d48dc2b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/9fec398fbde841ebd77143affeecfe38f132b6ca4560a9144cf2df937a447ebf.jpg)


$$
y = x ^ {\mu}
$$


指数函数


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/2ee34a39fba4cb8ab23f3831bd71ed801df1c4aae4061579ecf35de069c0c46e.jpg)


$$
y = a ^ {x}
$$


对数函数


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/81a1f56be2a4e17b2e25d167f89beb2f8169063aae65e82f37740a49418daec4.jpg)


$$
y = \log_ {a} x
$$


三角函数


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/0a2b1741761d08bc16ac10f63b35d4a3551ed39a3003b51e7e2eef5d14c3dcb4.jpg)


$$
y = \sin x
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/32f1f0e21a95d30e73c0566d98171f1151559f659c1536dc4547833d0310a33d.jpg)



$y = \cos x$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/5e17d5ef2839d49944654b294ab48d144d59a99a8c4b14f8ec038d1c925e2565.jpg)



$y=\tan x$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/5bf30902c6bf2476fe94a2fc471a6e5730dd4bfb39654ea046646d786aba1bc0.jpg)



$y = \cot x$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/e8a954117a2143fbe0839485fa99717b0f0e9ee4a85db817d8be6875e3cd0843.jpg)



y=sec x


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/c22b4a3dc412c36fe3df05b97b656b3cfe4ce41f459b6d5cf056c15115799e4f.jpg)



$y = \csc x$



反三角函数


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/d44b5e73b44b3f3ce85d8b8399ecd510dc46eeb3660ce1c65bf1bcc797c63615.jpg)



$y=\arcsin x$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/891ecebe40d2ebb261a1df65a92ed48a4d00baa6a542d42517e215ed431d6410.jpg)



$y=\arccos x$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/2f9ba5081357cfe5b59b68ff93e55ba8cd60462a5f6693e5376db3a4b886a01b.jpg)



$y = \arctan x$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/331eb9b3e2c03ad6324bd0e9c54ad8c03a140822e04c0ace251d21649cbf3edf.jpg)



$y = \operatorname{arccot} x$


# 附录Ⅲ

# 几种常用的曲线

(1) 三次抛物线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/9e41336ce1cae4d5491902d87df7fa517523b76537d29b27f267ddc38a1d5126.jpg)


$$
y = a x ^ {3}
$$

(2) 半立方抛物线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/0171e664ebb8d76fa4665e32add37365ab6aabfdbdb9173a559928d977c6b5c7.jpg)


$$
y ^ {2} = a x ^ {3}
$$

(3) 概率曲线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/a7c8c5fd7c555c5014f91b1f81f94691605956e83ea13eb9c6d519c632517060.jpg)


$$
y = \mathrm{e} ^ {- x ^ {2}}
$$

(4) 箕舌线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/5480e91352ac5573bc9ce2bcdf1b8ef0bd6dcc0767919b4f2da8d38c4d82757f.jpg)


$$
y = \frac {8 a ^ {3}}{x ^ {2} + 4 a ^ {2}}
$$

(5) 蔓叶线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/bdb3de22a5a6c734a4b53f229fd62795a77b271d3d2c8c70a1a2140d469ac36f.jpg)


$$
y ^ {2} (2 a - x) = x ^ {3}
$$

(6) 笛卡儿叶形线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/772a77b1e6f4a5d905bf1b28820d8d9e73d81c47deaa4d7f933c5b03bf708dc3.jpg)


$$
x ^ {3} + y ^ {3} - 3 a x y = 0
$$

$$
x = \frac {3 a t}{1 + t ^ {3}}, y = \frac {3 a t ^ {2}}{1 + t ^ {3}}
$$

(7) 星形线(内摆线的一种)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/010fdddeba02f0a6f375f2e0f2e26a23eded16070cce7d84dcafb23cf9ac4db6.jpg)


$$
x ^ {\frac {2}{3}} + y ^ {\frac {2}{3}} = a ^ {\frac {2}{3}}
$$

$$
\left\{ \begin{array}{l} x = a \cos^ {3} \theta \\ y = a \sin^ {3} \theta \end{array} \right.
$$

(8) 摆线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/d7a6346dbcf1c3117660963efa9c1684993211bb5a7d3384cf319b2ab2b2fe67.jpg)


$$
\left\{ \begin{array}{l} x = a (\theta - \sin \theta) \\ y = a (1 - \cos \theta) \end{array} \right.
$$

(9) 心形线(外摆线的一种)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/bbac919bbced2d41ca492297b314747e865e22d584815569b17a2af3681f7018.jpg)


$$
x ^ {2} + y ^ {2} + a x = a \sqrt {x ^ {2} + y ^ {2}}
$$

$$
\rho = a (1 - \cos \theta)
$$

(10) 阿基米德螺线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/936ff2f060caea6001ac6e98d22f3748ae6d309c24d9826fd63e77c724306c75.jpg)


$$
\rho = a \theta
$$

(11) 对数螺线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/fd8436b07cc3989cdd29b5943b7d503b0d4edc79e4a8fb741b9dd213edb7c9db.jpg)


(12) 双曲螺线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/a9f9e2bfed6f9efe489303b8bcd7e98456d62889a7d342a73fff4f2cb9c72f0c.jpg)


(13) 伯努利双纽线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/2e56b61449ab5d331c76af3a1ebb36b0724b9f6f5b5838267b0ad39b08a82abc.jpg)


$$
\left(x ^ {2} + y ^ {2}\right) ^ {2} = 2 a ^ {2} x y
$$

$$
\rho^ {2} = a ^ {2} \sin 2 \theta
$$

(14) 伯努利双纽线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/6115693be6144e7d0a1e7a5ccd933fd8dc8d396e5f2809e0154633c994cad342.jpg)


$$
\left(x ^ {2} + y ^ {2}\right) ^ {2} = a ^ {2} \left(x ^ {2} - y ^ {2}\right)
$$

$$
\rho^ {2} = a ^ {2} \cos 2 \theta
$$

(15) 三叶玫瑰线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/f4046ab9ac53a33f3cb1daabde0299dd4cc3276438363966d50e17f9ff57dfa5.jpg)


$$
\rho = a \cos 3 \theta
$$

(16) 三叶玫瑰线

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/7abc1245e75ec93053a74977fc01df7c6287814ad9c7bd23b02862cde4b9b7b3.jpg)


$$
\rho = a \sin 3 \theta
$$


(17) 四叶玫瑰线


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/1b16ea57e4a7f1e253764468bf1454b2f59055d9f7a9764193aabe535c829b8f.jpg)



$\rho = a\sin 2\theta$



(18) 四叶玫瑰线


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/ca7eea0e-072d-476e-a3b5-65d39d9627bd/a4831ee470b5d3d2658534d4691588de5b0d96d81b6d7069ce504d24d7abf1e2.jpg)



$\rho = a\cos 2\theta$


# 附录IV

# 积分表

# (一) 含有 $ax + b$ 的积分

1. $\int \frac{\mathrm{d}x}{ax + b} = \frac{1}{a}\ln |ax + b| + C.$ 

2. $\int (ax + b)^{\mu}\mathrm{d}x = \frac{1}{a(\mu + 1)} (ax + b)^{\mu + 1} + C (\mu \neq -1).$ 

3. $\int \frac{x}{ax + b}\mathrm{d}x = \frac{1}{a^2} (ax + b - b\ln |ax + b|) + C.$ 

4. $\int \frac{x^2}{ax + b}\mathrm{d}x = \frac{1}{a^3}\left[\frac{1}{2} (ax + b)^2 -2b(ax + b) + b^2\ln |ax + b|\right] + C.$ 

5. $\int \frac{\mathrm{d}x}{x(ax + b)} = -\frac{1}{b}\ln \left|\frac{ax + b}{x}\right| + C.$ 

6. $\int \frac{\mathrm{d}x}{x^2(ax + b)} = -\frac{1}{bx} +\frac{a}{b^2}\ln \left|\frac{ax + b}{x}\right| + C.$ 

7. $\int \frac{x}{(ax + b)^2} \mathrm{d}x = \frac{1}{a^2} \left( \ln |ax + b| + \frac{b}{ax + b} \right) + C.$ 

8. $\int \frac{x^2}{(ax + b)^2} \mathrm{d}x = \frac{1}{a^3} \left( ax + b - 2b \ln |ax + b| - \frac{b^2}{ax + b} \right) + C.$ 

9. $\int \frac{\mathrm{d}x}{x(ax + b)^2} = \frac{1}{b(ax + b)} -\frac{1}{b^2}\ln \left|\frac{ax + b}{x}\right| + C.$ 

# (二) 含有 $\sqrt{ax+b}$ 的积分

10. $\int \sqrt{ax + b} \, \mathrm{d}x = \frac{2}{3a} \sqrt{(ax + b)^3} + C.$ 

11. $\int x\sqrt{ax + b}\mathrm{d}x = \frac{2}{15a^2} (3ax - 2b)\sqrt{(ax + b)^3} +C.$ 

12. $\int x^{2}\sqrt{ax + b}\mathrm{d}x = \frac{2}{105a^{3}} (15a^{2}x^{2} - 12abx + 8b^{2})\sqrt{(ax + b)^{3}} +C.$ 

13. $\int \frac{x}{\sqrt{ax + b}}\mathrm{d}x = \frac{2}{3a^2} (ax - 2b)\sqrt{ax + b} +C.$ 

14. $\int \frac{x^2}{\sqrt{ax + b}}\mathrm{d}x = \frac{2}{15a^3}\left(3a^2 x^2 -4abx + 8b^2\right)\sqrt{ax + b} +C.$ 

15. $\int \frac{\mathrm{d}x}{x\sqrt{ax + b}} = \left\{ \begin{array}{ll} \frac{1}{\sqrt{b}}\ln \left|\frac{\sqrt{ax + b} - \sqrt{b}}{\sqrt{ax + b} + \sqrt{b}}\right| + C & (b > 0),\\  \frac{2}{\sqrt{-b}}\arctan \sqrt{\frac{ax + b}{-b}} +C & (b <   0). \end{array} \right.$ 

16. $\int \frac{\mathrm{d}x}{x^2\sqrt{ax + b}} = -\frac{\sqrt{ax + b}}{bx} -\frac{a}{2b}\int \frac{\mathrm{d}x}{x\sqrt{ax + b}}.$ 

17. $\int \frac{\sqrt{ax + b}}{x}\mathrm{d}x = 2\sqrt{ax + b} +b\int \frac{\mathrm{d}x}{x\sqrt{ax + b}}.$ 

18. $\int \frac{\sqrt{ax + b}}{x^2}\mathrm{d}x = -\frac{\sqrt{ax + b}}{x} +\frac{a}{2}\int \frac{\mathrm{d}x}{x\sqrt{ax + b}}.$ 

# (三) 含有 $x^{2} \pm a^{2}$ 的积分

19. $\int \frac{\mathrm{d}x}{x^2 + a^2} = \frac{1}{a}\arctan \frac{x}{a} + C.$ 

20. $\int \frac{\mathrm{d}x}{(x^2 + a^2)^n} = \frac{x}{2(n - 1)a^2(x^2 + a^2)^{n - 1}} +\frac{2n - 3}{2(n - 1)a^2}\int \frac{\mathrm{d}x}{(x^2 + a^2)^{n - 1}}.$ 

21. $\int \frac{\mathrm{d}x}{x^2 - a^2} = \frac{1}{2a}\ln \left|\frac{x - a}{x + a}\right| + C.$ 

# (四) 含有 $ax^{2}+b$ (a>0) 的积分

22. $\int \frac{\mathrm{d}x}{ax^2 + b} = \left\{ \begin{array}{ll} \frac{1}{\sqrt{ab}}\arctan \sqrt{\frac{a}{b}} x + C & (b > 0),\\  \frac{1}{2\sqrt{-ab}}\ln \left|\frac{\sqrt{a}x - \sqrt{-b}}{\sqrt{a}x + \sqrt{-b}}\right| + C & (b <   0). \end{array} \right.$ 

23. $\int \frac{x}{ax^2 + b}\mathrm{d}x = \frac{1}{2a}\ln |ax^2 +b| + C.$ 

24. $\int \frac{x^2}{ax^2 + b}\mathrm{d}x = \frac{x}{a} -\frac{b}{a}\int \frac{\mathrm{d}x}{ax^2 + b}.$ 

25. $\int \frac{\mathrm{d}x}{x(ax^2 + b)} = \frac{1}{2b}\ln \frac{x^2}{|ax^2 + b|} + C.$ 

26. $\int \frac{\mathrm{d}x}{x^2(ax^2 + b)} = -\frac{1}{bx} -\frac{a}{b}\int \frac{\mathrm{d}x}{ax^2 + b}.$ 

27. $\int \frac{\mathrm{d}x}{x^3(ax^2 + b)} = \frac{a}{2b^2}\ln \frac{|ax^2 + b|}{x^2} -\frac{1}{2bx^2} +C.$ 

28. $\int \frac{\mathrm{d}x}{(ax^2 + b)^2} = \frac{x}{2b(ax^2 + b)} +\frac{1}{2b}\int \frac{\mathrm{d}x}{ax^2 + b}.$ 

# (五) 含有 $ax^{2}+bx+c$ (a>0) 的积分

29. $\int \frac{\mathrm{d}x}{ax^2 + bx + c} = \left\{ \begin{array}{ll} \frac{2}{\sqrt{4ac - b^2}}\arctan \frac{2ax + b}{\sqrt{4ac - b^2}} + C & (b^2 < 4ac),\\  \frac{1}{\sqrt{b^2 - 4ac}}\ln \left|\frac{2ax + b - \sqrt{b^2 - 4ac}}{2ax + b + \sqrt{b^2 - 4ac}}\right| + C & (b^2 >4ac). \end{array} \right.$ 

30. $\int \frac{x}{ax^2 + bx + c}\mathrm{d}x = \frac{1}{2a}\ln |ax^2 +bx + c| - \frac{b}{2a}\int \frac{\mathrm{d}x}{ax^2 + bx + c}.$ 

# (六) 含有 $\sqrt{x^{2}+a^{2}}$ (a>0) 的积分

31. $\int \frac{\mathrm{d}x}{\sqrt{x^2 + a^2}} = \operatorname {arsh}\frac{x}{a} +C_1 = \ln (x + \sqrt{x^2 + a^2}) + C.$ 

32. $\int \frac{\mathrm{d}x}{\sqrt{(x^2 + a^2)^3}} = \frac{x}{a^2\sqrt{x^2 + a^2}} + C.$ 

33. $\int \frac{x}{\sqrt{x^2 + a^2}}\mathrm{d}x = \sqrt{x^2 + a^2} +C.$ 

34. $\int \frac{x}{\sqrt{(x^2 + a^2)^3}}\mathrm{d}x = -\frac{1}{\sqrt{x^2 + a^2}} +C.$ 

35. $\int \frac{x^2}{\sqrt{x^2 + a^2}}\mathrm{d}x = \frac{x}{2}\sqrt{x^2 + a^2} -\frac{a^2}{2}\ln (x + \sqrt{x^2 + a^2}) + C.$ 

36. $\int \frac{x^2}{\sqrt{(x^2 + a^2)^3}}\mathrm{d}x = -\frac{x}{\sqrt{x^2 + a^2}} +\ln (x + \sqrt{x^2 + a^2}) + C.$ 

37. $\int \frac{\mathrm{d}x}{x\sqrt{x^2 + a^2}} = \frac{1}{a}\ln \frac{\sqrt{x^2 + a^2} - a}{|x|} +C.$ 

38. $\int \frac{\mathrm{d}x}{x^2\sqrt{x^2 + a^2}} = -\frac{\sqrt{x^2 + a^2}}{a^2x} + C.$ 

39. $\int \sqrt{x^2 + a^2} \, \mathrm{d}x = \frac{x}{2}\sqrt{x^2 + a^2} + \frac{a^2}{2}\ln (x + \sqrt{x^2 + a^2}) + C.$ 

40. $\int \sqrt{(x^2 + a^2)^3} \, \mathrm{d}x = \frac{x}{8}(2x^2 + 5a^2) \sqrt{x^2 + a^2} + \frac{3}{8} a^4 \ln (x + \sqrt{x^2 + a^2}) + C.$ 

41. $\int x\sqrt{x^2 + a^2}\mathrm{d}x = \frac{1}{3}\sqrt{(x^2 + a^2)^3} +C.$ 

42. $\int x^{2}\sqrt{x^{2} + a^{2}}\mathrm{d}x = \frac{x}{8}(2x^{2} + a^{2})\sqrt{x^{2} + a^{2}} -\frac{a^{4}}{8}\ln (x + \sqrt{x^{2} + a^{2}}) + C.$ 

43. $\int \frac{\sqrt{x^2 + a^2}}{x}\mathrm{d}x = \sqrt{x^2 + a^2} +a\ln \frac{\sqrt{x^2 + a^2} - a}{|x|} +C.$ 

44. $\int \frac{\sqrt{x^2 + a^2}}{x^2}\mathrm{d}x = -\frac{\sqrt{x^2 + a^2}}{x} +\ln (x + \sqrt{x^2 + a^2}) + C.$ 

# (七) 含有 $\sqrt{x^{2}-a^{2}}$ (a>0) 的积分

45. $\int \frac{\mathrm{d}x}{\sqrt{x^2 - a^2}} = \frac{x}{|x|}$ arch $\frac{|x|}{a} + C_1 = \ln |x + \sqrt{x^2 - a^2}| + C.$ 

46. $\int \frac{\mathrm{d}x}{\sqrt{(x^2 - a^2)^3}} = -\frac{x}{a^2\sqrt{x^2 - a^2}} + C.$ 

47. $\int \frac{x}{\sqrt{x^2 - a^2}}\mathrm{d}x = \sqrt{x^2 - a^2} + C.$ 

48. $\int \frac{x}{\sqrt{(x^2 - a^2)^3}}\mathrm{d}x = -\frac{1}{\sqrt{x^2 - a^2}} +C.$ 

49. $\int \frac{x^2}{\sqrt{x^2 - a^2}}\mathrm{d}x = \frac{x}{2}\sqrt{x^2 - a^2} +\frac{a^2}{2}\ln |x + \sqrt{x^2 - a^2}| + C.$ 

50. $\int \frac{x^2}{\sqrt{(x^2 - a^2)^3}}\mathrm{d}x = -\frac{x}{\sqrt{x^2 - a^2}} +\ln |x + \sqrt{x^2 - a^2}| + C.$ 

51. $\int \frac{\mathrm{d}x}{x\sqrt{x^2 - a^2}} = \frac{1}{a}\arccos \frac{a}{|x|} + C.$ 

52. $\int \frac{\mathrm{d}x}{x^2\sqrt{x^2 - a^2}} = \frac{\sqrt{x^2 - a^2}}{a^2x} + C.$ 

53. $\int \sqrt{x^2 - a^2} \, \mathrm{d}x = \frac{x}{2} \sqrt{x^2 - a^2} - \frac{a^2}{2} \ln |x + \sqrt{x^2 - a^2}| + C.$ 

54. $\int \sqrt{(x^2 - a^2)^3} \, \mathrm{d}x = \frac{x}{8}(2x^2 - 5a^2) \sqrt{x^2 - a^2} + \frac{3}{8} a^4 \ln |x + \sqrt{x^2 - a^2}| + C.$ 

55. $\int x\sqrt{x^2 - a^2}\mathrm{d}x = \frac{1}{3}\sqrt{(x^2 - a^2)^3} +C.$ 

56. $\int x^{2}\sqrt{x^{2} - a^{2}}\mathrm{d}x = \frac{x}{8} (2x^{2} - a^{2})\sqrt{x^{2} - a^{2}} -\frac{a^{4}}{8}\ln |x + \sqrt{x^{2} - a^{2}}| + C.$ 

57. $\int \frac{\sqrt{x^2 - a^2}}{x} \mathrm{d}x = \sqrt{x^2 - a^2} - a \arccos \frac{a}{|x|} + C.$ 

58. $\int \frac{\sqrt{x^2 - a^2}}{x^2}\mathrm{d}x = -\frac{\sqrt{x^2 - a^2}}{x} +\ln |x + \sqrt{x^2 - a^2}| + C.$ 

(八) 含有 $\sqrt{a^{2}-x^{2}}$ (a>0) 的积分

59. $\int \frac{\mathrm{d}x}{\sqrt{a^2 - x^2}} = \arcsin \frac{x}{a} + C.$ 

60. $\int \frac{\mathrm{d}x}{\sqrt{(a^2 - x^2)^3}} = \frac{x}{a^2\sqrt{a^2 - x^2}} + C.$ 

61. $\int \frac{x}{\sqrt{a^2 - x^2}}\mathrm{d}x = -\sqrt{a^2 - x^2} + C.$ 

62. $\int \frac{x}{\sqrt{(a^2 - x^2)^3}}\mathrm{d}x = \frac{1}{\sqrt{a^2 - x^2}} +C.$ 

63. $\int \frac{x^2}{\sqrt{a^2 - x^2}}\mathrm{d}x = -\frac{x}{2}\sqrt{a^2 - x^2} +\frac{a^2}{2}\arcsin \frac{x}{a} +C.$ 

64. $\int \frac{x^2}{\sqrt{(a^2 - x^2)^3}}\mathrm{d}x = \frac{x}{\sqrt{a^2 - x^2}} -\arcsin \frac{x}{a} +C.$ 

65. $\int \frac{\mathrm{d}x}{x\sqrt{a^2 - x^2}} = \frac{1}{a}\ln \frac{a - \sqrt{a^2 - x^2}}{|x|} + C.$ 

66. $\int \frac{\mathrm{d}x}{x^2\sqrt{a^2 - x^2}} = -\frac{\sqrt{a^2 - x^2}}{a^2x} + C.$ 

67. $\int \sqrt{a^2 - x^2} \, \mathrm{d}x = \frac{x}{2}\sqrt{a^2 - x^2} + \frac{a^2}{2}\arcsin \frac{x}{a} + C.$ 

68. $\int \sqrt{(a^2 - x^2)^3} \, \mathrm{d}x = \frac{x}{8}(5a^2 - 2x^2) \sqrt{a^2 - x^2} + \frac{3}{8} a^4 \arcsin \frac{x}{a} + C.$ 

69. $\int x\sqrt{a^2 - x^2}\mathrm{d}x = -\frac{1}{3}\sqrt{(a^2 - x^2)^3} + C.$ 

70. $\int x^{2}\sqrt{a^{2} - x^{2}}\mathrm{d}x = \frac{x}{8}(2x^{2} - a^{2})\sqrt{a^{2} - x^{2}} +\frac{a^{4}}{8}\arcsin \frac{x}{a} +C.$ 

71. $\int \frac{\sqrt{a^2 - x^2}}{x}\mathrm{d}x = \sqrt{a^2 - x^2} + a\ln \frac{a - \sqrt{a^2 - x^2}}{|x|} + C.$ 

72. $\int \frac{\sqrt{a^2 - x^2}}{x^2}\mathrm{d}x = -\frac{\sqrt{a^2 - x^2}}{x} -\arcsin \frac{x}{a} +C.$ 

(九) 含有 $\sqrt{\pm ax^{2}+bx+c}$ (a>0) 的积分

73. $\int \frac{\mathrm{d}x}{\sqrt{ax^2 + bx + c}} = \frac{1}{\sqrt{a}}\ln \left|2ax + b + 2\sqrt{a}\sqrt{ax^2 + bx + c}\right| + C.$ 

74. $\int \sqrt{ax^2 + bx + c} \, \mathrm{d}x = \frac{2ax + b}{4a}\sqrt{ax^2 + bx + c} + \frac{4ac - b^2}{8\sqrt{a^3}}\ln \left|2ax + b + 2\sqrt{a}\sqrt{ax^2 + bx + c}\right| + C.$ 

75. $\int \frac{x}{\sqrt{ax^2 + bx + c}}\mathrm{d}x = \frac{1}{a}\sqrt{ax^2 + bx + c} -\frac{b}{2\sqrt{a^3}}\ln \left|2ax + b + 2\sqrt{a}\sqrt{ax^2 + bx + c}\right| + C.$ 

76. $\int \frac{\mathrm{d}x}{\sqrt{c + bx - ax^2}} = \frac{1}{\sqrt{a}}\arcsin \frac{2ax - b}{\sqrt{b^2 + 4ac}} +C.$ 

77. $\int \sqrt{c + bx - ax^2} \, \mathrm{d}x = \frac{2ax - b}{4a}\sqrt{c + bx - ax^2} + \frac{b^2 + 4ac}{8\sqrt{a^3}} \arcsin \frac{2ax - b}{\sqrt{b^2 + 4ac}} + C.$ 

78. $\int \frac{x}{\sqrt{c + bx - ax^2}}\mathrm{d}x = -\frac{1}{a}\sqrt{c + bx - ax^2} +\frac{b}{2\sqrt{a^3}}\arcsin \frac{2ax - b}{\sqrt{b^2 + 4ac}} +C.$ 

(十) 含有 $\sqrt{\pm\frac{x-a}{x-b}}$ 或 $\sqrt{(x-a)(b-x)}$ 的积分

79. $\int \sqrt{\frac{x - a}{x - b}}\mathrm{d}x = (x - b)\sqrt{\frac{x - a}{x - b}} +(b - a)\ln (\sqrt{|x - a|} +\sqrt{|x - b|}) + C.$ 

80. $\int \sqrt{\frac{x - a}{b - x}}\mathrm{d}x = (x - b)\sqrt{\frac{x - a}{b - x}} +(b - a)\arcsin \sqrt{\frac{x - a}{b - a}} +C.$ 

81. $\int \frac{\mathrm{d}x}{\sqrt{(x - a)(b - x)}} = 2\arcsin \sqrt{\frac{x - a}{b - a}} + C$ （ $a <   b$ 

82. $\int \sqrt{(x - a)(b - x)}\mathrm{d}x = \frac{2x - a - b}{4}\sqrt{(x - a)(b - x)} +\frac{(b - a)^2}{4}\arcsin \sqrt{\frac{x - a}{b - a}} +C(a <   b).$ 

# (十一) 含有三角函数的积分

83. $\int \sin x\mathrm{d}x = -\cos x + C.$ 

84. $\int \cos x\mathrm{d}x = \sin x + C.$ 

85. $\int \tan x\mathrm{d}x = -\ln |\cos x| + C.$ 

86. $\int \cot x\mathrm{d}x = \ln |\sin x| + C.$ 

87. $\int \sec x\mathrm{d}x = \ln \left|\tan \left(\frac{\pi}{4} +\frac{x}{2}\right)\right| + C = \ln |\sec x + \tan x| + C.$ 

88. $\int \csc x\mathrm{d}x = \ln \left|\tan \frac{x}{2}\right| + C = \ln |\csc x - \cot x| + C.$ 

89. $\int \sec^2 x\mathrm{d}x = \tan x + C.$ 

90. $\int \csc^2 x\mathrm{d}x = -\cot x + C.$ 

91. $\int \sec x\tan x\mathrm{d}x = \sec x + C.$ 

92. $\int \csc x\cot x\mathrm{d}x = -\csc x + C.$ 

93. $\int \sin^2 x\mathrm{d}x = \frac{x}{2} -\frac{1}{4}\sin 2x + C.$ 

94. $\int \cos^2 x\mathrm{d}x = \frac{x}{2} +\frac{1}{4}\sin 2x + C.$ 

95. $\int \sin^n x\mathrm{d}x = -\frac{1}{n}\sin^{n - 1}x\cos x + \frac{n - 1}{n}\int \sin^{n - 2}x\mathrm{d}x.$ 

96. $\int \cos^n x\mathrm{d}x = \frac{1}{n}\cos^{n - 1}x\sin x + \frac{n - 1}{n}\int \cos^{n - 2}x\mathrm{d}x.$ 

97. $\int \frac{\mathrm{d}x}{\sin^n x} = -\frac{1}{n - 1}\cdot \frac{\cos x}{\sin^{n - 1}x} +\frac{n - 2}{n - 1}\int \frac{\mathrm{d}x}{\sin^{n - 2}x}.$ 

98. $\int \frac{\mathrm{d}x}{\cos^n x} = \frac{1}{n - 1}\cdot \frac{\sin x}{\cos^{n - 1}x} +\frac{n - 2}{n - 1}\int \frac{\mathrm{d}x}{\cos^{n - 2}x}.$ 

99. $\int \cos^m x\sin^n x\mathrm{d}x = \frac{1}{m + n}\cos^{m - 1}x\sin^{n + 1}x + \frac{m - 1}{m + n}\int \cos^{m - 2}x\sin^n x\mathrm{d}x$ 

$$
= - \frac {1}{m + n} \cos^ {m + 1} x \sin^ {n - 1} x + \frac {n - 1}{m + n} \int \cos^ {m} x \sin^ {n - 2} x d x.
$$

100. $\int \sin ax\cos bx\mathrm{d}x = -\frac{1}{2(a + b)}\cos (a + b)x - \frac{1}{2(a - b)}\cos (a - b)x + C.$ 

101. $\int \sin ax\sin bx\mathrm{d}x = -\frac{1}{2(a + b)}\sin (a + b)x + \frac{1}{2(a - b)}\sin (a - b)x + C.$ 

102. $\int \cos ax\cos bx\mathrm{d}x = \frac{1}{2(a + b)}\sin (a + b)x + \frac{1}{2(a - b)}\sin (a - b)x + C.$ 

103. $\int \frac{\mathrm{d}x}{a + b\sin x} = \frac{2}{\sqrt{a^2 - b^2}}\arctan \frac{a\tan\frac{x}{2} + b}{\sqrt{a^2 - b^2}} +C (a^2 >b^2).$ 

104. $\int \frac{\mathrm{d}x}{a + b\sin x} = \frac{1}{\sqrt{b^2 - a^2}}\ln \left|\frac{a\tan\frac{x}{2} + b - \sqrt{b^2 - a^2}}{a\tan\frac{x}{2} + b + \sqrt{b^2 - a^2}}\right| + C(a^2 < b^2).$ 

105. $\int \frac{\mathrm{d}x}{a + b\cos x} = \frac{2}{a + b}\sqrt{\frac{a + b}{a - b}}\arctan \left(\sqrt{\frac{a - b}{a + b}}\tan \frac{x}{2}\right) + C(a^2 >b^2).$ 

106. $\int \frac{\mathrm{d}x}{a + b\cos x} = \frac{1}{a + b}\sqrt{\frac{a + b}{b - a}}\ln \left|\frac{\tan\frac{x}{2} + \sqrt{\frac{a + b}{b - a}}}{\tan\frac{x}{2} - \sqrt{\frac{a + b}{b - a}}}\right| + C(a^2 < b^2).$ 

107. $\int \frac{\mathrm{d}x}{a^2\cos^2 x + b^2\sin^2 x} = \frac{1}{ab}\arctan \left(\frac{b}{a}\tan x\right) + C.$ 

108. $\int \frac{\mathrm{d}x}{a^2\cos^2x - b^2\sin^2x} = \frac{1}{2ab}\ln \left|\frac{b\tan x + a}{b\tan x - a}\right| + C.$ 

109. $\int x\sin ax\mathrm{d}x = \frac{1}{a^2}\sin ax - \frac{1}{a} x\cos ax + C.$ 

110. $\int x^{2}\sin ax\mathrm{d}x = -\frac{1}{a} x^{2}\cos ax + \frac{2}{a^{2}} x\sin ax + \frac{2}{a^{3}}\cos ax + C.$ 

111. $\int x\cos ax\mathrm{d}x = \frac{1}{a^2}\cos ax + \frac{1}{a} x\sin ax + C.$ 

112. $\int x^{2}\cos ax\mathrm{d}x = \frac{1}{a} x^{2}\sin ax + \frac{2}{a^{2}} x\cos ax - \frac{2}{a^{3}}\sin ax + C.$ 

# (十二) 含有反三角函数的积分 (其中 $a > 0$ )

113. $\int \arcsin \frac{x}{a} \mathrm{d}x = x \arcsin \frac{x}{a} + \sqrt{a^2 - x^2} + C.$ 

114. $\int x\arcsin \frac{x}{a}\mathrm{d}x = \left(\frac{x^2}{2} -\frac{a^2}{4}\right)\arcsin \frac{x}{a} +\frac{x}{4}\sqrt{a^2 - x^2} +C.$ 

115. $\int x^{2}\arcsin \frac{x}{a}\mathrm{d}x = \frac{x^{3}}{3}\arcsin \frac{x}{a} +\frac{1}{9} (x^{2} + 2a^{2})\sqrt{a^{2} - x^{2}} +C.$ 

116. $\int \arccos \frac{x}{a} \mathrm{d}x = x \arccos \frac{x}{a} - \sqrt{a^2 - x^2} + C.$ 

117. $\int x\arccos \frac{x}{a}\mathrm{d}x = \left(\frac{x^2}{2} -\frac{a^2}{4}\right)\arccos \frac{x}{a} -\frac{x}{4}\sqrt{a^2 - x^2} +C.$ 

118. $\int x^{2}\arccos \frac{x}{a}\mathrm{d}x = \frac{x^{3}}{3}\arccos \frac{x}{a} -\frac{1}{9} (x^{2} + 2a^{2})\sqrt{a^{2} - x^{2}} +C.$ 

119. $\int \arctan \frac{x}{a} \mathrm{d}x = x \arctan \frac{x}{a} - \frac{a}{2} \ln (a^2 + x^2) + C.$ 

120. $\int x\arctan \frac{x}{a}\mathrm{d}x = \frac{1}{2} (a^2 +x^2)\arctan \frac{x}{a} -\frac{a}{2} x + C.$ 

121. $\int x^{2}\arctan \frac{x}{a}\mathrm{d}x = \frac{x^{3}}{3}\arctan \frac{x}{a} -\frac{a}{6} x^{2} + \frac{a^{3}}{6}\ln (a^{2} + x^{2}) + C.$ 

# (十三) 含有指数函数的积分

122. $\int a^{x}\mathrm{d}x = \frac{1}{\ln a} a^{x} + C.$ 

123. $\int \mathrm{e}^{ax}\mathrm{d}x = \frac{1}{a}\mathrm{e}^{ax} + C.$ 

124. $\int x\mathrm{e}^{ax}\mathrm{d}x = \frac{1}{a^2} (ax - 1)\mathrm{e}^{ax} + C.$ 

125. $\int x^{n}\mathrm{e}^{ax}\mathrm{d}x = \frac{1}{a} x^{n}\mathrm{e}^{ax} - \frac{n}{a}\int x^{n - 1}\mathrm{e}^{ax}\mathrm{d}x.$ 

126. $\int xa^{x}\mathrm{d}x = \frac{x}{\ln a} a^{x} - \frac{1}{(\ln a)^{2}} a^{x} + C.$ 

127. $\int x^{n}a^{x}\mathrm{d}x = \frac{1}{\ln a} x^{n}a^{x} - \frac{n}{\ln a}\int x^{n - 1}a^{x}\mathrm{d}x.$ 

128. $\int \mathrm{e}^{ax}\sin bx\mathrm{d}x = \frac{1}{a^2 + b^2}\mathrm{e}^{ax}(a\sin bx - b\cos bx) + C.$ 

129. $\int \mathrm{e}^{ax}\cos bx\mathrm{d}x = \frac{1}{a^2 + b^2}\mathrm{e}^{ax}(b\sin bx + a\cos bx) + C.$ 

130. $\int \mathrm{e}^{ax}\sin^n bx\mathrm{d}x = \frac{1}{a^2 + b^2n^2}\mathrm{e}^{ax}\sin^{n - 1}bx(a\sin bx - nb\cos bx) + \frac{n(n - 1)b^2}{a^2 + b^2n^2}\int \mathrm{e}^{ax}\sin^{n - 2}bx\mathrm{d}x.$ 

131. $\int \mathrm{e}^{ax}\cos^n bx\mathrm{d}x = \frac{1}{a^2 + b^2n^2}\mathrm{e}^{ax}\cos^{n - 1}bx(a\cos bx + nb\sin bx) + \frac{n(n - 1)b^2}{a^2 + b^2n^2}\int \mathrm{e}^{ax}\cos^{n - 2}bx\mathrm{d}x.$ 

# (十四) 含有对数函数的积分

132. $\int \ln x\mathrm{d}x = x\ln x - x + C.$ 

133. $\int \frac{\mathrm{d}x}{x\ln x} = \ln |\ln x| + C.$ 

134. $\int x^n\ln x\mathrm{d}x = \frac{1}{n + 1} x^{n + 1}\left(\ln x - \frac{1}{n + 1}\right) + C.$ 

135. $\int (\ln x)^n\mathrm{d}x = x(\ln x)^n -n\int (\ln x)^{n - 1}\mathrm{d}x.$ 

136. $\int x^{m}(\ln x)^{n}\mathrm{d}x = \frac{1}{m + 1} x^{m + 1}(\ln x)^{n} - \frac{n}{m + 1}\int x^{m}(\ln x)^{n - 1}\mathrm{d}x.$ 

# (十五) 含有双曲函数的积分

137. $\int \operatorname{sh} x \, \mathrm{d}x = \operatorname{ch} x + C$ . 

138. $\int \operatorname{ch} x \, \mathrm{d}x = \operatorname{sh} x + C$ . 

139. $\int \operatorname{th} x \, \mathrm{d}x = \ln \operatorname{ch} x + C$ . 

140. $\int \mathrm{sh}^2 x\mathrm{d}x = -\frac{x}{2} +\frac{1}{4}\mathrm{sh}2x + C.$ 

141. $\int \mathrm{ch}^2 x\mathrm{d}x = \frac{x}{2} +\frac{1}{4}\mathrm{sh}2x + C.$ 

# (十六) 定积分

142. $\int_{-\pi}^{\pi}\cos nx\mathrm{d}x = \int_{-\pi}^{\pi}\sin nx\mathrm{d}x = 0.$ 

143. $\int_{-\pi}^{\pi}\cos mx\sin nx\mathrm{d}x = 0.$ 

144. $\int_{-\pi}^{\pi}\cos mx\cos nx\mathrm{d}x = \left\{ \begin{array}{ll}0, & m\neq n,\\ \pi , & m = n. \end{array} \right.$ 

145. $\int_{-\pi}^{\pi}\sin mx\sin nx\mathrm{d}x = \left\{ \begin{array}{ll}0, & m\neq n,\\ \pi , & m = n. \end{array} \right.$ 

146. $\int_0^\pi \sin mx\sin nx\mathrm{d}x = \int_0^\pi \cos mx\cos nx\mathrm{d}x = \left\{ \begin{array}{ll}0, & m\neq n,\\ \frac{\pi}{2}, & m = n. \end{array} \right.$ 

147. $I_{n} = \int_{0}^{\frac{\pi}{2}}\sin^{n}x\mathrm{d}x = \int_{0}^{\frac{\pi}{2}}\cos^{n}x\mathrm{d}x,$ 

$$
I _ {n} = \frac {n - 1}{n} I _ {n - 2}
$$

$$
= \left\{ \begin{array}{l l} \frac {n - 1}{n} \cdot \frac {n - 3}{n - 2} \cdot \dots \cdot \frac {4}{5} \cdot \frac {2}{3} (n \text {为大于} 1 \text {的正奇数}), I _ {1} = 1, \\ \frac {n - 1}{n} \cdot \frac {n - 3}{n - 2} \cdot \dots \cdot \frac {3}{4} \cdot \frac {1}{2} \cdot \frac {\pi}{2} (n \text {为正偶数}), & I _ {0} = \frac {\pi}{2}. \end{array} \right.
$$

# 部分习题参考答案与提示

# 第一章

# 习题1-1（第15页）

1. (1) $\left[-\frac{2}{3}, +\infty\right)$ ; (2) $(- \infty, -1) \cup (-1, 1) \cup (1, +\infty)$ ; (3) $[-1, 0) \cup (0, 1]$ ; 

(4) $(-2, 2)$ ; (5) $[0, +\infty)$ ; (6) $\mathbb{R} \setminus \left\{\left(k + \frac{1}{2}\right) \pi - 1 \mid k \in \mathbb{Z}\right\}$ ; (7) $[2, 4]$ ; 

(8) $(- \infty, 0) \cup (0, 3]$ ; (9) $(-1, +\infty)$ ; (10) $(- \infty, 0) \cup (0, +\infty)$ . 

2. 略.

3. $\varphi\left(\frac{\pi}{6}\right)=\frac{1}{2},\varphi\left(\frac{\pi}{4}\right)=\frac{\sqrt{2}}{2},\varphi\left(-\frac{\pi}{4}\right)=\frac{\sqrt{2}}{2},\varphi(-2)=0,$ 图略.

4. (1)、(2) $f(x)$ 均在 R 上有界.

5. 略.

6.（1）当 $a > 0$ 时， $f(x)$ 在 $\left(-\infty, -\frac{b}{2a}\right)$ 内单调减少，在 $\left(-\frac{b}{2a}, +\infty\right)$ 内单调增加；

当 $a < 0$ 时， $f(x)$ 在 $\left(-\infty, -\frac{b}{2a}\right)$ 内单调增加，在 $\left(-\frac{b}{2a}, +\infty\right)$ 内单调减少；

(2) 当 $b > \frac{ad}{c}$ 时, $f(x)$ 分别在 $\left(-\infty, -\frac{d}{c}\right)$ 及 $\left(-\frac{d}{c}, +\infty\right)$ 内单调减少;

当 $b < \frac{ad}{c}$ 时， $f(x)$ 分别在 $\left(-\infty, -\frac{d}{c}\right)$ 及 $\left(-\frac{d}{c}, +\infty\right)$ 内单调增加；

当 $b=\frac{ad}{c}$ 时， $f(x)=\frac{a}{c}$ ，无单调性.

7—8. 略.

9.（1）偶函数；（2）既非奇函数又非偶函数；（3）偶函数；

(4) 奇函数; (5) 既非奇函数又非偶函数; (6) 偶函数.

10.（1）是周期函数，周期 $l=2\pi$ ；（2）是周期函数，周期 $l=\frac{\pi}{2}$ ;

(3) 是周期函数, 周期 l=2; (4) 不是周期函数;

(5) 是周期函数, 周期 $l = \pi$ .

11. (1) $y = x^3 - 1$ ; (2) $y = \frac{1 - x}{1 + x}$ ; (3) $y = \frac{-dx + b}{cx - a}$ ; 

(4) $y = \frac{1}{3}\arcsin \frac{x}{2}; \quad (5)y = e^{x - 1} - 2;\quad (6)y = \log_{2}\frac{x}{1 - x}.$ 

12. (1) $y = \sin^2 x, y_1 = \frac{1}{4}, y_2 = \frac{3}{4};$ 

(2) $y = \sin 2x, y_1 = \frac{\sqrt{2}}{2}, y_2 = 1;$ 

(3) $y = \sqrt{1 + x^2}, y_1 = \sqrt{2}, y_2 = \sqrt{5};$ 

(4) $y = e^{x^2}, y_1 = 1, y_2 = e;$ 

(5) $y = e^{2x}, y_1 = e^2, y_2 = e^{-2}.$ 

13. (1) $[-1, 1]$ ; (2) $\bigcup_{n \in \mathbb{Z}} [2n\pi, (2n + 1)\pi]$ ; (3) $[-a, 1 - a]$ ; 

(4) 若 $a \in \left(0, \frac{1}{2}\right]$ ，则 $D = [a, 1 - a]$ ；若 $a > \frac{1}{2}$ ，则 $D = \varnothing$ .

14. $f[g(x)] = \left\{ \begin{array}{ll}1, & x <   0,\\ 0, & x = 0,\\ -1, & x > 0; \end{array} \right.$ $g[f(x)] = \left\{ \begin{array}{ll}\mathrm{e}, & |x| <   1,\\ 1, & |x| = 1,\text{图略}.\\ \mathrm{e}^{-1}, & |x| > 1, \end{array} \right.$ 

15. $L = \frac{S_0}{h} +\frac{2 - \cos 40^\circ}{\sin 40^\circ} h,h\in (0,\sqrt{S_0\tan 40^\circ}).$ 

16. $S(t) = \left\{ \begin{array}{ll}\frac{1}{2} t^2, & 0\leqslant t\leqslant 1,\\ -\frac{1}{2} t^2 +2t - 1, & 1 <   t\leqslant 2,\\ 1, & t > 2. \end{array} \right.$ 

17. $F = 1.8C + 32$ 或 $C = \frac{5}{9} (F - 32)$ 