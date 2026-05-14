是向量 b 与 a 的差 b-a（图 8-7(b)）.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a6c0e6f8da26f04b3d420b24c7865d11e6935473fa14e454360911230eeb92f4.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/852d0d1cbceaad97cfc91c0cab73aec54460751944e6d96620177645d69051dc.jpg)



(b)



图8-7


由三角形两边之和大于第三边,有

$$
\mid a + b \mid \leqslant \mid a \mid + \mid b \mid \quad \text {及} \quad \mid a - b \mid \leqslant \mid a \mid + \mid b \mid ,
$$

其中等号在 a 与 b 同向或反向时成立.

# 2. 向量与数的乘法

向量 a 与实数 $\lambda$ 的乘积记作 $\lambda a$ ，规定 $\lambda a$ 是一个向量，它的模

$$
\mid \lambda a \mid = \mid \lambda \mid \mid a \mid ,
$$

它的方向当 $\lambda > 0$ 时与 $a$ 相同, 当 $\lambda < 0$ 时与 $a$ 相反.

当 $\lambda=0$ 时， $|\lambda a|=0$ ，即 $\lambda a$ 为零向量，这时它的方向可以是任意的。

特别地, 当 $\lambda = \pm 1$ 时, 有

$$
1 a = a, \quad (- 1) a = - a.
$$

向量与数的乘积符合下列运算规律：

(1) 结合律 $\lambda(\mu a)=\mu(\lambda a)=(\lambda\mu)a.$ 

这是因为由向量与数的乘积的规定可知, 向量 $\lambda(\mu a)$ , $\mu(\lambda a)$ , $(\lambda\mu)a$ 都是平行的向量, 它们的方向也是相同的, 而且

$$
\left| \lambda (\mu a) \right| = \left| \mu (\lambda a) \right| = \left| (\lambda \mu) a \right| = \left| \lambda \mu \right| | a |,
$$

所以

$$
\lambda (\mu a) = \mu (\lambda a) = (\lambda \mu) a.
$$

(2) 分配律

$$
(\lambda + \mu) a = \lambda a + \mu a, \tag {1-1}
$$

$$
\lambda (\boldsymbol {a} + \boldsymbol {b}) = \lambda \boldsymbol {a} + \lambda \boldsymbol {b}. \tag {1-2}
$$

这个规律同样可以按向量与数的乘积的规定来证明,这里从略了.

向量相加及数乘向量统称为向量的线性运算.

例 1 在平行四边形 ABCD 中, 设 $\overrightarrow{AB} = a, \overrightarrow{AD} = b$ . 试用 a 和 b 表示向量 $\overrightarrow{MA}, \overrightarrow{MB}, \overrightarrow{MC}$ 和 $\overrightarrow{MD}$ , 这里 M 是平行四边形对角线的交点(图 8-8).

解 由于平行四边形的对角线互相平分,所以

$$
\boldsymbol {a} + \boldsymbol {b} = \overrightarrow {A C} = 2 \overrightarrow {A M},
$$

即

$$
- (\boldsymbol {a} + \boldsymbol {b}) = 2 \overrightarrow {M A},
$$

于是

$$
\overrightarrow {M A} = - \frac {1}{2} (a + b).
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/db3e8abcc6be42844ee665d9342c4aa455301c26a02e94926b898f89227465b0.jpg)



图8-8


因为 $\overrightarrow{MC}=-\overrightarrow{MA}$ ，所以 $\overrightarrow{MC}=\frac{1}{2}(a+b)$ .

又因 $-a + b = \overrightarrow{BD} = 2\overrightarrow{MD}$ 所以 $\overrightarrow{MD} = \frac{1}{2} (b - a)$ 

由于 $\overrightarrow{MB}=-\overrightarrow{MD}$ ，所以 $\overrightarrow{MB}=\frac{1}{2}(a-b)$ .

前面已经讲过,模等于1的向量叫做单位向量.设 $e_{a}$ 表示与非零向量a同方向的单位向量,那么按照向量与数的乘积的规定,由于 $|a|>0$ ,所以 $|a|e_{a}$ 与 $e_{a}$ 的方向相同,即 $|a|e_{a}$ 与a的方向相同.又因 $|a|e_{a}$ 的模是

$$
\mid a \mid \mid e _ {a} \mid = \mid a \mid \cdot 1 = \mid a \mid ,
$$

即 $|a|e_a$ 与 $\pmb{a}$ 的模也相同，因此，

$$
a = | a | e _ {a}.
$$

我们规定, 当 $\lambda \neq 0$ 时, $\frac{a}{\lambda} = \frac{1}{\lambda} a$ . 由此, 上式又可写成

$$
\frac {a}{| a |} = e _ {a}.
$$

这表示一个非零向量除以它的模的结果是一个与原向量同方向的单位向量.

由于向量 $\lambda a$ 与 a 平行, 因此我们常用向量与数的乘积来说明两个向量的平行关系. 即有

定理 1 设向量 $a \neq 0$ ，则向量 b 平行于 a 的充分必要条件是：存在唯一的实数 $\lambda$ ，使 $b = \lambda a$ .

证 条件的充分性是显然的,下面证明条件的必要性.

设 $b \parallel a$ . 取 $|\lambda| = \frac{|b|}{|a|}$ , 当 $b$ 与 $a$ 同向时 $\lambda$ 取正值, 当 $b$ 与 $a$ 反向时 $\lambda$ 取负值, 即有 $b = \lambda a$ . 这是因为此时 $b$ 与 $\lambda a$ 同向, 且

$$
\mid \lambda a \mid = \mid \lambda \mid \mid a \mid = \frac {\mid b \mid}{\mid a \mid} \mid a \mid = \mid b \mid .
$$

再证数 $\lambda$ 的唯一性. 设 $b = \lambda a$ , 又设 $b = \mu a$ , 两式相减, 便得

$$
(\lambda - \mu) a = 0,
$$

即 $|\lambda - \mu||a| = 0$ . 因 $|a| \neq 0$ , 故 $|\lambda - \mu| = 0$ , 即 $\lambda = \mu$ .

定理证毕.

定理 1 是建立数轴的理论依据. 我们知道, 给定一个点、一个方向及单位长度, 就确定了一条数轴. 由于一个单位向量既确定了方向, 又确定了单位长度, 因此, 给定一个点及一个单位向量就确定了一条数轴. 设点 O 及单位向量 i 确定了数轴 Ox (图8-9), 对于轴上任一点 $P$ , 对应一个向量 $\overrightarrow{OP}$ , 由于 $\overrightarrow{OP} // i$ , 根据定理 1, 必有唯一的实数 $x$ , 使 $\overrightarrow{OP} = xi$ (实数 $x$ 叫做轴上有向线段 $\overrightarrow{OP}$ 的值), 并知 $\overrightarrow{OP}$ 与实数 $x$ 一一对应. 于是

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/48e48170f26fc2c5df99c0b980997e40d166041d8bda5990d2bf5e3f29c29336.jpg)



图8-9


点 $P \longleftrightarrow$ 向量 $\overrightarrow{OP} = xi \longleftrightarrow$ 实数 $x$ ,

从而轴上的点 $P$ 与实数 $x$ 有一一对应的关系. 据此, 定义实数 $x$ 为轴上点 $P$ 的坐标.

由此可知,轴上点 P 的坐标为 x 的充分必要条件是

$$
\overrightarrow {O P} = x i.
$$

# 三、空间直角坐标系

在空间取定一点 O 和三个两两垂直的单位向量 i, j, k，就确定了三条都以 O 为原点的两两垂直的数轴，依次记为 x 轴（横轴）、y 轴（纵轴）、z 轴（竖轴），统称坐标轴。它们构成一个空间直角坐标系，称为 Oxyz 坐标系或 [O; i, j, k] 坐标系（图 8-10）。通常把 x 轴和 y 轴配置在水平面上，而 z 轴则是铅垂线；它们的正向通常符合右手规则，即以右手握住 z 轴，当右手的四个手指从 x 轴正向以 $\frac{\pi}{2}$ 角度转向 y 轴正向时，大拇指的指向就是 z 轴的正向，如图 8-11 所示。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/2391c620a1457452fce2047d734bfdbab481861ef6404e15e75c8b9eb06e4434.jpg)



图8-10


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/d343619182311e23ff85d93ecb0a43723a68a93f8da69ec034aaeb8d411b7f97.jpg)



图8-11


三条坐标轴中的任意两条可以确定一个平面, 这样定出的三个平面统称为坐标面. $x$ 轴及 $y$ 轴所确定的坐标面叫做 $xOy$ 面, 另两个由 $y$ 轴及 $z$ 轴和由 $z$ 轴及 $x$ 轴所确定的坐标面,分别叫做 yOz 面及 zOx 面.三个坐标面把空间分成八个部分,每一部分叫做一个卦限.其中,在 xOy 面上方且 yOz 面前方、zOx 面右方的那个卦限叫做第一卦限,其他第二、第三、第四卦限,在 xOy 面的上方,按逆时针方向确定.第五至第八卦限,在 xOy 面的下方,由第一卦限之下的第五卦限,按逆时针方向确定,这八个卦限分别用字母 I, II, III, IV, V, VI, VII, VIII表示(图 8-12).

任给向量 r，有对应点 M，使 $\overrightarrow{OM}=r$ 。以 OM 为对角线、三条坐标轴为棱作长方体 RHMK-OPNQ，如图 8-13 所示，有

$$
\boldsymbol {r} = \overrightarrow {O M} = \overrightarrow {O P} + \overrightarrow {P N} + \overrightarrow {N M} = \overrightarrow {O P} + \overrightarrow {O Q} + \overrightarrow {O R},
$$

设 $\overrightarrow{OP} = x\mathbf{i},\overrightarrow{OQ} = y\mathbf{j},\overrightarrow{OR} = z\mathbf{k}$ ，则

$$
\boldsymbol {r} = \overrightarrow {O M} = x \boldsymbol {i} + y \boldsymbol {j} + z \boldsymbol {k}.
$$

上式称为向量 r 的坐标分解式, xi, yj 和 zk 称为向量 r 沿三个坐标轴方向的分向量.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/ea44edc4b4db47d161a81e7cfaf3de33780ebfc841e32ced09958a08872f444c.jpg)



图8-12


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/86405ace8df3d0f48076e51a5f4a4fa79dd8083da20b9dfeedb513e9e0ccbf85.jpg)



图8-13


显然,给定向量 r, 就确定了点 M 及 $\overrightarrow{OP}, \overrightarrow{OQ}, \overrightarrow{OR}$ 三个分向量, 进而确定了 x, y, z 三个有序数; 反之, 给定三个有序数 x, y, z, 也就确定了向量 r 与点 M. 于是点 M、向量 r 与三个有序数 x, y, z 之间有一一对应的关系

$$
M \longleftrightarrow r = \overrightarrow {O M} = x i + y j + z k \longleftrightarrow (x, y, z),
$$

据此,定义:有序数 x,y,z 称为向量 r (在坐标系 Oxyz 中) 的坐标,记作 $r=(x,y,z)$ ;有序数 x,y,z 也称为点 M (在坐标系 Oxyz 中) 的坐标,记作 $M(x,y,z)$ .

向量 $r=\overrightarrow{OM}$ 称为点 M 关于原点 O 的向径. 上述定义表明, 一个点与该点的向径有相同的坐标. 记号 $(x,y,z)$ 既表示点 M, 又表示向量 $\overrightarrow{OM}$ .

坐标面上和坐标轴上的点, 其坐标各有一定的特征. 例如: 如果点 $M$ 在 $yOz$ 面上, 那么 $x = 0$ ; 同样, 在 $zOx$ 面上的点, 有 $y = 0$ ; 在 $xOy$ 面上的点, 有 $z = 0$ . 如果点 $M$ 在 $x$ 轴上, 那么 $y = z = 0$ ; 同样, 在 $y$ 轴上的点, 有 $z = x = 0$ ; 在 $z$ 轴上的点, 有 $x = y = 0$ . 若点 $M$ 为

原点,则 x=y=z=0.

# 四、利用坐标作向量的线性运算

利用向量的坐标,可得向量的加法、减法以及向量与数的乘法的运算如下:

设 $a = (a_{x}, a_{y}, a_{z})$ ， $b = (b_{x}, b_{y}, b_{z})$ ，即

$$
\boldsymbol {a} = a _ {x} \boldsymbol {i} + a _ {y} \boldsymbol {j} + a _ {z} \boldsymbol {k}, \quad \boldsymbol {b} = b _ {x} \boldsymbol {i} + b _ {y} \boldsymbol {j} + b _ {z} \boldsymbol {k}.
$$

利用向量加法的交换律与结合律以及向量与数的乘法的结合律与分配律,有

$$
\boldsymbol {a} + \boldsymbol {b} = (a _ {x} + b _ {x}) \boldsymbol {i} + (a _ {y} + b _ {y}) \boldsymbol {j} + (a _ {z} + b _ {z}) \boldsymbol {k},
$$

$$
\boldsymbol {a} - \boldsymbol {b} = (a _ {x} - b _ {x}) \boldsymbol {i} + (a _ {y} - b _ {y}) \boldsymbol {j} + (a _ {z} - b _ {z}) \boldsymbol {k},
$$

$$
\lambda a = (\lambda a _ {x}) i + (\lambda a _ {y}) j + (\lambda a _ {z}) k \quad (\lambda \text {为实数}),
$$

即

$$
\boldsymbol {a} + \boldsymbol {b} = \left(a _ {x} + b _ {x}, a _ {y} + b _ {y}, a _ {z} + b _ {z}\right),
$$

$$
\boldsymbol {a} - \boldsymbol {b} = \left(a _ {x} - b _ {x}, a _ {y} - b _ {y}, a _ {z} - b _ {z}\right),
$$

$$
\lambda a = \left(\lambda a _ {x}, \lambda a _ {y}, \lambda a _ {z}\right).
$$

由此可见,对向量进行加、减及与数相乘,只需对向量的各个坐标分别进行相应的数量运算就行了.

定理 1 指出, 当向量 $a \neq 0$ 时, 向量 $b \parallel a$ 相当于 $b = \lambda a$ , 坐标表示式为

$$
\left(b _ {x}, b _ {y}, b _ {z}\right) = \lambda \left(a _ {x}, a _ {y}, a _ {z}\right),
$$

这也就相当于向量 b 与 a 对应的坐标成比例

$$
\frac {b _ {x}}{a _ {x}} = \frac {b _ {y}}{a _ {y}} = \frac {b _ {z}}{a _ {z}}. \tag {1-3}
$$

例 2 求解以向量为元的线性方程组

$$
\left\{ \begin{array}{l} 5 x - 3 y = a, \\ 3 x - 2 y = b, \end{array} \right.
$$

其中 $\boldsymbol{a}=(2,1,2)$ , $\boldsymbol{b}=(-1,1,-2)$ .

解 如同解以实数为元的线性方程组一样,可解得

$$
x = 2 a - 3 b, y = 3 a - 5 b.
$$

① 当 $a_{x}, a_{y}, a_{z}$ 有一个为零时，例如 $a_{x} = 0, a_{y}, a_{z} \neq 0$ ，这时(1-3)式应理解为

$$
\left\{ \begin{array}{l} b _ {x} = 0, \\ \frac {b _ {y}}{a _ {y}} = \frac {b _ {z}}{a _ {z}}; \end{array} \right.
$$

当 $a_{x}, a_{y}, a_{z}$ 有两个为零时，例如 $a_{x} = a_{y} = 0, a_{z} \neq 0$ ，这时(1-3)式应理解为

$$
\left\{ \begin{array}{l} b _ {x} = 0, \\ b _ {y} = 0. \end{array} \right.
$$

将 a, b 的坐标表示式代入, 即得

$$
x = 2 (2, 1, 2) - 3 (- 1, 1, - 2) = (7, - 1, 1 0),
$$

$$
y = 3 (2, 1, 2) - 5 (- 1, 1, - 2) = (1 1, - 2, 1 6).
$$

例3 已知两点 $A(x_{1},y_{1},z_{1})$ 和 $B(x_{2},y_{2},z_{2})$ 以及实数 $\lambda \neq -1$ ，在直线 $AB$ 上求点 $M$ ，使

$$
\overrightarrow {A M} = \lambda \overrightarrow {M B}.
$$

解 如图 8-14 所示. 由于

$$
\overrightarrow {A M} = \overrightarrow {O M} - \overrightarrow {O A}, \overrightarrow {M B} = \overrightarrow {O B} - \overrightarrow {O M},
$$

因此

$$
\overrightarrow {O M} - \overrightarrow {O A} = \lambda (\overrightarrow {O B} - \overrightarrow {O M}),
$$

从而

$$
\overrightarrow {O M} = \frac {1}{1 + \lambda} (\overrightarrow {O A} + \lambda \overrightarrow {O B}).
$$

将 $\overrightarrow{OA},\overrightarrow{OB}$ 的坐标（即点 $A$ 、点 $B$ 的坐标）代入，即得

$$
\overrightarrow {O M} = \left(\frac {x _ {1} + \lambda x _ {2}}{1 + \lambda}, \frac {y _ {1} + \lambda y _ {2}}{1 + \lambda}, \frac {z _ {1} + \lambda z _ {2}}{1 + \lambda}\right),
$$

这就是点 M 的坐标.

本例中的点 $M$ 叫做有向线段 $\overrightarrow{AB}$ 的 $\lambda$ 分点. 特别地, 当 $\lambda = 1$ 时, 得线段 $AB$ 的中点为

$$
M \left(\frac {x _ {1} + x _ {2}}{2}, \frac {y _ {1} + y _ {2}}{2}, \frac {z _ {1} + z _ {2}}{2}\right).
$$

通过本例,我们应注意以下两点:(1)由于点M与向量 $\overrightarrow{OM}$ 有相同的坐标,因此,求点M的坐标,就是求 $\overrightarrow{OM}$ 的坐标.(2)记号 $(x,y,z)$ 既可表示点M,又可表示向量 $\overrightarrow{OM}$ ,在几何中点与向量是两个不同的概念,不可混淆.因此,在看到记号 $(x,y,z)$ 时,须从上下文去认清它究竟表示点还是表示向量.当 $(x,y,z)$ 表示向量时,可对它进行运算;当 $(x,y,z)$ 表示点时,就不能进行运算.

# 五、向量的模、方向角、投影

# 1. 向量的模与两点间的距离公式

设向量 $r = (x,y,z)$ ，作 $\overrightarrow{OM} = r$ ，如图8-13所示，有

$$
r = \overrightarrow {O M} = \overrightarrow {O P} + \overrightarrow {O Q} + \overrightarrow {O R},
$$

按勾股定理可得

$$
| r | = | O M | = \sqrt {| O P | ^ {2} + | O Q | ^ {2} + | O R | ^ {2}}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/31d2767cad9d3ad8bdfd0415f323db43dc8471e3cac47fe88534d4636968d160.jpg)



图8-14


由 $\overrightarrow{OP} = xi, \overrightarrow{OQ} = yj, \overrightarrow{OR} = zk$ ，有

$$
\mid O P \mid = \mid x \mid , \quad \mid O Q \mid = \mid y \mid , \quad \mid O R \mid = \mid z \mid ,
$$

于是得向量模的坐标表示式

$$
| \boldsymbol {r} | = \sqrt {x ^ {2} + y ^ {2} + z ^ {2}}.
$$

设有点 $A(x_{1},y_{1},z_{1})$ 和点 $B(x_{2},y_{2},z_{2})$ ，则点 $A$ 与点 $B$ 间的距离 $|AB|$ 就是向量 $\overrightarrow{AB}$ 的模.由

$$
\overrightarrow {A B} = \overrightarrow {O B} - \overrightarrow {O A} = (x _ {2}, y _ {2}, z _ {2}) - (x _ {1}, y _ {1}, z _ {1}) = (x _ {2} - x _ {1}, y _ {2} - y _ {1}, z _ {2} - z _ {1}),
$$

即得 A, B 两点间的距离

$$
\mid A B \mid = \mid \overrightarrow {A B} \mid = \sqrt {\left(x _ {2} - x _ {1}\right) ^ {2} + \left(y _ {2} - y _ {1}\right) ^ {2} + \left(z _ {2} - z _ {1}\right) ^ {2}}.
$$

例4 求证以 $M_{1}(4,3,1), M_{2}(7,1,2), M_{3}(5,2,3)$ 三点为顶点的三角形是一个等腰三角形.

解 因为

$$
\begin{array}{l} \mid M _ {1} M _ {2} \mid^ {2} = (7 - 4) ^ {2} + (1 - 3) ^ {2} + (2 - 1) ^ {2} = 1 4, \\ \mid M _ {2} M _ {3} \mid^ {2} = (5 - 7) ^ {2} + (2 - 1) ^ {2} + (3 - 2) ^ {2} = 6, \\ \mid M _ {3} M _ {1} \mid^ {2} = (4 - 5) ^ {2} + (3 - 2) ^ {2} + (1 - 3) ^ {2} = 6, \\ \end{array}
$$

所以 $\left|M_{2}M_{3}\right|=\left|M_{3}M_{1}\right|$ ，即 $\triangle M_{1}M_{2}M_{3}$ 为等腰三角形.

例 5 在 z 轴上求与两点 A(-4,1,7) 和 B(3,5,-2) 等距离的点.

解 因为所求的点 M 在 z 轴上, 所以设该点为 $M(0,0,z)$ , 依题意有

$$
\mid M A \mid = \mid M B \mid ,
$$

即

$$
\sqrt {(0 + 4) ^ {2} + (0 - 1) ^ {2} + (z - 7) ^ {2}} = \sqrt {(3 - 0) ^ {2} + (5 - 0) ^ {2} + (- 2 - z) ^ {2}}.
$$

两边平方,解得

$$
z = \frac {1 4}{9},
$$

因此,所求的点为 $M\left(0,0,\frac{14}{9}\right)$ .

例6 已知两点 $A(4,0,5)$ 和 $B(7,1,3)$ ，求与 $\overrightarrow{AB}$ 方向相同的单位向量 $\pmb{e}_{\overrightarrow{AB}}$ 

解 因为

$$
\overrightarrow {A B} = \overrightarrow {O B} - \overrightarrow {O A} = (7, 1, 3) - (4, 0, 5) = (3, 1, - 2),
$$

所以

$$
\mid \overrightarrow {A B} \mid = \sqrt {3 ^ {2} + 1 ^ {2} + (- 2) ^ {2}} = \sqrt {1 4},
$$

于是

$$
e _ {\overrightarrow {A B}} = \frac {\overrightarrow {A B}}{| \overrightarrow {A B} |} = \frac {1}{\sqrt {1 4}} (3, 1, - 2).
$$

# 2. 方向角与方向余弦

非零向量 r 与三条坐标轴的夹角 $\alpha, \beta, \gamma$ 称为向量 r 的方向角. 从图 8-15 可见, 设 $\overrightarrow{OM} = r = (x, y, z)$ , 由于 x 是有向线段 $\overrightarrow{OP}$ 的值, $MP \perp OP$ , 故 $\lambda^{z}$ 

$$
\cos \alpha = \frac {x}{| O M |} = \frac {x}{| r |},
$$

类似可知

$$
\cos \beta = \frac {y}{| r |}, \quad \cos \gamma = \frac {z}{| r |}.
$$

从而

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/ef26179559996b01c6982a79d1490cfdc1a46a466ba45cd8b4166f10b20f7897.jpg)



图8-15


$$
(\cos \alpha , \cos \beta , \cos \gamma) = \left(\frac {x}{| r |}, \frac {y}{| r |}, \frac {z}{| r |}\right) = \frac {1}{| r |} (x, y, z) = \frac {r}{| r |} = e _ {r}.
$$

$\cos \alpha, \cos \beta, \cos \gamma$ 称为向量 $r$ 的方向余弦. 上式表明, 以向量 $r$ 的方向余弦为坐标的向量就是与 $r$ 同方向的单位向量 $e_r$ . 并由此可得

$$
\cos^ {2} \alpha + \cos^ {2} \beta + \cos^ {2} \gamma = 1.
$$

例 7 已知两点 $M_{1}(2,2,\sqrt{2})$ 和 $M_{2}(1,3,0)$ ，计算向量 $\overrightarrow{M_{1}M_{2}}$ 的模、方向余弦和方向角.

解 $\overrightarrow{M_1M_2} = (1 - 2,3 - 2,0 - \sqrt{2}) = (-1,1, - \sqrt{2})$ 

$$
\mid \overrightarrow {M _ {1} M _ {2}} \mid = \sqrt {(- 1) ^ {2} + 1 ^ {2} + (- \sqrt {2}) ^ {2}} = \sqrt {1 + 1 + 2} = \sqrt {4} = 2;
$$

$$
\cos \alpha = - \frac {1}{2}, \quad \cos \beta = \frac {1}{2}, \quad \cos \gamma = - \frac {\sqrt {2}}{2};
$$

$$
\alpha = \frac {2 \pi}{3}, \quad \beta = \frac {\pi}{3}, \quad \gamma = \frac {3 \pi}{4}.
$$

例8 设点 $A$ 位于第 I 卦限, 向径 $\overrightarrow{OA}$ 与 $x$ 轴、 $y$ 轴的夹角依次为 $\frac{\pi}{3}$ 和 $\frac{\pi}{4}$ , 且 $|\overrightarrow{OA}| = 6$ , 求点 $A$ 的坐标.

解 $\alpha = \frac{\pi}{3},\beta = \frac{\pi}{4}$ 由关系式 $\cos^2\alpha +\cos^2\beta +\cos^2\gamma = 1$ ，得

$$
\cos^ {2} \gamma = 1 - \left(\frac {1}{2}\right) ^ {2} - \left(\frac {\sqrt {2}}{2}\right) ^ {2} = \frac {1}{4},
$$

因点 A 在第 I 卦限, 知 $\cos \gamma > 0$ , 故

$$
\cos \gamma = \frac {1}{2}.
$$

于是

$$
\overrightarrow {O A} = | \overrightarrow {O A} | e _ {\overrightarrow {O A}} = 6 \left(\frac {1}{2}, \frac {\sqrt {2}}{2}, \frac {1}{2}\right) = (3, 3 \sqrt {2}, 3),
$$

这就是点 A 的坐标.

# 3. 向量在轴上的投影

如果撇开 $y$ 轴和 $z$ 轴, 单独考虑 $x$ 轴与向量 $\pmb{r} = \overrightarrow{OM}$ 的关系, 那么从图8-15可见, 过点 $M$ 作与 $x$ 轴垂直的平面, 此平面与 $x$ 轴的交点即是点 $P$ . 作出点 $P$ , 即得向量 $\pmb{r}$ 在 $x$ 轴上的分向量 $\overrightarrow{OP}$ ，进而由 $\overrightarrow{OP} = xi$ ，便得向量在 $x$ 轴上的坐标 $x$ ，且 $x = |r|\cos \alpha .$ 

一般地, 设点 O 及单位向量 e 确定 u 轴(图 8-16). 任给向量 r, 作 $\overrightarrow{OM}=r$ , 再过点 M 作与 u 轴垂直的平面交 u 轴于点 $M'$ (点 $M'$ 叫做点 M 在 u 轴上的投影), 则向量 $\overrightarrow{OM'}$ 称为向量 r 在 u 轴上的分向量. 设 $\overrightarrow{OM'}=\lambda e$ , 则数 $\lambda$ 称为向量 r 在 u 轴上的投影, 记作 $\operatorname{Prj}_{u} r$ 或 $(r)_{u}$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/dd5a5e0d5c98f702c5a29740b633b329b4f39e14ca3d18240b940aeeb47ca1d3.jpg)



图8-16


按此定义,向量 a 在直角坐标系 Oxyz 中的坐标 $a_{x}, a_{y}, a_{z}$ 就是 a 在三条坐标轴上的投影, 即

$$
a _ {x} = \operatorname{Prj} _ {x} a, \quad a _ {y} = \operatorname{Prj} _ {y} a, \quad a _ {z} = \operatorname{Prj} _ {z} a,
$$

或记作

$$
a _ {x} = (\boldsymbol {a}) _ {x}, \quad a _ {y} = (\boldsymbol {a}) _ {y}, \quad a _ {z} = (\boldsymbol {a}) _ {z}.
$$

由此可知,向量的投影具有与坐标相同的性质:

性质1 $\operatorname{Prj}_u\boldsymbol {a} = |\boldsymbol {a}|\cos \varphi$ （即 $(\pmb {a})_u = |\pmb {a}|\cos \varphi)$ ，其中 $\varphi$ 为向量 $\pmb{a}$ 与 $u$ 轴的夹角；

性质2 $\operatorname{Prj}_u(a + b) = \operatorname{Prj}_u a + \operatorname{Prj}_u b$ （即 $(a + b)_u = (a)_{u} + (b)_{u}$ ）；

性质3 $\operatorname{Prj}_u(\lambda a) = \lambda \operatorname{Prj}_u a$ （即 $(\lambda a)_u = \lambda(a)_u$ ）.

例9 设正方体的一条对角线为 $OM$ ，一条棱为 $OA$ ，且 $|OA|=a$ ，求 $\overrightarrow{OA}$ 在 $\overrightarrow{OM}$ 方向上的投影 $\operatorname{Prj}_{\overrightarrow{OM}}\overrightarrow{OA}$ .①

解 如图 8-17 所示, 记 $\angle MOA = \varphi$ , 有

$$
\cos \varphi = \frac {| O A |}{| O M |} = \frac {1}{\sqrt {3}},
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/1c39f14881255ca916bec1a19e330ce635ed0107f38d4025b7665d972229fd70.jpg)



图8-17


于是

$$
\operatorname{Prj} _ {\overrightarrow {O M}} \overrightarrow {O A} = | \overrightarrow {O A} | \cos \varphi = \frac {a}{\sqrt {3}}.
$$

# 习题8-1

1. 设 $u = a - b + {2c},v =  - a + {3b} - c$ . 试用 $a,b,c$ 表示 ${2u} - {3v}$ 

2. 如果平面上一个四边形的对角线互相平分,试用向量证明它是平行四边形.

3. 把 $\triangle ABC$ 的 $BC$ 边五等分, 设分点依次为 $D_{1}, D_{2}, D_{3}, D_{4}$ , 再把各分点与点 $A$ 连接. 试以 $\overrightarrow{AB} = c$ , $\overrightarrow{BC} = a$ 表示向量 $\overrightarrow{D_1A}, \overrightarrow{D_2A}, \overrightarrow{D_3A}$ 和 $\overrightarrow{D_4A}$ .

4. 已知两点 $M_{1}(0,1,2)$ 和 $M_{2}(1,-1,0)$ . 试用坐标表示式表示向量 $\overrightarrow{M_{1}M_{2}}$ 及 $-2\overrightarrow{M_{1}M_{2}}$ .

5. 求平行于向量 $a=(6,7,-6)$ 的单位向量.

6. 在空间直角坐标系中, 指出下列各点在哪个卦限?

$$
A (1, - 2, 3), \quad B (2, 3, - 4), \quad C (2, - 3, - 4), \quad D (- 2, - 3, 1).
$$

7. 在坐标面上和在坐标轴上的点的坐标各有什么特征？指出下列各点的位置：

$$
A (3, 4, 0), \quad B (0, 4, 3), \quad C (3, 0, 0), \quad D (0, - 1, 0).
$$

8. 求点 $(a,b,c)$ 关于(1)各坐标面:(2)各坐标轴:(3)坐标原点的对称点的坐标.

9. 自点 $P_{0}(x_{0}, \gamma_{0}, z_{0})$ 分别作各坐标面和各坐标轴的垂线，写出各垂足的坐标.

10. 过点 $P_{0}(x_{0}, y_{0}, z_{0})$ 分别作平行于 z 轴的直线和平行于 xOy 面的平面, 问在它们上面的点的坐标各有什么特点?

11. 一棱长为 a 的立方体放置在 xOy 面上, 其底面的中心在坐标原点, 底面的顶点在 x 轴和 y 轴上, 求它各顶点的坐标.

12. 求点 M(4, -3, 5) 到各坐标轴的距离.

13. 在 $\gamma Oz$ 面上, 求与三点 $A(3,1,2), B(4,-2,-2)$ 和 $C(0,5,1)$ 等距离的点.

14. 试证明以 $A(4,1,9), B(10,-1,6), C(2,4,3)$ 三点为顶点的三角形是等腰直角三角形.

15. 设已知两点 $M_{1}(4, \sqrt{2}, 1)$ 和 $M_{2}(3, 0, 2)$ , 计算向量 $\overrightarrow{M_{1} M_{2}}$ 的模、方向余弦和方向角.

16. 设向量的方向余弦分别满足(1) $\cos \alpha = 0$ ; (2) $\cos \beta = 1$ ; (3) $\cos \alpha = \cos \beta = 0$ , 问这些向量与坐标轴或坐标面的关系如何?

17. 设向量 r 的模是 4, 它与 u 轴的夹角是 $\frac{\pi}{3}$ , 求 r 在 u 轴上的投影.

18. 一向量的终点在点 $B(2, -1, 7)$ , 它在 $x$ 轴、 $y$ 轴和 $z$ 轴上的投影依次为 $4, -4$ 和 $7$ . 求这向量的起点 $A$ 的坐标.

19. 设 $m=3i+5j+8k$ , $n=2i-4j-7k$ 和 $p=5i+j-4k$ , 求向量 $a=4m+3n-p$ 在 x 轴上的投影及在 y 轴上的分向量.

20. 设 O 是 A, B 的连线以外的一点, 证明 A, B, C 三点共线的充分必要条件是 $\overrightarrow{OC} = \lambda \overrightarrow{OA} + \mu \overrightarrow{OB}$ , 其中 $\lambda + \mu = 1$ .

# 第二节 数量积 向量积 * 混合积

# 一、两向量的数量积

设一物体在恒力 F 作用下沿直线从点 $M_{1}$ 移动到点 $M_{2}$ ，以 s 表示位移 $\overrightarrow{M_{1}M_{2}}$ 。由物理学知道，力 F 所做的功为

$$
W = | \boldsymbol {F} | | s | \cos \theta ,
$$

其中 $\theta$ 为 F 与 s 的夹角(图 8-18).

从这个问题看出,我们有时要对两个向量 a 和 b 作这样的运算,运算的结果是一个数,它等于 $\left|a\right|$ , $\left|b\right|$ 及它们的夹角 $\theta$ 的余弦的乘积.我们把它叫做向量 a 与 b 的数量积,记作 $a \cdot b$ (图 8-19),即

$$
\boldsymbol {a} \cdot \boldsymbol {b} = | \boldsymbol {a} | | \boldsymbol {b} | \cos \theta .
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/6891faba4c2cf404370180c66ba0c9eede01c94ab93d69b932b1f246257bbb76.jpg)



图8-18


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/4c02757189091ffb8cd3dcff5b91f4fa531824843514c47fc688c8050bc9f4c2.jpg)



图8-19


根据这个定义,上述问题中力所做的功 W 是力 F 与位移 s 的数量积,即

$$
W = F \cdot s.
$$

由于 $|\pmb{b}|\cos \theta = |\pmb{b}|\cos (\widehat{\pmb{a},\pmb{b}})$ ，当 $\pmb {a}\neq \mathbf{0}$ 时是向量 $\pmb{b}$ 在向量 $\pmb{a}$ 的方向上的投影，用 $\mathrm{Prj}_a\pmb{b}$ 来表示这个投影，便有

$$
\boldsymbol {a} \cdot \boldsymbol {b} = | \boldsymbol {a} | \operatorname{Prj} _ {\boldsymbol {a}} \boldsymbol {b},
$$

同理, 当 $b \neq 0$ 时有

$$
\boldsymbol {a} \cdot \boldsymbol {b} = | \boldsymbol {b} | \operatorname{Prj} _ {b} \boldsymbol {a}.
$$

这就是说,两向量的数量积等于其中一个向量的模和另一个向量在这向量的方向上的投影的乘积.

由数量积的定义可以推得

(1) $a \cdot a = |a|^{2}$ . 

这是因为夹角 $\theta=0$ , 所以

$$
\boldsymbol {a} \cdot \boldsymbol {a} = | \boldsymbol {a} | ^ {2} \cos 0 = | \boldsymbol {a} | ^ {2}.
$$

（2）对于两个非零向量 $a, b$ ，如果 $a \cdot b = 0$ ，那么 $a \perp b$ ；反之，如果 $a \perp b$ ，那么 $a \cdot b = 0$ .

这是因为如果 $a \cdot b = 0$ ，由于 $|a| \neq 0, |b| \neq 0$ ，所以 $\cos \theta = 0$ ，从而 $\theta = \frac{\pi}{2}$ ，即 $a \perp b$ ；反之，如果 $a \perp b$ ，那么 $\theta = \frac{\pi}{2}, \cos \theta = 0$ ，于是 $a \cdot b = |a||b|\cos \theta = 0$ .

由于可以认为零向量与任何向量都垂直,因此,上述结论可叙述为:向量 $a \perp b$ 的充分必要条件是 $a \cdot b = 0$ .

数量积符合下列运算规律：

(1) 交换律 $a \cdot b = b \cdot a$ .

证 根据定义有

$$
\boldsymbol {a} \cdot \boldsymbol {b} = | \boldsymbol {a} | | \boldsymbol {b} | \cos (\widehat {\boldsymbol {a} , \boldsymbol {b}}), \quad \boldsymbol {b} \cdot \boldsymbol {a} = | \boldsymbol {b} | | \boldsymbol {a} | \cos (\widehat {\boldsymbol {b} , \boldsymbol {a}}),
$$

而

$$
| \textbf {a} | | \textbf {b} | = | \textbf {b} | | \textbf {a} | \quad \text {且} \quad \widehat {\cos (\textbf {a} , \textbf {b})} = \cos (\widehat {\textbf {b} , \textbf {a}}),
$$

所以

$$
\boldsymbol {a} \cdot \boldsymbol {b} = \boldsymbol {b} \cdot \boldsymbol {a}.
$$

(2) 分配律 $(a+b)\cdot c=a\cdot c+b\cdot c.$ 

证 当 $c = 0$ 时, 上式显然成立; 当 $c \neq 0$ 时, 有

$$
(a + b) \cdot c = | c | \operatorname{Prj} _ {c} (a + b),
$$

由投影性质 2, 可知

$$
\operatorname{Prj} _ {c} (a + b) = \operatorname{Prj} _ {c} a + \operatorname{Prj} _ {c} b,
$$

所以

$$
(a + b) \cdot c = | c | (\operatorname{Prj} _ {c} a + \operatorname{Prj} _ {c} b) = | c | \operatorname{Prj} _ {c} a + | c | \operatorname{Prj} _ {c} b = a \cdot c + b \cdot c.
$$

(3) 数量积还符合如下的结合律:

$$
(\lambda a) \cdot b = \lambda (a \cdot b), \quad \lambda \text {为数}.
$$

证 当 b=0 时, 上式显然成立; 当 $b \neq 0$ 时, 按投影性质 3, 可得

$$
(\lambda a) \cdot b = | b | \operatorname{Prj} _ {b} (\lambda a) = | b | \lambda \operatorname{Prj} _ {b} a = \lambda | b | \operatorname{Prj} _ {b} a = \lambda (a \cdot b).
$$

由上述结合律,利用交换律,容易推得

$$
\pmb {a} \cdot (\lambda \pmb {b}) = \lambda (\pmb {a} \cdot \pmb {b}) \quad \text {及} \quad (\lambda \pmb {a}) \cdot (\mu \pmb {b}) = \lambda \mu (\pmb {a} \cdot \pmb {b}).
$$

这是因为

$$
\boldsymbol {a} \cdot (\lambda \boldsymbol {b}) = (\lambda \boldsymbol {b}) \cdot \boldsymbol {a} = \lambda (\boldsymbol {b} \cdot \boldsymbol {a}) = \lambda (\boldsymbol {a} \cdot \boldsymbol {b}),
$$

$$
(\lambda a) \cdot (\mu b) = \lambda [ a \cdot (\mu b) ] = \lambda [ \mu (a \cdot b) ] = \lambda \mu (a \cdot b).
$$

例 1 试用向量证明三角形的余弦定理.

证 设在 $\triangle ABC$ 中, $\angle BCA = \theta$ (图8-20), $|BC| = a$ , $|CA| = b$ , $|AB| = c$ , 要证

$$
c ^ {2} = a ^ {2} + b ^ {2} - 2 a b \cos \theta .
$$

记 $\overrightarrow{CB} = a, \overrightarrow{CA} = b, \overrightarrow{AB} = c$ ，则有

$$
\boldsymbol {c} = \boldsymbol {a} - \boldsymbol {b},
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/870931445af4782ab91f879f599e3598d6ba75bb2786512fb3f8956cc24b6f58.jpg)



图8-20


从而

$$
\begin{array}{l} \mid c \mid^ {2} = c \cdot c = (a - b) \cdot (a - b) = a \cdot a + b \cdot b - 2 a \cdot b \\ = | \boldsymbol {a} | ^ {2} + | \boldsymbol {b} | ^ {2} - 2 | \boldsymbol {a} | | \boldsymbol {b} | \cos (\widehat {\boldsymbol {a} , \boldsymbol {b}}). \\ \end{array}
$$

由 $|a|=a,|b|=b,|c|=c$ 及 $(\widehat{a,b})=\theta$ ,即得

$$
c ^ {2} = a ^ {2} + b ^ {2} - 2 a b \cos \theta .
$$

下面我们来推导数量积的坐标表示式.

设 $a=a_{x}i+a_{y}j+a_{z}k,b=b_{x}i+b_{y}j+b_{z}k$ . 按数量积的运算规律可得

$$
\begin{array}{l} \boldsymbol {a} \cdot \boldsymbol {b} = (a _ {x} \boldsymbol {i} + a _ {y} \boldsymbol {j} + a _ {z} \boldsymbol {k}) \cdot (b _ {x} \boldsymbol {i} + b _ {y} \boldsymbol {j} + b _ {z} \boldsymbol {k}) \\ = a _ {x} \boldsymbol {i} \cdot \left(b _ {x} \boldsymbol {i} + b _ {y} \boldsymbol {j} + b _ {z} \boldsymbol {k}\right) + a _ {y} \boldsymbol {j} \cdot \left(b _ {x} \boldsymbol {i} + b _ {y} \boldsymbol {j} + b _ {z} \boldsymbol {k}\right) + a _ {z} \boldsymbol {k} \cdot \left(b _ {x} \boldsymbol {i} + b _ {y} \boldsymbol {j} + b _ {z} \boldsymbol {k}\right) \\ = a _ {x} b _ {x} \boldsymbol {i} \cdot \boldsymbol {i} + a _ {x} b _ {y} \boldsymbol {i} \cdot \boldsymbol {j} + a _ {x} b _ {z} \boldsymbol {i} \cdot \boldsymbol {k} + a _ {y} b _ {x} \boldsymbol {j} \cdot \boldsymbol {i} + a _ {y} b _ {y} \boldsymbol {j} \cdot \boldsymbol {j} + a _ {y} b _ {z} \boldsymbol {j} \cdot \boldsymbol {k} + \\ a _ {z} b _ {x} \boldsymbol {k} \cdot \boldsymbol {i} + a _ {z} b _ {y} \boldsymbol {k} \cdot \boldsymbol {j} + a _ {z} b _ {z} \boldsymbol {k} \cdot \boldsymbol {k}. \\ \end{array}
$$

因为 $i, j$ 和 $k$ 互相垂直，所以 $i \cdot j = j \cdot k = k \cdot i = 0, j \cdot i = k \cdot j = i \cdot k = 0.$ 又因为 $i, j$ 和 $k$ 的模均为1，所以 $i \cdot i = j \cdot j = k \cdot k = 1.$ 因而得

$$
\boldsymbol {a} \cdot \boldsymbol {b} = a _ {x} b _ {x} + a _ {y} b _ {y} + a _ {z} b _ {z}.
$$

这就是两个向量的数量积的坐标表示式.

因为 $a \cdot b = |a||b| \cos \theta$ ，所以当 a 与 b 都不是零向量时，有

$$
\cos \theta = \frac {\boldsymbol {a} \cdot \boldsymbol {b}}{| \boldsymbol {a} | | \boldsymbol {b} |}.
$$

将数量积的坐标表示式及向量的模的坐标表示式代入上式,就得

$$
\cos \theta = \frac {a _ {x} b _ {x} + a _ {y} b _ {y} + a _ {z} b _ {z}}{\sqrt {a _ {x} ^ {2} + a _ {y} ^ {2} + a _ {z} ^ {2}} \sqrt {b _ {x} ^ {2} + b _ {y} ^ {2} + b _ {z} ^ {2}}},
$$

这就是两向量夹角余弦的坐标表示式.

例2 已知三点 $M(1,1,1), A(2,2,1)$ 和 $B(2,1,2)$ ，求 $\angle AMB$ .

解 作向量 $\overrightarrow{MA}$ 及 $\overrightarrow{MB}, \angle AMB$ 就是向量 $\overrightarrow{MA}$ 与 $\overrightarrow{MB}$ 的夹角. 这里, $\overrightarrow{MA} = (1,1,0), \overrightarrow{MB} = (1,0,1)$ , 从而

$$
\overrightarrow {M A} \cdot \overrightarrow {M B} = 1 \times 1 + 1 \times 0 + 0 \times 1 = 1,
$$

$$
\mid \overrightarrow {M A} \mid = \sqrt {1 ^ {2} + 1 ^ {2} + 0 ^ {2}} = \sqrt {2}, \quad \mid \overrightarrow {M B} \mid = \sqrt {1 ^ {2} + 0 ^ {2} + 1 ^ {2}} = \sqrt {2}.
$$

# 

例题精讲

8-1 

代入两向量夹角余弦的表达式,得

$$
\cos \angle A M B = \frac {\overrightarrow {M A} \cdot \overrightarrow {M B}}{| \overrightarrow {M A} | | \overrightarrow {M B} |} = \frac {1}{\sqrt {2} \cdot \sqrt {2}} = \frac {1}{2}.
$$

由此得

$$
\angle A M B = \frac {\pi}{3}.
$$

例 3 设液体流过平面 S 上面积为 A 的一个区域, 液体在这区域上各点处的流速均为(常向量) v. 设 n 为垂直于 S 的单位向量(图 8-21(a)), 计算单位时间内经过这区域流向 n 所指一侧的液体的质量 m(液体的密度为 $\rho$ ).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/548704fa5c8471b73dffd967d4a3b01aa6e91f5361d42ae26afea110e6dd94b4.jpg)



图8-21


解 单位时间内流过这区域的液体组成一个底面积为 A、斜高为 $|v|$ 的斜柱体（图 8-21(b)）。这柱体的斜高与底面的垂线的夹角就是 v 与 n 的夹角 $\theta$ ，所以这柱体的高为 $|v| \cos \theta$ ，体积为

$$
A \mid v \mid \cos \theta = A v \cdot n.
$$

从而,单位时间内经过这区域流向 n 所指一侧的液体的质量为

$$
m = \rho A \boldsymbol {v} \cdot \boldsymbol {n}.
$$

# 二、两向量的向量积

在研究物体转动问题时,不但要考虑这物体所受的力,还要分析这些力所产生的力矩.下面就举一个简单的例子来说明表达力矩的方法.

设 O 为一根杠杆 L 的支点. 有一个力 F 作用于这杠杆上点 P 处. F 与 $\overrightarrow{OP}$ 的夹角为 $\theta$ （图 8-22）. 由力学规定, 力 F 对支点 O 的力矩是一向量 M, 它的模

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/b93d6928fe12c8e9e91b1031381363d4660575ec1d6e26a389c2526f2d8a4c13.jpg)



图8-22


$$
| \boldsymbol {M} | = | O Q | | \boldsymbol {F} | = | \overrightarrow {O P} | | \boldsymbol {F} | \sin \theta ,
$$

而 M 垂直于 $\overrightarrow{OP}$ 与 F 所决定的平面, M 的正向是按右手规则从 $\overrightarrow{OP}$ 以不超过 $\pi$ 的角转向 F 来确定的, 即当右手的四个手指从 $\overrightarrow{OP}$ 以不超过 $\pi$ 的角转向 F 握拳时, 大拇指的指向就是 M 的方向(图 8-23).

这种由两个已知向量按上面的规则来确定另一个向量的情况,在其他力学和物理问题中也会遇到.于是从中抽象出两个向量的向量积概念.

设向量 $c$ 由两个向量 $\pmb{a}$ 与 $\pmb{b}$ 按下列方式定出：

c 的模 $\left|c\right|=\left|a\right|\left|b\right|\sin\theta$ ，其中 $\theta$ 为 a 与 b 的夹角；c 垂直于 a 与 b 所决定的平面（即 c 既垂直于 a，又垂直于 b），c 的正向按右手规则从 a 转向 b 来确定（图 8-24），向量 c 叫做向量 a 与 b 的向量积，记作 $a\times b$ ，即

$$
\boldsymbol {c} = \boldsymbol {a} \times \boldsymbol {b}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/b9d97c28800bd25d9dc2193b94c79e806767427e2dfbd855accc33a6e7dfa6d7.jpg)



图8-23


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/9edacc8cf4e2bb2866b827c7b6ba999459fe75adc4a809bbb086bcf929374663.jpg)



图8-24


按此定义,上面的力矩 M 等于 $\overrightarrow{OP}$ 与 F 的向量积,即

$$
\boldsymbol {M} = \overrightarrow {O P} \times \boldsymbol {F}.
$$

由向量积的定义可以推得

(1) $a \times a = 0.$ 

这是因为夹角 $\theta = 0$ ，所以 $|\pmb {a}\times \pmb{a}| = |\pmb {a}|^2\sin 0 = 0.$ 

（2）对于两个非零向量 a, b，如果 $a \times b = 0$ ，那么 $a \parallel b$ ；反之，如果 $a \parallel b$ ，那么 $a \times b = 0$ 。

这是因为如果 $a \times b = 0$ ，由于 $|a| \neq 0, |b| \neq 0$ ，那么必有 $\sin \theta = 0$ ，于是 $\theta = 0$ 或 $\pi$ ，即 $a // b$ ；反之，如果 $a // b$ ，那么 $\theta = 0$ 或 $\pi$ ，于是 $\sin \theta = 0$ ，从而 $|a \times b| = 0$ ，即 $a \times b = 0$ .

由于可以认为零向量与任何向量都平行,因此,上述结论可叙述为:向量 $a \parallel b$ 的充分必要条件是 $a \times b = 0$ .

向量积符合下列运算规律：

(1) $b \times a = -a \times b.$ 

这是因为按右手规则从 b 转向 a 定出的方向恰好与按右手规则从 a 转向 b 定出的方向相反. 它表明交换律对向量积不成立.

(2) 分配律 $(a+b)\times c=a\times c+b\times c.$ 

(3) 向量积还符合如下的结合律:

$$
(\lambda a) \times b = a \times (\lambda b) = \lambda (a \times b) \quad (\lambda \text {为数}).
$$

这两个规律这里不予证明.

下面来推导向量积的坐标表示式.

设 $a = a_{x}i + a_{y}j + a_{z}k, b = b_{x}i + b_{y}j + b_{z}k.$ 那么，按上述运算规律，得

$$
\begin{array}{l} \boldsymbol {a} \times \boldsymbol {b} = (a _ {x} \boldsymbol {i} + a _ {y} \boldsymbol {j} + a _ {z} \boldsymbol {k}) \times (b _ {x} \boldsymbol {i} + b _ {y} \boldsymbol {j} + b _ {z} \boldsymbol {k}) \\ = a _ {x} \boldsymbol {i} \times \left(b _ {x} \boldsymbol {i} + b _ {y} \boldsymbol {j} + b _ {z} \boldsymbol {k}\right) + a _ {y} \boldsymbol {j} \times \left(b _ {x} \boldsymbol {i} + b _ {y} \boldsymbol {j} + b _ {z} \boldsymbol {k}\right) + a _ {z} \boldsymbol {k} \times \left(b _ {x} \boldsymbol {i} + b _ {y} \boldsymbol {j} + b _ {z} \boldsymbol {k}\right) \\ = a _ {x} b _ {x} (\boldsymbol {i} \times \boldsymbol {i}) + a _ {x} b _ {y} (\boldsymbol {i} \times \boldsymbol {j}) + a _ {x} b _ {z} (\boldsymbol {i} \times \boldsymbol {k}) + a _ {y} b _ {x} (\boldsymbol {j} \times \boldsymbol {i}) + a _ {y} b _ {y} (\boldsymbol {j} \times \boldsymbol {j}) + a _ {y} b _ {z} (\boldsymbol {j} \times \boldsymbol {k}) + \\ a _ {z} b _ {x} (\boldsymbol {k} \times \boldsymbol {i}) + a _ {z} b _ {y} (\boldsymbol {k} \times \boldsymbol {j}) + a _ {z} b _ {z} (\boldsymbol {k} \times \boldsymbol {k}). \\ \end{array}
$$

因为 $i \times i = j \times j = k \times k = 0, i \times j = k, j \times k = i, k \times i = j, j \times i = -k, k \times j = -i$ 和 $i \times k = -j$ , 所以

$$
\boldsymbol {a} \times \boldsymbol {b} = \left(a _ {y} b _ {z} - a _ {z} b _ {y}\right) \boldsymbol {i} + \left(a _ {z} b _ {x} - a _ {x} b _ {z}\right) \boldsymbol {j} + \left(a _ {x} b _ {y} - a _ {y} b _ {x}\right) \boldsymbol {k}.
$$

为了帮助记忆,利用三阶行列式,上式可写成

$$
\boldsymbol {a} \times \boldsymbol {b} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ a _ {x} & a _ {y} & a _ {z} \\ b _ {x} & b _ {y} & b _ {z} \end{array} \right|.
$$

例 4 设 $a=(2,1,-1)$ , $b=(1,-1,2)$ , 计算 $a \times b$ .

解

$$
\boldsymbol {a} \times \boldsymbol {b} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ 2 & 1 & - 1 \\ 1 & - 1 & 2 \end{array} \right| = \boldsymbol {i} - 5 \boldsymbol {j} - 3 \boldsymbol {k}.
$$

例 5 已知三角形 ABC 的顶点分别是 A(1,2,3), B(3,4,5) 和 C(2,4,7)，求三角形 ABC 的面积.

解 根据向量积的定义, 可知三角形 ABC 的面积

$$
S _ {\triangle A B C} = \frac {1}{2} | \overrightarrow {A B} | | \overrightarrow {A C} | \sin \angle A = \frac {1}{2} | \overrightarrow {A B} \times \overrightarrow {A C} |.
$$

由于 $\overrightarrow{AB} = (2,2,2),\overrightarrow{AC} = (1,2,4)$ ，因此

$$
\overrightarrow {A B} \times \overrightarrow {A C} = \left| \begin{array}{l l l} i & j & k \\ 2 & 2 & 2 \\ 1 & 2 & 4 \end{array} \right| = 4 i - 6 j + 2 k,
$$

于是

$$
S _ {\triangle A B C} = \frac {1}{2} | 4 i - 6 j + 2 k | = \frac {1}{2} \sqrt {4 ^ {2} + (- 6) ^ {2} + 2 ^ {2}} = \sqrt {1 4}.
$$

例 6 设刚体以等角速度 $\omega$ 绕 l 轴旋转, 计算刚体上一点 M 的线速度.

解 刚体绕 l 轴旋转时, 我们可以用在 l 轴上的一个向量 $\omega$ 表示角速度, 它的大小等于角速度的大小, 它的方向由右手规则定出: 即以右手握住 l 轴, 当右手的四个手指的转向与刚体的旋转方向一致时, 大拇指的指向就是 $\omega$ 的方向 (图 8-25).

设点 M 到旋转轴 l 的距离为 a，再在 l 轴上任取一点 O 作向量 $r = \overrightarrow{OM}$ ，并以 $\theta$ 表示 $\omega$ 与 r 的夹角，则

$$
a = | r | \sin \theta .
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/5336b321b927fac8498b51885cbaa67815ea601adce8638d53d3bb10a077441d.jpg)



图8-25


设点 M 的线速度为 v，由物理学上线速度与角速度间的关系可知，v 的大小为

$$
| \boldsymbol {v} | = | \omega | a = | \omega | | r | \sin \theta ;
$$

v 垂直于通过 M 点与 l 轴的平面, 即 v 既垂直于 $\omega$ 又垂直于 r; 又 v 的方向使 $\omega, r, v$ 符合右手规则. 因此有

$$
\boldsymbol {v} = \omega \times r.
$$

# * 三、向量的混合积

设已知三个向量 a, b 和 c. 先作两向量 a 和 b 的向量积 $a \times b$ ，把所得到的向量与第三个向量 c 再作数量积 $(a \times b) \cdot c$ ，这样得到的数叫做三向量 a, b, c 的混合积，记作 [abc].

下面我们来推出三向量的混合积的坐标表示式.

设 $a = (a_{x}, a_{y}, a_{z}), b = (b_{x}, b_{y}, b_{z}), c = (c_{x}, c_{y}, c_{z})$ ，因为

$$
\boldsymbol {a} \times \boldsymbol {b} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ a _ {x} & a _ {y} & a _ {z} \\ b _ {x} & b _ {y} & b _ {z} \end{array} \right| = \left| \begin{array}{c c} a _ {y} & a _ {z} \\ b _ {y} & b _ {z} \end{array} \right| \boldsymbol {i} - \left| \begin{array}{c c} a _ {x} & a _ {z} \\ b _ {x} & b _ {z} \end{array} \right| \boldsymbol {j} + \left| \begin{array}{c c} a _ {x} & a _ {y} \\ b _ {x} & b _ {y} \end{array} \right| \boldsymbol {k},
$$

再按两向量的数量积的坐标表示式,便得

$$
\begin{array}{l} [ \textbf {a b c} ] = (\textbf {a} \times \textbf {b}) \cdot \textbf {c} \\ = c _ {x} \left| \begin{array}{l l} a _ {y} & a _ {z} \\ b _ {y} & b _ {z} \end{array} \right| - c _ {y} \left| \begin{array}{l l} a _ {x} & a _ {z} \\ b _ {x} & b _ {z} \end{array} \right| + c _ {z} \left| \begin{array}{l l} a _ {x} & a _ {y} \\ b _ {x} & b _ {y} \end{array} \right| = \left| \begin{array}{l l l} a _ {x} & a _ {y} & a _ {z} \\ b _ {x} & b _ {y} & b _ {z} \\ c _ {x} & c _ {y} & c _ {z} \end{array} \right|. \\ \end{array}
$$

向量的混合积有下述几何意义：

向量的混合积 $[abc] = (a \times b) \cdot c$ 是这样一个数, 它的绝对值表示以向量 $a, b, c$ 为棱的平行六面体的体积. 如果向量 $a, b, c$ 组成右手系 (即 $c$ 的方向按右手规则从 $a$ 转向 b 来确定), 那么混合积的符号是正的; 如果 a, b, c 组成左手系 (即 c 的方向按左手规则从 a 转向 b 来确定), 那么混合积的符号是负的.

事实上, 设 $\overrightarrow{OA}=a, \overrightarrow{OB}=b, \overrightarrow{OC}=c$ . 按向量积的定义, 向量积 $a \times b = f$ 是一个向量, 它的模在数值上等于以向量 a 和 b 为邻边所作平行四边形 OADB 的面积, 它的方向垂直于这平行四边形的平面, 且当 a, b, c 组成右手系时, 向量 f 与向量 c 朝着这平面的同侧 (图 8-26); 当 a, b, c 组成左手系时, 向量 f 与向量 c 朝着这平面的异侧. 所以, 如设 f 与 c 的夹角为 $\alpha$ , 那么当 a, b, c 组成右手系时, $\alpha$ 为锐角; 当 a, b, c 组成左手系时, $\alpha$ 为钝角. 由于

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/f70fc9cbb539a2d2e65146ef4fc67940b8a91a107d2bbe6f74c8e8f8fe16cb2b.jpg)



图8-26


$$
[ a b c ] = (a \times b) \cdot c = | a \times b | | c | \cos \alpha ,
$$

所以当 $a, b, c$ 组成右手系时， $[abc]$ 为正；当 $a, b, c$ 组成左手系时， $[abc]$ 为负.

因为以向量 a, b, c 为棱的平行六面体的底(平行四边形 OADB)的面积 S 在数值上等于 $\left|a \times b\right|$ ，它的高 h 等于向量 c 在向量 f 上的投影的绝对值，即

$$
h = \left| \operatorname{Prj} _ {f} c \right| = \left| c \right| \left| \cos \alpha \right|,
$$

所以平行六面体的体积

$$
V = S h = | \boldsymbol {a} \times \boldsymbol {b} | | \boldsymbol {c} | | \cos \alpha | = | [ \boldsymbol {a b c} ] |.
$$

由上述混合积的几何意义可知,若混合积 $[a b c]\neq0$ ,则能以a,b,c三向量为棱构成平行六面体,从而a,b,c三向量不共面;反之,若a,b,c三向量不共面,则必能以a,b,c为棱构成平行六面体,从而 $[a b c]\neq0$ .于是有下述结论:

三向量 a, b, c 共面的充分必要条件是它们的混合积 $[a \ b \ c] = 0$ ，即

$$
\left| \begin{array}{c c c} a _ {x} & a _ {y} & a _ {z} \\ b _ {x} & b _ {y} & b _ {z} \\ c _ {x} & c _ {y} & c _ {z} \end{array} \right| = 0.
$$

例7 已知不在一平面上的四点 $A(x_{1},y_{1},z_{1}),B(x_{2},y_{2},z_{2}),C(x_{3},y_{3},z_{3}),D(x_{4},y_{4},z_{4})$ 。求四面体ABCD的体积.

解 由立体几何知道, 四面体的体积 V 等于以向量 $\overrightarrow{AB}, \overrightarrow{AC}$ 和 $\overrightarrow{AD}$ 为棱的平行六面体的体积的六分之一. 因而

$$
V = \frac {1}{6} \left| [ \overrightarrow {A B} \overrightarrow {A C} \overrightarrow {A D} ] \right|.
$$

由于

$$
\overrightarrow {A B} = \left(x _ {2} - x _ {1}, y _ {2} - y _ {1}, z _ {2} - z _ {1}\right),
$$

$$
\overrightarrow {A C} = \left(x _ {3} - x _ {1}, y _ {3} - y _ {1}, z _ {3} - z _ {1}\right),
$$

$$
\overrightarrow {A D} = \left(x _ {4} - x _ {1}, y _ {4} - y _ {1}, z _ {4} - z _ {1}\right),
$$

所以

$$
V = \pm \frac {1}{6} \left| \begin{array}{c c c} x _ {2} - x _ {1} & y _ {2} - y _ {1} & z _ {2} - z _ {1} \\ x _ {3} - x _ {1} & y _ {3} - y _ {1} & z _ {3} - z _ {1} \\ x _ {4} - x _ {1} & y _ {4} - y _ {1} & z _ {4} - z _ {1} \end{array} \right|,
$$

上式中符号的选择必须和行列式的符号一致.

例 8 已知 $A(1,2,0)$ , $B(2,3,1)$ , $C(4,2,2)$ , $M(x,y,z)$ 四点共面, 求点 M 的坐标 x, y, z 所满足的关系式.

解 $A, B, C, M$ 四点共面相当于 $\overrightarrow{AM}, \overrightarrow{AB}, \overrightarrow{AC}$ 三向量共面，这里 $\overrightarrow{AM} = (x - 1, y - 2, z)$ ， $\overrightarrow{AB} = (1, 1, 1), \overrightarrow{AC} = (3, 0, 2)$ . 按三向量共面的充分必要条件，可得

$$
\left| \begin{array}{c c c} x - 1 & y - 2 & z \\ 1 & 1 & 1 \\ 3 & 0 & 2 \end{array} \right| = 0,
$$

即

$$
2 x + y - 3 z - 4 = 0.
$$

这就是点 M 的坐标所满足的关系式.

# 习题8-2

1. 设 $a = 3i - j - 2k, b = i + 2j - k$ ，求

(1) $a \cdot b$ 及 $a \times b$ ; (2) $(-2a) \cdot 3b$ 及 $a \times 2b$ ; (3) $a, b$ 的夹角的余弦.

2. 设 a, b, c 为单位向量，且满足 $a + b + c = 0$ ，求 $a \cdot b + b \cdot c + c \cdot a$ .

3. 已知 $M_{1}(1, -1, 2), M_{2}(3, 3, 1)$ 和 $M_{3}(3, 1, 3)$ . 求与 $\overrightarrow{M_1M_2}, \overrightarrow{M_2M_3}$ 同时垂直的单位向量.

4. 设质量为 100 kg 的物体从点 $M_{1}(3,1,8)$ 沿直线移动到点 $M_{2}(1,4,2)$ ，计算重力所做的功（坐标系长度单位为 m，重力方向为 z 轴负方向）.

5. 在杠杆上支点 O 的一侧与点 O 的距离为 $x_{1}$ 的点 $P_{1}$ 处，作用着一个与 $\overrightarrow{OP_{1}}$ 成角 $\theta_{1}$ 的力 $F_{1}$ ; 在 O 的另一侧与点 O 的距离为 $x_{2}$ 的点 $P_{2}$ 处，作用着一个与 $\overrightarrow{OP_{2}}$ 成角 $\theta_{2}$ 的力 $F_{2}$ （图 8-27）. 问 $\theta_{1}, \theta_{2}, x_{1}, x_{2}, |F_{1}|, |F_{2}|$ 符合怎样的条件才能使杠杆保持平衡？

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/c787ec16047f74c31d52fde832013df637e72b01abd3421130df37b7d6ce7d0f.jpg)



图8-27


6. 求向量 $a=(4,-3,4)$ 在向量 $b=(2,2,1)$ 上的投影.

7. 设 $a=(3,5,-2)$ , $b=(2,1,4)$ ，问 $\lambda$ 与 $\mu$ 有怎样的关系，能使得 $\lambda a + \mu b$ 与 z 轴垂直？

8. 试用向量证明直径所对的圆周角是直角.

9. 已知向量 $a = 2i - 3j + k, b = i - j + 3k$ 和 $c = i - 2j$ , 计算:

(1) $(a \cdot b)c - (a \cdot c)b$ ; (2) $(a + b) \times (b + c)$ ; (3) $(a \times b) \cdot c$ . 

10. 设一平行四边形对角线为 $c = a + 2b, d = 3a - 4b$ ，其中 $a, b$ 为单位向量且 $a \perp b$ ，求该平行四边形的面积。

11. 设有四面体 OPQR （图 8-28），其中 $\triangle OPQ, \triangle OQR, \triangle OPR$ 和 $\triangle PQR$ 的面积分别为 A, B, C 和 D. 试用向量方法证明如下三维空间中的勾股定理：

$$
A ^ {2} + B ^ {2} + C ^ {2} = D ^ {2}.
$$

*12. 已知 $a = (a_x, a_y, a_z), b = (b_x, b_y, b_z), c = (c_x, c_y, c_z)$ ，试利用行列式的性质证明：

$$
(a \times b) \cdot c = (b \times c) \cdot a = (c \times a) \cdot b.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/f0f8063c4207260be03f6af0c04c23e7bd4ee99bd710fa4018ef622776114a08.jpg)



图8-28


13. 试用向量证明不等式：

$$
\sqrt {a _ {1} ^ {2} + a _ {2} ^ {2} + a _ {3} ^ {2}} \sqrt {b _ {1} ^ {2} + b _ {2} ^ {2} + b _ {3} ^ {2}} \geqslant \left| a _ {1} b _ {1} + a _ {2} b _ {2} + a _ {3} b _ {3} \right|,
$$

其中 $a_1, a_2, a_3, b_1, b_2, b_3$ 为任意实数，并指出等号成立的条件.

# 第三节 平面及其方程

# 一、曲面方程与空间曲线方程的概念

因为平面与空间直线分别是曲面与空间曲线的特例,所以在讨论平面与空间直线以前,先引入有关曲面方程与空间曲线方程的概念.

像在平面解析几何中把平面曲线当作动点的轨迹一样,在空间解析几何中,任何曲面或曲线都看作点的几何轨迹.在这样的意义下,如果曲面 S 与三元方程

$$
F (x, y, z) = 0 \tag {3-1}
$$

有下述关系：

(1) 曲面 S 上任一点的坐标都满足方程(3-1);

(2) 不在曲面 S 上的点的坐标都不满足方程(3-1)，那么，方程(3-1)就叫做曲面 S 的方程，而曲面 S 就叫做方程(3-1)的图形(图 8-29).

空间曲线可以看作两个曲面 $S_{1}, S_{2}$ 的交线. 设

$$
F (x, y, z) = 0 \quad {\text {和}} \quad G (x, y, z) = 0
$$

分别是这两个曲面的方程,它们的交线为 C（图 8-30）.因为曲线 C 上的任何点的坐标应同时满足这两个曲面的方程,所以应满足方程组

$$
\left\{ \begin{array}{l} F (x, y, z) = 0, \\ G (x, y, z) = 0. \end{array} \right. \tag {3-2}
$$

反过来,如果点 $M$ 不在曲线 $C$ 上,那么它不可能同时在两个曲面上,所以它的坐标不满足方程组(3-2).因此,曲线 $C$ 可以用方程组(3-2)来表示.方程组(3-2)就叫做空间曲线 $C$ 的方程,而曲线 $C$ 就叫做方程组(3-2)的图形.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/585df62700b673f47d2b726d07e1ac16201eabffe129cfa6699ea4de8b3867bf.jpg)



图8-29


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/262d13963294391d7310719f294b54d98d5c332018958b8487ef7028e7965ee1.jpg)



图8-30


在本节和下一节里,我们将以向量为工具,在空间直角坐标系中讨论最简单的曲面和曲线——平面和直线.

# 二、平面的点法式方程

如果一非零向量垂直于一平面,那么这个向量就叫做该平面的法向量.容易知道,平面上的任一向量均与该平面的法向量垂直.

因为过空间一点可以作而且只能作一平面垂直于一已知直线, 所以当平面 $\Pi$ 上一点 $M_0(x_0, y_0, z_0)$ 和它的一个法向量 $n = (A, B, C)$ 为已知时, 平面 $\Pi$ 的位置就完全确定了. 下面我们来建立平面 $\Pi$ 的方程.

设 $M(x,y,z)$ 是平面 $\Pi$ 上的任一点(图8-31).则向量 $\overrightarrow{M_0M}$ 必与平面 $\Pi$ 的法向量 $\pmb{n}$ 垂直，即它们的数量积等于零

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/0ebe4d306e6aeaf9de9e1c27efa7e06e7c881805f257a743b1f3f8602b4c241f.jpg)



图8-31


$$
\boldsymbol {n} \cdot \overrightarrow {M _ {0} M} = 0.
$$

因为 $n = (A, B, C), \overrightarrow{M_0M} = (x - x_0, y - y_0, z - z_0)$ ，所以有

$$
A (x - x _ {0}) + B (y - y _ {0}) + C (z - z _ {0}) = 0. \tag {3-3}
$$

这就是平面 $\Pi$ 上任一点 M 的坐标 x, y, z 所满足的方程.

反过来, 如果 $M(x,y,z)$ 不在平面 $\Pi$ 上, 那么向量 $\overrightarrow{M_{0}M}$ 与法向量 n 不垂直, 从而 $n \cdot \overrightarrow{M_{0}M} \neq 0$ , 即不在平面 $\Pi$ 上的点 M 的坐标 x, y, z 不满足方程 (3-3).

由此可知,平面 $\Pi$ 上的任一点的坐标 x,y,z 都满足方程(3-3),不在平面 $\Pi$ 上的点的坐标都不满足方程(3-3).这样,方程(3-3)就是平面 $\Pi$ 的方程,而平面 $\Pi$ 就是方程(3-3)的图形.因为方程(3-3)是由平面 $\Pi$ 上的一点 $M_{0}(x_{0},y_{0},z_{0})$ 及它的一个法向量 $n=(A,B,C)$ 确定的,所以方程(3-3)叫做平面的点法式方程.

例 1 求过点 $(2,-3,0)$ 且以 $n=(1,-2,3)$ 为法向量的平面的方程.

解 根据平面的点法式方程(3-3), 得所求平面的方程为

$$
(x - 2) - 2 (y + 3) + 3 z = 0,
$$

即

$$
x - 2 y + 3 z - 8 = 0.
$$

例2 求过三点 $M_{1}(2, - 1,4),M_{2}(-1,3, - 2)$ 和 $M_3(0,2,3)$ 的平面的方程.

解 先找出这平面的法向量 n. 因为向量 n 与向量 $\overrightarrow{M_{1}M_{2}}$ 和 $\overrightarrow{M_{1}M_{3}}$ 都垂直，而 $\overrightarrow{M_{1}M_{2}} = (-3, 4, -6)$ ， $\overrightarrow{M_{1}M_{3}} = (-2, 3, -1)$ ，所以可取它们的向量积为 n，即

$$
\boldsymbol {n} = \overrightarrow {M _ {1} M _ {2}} \times \overrightarrow {M _ {1} M _ {3}} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ - 3 & 4 & - 6 \\ - 2 & 3 & - 1 \end{array} \right| = 1 4 \boldsymbol {i} + 9 \boldsymbol {j} - \boldsymbol {k},
$$

根据平面的点法式方程(3-3)，得所求平面的方程为

$$
1 4 (x - 2) + 9 (y + 1) - (z - 4) = 0,
$$

即

$$
1 4 x + 9 y - z - 1 5 = 0.
$$

# 三、平面的一般方程

因为平面的点法式方程(3-3)是 $x, y$ 和 $z$ 的一次方程, 而任一平面都可以用它上面的一点及它的法向量来确定, 所以任一平面都可以用三元一次方程来表示.

反过来,设有三元一次方程

$$
A x + B y + C z + D = 0. \tag {3-4}
$$

我们任取满足该方程的一组数 $x_0, y_0, z_0$ ，即

$$
A x _ {0} + B y _ {0} + C z _ {0} + D = 0. \tag {3-5}
$$

把上述两等式相减,得

$$
A (x - x _ {0}) + B (y - y _ {0}) + C (z - z _ {0}) = 0. \tag {3-6}
$$

把它和平面的点法式方程(3-3)作比较,可以知道方程(3-6)是通过点 $M_{0}(x_{0},y_{0},z_{0})$ 且以 $n=(A,B,C)$ 为法向量的平面方程.方程(3-4)与方程(3-6)同解,这是因为由(3-4)减去(3-5)即得(3-6),又由(3-6)加上(3-5)就得(3-4).由此可知,任一三元一次方程(3-4)的图形总是一个平面.方程(3-4)称为平面的一般方程,其中x,y,z的系数就是该平面的一个法向量n的坐标,即 $n=(A,B,C)$ .

例如,方程

$$
3 x - 4 y + z - 9 = 0
$$

表示一个平面, $n=(3,-4,1)$ 是这平面的一个法向量.

对于一些特殊的三元一次方程,应该熟悉它们的图形的特点.

当 D=0 时, 方程(3-4)成为 $Ax+By+Cz=0$ , 它表示一个通过原点的平面.

当 $A = 0$ 时，方程(3-4)成为 $By + Cz + D = 0$ ，法向量 $\pmb {n} = (0,B,C)$ 垂直于 $x$ 轴，方程表示一个平行于(或包含) $x$ 轴的平面.

同样, 方程 $Ax + Cz + D = 0$ 和 $Ax + By + D = 0$ 分别表示一个平行于(或包含) y 轴和 z 轴的平面.

当 $A = B = 0$ 时，方程(3-4)成为 $Cz + D = 0$ 或 $z = -\frac{D}{C}$ ，法向量 $\pmb {n} = (0,0,C)$ 同时垂直于 $x$ 轴和 $y$ 轴，方程表示一个平行于（或重合于） $xOy$ 面的平面.

同样,方程 Ax+D=0 和 $By+D=0$ 分别表示一个平行于(或重合于) yOz 面和 zOx 面的平面.

例 3 求通过 x 轴和点 $(4, -3, -1)$ 的平面的方程.

解 由于平面通过 x 轴, 从而它的法向量垂直于 x 轴, 于是法向量在 x 轴上的投影为零, 即 A=0; 又由平面通过 x 轴, 它必通过原点, 于是 D=0. 因此可设这平面的方程为

$$
B y + C z = 0.
$$

又因这平面通过点 $(4,-3,-1)$ ，所以有

$$
- 3 B - C = 0, \quad \text { 或 } \quad C = - 3 B.
$$

以此代入所设方程并除以 $B(B \neq 0)$ ，便得所求的平面方程为

$$
y - 3 z = 0.
$$

例 4 设一平面与 x 轴、y 轴和 z 轴的交点依次为 $P(a,0,0)$ , $Q(0,b,0)$ , $R(0,0,c)$ 三点（图 8-32），求这平面的方程（其中 $a \neq 0, b \neq 0, c \neq 0$ ）.

解 设所求平面的方程为

$$
A x + B y + C z + D = 0.
$$

因为 $P(a,0,0)$ , $Q(0,b,0)$ 和 $R(0,0,c)$ 三点都在这平面上, 所以点 P, Q 和 R 的坐标都满足方程 (3-4), 即有

$$
\left\{ \begin{array}{l} a A + D = 0, \\ b B + D = 0, \\ c C + D = 0, \end{array} \right.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/83bc964c6a4322fb02b770c6368f4e33c86d3ff96f7e3ec6fae1abc5281f0221.jpg)



图8-32


解得

$$
A = - \frac {D}{a}, \quad B = - \frac {D}{b}, \quad C = - \frac {D}{c}.
$$

以此代入(3-4)并除以 $D(D \neq 0)$ , 便得所求的平面方程为

$$
\frac {x}{a} + \frac {y}{b} + \frac {z}{c} = 1. \tag {3-7}
$$

方程(3-7)叫做平面的截距式方程,而a,b和c依次叫做平面在x轴、y轴和z轴上的截距.

# 四、两平面的夹角

两平面的法向量的夹角(通常指锐角或直角)称为两平面的夹角.

设平面 $\Pi_1$ 和 $\Pi_2$ 的法向量依次为 $n_1 = (A_1, B_1, C_1)$ 和 $n_2 = (A_2, B_2, C_2)$ ，则平面 $\Pi_1$ 和 $\Pi_2$ 的夹角 $\theta$ （图8-33）应是 $(\widehat{n_1, n_2})$ 和 $(-n_1, n_2) = \pi - (\widehat{n_1, n_2})$ 两者中的锐角或直角，因此， $\cos \theta = |\cos (\widehat{n_1, n_2})|$ . 按两向量夹角余弦的坐标表示式，平面 $\Pi_1$ 和平面 $\Pi_2$ 的夹角 $\theta$ 可由

$$
\cos \theta = \frac {\left| A _ {1} A _ {2} + B _ {1} B _ {2} + C _ {1} C _ {2} \right|}{\sqrt {A _ {1} ^ {2} + B _ {1} ^ {2} + C _ {1} ^ {2}} \sqrt {A _ {2} ^ {2} + B _ {2} ^ {2} + C _ {2} ^ {2}}} \tag {3-8}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/d254d7be714aa5f314f1334f7c9e931b634f43beffd418491ef723537e90c282.jpg)



图8-33


来确定.

从两向量垂直、平行的充分必要条件立即推得下列结论：

两平面 $\Pi_{1}$ 和 $\Pi_{2}$ 互相垂直相当于 $A_{1}A_{2}+B_{1}B_{2}+C_{1}C_{2}=0$ ;

两平面 $\Pi_{1}$ 和 $\Pi_{2}$ 互相平行或重合相当于 $\frac{A_{1}}{A_{2}} = \frac{B_{1}}{B_{2}} = \frac{C_{1}}{C_{2}}$ .

例 5 求两平面 $x-y+2z-6=0$ 和 $2x+y+z-5=0$ 的夹角.

解 由公式(3-8)有

$$
\cos \theta = \frac {| 1 \times 2 + (- 1) \times 1 + 2 \times 1 |}{\sqrt {1 ^ {2} + (- 1) ^ {2} + 2 ^ {2}} \sqrt {2 ^ {2} + 1 ^ {2} + 1 ^ {2}}} = \frac {1}{2},
$$

因此,所求夹角 $\theta=\frac{\pi}{3}$ .

例 6 一平面通过两点 $M_{1}(1,1,1)$ 和 $M_{2}(0,1,-1)$ 且垂直于平面 $x+y+z=0$ ，求它的方程.

解 设所求平面的一个法向量为

$$
\boldsymbol {n} = (A, B, C).
$$

因 $\overrightarrow{M_1M_2} = (-1,0, - 2)$ 在所求平面上，它必与 $\pmb{n}$ 垂直，所以有

$$
- A - 2 C = 0. \tag {3-9}
$$

又因所求的平面垂直于已知平面 $x+y+z=0$ ，所以又有

$$
A + B + C = 0. \tag {3-10}
$$

由式(3-9)、式(3-10)得到

$$
A = - 2 C, \quad B = C.
$$

由平面的点法式方程可知,所求平面方程为

$$
A (x - 1) + B (y - 1) + C (z - 1) = 0.
$$

将 A = -2C 及 B = C 代入上式, 并约去 C ( $C \neq 0$ ), 便得

$$
- 2 (x - 1) + (y - 1) + (z - 1) = 0,
$$

即

$$
2 x - y - z = 0.
$$

这就是所求的平面方程.

例 7 设 $P_{0}(x_{0},y_{0},z_{0})$ 是平面 $Ax+By+Cz+D=0$ 外一点，求 $P_{0}$ 到这平面的距离（图 8-34）.

解 在平面上任取一点 $P_{1}(x_{1},y_{1},z_{1})$ ，并作一法向量 n，由图 8-34，并考虑到 $\overrightarrow{P_{1}P_{0}}$ 与 n 的夹角 $\theta$ 也可能是钝角，得所求的距离

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/f21633a5c9bf364dc7a48007414d1674461a6ca12961aa42247c33e03a41651c.jpg)



图8-34


$$
d = | \overrightarrow {P _ {1} P _ {0}} | | \cos \theta | = \frac {| \overrightarrow {P _ {1} P _ {0}} \cdot n |}{| n |}.
$$

而

$$
\boldsymbol {n} = (A, B, C), \quad \overrightarrow {P _ {1} P _ {0}} = \left(x _ {0} - x _ {1}, y _ {0} - y _ {1}, z _ {0} - z _ {1}\right),
$$

得

$$
\frac {\overrightarrow {P _ {1} P _ {0}} \cdot \boldsymbol {n}}{| \boldsymbol {n} |} = \frac {A (x _ {0} - x _ {1}) + B (y _ {0} - y _ {1}) + C (z _ {0} - z _ {1})}{\sqrt {A ^ {2} + B ^ {2} + C ^ {2}}} = \frac {A x _ {0} + B y _ {0} + C z _ {0} - (A x _ {1} + B y _ {1} + C z _ {1})}{\sqrt {A ^ {2} + B ^ {2} + C ^ {2}}}.
$$

因为 $Ax_{1} + By_{1} + Cz_{1} + D = 0$ ，所以

$$
\frac {\overrightarrow {P _ {1} P _ {0}} \cdot \boldsymbol {n}}{| \boldsymbol {n} |} = \frac {A x _ {0} + B y _ {0} + C z _ {0} + D}{\sqrt {A ^ {2} + B ^ {2} + C ^ {2}}}.
$$

由此得点 $P_{0}(x_{0},y_{0},z_{0})$ 到平面 $Ax + By + Cz + D = 0$ 的距离公式

$$
d = \frac {\mid A x _ {0} + B y _ {0} + C z _ {0} + D \mid}{\sqrt {A ^ {2} + B ^ {2} + C ^ {2}}}. \tag {3-11}
$$

例如,求点 $(2,1,1)$ 到平面 $x+y-z+1=0$ 的距离,可利用公式 $(3-11)$ ,便得

$$
d = \frac {\mid 1 \times 2 + 1 \times 1 - 1 \times 1 + 1 \mid}{\sqrt {1 ^ {2} + 1 ^ {2} + (- 1) ^ {2}}} = \frac {3}{\sqrt {3}} = \sqrt {3}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a60ac6a5cf2927cdf506581ec6bf05ba7c231255e97c0159d7ebc690254db159.jpg)


例题精讲
8-2

# 习题8-3

1. 求过点 $(3,0,-1)$ 且与平面 $3x-7y+5z-12=0$ 平行的平面方程.

2. 求过点 $M_{0}(2,9,-6)$ 且与连接坐标原点及点 $M_{0}$ 的线段 $OM_{0}$ 垂直的平面方程.

3. 求过 $M_{1}(1,1,-1)$ , $M_{2}(-2,-2,2)$ 和 $M_{3}(1,-1,2)$ 三点的平面方程.

4. 指出下列各平面的特殊位置,并画出各平面:

(1) x=0; 

(2) 3y-1=0; 

(3) 2x-3y-6=0; 

(4) $x - \sqrt{3} y = 0$ ; 

5. 求平面 $2x-2y+z+5=0$ 与各坐标面的夹角的余弦.

6. 设一平面过点 $M_{0}(1,2,-1)$ 且垂直于平面 $3x-4y+z+16=0$ 和 $4x-z+6=0$ ，试求这平面方程.

7. 求三平面 $x+3y+z=1,2x-y-z=0,-x+2y+2z=3$ 的交点.

8. 分别按下列条件求平面方程：

(1) 平行于 zOx 面且经过点 $(2, -5, 3)$ ;

(2) 通过 z 轴和点 $(-3,1,-2)$ ;

(3) 平行于 x 轴且经过两点 $(4,0,-2)$ 和 $(5,1,7)$ .

9. 求点 $(1,2,1)$ 到平面 $x+2y+2z-10=0$ 的距离.

# 第四节 空间直线及其方程

# 一、空间直线的一般方程

空间直线 L 可以看做是两个平面 $\Pi_{1}$ 和 $\Pi_{2}$ 的交线（图 8-35）。如果两个相交的平面 $\Pi_{1}$ 和 $\Pi_{2}$ 的方程分别为 $A_{1}x + B_{1}y + C_{1}z + D_{1} = 0$ 和 $A_{2}x + B_{2}y + C_{2}z + D_{2} = 0$ ，那么直线 L 上的任一点的坐标应同时满足这两个平面的方程，即应满足方程组

$$
\left\{ \begin{array}{l} A _ {1} x + B _ {1} y + C _ {1} z + D _ {1} = 0, \\ A _ {2} x + B _ {2} y + C _ {2} z + D _ {2} = 0. \end{array} \right. \tag {4-1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/038a35e74ce1737d1d156c790e2e47c8316e373d02be4618218f1077a38bba0b.jpg)



图8-35


反过来,如果点 M 不在直线 L 上,那么它不可能同时在平面 $\Pi_{1}$ 和 $\Pi_{2}$ 上,所以它的坐标不满足方程组(4-1).因此,直线 L 可以用方程组(4-1)来表示.方程组(4-1)叫做空间直线的一般方程.

通过空间一直线 L 的平面有无限多个, 只要在这无限多个平面中任意选取两个,

把它们的方程联立起来,所得的方程组就表示空间直线 L.

# 二、空间直线的对称式方程与参数方程

如果一个非零向量平行于一条已知直线,那么这个向量就叫做这条直线的方向向量.

由于过空间一点可作而且只能作一条直线平行于一已知直线,所以当直线 L 上一点 $M_{0}(x_{0},y_{0},z_{0})$ 和它的一方向向量 $s=(m,n,p)$ 为已知时,直线 L 的位置就完全确定了.下面我们来建立这条直线的方程.

设点 $M(x,y,z)$ 是直线 $L$ 上的任一点，则向量 $\overrightarrow{M_0M}$ 与 $L$ 的方向向量 $s$ 平行（图8-36).所以两向量的对应坐标成比例，由于 $\overrightarrow{M_0M} = (x - x_0,y - y_0,z - z_0),s = (m,n,p)$ ，从而有

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/9482da9683fed726540de6335472d321a843549793e16b4bc4502103dea559a8.jpg)



图8-36


$$
\frac {x - x _ {0}}{m} = \frac {y - y _ {0}}{n} = \frac {z - z _ {0}}{p}. ^ {(1)} \tag {4-2}
$$

反过来,如果点 M 不在直线 L 上,那么由于 $\overrightarrow{M_{0}M}$ 与 s 不平行,这两向量的对应坐标就不成比例.因此方程组(4-2)就是直线 L 的方程,叫做直线的对称式方程或点向式方程.

直线的任一方向向量 s 的坐标 m, n 和 p 叫做这条直线的一组方向数, 而向量 s 的方向余弦叫做该直线的方向余弦.

由直线的对称式方程容易导出直线的参数方程.如设

$$
\frac {x - x _ {0}}{m} = \frac {y - y _ {0}}{n} = \frac {z - z _ {0}}{p} = t,
$$

则

$$
\left\{ \begin{array}{l} x = x _ {0} + m t, \\ y = y _ {0} + n t, \\ z = z _ {0} + p t. \end{array} \right. \tag {4-3}
$$

$$
\left\{ \begin{array}{l} x - x _ {0} = 0, \\ \frac {y - y _ {0}}{n} = \frac {z - z _ {0}}{p}; \end{array} \right.
$$

$$
\left\{ \begin{array}{l} x - x _ {0} = 0, \\ y - y _ {0} = 0. \end{array} \right.
$$

方程组(4-3)就是直线的参数方程.

例 1 用对称式方程及参数方程表示直线

$$
\left\{ \begin{array}{l} x + y + z + 1 = 0, \\ 2 x - y + 3 z + 4 = 0. \end{array} \right. \tag {4-4}
$$

解 先找出这条直线上的一点 $(x_0, y_0, z_0)$ . 例如, 可以取 $x_0 = 1$ , 代入方程组 (4-4), 得

$$
\left\{ \begin{array}{l} y _ {0} + z _ {0} = - 2, \\ y _ {0} - 3 z _ {0} = 6. \end{array} \right.
$$

解这个二元一次方程组,得

$$
y _ {0} = 0, \quad z _ {0} = - 2,
$$

即 $(1,0,-2)$ 是这条直线上的一点.

下面再找出这条直线的方向向量 s. 因为两平面的交线与这两平面的法向量 $n_{1}=(1,1,1)$ , $n_{2}=(2,-1,3)$ 都垂直, 所以可取

$$
s = \boldsymbol {n} _ {1} \times \boldsymbol {n} _ {2} = \left| \begin{array}{c c c} i & j & k \\ 1 & 1 & 1 \\ 2 & - 1 & 3 \end{array} \right| = 4 i - j - 3 k.
$$

因此,所给直线的对称式方程为

$$
\frac {x - 1}{4} = \frac {y}{- 1} = \frac {z + 2}{- 3}.
$$

令 $\frac{x-1}{4}=\frac{y}{-1}=\frac{z+2}{-3}=t$ ，得所给直线的参数方程为

$$
\left\{ \begin{array}{l} x = 1 + 4 t, \\ y = - t, \\ z = - 2 - 3 t. \end{array} \right.
$$

# 三、两直线的夹角

两直线的方向向量的夹角(通常指锐角或直角)叫做两直线的夹角.

设直线 $L_{1}$ 和 $L_{2}$ 的方向向量依次为 $s_1 = (m_1, n_1, p_1)$ 和 $s_2 = (m_2, n_2, p_2)$ ，则 $L_{1}$ 和 $L_{2}$ 的夹角 $\varphi$ 应是 $(\widehat{s_1, s_2})$ 和 $(- \widehat{s_1, s_2}) = \pi - (\widehat{s_1, s_2})$ 两者中的锐角或直角，因此 $\cos \varphi = |\cos (\widehat{s_1, s_2})|$ . 按两向量的夹角的余弦公式，直线 $L_{1}$ 和直线 $L_{2}$ 的夹角 $\varphi$ 可由

$$
\cos \varphi = \frac {\left| m _ {1} m _ {2} + n _ {1} n _ {2} + p _ {1} p _ {2} \right|}{\sqrt {m _ {1} ^ {2} + n _ {1} ^ {2} + p _ {1} ^ {2}} \sqrt {m _ {2} ^ {2} + n _ {2} ^ {2} + p _ {2} ^ {2}}} \tag {4-5}
$$

来确定.

从两向量垂直、平行的充分必要条件立即推得下列结论：

两直线 $L_{1}$ 和 $L_{2}$ 互相垂直相当于 $m_{1}m_{2}+n_{1}n_{2}+p_{1}p_{2}=0$ ;

两直线 $L_{1}$ 和 $L_{2}$ 互相平行或重合相当于 $\frac{m_{1}}{m_{2}} = \frac{n_{1}}{n_{2}} = \frac{p_{1}}{p_{2}}$ .

例2 求直线 $L_{1}:\frac{x - 1}{1} = \frac{y}{-4} = \frac{z + 3}{1}$ 和 $L_{2}:\frac{x}{2} = \frac{y + 2}{-2} = \frac{z}{-1}$ 的夹角.

解 直线 $L_{1}$ 的方向向量为 $s_{1}=(1,-4,1)$ ，直线 $L_{2}$ 的方向向量为 $s_{2}=(2,-2,-1)$ 。设直线 $L_{1}$ 和 $L_{2}$ 的夹角为 $\varphi$ ，则由公式(4-5)有

$$
\cos \varphi = \frac {\mid 1 \times 2 + (- 4) \times (- 2) + 1 \times (- 1) \mid}{\sqrt {1 ^ {2} + (- 4) ^ {2} + 1 ^ {2}} \sqrt {2 ^ {2} + (- 2) ^ {2} + (- 1) ^ {2}}} = \frac {1}{\sqrt {2}},
$$

所以

$$
\varphi = \frac {\pi}{4}.
$$

# 四、直线与平面的夹角

当直线与平面不垂直时, 直线和它在平面上的投影直线的夹角 $\varphi\left(0 \leqslant \varphi < \frac{\pi}{2}\right)$ 称为直线与平面的夹角 (图 8-37), 当直线与平面垂直时, 规定直线与平面的夹角为 $\frac{\pi}{2}$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/cb1fe480c95b4dc8f85ca0c2f6c9cf784a6ca328e71417d0ff09d1365cbd7c50.jpg)



图8-37


设直线的方向向量为 $s = (m, n, p)$ ，平面的法向量为 $n = (A, B, C)$ ，直线与平面的夹角为 $\varphi$ ，那么 $\varphi = \left|\frac{\pi}{2} - (\widehat{s, n})\right|$ ，因此 $\sin \varphi = |\cos (\widehat{s, n})|$ . 按两向量夹角余弦的坐标表示式，有

$$
\sin \varphi = \frac {\mid A m + B n + C p \mid}{\sqrt {A ^ {2} + B ^ {2} + C ^ {2}} \sqrt {m ^ {2} + n ^ {2} + p ^ {2}}}. \tag {4-6}
$$

因为直线与平面垂直相当于直线的方向向量与平面的法向量平行,所以,直线与平面垂直相当于

$$
\frac {A}{m} = \frac {B}{n} = \frac {C}{p}. \tag {4-7}
$$

因为直线与平面平行或直线在平面上相当于直线的方向向量与平面的法向量垂直,所以,直线与平面平行或直线在平面上相当于

$$
A m + B n + C p = 0. \tag {4-8}
$$

例 3 求过点 $(1,-2,4)$ 且与平面 $2x-3y+z-4=0$ 垂直的直线的方程.

解 因为所求直线垂直于已知平面,所以可以取已知平面的法向量(2,-3,1)作为所求直线的方向向量.由此可得所求直线的方程为

$$
\frac {x - 1}{2} = \frac {y + 2}{- 3} = \frac {z - 4}{1}.
$$

# 五、杂例

例 4 求与两平面 x-4z=3 和 2x-y-5z=1 的交线平行且过点 $(-3,2,5)$ 的直线的方程.

解法一 因为所求直线与两平面的交线平行,也就是直线的方向向量 s 一定同时与两平面的法向量 $n_{1}, n_{2}$ 垂直,所以可以取

$$
s = \pmb {n} _ {1} \times \pmb {n} _ {2} = \left| \begin{array}{c c c} \pmb {i} & \pmb {j} & \pmb {k} \\ 1 & 0 & - 4 \\ 2 & - 1 & - 5 \end{array} \right| = - (4 \pmb {i} + 3 \pmb {j} + \pmb {k}),
$$

因此所求直线的方程为

$$
\frac {x + 3}{4} = \frac {y - 2}{3} = \frac {z - 5}{1}.
$$

解法二 过点 $(-3,2,5)$ 且与平面x-4z=3平行的平面的方程为

$$
x - 4 z = - 2 3,
$$

过点 $(-3,2,5)$ 且与平面2x-y-5z=1平行的平面的方程为

$$
2 x - y - 5 z = - 3 3,
$$

所求直线为上述两平面的交线,故其方程为

$$
\left\{ \begin{array}{l} x - 4 z = - 2 3, \\ 2 x - y - 5 z = - 3 3. \end{array} \right.
$$

例5 求直线 $\frac{x - 2}{1} = \frac{y - 3}{1} = \frac{z - 4}{2}$ 与平面 $2x + y + z - 6 = 0$ 的交点.

解 所给直线的参数方程为

$$
x = 2 + t, \quad y = 3 + t, \quad z = 4 + 2 t,
$$

代入平面方程中,得

$$
2 (2 + t) + (3 + t) + (4 + 2 t) - 6 = 0.
$$

解以上方程, 得 t = -1. 把求得的 t 值代入直线的参数方程中, 即得所求交点的坐标为

$$
x = 1, \quad y = 2, \quad z = 2.
$$

例6 求过点(2,1,3)且与直线 $\frac{x + 1}{3} = \frac{y - 1}{2} = \frac{z}{-1}$ 垂直相交的直线的方程.

解 先作一平面过点(2,1,3)且垂直于已知直线,那么这平面的方程应为

$$
3 (x - 2) + 2 (y - 1) - (z - 3) = 0. \tag {4-9}
$$

再求已知直线与这平面的交点.已知直线的参数方程为

$$
x = - 1 + 3 t, \quad y = 1 + 2 t, \quad z = - t. \tag {4-10}
$$

把(4-10)代入(4-9)中,求得 $t=\frac{3}{7}$ , 从而求得交点为 $\left(\frac{2}{7},\frac{13}{7},-\frac{3}{7}\right)$ .

以点(2,1,3)为起点,点 $\left(\frac{2}{7},\frac{13}{7},-\frac{3}{7}\right)$ 为终点的向量

$$
\left(\frac {2}{7} - 2, \frac {1 3}{7} - 1, - \frac {3}{7} - 3\right) = - \frac {6}{7} (2, - 1, 4)
$$

是所求直线的一个方向向量,故所求直线的方程为

$$
\frac {x - 2}{2} = \frac {y - 1}{- 1} = \frac {z - 3}{4}.
$$

有时用平面束的方程解题比较方便,现在我们来介绍它的方程.

设直线 L 由方程组

$$
\left\{ \begin{array}{l} A _ {1} x + B _ {1} y + C _ {1} z + D _ {1} = 0, \\ A _ {2} x + B _ {2} y + C _ {2} z + D _ {2} = 0 \end{array} \right. \tag {4-11}
$$

所确定,其中系数 $A_{1},B_{1},C_{1}$ 与 $A_{2},B_{2},C_{2}$ 不成比例.我们建立三元一次方程

$$
A _ {1} x + B _ {1} y + C _ {1} z + D _ {1} + \lambda \left(A _ {2} x + B _ {2} y + C _ {2} z + D _ {2}\right) = 0, \tag {4-13}
$$

其中 $\lambda$ 为任意常数. 因为 $A_{1}, B_{1}, C_{1}$ 与 $A_{2}, B_{2}, C_{2}$ 不成比例, 所以对于任何一个 $\lambda$ 值, 方程 (4-13) 的系数: $A_{1} + \lambda A_{2}, B_{1} + \lambda B_{2}, C_{1} + \lambda C_{2}$ 不全为零, 从而方程 (4-13) 表示一个平面, 若一点在直线 L 上, 则点的坐标必同时满足方程 (4-11) 和 (4-12), 因而也满足方程 (4-13), 故方程 (4-13) 表示通过直线 L 的平面, 且对应于不同的 $\lambda$ 值, 方程 (4-13) 表示通过直线 L 的不同的平面. 反之, 通过直线 L 的任何平面 (除平面 (4-12) 外) 都包含在方程 (4-13) 所表示的一族平面内. 通过定直线的所有平面的全体称为平面束, 而方程 (4-13) 就作为通过直线 L 的平面束的方程 (实际上, 方程 (4-13) 表示缺少平面 (4-12) 的平面束).

例7 求直线 $\left\{ \begin{array}{l} x + y - z - 1 = 0, \\ x - y + z + 1 = 0 \end{array} \right.$ 在平面 $x + y + z = 0$ 上的投影直线的方程.

解 过直线 $\left\{\begin{aligned}x+y-z-1&=0,\\ x-y+z+1&=0\end{aligned}\right.$ 的平面束的方程为

$$
(x + y - z - 1) + \lambda (x - y + z + 1) = 0,
$$

即

$$
(1 + \lambda) x + (1 - \lambda) y + (- 1 + \lambda) z + (- 1 + \lambda) = 0, \tag {4-14}
$$

其中 $\lambda$ 为待定常数. 这平面与平面 $x+y+z=0$ 垂直的条件是

$$
(1 + \lambda) \cdot 1 + (1 - \lambda) \cdot 1 + (- 1 + \lambda) \cdot 1 = 0,
$$

即

$$
\lambda + 1 = 0,
$$

由此得

$$
\lambda = - 1.
$$

代入(4-14)式,得投影平面的方程为

$$
2 y - 2 z - 2 = 0,
$$

即

$$
y - z - 1 = 0.
$$

所以投影直线的方程为

$$
\left\{ \begin{array}{l} y - z - 1 = 0, \\ x + y + z = 0. \end{array} \right.
$$

# 习题8-4

1. 求过点(4,-1,3)且平行于直线 $\frac{x-3}{2}=\frac{y}{1}=\frac{z-1}{5}$ 的直线方程.

2. 求过两点 $M_{1}(3,-2,1)$ 和 $M_{2}(-1,0,2)$ 的直线方程.

3. 用对称式方程及参数方程表示直线 $\left\{ \begin{array}{l} x - y + z = 1, \\ 2x + y + z = 4. \end{array} \right.$ 

4. 求过点 $(2,0,-3)$ 且与直线 $\left\{\begin{aligned}x-2y+4z-7&=0,\\ 3x+5y-2z&=1&=0\end{aligned}\right.$ 垂直的平面方程.

5. 求直线 $\left\{\begin{aligned}5x-3y+3z-9=0,\\ 3x-2y+z-1=0\end{aligned}\right.$ 与直线 $\left\{\begin{aligned}2x+2y-z+23=0,\\ 3x+8y+z-18=0\end{aligned}\right.$ 的夹角的余弦.

6. 证明直线 $\left\{ \begin{array}{l} x + 2y - z = 7, \\ -2x + y + z = 7 \end{array} \right.$ 与直线 $\left\{ \begin{array}{l} 3x + 6y - 3z = 8, \\ 2x - y - z = 0 \end{array} \right.$ 平行.

7. 求过点 $(1,0,-2)$ 且与平面 $3x+4y-z+6=0$ 平行，又与直线 $\frac{x-3}{1}=\frac{y+2}{4}=\frac{z}{1}$ 垂直的直线方程.

8. 求过点 $(3,1,-2)$ 且通过直线 $\frac{x-4}{5}=\frac{y+3}{2}=\frac{z}{1}$ 的平面方程.

9. 求直线 $\left\{\begin{aligned} x+y+3z &= 0, \\ x-y-z &= 0 \end{aligned}\right.$ 与平面 $x-y-z+1=0$ 的夹角.

10. 试确定下列各组中的直线和平面间的关系：

(1) $\frac{x+3}{-2}=\frac{y+4}{-7}=\frac{z}{3}$ 和4x-2y-2z=3;

(2) $\frac{x}{3}=\frac{y}{-2}=\frac{z}{7}$ 和 $3x-2y+7z=8$ ;

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/0b8db5d4691632a399e0b934e6f979457293f0a7e0a8c9e03a07311d672d06c6.jpg)


例题精讲

8-3 

(3) $\frac{x-2}{3}=\frac{y+2}{1}=\frac{z-3}{-4}$ 和 $x+y+z=3.$ 

11. 求过点(1,2,1)且与两直线 $\left\{\begin{aligned}x+2y-z+1=0,\\ x-y+z-1=0\end{aligned}\right.$ 和 $\left\{\begin{aligned}2x-y+z=0,\\ x-y+z=0\end{aligned}\right.$ 都平行的平面的方程.

12. 求点 $(-1,2,0)$ 在平面 $x+2y-z+1=0$ 上的投影.

13. 求点 $P(3,-1,2)$ 到直线 $\left\{\begin{aligned} x+y-z+1&=0,\\ 2x-y+z-4&=0\end{aligned}\right.$ 的距离.

14. 设 $M_{0}$ 是直线 L 外一点, M 是直线 L 上任意一点, 且直线的方向向量为 s, 试证: 点 $M_{0}$ 到直线 L 的距离

$$
d = \frac {\mid \overrightarrow {M _ {0} M} \times s \mid}{\mid s \mid}.
$$

15. 求直线 $\left\{\begin{aligned}&2x-4y+z=0,\\ &3x-y-2z-9=0\end{aligned}\right.$ 在平面 $4x-y+z=1$ 上的投影直线的方程.

16. 画出下列各平面所围成的立体的图形：

(1) x=0, y=0, z=0, x=2, y=1, $3x+4y+2z-12=0$ ; 

(2) $x = 0, z = 0, x = 1, y = 2, z = \frac{y}{4}$ . 

# 第五节 曲面及其方程

# 一、曲面研究的基本问题

在空间解析几何中,关于曲面的研究有下列两个基本问题:

(1) 已知一曲面作为点的几何轨迹时, 建立这曲面的方程;

(2) 已知坐标 x, y 和 z 间的一个方程时, 研究这方程所表示的曲面的形状.

在第三节中关于建立一种最简单的曲面——平面方程的例子就属于基本问题(1)，以下是建立另一种特殊曲面——球面方程的例子.

例 1 建立球心在点 $M_{0}(x_{0},y_{0},z_{0})$ 、半径为 R 的球面的方程.

解 设 $M(x, y, z)$ 是球面上的任一点(图8-38)，则

$$
\mid M _ {0} M \mid = R.
$$

由于

$$
\mid M _ {0} M \mid = \sqrt {\left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} + \left(z - z _ {0}\right) ^ {2}},
$$

所以

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/9a2926a68b06c995ade1508461f8b18a7b6aac9d3cec867a849ed5b30a2af6cb.jpg)



图8-38


$$
\sqrt {\left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} + \left(z - z _ {0}\right) ^ {2}} = R,
$$

或

$$
\left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} + \left(z - z _ {0}\right) ^ {2} = R ^ {2}. \tag {5-1}
$$

这就是球面上的点的坐标所满足的方程. 而不在球面上的点的坐标都不满足这方程. 所以方程(5-1)就是以 $M_0(x_0, y_0, z_0)$ 为球心、 $R$ 为半径的球面方程.

如果球心在原点,那么 $x_{0}=y_{0}=z_{0}=0$ ,从而球面方程为

$$
x ^ {2} + y ^ {2} + z ^ {2} = R ^ {2}.
$$

下面举一个由已知方程研究它所表示的曲面的例子.

例 2 方程 $x^{2}+y^{2}+z^{2}-2x+4y=0$ 表示怎样的曲面？

解 通过配方,原方程可以改写成

$$
(x - 1) ^ {2} + (y + 2) ^ {2} + z ^ {2} = 5.
$$

与(5-1)式比较,就知道原方程表示球心在点 $M_{0}(1,-2,0)$ 、半径 $R=\sqrt{5}$ 的球面.

一般地,设有三元二次方程

$$
A x ^ {2} + A y ^ {2} + A z ^ {2} + D x + E y + F z + G = 0,
$$

这个方程的特点是缺 $xy, yz, zx$ 各项，而且平方项系数相同，只要将方程经过配方可以化成方程(5-1)的形式，则它的图形就是一个球面.

下一目中讨论旋转曲面,也是基本问题(1)的例子;而第三、四目中分别讨论柱面、二次曲面,则是基本问题(2)的例子.

# 二、旋转曲面

以一条平面曲线绕其平面上的一条直线旋转一周所成的曲面叫做旋转曲面,旋转曲线和定直线依次叫做旋转曲面的母线和轴.

设在 yOz 坐标面上有一已知曲线 C, 它的方程为

$$
f (y, z) = 0,
$$

把这曲线绕 z 轴旋转一周, 就得到一个以 z 轴为轴的旋转曲面(图 8-39). 它的方程可以求得如下:

设 $M_{1}(0, y_{1}, z_{1})$ 为曲线 $C$ 上的任一点，则有

$$
f \left(y _ {1}, z _ {1}\right) = 0. \tag {5-2}
$$

当曲线 C 绕 z 轴旋转时，点 $M_{1}$ 绕 z 轴转到另一点 $M(x,y,z)$ ，这时 $z=z_{1}$ 保持不变，且点 M 到 z 轴的距离

$$
d = \sqrt {x ^ {2} + y ^ {2}} = | y _ {1} |.
$$

将 $z_{1} = z, y_{1} = \pm \sqrt{x^{2} + y^{2}}$ 代入(5-2)式，就有

$$
f \left(\pm \sqrt {x ^ {2} + y ^ {2}}, z\right) = 0, \tag {5-3}
$$

这就是所求旋转曲面的方程.

由此可知,在曲线 C 的方程 $f(y,z)=0$ 中将 y 改成 $\pm\sqrt{x^{2}+y^{2}}$ , 便得曲线 C 绕 z 轴旋转所成的旋转曲面的方程.

同理,曲线 C 绕 y 轴旋转所成的旋转曲面的方程为

$$
f (y, \pm \sqrt {x ^ {2} + z ^ {2}}) = 0. \tag {5-4}
$$

例 3 直线 L 绕另一条与 L 相交的直线旋转一周, 所得旋转曲面叫做圆锥面. 两直线的交点叫做圆锥面的顶点, 两直线的夹角 $\alpha\left(0<\alpha<\frac{\pi}{2}\right)$ 叫做圆锥面的半顶角. 试建立顶点在坐标原点 O, 旋转轴为 z 轴, 半顶角为 $\alpha$ 的圆锥面 (图 8-40) 的方程.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/7756fa52ee4d68eaf138fe5ceb39bdf878b736d6bbe7025d671a2aa92e825688.jpg)



图8-39


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/e3058dfd58a081449a91e12db76348d6e6e55c9dc3fdca0e75c9c98c02eca39c.jpg)



图8-40


解 在 yOz 坐标面上, 直线 L 的方程为

$$
z = y \cot \alpha , \tag {5-5}
$$

因为旋转轴为 z 轴, 所以只要将方程(5-5)中的 y 改成 $\pm\sqrt{x^{2}+y^{2}}$ , 便得到这圆锥面的方程

$$
z = \pm \sqrt {x ^ {2} + y ^ {2}} \cot \alpha
$$

或

$$
z ^ {2} = a ^ {2} \left(x ^ {2} + y ^ {2}\right), \tag {5-6}
$$

其中 $a=\cot\alpha.$ 

显然,圆锥面上任一点 M 的坐标一定满足方程(5-6).如果点 M 不在圆锥面上,那么直线 OM 与 z 轴的夹角就不等于 $\alpha$ ,于是点 M 的坐标就不满足方程(5-6).

例 4 将 zOx 坐标面上的双曲线

$$
\frac {x ^ {2}}{a ^ {2}} - \frac {z ^ {2}}{c ^ {2}} = 1
$$

分别绕 z 轴和 x 轴旋转一周, 求所生成的旋转曲面的方程.

解 绕 z 轴旋转所成的旋转曲面叫做旋转单叶双曲面(图 8-41), 它的方程为

$$
\frac {x ^ {2} + y ^ {2}}{a ^ {2}} - \frac {z ^ {2}}{c ^ {2}} = 1.
$$

绕 $x$ 轴旋转所成的旋转曲面叫做旋转双叶双曲面（图8-42），它的方程为

$$
\frac {x ^ {2}}{a ^ {2}} - \frac {y ^ {2} + z ^ {2}}{c ^ {2}} = 1.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/f52c863153664d3a6faaa42cb08f01e231e0b711c74c8ddf73c8b8e46d7f729b.jpg)



图8-41


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/420cd1d7785bd765f559f54995a5b458270f41570c3cddb1e4851de2ec99a679.jpg)



图8-42


# 三、柱面

我们先分析一个具体的例子.

例5 方程 $x^{2} + y^{2} = R^{2}$ 表示怎样的曲面？

解 方程 $x^{2} + y^{2} = R^{2}$ 在 $xOy$ 面上表示圆心在原点 $O$ 、半径为 $R$ 的圆. 在空间直角坐标系中, 这方程不含竖坐标 $z$ , 即不论空间点的竖坐标 $z$ 怎样, 只要它的横坐标 $x$ 和纵坐标 $y$ 能满足这方程, 那么这些点就在这曲面上. 这就是说, 凡是通过 $xOy$ 面内圆 $x^{2} + y^{2} = R^{2}$ 上一点 $M(x, y, 0)$ , 且平行于 $z$ 轴的直线 $l$ 都在这曲面上, 因此, 这曲面可以看做是由平行于 $z$ 轴的直线 $l$ 沿 $xOy$ 面上的圆 $x^{2} + y^{2} = R^{2}$ 移动而形成的. 这曲面叫做圆柱面 (图 8-43), $xOy$ 面上的圆 $x^{2} + y^{2} = R^{2}$ 叫做它的准线, 这平行于 $z$ 轴的直线 $l$ 叫做它的母线.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/c587aac0e8ab65bda1ca0daa616ba168c324345ae00eb20186b0be6d39b7e891.jpg)



图8-43


一般地, 直线 L 沿定曲线 C 平行移动形成的轨迹叫做柱面, 定曲线 C 叫做柱面的准线, 动直线 L 叫做柱面的母线.

上面我们看到,不含 z 的方程 $x^{2}+y^{2}=R^{2}$ 在空间直角坐标系中表示圆柱面,它的母线平行于 z 轴,它的准线是 xOy 面上的圆 $x^{2}+y^{2}=R^{2}$ .

类似地,方程 $y^{2}=2x$ 表示母线平行于 z 轴的柱面,它的准线是 xOy 面上的抛物线

$y^{2}=2x$ ,该柱面叫做抛物柱面(图8-44).

又如, 方程 x-y=0 表示母线平行于 z 轴的柱面, 其准线是 xOy 面上的直线 x-y=0, 所以它是过 z 轴的平面(图 8-45).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/e466ea413f77ae542cdd5c6c5420bc3bdcf0e93937786e737019bc4776507739.jpg)



图8-44


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/b0f086c679afacf1cc3b75bde38447c2b94f44bf8a47e4fa802753e4bbcd15ed.jpg)



图8-45


一般地, 只含 x, y 而缺 z 的方程 $F(x, y) = 0$ 在空间直角坐标系中表示母线平行于 z 轴的柱面, 其准线是 xOy 面上的曲线 $C: F(x, y) = 0$ (图 8-46).

类似可知, 只含 x, z 而缺 y 的方程 $G(x, z) = 0$ 和只含 y, z 而缺 x 的方程 $H(y, z) = 0$ 分别表示母线平行于 y 轴和 x 轴的柱面.

例如, 方程 x-z=0 表示母线平行于 y 轴的柱面, 其准线是 zOx 面上的直线 x-z=0. 所以它是过 y 轴的平面(图 8-47).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/11b4a67b23aa1207c96f353b8f5d5b784acbb10dff0ea16bf64fe8384a084ca7.jpg)



图8-46


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/744bc6917bcb79f90e3346bf8951a5451f285564c407d45791869cbf27507460.jpg)



图8-47


# 四、二次曲面

与平面解析几何中规定的二次曲线相类似,我们把三元二次方程 $F(x,y,z)=0$ 所表示的曲面称为二次曲面,把平面称为一次曲面.

二次曲面有九种,适当选取空间直角坐标系,可得它们的标准方程.下面就九种二

次曲面的标准方程来讨论二次曲面的形状.

(1) 椭圆锥面 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=z^{2}$ 

以垂直于 $z$ 轴的平面 $z = t$ 截此曲面，当 $t = 0$ 时得一点 $(0,0,0)$ ；当 $t \neq 0$ 时，得平面 $z = t$ 上的椭圆

$$
\frac {x ^ {2}}{(a t) ^ {2}} + \frac {y ^ {2}}{(b t) ^ {2}} = 1.
$$

当 t 变化时, 上式表示一族长短轴比例不变的椭圆, 当 $\left|t\right|$ 从大到小并变为 0 时, 这族椭圆从大到小并缩为一点. 综合上述讨论, 可得椭圆锥面 (1) 的形状如图 8-48 所示.

平面 z=t 与曲面 $F(x,y,z)=0$ 的交线称为截痕. 通过综合截痕的变化来了解曲面形状的方法称为截痕法.

我们还可以用伸缩变形的方法来得出椭圆锥面(1)的形状.

先说明 $xOy$ 平面上的图形伸缩变形的方法. 在 $xOy$ 平面上, 把点 $M(x, y)$ 变为点 $M'(x, \lambda y)$ , 从而把点 $M$ 的轨迹 $C$ 变为点 $M'$ 的轨迹 $C'$ , 称为把图形 $C$ 沿 $y$ 轴方向伸缩 $\lambda$ 倍变成图形 $C'$ . 假如 $C$ 为曲线 $F(x, y) = 0$ , 点 $M(x_1, y_1) \in C$ , 点 $M$ 变为点 $M'(x_2, y_2)$ , 其中 $x_2 = x_1, y_2 = \lambda y_1$ , 即 $x_1 = x_2, y_1 = \frac{1}{\lambda} y_2$ , 因点 $M \in C$ , 有 $F(x_1, y_1) = 0$ , 故 $F\left(x_2, \frac{1}{\lambda} y_2\right) = 0$ , 因此点 $M'(x_2, y_2)$ 的轨迹 $C'$ 的方程为 $F\left(x, \frac{1}{\lambda} y\right) = 0$ . 例如把圆 $x^2 + y^2 = a^2$ 沿 $y$ 轴方向伸缩 $\frac{b}{a}$ 倍, 就变为椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ (图8-49).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/e6be46ee0c78d88acda125a4e3fa55269d4f2fbc197d70fc7c9443c2fe6ea173.jpg)



图8-48


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/87b3b4909555ec67c3ea363c34d19659f918b7b5b427ab59d7f3fb29baa5d777.jpg)



图8-49


类似地, 把空间图形沿 y 轴方向伸缩 $\frac{b}{a}$ 倍, 圆锥面 $\frac{x^{2}+y^{2}}{a^{2}}=z^{2}$ (图 8-40) 就变为椭圆锥面 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=z^{2}$ (图 8-48).

利用圆锥面(旋转曲面)的伸缩变形来得出椭圆锥面的形状,这种方法是研究曲面形状的一种较方便的方法.

(2) 椭球面 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}+\frac{z^{2}}{c^{2}}=1$ 

把 $zOx$ 面上的椭圆 $\frac{x^2}{a^2} +\frac{z^2}{c^2} = 1$ 绕 $z$ 轴旋转，所得曲面称为旋转椭球面，其方程为

$$
\frac {x ^ {2} + y ^ {2}}{a ^ {2}} + \frac {z ^ {2}}{c ^ {2}} = 1.
$$

再把旋转椭球面沿 y 轴方向伸缩 $\frac{b}{a}$ 倍, 便得椭球面(2)的形状如图 8-50 所示.

当 $a = b = c$ 时，椭球面(2)成为 $x^{2} + y^{2} + z^{2} = a^{2}$ ，这是球心在原点、半径为 $a$ 的球面。显然，球面是旋转椭球面的特殊情形，旋转椭球面是椭球面的特殊情形。把球面 $x^{2} + y^{2} + z^{2} = a^{2}$ 沿 $z$ 轴方向伸缩 $\frac{c}{a}$ 倍，即得旋转椭球面 $\frac{x^2 + y^2}{a^2} + \frac{z^2}{c^2} = 1$ ；再沿 $y$ 轴方向伸缩 $\frac{b}{a}$ 倍，即得椭球面(2)。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/8b1e848f215e19dd83666dfc3b3db64cfb7d0eff02721a4bb28a13a1b3c0e438.jpg)



图8-50


(3) 单叶双曲面 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}-\frac{z^{2}}{c^{2}}=1$ 

把 $zOx$ 面上的双曲线 $\frac{x^2}{a^2} -\frac{z^2}{c^2} = 1$ 绕 $z$ 轴旋转，得旋转单叶双曲面 $\frac{x^2 + y^2}{a^2} -\frac{z^2}{c^2} = 1$ （图8-41).把此旋转曲面沿 $y$ 轴方向伸缩 $\frac{b}{a}$ 倍，即得单叶双曲面(3).

(4) 双叶双曲面 $\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} - \frac{z^{2}}{c^{2}} = 1$ 

把 $zOx$ 面上的双曲线 $\frac{x^2}{a^2} -\frac{z^2}{c^2} = 1$ 绕 $x$ 轴旋转，得旋转双叶双曲面 $\frac{x^2}{a^2} -\frac{y^2 + z^2}{c^2} = 1$ （图8-42），把此旋转曲面沿 $y$ 轴方向伸缩 $\frac{b}{c}$ 倍，即得双叶双曲面(4).

(5) 椭圆抛物面 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=z$ 

把 $zOx$ 面上的抛物线 $\frac{x^2}{a^2} = z$ 绕 $z$ 轴旋转, 所得曲面叫做旋转抛物面, 如图 8-51 所示. 把此旋转曲面沿 $y$ 轴方向伸缩 $\frac{b}{a}$ 倍, 即得椭圆抛物面 (5).

(6) 双曲抛物面 $\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = z$ 

双曲抛物面又称马鞍面,我们用截痕法来讨论它的形状.

用平面 $x = t$ 截此曲面，所得截痕 $l$ 为平面 $x = t$ 上的抛物线

$$
- \frac {y ^ {2}}{b ^ {2}} = z - \frac {t ^ {2}}{a ^ {2}},
$$

此抛物线开口朝下,其顶点坐标为

$$
x = t, \quad y = 0, \quad z = \frac {t ^ {2}}{a ^ {2}}.
$$

当 $t$ 变化时， $l$ 的形状不变，位置只作平移，而 $l$ 的顶点的轨迹 $L$ 为平面 $y = 0$ 上的抛物线

$$
z = \frac {x ^ {2}}{a ^ {2}}.
$$

因此,以 l 为母线,L 为准线,母线 l 的顶点在准线 L 上滑动,且母线作平行移动,这样得到的曲面便是双曲抛物面(6),如图 8-52 所示.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/1c8053b3f7ffd3301dc7b627ac09383f2ce6f04b3f29e38be80f3753b6a6688d.jpg)



图8-51


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/0fe78f5894af7bd27b8b4bae63c92f25312bc8cea73edce31965173ac38bf19a.jpg)



图8-52


还有三种二次曲面是以三种二次曲线为准线的柱面

$$
\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} = 1, \quad \frac {x ^ {2}}{a ^ {2}} - \frac {y ^ {2}}{b ^ {2}} = 1, \quad x ^ {2} = a y,
$$

依次称为椭圆柱面、双曲柱面、抛物柱面. 柱面的形状在第三目中已经讨论过, 这里不再赘述.

# 习题8-5

1. 一球面过原点及 $A(4,0,0), B(1,3,0)$ 和 $C(0,0,-4)$ 三点，求球面的方程及球心的坐标和半径.

2. 已知一球面的球心在点 $P_{0}(3,-5,2)$ 且与平面 $\Pi:2x-y+3z+9=0$ 相切，求该球面方程.

3. 方程 $x^{2}+y^{2}+z^{2}-2x+4y+2z=0$ 表示什么曲面？

4. 求与坐标原点 O 及点 $(2,3,4)$ 的距离之比为 1:2 的点的全体所组成的曲面的方程, 它表示怎样的曲面?

5. 将 zOx 坐标面上的抛物线 $z^{2}=5x$ 绕 x 轴旋转一周, 求所生成的旋转曲面的方程.

6. 将 $zOx$ 坐标面上的圆 $x^{2} + z^{2} = 9$ 绕 $z$ 轴旋转一周, 求所生成的旋转曲面的方程.

7. 将 $xOy$ 坐标面上的双曲线 $4x^{2} - 9y^{2} = 36$ 分别绕 $x$ 轴及 $y$ 轴旋转一周, 求所生成的旋转曲面的方程.

8. 画出下列各方程所表示的曲面：

(1) $\left(x-\frac{a}{2}\right)^{2}+y^{2}=\left(\frac{a}{2}\right)^{2};$ 

(2) $-\frac{x^{2}}{4}+\frac{y^{2}}{9}=1;$ 

(3) $\frac{x^2}{9} + \frac{z^2}{4} = 1$ ; 

(4) $y^{2}-z=0;$ 

(5) $z = 2 - x^{2}$ . 

9. 指出下列方程在平面解析几何中和在空间解析几何中分别表示什么图形：

(1) $x = 2$ ; 

(2) $y = x + 1$ ; 

(3) $x^{2} + y^{2} = 4$ 

(4) $x^{2} - y^{2} = 1$ . 

10. 说明下列旋转曲面是怎样形成的：

(1) $\frac{x^{2}}{4}+\frac{y^{2}}{9}+\frac{z^{2}}{9}=1;$ 

(2) $x^{2} - \frac{y^{2}}{4} + z^{2} = 1$ ; 

(3) $x^{2} - y^{2} - z^{2} = 1$ 

(4) $(z - a)^{2} = x^{2} + y^{2}$ . 

11. 画出下列方程所表示的曲面：

(1) $4x^{2}+y^{2}-z^{2}=4;$ 

(2) $x^{2} - y^{2} - 4z^{2} = 4$ 

(3) $\frac{z}{3}=\frac{x^{2}}{4}+\frac{y^{2}}{9}.$ 

12. 画出下列各曲面所围立体的图形：

(1) z=0, z=3, x-y=0, $x-\sqrt{3}y=0$ , $x^{2}+y^{2}=1$ (在第Ⅰ卦限内);

(2) $x = 0, y = 0, z = 0, x^2 + y^2 = R^2, y^2 + z^2 = R^2$ （在第I卦限内）.

# 第六节 空间曲线及其方程

# 一、空间曲线的一般方程

在第三节中,我们已经知道空间曲线可以看做两个曲面的交线.设

$$
F (x, y, z) = 0 \quad {\text {和}} \quad G (x, y, z) = 0
$$

是两个曲面的方程,则方程组

$$
\left\{ \begin{array}{l} F (x, y, z) = 0, \\ G (x, y, z) = 0. \end{array} \right. \tag {6-1}
$$

就是这两个曲面的交线 C 的方程, 方程组(6-1)也叫做空间曲线 C 的一般方程.

例1 方程组 $\left\{ \begin{array}{l} x^{2} + y^{2} = 1, \\ 2x + 3z = 6 \end{array} \right.$ 表示怎样的曲线？

解 方程组中第一个方程表示母线平行于 $z$ 轴的圆柱面, 其准线是 $xOy$ 面上的圆, 圆心在原点 $O$ , 半径为 1. 方程组中第二个方程表示一个母线平行于 $y$ 轴的柱面, 由于它的准线是 $zOx$ 面上的直线, 因此它是一个平面. 方程组就表示上述平面与圆柱面的交线, 如图 8-53 所示.

例2 方程组 $\left\{ \begin{array}{l} z = \sqrt{a^2 - x^2 - y^2}, \\ \left(x - \frac{a}{2}\right)^2 + y^2 = \left(\frac{a}{2}\right)^2 \end{array} \right.$ 表示怎样的曲线？

解 方程组中第一个方程表示球心在坐标原点 $O$ ，半径为 $a$ 的上半球面。第二个方程表示母线平行于 $z$ 轴的圆柱面，它的准线是 $xOy$ 面上的圆，这圆的圆心在点 $\left(\frac{a}{2}, 0\right)$ ，半径为 $\frac{a}{2}$ 。方程组就表示上述半球面与圆柱面的交线，如图8-54所示。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/4bce006dc3fdd599fab44c52d91a46c16c8fc737cc83322dd51e6b8d0ff06962.jpg)



图8-53


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/965aea0e9f23ff3239149c4ae717d909cd702d01c70e4ca45be6af9d4783138d.jpg)



图8-54


# 二、空间曲线的参数方程

空间曲线 $C$ 的方程除了一般方程之外, 也可以用参数形式表示, 只要将 $C$ 上动点的坐标 $x, y$ 和 $z$ 表示为参数 $t$ 的函数

$$
\left\{ \begin{array}{l} x = x (t), \\ y = y (t), \\ z = z (t). \end{array} \right. \tag {6-2}
$$

当给定 $t=t_{1}$ 时, 就得到曲线 C 上的一个点 $(x_{1}, y_{1}, z_{1})$ ; 随着 t 的变动便可得曲线 C 上的全部点. 方程组 (6-2) 叫做空间曲线的参数方程.

例 3 如果空间一点 M 在圆柱面 $x^{2}+y^{2}=a^{2}$ 上以角速度 $\omega$ 绕 z 轴旋转, 同时又以线速度 v 沿平行于 z 轴的正方向上升(其中 $\omega$ 和 v 都是常数), 那么点 M 构成的图形叫做螺旋线. 试建立其参数方程.

解 取时间 t 为参数. 设当 t=0 时, 动点位于 x 轴上的一点 $A(a,0,0)$ 处. 经过时间 t, 动点由 A 运动到 $M(x,y,z)$ (图 8-55). 记 M 在 xOy 面上的投影为 $M'$ , $M'$ 的坐标为 $(x, y, 0)$ . 由于动点在圆柱面上以角速度 $\omega$ 绕 $z$ 轴旋转, 所以经过时间 $t$ , $\angle AOM' = \omega t$ . 从而

$$
x = \left| O M ^ {\prime} \right| \cos \angle A O M ^ {\prime} = a \cos \omega t,
$$

$$
y = \mid O M ^ {\prime} \mid \sin \angle A O M ^ {\prime} = a \sin \omega t.
$$

由于动点同时以线速度 v 沿平行于 z 轴的正方向上升，所以

$$
z = M ^ {\prime} M = v t.
$$

因此螺旋线的参数方程为

$$
\left\{ \begin{array}{l} x = a \cos \omega t, \\ y = a \sin \omega t, \\ z = v t. \end{array} \right.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/d121b63a676965d0a692f73386cd47d0a413613cf1f6156cfe2dbc82e3abcf9d.jpg)



图8-55


也可以用其他变量作参数.例如令 $\theta = \omega t$ ，则螺旋线的参数方程可写为

$$
\left\{ \begin{array}{l} x = a \cos \theta , \\ y = a \sin \theta , \\ z = b \theta . \end{array} \right.
$$

这里 $b = \frac{v}{\omega}$ ，而参数为 $\theta$ 

螺旋线是实践中常用的曲线.例如,平头螺丝钉的外缘曲线就是螺旋线.当我们拧紧平头螺丝钉时,它的外缘曲线上的任一点M,一方面绕螺丝钉的轴旋转,另一方面又沿平行于轴线的方向前进,点M就走出一段螺旋线.

螺旋线有一个重要性质: 当 $\theta$ 从 $\theta_{0}$ 变到 $\theta_{0} + \alpha$ 时, z 由 $b\theta_{0}$ 变到 $b\theta_{0} + b\alpha$ . 这说明当 $OM'$ 转过角 $\alpha$ 时, 点 M 沿螺旋线上升了高度 $b\alpha$ , 即上升的高度与 $OM'$ 转过的角度成正比. 特别是当 $OM'$ 转过一周, 即 $\alpha = 2\pi$ 时, 点 M 就上升固定的高度 $h = 2\pi b$ . 这个高度 $h = 2\pi b$ 在工程技术上叫做螺距.

* 曲面的参数方程

下面顺便介绍一下曲面的参数方程. 曲面的参数方程通常是含两个参数的方程, 形如

$$
\left\{ \begin{array}{l} x = x (s, t), \\ y = y (s, t), \\ z = z (s, t). \end{array} \right. \tag {6-3}
$$

例如空间曲线 $\Gamma$ 

$$
\left\{ \begin{array}{l l} x = \varphi (t), \\ y = \psi (t), & (\alpha \leqslant t \leqslant \beta) \\ z = \omega (t) \end{array} \right.
$$

绕 z 轴旋转,所得旋转曲面的方程为

$$
\left\{ \begin{array}{l l} x = \sqrt {\left[ \varphi (t) \right] ^ {2} + \left[ \psi (t) \right] ^ {2}} \cos \theta , \\ y = \sqrt {\left[ \varphi (t) \right] ^ {2} + \left[ \psi (t) \right] ^ {2}} \sin \theta , & \alpha \leqslant t \leqslant \beta , 0 \leqslant \theta \leqslant 2 \pi . \\ z = \omega (t), \end{array} \right. \tag {6-4}
$$

这是因为, 固定一个 $t$ , 得 $\Gamma$ 上一点 $M_{1}(\varphi(t), \psi(t), \omega(t))$ , 点 $M_{1}$ 绕 $z$ 轴旋转, 得空间的一个圆, 该圆在平面 $z = \omega(t)$ 上, 其半径为点 $M_{1}$ 到 $z$ 轴的距离 $\sqrt{[\varphi(t)]^2 + [\psi(t)]^2}$ , 因此, 固定 $t$ 的方程 (6-4) 就是该圆的参数方程. 再令 $t$ 在 $[\alpha, \beta]$ 内变动, 方程 (6-4) 便是旋转曲面的方程.

例如直线

$$
\left\{ \begin{array}{l} x = 1, \\ y = t, \\ z = 2 t \end{array} \right.
$$

绕 z 轴旋转所得旋转曲面(图 8-56)的方程为

$$
\left\{ \begin{array}{l} x = \sqrt {1 + t ^ {2}} \cos \theta , \\ y = \sqrt {1 + t ^ {2}} \sin \theta , \\ z = 2 t \end{array} \right.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/67af8e94ba267e95917273a22bde395eda0dab4f2f2af0a0c4c28f389b26052f.jpg)



图8-56


（上式消去 $t$ 和 $\theta$ ，得曲面的直角坐标方程为 $x^{2} + y^{2} = 1 + \frac{z^{2}}{4}$ 

又如球面 $x^{2} + y^{2} + z^{2} = a^{2}$ 可看成 $zOx$ 面上的半圆周

$$
\left\{ \begin{array}{l l} x = a \sin \varphi , \\ y = 0, & 0 \leqslant \varphi \leqslant \pi \\ z = a \cos \varphi , \end{array} \right.
$$

绕 z 轴旋转所得(图 8-57)，故球面方程为

$$
\left\{ \begin{array}{l l} x = a \sin \varphi \cos \theta , \\ y = a \sin \varphi \sin \theta , & 0 \leqslant \varphi \leqslant \pi , 0 \leqslant \theta \leqslant 2 \pi . \\ z = a \cos \varphi , \end{array} \right.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/89fdc48687812dcd327b3f5b6ba5aeb61011986cefb934602368a4f2729f7748.jpg)



图8-57


# 三、空间曲线在坐标面上的投影

设空间曲线 C 的一般方程为 $(6-1)$ ，现在来研究由方程组 $(6-1)$ 消去变量 z 后（如果可能的话）所得的方程

$$
H (x, y) = 0. \tag {6-5}
$$

由于方程(6-5)是由方程组(6-1)消去z后所得的结果,因此当x,y和z满足方程组(6-1)时,前两个坐标x,y必定满足方程(6-5),这说明曲线C上的所有点都在

由方程(6-5)所表示的曲面上.

由上节知道,方程(6-5)表示一个母线平行于z轴的柱面.由上面的讨论可知,这柱面必定包含曲线C.以曲线C为准线、母线平行于z轴(即垂直于xOy面)的柱面叫做曲线C关于xOy面的投影柱面,投影柱面与xOy面的交线叫做空间曲线C在xOy面上的投影曲线,或简称投影.因此,方程(6-5)所表示的柱面必定包含投影柱面,而方程

$$
\left\{ \begin{array}{l} H (x, y) = 0, \\ z = 0 \end{array} \right.
$$

所表示的曲线必定包含空间曲线 C 在 xOy 面上的投影.

同理, 消去方程组(6-1)中的变量 x 或变量 y, 再分别和 x=0 或 y=0 联立, 我们就可得到包含曲线 C 在 yOz 面或 zOx 面上的投影的曲线方程:

$$
\left\{ \begin{array}{l l} {R (y, z) = 0,} \\ {x = 0,} \end{array} \right. \quad \text {或} \quad \left\{ \begin{array}{l l} {T (x, z) = 0,} \\ {y = 0.} \end{array} \right.
$$

例4 已知两球面的方程为

$$
x ^ {2} + y ^ {2} + z ^ {2} = 1 \tag {6-6}
$$

和

$$
x ^ {2} + (y - 1) ^ {2} + (z - 1) ^ {2} = 1, \tag {6-7}
$$

求它们的交线 C 在 xOy 面上的投影的方程.

解 先求包含交线 $C$ 而母线平行于 $z$ 轴的柱面方程. 因此要由方程(6-6)、(6-7)消去 $z$ , 为此可先从(6-6)式减去(6-7)式并化简, 得到

$$
y + z = 1.
$$

再以 $z = 1 - y$ 代入方程(6-6)或(6-7)即得所求的柱面方程为

$$
x ^ {2} + 2 y ^ {2} - 2 y = 0.
$$

容易看出,这就是交线 C 关于 xOy 面的投影柱面方程,于是两球面的交线在 xOy 面上的投影的方程是

$$
\left\{ \begin{array}{l} x ^ {2} + 2 y ^ {2} - 2 y = 0, \\ z = 0. \end{array} \right.
$$

在重积分和曲面积分的计算中,往往需要确定一个立体或曲面在坐标面上的投影,这时要利用投影柱面和投影曲线.

例5 设一个立体由上半球面 $z = \sqrt{4 - x^2 - y^2}$ 和锥面 $z = \sqrt{3(x^2 + y^2)}$ 所围成（图8-58），求它在 $xOy$ 面上的投影.

解 半球面和锥面的交线为

$$
C: \left\{ \begin{array}{l} z = \sqrt {4 - x ^ {2} - y ^ {2}}, \\ z = \sqrt {3 (x ^ {2} + y ^ {2})}. \end{array} \right.
$$

由上列方程组消去 $z$ ，得到 $x^{2} + y^{2} = 1.$ 这是一个母线平行于 $z$ 轴的圆柱面，容易看出，这恰好是交线 $C$ 关于 $xOy$ 面的投影柱面，因此交线 $C$ 在 $xOy$ 面上的投影曲线为

$$
\left\{ \begin{array}{l} x ^ {2} + y ^ {2} = 1, \\ z = 0. \end{array} \right.
$$

这是 $xOy$ 面上的一个圆, 于是所求立体在 $xOy$ 面上的投影, 就是该圆在 $xOy$ 面上所围的部分

$$
x ^ {2} + y ^ {2} \leqslant 1.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/9c3830081706c13467e9aee859d0e1f20b26258c4e40ed318325afe166853cb3.jpg)



图8-58


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/d449145c46b446009c75c8eb2637818c670522f8603f787526a7315b3890bfb2.jpg)


# 习题8-6

1. 画出下列曲线在第Ⅰ卦限内的图形：

(1) $\left\{\begin{aligned}x&=1,\\ y&=2;\end{aligned}\right.$ 

(2) $\left\{ \begin{array}{l} z = \sqrt{4 - x^2 - y^2}, \\ x - y = 0; \end{array} \right.$ 

(3) $\left\{ \begin{array}{l} x^{2} + y^{2} = a^{2}, \\ x^{2} + z^{2} = a^{2}. \end{array} \right.$ 

2. 指出下列方程组在平面解析几何中与在空间解析几何中分别表示什么图形：

(1) $\left\{ \begin{array}{l} y = 5x + 1, \\ y = 2x - 3; \end{array} \right.$ 

(2) $\left\{\begin{aligned}\frac{x^{2}}{4}+\frac{y^{2}}{9}&=1,\\ y&=3.\end{aligned}\right.$ 

3. 分别求母线平行于 $x$ 轴及 $y$ 轴而且通过曲线 $\left\{ \begin{array}{l} 2x^{2} + y^{2} + z^{2} = 16, \\ x^{2} + z^{2} - y^{2} = 0 \end{array} \right.$ 的柱面方程.

4. 求下列两曲面的交线在 $xOy$ 面上的投影的方程：

(1) 球面 $x^{2}+y^{2}+z^{2}=9$ 与平面 $x+z=1$ ;

(2) 椭球面 $x^{2}+y^{2}+4z^{2}=1$ 与圆锥面 $z^{2}=x^{2}+y^{2}$ .

5. 将下列曲线的一般方程化为参数方程：

(1) $\left\{ \begin{array}{l} x^{2} + y^{2} + z^{2} = 9, \\ y = x; \end{array} \right.$ 

(2) $\left\{ \begin{array}{l} (x - 1)^2 + y^2 + (z + 1)^2 = 4, \\ z = 0. \end{array} \right.$ 

6. 求螺旋线 $\left\{\begin{aligned} x &= a \cos \theta, \\ y &= a \sin \theta, \\ z &= b \theta \end{aligned}\right.$ 在三个坐标面上的投影曲线的直角坐标方程.

7. 求上半球 $0 \leqslant z \leqslant \sqrt{a^2 - x^2 - y^2}$ 与圆柱体 $x^2 + y^2 \leqslant ax (a > 0)$ 的公共部分在 $xOy$ 面和 $zOx$ 面上的投影.

8. 求旋转抛物面 $z = x^{2} + y^{2}$ ( $0 \leqslant z \leqslant 4$ ) 在三坐标面上的投影.

# 总习题八

1. 填空：

（1）设在坐标系 $[O;i,j,k]$ 中点A和点M的坐标依次为 $(x_{0},y_{0},z_{0})$ 和 $(x,y,z)$ ，则在 $[A;i,j,k]$ 坐标系中，点M的坐标为____，向量 $\overrightarrow{OM}$ 的坐标为____；

(2) 设数 $\lambda_{1}, \lambda_{2}, \lambda_{3}$ 不全为 0，使 $\lambda_{1}a + \lambda_{2}b + \lambda_{3}c = 0$ ，则 a, b, c 三个向量是 ____ 的；

(3) 设 $a=(2,1,2)$ , $b=(4,-1,10)$ , $c=b-\lambda a$ , 且 $a \perp c$ , 则 $\lambda=$ ____;

(4) 设 $\left|a\right|=3,\left|b\right|=4,\left|c\right|=5$ , 且满足 $a+b+c=0$ , 则 $\left|a\times b+b\times c+c\times a\right|=$ ____.

2. 下列两题中给出了四个结论,从中选出一个正确的结论:

（1）设直线 L 的方程为 $\left\{\begin{aligned}x-y+z=1,\\ 2x+y+z=4,\end{aligned}\right.$ 则 L 的参数方程为（ ）；

(A) $\left\{ \begin{array}{l} x = 1 - 2t, \\ y = 1 + t, \\ z = 1 + 3t \end{array} \right.$ 

(B) $\left\{ \begin{array}{l} x = 1 - 2t, \\ y = -1 + t, \\ z = 1 + 3t \end{array} \right.$ 

(C) $\left\{ \begin{array}{l} x = 1 - 2t, \\ y = 1 - t, \\ z = 1 + 3t \end{array} \right.$ 

(D) $\left\{ \begin{array}{l} x = 1 - 2t, \\ y = -1 - t, \\ z = 1 + 3t \end{array} \right.$ 

(2) 下列结论中, 错误的是().

(A) $z+2x^{2}+y^{2}=0$ 表示椭圆抛物面

(B) $x^{2} + 2y^{2} = 1 + 3z^{2}$ 表示双叶双曲面

(C) $x^{2}+y^{2}-(z-1)^{2}=0$ 表示圆锥面

(D) $y^{2}=5x$ 表示抛物柱面

3. 在 y 轴上求与点 A(1, -3, 7) 和点 B(5, 7, -5) 等距离的点.

4. 已知 $\triangle ABC$ 的顶点为 $A(3,2,-1), B(5,-4,7)$ 和 $C(-1,1,2)$ ，求从顶点 $C$ 所引中线的长度.

5. 设 $\triangle ABC$ 的三边 $\overrightarrow{BC} = a, \overrightarrow{CA} = b, \overrightarrow{AB} = c$ , 三边中点依次为 $D, E, F$ , 试用向量 $a, b, c$ 表示 $\overrightarrow{AD}, \overrightarrow{BE}, \overrightarrow{CF}$ , 并证明

$$
\overrightarrow {A D} + \overrightarrow {B E} + \overrightarrow {C F} = 0.
$$

6. 试用向量证明: 梯形两腰中点的连线平行于底边, 且其长度等于上、下两底边长度之和的一半.

7. 设 $\left|a+b\right|=\left|a-b\right|$ , $a=(3,-5,8)$ , $b=(-1,1,z)$ , 求 z.

8. 设 $\left|a\right|=\sqrt{3}$ , $\left|b\right|=1$ , $(\widehat{a,b})=\frac{\pi}{6}$ , 求向量 $a+b$ 与 a-b 的夹角.

9. 设 $(a+3b)\perp(7a-5b),(a-4b)\perp(7a-2b)$ ，求 $(\widehat{a,b})$ .

10. 设向量 $a = (1, -2, 2), b = (-2, 1, 2)$ , 若存在向量 $c$ , 使 $a \times c = b$ , 试求向量 $c$ ; 若向量 $c$ 不止一个, 试找出模最小的那个 $c$ .

11. 设 $|a| = 4, |b| = 3, (\widehat{a,b}) = \frac{\pi}{6}$ , 求以 $a + 2b$ 和 $a - 3b$ 为边的平行四边形的面积.

12. 设 $a = (2, -3, 1)$ , $b = (1, -2, 3)$ , $c = (2, 1, 2)$ , 向量 $r$ 满足 $r \perp a$ , $r \perp b$ , $\operatorname{Prj}_c r = 14$ , 求 $r$ .

13. 设 $a = (-1, 3, 2), b = (2, -3, -4), c = (-3, 12, 6)$ ，证明三向量 $a, b, c$ 共面，并用 $a$ 和 $b$ 表

示c.

14. 已知动点 $M(x, y, z)$ 到 $xOy$ 面的距离与点 $M$ 到点 $(1, -1, 2)$ 的距离相等, 求点 $M$ 的轨迹的方程.

15. 指出下列旋转曲面的一条母线和旋转轴：

(1) $z = 2(x^{2} + y^{2})$ 

(2) $\frac{x^{2}}{36}+\frac{y^{2}}{9}+\frac{z^{2}}{36}=1;$ 

(3) $z^2 = 3(x^2 + y^2)$ ; 

(4) $x^{2}-\frac{y^{2}}{4}-\frac{z^{2}}{4}=1.$ 

16. 求通过点 $A(3,0,0)$ 和 $B(0,0,1)$ 且与 $xOy$ 面成 $\frac{\pi}{3}$ 角的平面的方程.

17. 设一平面垂直于平面 $z = 0$ ，并通过从点 $(1, -1, 1)$ 到直线 $\left\{ \begin{array}{l} y - z + 1 = 0, \\ x = 0 \end{array} \right.$ 的垂线，求此平面的方程.

18. 求过点 $(-1,0,4)$ , 且平行于平面 $3x - 4y + z - 10 = 0$ , 又与直线 $\frac{x + 1}{1} = \frac{y - 3}{1} = \frac{z}{2}$ 相交的直线的方程.

19. 一直线 l 过点 A(-3,5,-9) 且与两直线 $l_{1}:\left\{\begin{aligned}y=3x+5,\\ z=2x-3,\end{aligned}\right.$ $l_{2}:\left\{\begin{aligned}y=4x-7,\\ z=5x+10\end{aligned}\right.$ 相交，求此直线方程.

20. 已知点 $A(1,0,0)$ 及点 $B(0,2,1)$ , 试在 $z$ 轴上求一点 $C$ , 使 $\triangle ABC$ 的面积最小.

21. 求曲线 $\left\{\begin{aligned}z&=2-x^{2}-y^{2},\\ z&(=x-1)^{2}+(y-1)^{2}\end{aligned}\right.$ 在三个坐标面上的投影曲线的方程.

22. 求锥面 $z = \sqrt{x^2 + y^2}$ 与柱面 $z^2 = 2x$ 所围立体在三个坐标面上的投影.

23. 画出下列各曲面所围立体的图形：

（1）抛物柱面 $2y^{2}=x$ ，平面 z=0 及 $\frac{x}{4}+\frac{y}{2}+\frac{z}{2}=1$ ;

(2) 抛物柱面 $x^{2}=1-z$ ，平面 y=0, z=0 及 $x+y=1$ ;

(3) 圆锥面 $z = \sqrt{x^{2} + y^{2}}$ 及旋转抛物面 $z = 2 - x^{2} - y^{2}$ ;

(4) 旋转抛物面 $x^{2} + y^{2} = z$ ，柱面 $y^{2} = x$ ，平面 z = 0 及 x = 1。


第八章释疑解难


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/b0dbafce0ccdbe6d13cb29a34a1ad10e0e3c59f7b8878965557b5a1c56ddf5c0.jpg)



第八章例题精讲


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/777c73cd742300c86d93b44994be404d5f885fb9da63ca71ee478efb09880510.jpg)


# 第九章

# 多元函数微分法及其应用

上册中我们讨论的函数都只有一个自变量,这种函数叫做一元函数.但在很多实际问题中往往牵涉多方面的因素,反映到数学上,就是一个变量依赖于多个变量的情形.这就提出了多元函数以及多元函数的微分和积分问题.本章将在一元函数微分学的基础上,讨论多元函数的微分法及其应用.讨论中我们以二元函数为主,因为从一元函数到二元函数会产生新的问题,而从二元函数到二元以上的多元函数则可以类推.

# 第一节 多元函数的基本概念

# 一、平面点集 $^{*}$ n 维空间

在讨论一元函数时,一些概念、理论和方法都是基于 $\mathbf{R}^{1}$ 中的点集、两点间的距离、区间和邻域等概念.为了将一元函数微积分推广到多元的情形,首先需要将上述一些概念加以推广,同时还需涉及一些其他概念.为此先引入平面点集的一些基本概念,将有关概念从 $\mathbf{R}^{1}$ 中的情形推广到 $\mathbf{R}^{2}$ 中;然后引入 $n$ 维空间,以便推广到一般的 $\mathbf{R}^{n}$ 中.

# 1. 平面点集

由平面解析几何知道,当在平面上引入了一个直角坐标系后,平面上的点 $P$ 与有序二元实数组 $(x,y)$ 之间就建立了一一对应.于是,我们常把有序实数组 $(x,y)$ 与平面上的点 $P$ 视作是等同的.这种建立了坐标系的平面称为坐标平面.二元有序实数组 $(x,y)$ 的全体,即 $\mathbf{R}^2 = \mathbf{R} \times \mathbf{R} = \{(x,y) | x,y \in \mathbb{R}\}$ 就表示坐标平面.

坐标平面上具有某种性质 P 的点的集合, 称为平面点集, 记作

$$
E = \{(x, y) | (x, y) \text {具有性质} P \}.
$$

例如,平面上以原点为中心、r为半径的圆内所有点的集合是

$$
C = \{(x, y) | x ^ {2} + y ^ {2} <   r ^ {2} \}.
$$

如果以点 $P$ 表示 $(x, y)$ , $|OP|$ 表示点 $P$ 到原点 $O$ 的距离, 那么集合 $C$ 也可表成

$$
C = \{P | | O P | <   r \}.
$$

现在我们来引入 $\mathbb{R}^2$ 中邻域的概念.

设 $P_{0}(x_{0},y_{0})$ 是 $xOy$ 平面上的一个点， $\delta$ 是某一正数。与点 $P_{0}(x_{0},y_{0})$ 距离小于 $\delta$ 的点 $P(x,y)$ 的全体，称为点 $P_{0}$ 的 $\delta$ 邻域，记作 $U(P_0,\delta)$ ，即

$$
U (P _ {0}, \delta) = \{P | | P P _ {0} | <   \delta \},
$$

也就是

$$
U (P _ {0}, \delta) = \{(x, y) | \sqrt {(x - x _ {0}) ^ {2} + (y - y _ {0}) ^ {2}} <   \delta \}.
$$

点 $P_{0}$ 的去心 $\delta$ 邻域，记作 $\mathring{U}(P_0,\delta)$ ，即

$$
\stackrel {\circ} {U} (P _ {0}, \delta) = \{P | 0 <   | P P _ {0} | <   \delta \}.
$$

在几何上, $U(P_{0},\delta)$ 就是xOy平面上以点 $P_{0}(x_{0},y_{0})$ 为中心、 $\delta>0$ 为半径的圆内部的点 $P(x,y)$ 的全体.

如果不需要强调邻域的半径 $\delta$ ，则用 $U(P_0)$ 表示点 $P_0$ 的某个邻域，点 $P_0$ 的去心邻域记作 $\mathring{U}(P_0)$ .

下面利用邻域来描述点和点集之间的关系.

任意一点 $P \in \mathbb{R}^2$ 与任意一个点集 $E \subset \mathbb{R}^2$ 之间必有以下三种关系中的一种：

(1) 内点: 如果存在点 P 的某个邻域 $U(P)$ ，使得 $U(P) \subset E$ ，那么称 P 为 E 的内点（如图 9-1 中， $P_{1}$ 为 E 的内点）；

(2) 外点: 如果存在点 P 的某个邻域 $U(P)$ ，使得 $U(P) \cap E = \varnothing$ ，那么称 P 为 E 的外点（如图 9-1 中， $P_{2}$ 为 E 的外点）；

(3) 边界点: 如果点 P 的任一邻域内既含有属于 E 的点, 又含有不属于 E 的点, 那么称 P 为 E 的边界点 (如图 9-1 中, $P_{3}$ 为 E 的边界点).

E 的边界点的全体, 称为 E 的边界, 记作 $\partial E$ .

$E$ 的内点必属于 $E; E$ 的外点必定不属于 $E$ ; 而 $E$ 的边界点可能属于 $E$ , 也可能不属于 $E$ .

任意一点 $P$ 与一个点集 $E$ 之间除了上述三种关系之外, 还有另一种关系, 这就是下面定义的聚点.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/ad58adff1d771c80fad6e14ab5b4175c0f976925ec197f53ec54d82c2b3eaf3e.jpg)



图9-1


聚点:如果对于任意给定的 $\delta>0$ , 点 P 的去心邻域 $\mathring{U}(P,\delta)$ 内总有 E 中的点, 那么称 P 是 E 的聚点.

由聚点的定义可知, 点集 E 的聚点 P 本身, 可以属于 E, 也可以不属于 E.

例如,设平面点集

$$
E = \{(x, y) | 1 <   x ^ {2} + y ^ {2} \leqslant 2 \}.
$$

满足 $1 < x^{2} + y^{2} < 2$ 的一切点 $(x, y)$ 都是 $E$ 的内点；满足 $x^{2} + y^{2} = 1$ 的一切点 $(x, y)$ 都是 $E$ 的边界点，它们都不属于 $E$ ；满足 $x^{2} + y^{2} = 2$ 的一切点 $(x, y)$ 也是 $E$ 的边界点，它们都属于 $E$ ；点集 $E$ 以及它的边界 $\partial E$ 上的一切点都是 $E$ 的聚点。

根据点集所属点的特征,再来定义一些重要的平面点集.

开集:如果点集 E 的点都是 E 的内点,那么称 E 为开集.

闭集:如果点集 E 的边界 $\partial E \subset E$ , 那么称 E 为闭集.

例如，集合 $\{(x,y) \mid 1 < x^2 + y^2 < 2\}$ 是开集；集合 $\{(x,y) \mid 1 \leqslant x^2 + y^2 \leqslant 2\}$ 是闭集；而集合 $\{(x,y) \mid 1 < x^2 + y^2 \leqslant 2\}$ 既非开集，也非闭集.

连通集:如果点集 E 内任何两点,都可用折线连接起来,且该折线上的点都属于 E,那么称 E 为连通集.

区域(或开区域): 连通的开集称为区域或开区域.

闭区域:开区域连同它的边界一起所构成的点集称为闭区域.

例如，集合 $\{(x,y) | 1 < x^2 + y^2 < 2\}$ 是区域，而集合 $\{(x,y) | 1 \leqslant x^2 + y^2 \leqslant 2\}$ 是闭区域.

有界集:对于平面点集 E, 如果存在某一正数 r, 使得

$$
E \subset U (O, r),
$$

其中 O 是坐标原点,那么称 E 为有界集.

无界集:一个集合如果不是有界集,就称这个集合为无界集.

例如,集合 $\{(x,y)\mid1\leqslant x^{2}+y^{2}\leqslant2\}$ 是有界闭区域,集合 $\{(x,y)\mid x+y>0\}$ 是无界开区域,集合 $\{(x,y)\mid x+y\geqslant0\}$ 是无界闭区域.

# *2. $n$ 维空间

设 n 为取定的一个正整数, 我们用 $R^{n}$ 表示 n 元有序实数组 $(x_{1}, x_{2}, \cdots, x_{n})$ 的全体所构成的集合, 即

$$
\mathbf {R} ^ {n} = \mathbf {R} \times \mathbf {R} \times \dots \times \mathbf {R} = \left\{\left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \mid x _ {i} \in \mathbf {R}, i = 1, 2, \dots , n \right\}.
$$

$R^{n}$ 中的元素 $(x_{1},x_{2},\cdots,x_{n})$ 有时也用单个字母x来表示，即 $x=(x_{1},x_{2},\cdots,x_{n})$ .当所有的 $x_{i}\quad(i=1,2,\cdots,n)$ 都为零时，称这样的元素为 $R^{n}$ 中的零元，记为0或0.在解析几何中，通过直角坐标系， $R^{2}$ （或 $R^{3}$ )中的元素分别与平面（或空间）中的点或向量建立一一对应，因而 $R^{n}$ 中的元素 $x=(x_{1},x_{2},\cdots,x_{n})$ 也称为 $R^{n}$ 中的一个点或一个n维向量, $x_{i}$ 称为点x的第i个坐标或n维向量x的第i个分量.特别地, $R^{n}$ 中的零元0称为 $R^{n}$ 中的坐标原点或n维零向量.

为了在集合 $\mathbb{R}^n$ 中的元素之间建立联系, 在 $\mathbb{R}^n$ 中定义线性运算如下:

设 $x=(x_{1},x_{2},\cdots,x_{n})$ , $y=(y_{1},y_{2},\cdots,y_{n})$ 为 $R^{n}$ 中任意两个元素, $\lambda\in R$ , 规定

$$
\boldsymbol {x} + \boldsymbol {y} = \left(x _ {1} + y _ {1}, x _ {2} + y _ {2}, \dots , x _ {n} + y _ {n}\right),
$$

$$
\lambda x = \left(\lambda x _ {1}, \lambda x _ {2}, \dots , \lambda x _ {n}\right).
$$

这样定义了线性运算的集合 $\mathbb{R}^n$ 称为 $n$ 维空间.

$R^{n}$ 中点 $x=(x_{1},x_{2},\cdots,x_{n})$ 和点 $y=(y_{1},y_{2},\cdots,y_{n})$ 间的距离,记作 $\rho(x,y)$ ,规定

$$
\rho (x, y) = \sqrt {\left(x _ {1} - y _ {1}\right) ^ {2} + \left(x _ {2} - y _ {2}\right) ^ {2} + \cdots + \left(x _ {n} - y _ {n}\right) ^ {2}}.
$$

显然, n=1,2,3 时, 上述规定与数轴上、直角坐标系下平面及空间中两点间的距离一致.

$R^{n}$ 中元素 $x=(x_{1},x_{2},\cdots,x_{n})$ 与零元0之间的距离 $\rho(x,0)$ 记作 $\|x\|$ （在 $R^{1},R^{2},R^{3}$ 中，通常将 $\|x\|$ 记作 $|x|$ ），即

$$
\| x \| = \sqrt {x _ {1} ^ {2} + x _ {2} ^ {2} + \cdots + x _ {n} ^ {2}}.
$$

采用这一记号,结合向量的线性运算,便得

$$
\| x - y \| = \sqrt {\left(x _ {1} - y _ {1}\right) ^ {2} + \left(x _ {2} - y _ {2}\right) ^ {2} + \cdots + \left(x _ {n} - y _ {n}\right) ^ {2}} = \rho (x, y).
$$

在 n 维空间 $R^{n}$ 中定义了距离以后, 就可以定义 $R^{n}$ 中变元的极限:

设 $\boldsymbol{x}=(x_{1},x_{2},\cdots,x_{n}),\boldsymbol{a}=(a_{1},a_{2},\cdots,a_{n})\in\mathbb{R}^{n}$ . 如果

$$
\| x - a \| \rightarrow 0,
$$

那么称变元 x 在 $R^{n}$ 中趋于固定元 a，记作 $x \to a$ 。

显然，

$$
x \rightarrow a \Leftrightarrow x _ {1} \rightarrow a _ {1}, x _ {2} \rightarrow a _ {2}, \dots , x _ {n} \rightarrow a _ {n}.
$$

在 $\mathbb{R}^n$ 中引入线性运算和距离, 使得前面讨论过的有关平面点集的一系列概念, 可以方便地引入到 $n (n \geqslant 3)$ 维空间中来, 例如,

设 $a=(a_{1},a_{2},\cdots,a_{n})\in\mathbb{R}^{n},\delta$ 是某一正数，则 n 维空间内的点集

$$
U (a, \delta) = \{x \mid x \in \mathbb {R} ^ {n}, \rho (x, a) <   \delta \}
$$

就定义为 $R^{n}$ 中点 a 的 $\delta$ 邻域. 以邻域为基础, 可以定义点集的内点、外点、边界点和聚点以及开集、闭集、区域等一系列概念. 这里不再赘述.

# 二、多元函数的概念

在很多自然现象以及实际问题中,经常会遇到多个变量之间的依赖关系,举例如下:

例 1 圆柱体的体积 V 和它的底半径 r、高 h 之间具有关系

$$
V = \pi r ^ {2} h.
$$

这里, 当 r 和 h 在集合 $\{(r,h) \mid r>0, h>0\}$ 内取定一对值 $(r,h)$ 时, V 的对应值就随之确定.

例 2 一定量的理想气体的压强 p、体积 V 和绝对温度 T 之间具有关系

$$
p = \frac {R T}{V},
$$

其中 R 为常数. 这里, 当 V 和 T 在集合 $\{(V, T) \mid V > 0, T > T_{0}\}$ 内取定一对值 $(V, T)$ 时, p 的对应值就随之确定.

例 3 设 R 是电阻 $R_{1}$ 和 $R_{2}$ 并联后的总电阻, 由电学知道, 它们之间具有关系

$$
R = \frac {R _ {1} R _ {2}}{R _ {1} + R _ {2}}.
$$

这里，当 $R_{1}$ 和 $R_{2}$ 在集合 $\{(R_1,R_2)\mid R_1 > 0,R_2 > 0\}$ 内取定一对值 $(R_{1},R_{2})$ 时， $R$ 的对应值就随之确定.

上面三个例子的具体意义虽各不相同,但它们却有共同的性质,抽出这些共性就可得出以下二元函数的定义.

定义 1 设 D 是 $R^{2}$ 的一个非空子集, 称映射 $f: D \rightarrow R$ 为定义在 D 上的二元函数, 通常记为

$$
z = f (x, y), \quad (x, y) \in D
$$

或

$$
z = f (P), \quad P \in D,
$$

其中点集 D 称为该函数的定义域, x 和 y 称为自变量, z 称为因变量.

上述定义中,与自变量 x 和 y 的一对值(即二元有序实数组) $(x,y)$ 相对应的因变量 z 的值,也称为 f 在点 $(x,y)$ 处的函数值,记作 $f(x,y)$ , 即 $z=f(x,y)$ . 函数值 $f(x,y)$ 的全体所构成的集合称为函数 f 的值域,记作 $f(D)$ , 即

$$
f (D) = \{z \mid z = f (x, y), (x, y) \in D \}.
$$

与一元函数的情形相仿,记号f与 $f(x,y)$ 的意义是有区别的,但习惯上常用记号“ $f(x,y),(x,y)\in D$ ”或“ $z=f(x,y),(x,y)\in D$ ”来表示D上的二元函数f.表示二元函数的记号f也是可以任意选取的,例如也可以记为 $z=\varphi(x,y),z=z(x,y)$ 等.

类似地, 可以定义三元函数 $u = f(x, y, z), (x, y, z) \in D$ 以及三元以上的函数. 一般地, 把定义 1 中的平面点集 $D$ 换成 $n$ 维空间 $\mathbb{R}^n$ 内的点集 $D$ , 映射 $f: D \to \mathbb{R}$ 就称为定义在 $D$ 上的 $n$ 元函数, 通常记为

$$
u = f \left(x _ {1}, x _ {2}, \dots , x _ {n}\right), \quad \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \in D,
$$

或简记为

$$
u = f (x), \quad x = \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \in D,
$$

也可记为

$$
u = f (P), \quad P \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \in D.
$$

当 $n = 2$ 或 $n = 3$ 时，习惯上将点 $(x_{1}, x_{2})$ 与点 $(x_{1}, x_{2}, x_{3})$ 分别写成 $(x, y)$ 与 $(x, y, z)$ . 这时，若用字母表示 $\mathbb{R}^2$ 或 $\mathbb{R}^3$ 中的点，即写成 $P(x, y)$ 或 $M(x, y, z)$ ，则相应的二元函数及三元函数也可简记为 $z = f(P)$ 及 $u = f(M)$ .

当 $n = 1$ 时， $n$ 元函数就是一元函数；当 $n \geqslant 2$ 时， $n$ 元函数统称为多元函数。

关于多元函数的定义域,与一元函数相类似,我们作如下约定:在一般地讨论用算式表达的多元函数 $u=f(x)$ 时,就以使这个算式有意义的变元 x 的值所组成的点集为这个多元函数的自然定义域.因而,对这类函数,它的定义域不再特别标出.例如,函数 $z=\ln(x+y)$ 的定义域为

$$
\{(x, y) \mid x + y > 0 \}
$$

(图 9-2), 这是一个无界开区域. 又如, 函数 $z = \arcsin(x^{2} + y^{2})$ 的定义域为

$$
\{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 1 \}
$$

(图 9-3), 这是一个有界闭区域.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/250bc318f767461682901738404440cddda22e7ddf6e941d888a9207ad3e87aa.jpg)



图9-2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/36751c709d66c7f77b1075c0e8e12b8954a48543da0f8f1e6360842ab83e8cd0.jpg)



图9-3


设函数 $z=f(x,y)$ 的定义域为 D. 对于任意取定的点 $P(x,y) \in D$ , 对应的函数值为

$z=f(x,y)$ . 这样, 以 x 为横坐标、y 为纵坐标和 $z=f(x,y)$ 为竖坐标在空间就确定一点 $M(x,y,z)$ . 当 $(x,y)$ 遍取 D 上的一切点时, 得到一个空间点集

$$
\{(x, y, z) \mid z = f (x, y), (x, y) \in D \},
$$

这个点集称为二元函数 $z = f(x, y)$ 的图形（图9-4）. 通常我们也说二元函数的图形是一张曲面.

例如,由空间解析几何知道,线性函数 $z=ax+by+c$ 的图形是一张平面,而函数 $z=x^{2}+y^{2}$ 的图形是旋转抛物面.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/8c439bc4f2eb1a618edee29129c9796d428162949755fcb385ac01d0ba0de77d.jpg)



图9-4


# 三、多元函数的极限

先讨论二元函数 $z = f(x,y)$ 当 $(x,y)\rightarrow (x_0,y_0)$ ，即 $P(x,y)\to P_0(x_0,y_0)$ 时的极限

这里 $P \rightarrow P_{0}$ 表示点 P 以任何方式趋于点 $P_{0}$ ，也就是点 P 与点 $P_{0}$ 间的距离趋于零，即

$$
\mid P P _ {0} \mid = \sqrt {\left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2}} \rightarrow 0.
$$

与一元函数的极限概念类似, 如果在 $P(x,y) \rightarrow P_{0}(x_{0},y_{0})$ 的过程中, 对应的函数值 $f(x,y)$ 无限接近于一个确定的常数 A, 那么就说 A 是函数 $f(x,y)$ 当 $(x,y) \rightarrow (x_{0},y_{0})$ 时的极限. 下面用“ $\varepsilon-\delta$ ”语言描述这个极限概念.

定义2 设二元函数 $f(P) = f(x, y)$ 的定义域为 $D, P_0(x_0, y_0)$ 是 $D$ 的聚点. 如果存在常数 $A$ , 对于任意给定的正数 $\varepsilon$ , 总存在正数 $\delta$ , 使得当点 $P(x, y) \in D \cap \overset{\circ}{U}(P_0, \delta)$ 时, 都有

$$
\mid f (P) - A \mid = \mid f (x, y) - A \mid <   \varepsilon
$$

成立,那么就称常数 A 为函数 $f(x,y)$ 当 $(x,y)\rightarrow(x_{0},y_{0})$ 时的极限,记作

$$
\lim _ {(x, y) \to (x _ {0}, y _ {0})} f (x, y) = A \quad {\text {或}} \quad f (x, y) \to A ((x, y) \to (x _ {0}, y _ {0}))  ,
$$

也记作

$$
\lim _ {P \to P _ {0}} f (  P  ) = A \quad {\text {或}} \quad f (  P  ) \to A \quad (  P \to P _ {0}  )  .
$$

为了区别于一元函数的极限,我们把二元函数的极限叫做二重极限.

例4 设 $f(x, y) = (x^2 + y^2) \sin \frac{1}{x^2 + y^2}$ , 求证:

$$
\lim _ {(x, y) \rightarrow (0, 0)} f (x, y) = 0.
$$

证 这里函数 $f(x, y)$ 的定义域为 $D = \mathbb{R}^2 \setminus \{(0, 0)\}$ , 点 $O(0, 0)$ 为 $D$ 的聚点. 因为

$$
\left| f (x, y) - 0 \right| = \left| \left(x ^ {2} + y ^ {2}\right) \sin \frac {1}{x ^ {2} + y ^ {2}} - 0 \right| \leqslant x ^ {2} + y ^ {2},
$$

可见， $\forall \varepsilon > 0$ ，取 $\delta = \sqrt{\varepsilon}$ ，则当

$$
0 <   \sqrt {(x - 0) ^ {2} + (y - 0) ^ {2}} <   \delta ,
$$

即 $P(x,y) \in D \cap \overset{\circ}{U}(O,\delta)$ 时,总有

$$
\left| f (x, y) - 0 \right| <   \varepsilon
$$

成立,所以

$$
\lim _ {(x, y) \rightarrow (0, 0)} f (x, y) = 0.
$$

必须注意,所谓二重极限存在,是指 $P(x,y)$ 以任何方式趋于 $P_{0}(x_{0},y_{0})$ 时, $f(x,y)$ 都无限接近于 A. 因此,如果 $P(x,y)$ 以某一特殊方式,例如沿着一条定直线或定曲线趋于 $P_{0}(x_{0},y_{0})$ 时，即使 $f(x,y)$ 无限接近于某一确定值，我们还不能由此断定函数的极限存在.但是反过来，如果当 $P(x,y)$ 以不同的方式趋于 $P_{0}(x_{0},y_{0})$ 时， $f(x,y)$ 趋于不同的值，那么就可以断定这函数的极限不存在.下面用例子来说明这种情形.

考察函数

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {x y}{x ^ {2} + y ^ {2}}, & x ^ {2} + y ^ {2} \neq 0, \\ 0, & x ^ {2} + y ^ {2} = 0. \end{array} \right.
$$

显然, 当点 $P(x,y)$ 沿 x 轴趋于点 $(0,0)$ 时,

$$
\lim_{\substack{(x,y)\to (0,0)\\ y = 0}}f(x,y) = \lim_{x\to 0}f(x,0) = \lim_{x\to 0}0 = 0;
$$

又当点 $P(x,y)$ 沿 y 轴趋于点 $(0,0)$ 时，

$$
\lim_{\substack{(x,y)\to (0,0)\\ x = 0}}f(x,y) = \lim_{y\to 0}f(0,y) = \lim_{y\to 0}0 = 0.
$$

虽然点 $P(x,y)$ 以上述两种特殊方式（沿 $x$ 轴或沿 $y$ 轴）趋于原点时函数的极限存在并且相等，但是 $\lim_{(x,y)\to (0,0)}f(x,y)$ 并不存在.这是因为当点 $P(x,y)$ 沿着直线 $y = kx$ 趋于点(0,0)时，有

$$
\lim_{\substack{(x,y)\to (0,0)\\ y = kx}}\frac{xy}{x^{2} + y^{2}} = \lim_{x\to 0}\frac{kx^{2}}{x^{2} + k^{2}x^{2}} = \frac{k}{1 + k^{2}},
$$

显然它是随着 k 的值的不同而改变的.

以上关于二元函数的极限概念,可相应地推广到 n 元函数 $u=f(P)$ , 即 $u=f(x_{1}, x_{2}, \cdots, x_{n})$ 上去.

关于多元函数的极限运算,有与一元函数类似的运算法则.

例5 求 $\lim_{(x,y)\to (0,2)}\frac{\sin(xy)}{x}$ 

解 这里函数 $\frac{\sin(xy)}{x}$ 的定义域为 $D = \{(x, y) \mid x \neq 0, y \in \mathbb{R}\}$ , $P_0(0, 2)$ 为 $D$ 的聚点.

由积的极限运算法则,得

$$
\lim _ {(x, y) \rightarrow (0, 2)} \frac {\sin (x y)}{x} = \lim _ {(x, y) \rightarrow (0, 2)} \left[ \frac {\sin (x y)}{x y} \cdot y \right] = \lim _ {x y \rightarrow 0} \frac {\sin (x y)}{x y} \cdot \lim _ {y \rightarrow 2} y = 1 \times 2 = 2.
$$

# 四、多元函数的连续性

明白了函数极限的概念,就不难说明多元函数的连续性.

定义3 设二元函数 $f(P) = f(x, y)$ 的定义域为 $D, P_0(x_0, y_0)$ 为 $D$ 的聚点，且 $P_0 \in$ 

# D. 如果

$$
\lim _ {(x, y) \rightarrow (x _ {0}, y _ {0})} f (x, y) = f (x _ {0}, y _ {0}),
$$

那么称函数 $f(x, y)$ 在点 $P_{0}(x_{0}, y_{0})$ 连续.

设函数 $f(x,y)$ 在D上有定义，D内的每一点都是函数定义域的聚点。如果函数 $f(x,y)$ 在D的每一点都连续，那么就称函数 $f(x,y)$ 在D上连续，或者称 $f(x,y)$ 是D上的连续函数。

以上关于二元函数的连续性概念,可相应地推广到 n 元函数 $f(P)$ 上去.

下面,我们把一元基本初等函数看成二元函数的特例(即另一个自变量不出现),来讨论它的连续性.先看一个例子.

例6 设 $f(x, y) = \sin x$ ，证明 $f(x, y)$ 是 $\mathbb{R}^2$ 上的连续函数.

证 设 $P_0(x_0, y_0) \in \mathbb{R}^2$ . $\forall \varepsilon > 0$ ，由于 $\sin x$ 在 $x_0$ 处连续，故 $\exists \delta > 0$ ，当 $|x - x_0| < \delta$ 时，有

$$
\left| \sin x - \sin x _ {0} \right| <   \varepsilon .
$$

以上述 $\delta$ 作 $P_0$ 的 $\delta$ 邻域 $U(P_0, \delta)$ ，则当 $P(x, y) \in U(P_0, \delta)$ 时，显然

$$
\mid x - x _ {0} \mid \leqslant \rho (P, P _ {0}) <   \delta ,
$$

从而

$$
\left| f (x, y) - f \left(x _ {0}, y _ {0}\right) \right| = \left| \sin x - \sin x _ {0} \right| <   \varepsilon ,
$$

即 $f(x, y) = \sin x$ 在点 $P_0(x_0, y_0)$ 连续. 由 $P_0$ 的任意性知, $\sin x$ 作为 $x, y$ 的二元函数在 $\mathbf{R}^2$ 上连续.

类似的讨论可知,一元基本初等函数看成二元函数或二元以上的多元函数时,它们在各自的定义域内都是连续的.

定义4 设函数 $f(x, y)$ 的定义域为 $D, P_0(x_0, y_0)$ 是 $D$ 的聚点. 如果函数 $f(x, y)$ 在点 $P_0(x_0, y_0)$ 不连续, 那么称 $P_0(x_0, y_0)$ 为函数 $f(x, y)$ 的间断点.

例如,前面讨论过的函数

$$
f (x, y) = \left\{ \begin{array}{c c} \frac {x y}{x ^ {2} + y ^ {2}}, & x ^ {2} + y ^ {2} \neq 0, \\ 0, & x ^ {2} + y ^ {2} = 0, \end{array} \right.
$$

其定义域 $D = \mathbf{R}^2$ ，点 $O(0,0)$ 是 $D$ 的聚点. $f(x,y)$ 当 $(x,y)\to (0,0)$ 时的极限不存在，所以点 $O(0,0)$ 是该函数的一个间断点；又如函数

$$
f (x, y) = \sin \frac {1}{x ^ {2} + y ^ {2} - 1},
$$

其定义域为

$$
D = \{(x, y) | x ^ {2} + y ^ {2} \neq 1 \},
$$

圆周 $C = \{(x, y) | x^2 + y^2 = 1\}$ 上的点都是 $D$ 的聚点，而 $f(x, y)$ 在 $C$ 上没有定义，当然 $f(x, y)$ 在 $C$ 上各点都不连续，所以圆周 $C$ 上各点都是该函数的间断点.

前面已经指出:一元函数中关于极限的运算法则,对于多元函数仍然适用.根据多元函数的极限运算法则,可以证明多元连续函数的和、差、积仍为连续函数;连续函数的商在分母不为零处仍连续;多元连续函数的复合函数也是连续函数.

与一元初等函数相类似,多元初等函数是指可用一个式子表示的多元函数,这个式子是由常数及具有不同自变量的一元基本初等函数经过有限次的四则运算和复合运算而得到的.例如, $\frac{x+x^{2}-y^{2}}{1+y^{2}},\sin(x+y),e^{x^{2}+y^{2}+z^{2}}$ 等都是多元初等函数.

根据上面指出的连续函数的和、差、积、商的连续性以及连续函数的复合函数的连续性,再利用基本初等函数的连续性,我们进一步可以得出如下结论:

一切多元初等函数在其定义区域内是连续的.所谓定义区域是指包含在定义域内的区域或闭区域.

由多元初等函数的连续性,如果要求它在点 $P_{0}$ 处的极限,而该点又在此函数的定义区域内,那么此极限值就是函数在该点的函数值,即

$$
\lim _ {P \rightarrow P _ {0}} f (P) = f (P _ {0}).
$$

例7 求 $\lim_{(x,y)\to (1,2)}\frac{x + y}{xy}$ 

解 函数 $f(x, y) = \frac{x + y}{xy}$ 是初等函数, 它的定义域为

$$
D = \{(x, y) | x \neq 0, y \neq 0 \}.
$$

$P_{0}(1,2)$ 为 $D$ 的内点，故存在 $P_{0}$ 的某一邻域 $U(P_{0}) \subset D$ ，而任何邻域都是区域，所以 $U(P_{0})$ 是 $f(x,y)$ 的一个定义区域，因此

$$
\lim _ {(x, y) \rightarrow (1, 2)} \frac {x + y}{x y} = f (1, 2) = \frac {3}{2}.
$$

一般地,求 $\lim_{P\to P_{0}}f(P)$ 时,如果 $f(P)$ 是初等函数,且 $P_{0}$ 是 $f(P)$ 的定义域的内点,那么 $f(P)$ 在点 $P_{0}$ 处连续,于是

$$
\lim _ {P \rightarrow P _ {0}} f (P) = f (P _ {0}).
$$

例8 求 $\lim_{(x,y)\to (0,0)}\frac{\sqrt{xy + 1} - 1}{xy}$ 

解 $\lim_{(x,y)\to (0,0)}\frac{\sqrt{xy + 1} - 1}{xy} = \lim_{(x,y)\to (0,0)}\frac{xy + 1 - 1}{xy(\sqrt{xy + 1} + 1)} = \lim_{(x,y)\to (0,0)}\frac{1}{\sqrt{xy + 1} + 1} = \frac{1}{2}.$ 

以上运算的最后一步用到了二元函数 $\frac{1}{\sqrt{xy+1}+1}$ 在点(0,0)的连续性.

与闭区间上一元连续函数的性质相类似,在有界闭区域上连续的多元函数具有如下性质:

性质1(有界性与最大值最小值定理) 在有界闭区域 $D$ 上的多元连续函数, 必定在 $D$ 上有界, 且能取得它的最大值和最小值.

性质1就是说,若 $f(P)$ 在有界闭区域D上连续,则必定存在常数M>0,使得对一切 $P\in D$ ,有 $\left|f(P)\right|\leqslant M$ ;且存在 $P_{1},P_{2}\in D$ ,使得

$$
f \left(P _ {1}\right) = \max \{f (P) \mid P \in D \}, f \left(P _ {2}\right) = \min \{f (P) \mid P \in D \}.
$$

性质2（介值定理）在有界闭区域 $D$ 上的多元连续函数必取得介于最大值和最小值之间的任何值.

* 性质 3(一致连续性定理) 在有界闭区域 D 上的多元连续函数必定在 D 上一致连续.

性质3就是说,若 $f(P)$ 在有界闭区域D上连续,则对于任意给定的正数 $\varepsilon$ ,总存在正数 $\delta$ ,使得对于D上的任意两点 $P_{1},P_{2}$ ,只要当 $|P_{1}P_{2}|<\delta$ 时,都有

$$
\left| f (P _ {1}) - f (P _ {2}) \right| <   \varepsilon
$$

成立.

# 习题9-1

1. 判定下列平面点集中哪些是开集、闭集、区域、有界集、无界集，并分别指出它们的聚点所成的点集（称为导集）和边界。

(1) $\{(x,y)\mid x\neq0,y\neq0\}$ ; 

(2) $\{(x,y)\mid1<x^{2}+y^{2}\leqslant4\}$ ; 

(3) $\{(x,y)\mid y>x^{2}\}$ ; 

(4) $\{(x,y) | x^2 + (y - 1)^2 \geqslant 1\} \cap \{(x,y) | x^2 + (y - 2)^2 \leqslant 4\}$ . 

2. 已知函数 $f(x, y) = x^2 + y^2 - xy \tan \frac{x}{y}$ ，试求 $f(tx, ty)$ .

3. 试证函数 $F(x, y) = \ln x \cdot \ln y$ 满足关系式

$$
F (x y, u v) = F (x, u) + F (x, v) + F (y, u) + F (y, v).
$$

4. 已知函数 $f(u, v, w) = u^w + w^{u + v}$ ，试求 $f(x + y, x - y, xy)$ .

5. 求下列各函数的定义域：

(1) $z = \ln (y^2 - 2x + 1)$ ; 

(2) $z = \frac{1}{\sqrt{x + y}} +\frac{1}{\sqrt{x - y}};$ 

(3) $z = \sqrt{x - \sqrt{y}}$ ; 

(4) $z = \ln (y - x) + \frac{\sqrt{x}}{\sqrt{1 - x^2 - y^2}};$ 

(5) $u = \sqrt{R^2 - x^2 - y^2 - z^2} + \frac{1}{\sqrt{x^2 + y^2 + z^2 - r^2}} (R > r > 0)$ ; 

(6) $u = \arccos \frac{z}{\sqrt{x^2 + y^2}}.$ 

6. 求下列各极限：

(1) $\lim_{(x,y)\to (0,1)}\frac{1 - xy}{x^2 + y^2};$ 

(2) $\lim_{(x,y)\to (1,0)}\frac{\ln(x + e^y)}{\sqrt{x^2 + y^2}};$ 

(3) $\lim_{(x,y)\to(0,0)}\frac{2-\sqrt{xy+4}}{xy};$ 

(4) $\lim_{(x,y)\to (0,0)}\frac{xy}{\sqrt{2 - e^{xy}} - 1};$ 

(5) $\lim_{(x,y)\to (2,0)}\frac{\tan(xy)}{y};$ 

(6) $\lim_{(x,y)\to (0,0)}\frac{1 - \cos(x^2 + y^2)}{(x^2 + y^2)e^{x^2y^2}}.$ 

*7. 证明下列极限不存在:

(1) $\lim_{(x,y)\to (0,0)}\frac{x + y}{x - y};$ 

(2) $\lim_{(x,y)\to (0,0)}\frac{x^2y^2}{x^2y^2 + (x - y)^2};$ 

(3) $\lim_{(x,y)\to(0,0)}\frac{xy}{x+y};$ 

(4) $\lim_{(x,y)\to (0,0)}\frac{1 - \cos(x + y)}{(x + y)xy}.$ 

8. 函数 $z=\frac{y^{2}+2x}{y^{2}-2x}$ 在何处是间断的？

*9. 证明 $\lim_{(x,y)\to (0,0)}\frac{xy}{\sqrt{x^2 + y^2}} = 0.$ 

*10. 设 $F(x, y) = f(x)$ , $f(x)$ 在点 $x_0$ 处连续, 证明: 对任意 $y_0 \in \mathbb{R}$ , $F(x, y)$ 在点 $(x_0, y_0)$ 处连续.

# 第二节 偏导数

# 一、偏导数的定义及其计算法

在研究一元函数时,我们从研究函数的变化率引入了导数的概念.对于多元函数同样需要讨论它的变化率.但多元函数的自变量不止一个,因变量与自变量的关系要比一元函数复杂得多.在这一节里,我们首先考虑多元函数关于其中一个自变量的变化率.以二元函数 $z=f(x,y)$ 为例,如果只有自变量x变化,而自变量y固定(即看做常量),这时它就是x的一元函数,这函数对x的导数,就称为二元函数 $z=f(x,y)$ 对x的偏导数,即有如下定义:

定义 设函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 的某一邻域内有定义，当 $y$ 固定在 $y_0$ 而 $x$ 在 $x_0$ 处有增量 $\Delta x$ 时，相应的函数有增量

$$
f (x _ {0} + \Delta x, y _ {0}) - f (x _ {0}, y _ {0}),
$$

如果

$$
\lim _ {\Delta x \to 0} \frac {f (x _ {0} + \Delta x , y _ {0}) - f (x _ {0} , y _ {0})}{\Delta x} \tag {2-1}
$$

存在,那么称此极限为函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处对 $x$ 的偏导数,记作

$$
\frac {\partial z}{\partial x} \Bigg | _ { \begin{array}{c} {x = x _ {0}} \\ {y = y _ {0}} \end{array} }, \quad \frac {\partial f}{\partial x} \Bigg | _ { \begin{array}{c} {z = x _ {0}} \\ {y = y _ {0}} \end{array} }, \quad z _ {x} \Bigg | _ { \begin{array}{c} {x = x _ {0}} \\ {y = y _ {0}} \end{array} } \text {或} f _ {x} (x _ {0}, y _ {0}). ①
$$

例如,极限(2-1)可以表示为

$$
f _ {x} \left(x _ {0}, y _ {0}\right) = \lim _ {\Delta x \rightarrow 0} \frac {f \left(x _ {0} + \Delta x , y _ {0}\right) - f \left(x _ {0} , y _ {0}\right)}{\Delta x}. \tag {2-2}
$$

类似地, 函数 $z=f(x,y)$ 在点 $(x_{0},y_{0})$ 处对 y 的偏导数定义为

$$
\lim _ {\Delta y \rightarrow 0} \frac {f \left(x _ {0} , y _ {0} + \Delta y\right) - f \left(x _ {0} , y _ {0}\right)}{\Delta y}, \tag {2-3}
$$

记作

$$
\frac {\partial z}{\partial y} \Bigg | _ {x = x _ {0} \atop y = y _ {0}}, \quad \frac {\partial f}{\partial y} \Bigg | _ {x = x _ {0} \atop y = y _ {0}}, \quad z _ {y} \Bigg | _ {x = x _ {0} \atop y = y _ {0}} \quad \text {或} \quad f _ {y} (x _ {0}, y _ {0}).
$$

如果函数 $z = f(x,y)$ 在区域 $D$ 内每一点 $(x,y)$ 处对 $x$ 的偏导数都存在, 那么这个偏导数就是 $x,y$ 的函数, 它就称为函数 $z = f(x,y)$ 对自变量 $x$ 的偏导函数, 记作

$$
\frac {\partial z}{\partial x}, \quad \frac {\partial f}{\partial x}, \quad z _ {x} \quad \text {或} \quad f _ {x} (x, y).
$$

类似地,可以定义函数 $z=f(x,y)$ 对自变量 y 的偏导函数,记作

$$
\frac {\partial z}{\partial y}, \quad \frac {\partial f}{\partial y}, \quad z _ {y} \quad \text {或} \quad f _ {y} (x, y).
$$

由偏导函数的概念可知， $f(x,y)$ 在点 $(x_{0},y_{0})$ 处对 x 的偏导数 $f_{x}(x_{0},y_{0})$ 显然就是偏导函数 $f_{x}(x,y)$ 在点 $(x_{0},y_{0})$ 处的函数值； $f_{y}(x_{0},y_{0})$ 就是偏导函数 $f_{y}(x,y)$ 在点 $(x_{0},y_{0})$ 处的函数值。就像一元函数的导函数一样，以后在不至于混淆的地方也把偏导函数简称为偏导数。

至于实际求 $z = f(x, y)$ 的偏导数，并不需要用新的方法，因为这里只有一个自变量在变动，另一个自变量是看做固定的，所以仍旧是一元函数的微分法问题。求 $\frac{\partial f}{\partial x}$ 时，只要把 $y$ 暂时看做常量而对 $x$ 求导数；求 $\frac{\partial f}{\partial y}$ 时，只要把 $x$ 暂时看做常量而对 $y$ 求导数。

偏导数的概念还可推广到二元以上的函数.例如三元函数 $u = f(x,y,z)$ 在点 $(x,y,z)$ 处对 $x$ 的偏导数定义为

$$
f _ {x} (x, y, z) = \lim _ {\Delta x \rightarrow 0} \frac {f (x + \Delta x , y , z) - f (x , y , z)}{\Delta x},
$$

其中 $(x, y, z)$ 是函数 $u = f(x, y, z)$ 的定义域的内点. 它们的求法也仍旧是一元函数的微分法问题.

例 1 求 $z=x^{2}+3xy+y^{2}$ 在点 $(1,2)$ 处的偏导数.

解 把 y 看做常量, 得

$$
\frac {\partial z}{\partial x} = 2 x + 3 y;
$$

把 $x$ 看做常量，得

$$
\frac {\partial z}{\partial y} = 3 x + 2 y.
$$

将(1,2)代入上面的结果,就得

$$
\left. \frac {\partial z}{\partial x} \right| _ {x = 1 \atop y = 2} = 2 \times 1 + 3 \times 2 = 8, \quad \left. \frac {\partial z}{\partial y} \right| _ {x = 1 \atop y = 2} = 3 \times 1 + 2 \times 2 = 7.
$$

例 2 求 $z=x^{2}\sin2y$ 的偏导数.

解 $\frac{\partial z}{\partial x}=2x\sin2y,\quad\frac{\partial z}{\partial y}=2x^{2}\cos2y.$ 

例3 设 $z = x^{y}$ ( $x > 0, x \neq 1$ ), 求证: $\frac{x}{y} \frac{\partial z}{\partial x} + \frac{1}{\ln x} \frac{\partial z}{\partial y} = 2z$ .

证 因为 $\frac{\partial z}{\partial x} = yx^{y - 1},\frac{\partial z}{\partial y} = x^y\ln x.$ 所以

$$
\frac {x}{y} \frac {\partial z}{\partial x} + \frac {1}{\ln x} \frac {\partial z}{\partial y} = \frac {x}{y} y x ^ {y - 1} + \frac {1}{\ln x} x ^ {y} \ln x = x ^ {y} + x ^ {y} = 2 z.
$$

例4 求 $r = \sqrt{x^2 + y^2 + z^2}$ 的偏导数.

解 把 y 和 z 都看做常量, 得

$$
\frac {\partial r}{\partial x} = \frac {x}{\sqrt {x ^ {2} + y ^ {2} + z ^ {2}}} = \frac {x}{r}.
$$

由于所给函数关于自变量的对称性①,所以

$$
\frac {\partial r}{\partial y} = \frac {y}{r}, \quad \frac {\partial r}{\partial z} = \frac {z}{r}.
$$

例 5 已知理想气体的状态方程 pV=RT (R 为常量), 求证:

$$
\frac {\partial p}{\partial V} \cdot \frac {\partial V}{\partial T} \cdot \frac {\partial T}{\partial p} = - 1.
$$

证 因为

$$
p = \frac {R T}{V}, \quad \frac {\partial p}{\partial V} = - \frac {R T}{V ^ {2}};
$$

$$
\begin{array}{l} V = \frac {R T}{p}, \quad \frac {\partial V}{\partial T} = \frac {R}{p}; \\ T = \frac {p V}{R}, \quad \frac {\partial T}{\partial p} = \frac {V}{R}, \\ \end{array}
$$

所以

$$
\frac {\partial p}{\partial V} \cdot \frac {\partial V}{\partial T} \cdot \frac {\partial T}{\partial p} = - \frac {R T}{V ^ {2}} \cdot \frac {R}{p} \cdot \frac {V}{R} = - \frac {R T}{p V} = - 1.
$$

我们知道,对一元函数来说, $\frac{dy}{dx}$ 可看做函数的微分dy与自变量的微分dx之商.而上式表明,偏导数的记号是一个整体记号,不能看做分子与分母之商.

二元函数 $z=f(x,y)$ 在点 $(x_{0},y_{0})$ 的偏导数有下述几何意义.

设 $M_0(x_0, y_0, f(x_0, y_0))$ 为曲面 $z = f(x, y)$ 上的一点，过 $M_0$ 作平面 $y = y_0$ ，截此曲面得一曲线，此曲线在平面 $y = y_0$ 上的方程为 $z = f(x, y_0)$ ，则导数 $\frac{\mathrm{d}}{\mathrm{d}x} f(x, y_0) \bigg|_{x = x_0}$ ，即偏导数 $f_x(x_0, y_0)$ ，就是这曲线在点 $M_0$ 处的切线 $M_0T_x$ 对 $x$ 轴的斜率（图9-5）。同样，偏导数 $f_y(x_0, y_0)$ 的几何意义是曲面被平面 $x = x_0$ 所截得的曲线在点 $M_0$ 处的切线 $M_0T_y$ 对 $y$ 轴的斜率。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/0d23a6f14142169a450c153a1b29e191dccc311e3456cfe853048f57f7e58040.jpg)



图9-5


我们已经知道,如果一元函数在某点具有导数,那么它在该点必定连续.但对于多元函数来说,即使各偏导数在某点都存在,也不能保证函数在该点连续.这是因为各偏导数存在只能保证点P沿着平行于坐标轴的方向趋于 $P_{0}$ 时,函数值 $f(P)$ 趋于 $f(P_{0})$ ,但不能保证点P按任何方式趋于 $P_{0}$ 时,函数值 $f(P)$ 都趋于 $f(P_{0})$ .例如,函数

$$
z = f (x, y) = \left\{ \begin{array}{l l} \frac {x y}{x ^ {2} + y ^ {2}}, & x ^ {2} + y ^ {2} \neq 0, \\ 0, & x ^ {2} + y ^ {2} = 0 \end{array} \right.
$$

在点 $(0,0)$ 处对x的偏导数为

$$
f _ {x} (0, 0) = \lim _ {\Delta x \rightarrow 0} \frac {f (0 + \Delta x , 0) - f (0 , 0)}{\Delta x} = \lim _ {\Delta x \rightarrow 0} 0 = 0;
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/2c81c617e1ece86751884e2681816c395aefb29cd40683815cefd866f6fb78bc.jpg)


释疑解难

9-1 

同样有

$$
f _ {y} (0, 0) = \lim _ {\Delta y \rightarrow 0} \frac {f (0 , 0 + \Delta y) - f (0 , 0)}{\Delta y} = \lim _ {\Delta y \rightarrow 0} 0 = 0.
$$

但是在第一节中已经知道这函数在点(0,0)并不连续.

# 二、高阶偏导数

设函数 $z = f(x,y)$ 在区域 $D$ 内具有偏导数

$$
\frac {\partial z}{\partial x} = f _ {x} (x, y), \quad \frac {\partial z}{\partial y} = f _ {y} (x, y),
$$

于是在 D 内 $f_{x}(x,y)$ , $f_{y}(x,y)$ 都是 x, y 的函数. 如果这两个函数的偏导数也存在, 那么称它们是函数 $z=f(x,y)$ 的二阶偏导数. 按照对变量求导次序的不同有下列四个二阶偏导数:

$$
\begin{array}{l} \frac {\partial}{\partial x} \left(\frac {\partial z}{\partial x}\right) = \frac {\partial^ {2} z}{\partial x ^ {2}} = f _ {x x} (x, y), \quad \frac {\partial}{\partial y} \left(\frac {\partial z}{\partial x}\right) = \frac {\partial^ {2} z}{\partial x \partial y} = f _ {x y} (x, y), \\ \frac {\partial}{\partial x} \left(\frac {\partial z}{\partial y}\right) = \frac {\partial^ {2} z}{\partial y \partial x} = f _ {y x} (x, y), \quad \frac {\partial}{\partial y} \left(\frac {\partial z}{\partial y}\right) = \frac {\partial^ {2} z}{\partial y ^ {2}} = f _ {y y} (x, y). \\ \end{array}
$$

其中第二、三两个偏导数称为混合偏导数. 同样可得三阶、四阶……以及 n 阶偏导数. 二阶及二阶以上的偏导数统称为高阶偏导数.

例6 设 $z = x^{3}y^{2} - 3xy^{3} - xy + 1$ ，求 $\frac{\partial^2z}{\partial x^2},\frac{\partial^2z}{\partial y\partial x},\frac{\partial^2z}{\partial x\partial y},\frac{\partial^2z}{\partial y^2}$ 及 $\frac{\partial^3z}{\partial x^3}$ 

解 $\frac{\partial z}{\partial x} = 3x^{2}y^{2} - 3y^{3} - y,$ $\frac{\partial z}{\partial y} = 2x^3 y - 9xy^2 -x;$ 

$$
\frac {\partial^ {2} z}{\partial x ^ {2}} = 6 x y ^ {2}, \quad \frac {\partial^ {2} z}{\partial y \partial x} = 6 x ^ {2} y - 9 y ^ {2} - 1, \quad \frac {\partial^ {2} z}{\partial x \partial y} = 6 x ^ {2} y - 9 y ^ {2} - 1, \quad \frac {\partial^ {2} z}{\partial y ^ {2}} = 2 x ^ {3} - 1 8 x y;
$$

$$
\frac {\partial^ {3} z}{\partial x ^ {3}} = 6 y ^ {2}.
$$

我们看到例6中两个二阶混合偏导数相等, 即 $\frac{\partial^{2}z}{\partial y\partial x}=\frac{\partial^{2}z}{\partial x\partial y}$ . 这不是偶然的, 事实上, 有下述定理.

定理 如果函数 $z = f(x, y)$ 的两个二阶混合偏导数 $\frac{\partial^2 z}{\partial y \partial x}$ 及 $\frac{\partial^2 z}{\partial x \partial y}$ 在区域 $D$ 内连续，那么在该区域内这两个二阶混合偏导数必相等.

换句话说,二阶混合偏导数在连续的条件下与求导的次序无关.这定理的证明从略.

对于二元以上的函数,也可以类似地定义高阶偏导数,而且高阶混合偏导数在偏导数连续的条件下也与求导的次序无关.

例7 验证函数 $z = \ln \sqrt{x^2 + y^2}$ 满足方程

$$
\frac {\partial^ {2} z}{\partial x ^ {2}} + \frac {\partial^ {2} z}{\partial y ^ {2}} = 0.
$$

证 因为 $z = \ln \sqrt{x^2 + y^2} = \frac{1}{2}\ln (x^2 + y^2)$ ，所以

$$
\frac {\partial z}{\partial x} = \frac {x}{x ^ {2} + y ^ {2}}, \quad \frac {\partial z}{\partial y} = \frac {y}{x ^ {2} + y ^ {2}},
$$

$$
\frac {\partial^ {2} z}{\partial x ^ {2}} = \frac {(x ^ {2} + y ^ {2}) - x \cdot 2 x}{(x ^ {2} + y ^ {2}) ^ {2}} = \frac {y ^ {2} - x ^ {2}}{(x ^ {2} + y ^ {2}) ^ {2}}, \quad \frac {\partial^ {2} z}{\partial y ^ {2}} = \frac {(x ^ {2} + y ^ {2}) - y \cdot 2 y}{(x ^ {2} + y ^ {2}) ^ {2}} = \frac {x ^ {2} - y ^ {2}}{(x ^ {2} + y ^ {2}) ^ {2}}.
$$

因此

$$
\frac {\partial^ {2} z}{\partial x ^ {2}} + \frac {\partial^ {2} z}{\partial y ^ {2}} = \frac {y ^ {2} - x ^ {2}}{\left(x ^ {2} + y ^ {2}\right) ^ {2}} + \frac {x ^ {2} - y ^ {2}}{\left(x ^ {2} + y ^ {2}\right) ^ {2}} = 0.
$$

例8 证明函数 $u = \frac{1}{r}$ 满足方程

$$
\frac {\partial^ {2} u}{\partial x ^ {2}} + \frac {\partial^ {2} u}{\partial y ^ {2}} + \frac {\partial^ {2} u}{\partial z ^ {2}} = 0,
$$

其中 $r = \sqrt{x^2 + y^2 + z^2}$ 

证 $\frac{\partial u}{\partial x} = -\frac{1}{r^2}\frac{\partial r}{\partial x} = -\frac{1}{r^2}\cdot \frac{x}{r} = -\frac{x}{r^3},$ 

$$
\frac {\partial^ {2} u}{\partial x ^ {2}} = - \frac {1}{r ^ {3}} + \frac {3 x}{r ^ {4}} \cdot \frac {\partial r}{\partial x} = - \frac {1}{r ^ {3}} + \frac {3 x ^ {2}}{r ^ {5}}.
$$

因为函数关于自变量的对称性,所以

$$
\frac {\partial^ {2} u}{\partial y ^ {2}} = - \frac {1}{r ^ {3}} + \frac {3 y ^ {2}}{r ^ {5}}, \quad \frac {\partial^ {2} u}{\partial z ^ {2}} = - \frac {1}{r ^ {3}} + \frac {3 z ^ {2}}{r ^ {5}}.
$$

因此

$$
\frac {\partial^ {2} u}{\partial x ^ {2}} + \frac {\partial^ {2} u}{\partial y ^ {2}} + \frac {\partial^ {2} u}{\partial z ^ {2}} = - \frac {3}{r ^ {3}} + \frac {3 (x ^ {2} + y ^ {2} + z ^ {2})}{r ^ {5}} = - \frac {3}{r ^ {3}} + \frac {3 r ^ {2}}{r ^ {5}} = 0.
$$

例 7 和例 8 中的两个方程都叫做拉普拉斯(Laplace)方程, 它是数学物理方程中一种很重要的方程.

# 习题9-2

1. 设 $f(x, y) = \mathrm{e}^{\sqrt{x^2 + y^4}}$ ，求 $f_x(0, 0), f_y(0, 0)$ .

2. 求下列函数的偏导数：

(1) $z = x^{3}y - y^{3}x;$ 

(2) $s = \frac{u^2 + v^2}{uv}$ ; 

(3) $z = \sqrt{\ln(xy)}$ ; 

(4) $z = \sin (xy) + \cos^2 (xy)$ ; 

(5) $z = \ln \tan \frac{x}{y}$ ; 

(6) $z = (1 + xy)^y$ ; 

(7) $u = x^{\frac{y}{z}}$ ; 

(8) $u = \arctan(x - y)^{2}$ . 

3. 设 $T=2\pi\sqrt{\frac{l}{g}}$ ，求证 $l\frac{\partial T}{\partial l}+g\frac{\partial T}{\partial g}=0$ .

4. 设 $z=e^{-\left(\frac{1}{x}+\frac{1}{y}\right)}$ ，求证 $x^{2}\frac{\partial z}{\partial x}+y^{2}\frac{\partial z}{\partial y}=2z.$ 

5. 设 $f(x, y) = x + (y - 1) \arcsin \sqrt{\frac{x}{y}}$ ，求 $f_x(x, 1)$ .

6. 求曲线 $\left\{\begin{aligned} z &= \frac{x^{2} + y^{2}}{4}, \\ y &= 4 \end{aligned}\right.$ ，在点 $(2,4,5)$ 处的切线对于 x 轴的倾角.

7. 求下列函数的 $\frac{\partial^2 z}{\partial x^2}, \frac{\partial^2 z}{\partial y^2}$ 和 $\frac{\partial^2 z}{\partial x \partial y}$ :

(1) $z = x^{4} + y^{4} - 4x^{2}y^{2}$ ; 

(2) $z = \arctan \frac{y}{x}$ ; 

(3) $z=y^{x}$ . 

8. 设 $f(x, y, z) = xy^2 + yz^2 + zx^2$ ，求 $f_{xx}(0, 0, 1), f_{xz}(1, 0, 2), f_{yz}(0, -1, 0)$ 及 $f_{zzx}(2, 0, 1)$ .

9. 设 $z = x \ln(xy)$ , 求 $\frac{\partial^3 z}{\partial x^2 \partial y}$ 及 $\frac{\partial^3 z}{\partial x \partial y^2}$ .

10. 验证：

(1) $y=e^{-kn^{2}t}\sin nx$ 满足 $\frac{\partial y}{\partial t}=k\frac{\partial^{2}y}{\partial x^{2}};$ 

(2) $r = \sqrt{x^2 + y^2 + z^2}$ 满足 $\frac{\partial^2r}{\partial x^2} +\frac{\partial^2r}{\partial y^2} +\frac{\partial^2r}{\partial z^2} = \frac{2}{r}.$ 

# 第三节 全微分

# 一、全微分的定义

由偏导数的定义知道,二元函数对某个自变量的偏导数表示当另一个自变量固定时,因变量相对于该自变量的变化率.根据一元函数微分学中增量与微分的关系,可得

$$
f (x + \Delta x, y) - f (x, y) \approx f _ {x} (x, y) \Delta x,
$$

$$
f (x, y + \Delta y) - f (x, y) \approx f _ {y} (x, y) \Delta y.
$$

上面两式的左端分别叫做二元函数对 x 和对 y 的偏增量,而右端分别叫做二元函数对

x 和对 y 的偏微分.
在实际问题中,有时需要研究多元函数中各个自变量都取得增量时因变量所获得

的增量,即所谓全增量的问题.下面以二元函数为例进行设函数 $z=f(x,y)$ 在点 $P(x,y)$ 的某邻域内有定义, $P'(x+\Delta x,y+\Delta y)$ 为这邻域内的任意一点,则称这两点的函数值之差 $f(x+\Delta x,y+\Delta y)-f(x,y)$ 为函数在点P对应于自变量增量 $\Delta x$ 和 $\Delta y$ 的全增量,记作 $\Delta z$ ,即

$$
\Delta z = f (x + \Delta x, y + \Delta y) - f (x, y). \tag {3-1}
$$

一般说来,计算全增量 $\Delta z$ 比较复杂.与一元函数的情形一样,我们希望用自变量的增量 $\Delta x, \Delta y$ 的线性函数来近似地代替函数的全增量 $\Delta z$ ,从而引入如下定义:增量

可表示为

$$
\Delta z = f (x + \Delta x, y + \Delta y) - f (x, y)
$$

$$
\Delta z = A \Delta x + B \Delta y + o (\rho), \tag {3-2}
$$

其中 A 和 B 不依赖于 $\Delta x$ 和 $\Delta y$ 而仅与 x 和 y 有关, $\rho = \sqrt{(\Delta x)^{2} + (\Delta y)^{2}}$ , 那么称函数 $z = f(x, y)$ 在点 $(x, y)$ 可微分, 而 $A\Delta x + B\Delta y$ 称为函数 $z = f(x, y)$ 在点 $(x, y)$ 的全微分, 记作 dz, 即

$$
\mathrm{d} z = A \Delta x + B \Delta y.
$$

如果函数在区域 D 内各点处都可微分,那么称这函数在 D 内可微分.
在第二节中曾指出,多元函数在某点的值是

(2) 证明函数在某点的偏导数存在, 并不能保证函数在该点连续. 但是, 由上述定义可知, 如果函数 $z = f(x, y)$ 在点 $(x, y)$ 可微分, 那么这函数在该点必定连续. 事实上, 这时由 (3-2) 式可得

从而①

$$
\lim _ {\rho \rightarrow 0} \Delta z = 0,
$$

$\lim_{(\Delta x, \Delta y) \to (0, 0)} f(x + \Delta x, y + \Delta y) = \lim_{\rho \to 0} [f(x, y) + \Delta z] = f(x, y)$ . 因此函数 $z = f(x, y)$ 在点 $(x, y)$ 处连续.

下面讨论函数 $z=f(x,y)$ 在点 $(x,y)$ 可微分的条件.

定理1（必要条件）如果函数 $z = f(x,y)$ 在点 $(x,y)$ 可微分，那么该函数在点 $(x,y)$ 的偏导数 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$ 必定存在，且函数 $z = f(x,y)$ 在点 $(x,y)$ 的全微分为

$$
\mathrm{d} z = \frac {\partial z}{\partial x} \Delta x + \frac {\partial z}{\partial y} \Delta y. \tag {3-3}
$$

证 设函数 $z=f(x,y)$ 在点 $P(x,y)$ 可微分. 于是, 对于点 P 的某个邻域内的任意一点 $P'(x+\Delta x,y+\Delta y)$ , (3-2) 式总成立. 特别当 $\Delta y=0$ 时 (3-2) 式也应成立, 这时 $\rho=|\Delta x|$ , 所以 (3-2) 式成为

$$
f (x + \Delta x, y) - f (x, y) = A \cdot \Delta x + o (\mid \Delta x \mid).
$$

① 这里, $\rho\rightarrow0$ 与 $(\Delta x,\Delta y)\rightarrow(0,0)$ 等价.

上式两端各除以 $\Delta x$ ，再令 $\Delta x \rightarrow 0$ 而取极限，就得

$$
\lim _ {\Delta x \rightarrow 0} \frac {f (x + \Delta x , y) - f (x , y)}{\Delta x} = A,
$$

从而偏导数 $\frac{\partial z}{\partial x}$ 存在，且等于 $A$ 。同样可证 $\frac{\partial z}{\partial y} = B$ 。所以(3-3)式成立。证毕。

我们知道,一元函数在某点的导数存在是微分存在的充分必要条件.但对于多元函数来说,情形就不同了.当函数的各偏导数都存在时,虽然能形式地写出 $\frac{\partial z}{\partial x}\Delta x+\frac{\partial z}{\partial y}\Delta y$ ,但它与 $\Delta z$ 之差并不一定是较 $\rho$ 高阶的无穷小,因此它不一定是函数的全微分.换句话说,各偏导数的存在只是全微分存在的必要条件而不是充分条件.例如,函数

$$
z = f (x, y) = \left\{ \begin{array}{l l} \frac {x y}{\sqrt {x ^ {2} + y ^ {2}}}, & x ^ {2} + y ^ {2} \neq 0, \\ 0, & x ^ {2} + y ^ {2} = 0 \end{array} \right.
$$

在点 $(0,0)$ 处有 $f_{x}(0,0) = 0$ 及 $f_{y}(0,0) = 0$ ，所以

$$
\Delta z - \left[ f _ {x} (0, 0) \cdot \Delta x + f _ {y} (0, 0) \cdot \Delta y \right] = \frac {\Delta x \cdot \Delta y}{\sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}}},
$$

如果考虑点 $P^{\prime}(\Delta x,\Delta y)$ 沿着直线 $y = x$ 趋于 $(0,0)$ ，那么

$$
\frac {\frac {\Delta x \cdot \Delta y}{\sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}}}}{\rho} = \frac {\Delta x \cdot \Delta y}{(\Delta x) ^ {2} + (\Delta y) ^ {2}} = \frac {\Delta x \cdot \Delta x}{(\Delta x) ^ {2} + (\Delta x) ^ {2}} = \frac {1}{2},
$$

它不能随 $\rho \to 0$ 而趋于0，这表示 $\rho \rightarrow 0$ 时，

$$
\Delta z - \left[ f _ {x} (0, 0) \Delta x + f _ {y} (0, 0) \Delta y \right]
$$

并不是较 $\rho$ 高阶的无穷小, 因此函数在点(0,0)处的全微分并不存在, 即函数在点(0,0)处是不可微分的.

由定理 1 及这个例子可知,偏导数存在是可微分的必要条件而不是充分条件.但是,如果再假定函数的各个偏导数连续,那么可以证明函数是可微分的,即有下面的定理.

定理2（充分条件）如果函数 $z = f(x,y)$ 的偏导数 $\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}$ 在点 $(x,y)$ 连续①，那么函数在该点可微分.

证 由假定,函数的偏导数 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$ 在点 $P(x,y)$ 的某邻域内存在.设点 $(x+\Delta x,y+\Delta y)$ 为该邻域内任意一点,考察函数的全增量

$$
\begin{array}{l} \Delta z = f (x + \Delta x, y + \Delta y) - f (x, y) \\ = [ f (x + \Delta x, y + \Delta y) - f (x, y + \Delta y) ] + [ f (x, y + \Delta y) - f (x, y) ]. \\ \end{array}
$$

在第一个方括号内的表达式,由于 $y+\Delta y$ 不变,因而可以看做是 x 的一元函数 $f(x,y+\Delta y)$ 的增量.于是,应用拉格朗日中值定理,得到

$$
f (x + \Delta x, y + \Delta y) - f (x, y + \Delta y) = f _ {x} (x + \theta_ {1} \Delta x, y + \Delta y) \Delta x \quad (0 <   \theta_ {1} <   1).
$$

又依假设， $f_{x}(x,y)$ 在点 $(x,y)$ 连续，所以上式可写为

$$
f (x + \Delta x, y + \Delta y) - f (x, y + \Delta y) = f _ {x} (x, y) \Delta x + \varepsilon_ {1} \Delta x, \tag {3-4}
$$

其中 $\varepsilon_{1}$ 为 $\Delta x$ 与 $\Delta y$ 的函数，且当 $\Delta x \to 0, \Delta y \to 0$ 时， $\varepsilon_{1} \to 0$ .

同理可证第二个方括号内的表达式可写为

$$
f (x, y + \Delta y) - f (x, y) = f _ {y} (x, y) \Delta y + \varepsilon_ {2} \Delta y, \tag {3-5}
$$

其中 $\varepsilon_{2}$ 为 $\Delta y$ 的函数，且当 $\Delta y \to 0$ 时， $\varepsilon_{2} \to 0$ .

由(3-4)、(3-5)两式可见,在偏导数连续的假定下,全增量 $\Delta z$ 可以表示为

$$
\Delta z = f _ {x} (x, y) \Delta x + f _ {y} (x, y) \Delta y + \varepsilon_ {1} \Delta x + \varepsilon_ {2} \Delta y. \tag {3-6}
$$

容易看出

$$
\left| \frac {\varepsilon_ {1} \Delta x + \varepsilon_ {2} \Delta y}{\rho} \right| \leqslant | \varepsilon_ {1} | + | \varepsilon_ {2} |,
$$

它是随着 $(\Delta x, \Delta y) \to (0, 0)$ 即 $\rho \to 0$ 而趋于零的.

这就证明了 $z = f(x,y)$ 在点 $P(x,y)$ 是可微分的.

以上关于二元函数全微分的定义及可微分的必要条件和充分条件,可以完全类似地推广到三元和三元以上的多元函数.

习惯上,我们将自变量的增量 $\Delta x$ 与 $\Delta y$ 分别记作 dx 与 dy,并分别称为自变量 x 与 y 的微分.这样,函数 $z=f(x,y)$ 的全微分就可写为

$$
\mathrm{d} z = \frac {\partial z}{\partial x} \mathrm{d} x + \frac {\partial z}{\partial y} \mathrm{d} y. \tag {3-7}
$$

通常把二元函数的全微分等于它的两个偏微分之和这个结论称为二元函数的微分符合叠加原理.

叠加原理也适用于二元以上的函数.例如,如果三元函数 $u=f(x,y,z)$ 可微分,那么它的全微分就等于它的三个偏微分之和,即

$$
\mathrm{d} u = \frac {\partial u}{\partial x} \mathrm{d} x + \frac {\partial u}{\partial y} \mathrm{d} y + \frac {\partial u}{\partial z} \mathrm{d} z.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/4a45b77fdcd4090b267abd6f3c2d580d74e9ca95d10e86d4a1ecc0f4f391c12e.jpg)


例 1 计算函数 $z=x^{2}y+y^{2}$ 的全微分.

解 因为 $\frac{\partial z}{\partial x} = 2xy, \frac{\partial z}{\partial y} = x^2 + 2y$ ，所以

$$
\mathrm{d} z = 2 x y \mathrm{d} x + (x ^ {2} + 2 y) \mathrm{d} y.
$$

例 2 计算函数 $z=e^{xy}$ 在点 $(2,1)$ 处的全微分.

解 因为

$$
\frac {\partial z}{\partial x} = y \mathrm{e} ^ {x y}, \frac {\partial z}{\partial y} = x \mathrm{e} ^ {x y}; \left. \frac {\partial z}{\partial x} \right| _ {\substack {x = 2 \\ y = 1}} = \mathrm{e} ^ {2}, \left. \frac {\partial z}{\partial y} \right| _ {\substack {x = 2 \\ y = 1}} = 2 \mathrm{e} ^ {2},
$$

所以

$$
\mathrm{dz}\Big|_{\substack{x = 2\\ y = 1}} = \mathrm{e}^{2}\mathrm{dx} + 2\mathrm{e}^{2}\mathrm{dy}.
$$

例 3 计算函数 $u = x + \sin \frac{y}{2} + e^{yz}$ 的全微分.

解 因为 $\frac{\partial u}{\partial x} = 1, \frac{\partial u}{\partial y} = \frac{1}{2}\cos \frac{y}{2} + ze^{yz}, \frac{\partial u}{\partial z} = ye^{yz}$ , 所以

$$
\mathrm{d} u = \mathrm{d} x + \left(\frac {1}{2} \cos \frac {y}{2} + z \mathrm{e} ^ {y z}\right) \mathrm{d} y + y \mathrm{e} ^ {y z} \mathrm{d} z.
$$

# *二、全微分在近似计算中的应用

由二元函数全微分的定义及关于全微分存在的充分条件可知,当二元函数 $z=f(x,y)$ 在点 $P(x,y)$ 的两个偏导数 $f_{x}(x,y)$ , $f_{y}(x,y)$ 连续,并且 $\left|\Delta x\right|$ , $\left|\Delta y\right|$ 都较小时,就有近似等式

$$
\Delta z \approx \mathrm{d} z = f _ {x} (x, y) \Delta x + f _ {y} (x, y) \Delta y. \tag {3-8}
$$

上式也可以写成

$$
f (x + \Delta x, y + \Delta y) \approx f (x, y) + f _ {x} (x, y) \Delta x + f _ {y} (x, y) \Delta y. \tag {3-9}
$$

与一元函数的情形相类似,可以利用(3-8)式或(3-9)式对二元函数作近似计算和误差估计,举例于下.

例 4 有一圆柱体受压后发生形变, 它的半径由 20 cm 增大到 20.05 cm, 高度由 100 cm 减少到 99 cm. 求此圆柱体体积变化的近似值.

解 设圆柱体的半径、高和体积依次为 r, h 和 V, 则有

$$
V = \pi r ^ {2} h.
$$

记 r, h 和 V 的增量依次为 $\Delta r, \Delta h$ 和 $\Delta V$ . 应用公式(3-8)，有

$$
\Delta V \approx \mathrm{d} V = V _ {r} \Delta r + V _ {h} \Delta h = 2 \pi r h \Delta r + \pi r ^ {2} \Delta h.
$$

把 $r = 20, h = 100, \Delta r = 0.05, \Delta h = -1$ 代入，得

$$
\Delta V \approx 2 \pi \times 2 0 \times 1 0 0 \times 0. 0 5 + \pi \times 2 0 ^ {2} \times (- 1) = - 2 0 0 \pi (\mathrm{cm} ^ {3}).
$$

即此圆柱体在受压后体积约减少了 $200 \pi \mathrm{~cm}^{3}$ .

例 5 计算 $1.04^{2.02}$ 的近似值.

解 设函数 $f(x, y) = x^y$ . 显然, 要计算的值就是函数在 $x = 1.04, y = 2.02$ 时的函数值 $f(1.04, 2.02)$ .

取 $x = 1, y = 2, \Delta x = 0.04, \Delta y = 0.02$ . 由于

$$
f _ {x} (x, y) = y x ^ {y - 1}, \quad f _ {y} (x, y) = x ^ {y} \ln x,
$$

$$
f (1, 2) = 1, \quad f _ {x} (1, 2) = 2, \quad f _ {y} (1, 2) = 0,
$$

所以,应用公式(3-9)便有

$$
1. 0 4 ^ {2. 0 2} \approx 1 + 2 \times 0. 0 4 + 0 \times 0. 0 2 = 1. 0 8.
$$

例6 利用单摆摆动测定重力加速度 $g$ 的公式是

$$
g = \frac {4 \pi^ {2} l}{T ^ {2}}.
$$

现测得单摆摆长 l 与振动周期 T 分别为 $l=(100\pm0.1)\mathrm{cm}, T=(2\pm0.004)\mathrm{s}$ . 问由于测定 l 与 T 的误差而引起 g 的绝对误差和相对误差各为多少①?

解 如果把测量 $l$ 与 $T$ 时所产生的误差当作 $|\Delta l|$ 与 $|\Delta T|$ ，那么利用上述计算公式所产生的误差就是二元函数 $g = \frac{4\pi^2l}{T^2}$ 的全增量的绝对值 $|\Delta g|$ . 由于 $|\Delta l|, |\Delta T|$ 都很小，因此我们可以用 $\mathrm{dg}$ 来近似地代替 $\Delta g$ . 这样就得到 $g$ 的误差为

$$
\begin{array}{l} \mid \Delta g \mid \approx \mid \mathrm{d} g \mid = \left| \frac {\partial g}{\partial l} \Delta l + \frac {\partial g}{\partial T} \Delta T \right| \\ \leqslant \left| \frac {\partial g}{\partial l} \right| \cdot \delta_ {l} + \left| \frac {\partial g}{\partial T} \right| \cdot \delta_ {T} = 4 \pi^ {2} \left(\frac {1}{T ^ {2}} \delta_ {l} + \frac {2 l}{T ^ {3}} \delta_ {T}\right), \\ \end{array}
$$

其中 $\delta_{l}$ 与 $\delta_{T}$ 分别为 l 与 T 的绝对误差. 把 $l=100\ cm, T=2\ s, \delta_{l}=0.1\ cm, \delta_{T}=0.004\ s$ 代入上式, 得 g 的绝对误差约为

$$
\delta_ {g} = 4 \pi^ {2} \left(\frac {0 . 1}{2 ^ {2}} + \frac {2 \times 1 0 0}{2 ^ {3}} \times 0. 0 0 4\right) = 0. 5 \pi^ {2} \approx 4. 9 3 (\mathrm{cm/s} ^ {2}).
$$

从而 $g$ 的相对误差约为

$$
\frac {\delta_ {g}}{g} = \frac {0 . 5 \pi^ {2}}{\frac {4 \pi^ {2} \times 1 0 0}{2 ^ {2}}} = 0.5 \%.
$$

从上面的例子可以看到,对于一般的二元函数 $z=f(x,y)$ , 如果自变量 x,y 的绝对误差分别为 $\delta_{x},\delta_{y}$ , 即

$$
\mid \Delta x \mid \leqslant \delta_ {x}, \quad \mid \Delta y \mid \leqslant \delta_ {y},
$$

那么 $z$ 的误差

$$
\begin{array}{l} \mid \Delta z \mid \approx \mid \mathrm{d} z \mid = \left| \frac {\partial z}{\partial x} \Delta x + \frac {\partial z}{\partial y} \Delta y \right| \\ \leqslant \left| \frac {\partial z}{\partial x} \right| \cdot | \Delta x | + \left| \frac {\partial z}{\partial y} \right| \cdot | \Delta y | \leqslant \left| \frac {\partial z}{\partial x} \right| \delta_ {x} + \left| \frac {\partial z}{\partial y} \right| \delta_ {y}, \\ \end{array}
$$

从而得到 $z$ 的绝对误差约为

$$
\delta_ {z} = \left| \frac {\partial z}{\partial x} \right| \delta_ {x} + \left| \frac {\partial z}{\partial y} \right| \delta_ {y}, \tag {3-10}
$$

$z$ 的相对误差约为

$$
\frac {\delta_ {z}}{| z |} = \left| \frac {\frac {\partial z}{\partial x}}{z} \right| \delta_ {x} + \left| \frac {\frac {\partial z}{\partial y}}{z} \right| \delta_ {y}. \tag {3-11}
$$

# 习题9-3

1. 求下列函数的全微分：

(1) $z = xy + \frac{x}{y}$ ; 

(2) $z = \mathrm{e}^{\frac{y}{x}};$ 

(3) $z = \frac{y}{\sqrt{x^2 + y^2}};$ 

(4) $u = x^{yz}$ . 

2. 求函数 $z=\ln(1+x^{2}+y^{2})$ 当 x=1, y=2 时的全微分.

3. 求函数 $z=\frac{y}{x}$ 当 x=2, y=1, $\Delta x=0.1$ , $\Delta y=-0.2$ 时的全增量和全微分.

4. 求函数 $z=e^{xy}$ 当 x=1, y=1, $\Delta x=0.15$ , $\Delta y=0.1$ 时的全微分.

5. 考虑二元函数 $f(x, y)$ 的下面四条性质：

(1) $f(x,y)$ 在点 $(x_{0},y_{0})$ 连续；
(2) $f_{x}(x,y)$ , $f_{y}(x,y)$ 在点 $(x_{0},y_{0})$ 连续；

(3) $f(x,y)$ 在点 $(x_0,y_0)$ 可微分； (4) $f_{x}(x_{0},y_{0}),f_{y}(x_{0},y_{0})$ 存在.

若用“ $P \Rightarrow Q$ ”表示可由性质 P 推出性质 Q，则下列四个选项中正确的是()。

(A) (2) $\Rightarrow$ (3) $\Rightarrow$ (1) 

(B) (3) $\Rightarrow$ (2) $\Rightarrow$ (1) 

(C) (3) $\Rightarrow$ (4) $\Rightarrow$ (1) 

(D) (3) $\Rightarrow$ (1) $\Rightarrow$ (4) 

*6. 计算 $\sqrt{1.02^3 + 1.97^3}$ 的近似值.

*7. 计算 $1.97^{1.05}$ 的近似值 (ln 2=0.693).

*8. 已知边长为 $x = 6 \mathrm{~m}$ 与 $y = 8 \mathrm{~m}$ 的矩形, 如果 $x$ 边增加 $5 \mathrm{~cm}$ 而 $y$ 边减少 $10 \mathrm{~cm}$ , 问这个矩形的对角线的近似变化怎样?

*9. 设有一无盖圆柱形容器, 容器的壁与底的厚度均为 $0.1 \mathrm{~cm}$ , 内高为 $20 \mathrm{~cm}$ , 内半径为 $4 \mathrm{~cm}$ . 求这个容器外壳体积的近似值.

* 10. 设有直角三角形, 测得其两直角边的长分别为 $(7 \pm 0.1) \mathrm{cm}$ 和 $(24 \pm 0.1) \mathrm{cm}$ . 试求利用上述两值来计算斜边长度时的绝对误差.

*11. 测得一块三角形土地的两边边长分别为 $(63 \pm 0.1) \mathrm{~m}$ 和 $(78 \pm 0.1) \mathrm{~m}$ , 这两边的夹角为 $60^{\circ} \pm 1^{\circ}$ . 试求这块三角形土地面积的近似值, 并求其绝对误差和相对误差.

* 12. 利用全微分证明:两数之和的绝对误差等于它们各自的绝对误差之和.

*13. 利用全微分证明:乘积的相对误差等于各因子的相对误差之和,商的相对误差等于被除数及除数的相对误差之和.

# 第四节 多元复合函数的求导法则

本节要将一元函数微分学中复合函数的求导法则推广到多元复合函数的情形.多元复合函数的求导法则在多元函数微分学中也起着重要作用.

下面按照多元复合函数不同的复合情形,分三种情形讨论.

# 1. 一元函数与多元函数复合的情形

定理1 如果函数 $u = \varphi(t)$ 及 $v = \psi(t)$ 都在点 $t$ 可导, 函数 $z = f(u, v)$ 在对应点 $(u, v)$ 具有连续偏导数, 那么复合函数 $z = f[\varphi(t), \psi(t)]$ 在点 $t$ 可导, 且有

$$
\frac {\mathrm{d} z}{\mathrm{d} t} = \frac {\partial z}{\partial u} \frac {\mathrm{d} u}{\mathrm{d} t} + \frac {\partial z}{\partial v} \frac {\mathrm{d} v}{\mathrm{d} t}. \tag {4-1}
$$

证 设 $t$ 获得增量 $\Delta t$ , 这时 $u = \varphi(t), v = \psi(t)$ 的对应增量为 $\Delta u, \Delta v$ , 由此, 函数 $z = f(u, v)$ 相应地获得增量 $\Delta z$ . 按假定, 函数 $z = f(u, v)$ 在点 $(u, v)$ 具有连续偏导数, 这时函数的全增量 $\Delta z$ 可表示为

$$
\Delta z = \frac {\partial z}{\partial u} \Delta u + \frac {\partial z}{\partial v} \Delta v + \varepsilon_ {1} \Delta u + \varepsilon_ {2} \Delta v,
$$

这里，当 $\Delta u\to 0,\Delta v\to 0$ 时， $\varepsilon_{1}\rightarrow 0,\varepsilon_{2}\rightarrow 0.$ ①

将上式两端各除以 $\Delta t$ ，得

$$
\frac {\Delta z}{\Delta t} = \frac {\partial z}{\partial u} \frac {\Delta u}{\Delta t} + \frac {\partial z}{\partial v} \frac {\Delta v}{\Delta t} + \varepsilon_ {1} \frac {\Delta u}{\Delta t} + \varepsilon_ {2} \frac {\Delta v}{\Delta t}.
$$

因为当 $\Delta t\to 0$ 时， $\Delta u\rightarrow 0,\Delta v\rightarrow 0,\frac{\Delta u}{\Delta t}\xrightarrow{\mathrm{d}u}\frac{\mathrm{d}u}{\mathrm{d}t},\frac{\Delta v}{\Delta t}\xrightarrow{\mathrm{d}v}\frac{\mathrm{d}v}{\mathrm{d}t}$ 所以

$$
\lim _ {\Delta t \rightarrow 0} \frac {\Delta z}{\Delta t} = \frac {\partial z}{\partial u} \frac {\mathrm{d} u}{\mathrm{d} t} + \frac {\partial z}{\partial v} \frac {\mathrm{d} v}{\mathrm{d} t}.
$$

这就证明了复合函数 $z = f[\varphi (t),\psi (t)]$ 在点 $t$ 可导，且其导数可用公式(4-1)计算.证毕.

用同样的方法,可把定理推广到复合函数的中间变量多于两个的情形.例如,设 $z=f(u,v,w)$ , $u=\varphi(t)$ , $v=\psi(t)$ , $w=\omega(t)$ 复合而得复合函数

$$
z = f [ \varphi (t), \psi (t), \omega (t) ],
$$

则在与定理相类似的条件下,这个复合函数在点 t 可导,且其导数可用下列公式计算:

$$
\frac {\mathrm{d} z}{\mathrm{d} t} = \frac {\partial z}{\partial u} \frac {\mathrm{d} u}{\mathrm{d} t} + \frac {\partial z}{\partial v} \frac {\mathrm{d} v}{\mathrm{d} t} + \frac {\partial z}{\partial w} \frac {\mathrm{d} w}{\mathrm{d} t}. \tag {4-2}
$$

公式(4-1)及(4-2)中的导数 $\frac{dz}{dt}$ 称为全导数.

# 2. 多元函数与多元函数复合的情形

定理2 如果函数 $u = \varphi(x, y)$ 及 $v = \psi(x, y)$ 都在点 $(x, y)$ 具有对 $x$ 及对 $y$ 的偏导数，函数 $z = f(u, v)$ 在对应点 $(u, v)$ 具有连续偏导数，那么复合函数 $z = f[\varphi(x, y), \psi(x, y)]$ 在点 $(x, y)$ 的两个偏导数都存在，且有

$$
\frac {\partial z}{\partial x} = \frac {\partial z}{\partial u} \frac {\partial u}{\partial x} + \frac {\partial z}{\partial v} \frac {\partial v}{\partial x}, \tag {4-3}
$$

$$
\frac {\partial z}{\partial y} = \frac {\partial z}{\partial u} \frac {\partial u}{\partial y} + \frac {\partial z}{\partial v} \frac {\partial v}{\partial y}. \tag {4-4}
$$

事实上,这里求 $\frac{\partial z}{\partial x}$ 时,将y看做常量,因此 $u=\varphi(x,y)$ 及 $v=\psi(x,y)$ 仍可看做一元函数而应用定理1.但由于复合函数 $z=f[\varphi(x,y),\psi(x,y)]$ 以及 $u=\varphi(x,y)$ 和 $v=\psi(x,y)$ 都是x,y的二元函数,所以应把(4-1)式中的d改为 $\partial$ ,再把t换成x,这样便由(4-1)式得(4-3)式.同理由(4-1)式可得(4-4)式.

类似地, 设 $u=\varphi(x,y)$ , $v=\psi(x,y)$ 及 $w=\omega(x,y)$ 都在点 $(x,y)$ 具有对 x 及对 y 的偏导数, 函数 $z=f(u,v,w)$ 在对应点 $(u,v,w)$ 具有连续偏导数, 则复合函数

$$
z = f [ \varphi (x, y), \psi (x, y), \omega (x, y) ]
$$

在点 $(x, y)$ 的两个偏导数都存在，且可用下列公式计算：

$$
\frac {\partial z}{\partial x} = \frac {\partial z}{\partial u} \frac {\partial u}{\partial x} + \frac {\partial z}{\partial v} \frac {\partial v}{\partial x} + \frac {\partial z}{\partial w} \frac {\partial w}{\partial x}, \tag {4-5}
$$

$$
\frac {\partial z}{\partial y} = \frac {\partial z}{\partial u} \frac {\partial u}{\partial y} + \frac {\partial z}{\partial v} \frac {\partial v}{\partial y} + \frac {\partial z}{\partial w} \frac {\partial w}{\partial y}. \tag {4-6}
$$

# 3. 其他情形

定理3 如果函数 $u = \varphi (x,y)$ 在点 $(x,y)$ 具有对 $x$ 及对 $y$ 的偏导数，函数 $v = \psi (y)$ 

在点 $y$ 可导, 函数 $z = f(u, v)$ 在对应点 $(u, v)$ 具有连续偏导数, 那么复合函数 $z = f[\varphi(x, y), \psi(y)]$ 在点 $(x, y)$ 的两个偏导数都存在, 且有

$$
\frac {\partial z}{\partial x} = \frac {\partial z}{\partial u} \frac {\partial u}{\partial x}, \tag {4-7}
$$

$$
\frac {\partial z}{\partial y} = \frac {\partial z}{\partial u} \frac {\partial u}{\partial y} + \frac {\partial z}{\partial v} \frac {\mathrm{d} v}{\mathrm{d} y}. \tag {4-8}
$$

上述情形实际上是情形2的一种特例,即在情形2中,如变量v与x无关,从而 $\frac{\partial v}{\partial x}=0$ ;在v对y求导时,由于 $v=\psi(y)$ 是一元函数,故 $\frac{\partial v}{\partial y}$ 换成了 $\frac{dv}{dy}$ ,这就得出上述结果.

在情形3中,还会遇到这样的情形:复合函数的某些中间变量本身又是复合函数的自变量.例如,设 $z=f(u,x,y)$ 具有连续偏导数,而 $u=\varphi(x,y)$ 具有偏导数,则复合函数 $z=f[\varphi(x,y),x,y]$ 可看做情形2中当v=x,w=y的特殊情形.因此

$$
\frac {\partial v}{\partial x} = 1, \quad \frac {\partial w}{\partial x} = 0, \quad \frac {\partial v}{\partial y} = 0, \quad \frac {\partial w}{\partial y} = 1.
$$

从而复合函数 $z = f[\varphi (x,y),x,y]$ 具有对自变量 $x$ 及 $y$ 的偏导数，且由公式(4-5)、(4-6)得

$$
\frac {\partial z}{\partial x} = \frac {\partial f}{\partial u} \frac {\partial u}{\partial x} + \frac {\partial f}{\partial x}, \quad \frac {\partial z}{\partial y} = \frac {\partial f}{\partial u} \frac {\partial u}{\partial y} + \frac {\partial f}{\partial y}.
$$

注意 这里 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial f}{\partial x}$ 是不同的, $\frac{\partial z}{\partial x}$ 是把复合函数 $z = f[\varphi(x, y), x, y]$ 中的 $y$ 看做不变而对 $x$ 的偏导数, $\frac{\partial f}{\partial x}$ 是把 $f(u, x, y)$ 中的 $u$ 及 $y$ 看做不变而对 $x$ 的偏导数. $\frac{\partial z}{\partial y}$ 与 $\frac{\partial f}{\partial y}$ 也有类似的区别.

例1 设 $z = \mathrm{e}^u\sin v$ ，而 $u = xy, v = x + y.$ 求 $\frac{\partial z}{\partial x}$ 和 $\frac{\partial z}{\partial y}$ .

解 $\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} +\frac{\partial z}{\partial v}\frac{\partial v}{\partial x} = \mathrm{e}^u\sin v\cdot y + \mathrm{e}^u\cos v\cdot 1 = \mathrm{e}^{xy}[y\sin (x + y) + \cos (x + y)],$ 

$$
\frac {\partial z}{\partial y} = \frac {\partial z}{\partial u} \frac {\partial u}{\partial y} + \frac {\partial z}{\partial v} \frac {\partial v}{\partial y} = e ^ {u} \sin v \cdot x + e ^ {u} \cos v \cdot 1 = e ^ {x y} [ x \sin (x + y) + \cos (x + y) ].
$$

例2 设 $u = f(x, y, z) = \mathrm{e}^{x^2 + y^2 + z^2}$ , 而 $z = x^2 \sin y$ . 求 $\frac{\partial u}{\partial x}$ 和 $\frac{\partial u}{\partial y}$ .

解 $\frac{\partial u}{\partial x} = \frac{\partial f}{\partial x} +\frac{\partial f}{\partial z}\frac{\partial z}{\partial x} = 2x\mathrm{e}^{x^2 +y^2 +z^2} + 2z\mathrm{e}^{x^2 +y^2 +z^2}\cdot 2x\sin y = 2x(1 + 2x^2\sin^2 y)\mathrm{e}^{x^2 +y^2 +x^4\sin^2 y}.$ 

$$
\frac {\partial u}{\partial y} = \frac {\partial f}{\partial y} + \frac {\partial f}{\partial z} \frac {\partial z}{\partial y} = 2 y \mathrm{e} ^ {x ^ {2} + y ^ {2} + z ^ {2}} + 2 z \mathrm{e} ^ {x ^ {2} + y ^ {2} + z ^ {2}} \cdot x ^ {2} \cos y = 2 (y + x ^ {4} \sin y \cos y) \mathrm{e} ^ {x ^ {2} + y ^ {2} + x ^ {4} \sin^ {2} y}.
$$

例3 设 $z = f(u, v, t) = uv + \sin t$ ，而 $u = e^t, v = \cos t$ . 求全导数 $\frac{\mathrm{d}z}{\mathrm{d}t}$ .

解 $\frac{\mathrm{d}z}{\mathrm{d}t} = \frac{\partial f}{\partial u}\frac{\mathrm{d}u}{\mathrm{d}t} +\frac{\partial f}{\partial v}\frac{\mathrm{d}v}{\mathrm{d}t} +\frac{\partial f}{\partial t} = v\mathrm{e}^t -u\sin t + \cos t$ 

$$
= \mathrm{e} ^ {t} \cos t - \mathrm{e} ^ {t} \sin t + \cos t = \mathrm{e} ^ {t} (\cos t - \sin t) + \cos t.
$$

例4 设 $w = f(x + y + z, xyz)$ , $f$ 具有二阶连续偏导数, 求 $\frac{\partial w}{\partial x}$ 及 $\frac{\partial^2 w}{\partial x \partial z}$ .

解 令 $u = x + y + z, v = xyz$ ，则 $w = f(u, v)$ .

因所给函数由 $w = f(u, v)$ 及 $u = x + y + z, v = xyz$ 复合而成，根据复合函数求导法则，有

$$
\frac {\partial w}{\partial x} = \frac {\partial f}{\partial u} \frac {\partial u}{\partial x} + \frac {\partial f}{\partial v} \frac {\partial v}{\partial x} = f _ {u} + y z f _ {v},
$$

$$
\frac {\partial^ {2} w}{\partial x \partial z} = \frac {\partial}{\partial z} (f _ {u} + y z f _ {v}) = \frac {\partial f _ {u}}{\partial z} + y f _ {v} + y z \frac {\partial f _ {v}}{\partial z}.
$$

求 $\frac{\partial f_u}{\partial z}$ 及 $\frac{\partial f_v}{\partial z}$ 时，应注意 $f_{u}(u,v)$ 及 $f_{v}(u,v)$ 中 $u,v$ 是中间变量，根据复合函数求导法则，有

$$
\frac {\partial f _ {u}}{\partial z} = \frac {\partial f _ {u}}{\partial u} \frac {\partial u}{\partial z} + \frac {\partial f _ {u}}{\partial v} \frac {\partial v}{\partial z} = f _ {u u} + x y f _ {u v},
$$

$$
\frac {\partial f _ {v}}{\partial z} = \frac {\partial f _ {v}}{\partial u} \frac {\partial u}{\partial z} + \frac {\partial f _ {v}}{\partial v} \frac {\partial v}{\partial z} = f _ {v u} + x y f _ {v v},
$$

于是

$$
\frac {\partial^ {2} w}{\partial x \partial z} = f _ {u u} + x y f _ {u v} + y f _ {v} + y z f _ {v u} + x y ^ {2} z f _ {v v} = f _ {u u} + y (x + z) f _ {u v} + x y ^ {2} z f _ {v v} + y f _ {v}.
$$

有时,为表达简便起见,引入以下记号:

$$
f _ {1} ^ {\prime} (u, v) = f _ {u} (u, v), \quad f _ {2} ^ {\prime} (u, v) = f _ {v} (u, v), \quad f _ {1 2} ^ {\prime \prime} (u, v) = f _ {u v} (u, v),
$$

这里,下标1表示对第一个变量u求偏导数,下标2表示对第二个变量v求偏导数.同理有 $f_{11}^{\prime\prime},f_{22}^{\prime\prime},f_{21}^{\prime\prime}$ 等.利用这种记号,例4的结果可表示成

$$
\frac {\partial w}{\partial x} = f _ {1} ^ {\prime} + y z f _ {2} ^ {\prime},
$$

$$
\frac {\partial^ {2} w}{\partial x \partial z} = f _ {1 1} ^ {\prime \prime} + y (x + z) f _ {1 2} ^ {\prime \prime} + x y ^ {2} z f _ {2 2} ^ {\prime \prime} + y f _ {2} ^ {\prime}.
$$

例 5 设 $u=f(x,y)$ 的所有二阶偏导数连续, 把下列表达式转换为极坐标系中的形式:

(1) $\left(\frac{\partial u}{\partial x}\right)^{2}+\left(\frac{\partial u}{\partial y}\right)^{2};$ 

(2) $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}$ . 

解 由直角坐标与极坐标间的关系式

$$
x = \rho \cos \theta , \quad y = \rho \sin \theta ,
$$

可把函数 $u = f(x,y)$ 换成极坐标 $\rho$ 及 $\theta$ 的函数：

$$
u = f (x, y) = f (\rho \cos \theta , \rho \sin \theta) = F (\rho , \theta).
$$

现在要将式子 $\left(\frac{\partial u}{\partial x}\right)^2 +\left(\frac{\partial u}{\partial y}\right)^2$ 及 $\frac{\partial^2u}{\partial x^2} +\frac{\partial^2u}{\partial y^2}$ 用 $\rho ,\theta$ 及函数 $u = F(\rho ,\theta)$ 对 $\rho ,\theta$ 的偏导数来表达.为此，要求出 $u = f(x,y)$ 的偏导数 $\frac{\partial u}{\partial x},\frac{\partial u}{\partial y},\frac{\partial^2u}{\partial x^2}$ 及 $\frac{\partial^2u}{\partial y^2}$ 这里 $u = f(x,y)$ 要看做由 $u = F(\rho ,\theta)$ 及

$$
\rho = \sqrt {x ^ {2} + y ^ {2}}, \quad \theta = \arctan \frac {y}{x} ①
$$

复合而成,应用复合函数求导法则,得

$$
\frac {\partial u}{\partial x} = \frac {\partial u}{\partial \rho} \frac {\partial \rho}{\partial x} + \frac {\partial u}{\partial \theta} \frac {\partial \theta}{\partial x} = \frac {\partial u}{\partial \rho} \frac {x}{\rho} - \frac {\partial u}{\partial \theta} \frac {y}{\rho^ {2}} = \frac {\partial u}{\partial \rho} \cos \theta - \frac {\partial u}{\partial \theta} \frac {\sin \theta}{\rho},
$$

$$
\frac {\partial u}{\partial y} = \frac {\partial u}{\partial \rho} \frac {\partial \rho}{\partial y} + \frac {\partial u}{\partial \theta} \frac {\partial \theta}{\partial y} = \frac {\partial u}{\partial \rho} \frac {y}{\rho} + \frac {\partial u}{\partial \theta} \frac {x}{\rho^ {2}} = \frac {\partial u}{\partial \rho} \sin \theta + \frac {\partial u}{\partial \theta} \frac {\cos \theta}{\rho}.
$$

两式平方后相加,得

$$
\left(\frac {\partial u}{\partial x}\right) ^ {2} + \left(\frac {\partial u}{\partial y}\right) ^ {2} = \left(\frac {\partial u}{\partial \rho}\right) ^ {2} + \frac {1}{\rho^ {2}} \left(\frac {\partial u}{\partial \theta}\right) ^ {2}.
$$

再求二阶偏导数,得

$$
\begin{array}{l} \frac {\partial^ {2} u}{\partial x ^ {2}} = \frac {\partial}{\partial \rho} \left(\frac {\partial u}{\partial x}\right) \cdot \frac {\partial \rho}{\partial x} + \frac {\partial}{\partial \theta} \left(\frac {\partial u}{\partial x}\right) \cdot \frac {\partial \theta}{\partial x} \\ = \left[ \frac {\partial}{\partial \rho} \left(\frac {\partial u}{\partial \rho} \cos \theta - \frac {\partial u}{\partial \theta} \frac {\sin \theta}{\rho}\right) \right] \cdot \cos \theta - \left[ \frac {\partial}{\partial \theta} \left(\frac {\partial u}{\partial \rho} \cos \theta - \frac {\partial u}{\partial \theta} \frac {\sin \theta}{\rho}\right) \right] \cdot \frac {\sin \theta}{\rho} \\ = \frac {\partial^ {2} u}{\partial \rho^ {2}} \cos^ {2} \theta - \frac {\partial^ {2} u}{\partial \rho \partial \theta} \frac {\sin 2 \theta}{\rho} + \frac {\partial^ {2} u}{\partial \theta^ {2}} \frac {\sin^ {2} \theta}{\rho^ {2}} + \frac {\partial u}{\partial \theta} \frac {\sin 2 \theta}{\rho^ {2}} + \frac {\partial u}{\partial \rho} \frac {\sin^ {2} \theta}{\rho}. \\ \end{array}
$$

同理可得

$$
\frac {\partial^ {2} u}{\partial y ^ {2}} = \frac {\partial^ {2} u}{\partial \rho^ {2}} \sin^ {2} \theta + \frac {\partial^ {2} u}{\partial \rho \partial \theta} \frac {\sin 2 \theta}{\rho} + \frac {\partial^ {2} u}{\partial \theta^ {2}} \frac {\cos^ {2} \theta}{\rho^ {2}} - \frac {\partial u}{\partial \theta} \frac {\sin 2 \theta}{\rho^ {2}} + \frac {\partial u}{\partial \rho} \frac {\cos^ {2} \theta}{\rho}.
$$

① 当点 $P(x, y)$ 在第一、四象限时，规定 $\theta$ 的取值范围为 $-\frac{\pi}{2} < \theta < \frac{\pi}{2}$ ，则

$$
\theta = \arctan \frac {y}{x};
$$

当点 $P(x,y)$ 在第二、三象限时，规定 $\theta$ 的取值范围为 $\frac{\pi}{2} < \theta < \frac{3}{2}\pi$ ，则

$$
\theta = \arctan \frac {y}{x} + \pi ,
$$

此时以下推导仍成立.

两式相加, 得

$$
\frac {\partial^ {2} u}{\partial x ^ {2}} + \frac {\partial^ {2} u}{\partial y ^ {2}} = \frac {\partial^ {2} u}{\partial \rho^ {2}} + \frac {1}{\rho} \frac {\partial u}{\partial \rho} + \frac {1}{\rho^ {2}} \frac {\partial^ {2} u}{\partial \theta^ {2}} = \frac {1}{\rho^ {2}} \left[ \rho \frac {\partial}{\partial \rho} \left(\rho \frac {\partial u}{\partial \rho}\right) + \frac {\partial^ {2} u}{\partial \theta^ {2}} \right].
$$

全微分形式不变性 设函数 $z=f(u,v)$ 具有连续偏导数, 则有全微分

$$
\mathrm{d} z = \frac {\partial z}{\partial u} \mathrm{d} u + \frac {\partial z}{\partial v} \mathrm{d} v.
$$

如果 u 和 v 又是中间变量, 即 $u = \varphi(x, y)$ , $v = \psi(x, y)$ , 且这两个函数也具有连续偏导数, 那么复合函数

$$
z = f [ \varphi (x, y), \psi (x, y) ]
$$

的全微分为

$$
\mathrm{d} z = \frac {\partial z}{\partial x} \mathrm{d} x + \frac {\partial z}{\partial y} \mathrm{d} y,
$$

其中 $\frac{\partial z}{\partial x}$ 及 $\frac{\partial z}{\partial y}$ 分别由公式(4-3)及(4-4)给出.把公式(4-3)及(4-4)中的 $\frac{\partial z}{\partial x}$ 及 $\frac{\partial z}{\partial y}$ 代入上式,得

$$
\begin{array}{l} \mathrm{d} z = \left(\frac {\partial z}{\partial u} \frac {\partial u}{\partial x} + \frac {\partial z}{\partial v} \frac {\partial v}{\partial x}\right) \mathrm{d} x + \left(\frac {\partial z}{\partial u} \frac {\partial u}{\partial y} + \frac {\partial z}{\partial v} \frac {\partial v}{\partial y}\right) \mathrm{d} y \\ = \frac {\partial z}{\partial u} \left(\frac {\partial u}{\partial x} \mathrm{d} x + \frac {\partial u}{\partial y} \mathrm{d} y\right) + \frac {\partial z}{\partial v} \left(\frac {\partial v}{\partial x} \mathrm{d} x + \frac {\partial v}{\partial y} \mathrm{d} y\right) = \frac {\partial z}{\partial u} \mathrm{d} u + \frac {\partial z}{\partial v} \mathrm{d} v. \\ \end{array}
$$

由此可见,无论 u 和 v 是自变量还是中间变量,函数 $z=f(u,v)$ 的全微分形式是一样的.这个性质叫做全微分形式不变性.

例 6 利用全微分形式不变性解本节的例 1.

解 $\mathrm{dz} = \mathrm{d}\left(\mathrm{e}^u\sin v\right) = \mathrm{e}^u\sin v\mathrm{d}u + \mathrm{e}^u\cos v\mathrm{d}v,$ 

因

$$
\mathrm{d} u = \mathrm{d} (x y) = y \mathrm{d} x + x \mathrm{d} y, \mathrm{d} v = \mathrm{d} (x + y) = \mathrm{d} x + \mathrm{d} y,
$$

代入后归并含 dx 及 dy 的项, 得

$$
\mathrm{d} z = \left(\mathrm{e} ^ {u} \sin v \cdot y + \mathrm{e} ^ {u} \cos v\right) \mathrm{d} x + \left(\mathrm{e} ^ {u} \sin v \cdot x + \mathrm{e} ^ {u} \cos v\right) \mathrm{d} y,
$$

即

$$
\frac {\partial z}{\partial x} \mathrm{d} x + \frac {\partial z}{\partial y} \mathrm{d} y = \mathrm{e} ^ {x y} [ y \sin (x + y) + \cos (x + y) ] \mathrm{d} x + \mathrm{e} ^ {x y} [ x \sin (x + y) + \cos (x + y) ] \mathrm{d} y.
$$

比较上式两端的 dx 和 dy 的系数, 就同时得到两个偏导数 $\frac{\partial z}{\partial x}$ 和 $\frac{\partial z}{\partial y}$ , 它们与例 1 的结果一样.

# 习题9-4

1. 设 $z = u^2 + v^2$ ，而 $u = x + y, v = x - y$ ，求 $\frac{\partial z}{\partial x}, \frac{\partial z}{\partial y}$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/4d3c8b375fa6da32c69e1b350534432383eb83df6d6571d9ec283be352e4f422.jpg)


释疑解难

9-3 

2. 设 $z = u^2 \ln v$ ，而 $u = \frac{x}{y}, v = 3x - 2y$ ，求 $\frac{\partial z}{\partial x}, \frac{\partial z}{\partial y}$ .

3. 设 $z = \mathrm{e}^{x - 2y}$ , 而 $x = \sin t, y = t^3$ , 求 $\frac{\mathrm{d}z}{\mathrm{d}t}$ .

4. 设 $z = \arcsin (x - y)$ , 而 $x = 3t, y = 4t^3$ , 求 $\frac{\mathrm{d}z}{\mathrm{d}t}$ .

5. 设 $z = \arctan(xy)$ ，而 $y = e^{x}$ ，求 $\frac{dz}{dx}$ .

6. 设 $u = \frac{\mathrm{e}^{ax}(y - z)}{a^2 + 1}$ , 而 $y = a\sin x, z = \cos x$ , 求 $\frac{\mathrm{d}u}{\mathrm{d}x}$ .

7. 设 $z = \arctan \frac{x}{y}$ , 而 $x = u + v, y = u - v$ , 验证 $\frac{\partial z}{\partial u} + \frac{\partial z}{\partial v} = \frac{u - v}{u^2 + v^2}$ .

8. 求下列函数的一阶偏导数（其中 f 具有一阶连续偏导数）：

(1) $u = f(x^{2} - y^{2},\mathrm{e}^{xy})$ 

(2) $u = f\left(\frac{x}{y},\frac{y}{z}\right)$ ; 

(3) $u=f(x,xy,xyz)$ . 

9. 设 $z = xy + xF(u)$ , 而 $u = \frac{y}{x}, F(u)$ 为可导函数, 证明 $x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y} = z + xy$ .

10. 设 $z = \frac{y}{f(x^2 - y^2)}$ ，其中 $f(u)$ 为可导函数，验证 $\frac{1}{x} \frac{\partial z}{\partial x} + \frac{1}{y} \frac{\partial z}{\partial y} = \frac{z}{y^2}$ .

11. 设函数 $f(x, y, z)$ 满足 $f(tx, ty, tz) = t^n f(x, y, z)$ ( $t$ 为任意实数), 则称函数 $f$ 为 $n$ 次齐次函数. 证明: $n$ 次齐次函数 $f$ 满足关系式

$$
x f _ {x} + y f _ {y} + z f _ {z} = n f (x, y, z),
$$

其中函数f具有一阶连续偏导数.

12. 设 $z = f(x^2 + y^2)$ ，其中 $f$ 具有二阶导数，求 $\frac{\partial^2 z}{\partial x^2}, \frac{\partial^2 z}{\partial x \partial y}, \frac{\partial^2 z}{\partial y^2}$ .

* 13. 求下列函数的 $\frac{\partial^2 z}{\partial x^2}, \frac{\partial^2 z}{\partial x \partial y}, \frac{\partial^2 z}{\partial y^2}$ （其中 $f$ 具有二阶连续偏导数）：

(1) $z=f(xy,y)$ ; 

(2) $z = f\left(x, \frac{x}{y}\right)$ ; 

(3) $z=f(xy^{2},x^{2}y)$ ; 

(4) $z = f(\sin x, \cos y, e^{x + y})$ . 

*14. 设 $u = f(x, y)$ 的所有二阶偏导数连续，而

$$
x = \frac {s - \sqrt {3} t}{2}, \quad y = \frac {\sqrt {3} s + t}{2},
$$

证明

$$
\left(\frac {\partial u}{\partial x}\right) ^ {2} + \left(\frac {\partial u}{\partial y}\right) ^ {2} = \left(\frac {\partial u}{\partial s}\right) ^ {2} + \left(\frac {\partial u}{\partial t}\right) ^ {2} \quad \text {及} \quad \frac {\partial^ {2} u}{\partial x ^ {2}} + \frac {\partial^ {2} u}{\partial y ^ {2}} = \frac {\partial^ {2} u}{\partial s ^ {2}} + \frac {\partial^ {2} u}{\partial t ^ {2}}.
$$

# 第五节 隐函数的求导公式

# 一、一个方程的情形

在第二章第四节中我们已经提出了隐函数的概念,并且指出了不经过显化直接由方程

$$
F (x, y) = 0 \tag {5-1}
$$

求它所确定的隐函数的导数的方法. 现在介绍隐函数存在定理, 并根据多元复合函数的求导法来导出隐函数的导数公式.

隐函数存在定理1 设函数 $F(x, y)$ 在点 $P(x_0, y_0)$ 的某一邻域内具有连续偏导数，且 $F(x_0, y_0) = 0, F_y(x_0, y_0) \neq 0$ ，则方程 $F(x, y) = 0$ 在点 $(x_0, y_0)$ 的某一邻域内恒能唯一确定一个连续且具有连续导数的函数 $y = f(x)$ ，它满足条件 $y_0 = f(x_0)$ ，并有

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = - \frac {F _ {x}}{F _ {y}}. \tag {5-2}
$$

公式(5-2)就是隐函数的求导公式.

这个定理我们不证.现仅就公式(5-2)作如下推导：

将方程(5-1)所确定的函数 $y=f(x)$ 代入(5-1)，得恒等式

$$
F (x, f (x)) \equiv 0,
$$

其左端可以看做是 $x$ 的一个复合函数, 求这个函数的全导数, 由于恒等式两端求导后仍然恒等, 即得

$$
\frac {\partial F}{\partial x} + \frac {\partial F}{\partial y} \frac {\mathrm{d} y}{\mathrm{d} x} = 0,
$$

因为 $F_{y}$ 连续，且 $F_{y}(x_{0},y_{0})\neq 0$ ，所以存在 $(x_0,y_0)$ 的一个邻域，在这个邻域内 $F_{y}\neq 0$ ，于是得

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = - \frac {F _ {x}}{F _ {y}}.
$$

如果 $F(x, y)$ 的二阶偏导数也都连续, 我们可以把等式(5-2)的两端看做 $x$ 的复合函数而再一次求导, 即得

$$
\begin{array}{l} \frac {\mathrm{d} ^ {2} y}{\mathrm{d} x ^ {2}} = \frac {\partial}{\partial x} \left(- \frac {F _ {x}}{F _ {y}}\right) + \frac {\partial}{\partial y} \left(- \frac {F _ {x}}{F _ {y}}\right) \frac {\mathrm{d} y}{\mathrm{d} x} \\ = - \frac {F _ {x x} F _ {y} - F _ {y x} F _ {x}}{F _ {y} ^ {2}} - \frac {F _ {x y} F _ {y} - F _ {y y} F _ {x}}{F _ {y} ^ {2}} \left(- \frac {F _ {x}}{F _ {y}}\right) = - \frac {F _ {x x} F _ {y} ^ {2} - 2 F _ {x y} F _ {x} F _ {y} + F _ {y y} F _ {x} ^ {2}}{F _ {y} ^ {3}}. \\ \end{array}
$$

例 1 验证方程 $x^{2}+y^{2}-1=0$ 在点 $(0,1)$ 的某一邻域内能唯一确定一个有连续导数，当 x=0, y=1 时的隐函数 $y=f(x)$ ，并求这函数的一阶与二阶导数在 x=0 的值.

解 设 $F(x, y) = x^2 + y^2 - 1$ ，则 $F_x = 2x, F_y = 2y, F_x(0, 1) = 0, F_y(0, 1) = 2 \neq 0$ . 因此由定理1可知，方程 $x^2 + y^2 - 1 = 0$ 在点 $(0, 1)$ 的某邻域内能唯一确定一个有连续导数，当 $x = 0, y = 1$ 时的函数 $y = f(x)$ .

下面求这函数的一阶及二阶导数.

$$
\begin{array}{l} \frac {\mathrm{d} y}{\mathrm{d} x} = - \frac {F _ {x}}{F _ {y}} = - \frac {x}{y}, \quad \left. \frac {\mathrm{d} y}{\mathrm{d} x} \right| _ {\substack {x = 0 \\ y = 1}} = 0; \\ \frac {\mathrm{d} ^ {2} y}{\mathrm{d} x ^ {2}} = - \frac {y - x y ^ {\prime}}{y ^ {2}} = - \frac {y - x \left(- \frac {x}{y}\right)}{y ^ {2}} = - \frac {y ^ {2} + x ^ {2}}{y ^ {3}} = - \frac {1}{y ^ {3}}, \quad \left. \frac {\mathrm{d} ^ {2} y}{\mathrm{d} x ^ {2}} \right| _ {\substack {x = 0 \\ y = 1}} = - 1. \\ \end{array}
$$

隐函数存在定理还可以推广到多元函数.既然一个二元方程(5-1)可以确定一个一元隐函数,那么一个三元方程

$$
F (x, y, z) = 0 \tag {5-3}
$$

就有可能确定一个二元隐函数.

与定理1一样, 我们同样可以由三元函数 $F(x, y, z)$ 的性质来断定由方程 $F(x, y, z) = 0$ 所确定的二元函数 $z = f(x, y)$ 的存在以及这个函数的性质. 这就是下面的定理.

隐函数存在定理2 设函数 $F(x, y, z)$ 在点 $P(x_0, y_0, z_0)$ 的某一邻域内具有连续偏导数，且 $F(x_0, y_0, z_0) = 0, F_z(x_0, y_0, z_0) \neq 0$ ，则方程 $F(x, y, z) = 0$ 在点 $(x_0, y_0, z_0)$ 的某一邻域内恒能唯一确定一个连续且具有连续偏导数的函数 $z = f(x, y)$ ，它满足条件 $z_0 = f(x_0, y_0)$ ，并有

$$
\frac {\partial z}{\partial x} = - \frac {F _ {x}}{F _ {z}}, \quad \frac {\partial z}{\partial y} = - \frac {F _ {y}}{F _ {z}}. \tag {5-4}
$$

这个定理我们不证.与定理1类似,仅就公式(5-4)作如下推导:

由于 $F[x,y,f(x,y)]\equiv0$ , 将上式两端分别对 x 和 y 求导, 应用复合函数求导法则得

$$
F _ {x} + F _ {z} \frac {\partial z}{\partial x} = 0, \quad F _ {y} + F _ {z} \frac {\partial z}{\partial y} = 0.
$$

因为 $F_{z}$ 连续，且 $F_{z}(x_{0},y_{0},z_{0})\neq 0$ ，所以存在点 $(x_0,y_0,z_0)$ 的一个邻域，在这个邻域内 $F_{z}\neq 0$ ，于是得

$$
\frac {\partial z}{\partial x} = - \frac {F _ {x}}{F _ {z}}, \quad \frac {\partial z}{\partial y} = - \frac {F _ {y}}{F _ {z}}.
$$

例2 设 $x^{2} + y^{2} + z^{2} - 4z = 0$ ，求 $\frac{\partial^2z}{\partial x^2}$ .

解 设 $F(x, y, z) = x^2 + y^2 + z^2 - 4z$ ，则 $F_x = 2x, F_z = 2z - 4$ . 当 $z \neq 2$ 时，应用公式 (5-4)，得

$$
\frac {\partial z}{\partial x} = \frac {x}{2 - z}.
$$

再一次对 x 求偏导数, 得

$$
\frac {\partial^ {2} z}{\partial x ^ {2}} = \frac {(2 - z) + x \frac {\partial z}{\partial x}}{(2 - z) ^ {2}} = \frac {(2 - z) + x \cdot \frac {x}{2 - z}}{(2 - z) ^ {2}} = \frac {(2 - z) ^ {2} + x ^ {2}}{(2 - z) ^ {3}}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a3bdb87734cb00b1ffe4d75f6c431712716020f23bf6ca4857a012ac08502ac9.jpg)


# 二、方程组的情形

下面我们将隐函数存在定理作另一方面的推广.我们不仅增加方程中变量的个数,而且增加方程的个数.例如,考虑方程组

$$
\left\{ \begin{array}{l} F (x, y, u, v) = 0, \\ G (x, y, u, v) = 0. \end{array} \right. \tag {5-5}
$$

这时,在四个变量中,一般只能有两个变量独立变化,因此方程组(5-5)就有可能确定两个二元函数.在这种情况下,我们可以由函数F,G的性质来断定由方程组(5-5)所确定的两个二元函数的存在以及它们的性质.我们有下面的定理.

隐函数存在定理3 设 $F(x, y, u, v), G(x, y, u, v)$ 在点 $P(x_0, y_0, u_0, v_0)$ 的某一邻域内具有对各个变量的连续偏导数，又 $F(x_0, y_0, u_0, v_0) = 0, G(x_0, y_0, u_0, v_0) = 0$ ，且偏导数所组成的函数行列式（或称雅可比（Jacobi）式）

$$
J = \frac {\partial (F , G)}{\partial (u , v)} = \left| \begin{array}{l l} \frac {\partial F}{\partial u} & \frac {\partial F}{\partial v} \\ \frac {\partial G}{\partial u} & \frac {\partial G}{\partial v} \end{array} \right|
$$

在点 $P(x_0, y_0, u_0, v_0)$ 不等于零，则方程组 $F(x, y, u, v) = 0, G(x, y, u, v) = 0$ 在点 $(x_0, y_0, u_0, v_0)$ 的某一邻域内恒能唯一确定一组连续且具有连续偏导数的函数 $u = u(x, y), v = v(x, y)$ ，它们满足条件 $u_0 = u(x_0, y_0), v_0 = v(x_0, y_0)$ ，并有

$$
\frac {\partial u}{\partial x} = - \frac {1}{J} \frac {\partial (F , G)}{\partial (x , v)} = - \frac {\left| \begin{array}{l l} F _ {x} & F _ {v} \\ G _ {x} & G _ {v} \end{array} \right|}{\left| \begin{array}{l l} F _ {u} & F _ {v} \\ G _ {u} & G _ {v} \end{array} \right|},
$$

$$
\begin{array}{l} \frac {\partial v}{\partial x} = - \frac {1}{J} \frac {\partial (F , G)}{\partial (u , x)} = - \frac {\left| \begin{array}{l l} F _ {u} & F _ {x} \\ G _ {u} & G _ {x} \end{array} \right|}{\left| \begin{array}{l l} F _ {u} & F _ {v} \\ G _ {u} & G _ {v} \end{array} \right|}, \tag {5-6} \\ \frac {\partial u}{\partial y} = - \frac {1}{J} \frac {\partial (F , G)}{\partial (y , v)} = - \frac {\left| \begin{array}{l l} F _ {y} & F _ {v} \\ G _ {y} & G _ {v} \end{array} \right|}{\left| \begin{array}{l l} F _ {u} & F _ {v} \\ G _ {u} & G _ {v} \end{array} \right|}, \\ \frac {\partial v}{\partial y} = - \frac {1}{J} \frac {\partial (F , G)}{\partial (u , y)} = - \frac {\left| \begin{array}{l l} F _ {u} & F _ {y} \\ G _ {u} & G _ {y} \end{array} \right|}{\left| \begin{array}{l l} F _ {u} & F _ {v} \\ G _ {u} & G _ {v} \end{array} \right|}. \\ \end{array}
$$

这个定理我们不证.与前两个定理类似,下面仅就公式(5-6)作如下推导:

由于

$$
F [ x, y, u (x, y), v (x, y) ] \equiv 0, \quad G [ x, y, u (x, y), v (x, y) ] \equiv 0,
$$

将恒等式两端分别对 x 求导,应用复合函数求导法则得

$$
\left\{ \begin{array}{l} F _ {x} + F _ {u} \frac {\partial u}{\partial x} + F _ {v} \frac {\partial v}{\partial x} = 0, \\ G _ {x} + G _ {u} \frac {\partial u}{\partial x} + G _ {v} \frac {\partial v}{\partial x} = 0. \end{array} \right.
$$

这是关于 $\frac{\partial u}{\partial x}$ 和 $\frac{\partial v}{\partial x}$ 的线性方程组，由假设可知在点 $P(x_0, y_0, u_0, v_0)$ 的一个邻域内，系数行列式

$$
J = \left| \begin{array}{c c} F _ {u} & F _ {v} \\ G _ {u} & G _ {v} \end{array} \right| \neq 0,
$$

从而可解出 $\frac{\partial u}{\partial x}, \frac{\partial v}{\partial x}$ , 得

$$
\frac {\partial u}{\partial x} = - \frac {1}{J} \frac {\partial (F , G)}{\partial (x , v)}, \quad \frac {\partial v}{\partial x} = - \frac {1}{J} \frac {\partial (F , G)}{\partial (u , x)}.
$$

同理,可得

$$
\frac {\partial u}{\partial y} = - \frac {1}{J} \frac {\partial (F , G)}{\partial (y , v)}, \quad \frac {\partial v}{\partial y} = - \frac {1}{J} \frac {\partial (F , G)}{\partial (u , y)}.
$$

例3 设 $xu - yv = 0, yu + xv = 1$ ，求 $\frac{\partial u}{\partial x}, \frac{\partial u}{\partial y}, \frac{\partial v}{\partial x}$ 和 $\frac{\partial v}{\partial y}$ .

解 此题可直接利用公式(5-6)，但也可依照推导公式(5-6)的方法来求解.下面我们用后一种方法来做.

将所给方程的两端对 x 求导并移项, 得

$$
\left\{ \begin{array}{l} x \frac {\partial u}{\partial x} - y \frac {\partial v}{\partial x} = - u, \\ y \frac {\partial u}{\partial x} + x \frac {\partial v}{\partial x} = - v. \end{array} \right.
$$

在 $J = \left| \begin{array}{cc}x & -y\\ y & x \end{array} \right| = x^2 +y^2\neq 0$ 的条件下，

$$
\frac {\partial u}{\partial x} = \frac {\left| \begin{array}{c c} - u & - y \\ - v & x \end{array} \right|}{\left| \begin{array}{c c} x & - y \\ y & x \end{array} \right|} = - \frac {x u + y v}{x ^ {2} + y ^ {2}}, \quad \frac {\partial v}{\partial x} = \frac {\left| \begin{array}{c c} x & - u \\ y & - v \end{array} \right|}{\left| \begin{array}{c c} x & - y \\ y & x \end{array} \right|} = \frac {y u - x v}{x ^ {2} + y ^ {2}}.
$$

将所给方程的两端对 $y$ 求导. 用同样方法在 $J = x^{2} + y^{2} \neq 0$ 的条件下可得

$$
\frac {\partial u}{\partial y} = \frac {x v - y u}{x ^ {2} + y ^ {2}}, \quad \frac {\partial v}{\partial y} = - \frac {x u + y v}{x ^ {2} + y ^ {2}}.
$$

例4 设函数 $x = x(u, v), y = y(u, v)$ 在点 $(u, v)$ 的某一邻域内连续且有连续偏导数，又

$$
\frac {\partial (x , y)}{\partial (u , v)} \neq 0.
$$

(1) 证明方程组

$$
\left\{ \begin{array}{l} x = x (u, v), \\ y = y (u, v) \end{array} \right. \tag {5-7}
$$

在点 $(x, y, u, v)$ 的某一邻域内唯一确定一组连续且具有连续偏导数的反函数 $u = u(x, y)$ , $v = v(x, y)$ .

(2) 求反函数 $u = u(x, y)$ , $v = v(x, y)$ 对 x, y 的偏导数.

解（1）将方程组(5-7)改写成

$$
\left\{ \begin{array}{l} F (x, y, u, v) \equiv x - x (u, v) = 0, \\ G (x, y, u, v) \equiv y - y (u, v) = 0. \end{array} \right.
$$

则按假设

$$
J = \frac {\partial (F , G)}{\partial (u , v)} = \frac {\partial (x , y)}{\partial (u , v)} \neq 0.
$$

由隐函数存在定理 3, 即得所要证的结论.

(2) 将方程组(5-7)所确定的反函数 $u = u(x, y)$ , $v = v(x, y)$ 代入(5-7)，即得

$$
\left\{ \begin{array}{l} x \equiv x [ u (x, y), v (x, y) ], \\ y \equiv y [ u (x, y), v (x, y) ]. \end{array} \right.
$$

将上述恒等式两端分别对 x 求偏导数, 得

$$
\left\{ \begin{array}{l} 1 = \frac {\partial x}{\partial u} \frac {\partial u}{\partial x} + \frac {\partial x}{\partial v} \frac {\partial v}{\partial x}, \\ 0 = \frac {\partial y}{\partial u} \frac {\partial u}{\partial x} + \frac {\partial y}{\partial v} \frac {\partial v}{\partial x}. \end{array} \right.
$$

由于 $J \neq 0$ ，故可解得

$$
\frac {\partial u}{\partial x} = \frac {1}{J} \frac {\partial y}{\partial v}, \quad \frac {\partial v}{\partial x} = - \frac {1}{J} \frac {\partial y}{\partial u}.
$$

[NO TEXT] 

释疑解难

9-4 

同理,可得

$$
\frac {\partial u}{\partial y} = - \frac {1}{J} \frac {\partial x}{\partial v}, \quad \frac {\partial v}{\partial y} = \frac {1}{J} \frac {\partial x}{\partial u}.
$$

# 习题9-5

1. 设 $\sin y + e^x - xy^2 = 0$ ，求 $\frac{dy}{dx}$ .

2. 设 $\ln\sqrt{x^{2}+y^{2}}=\arctan\frac{y}{x}$ ，求 $\frac{dy}{dx}$ .

3. 设 $x+2y+z-2\sqrt{xyz}=0$ , 求 $\frac{\partial z}{\partial x}$ 及 $\frac{\partial z}{\partial y}$ .

4. 设 $\frac{x}{z}=\ln\frac{z}{y}$ ，求 $\frac{\partial z}{\partial x}$ 及 $\frac{\partial z}{\partial y}$ .

5. 设 $2\sin(x+2y-3z)=x+2y-3z$ ，证明 $\frac{\partial z}{\partial x}+\frac{\partial z}{\partial y}=1$ .

6. 设 $x=x(y,z)$ , $y=y(x,z)$ , $z=z(x,y)$ 都是由方程 $F(x,y,z)=0$ 所确定的具有连续偏导数的函数, 证明 $\frac{\partial x}{\partial y} \cdot \frac{\partial y}{\partial z} \cdot \frac{\partial z}{\partial x} = -1$ .

7. 设 $\Phi(u,v)$ 具有连续偏导数, 证明由方程 $\Phi(cx-az,cy-bz)=0$ 所确定的函数 $z=f(x,y)$ 满足 $a\frac{\partial z}{\partial x}+b\frac{\partial z}{\partial y}=c.$ 

8. 设 $z = z(x, y)$ 是由方程 $2xz - 2xyz + \ln (xyz) = 0$ 所确定的隐函数，求 $\mathrm{dz}$ .

* 9. 设 $e^z - xyz = 0$ , 求 $\frac{\partial^2 z}{\partial x^2}$ .

* 10. 设 $z^3 - 3xyz = a^3$ ，求 $\frac{\partial^2 z}{\partial x \partial y}$ .

11. 求由下列方程组所确定的函数的导数或偏导数：

(1) 设 $\left\{\begin{aligned} z &= x^{2} + y^{2}, \\ x^{2} &= 2y^{2} + 3z^{2} = 20, \end{aligned}\right.$ 求 $\frac{dy}{dx}, \frac{dz}{dx};$ 

(2) 设 $\left\{\begin{aligned} x+y+z=0, \\ x^{2}+y^{2}+z^{2}=1, \end{aligned}\right.$ 求 $\frac{dx}{dz}, \frac{dy}{dz};$ 

(3) 设 $\left\{\begin{aligned} u &= f(ux, v+y), \\ v &= g(u-x, v^{2}y), \end{aligned}\right.$ 其中 f, g 具有一阶连续偏导数，求 $\frac{\partial u}{\partial x}, \frac{\partial v}{\partial x};$ 

(4) 设 $\left\{\begin{aligned} x &= e^{u} + u \sin v, \\ y &= e^{u} - u \cos v, \end{aligned}\right.$ 求 $\frac{\partial u}{\partial x}, \frac{\partial u}{\partial y}, \frac{\partial v}{\partial x}, \frac{\partial v}{\partial y}.$ 

12. 设 $y = f(x, t)$ ，而 $t = t(x, y)$ 是由方程 $F(x, y, t) = 0$ 所确定的函数，其中 $f, F$ 都具有一阶连续偏导数。试证明

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \frac {\frac {\partial f}{\partial x} \frac {\partial F}{\partial t} - \frac {\partial f}{\partial t} \frac {\partial F}{\partial x}}{\frac {\partial f}{\partial t} \frac {\partial F}{\partial y} + \frac {\partial F}{\partial t}}.
$$

# 第六节 多元函数微分学的几何应用

本节先介绍一元向量值函数及其导数,再讨论多元函数微分学的几何应用.

# 一、一元向量值函数及其导数

由空间解析几何知道,空间曲线 $\Gamma$ 的参数方程为

$$
\left\{ \begin{array}{l l} x = \varphi (t), \\ y = \psi (t), & t \in [ \alpha , \beta ]. \\ z = \omega (t), \end{array} \right. \tag {6-1}
$$

方程(6-1)也可以写成向量形式.若记

$$
\boldsymbol {r} = x \boldsymbol {i} + y \boldsymbol {j} + z \boldsymbol {k}, \quad \boldsymbol {f} (t) = \varphi (t) \boldsymbol {i} + \psi (t) \boldsymbol {j} + \omega (t) \boldsymbol {k},
$$

则方程(6-1)就成为向量方程

$$
\boldsymbol {r} = \boldsymbol {f} (t), \quad t \in [ \alpha , \beta ]. \tag {6-2}
$$

方程(6-2)确定了一个映射 $f:[\alpha,\beta]\rightarrow\mathbb{R}^{3}$ .由于这个映射将每一个 $t\in[\alpha,\beta]$ 映成一个向量 $f(t)\in\mathbb{R}^{3}$ ，故称这映射为一元向量值函数.一般地，有如下定义.

定义1 设数集 $D \subset \mathbb{R}$ , 则称映射 $f: D \to \mathbb{R}^n$ 为一元向量值函数, 通常记为

$$
r = f (t), \quad t \in D,
$$

其中数集 D 称为函数的定义域, t 称为自变量, r 称为因变量.

一元向量值函数是普通一元函数的推广.现在,自变量 t 依然取实数值,但因变量

r 不取实数值,而取值为 n 维向量.

在本教材中, 只讨论一元向量值函数, 并对因变量的取值以 $n = 3$ 的情形作为代表, 即 $\pmb{r}$ 的取值为 3 维向量. 为简单起见, 以下将一元向量值函数简称为向量值函数, 并把普通的实值函数称为数量函数.

在 $\mathbf{R}^3$ 中, 若向量值函数 $f(t)$ , $t \in D$ 的三个分量函数依次为 $f_1(t)$ , $f_2(t)$ , $f_3(t)$ , $t \in D$ , 则向量值函数 $f(t)$ 可表示为

$$
\boldsymbol {f} (t) = f _ {1} (t) \boldsymbol {i} + f _ {2} (t) \boldsymbol {j} + f _ {3} (t) \boldsymbol {k}, \quad t \in D \tag {6-3}
$$

或

$$
\boldsymbol {f} (t) = \left(f _ {1} (t), f _ {2} (t), f _ {3} (t)\right), \quad t \in D. \tag {$6-3^{\prime$}}
$$

设(变)向量 r 的起点取在坐标系的原点 O 处, 终点在 M 处, 即 $r = \overrightarrow{OM}$ (图 9-6). 当 t 改变时, r 跟着改变, 从而终点 M 也随之改变. 终点 M 的轨迹(记作曲线 $\Gamma$ ) 称为向量值函数 $r = f(t)$ ( $t \in D$ ) 的终端曲线, 曲线 $\Gamma$ 也称为向量值函数 $r = f(t)$ ( $t \in D$ ) 的图形.

由于向量值函数 $r = f(t) (t \in D)$ 与空间曲线 $\Gamma$ 是一一对应的，因此

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/9d3ca3cafc7902a14371bc7d1f341e3db1e89347f39ced901fa49f2ff5f843fc.jpg)



图9-6


$$
\boldsymbol {r} = \boldsymbol {f} (t) = \left(f _ {1} (t), f _ {2} (t), f _ {3} (t)\right), \quad t \in D \tag {6-4}
$$

称为曲线 $\Gamma$ 的向量方程.

根据 $R^{3}$ 中的向量的线性运算及向量的模的概念, 可以类似于定义数量函数的极限、连续、导数等概念的形式来定义向量值函数的相应概念, 现简述如下:

定义2 设向量值函数 $f(t)$ 在点 $t_0$ 的某一去心邻域内有定义, 如果存在一个常向量 $r_0$ , 对于任意给定的正数 $\varepsilon$ , 总存在正数 $\delta$ , 使得当 $t$ 满足 $0 < |t - t_0| < \delta$ 时, 对应的函数值 $f(t)$ 都满足不等式

$$
\left| f (t) - r _ {0} \right| <   \varepsilon ,
$$

那么常向量 $r_{0}$ 就叫做向量值函数 $f(t)$ 当 $t\to t_0$ 时的极限,记作

$$
\lim _ {t \to t _ {0}} f (t) = r _ {0} \quad {\text {或}} \quad f (t) \longrightarrow r _ {0},   t \longrightarrow t _ {0}.
$$

容易证明:向量值函数 $f(t)$ 当 $t\to t_{0}$ 时的极限存在的充分必要条件是: $f(t)$ 的三个分量函数 $f_{1}(t)$ , $f_{2}(t)$ , $f_{3}(t)$ 当 $t\to t_{0}$ 时的极限都存在;在函数 $f(t)$ 当 $t\to t_{0}$ 时的极限存在时,其极限

$$
\lim _ {t \to t _ {0}} f (t) = \left(\lim _ {t \to t _ {0}} f _ {1} (t), \lim _ {t \to t _ {0}} f _ {2} (t), \lim _ {t \to t _ {0}} f _ {3} (t)\right). \tag {6-5}
$$

设向量值函数 $f(t)$ 在点 $t_{0}$ 的某一邻域内有定义,若

$$
\lim _ {t \rightarrow t _ {0}} f (t) = f (t _ {0}),
$$

则称向量值函数 $f(t)$ 在 $t_{0}$ 连续.

向量值函数 $f(t)$ 在 $t_{0}$ 连续的充分必要条件是: $f(t)$ 的三个分量函数 $f_{1}(t), f_{2}(t), f_{3}(t)$ 都在 $t_{0}$ 连续.

设向量值函数 $f(t), t \in D$ . 若 $D_{1} \subset D, f(t)$ 在 $D_{1}$ 中的每一点处都连续，则称 $f(t)$ 在 $D_{1}$ 上连续，并称 $f(t)$ 是 $D_{1}$ 上的连续函数.

下面给出向量值函数的导数(或导向量)的定义.

定义 3 设向量值函数 $r=f(t)$ 在点 $t_{0}$ 的某一邻域内有定义, 如果

$$
\lim _ {\Delta t \rightarrow 0} \frac {\Delta r}{\Delta t} = \lim _ {\Delta t \rightarrow 0} \frac {f (t _ {0} + \Delta t) - f (t _ {0})}{\Delta t}
$$

存在,那么就称这个极限向量为向量值函数 $r=f(t)$ 在 $t_{0}$ 处的导数或导向量,记作 $f'(t_{0})$ 或 $\frac{\mathrm{d}r}{\mathrm{d}t}\bigg|_{t=t_{0}}$ .

设向量值函数 $r = f(t), t \in D$ . 若 $D_{1} \subset D, f(t)$ 在 $D_{1}$ 中的每一点 $t$ 处都存在导向量 $f'(t)$ 或 $\frac{\mathrm{d}r}{\mathrm{d}t}$ , 则称 $f(t)$ 在 $D_{1}$ 上可导.

向量值函数 $f(t)$ 在 $t_{0}$ 可导（即存在导数）的充分必要条件是： $f(t)$ 的三个分量函数 $f_{1}(t), f_{2}(t), f_{3}(t)$ 都在 $t_{0}$ 可导；当 $f(t)$ 在 $t_{0}$ 可导时，其导数

$$
\boldsymbol {f} ^ {\prime} (t _ {0}) = f _ {1} ^ {\prime} (t _ {0}) \boldsymbol {i} + f _ {2} ^ {\prime} (t _ {0}) \boldsymbol {j} + f _ {3} ^ {\prime} (t _ {0}) \boldsymbol {k}. \tag {6-6}
$$

向量值函数的导数运算法则与数量函数的导数运算法则的形式相同,现列出如下:

设 $u(t)$ , $v(t)$ 是可导的向量值函数, C 是常向量, c 是任一常数, $\varphi(t)$ 是可导的数量函数, 则

(1) $\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{C} = 0;$ 

(2) $\frac{\mathrm{d}}{\mathrm{d}t}\left[c\pmb {u}(t)\right] = c\pmb{u}'(t);$ 

(3) $\frac{\mathrm{d}}{\mathrm{d}t}\left[\boldsymbol{u}(t)\pm \boldsymbol{v}(t)\right] = \boldsymbol{u}'(t)\pm \boldsymbol{v}'(t);$ 

(4) $\frac{\mathrm{d}}{\mathrm{d}t}\left[\varphi(t)\boldsymbol{u}(t)\right]=\varphi'(t)\boldsymbol{u}(t)+\varphi(t)\boldsymbol{u}'(t);$ 

(5) $\frac{\mathrm{d}}{\mathrm{d}t}\left[\boldsymbol{u}(t)\cdot \boldsymbol{v}(t)\right] = \boldsymbol{u}'(t)\cdot \boldsymbol{v}(t) + \boldsymbol{u}(t)\cdot \boldsymbol{v}'(t);$ 

(6) $\frac{\mathrm{d}}{\mathrm{d}t} [u(t)\times v(t)] = u'(t)\times v(t) + u(t)\times v'(t);$ 

(7) $\frac{\mathrm{d}}{\mathrm{d}t}\boldsymbol {u}[\varphi (t)] = \varphi '(t)\boldsymbol {u}'[\varphi (t)].$ 

仿照对数量函数的导数运算法则的证明方法,或对向量函数的分量运用对应的数量函数的导数运算法则,可以证明以上法则,读者可作为练习自行证明.

下面,讨论向量值函数 $r=f(t)$ 的导向量的几何意义.

设空间曲线 $\Gamma$ 是向量值函数 $r=f(t), t \in D$ 的终端曲线，向量 $\overrightarrow{OM}=f(t_{0}), \overrightarrow{ON}=f(t_{0}+\Delta t)$ ，如图 9-7 所示。又设导向量 $f'(t_{0})$ 不是零向量。

当 $\Delta t > 0$ 时，向量 $\Delta r = f(t_{0} + \Delta t) - f(t_{0})$ 的方向与 t 增大时点 M 移动的走向（以下简称 t 的增长方向）一致；当

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/2a05b89ffa04e07b57d1916e6bddaf02b18271c25a3a8cb9e7381d997cb9ebb4.jpg)



图9-7


$\Delta t < 0$ 时，向量 $\Delta r = f(t_0 + \Delta t) - f(t_0)$ 的方向与 $t$ 的增长方向相反.但不论 $\Delta t > 0$ 或 $\Delta t < 0$ 向量 $\frac{\Delta r}{\Delta t} = \frac{1}{\Delta t}\Delta r$ 的方向总与 $t$ 的增长方向一致.于是，导向量 $f^{\prime}(t_0) = \lim_{\Delta t\to 0}\frac{\Delta r}{\Delta t}$ 是向量值函数 $r = f(t)$ 的终端曲线 $\Gamma$ 在点 $M$ 处的一个切向量，其方向与 $t$ 的增长方向一致.

设向量值函数 $r=f(t)$ 是沿空间光滑曲线运动的质点 M 的位置向量，则向量值函数 $r=f(t)$ 的导向量有以下的物理意义：

$v(t)=\frac{dr}{dt}$ 是质点M的速度向量,其方向与曲线相切;

$a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=\frac{\mathrm{d}^{2}r}{\mathrm{d}t^{2}}$ 是质点 M 的加速度向量.

例1 设 $f(t) = (\cos t)i + (\sin t)j + tk$ ，求 $\lim_{t \to \frac{\pi}{4}} f(t)$ .

解 $\lim_{t\to \frac{\pi}{4}}f(t) = \left(\lim_{t\to \frac{\pi}{4}}\cos t\right)i + \left(\lim_{t\to \frac{\pi}{4}}\sin t\right)j + \left(\lim_{t\to \frac{\pi}{4}}t\right)k = \frac{\sqrt{2}}{2} i + \frac{\sqrt{2}}{2} j + \frac{\pi}{4} k.$ 

例2 设空间曲线 $\Gamma$ 的向量方程为

$$
\boldsymbol {r} = \boldsymbol {f} (t) = \left(t ^ {2} + 1, 4 t - 3, 2 t ^ {2} - 6 t\right), \quad t \in \mathbf {R},
$$

求曲线 $\Gamma$ 在与 t=2 相应的点处的单位切向量.

解 $f'(t)=(2t,4,4t-6)$ ， $t\in R$ 

$$
f ^ {\prime} (2) = (4, 4, 2), \quad | f ^ {\prime} (2) | = \sqrt {4 ^ {2} + 4 ^ {2} + 2 ^ {2}} = 6.
$$

由导向量的几何意义知, 曲线 $\Gamma$ 在与 t=2 相应的点处的一个单位切向量是 $\left(\frac{2}{3},\frac{2}{3},\frac{1}{3}\right)$ , 其方向与 t 的增长方向一致; 另一个单位切向量是 $\left(-\frac{2}{3},-\frac{2}{3},-\frac{1}{3}\right)$ , 其方向与 t 的增长方向相反.

例3 一个人在悬挂式滑翔机上由于快速上升气流而沿位置向量为 $r = f(t) = (3\cos t)i + (3\sin t)j + t^2 k$ 的路径螺旋式向上.求

(1) 滑翔机在任意时刻 t 的速度向量和加速度向量;

(2) 滑翔机在任意时刻 $t$ 的速率;

(3) 滑翔机的加速度与速度正交的时刻.

解 (1) $r = f(t) = (3\cos t)i + (3\sin t)j + t^2 k,$ 

$$
\boldsymbol {v} = \frac {\mathrm{d} \boldsymbol {r}}{\mathrm{d} t} = (- 3 \sin t) \boldsymbol {i} + (3 \cos t) \boldsymbol {j} + 2 t \boldsymbol {k},
$$

$$
\boldsymbol {a} = \frac {\mathrm{d} ^ {2} \boldsymbol {r}}{\mathrm{d} t ^ {2}} = (- 3 \cos t) \boldsymbol {i} - (3 \sin t) \boldsymbol {j} + 2 \boldsymbol {k}.
$$

(2) 速率是速度v的大小, 即

$$
| \boldsymbol {v} | = \sqrt {(- 3 \sin t) ^ {2} + (3 \cos t) ^ {2} + (2 t) ^ {2}} = \sqrt {9 + 4 t ^ {2}}.
$$

这一结果表明:滑翔机沿其路径升高时,运动得越来越快.

（3）由 $v \cdot a = 9\sin t \cos t - 9\sin t \cos t + 4t = 0$ ，得 t = 0。这表明：加速度与速度正交的唯一时刻是在 t = 0。

# 二、空间曲线的切线与法平面

设空间曲线 $\Gamma$ 的参数方程为

$$
\left\{ \begin{array}{l l} x = \varphi (t), \\ y = \psi (t), & t \in [ \alpha , \beta ]. \\ z = \omega (t), \end{array} \right. \tag {6-7}
$$

这里假定(6-7)式的三个函数都在 $[\alpha,\beta]$ 上可导,且三个导数不同时为零.

现在要求曲线 $\Gamma$ 在其上一点 $M(x_{0}, y_{0}, z_{0})$ 处的切线及法平面方程.

设与点 M 对应的参数为 $t_{0}$ ，记 $f(t)=(\varphi(t),\psi(t),\omega(t))$ ， $t\in[\alpha,\beta]$ 。由向量值函数的导向量的几何意义知，向量 $T=f'(t_{0})=(\varphi'(t_{0}),\psi'(t_{0}),\omega'(t_{0}))$ 就是曲线 $\Gamma$ 在点 M 处的一个切向量，从而曲线 $\Gamma$ 在点 M 处的切线方程为

$$
\frac {x - x _ {0}}{\varphi^ {\prime} (t _ {0})} = \frac {y - y _ {0}}{\psi^ {\prime} (t _ {0})} = \frac {z - z _ {0}}{\omega^ {\prime} (t _ {0})}. \tag {6-8}
$$

通过点 M 且与切线垂直的平面称为曲线 $\Gamma$ 在点 M 处的法平面, 它是通过点 $M(x_{0}, y_{0}, z_{0})$ 且以 $T = f'(t_{0})$ 为法向量的平面, 因此法平面方程为

$$
\varphi^ {\prime} (t _ {0}) (x - x _ {0}) + \psi^ {\prime} (t _ {0}) (y - y _ {0}) + \omega^ {\prime} (t _ {0}) (z - z _ {0}) = 0. \tag {6-9}
$$

例 4 求曲线 $x=t, y=t^{2}, z=t^{3}$ 在点 $(1,1,1)$ 处的切线及法平面方程.

解 因为 $x_{t}^{\prime}=1, y_{t}^{\prime}=2t, z_{t}^{\prime}=3t^{2}$ ，而点 $(1,1,1)$ 所对应的参数 $t_{0}=1$ ，所以

$$
T = (1, 2, 3).
$$

于是,切线方程为

$$
\frac {x - 1}{1} = \frac {y - 1}{2} = \frac {z - 1}{3},
$$

法平面方程为

$$
(x - 1) + 2 (y - 1) + 3 (z - 1) = 0,
$$

即

$$
x + 2 y + 3 z = 6.
$$

现在我们再来讨论空间曲线 $\Gamma$ 的方程以另外两种形式给出的情形.

如果空间曲线 $\Gamma$ 的方程以

$$
\left\{ \begin{array}{l} y = \varphi (x), \\ z = \psi (x) \end{array} \right.
$$

的形式给出,取 x 为参数,它就可以表示为参数方程的形式

$$
\left\{ \begin{array}{l} x = x, \\ y = \varphi (x), \\ z = \psi (x). \end{array} \right.
$$

若 $\varphi(x),\psi(x)$ 都在 $x = x_0$ 处可导，则根据上面的讨论可知， $T = (1,\varphi'(x_0),\psi'(x_0))$ ，因此曲线 $\Gamma$ 在点 $M(x_0,y_0,z_0)$ 处的切线方程为

$$
\frac {x - x _ {0}}{1} = \frac {y - y _ {0}}{\varphi^ {\prime} (x _ {0})} = \frac {z - z _ {0}}{\psi^ {\prime} (x _ {0})}, \tag {6-10}
$$

在点 $M(x_0, y_0, z_0)$ 处的法平面方程为

$$
(x - x _ {0}) + \varphi^ {\prime} (x _ {0}) (y - y _ {0}) + \psi^ {\prime} (x _ {0}) (z - z _ {0}) = 0. \tag {6-11}
$$

设空间曲线 $\Gamma$ 的方程以

$$
\left\{ \begin{array}{l} F (x, y, z) = 0, \\ G (x, y, z) = 0 \end{array} \right. \tag {6-12}
$$

的形式给出, $M(x_{0},y_{0},z_{0})$ 是曲线 $\Gamma$ 上的一个点.又设F,G有对各个变量的连续偏导数,且

$$
\left. \frac {\partial (F , G)}{\partial (y , z)} \right| _ {(x _ {0}, y _ {0}, z _ {0})} \neq 0.
$$

这时方程组(6-12)在点 $M(x_0, y_0, z_0)$ 的某一邻域内确定了一组函数 $y = \varphi(x)$ , $z = \psi(x)$ . 要求曲线 $\Gamma$ 在点 $M$ 处的切线方程和法平面方程, 只要求出 $\varphi'(x_0), \psi'(x_0)$ , 然后代入(6-10)、(6-11)两式就行了. 为此, 我们在恒等式

$$
F [ x, \varphi (x), \psi (x) ] \equiv 0, \quad G [ x, \varphi (x), \psi (x) ] \equiv 0
$$

两端分别对 x 求全导数, 得

$$
\left\{ \begin{array}{l} \frac {\partial F}{\partial x} + \frac {\partial F}{\partial y} \frac {\mathrm{d} y}{\mathrm{d} x} + \frac {\partial F}{\partial z} \frac {\mathrm{d} z}{\mathrm{d} x} = 0, \\ \frac {\partial G}{\partial x} + \frac {\partial G}{\partial y} \frac {\mathrm{d} y}{\mathrm{d} x} + \frac {\partial G}{\partial z} \frac {\mathrm{d} z}{\mathrm{d} x} = 0. \end{array} \right.
$$

由假设可知,在点 M 的某个邻域内

$$
J = \frac {\partial (F , G)}{\partial (y , z)} \neq 0,
$$

故可解得

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = \varphi^ {\prime} (x) = \frac {\left| \begin{array}{l l} F _ {z} & F _ {x} \\ G _ {z} & G _ {x} \end{array} \right|}{\left| \begin{array}{l l} F _ {y} & F _ {z} \\ G _ {y} & G _ {z} \end{array} \right|}, \quad \frac {\mathrm{d} z}{\mathrm{d} x} = \psi^ {\prime} (x) = \frac {\left| \begin{array}{l l} F _ {x} & F _ {y} \\ G _ {x} & G _ {y} \end{array} \right|}{\left| \begin{array}{l l} F _ {y} & F _ {z} \\ G _ {y} & G _ {z} \end{array} \right|}.
$$

于是 $T=(1,\varphi'(x_{0}),\psi'(x_{0}))$ 是曲线 $\Gamma$ 在点 M 处的一个切向量, 这里

$$
\varphi^ {\prime} (x _ {0}) = \frac {\left| \begin{array}{c c} F _ {z} & F _ {x} \\ G _ {z} & G _ {x} \end{array} \right| _ {M}}{\left| \begin{array}{c c} F _ {y} & F _ {z} \\ G _ {y} & G _ {z} \end{array} \right| _ {M}}, \quad \psi^ {\prime} (x _ {0}) = \frac {\left| \begin{array}{c c} F _ {x} & F _ {y} \\ G _ {x} & G _ {y} \end{array} \right| _ {M}}{\left| \begin{array}{c c} F _ {y} & F _ {z} \\ G _ {y} & G _ {z} \end{array} \right| _ {M}},
$$

分子、分母中带下标 M 的行列式表示行列式在点 $M(x_{0}, y_{0}, z_{0})$ 的值. 把上面的切向量 T 乘 $\left|\begin{matrix} F_{y} & F_{z} \\ G_{y} & G_{z} \end{matrix}\right|_{M}$ ，得

$$
\boldsymbol {T} _ {1} = \left(\left| \begin{array}{c c} F _ {y} & F _ {z} \\ G _ {y} & G _ {z} \end{array} \right| _ {M}, \left| \begin{array}{c c} F _ {z} & F _ {x} \\ G _ {z} & G _ {x} \end{array} \right| _ {M}, \left| \begin{array}{c c} F _ {x} & F _ {y} \\ G _ {x} & G _ {y} \end{array} \right| _ {M}\right),
$$

这也是曲线 $\Gamma$ 在点 $M$ 处的一个切向量. 由此可写出曲线 $\Gamma$ 在点 $M(x_0, y_0, z_0)$ 处的切线方程为

$$
\frac {x - x _ {0}}{\left| \begin{array}{l l} F _ {y} & F _ {z} \\ G _ {y} & G _ {z} \end{array} \right| _ {M}} = \frac {y - y _ {0}}{\left| \begin{array}{l l} F _ {z} & F _ {x} \\ G _ {z} & G _ {x} \end{array} \right| _ {M}} = \frac {z - z _ {0}}{\left| \begin{array}{l l} F _ {x} & F _ {y} \\ G _ {x} & G _ {y} \end{array} \right| _ {M}}, \tag {6-13}
$$

曲线 $\Gamma$ 在点 $M(x_0, y_0, z_0)$ 处的法平面方程为

$$
\left| \begin{array}{l l} F _ {y} & F _ {z} \\ G _ {y} & G _ {z} \end{array} \right| _ {M} (x - x _ {0}) + \left| \begin{array}{l l} F _ {z} & F _ {x} \\ G _ {z} & G _ {x} \end{array} \right| _ {M} (y - y _ {0}) + \left| \begin{array}{l l} F _ {x} & F _ {y} \\ G _ {x} & G _ {y} \end{array} \right| _ {M} (z - z _ {0}) = 0. \tag {6-14}
$$

如果 $\frac{\partial(F,G)}{\partial(y,z)}\Bigg|_M = 0$ 而 $\frac{\partial(F,G)}{\partial(z,x)}\Bigg|_M,\frac{\partial(F,G)}{\partial(x,y)}\Bigg|_M$ 中至少有一个不等于零，那么我们可得同样的结果.

例 5 求曲线 $x^{2}+y^{2}+z^{2}=6, x+y+z=0$ 在点 $(1,-2,1)$ 处的切线及法平面方程.

解 这里可直接利用公式(6-13)及(6-14)来解,但下面我们依照推导公式的方法来做.

将所给方程的两端对 x 求导并移项, 得

$$
\left\{ \begin{array}{l} y \frac {\mathrm{d} y}{\mathrm{d} x} + z \frac {\mathrm{d} z}{\mathrm{d} x} = - x, \\ \frac {\mathrm{d} y}{\mathrm{d} x} + \frac {\mathrm{d} z}{\mathrm{d} x} = - 1. \end{array} \right.
$$

由此得

$$
\begin{array}{l} \frac {\mathrm{d} y}{\mathrm{d} x} = \frac {\left| \begin{array}{c c} - x & z \\ - 1 & 1 \end{array} \right|}{\left| \begin{array}{c c} y & z \\ 1 & 1 \end{array} \right|} = \frac {z - x}{y - z}, \quad \frac {\mathrm{d} z}{\mathrm{d} x} = \frac {\left| \begin{array}{c c} y & - x \\ 1 & - 1 \end{array} \right|}{\left| \begin{array}{c c} y & z \\ 1 & 1 \end{array} \right|} = \frac {x - y}{y - z}. \\ \left. \frac {\mathrm{d} y}{\mathrm{d} x} \right| _ {(1, - 2, 1)} = 0, \quad \left. \frac {\mathrm{d} z}{\mathrm{d} x} \right| _ {(1, - 2, 1)} = - 1. \\ \end{array}
$$

从而

$$
\boldsymbol {T} = (1, 0, - 1).
$$

故所求切线方程为

$$
\frac {x - 1}{1} = \frac {y + 2}{0} = \frac {z - 1}{- 1},
$$

法平面方程为

$$
(x - 1) + 0 \cdot (y + 2) - (z - 1) = 0,
$$

即

$$
x - z = 0.
$$

# 三、曲面的切平面与法线

我们先讨论由隐式给出曲面方程

$$
F (x, y, z) = 0 \tag {6-15}
$$

的情形,然后把由显式给出的曲面方程 $z=f(x,y)$ 作为它的特殊情形.

设曲面 $\Sigma$ 由方程(6-15)给出， $M(x_0, y_0, z_0)$ 是曲面 $\Sigma$ 上的一点，并设函数 $F(x, y, z)$ 的偏导数在该点连续且不同时为零。在曲面 $\Sigma$ 上，通过点 $M$ 任意引一条曲线 $\Gamma$ （图9-8），假定曲线 $\Gamma$ 的参数方程为

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/74f02b5f65da9508fa2e7cd5f781cfb5a64eae3570901cba60b19cfda16c58b1.jpg)



图9-8


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/9fd65edb50ca3b9ae0d8c33ed9919bb46d46488caabd75db986f01368fcdd5b9.jpg)


释疑解难

9-5 

$$
x = \varphi (t), y = \psi (t), z = \omega (t) \quad (\alpha \leqslant t \leqslant \beta), \tag {6-16}
$$

$t=t_{0}$ 对应于点 $M(x_{0},y_{0},z_{0})$ 且 $\varphi'(t_{0}),\psi'(t_{0}),\omega'(t_{0})$ 不全为零，则由(6-8)式可得这曲线的切线方程为

$$
\frac {x - x _ {0}}{\varphi^ {\prime} (t _ {0})} = \frac {y - y _ {0}}{\psi^ {\prime} (t _ {0})} = \frac {z - z _ {0}}{\omega^ {\prime} (t _ {0})}.
$$

我们现在要证明,在曲面 $\Sigma$ 上通过点 M 且在点 M 处具有切线的任何曲线,它们在点 M 处的切线都在同一个平面上.事实上,因为曲线 $\Gamma$ 完全在曲面 $\Sigma$ 上,所以有恒等式

$$
F [ \varphi (t), \psi (t), \omega (t) ] \equiv 0,
$$

又因为 $F(x,y,z)$ 在点 $(x_{0},y_{0},z_{0})$ 处有连续偏导数，且 $\varphi'(t_{0}),\psi'(t_{0})$ 和 $\omega'(t_{0})$ 存在，所以这恒等式左端的复合函数在 $t=t_{0}$ 时有全导数，且这全导数等于零：

$$
\frac {\mathrm{d}}{\mathrm{d} t} F [ \varphi (t), \psi (t), \omega (t) ] \Big | _ {t = t _ {0}} = 0,
$$

即有

$$
F _ {x} \left(x _ {0}, y _ {0}, z _ {0}\right) \varphi^ {\prime} \left(t _ {0}\right) + F _ {y} \left(x _ {0}, y _ {0}, z _ {0}\right) \psi^ {\prime} \left(t _ {0}\right) + F _ {z} \left(x _ {0}, y _ {0}, z _ {0}\right) \omega^ {\prime} \left(t _ {0}\right) = 0. \tag {6-17}
$$

引入向量

$$
\boldsymbol {n} = \left(F _ {x} (x _ {0}, y _ {0}, z _ {0}), F _ {y} (x _ {0}, y _ {0}, z _ {0}), F _ {z} (x _ {0}, y _ {0}, z _ {0})\right),
$$

则(6-17)式表示曲线(6-16)在点 M 处的切向量

$$
\boldsymbol {T} = \left(\varphi^ {\prime} \left(t _ {0}\right), \psi^ {\prime} \left(t _ {0}\right), \omega^ {\prime} \left(t _ {0}\right)\right)
$$

与向量 n 垂直. 因为曲线(6-16)是曲面上通过点 M 的任意一条曲线, 它们在点 M 的切线都与同一个向量 n 垂直, 所以曲面上通过点 M 的一切曲线在点 M 的切线都在同一个平面上(图 9-8). 这个平面称为曲面 $\Sigma$ 在点 M 的切平面. 这切平面的方程是

$$
F _ {x} \left(x _ {0}, y _ {0}, z _ {0}\right) \left(x - x _ {0}\right) + F _ {y} \left(x _ {0}, y _ {0}, z _ {0}\right) \left(y - y _ {0}\right) + F _ {z} \left(x _ {0}, y _ {0}, z _ {0}\right) \left(z - z _ {0}\right) = 0. \tag {6-18}
$$

通过点 $M(x_{0},y_{0},z_{0})$ 且垂直于切平面(6-18)的直线称为曲面在该点的法线. 法线方程是

$$
\frac {x - x _ {0}}{F _ {x} \left(x _ {0} , y _ {0} , z _ {0}\right)} = \frac {y - y _ {0}}{F _ {y} \left(x _ {0} , y _ {0} , z _ {0}\right)} = \frac {z - z _ {0}}{F _ {z} \left(x _ {0} , y _ {0} , z _ {0}\right)}. \tag {6-19}
$$

垂直于曲面上切平面的向量称为曲面的法向量. 向量

$$
\boldsymbol {n} = \left(F _ {x} \left(x _ {0}, y _ {0}, z _ {0}\right), F _ {y} \left(x _ {0}, y _ {0}, z _ {0}\right), F _ {z} \left(x _ {0}, y _ {0}, z _ {0}\right)\right)
$$

就是曲面 $\Sigma$ 在点 M 处的一个法向量.

现在来考虑曲面方程

$$
z = f (x, y). \tag {6-20}
$$

令

$$
F (x, y, z) = f (x, y) - z,
$$

可见

$$
F _ {x} (x, y, z) = f _ {x} (x, y), \quad F _ {y} (x, y, z) = f _ {y} (x, y), \quad F _ {z} (x, y, z) = - 1.
$$

于是,当函数 $f(x,y)$ 的偏导数 $f_{x}(x,y)$ , $f_{y}(x,y)$ 在点 $(x_{0},y_{0})$ 连续时,曲面(6-20)在点 $M(x_{0},y_{0},z_{0})$ 处的法向量为

$$
\boldsymbol {n} = \left(f _ {x} \left(x _ {0}, y _ {0}\right), f _ {y} \left(x _ {0}, y _ {0}\right), - 1\right),
$$

切平面方程为

$$
f _ {x} \left(x _ {0}, y _ {0}\right) \left(x - x _ {0}\right) + f _ {y} \left(x _ {0}, y _ {0}\right) \left(y - y _ {0}\right) - \left(z - z _ {0}\right) = 0,
$$

或

$$
z - z _ {0} = f _ {x} \left(x _ {0}, y _ {0}\right) \left(x - x _ {0}\right) + f _ {y} \left(x _ {0}, y _ {0}\right) \left(y - y _ {0}\right), \tag {6-21}
$$

而法线方程为

$$
\frac {x - x _ {0}}{f _ {x} (x _ {0} , y _ {0})} = \frac {y - y _ {0}}{f _ {y} (x _ {0} , y _ {0})} = \frac {z - z _ {0}}{- 1}. \tag {6-22}
$$

这里顺便指出,方程(6-21)右端恰好是函数 $z=f(x,y)$ 在点 $(x_{0},y_{0})$ 的全微分,而左端是切平面上点的竖坐标的增量.因此,函数 $z=f(x,y)$ 在点 $(x_{0},y_{0})$ 的全微分,在几何上表示曲面 $z=f(x,y)$ 在点 $(x_{0},y_{0},z_{0})$ 处的切平面上点的竖坐标的增量.

如果用 $\alpha, \beta$ 和 $\gamma$ 表示曲面的法向量的方向角，并假定法向量的方向是向上的，即使得它与 z 轴的正向所夹的角 $\gamma$ 是一锐角，那么法向量的方向余弦为

$$
\cos \alpha = \frac {- f _ {x}}{\sqrt {1 + f _ {x} ^ {2} + f _ {y} ^ {2}}}, \quad \cos \beta = \frac {- f _ {y}}{\sqrt {1 + f _ {x} ^ {2} + f _ {y} ^ {2}}}, \quad \cos \gamma = \frac {1}{\sqrt {1 + f _ {x} ^ {2} + f _ {y} ^ {2}}}.
$$

这里，把 $f_{x}(x_{0},y_{0})$ 和 $f_{y}(x_{0},y_{0})$ 分别简记为 $f_{x}$ 和 $f_{y}$ 

例6 求球面 $x^{2} + y^{2} + z^{2} = 14$ 在点(1,2,3)处的切平面及法线方程.

解 $F(x,y,z)=x^{2}+y^{2}+z^{2}-14,$ 

$$
\boldsymbol {n} = \left(F _ {x}, F _ {y}, F _ {z}\right) = (2 x, 2 y, 2 z), \quad \boldsymbol {n} \mid_ {(1, 2, 3)} = (2, 4, 6).
$$

所以在点(1,2,3)处此球面的切平面方程为

$$
2 (x - 1) + 4 (y - 2) + 6 (z - 3) = 0,
$$

即

$$
x + 2 y + 3 z - 1 4 = 0.
$$

法线方程为

$$
\frac {x - 1}{1} = \frac {y - 2}{2} = \frac {z - 3}{3},
$$

即

$$
\frac {x}{1} = \frac {y}{2} = \frac {z}{3}.
$$

由此可见,法线经过原点(即球心).

例 7 求旋转抛物面 $z=x^{2}+y^{2}-1$ 在点 $(2,1,4)$ 处的切平面及法线方程.

解 $f(x,y) = x^{2} + y^{2} - 1,$ 

$$
\boldsymbol {n} = \left(f _ {x}, f _ {y}, - 1\right) = (2 x, 2 y, - 1), \quad \boldsymbol {n} \mid_ {(2, 1, 4)} = (4, 2, - 1).
$$

所以在点(2,1,4)处的切平面方程为

$$
4 (x - 2) + 2 (y - 1) - (z - 4) = 0,
$$

即

$$
4 x + 2 y - z - 6 = 0.
$$

法线方程为

$$
\frac {x - 2}{4} = \frac {y - 1}{2} = \frac {z - 4}{- 1}.
$$

# 习题9-6

1. 设 $f(t) = f_{1}(t)i + f_{2}(t)j + f_{3}(t)k$ , $g(t) = g_{1}(t)i + g_{2}(t)j + g_{3}(t)k$ , $\lim_{t \to t_{0}} f(t) = u$ , $\lim_{t \to t_{0}} g(t) = v$ , 证明

$$
\lim _ {t \rightarrow t _ {0}} [ f (t) \times g (t) ] = u \times v.
$$

2. 下列各题中, $r=f(t)$ 是空间中的质点M在时刻t的位置,求质点M在时刻 $t_{0}$ 的速度向量和加速度向量以及在任意时刻t的速率:

(1) $r = f(t) = (t + 1)i + (t^2 -1)j + 2tk,t_0 = 1;$ 

(2) $r = f(t) = (2\cos t)i + (3\sin t)j + 4tk, t_0 = \frac{\pi}{2};$ 

(3) $r = f(t) = (2\ln (t + 1))i + t^2 j + \frac{1}{2} t^2 k, t_0 = 1.$ 

3. 求曲线 $r = f(t) = (t - \sin t)i + (1 - \cos t)j + \left(4\sin \frac{t}{2}\right)k$ 在与 $t_0 = \frac{\pi}{2}$ 相应的点处的切线及法平面方程.

4. 求曲线 $x=\frac{t}{1+t}, y=\frac{1+t}{t}, z=t^{2}$ 在对应于 $t_{0}=1$ 的点处的切线及法平面方程.

5. 求曲线 $y^{2}=2mx, z^{2}=m-x$ 在点 $(x_{0}, y_{0}, z_{0})$ 处的切线及法平面方程.

6. 求曲线 $\left\{\begin{aligned}x^{2}+y^{2}+z^{2}-3x=0,\\ 2x-3y+5z-4=0\end{aligned}\right.$ 在点 $(1,1,1)$ 处的切线及法平面方程.

7. 求出曲线 $x = t, y = t^2, z = t^3$ 上的点，使在该点的切线平行于平面 $x + 2y + z = 4$ .

8. 求曲面 $e^{z}-z+xy=3$ 在点 $(2,1,0)$ 处的切平面及法线方程.

9. 求曲面 $ax^{2}+by^{2}+cz^{2}=1$ 在点 $(x_{0},y_{0},z_{0})$ 处的切平面及法线方程.

10. 求椭球面 $x^{2} + 2y^{2} + z^{2} = 1$ 上平行于平面 $x - y + 2z = 0$ 的切平面方程.

11. 设曲面 $3x^{2} + y^{2} - z^{2} = 27$ 的切平面通过直线 $L: \left\{ \begin{array}{l} 10x + 2y - 2z = 27, \\ x + y - z = 0. \end{array} \right.$ 求此切平面的方程.

12. 设 L 是曲面 $\Sigma: z = y^{2} + x^{3}y$ 上一条曲线的切线，切点为 $P(2,1,9)$ ，L 在 xOy 面上的投影平行于 x 轴，求切线 L 的参数方程.

13. 求旋转椭球面 $3x^{2} + y^{2} + z^{2} = 16$ 上点 $(-1, -2, 3)$ 处的切平面与 $xOy$ 面的夹角的余弦.

14. 试证曲面 $\sqrt{x} + \sqrt{y} + \sqrt{z} = \sqrt{a}$ ( $a > 0$ ) 上任何点处的切平面在各坐标轴上的截距之和等于 $a$ .

15. 设 $u(t)$ , $v(t)$ 是可导的向量值函数, 证明:

(1) $\frac{\mathrm{d}}{\mathrm{d}t}\left[\boldsymbol{u}(t)\pm \boldsymbol{v}(t)\right] = \boldsymbol{u}'(t)\pm \boldsymbol{v}'(t);$ 

(2) $\frac{\mathrm{d}}{\mathrm{d}t} [u(t)\cdot v(t)] = u'(t)\cdot v(t) + u(t)\cdot v'(t);$ 

(3) $\frac{\mathrm{d}}{\mathrm{d}t} [u(t)\times v(t)] = u'(t)\times v(t) + u(t)\times v'(t).$ 

# 第七节 方向导数与梯度

# 一、方向导数

偏导数反映的是函数沿坐标轴方向的变化率.但许多物理现象告诉我们,只考虑函数沿坐标轴方向的变化率是不够的.因此我们有必要来讨论函数沿任一指定方向的变化率问题.

设 l 是 xOy 平面上以 $P_{0}(x_{0}, y_{0})$ 为始点的一条射线, $e_{l} = (\cos \alpha, \cos \beta)$ 是与 l 同方向的单位向量(图 9-9). 射线 l 的参数方程为

$$
\left\{ \begin{array}{l l} x = x _ {0} + t \cos \alpha , \\ y = y _ {0} + t \cos \beta \end{array} \right. (t \geqslant 0).
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/e9e2cd99e5c7cc8235581c6595e0f0ae56d0af391ef27bbfd7c7780880531cbc.jpg)



图9-9


设函数 $z = f(x,y)$ 在点 $P_0(x_0,y_0)$ 的某个邻域$U(P_0)$ 内有定义， $P(x_0 + t\cos \alpha ,y_0 + t\cos \beta)$ 为 $l$ 上另一点，且 $P\in U(P_0)$ .如果函数增量 $f(x_0 + t\cos \alpha ,y_0 + t\cos \beta) - f(x_0,y_0)$ 与 $P$ 到 $P_{0}$ 的距离 $\mid PP_0\mid = t$ 的比值

$$
\frac {f (x _ {0} + t \cos \alpha , y _ {0} + t \cos \beta) - f (x _ {0} , y _ {0})}{t}
$$

当 $P$ 沿着 $l$ 趋于 $P_0$ （即 $t \to 0^+$ ）时的极限存在，那么称此极限为函数 $f(x, y)$ 在点 $P_0$ 沿方向 $l$ 的方向导数，记作 $\frac{\partial f}{\partial l}\Bigg|_{(x_0, y_0)}$ ，即

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0})} = \lim _ {t \rightarrow 0 ^ {+}} \frac {f (x _ {0} + t \cos \alpha , y _ {0} + t \cos \beta) - f (x _ {0} , y _ {0})}{t}. \tag {7-1}
$$

从方向导数的定义可知, 方向导数 $\left.\frac{\partial f}{\partial l}\right|_{(x_{0},y_{0})}$ 就是函数 $f(x,y)$ 在点 $P_{0}(x_{0},y_{0})$ 处沿方向 l 的变化率. 若函数 $f(x,y)$ 在点 $P_{0}(x_{0},y_{0})$ 的偏导数存在, $e_{l}=i=(1,0)$ , 则

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0})} = \lim _ {t \to 0 ^ {+}} \frac {f (x _ {0} + t , y _ {0}) - f (x _ {0} , y _ {0})}{t} = f _ {x} (x _ {0}, y _ {0});
$$

又若 $e_l = j = (0,1)$ ，则

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0})} = \lim _ {t \rightarrow 0 ^ {+}} \frac {f (x _ {0} , y _ {0} + t) - f (x _ {0} , y _ {0})}{t} = f _ {y} (x _ {0}, y _ {0}).
$$

但反之, 若 $e_{l}=i,\frac{\partial z}{\partial l}\bigg|_{(x_{0},y_{0})}$ 存在, 则 $\frac{\partial z}{\partial x}\bigg|_{(x_{0},y_{0})}$ 未必存在. 例如, $z=\sqrt{x^{2}+y^{2}}$ 在点 $O(0,0)$ 处沿 l=i 方向的方向导数 $\frac{\partial z}{\partial l}\bigg|_{(0,0)}=1$ , 而偏导数 $\frac{\partial z}{\partial x}\bigg|_{(0,0)}$ 不存在.

关于方向导数的存在及计算,我们有以下定理:

定理 如果函数 $f(x, y)$ 在点 $P_0(x_0, y_0)$ 可微分，那么函数在该点沿任一方向 $l$ 的方向导数存在，且有

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0})} = f _ {x} (x _ {0}, y _ {0}) \cos \alpha + f _ {y} (x _ {0}, y _ {0}) \cos \beta , \tag {7-2}
$$

其中 $\cos \alpha$ 和 $\cos \beta$ 是方向 l 的方向余弦.

证 由假设, $f(x,y)$ 在点 $(x_{0},y_{0})$ 可微分,故有

$$
f \left(x _ {0} + \Delta x, y _ {0} + \Delta y\right) - f \left(x _ {0}, y _ {0}\right) = f _ {x} \left(x _ {0}, y _ {0}\right) \Delta x + f _ {y} \left(x _ {0}, y _ {0}\right) \Delta y + o \left(\sqrt {\left(\Delta x\right) ^ {2} + \left(\Delta y\right) ^ {2}}\right).
$$

但点 $(x_0 + \Delta x, y_0 + \Delta y)$ 在以 $(x_0, y_0)$ 为始点的射线 $l$ 上时，应有 $\Delta x = t\cos \alpha, \Delta y = t\cos \beta,$ $\sqrt{(\Delta x)^2 + (\Delta y)^2} = t.$ 所以

$$
\lim _ {t \rightarrow 0 ^ {+}} \frac {f (x _ {0} + t \cos \alpha , y _ {0} + t \cos \beta) - f (x _ {0} , y _ {0})}{t} = f _ {x} (x _ {0}, y _ {0}) \cos \alpha + f _ {y} (x _ {0}, y _ {0}) \cos \beta .
$$

这就证明了方向导数存在,且其值为

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0})} = f _ {x} (x _ {0}, y _ {0}) \cos \alpha + f _ {y} (x _ {0}, y _ {0}) \cos \beta .
$$

例 1 求函数 $z = x e^{2y}$ 在点 $P(1,0)$ 处沿从点 $P(1,0)$ 到点 $Q(2,-1)$ 的方向的方向导数.

解 这里方向 $l$ 即向量 $\overrightarrow{PQ} = (1, -1)$ 的方向，与 $l$ 同向的单位向量为 $e_l = \left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$ .

因为函数可微分,且

$$
\left. \frac {\partial z}{\partial x} \right| _ {(1, 0)} = \mathrm{e} ^ {2 y} \Bigg | _ {(1, 0)} = 1, \quad \left. \frac {\partial z}{\partial y} \right| _ {(1, 0)} = 2 x \mathrm{e} ^ {2 y} \Bigg | _ {(1, 0)} = 2,
$$

故所求方向导数为

$$
\left. \frac {\partial z}{\partial l} \right| _ {(1, 0)} = 1 \times \frac {1}{\sqrt {2}} + 2 \times \left(- \frac {1}{\sqrt {2}}\right) = - \frac {\sqrt {2}}{2}.
$$

对于三元函数 $f(x, y, z)$ 来说，它在空间一点 $P_{0}(x_{0}, y_{0}, z_{0})$ 沿方向 $\pmb{e}_{l} = (\cos \alpha, \cos \beta, \cos \gamma)$ 的方向导数为

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0}, z _ {0})} = \lim _ {t \rightarrow 0 ^ {+}} \frac {f (x _ {0} + t \cos \alpha , y _ {0} + t \cos \beta , z _ {0} + t \cos \gamma) - f (x _ {0} , y _ {0} , z _ {0})}{t}. \tag {7-3}
$$

同样可以证明:如果函数 $f(x,y,z)$ 在点 $(x_{0},y_{0},z_{0})$ 可微分,那么函数在该点沿方向 $e_{l}=(\cos\alpha,\cos\beta,\cos\gamma)$ 的方向导数为

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0}, z _ {0})} = f _ {x} (x _ {0}, y _ {0}, z _ {0}) \cos \alpha + f _ {y} (x _ {0}, y _ {0}, z _ {0}) \cos \beta + f _ {z} (x _ {0}, y _ {0}, z _ {0}) \cos \gamma . \tag {7-4}
$$

例 2 求 $f(x,y,z)=xy+yz+zx$ 在点 $(1,1,2)$ 沿方向 l 的方向导数，其中 l 的方向角分别为 $60^{\circ},45^{\circ},60^{\circ}$ .

解 与 $l$ 同向的单位向量

$$
e _ {l} = (\cos 6 0 ^ {\circ}, \cos 4 5 ^ {\circ}, \cos 6 0 ^ {\circ}) = \left(\frac {1}{2}, \frac {\sqrt {2}}{2}, \frac {1}{2}\right).
$$

因为函数可微分,且

$$
f _ {x} (1, 1, 2) = (y + z) \mid_ {(1, 1, 2)} = 3,
$$

$$
f _ {y} (1, 1, 2) = (x + z) \mid_ {(1, 1, 2)} = 3,
$$

$$
f _ {z} (1, 1, 2) = (y + x) \mid_ {(1, 1, 2)} = 2.
$$

由公式(7-4)，得

$$
\left. \frac {\partial f}{\partial l} \right| _ {(1, 1, 2)} = 3 \times \frac {1}{2} + 3 \times \frac {\sqrt {2}}{2} + 2 \times \frac {1}{2} = \frac {1}{2} (5 + 3 \sqrt {2}).
$$

# 二、梯度

与方向导数有关联的一个概念是函数的梯度.在二元函数的情形,设函数 $f(x,y)$ 在平面区域D内具有一阶连续偏导数,则对于每一点 $P_{0}(x_{0},y_{0})\in D$ ,都可定出一个向量

$$
f _ {x} \left(x _ {0}, y _ {0}\right) i + f _ {y} \left(x _ {0}, y _ {0}\right) j,
$$

这向量称为函数 $f(x,y)$ 在点 $P_{0}(x_{0},y_{0})$ 的梯度，记作 $\operatorname{grad} f(x_{0},y_{0})$ 或 $\nabla f(x_{0},y_{0})$ ，即

$$
\operatorname{grad} f \left(x _ {0}, y _ {0}\right) = \nabla f \left(x _ {0}, y _ {0}\right) = f _ {x} \left(x _ {0}, y _ {0}\right) i + f _ {y} \left(x _ {0}, y _ {0}\right) j,
$$

其中 $\nabla = \frac{\partial}{\partial x} i + \frac{\partial}{\partial y} j$ 称为（二维的）向量微分算子或Nabla算子， $\nabla f = \frac{\partial f}{\partial x} i + \frac{\partial f}{\partial y} j.$ 

如果函数 $f(x,y)$ 在点 $P_0(x_0,y_0)$ 可微分， $\pmb{e}_l = (\cos \alpha, \cos \beta)$ 是与方向 $l$ 同向的单位向量，那么

$$
\begin{array}{l} \left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0})} = f _ {x} (x _ {0}, y _ {0}) \cos \alpha + f _ {y} (x _ {0}, y _ {0}) \cos \beta \\ = \operatorname{grad} f \left(x _ {0}, y _ {0}\right) \cdot e _ {l} = | \operatorname{grad} f \left(x _ {0}, y _ {0}\right) | \cos \theta , \\ \end{array}
$$

其中 $\theta = (\mathrm{grad}f(x_0,y_0),\widehat{e_l})$ 

这一关系式表明了函数在一点的梯度与函数在这点的方向导数间的关系.特别，由这关系可知：

（1）当 $\theta = 0$ ，即方向 $e_l$ 与梯度 $\operatorname{grad} f(x_0, y_0)$ 的方向相同时，函数 $f(x, y)$ 增加最快.此时，函数在这个方向的方向导数达到最大值，这个最大值就是梯度 $\operatorname{grad} f(x_0, y_0)$ 的模，即

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0})} = | \operatorname{grad} f (x _ {0}, y _ {0}) |.
$$

这个结果也表示: 函数 $f(x,y)$ 在一点的梯度 grad f 是这样一个向量, 它的方向是函数在这点的方向导数取得最大值的方向, 它的模就等于方向导数的最大值.

（2）当 $\theta = \pi$ ，即方向 $e_l$ 与梯度 $\operatorname{grad} f(x_0, y_0)$ 的方向相反时，函数 $f(x, y)$ 减少最快，函数在这个方向的方向导数达到最小值，即

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0})} = - | \operatorname{grad} f (x _ {0}, y _ {0}) |.
$$

(3) 当 $\theta=\frac{\pi}{2}$ ，即方向 $e_{l}$ 与梯度 grad $f(x_{0},y_{0})$ 的方向正交时，函数的变化率为零，即

$$
\left. \frac {\partial f}{\partial l} \right| _ {(x _ {0}, y _ {0})} = | \operatorname{grad} f (x _ {0}, y _ {0}) | \cos \theta = 0.
$$

我们知道,一般说来二元函数 $z=f(x,y)$ 在几何上表示一个曲面,这曲面被平面 z=c (c 是常数) 所截得的曲线 L 的方程为

$$
\left\{ \begin{array}{l} z = f (x, y), \\ z = c. \end{array} \right.
$$

这条曲线 L 在 xOy 面上的投影是一条平面曲线 $L^{*}$ （图 9-10），它在 xOy 平面直角坐标系中的方程为

$$
f (x, y) = c.
$$

对于曲线 $L^{*}$ 上的一切点, 已给函数的函数值都是 c, 所以我们称平面曲线 $L^{*}$ 为函数 $z = f(x, y)$ 的等值线.

若 $f_{x}, f_{y}$ 不同时为零，则等值线 $f(x, y) = c$ 上任一点 $P_{0}(x_{0}, y_{0})$ 处的一个单位法向

量为

$$
n = \frac {1}{\sqrt {f _ {x} ^ {2} (x _ {0} , y _ {0}) + f _ {y} ^ {2} (x _ {0} , y _ {0})}} \left(f _ {x} (x _ {0}, y _ {0}), f _ {y} (x _ {0}, y _ {0})\right) = \frac {\nabla f (x _ {0} , y _ {0})}{| \nabla f (x _ {0} , y _ {0}) |}.
$$

这表明函数 $f(x, y)$ 在一点 $(x_0, y_0)$ 的梯度 $\nabla f(x_0, y_0)$ 的方向就是等值线 $f(x, y) = c$ 在这点的法线方向 $\pmb{n}$ , 而梯度的模 $|\nabla f(x_0, y_0)|$ 就是沿这个法线方向的方向导数 $\frac{\partial f}{\partial n}$ , 于是有

$$
\nabla f (x _ {0}, y _ {0}) = \frac {\partial f}{\partial n} \boldsymbol {n}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/3b7d9817cfb7908a9278d1637534f7d71275a71050942cc03cc9bd69ae4902bb.jpg)



图9-10


上面讨论的梯度概念可以类似地推广到三元函数的情形. 设函数 $f(x, y, z)$ 在空间区域 $G$ 内具有一阶连续偏导数, 则对于每一点 $P_{0}(x_{0}, y_{0}, z_{0}) \in G$ , 都可定出一个向量

$$
f _ {x} \left(x _ {0}, y _ {0}, z _ {0}\right) i + f _ {y} \left(x _ {0}, y _ {0}, z _ {0}\right) j + f _ {z} \left(x _ {0}, y _ {0}, z _ {0}\right) k,
$$

这向量称为函数 $f(x, y, z)$ 在点 $P_0(x_0, y_0, z_0)$ 的梯度，将它记作 $\operatorname{grad} f(x_0, y_0, z_0)$ 或 $\nabla f(x_0, y_0, z_0)$ ，即

$$
\operatorname{grad} f \left(x _ {0}, y _ {0}, z _ {0}\right) = \nabla f \left(x _ {0}, y _ {0}, z _ {0}\right) = f _ {x} \left(x _ {0}, y _ {0}, z _ {0}\right) i + f _ {y} \left(x _ {0}, y _ {0}, z _ {0}\right) j + f _ {z} \left(x _ {0}, y _ {0}, z _ {0}\right) k,
$$

其中 $\nabla = \frac{\partial}{\partial x}\mathbf{i} + \frac{\partial}{\partial y}\mathbf{j} + \frac{\partial}{\partial z}\mathbf{k}$ 称为（三维的）向量微分算子或Nabla算子， $\nabla f = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j} + \frac{\partial f}{\partial z}\mathbf{k}$ 

经过与二元函数的情形完全类似的讨论可知,三元函数 $f(x,y,z)$ 在一点的梯度 $\nabla f$ 是这样一个向量,它的方向是函数 $f(x,y,z)$ 在这点的方向导数取得最大值的方向,它的模就等于方向导数的最大值.

如果引进曲面

$$
f (x, y, z) = c
$$

为函数 $f(x, y, z)$ 的等值面的概念, 那么可得函数 $f(x, y, z)$ 在一点 $(x_0, y_0, z_0)$ 的梯度 $\nabla f(x_0, y_0, z_0)$ 的方向就是等值面 $f(x, y, z) = c$ 在这点的法向量 $\pmb{n}$ , 而梯度的模$\left|\nabla f(x_{0},y_{0},z_{0})\right|$ 就是函数沿这个法向量的方向导数 $\frac{\partial f}{\partial n}$ .

例3 求 $\operatorname{grad} \frac{1}{x^2 + y^2}$ .

解 这里 $f(x,y) = \frac{1}{x^2 + y^2}$ . 因为

$$
\frac {\partial f}{\partial x} = - \frac {2 x}{\left(x ^ {2} + y ^ {2}\right) ^ {2}}, \quad \frac {\partial f}{\partial y} = - \frac {2 y}{\left(x ^ {2} + y ^ {2}\right) ^ {2}},
$$

所以

$$
\operatorname{grad} \frac {1}{x ^ {2} + y ^ {2}} = - \frac {2 x}{(x ^ {2} + y ^ {2}) ^ {2}} i - \frac {2 y}{(x ^ {2} + y ^ {2}) ^ {2}} j.
$$

例4 设 $f(x, y) = \frac{1}{2} (x^2 + y^2)$ ，点 $P_0(1, 1)$ ，求：

(1) $f(x,y)$ 在点 $P_{0}$ 处增加最快的方向以及 $f(x,y)$ 沿这个方向的方向导数；

(2) $f(x,y)$ 在点 $P_{0}$ 处减少最快的方向以及 $f(x,y)$ 沿这个方向的方向导数；

(3) $f(x,y)$ 在点 $P_{0}$ 处的变化率为零的方向.

解 (1) $f(x,y)$ 在点 $P_0$ 处沿 $\nabla f(1,1)$ 的方向增加最快，

$$
\nabla f (1, 1) = (x \boldsymbol {i} + y \boldsymbol {j}) \mid_ {(1, 1)} = \boldsymbol {i} + \boldsymbol {j},
$$

故所求方向可取为

$$
n = \frac {\nabla f (1 , 1)}{| \nabla f (1 , 1) |} = \frac {1}{\sqrt {2}} i + \frac {1}{\sqrt {2}} j,
$$

方向导数为

$$
\left. \frac {\partial f}{\partial n} \right| _ {(1, 1)} = | \nabla f (1, 1) | = \sqrt {2}.
$$

(2) $f(x,y)$ 在点 $P_{0}$ 处沿 $-\nabla f(1,1)$ 的方向减少最快,这方向可取为

$$
\boldsymbol {n} _ {1} = - \boldsymbol {n} = - \frac {1}{\sqrt {2}} i - \frac {1}{\sqrt {2}} j,
$$

方向导数为

$$
\frac {\partial f}{\partial n _ {1}} \mid_ {(1, 1)} = - | \nabla f (1, 1) | = - \sqrt {2}.
$$

(3) $f(x, y)$ 在点 $P_{0}$ 处沿垂直于 $\nabla f(1, 1)$ 的方向变化率为零, 这方向是

$$
\pmb {n} _ {2} = - \frac {1}{\sqrt {2}}   i + \frac {1}{\sqrt {2}}   j \quad \text {或} \quad \pmb {n} _ {3} = \frac {1}{\sqrt {2}}   i - \frac {1}{\sqrt {2}}   j.
$$

例 5 设 $f(x,y,z)=x^{3}-xy^{2}-z$ ，点 $P_{0}(1,1,0)$ 。问 $f(x,y,z)$ 在点 $P_{0}$ 处沿什么方向变化最快，在这个方向的变化率是多少？

解 $\nabla f = f_{x}\mathbf{i} + f_{y}\mathbf{j} + f_{z}\mathbf{k} = (3x^{2} - y^{2})\mathbf{i} - 2xy\mathbf{j} - \mathbf{k},\nabla f(1,1,0) = 2\mathbf{i} - 2\mathbf{j} - \mathbf{k}.$ 

$f(x,y,z)$ 在点 $P_{0}$ 处沿 $\nabla f(1,1,0)$ 的方向增加最快，沿 $-\nabla f(1,1,0)$ 的方向减少最快，在这两个方向的变化率分别是

$$
\begin{array}{l} \left| \nabla f (1, 1, 0) \right| = \sqrt {2 ^ {2} + (- 2) ^ {2} + 1} = 3, \\ - | \nabla f (1, 1, 0) | = - 3. \\ \end{array}
$$

例 6 求曲面 $x^{2}+y^{2}+z=9$ 在点 $P_{0}(1,2,4)$ 的切平面和法线方程.

解 设 $f(x,y,z)=x^{2}+y^{2}+z$ . 由梯度与等值面的关系可知, 梯度

$$
\nabla f \Big | _ {P _ {0}} = (2 x i + 2 y j + k) \Big | _ {(1, 2, 4)} = 2 i + 4 j + k
$$

的方向是等值面 $f(x,y,z)=9$ 在点 $P_{0}$ 的法线方向,因此切平面方程是

$$
2 (x - 1) + 4 (y - 2) + (z - 4) = 0,
$$

即

$$
2 x + 4 y + z = 1 4,
$$

曲面在点 $P_{0}$ 处的法线方程是

$$
x = 1 + 2 t, \quad y = 2 + 4 t, z = 4 + t \quad (t \text {为任意常数}).
$$

下面我们简单地介绍数量场与向量场的概念.

如果对于空间区域 G 内的任一点 M, 都有一个确定的数量 $f(M)$ , 那么称在这空间区域 G 内确定了一个数量场 (例如温度场、密度场等). 一个数量场可用一个数量函数 $f(M)$ 来确定. 如果与点 M 相对应的是一个向量 $F(M)$ , 那么称在这空间区域 G 内确定了一个向量场 (例如力场、速度场等). 一个向量场可用一个向量值函数 $F(M)$ 来确定, 而

$$
\boldsymbol {F} (M) = P (M) \boldsymbol {i} + Q (M) \boldsymbol {j} + R (M) \boldsymbol {k},
$$

其中 $P(M)$ , $Q(M)$ , $R(M)$ 是点 M 的数量函数.

若向量场 $F(M)$ 是某个数量函数 $f(M)$ 的梯度, 则称 $f(M)$ 是向量场 $F(M)$ 的一个势函数, 并称向量场 $F(M)$ 为势场. 由此可知, 由数量函数 $f(M)$ 产生的梯度场 grad $f(M)$ 是一个势场. 但需注意, 任意一个向量场并不一定都是势场, 因为它不一定是某个数量函数的梯度.

例 7 试求数量场 $\frac{m}{r}$ 所产生的梯度场, 其中常数 m > 0, $r = \sqrt{x^{2} + y^{2} + z^{2}}$ 为原点 O 与点 $M(x, y, z)$ 间的距离.

解 $\frac{\partial}{\partial x}\left(\frac{m}{r}\right) = -\frac{m}{r^2}\frac{\partial r}{\partial x} = -\frac{mx}{r^3},$ 

同理

$$
\frac {\partial}{\partial y} \left(\frac {m}{r}\right) = - \frac {m y}{r ^ {3}}, \quad \frac {\partial}{\partial z} \left(\frac {m}{r}\right) = - \frac {m z}{r ^ {3}}.
$$

从而

$$
\operatorname{grad} \frac {m}{r} = - \frac {m}{r ^ {2}} \left(\frac {x}{r} i + \frac {y}{r} j + \frac {z}{r} k\right).
$$

如果用 $e_r$ 表示与 $\overrightarrow{OM}$ 同方向的单位向量, 那么

$$
e _ {r} = \frac {x}{r} i + \frac {y}{r} j + \frac {z}{r} k,
$$

因此

$$
\operatorname{grad} \frac {m}{r} = - \frac {m}{r ^ {2}} e _ {r}.
$$

上式右端在力学上可解释为,位于原点 O 而质量为 m 的质点对位于点 M 而质量为 1 的质点的引力.这引力的大小与两质点的质量的乘积成正比、而与它们的距离平方成反比,这引力的方向由点 M 指向原点.因此数量场 $\frac{m}{r}$ 的势场,即梯度场 $\frac{m}{r}$ ,称为引力场,而函数 $\frac{m}{r}$ 称为引力势.

# 习题9-7

1. 求函数 $z=x^{2}+y^{2}$ 在点 $(1,2)$ 处沿从点 $(1,2)$ 到点 $(2,2+\sqrt{3})$ 的方向的方向导数.

2. 求函数 $z=\ln(x+y)$ 在抛物线 $y^{2}=4x$ 上点 (1,2) 处，沿着这抛物线在该点处偏向 x 轴正向的切线方向的方向导数.

3. 求函数 $z = 1 - \left(\frac{x^2}{a^2} + \frac{y^2}{b^2}\right)$ 在点 $\left(\frac{a}{\sqrt{2}}, \frac{b}{\sqrt{2}}\right)$ 处沿曲线 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ 在该点的内法线方向的方向导数.

4. 求函数 $u = xy^{2} + z^{3} - xyz$ 在点 $(1, 1, 2)$ 处沿方向角为 $\alpha = \frac{\pi}{3}, \beta = \frac{\pi}{4}, \gamma = \frac{\pi}{3}$ 的方向的方向导数.

5. 求函数 u=xyz 在点 $(5,1,2)$ 处沿从点 $(5,1,2)$ 到点 $(9,4,14)$ 的方向的方向导数.

6. 求函数 $u=x^{2}+y^{2}+z^{2}$ 在曲线 x=t, $y=t^{2}$ , $z=t^{3}$ 上点 (1,1,1) 处，沿曲线在该点的切线正方向（对应于 t 增大的方向）的方向导数.

7. 求函数 $u = x + y + z$ 在球面 $x^{2} + y^{2} + z^{2} = 1$ 上点 $(x_{0}, y_{0}, z_{0})$ 处，沿球面在该点的外法线方向的方向导数.

8. 设 $f(x, y, z) = x^{2} + 2y^{2} + 3z^{2} + xy + 3x - 2y - 6z$ ，求

$\operatorname{grad} f(0,0,0)$ 及 $\operatorname{grad} f(1,1,1)$ .

9. 设函数 $u(x,y,z)$ , $v(x,y,z)$ 的各个偏导数都存在且连续, 证明:

(1) $\nabla(cu)=c\nabla u$ (其中 c 为常数);

(2) $\nabla (u\pm v) = \nabla u\pm \nabla v;$ 

(3) $\nabla(uv)=v\nabla u+u\nabla v;$ 

(4) $\nabla \left(\frac{u}{v}\right) = \frac{v\nabla u - u\nabla v}{v^2} (v\neq 0).$ 

10. 求函数 $u = xy^{2}z$ 在点 $P_{0}(1, -1, 2)$ 处变化最快的方向，并求沿这个方向的方向导数.

# 第八节 多元函数的极值及其求法

# 一、多元函数的极值及最大值与最小值

在实际问题中,往往会遇到多元函数的最大值与最小值问题.与一元函数相类似,多元函数的最大值、最小值与极大值、极小值有密切联系,因此我们以二元函数为例,先来讨论多元函数的极值问题.

定义 设函数 $z = f(x, y)$ 的定义域为 $D, P_0(x_0, y_0)$ 为 $D$ 的内点. 若存在 $P_0$ 的某个邻域 $U(P_0) \subset D$ , 使得对于该邻域内异于 $P_0$ 的任何点 $(x, y)$ , 都有

$$
f (x, y) <   f \left(x _ {0}, y _ {0}\right),
$$

则称函数 $f(x,y)$ 在点 $(x_{0},y_{0})$ 有极大值 $f(x_{0},y_{0})$ ，点 $(x_{0},y_{0})$ 称为函数 $f(x,y)$ 的极大值点；若对于该邻域内异于 $P_{0}$ 的任何点 $(x,y)$ ，都有

$$
f (x, y) > f \left(x _ {0}, y _ {0}\right),
$$

则称函数 $f(x,y)$ 在点 $(x_{0},y_{0})$ 有极小值 $f(x_{0},y_{0})$ ，点 $(x_{0},y_{0})$ 称为函数 $f(x,y)$ 的极小值点。极大值与极小值统称为极值。使得函数取得极值的点称为极值点。

例 1 函数 $z=3x^{2}+4y^{2}$ 在点 $(0,0)$ 处有极小值. 因为对于点 $(0,0)$ 的任一邻域内异于 $(0,0)$ 的点, 函数值都为正, 而在点 $(0,0)$ 处的函数值为零. 从几何上看这是显然的, 因为点 $(0,0,0)$ 是开口朝上的椭圆抛物面 $z=3x^{2}+4y^{2}$ 的顶点.

例2 函数 $z = -\sqrt{x^2 + y^2}$ 在点 $(0,0)$ 处有极大值. 因为在点 $(0,0)$ 处函数值为零, 而对于点 $(0,0)$ 的任一邻域内异于 $(0,0)$ 的点, 函数值都为负. 点 $(0,0,0)$ 是位于 $xOy$ 平面下方的锥面 $z = -\sqrt{x^2 + y^2}$ 的顶点.

例 3 函数 z=xy 在点 $(0,0)$ 处既不取得极大值也不取得极小值. 因为在点 $(0,0)$ 处的函数值为零, 而在点 $(0,0)$ 的任一邻域内, 总有使函数值为正的点, 也有使函数值为负的点.

以上关于二元函数的极值概念, 可推广到 n 元函数. 设 n 元函数 $u = f(P)$ 的定义域为 D, $P_{0}$ 为 D 的内点. 若存在 $P_{0}$ 的某个邻域 $U(P_{0}) \subset D$ , 使得该邻域内异于 $P_{0}$ 的任何点 P, 都有

$$
f (P) <   f (P _ {0}) (\text {或} f (P) > f (P _ {0})),
$$

则称函数 $f(P)$ 在点 $P_{0}$ 有极大值(或极小值) $f(P_{0})$ .

二元函数的极值问题,一般可以利用偏导数来解决.下面两个定理就是关于这问题的结论.

定理1（必要条件）设函数 $z = f(x,y)$ 在点 $(x_0,y_0)$ 具有偏导数，且在点 $(x_0,y_0)$ 处有极值，则有

$$
f _ {x} (x _ {0}, y _ {0}) = 0, \quad f _ {y} (x _ {0}, y _ {0}) = 0.
$$

证 不妨设 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处有极大值. 依照极大值的定义, 在点 $(x_0, y_0)$ 的某邻域内异于 $(x_0, y_0)$ 的点 $(x, y)$ 都适合不等式

$$
f (x, y) <   f \left(x _ {0}, y _ {0}\right).
$$

特殊地,在该邻域内取 $y=y_{0}$ 而 $x\neq x_{0}$ 的点,也应适合不等式

$$
f (x, y _ {0}) <   f (x _ {0}, y _ {0}).
$$

这表明一元函数 $f(x, y_0)$ 在 $x = x_0$ 处取得极大值，因而必有

$$
f _ {x} (x _ {0}, y _ {0}) = 0.
$$

类似可证

$$
f _ {y} (x _ {0}, y _ {0}) = 0.
$$

从几何上看,这时如果曲面 $z=f(x,y)$ 在点 $(x_{0},y_{0},z_{0})$ 处有切平面,则切平面

$$
z - z _ {0} = f _ {x} (x _ {0}, y _ {0}) (x - x _ {0}) + f _ {y} (x _ {0}, y _ {0}) (y - y _ {0})
$$

成为平行于 $xOy$ 坐标面的平面 $z - z_0 = 0$ .

类似地推得,如果三元函数 $u=f(x,y,z)$ 在点 $(x_{0},y_{0},z_{0})$ 具有偏导数,那么它在点 $(x_{0},y_{0},z_{0})$ 具有极值的必要条件为

$$
f _ {x} (x _ {0}, y _ {0}, z _ {0}) = 0, \quad f _ {\gamma} (x _ {0}, y _ {0}, z _ {0}) = 0, \quad f _ {z} (x _ {0}, y _ {0}, z _ {0}) = 0.
$$

仿照一元函数,凡是能使 $f_{x}(x,y)=0,f_{y}(x,y)=0$ 同时成立的点 $(x_{0},y_{0})$ 称为函数 $z=f(x,y)$ 的驻点.从定理1可知,具有偏导数的函数的极值点必定是驻点.但函数的驻点不一定是极值点,例如,点(0,0)是函数z=xy的驻点,但函数在该点并无极值.

怎样判定一个驻点是否是极值点呢？下面的定理回答了这个问题.

定理2（充分条件）设函数 $z = f(x,y)$ 在点 $(x_0,y_0)$ 的某邻域内连续且有一阶及二阶连续偏导数，又 $f_{x}(x_{0},y_{0}) = 0,f_{y}(x_{0},y_{0}) = 0$ ，令

$$
f _ {x x} \left(x _ {0}, y _ {0}\right) = A, \quad f _ {x y} \left(x _ {0}, y _ {0}\right) = B, \quad f _ {y y} \left(x _ {0}, y _ {0}\right) = C,
$$

则 $f(x, y)$ 在 $(x_0, y_0)$ 处是否取得极值的条件如下：

(1) $AC - B^{2} > 0$ 时具有极值, 且当 $A < 0$ 时有极大值, 当 $A > 0$ 时有极小值;

(2) $AC - B^{2} < 0$ 时没有极值；

(3) $AC - B^{2} = 0$ 时可能有极值, 也可能没有极值, 还需另作讨论.

这个定理现在不证①.利用定理1、定理2,我们把具有二阶连续偏导数的函数 $z=f(x,y)$ 的极值的求法叙述如下:

第一步 解方程组

$$
f _ {x} (x, y) = 0, \quad f _ {y} (x, y) = 0,
$$

求得一切实数解,即可求得一切驻点.

第二步 对于每一个驻点 $(x_0, y_0)$ ，求出二阶偏导数的值 $A, B$ 和 $C$ .

第三步 定出 $AC - B^2$ 的符号, 按定理2的结论判定 $f(x_0, y_0)$ 是不是极值、是极大值还是极小值.

例 4 求函数 $f(x,y)=x^{3}-y^{3}+3x^{2}+3y^{2}-9x$ 的极值.

解 先解方程组

$$
\left\{ \begin{array}{l} f _ {x} (x, y) = 3 x ^ {2} + 6 x - 9 = 0, \\ f _ {y} (x, y) = - 3 y ^ {2} + 6 y = 0, \end{array} \right.
$$

求得驻点为(1,0)，(1,2)，(-3,0)，(-3,2).

再求出二阶偏导数

$$
f _ {x x} (x, y) = 6 x + 6, \quad f _ {x y} (x, y) = 0, \quad f _ {y y} (x, y) = - 6 y + 6.
$$

在点(1,0)处, 因为 $AC-B^{2}=12\times6>0$ , 又 A>0, 所以函数在(1,0)处有极小值 $f(1,0)=-5$ ;

在点(1,2)处,因为 $AC-B^{2}=12\times(-6)<0$ , 所以 $f(1,2)$ 不是极值;

在点 $(-3,0)$ 处，因为 $AC-B^{2}=-12\times6<0$ ，所以 $f(-3,0)$ 不是极值；

在点 $(-3,2)$ 处，因为 $AC-B^{2}=-12\times(-6)>0$ ，又A<0，所以函数在 $(-3,2)$ 处有极大值 $f(-3,2)=31$ .

讨论函数的极值问题时,如果函数在所讨论的区域内具有偏导数,那么由定理1可知,极值只可能在驻点处取得.然而,如果函数在个别点处的偏导数不存在,这些点当然不是驻点,但也可能是极值点.例如在例2中,函数 $z=-\sqrt{x^{2}+y^{2}}$ 在点(0,0)处的偏导数不存在,但该函数在点(0,0)处却具有极大值.因此,在考虑函数的极值问题时,除了考虑函数的驻点外,如果有偏导数不存在的点,那么对这些点也应当考虑.

与一元函数相类似,我们可以利用函数的极值来求函数的最大值和最小值.在第一节中已经指出,如果 $f(x,y)$ 在有界闭区域D上连续,那么 $f(x,y)$ 在D上必定能取得最大值和最小值.这种使函数取得最大值或最小值的点既可能在D的内部,也可能在D的边界上.我们假定,函数在D上连续、在D内可微分且只有有限个驻点,这时如果函数在 D 的内部取得最大值(最小值),那么这个最大值(最小值)也是函数的极大值(极小值).因此,在上述假定下,求函数的最大值和最小值的一般方法是:将函数 $f(x,y)$ 在 D 内的所有驻点处的函数值及在 D 的边界上的最大值和最小值相互比较,其中最大的就是最大值,最小的就是最小值.但这种做法,由于要求出 $f(x,y)$ 在 D 的边界上的最大值和最小值,所以往往相当复杂.在通常遇到的实际问题中,如果根据问题的性质,知道函数 $f(x,y)$ 的最大值(最小值)一定在 D 的内部取得,而函数在 D 内只有一个驻点,那么可以肯定该驻点处的函数值就是函数 $f(x,y)$ 在 D 上的最大值(最小值).

例 5 某厂要用铁板做成一个体积为 $2 \, m^{3}$ 的有盖长方体水箱. 问当长、宽和高各取怎样的尺寸时, 才能使用料最省.

解 设水箱的长为 $x \mathrm{~m}$ , 宽为 $y \mathrm{~m}$ , 则其高应为 $\frac{2}{xy} \mathrm{~m}$ . 此水箱所用材料的面积为 $A = 2 \left( xy + y \cdot \frac{2}{xy} + x \cdot \frac{2}{xy} \right)$ , 即

$$
A = 2 \left(x y + \frac {2}{x} + \frac {2}{y}\right) (x > 0, y > 0).
$$

可见材料面积 $A = A(x,y)$ 是 $x$ 和 $y$ 的二元函数，这就是目标函数，下面求使这函数取得最小值的点 $(x,y)$ .

令

$$
A _ {x} = 2 \left(y - \frac {2}{x ^ {2}}\right) = 0, A _ {y} = 2 \left(x - \frac {2}{y ^ {2}}\right) = 0.
$$

解这方程组,得

$$
x = \sqrt [ 3 ]{2}, \quad y = \sqrt [ 3 ]{2}.
$$

根据题意可以知道,水箱所用材料面积的最小值一定存在,并在开区域 $D = \{(x, y) | x > 0, y > 0\}$ 内取得. 又函数在 $D$ 内只有唯一的驻点 $(\sqrt[3]{2}, \sqrt[3]{2})$ , 因此可断定当 $x = \sqrt[3]{2}, y = \sqrt[3]{2}$ 时, $A$ 取得最小值. 就是说, 当水箱的长为 $\sqrt[3]{2} \mathrm{~m}$ 、宽为 $\sqrt[3]{2} \mathrm{~m}$ 、高为 $\frac{2}{\sqrt[3]{2} \cdot \sqrt[3]{2}} = \sqrt[3]{2} \mathrm{~m}$ 时, 水箱所用的材料最省.

从这个例子还可看出,在体积一定的长方体中,以立方体的表面积为最小.

例 6 有一宽为 24 cm 的长方形铁板,把它两边折起来做成一断面为等腰梯形的水槽.问怎样折法才能使断面的面积最大?

解 设折起来的边长为 $x \mathrm{~cm}$ , 倾角为 $\alpha$ (图9-11), 则梯形断面的下底长为 $(24 - 2x) \mathrm{cm}$ , 上底长为 $(24 - 2x + 2x \cos \alpha) \mathrm{cm}$ , 高为 $(x \sin \alpha) \mathrm{cm}$ , 所以断面面积

$$
A = \frac {1}{2} (2 4 - 2 x + 2 x \cos \alpha + 2 4 - 2 x) \cdot x \sin \alpha ,
$$

即

$$
A = 2 4 x \sin \alpha - 2 x ^ {2} \sin \alpha + x ^ {2} \sin \alpha \cos \alpha \quad \left(0 <   x <   1 2, 0 <   \alpha \leqslant \frac {\pi}{2}\right).
$$

可见断面面积 $A = A(x, \alpha)$ , 这就是目标函数, 下面求使这函数取得最大值的点 $(x, \alpha)$ . 令

$$
\left\{ \begin{array}{l} A _ {x} = 2 4 \sin \alpha - 4 x \sin \alpha + 2 x \sin \alpha \cos \alpha = 0, \\ A _ {\alpha} = 2 4 x \cos \alpha - 2 x ^ {2} \cos \alpha + x ^ {2} (\cos^ {2} \alpha - \sin^ {2} \alpha) = 0. \end{array} \right.
$$

由于 $\sin \alpha \neq 0, x \neq 0$ ，上述方程组可化为

$$
\left\{ \begin{array}{l} 1 2 - 2 x + x \cos \alpha = 0, \\ 2 4 \cos \alpha - 2 x \cos \alpha + x (\cos^ {2} \alpha - \sin^ {2} \alpha) = 0. \end{array} \right.
$$

解这方程组, 得

$$
\alpha = \frac {\pi}{3}, \quad x = 8.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a3997f70a97eb7865e5b5957cfad93ce400fca3f0edbfc39dc53daeabf732c7f.jpg)



图9-11


根据题意可知断面面积的最大值一定存在,并且在 $D=\left\{(x,\alpha)\mid0<x<12,0<\alpha\leqslant\frac{\pi}{2}\right\}$ 内取得.通过计算得知 $\alpha=\frac{\pi}{2}$ 时的函数值比 $\alpha=\frac{\pi}{3}, x=8$ 时的函数值小.又函数在 D 内只有一个驻点,因此可以断定,当 $x=8,\alpha=\frac{\pi}{3}$ 时,就能使断面的面积最大.

# 二、条件极值 拉格朗日乘数法

上面所讨论的极值问题,对于函数的自变量,除了限制在函数的定义域内以外,并无其他条件,所以有时候称为无条件极值.但在实际问题中,有时会遇到对函数的自变量还有附加条件的极值问题.例如,求表面积为 $a^{2}$ 而体积为最大的长方体的体积问题.设长方体的三棱的长为x,y与z,则体积V=xyz.又因假定表面积为 $a^{2}$ ,所以自变量x,y与z还必须满足附加条件 $2(xy+yz+xz)=a^{2}$ .像这种对自变量有附加条件的极值称为条件极值.对于有些实际问题,可以把条件极值化为无条件极值,然后利用第一目中的方法加以解决.例如上述问题,可由条件 $2(xy+yz+xz)=a^{2}$ ,将z表示成

$$
z = \frac {a ^ {2} - 2 x y}{2 (x + y)}.
$$

再把它代入 $V = xyz$ 中, 于是问题就化为求

$$
V = \frac {x y}{2} \left(\frac {a ^ {2} - 2 x y}{x + y}\right)
$$

的无条件极值.例5也是属于把条件极值化为无条件极值的例子.

但在很多情形下,将条件极值化为无条件极值并不这样简单.另有一种直接寻求条件极值的方法,可以不必先把问题化到无条件极值的问题,这就是下面要介绍的拉格朗日乘数法.

现在先来寻求函数

$$
z = f (x, y) \tag {8-1}
$$

在条件

$$
\varphi (x, y) = 0 \tag {8-2}
$$

下取得极值的必要条件.

如果函数(8-1)在 $(x_{0},y_{0})$ 取得所求的极值,那么首先有

$$
\varphi \left(x _ {0}, y _ {0}\right) = 0. \tag {8-3}
$$

我们假定在 $(x_0, y_0)$ 的某一邻域内 $f(x, y)$ 与 $\varphi(x, y)$ 均有连续的一阶偏导数，而 $\varphi_y(x_0, y_0) \neq 0$ 。由隐函数存在定理可知，方程(8-2)确定一个连续且具有连续导数的函数 $y = \psi(x)$ ，将其代入(8-1)式，结果得到一个变量 $x$ 的函数

$$
z = f [ x, \psi (x) ]. \tag {8-4}
$$

于是函数(8-1)在 $(x_{0},y_{0})$ 取得所求的极值,也就是相当于函数(8-4)在 $x=x_{0}$ 取得极值.由一元可导函数取得极值的必要条件知道

$$
\left. \frac {\mathrm{d} z}{\mathrm{d} x} \right| _ {x = x _ {0}} = f _ {x} \left(x _ {0}, y _ {0}\right) + f _ {y} \left(x _ {0}, y _ {0}\right) \frac {\mathrm{d} y}{\mathrm{d} x} \Bigg | _ {x = x _ {0}} = 0, \tag {8-5}
$$

而由(8-2)用隐函数求导公式,有

$$
\left. \frac {\mathrm{d} y}{\mathrm{d} x} \right| _ {x = x _ {0}} = - \frac {\varphi_ {x} (x _ {0} , y _ {0})}{\varphi_ {y} (x _ {0} , y _ {0})}.
$$

把上式代入(8-5)式,得

$$
f _ {x} \left(x _ {0}, y _ {0}\right) - f _ {y} \left(x _ {0}, y _ {0}\right) \frac {\varphi_ {x} \left(x _ {0} , y _ {0}\right)}{\varphi_ {y} \left(x _ {0} , y _ {0}\right)} = 0. \tag {8-6}
$$

(8-3)、(8-6)两式就是函数(8-1)在条件(8-2)下在 $(x_0, y_0)$ 取得极值的必要条件.

设 $\frac{f_y(x_0,y_0)}{\varphi_y(x_0,y_0)} = -\lambda$ ，上述必要条件就变为

$$
\left\{ \begin{array}{l} f _ {x} \left(x _ {0}, y _ {0}\right) + \lambda \varphi_ {x} \left(x _ {0}, y _ {0}\right) = 0, \\ f _ {y} \left(x _ {0}, y _ {0}\right) + \lambda \varphi_ {y} \left(x _ {0}, y _ {0}\right) = 0, \\ \varphi \left(x _ {0}, y _ {0}\right) = 0. \end{array} \right. \tag {8-7}
$$

若引进辅助函数

$$
L (x, y) = f (x, y) + \lambda \varphi (x, y),
$$

则不难看出，(8-7)中前两式就是

$$
L _ {x} (x _ {0}, y _ {0}) = 0, \quad L _ {y} (x _ {0}, y _ {0}) = 0.
$$

函数 $L(x,y)$ 称为拉格朗日函数, 参数 $\lambda$ 称为拉格朗日乘子.

由以上讨论,我们得到以下结论:

拉格朗日乘数法 要找函数 $z = f(x,y)$ 在附加条件 $\varphi (x,y) = 0$ 下的可能极值点，可以先作拉格朗日函数

$$
L (x, y) = f (x, y) + \lambda \varphi (x, y),
$$

其中 $\lambda$ 为参数. 求其对 $x$ 与 $y$ 的一阶偏导数, 并使之为零, 然后与方程(8-2)联立起来:

$$
\left\{ \begin{array}{l} f _ {x} (x, y) + \lambda \varphi_ {x} (x, y) = 0, \\ f _ {y} (x, y) + \lambda \varphi_ {y} (x, y) = 0, \\ \varphi (x, y) = 0. \end{array} \right. \tag {8-8}
$$

由这方程组解出 $x, y$ 及 $\lambda$ , 这样得到的 $(x, y)$ 就是函数 $f(x, y)$ 在附加条件 $\varphi(x, y) = 0$ 下的可能极值点.

这方法还可以推广到自变量多于两个而条件多于一个的情形.例如,要求函数

$$
u = f (x, y, z, t)
$$

在附加条件

$$
\varphi (x, y, z, t) = 0, \quad \psi (x, y, z, t) = 0 \tag {8-9}
$$

下的极值,可以先作拉格朗日函数

$$
L (x, y, z, t) = f (x, y, z, t) + \lambda \varphi (x, y, z, t) + \mu \psi (x, y, z, t),
$$

其中 $\lambda, \mu$ 均为参数, 求其一阶偏导数, 并使之为零, 然后与 (8-9) 中的两个方程联立起来求解, 这样得出的 $(x, y, z, t)$ 就是函数 $f(x, y, z, t)$ 在附加条件 (8-9) 下的可能极值点.

至于如何确定所求得的点是不是极值点,在实际问题中往往可根据问题本身的性质来判定.

例 7 求表面积为 $a^{2}$ 而体积为最大的长方体的体积.

解 设长方体的三棱长为 $x, y$ 与 $z$ , 则问题就是在条件

$$
\varphi (x, y, z) = 2 x y + 2 y z + 2 x z - a ^ {2} = 0 \tag {8-10}
$$

下,求函数

$$
V = x y z \quad (x > 0, y > 0, z > 0)
$$

的最大值.作拉格朗日函数

$$
L (x, y, z) = x y z + \lambda (2 x y + 2 y z + 2 x z - a ^ {2}),
$$

求其对 $x, y$ 与 $z$ 的偏导数，并使之为零，得到

$$
\left\{ \begin{array}{l} y z + 2 \lambda (y + z) = 0, \\ x z + 2 \lambda (x + z) = 0, \\ x y + 2 \lambda (y + x) = 0. \end{array} \right. \tag {8-11}
$$

再与(8-10)联立求解.

因为 $x, y$ 与 $z$ 都不等于零，所以由(8-11)可得

$$
\frac {x}{y} = \frac {x + z}{y + z}, \quad \frac {y}{z} = \frac {x + y}{x + z}.
$$

由以上两式解得

$$
x = y = z.
$$

将此代入(8-10)式,便得

$$
x = y = z = \frac {\sqrt {6}}{6} a,
$$

这是唯一可能的极值点.因为由问题本身可知最大值一定存在,所以最大值就在这个可能的极值点处取得.也就是说,表面积为 $a^{2}$ 的长方体中,以棱长为 $\frac{\sqrt{6}}{6}a$ 的立方体的体积为最大,最大体积 $V=\frac{\sqrt{6}}{36}a^{3}$ .

例8 求函数 $u = xyz$ 在附加条件

$$
\frac {1}{x} + \frac {1}{y} + \frac {1}{z} = \frac {1}{a} (x > 0, y > 0, z > 0, a > 0) \tag {8-12}
$$

下的极值.

解 作拉格朗日函数

$$
L (x, y, z) = x y z + \lambda \left(\frac {1}{x} + \frac {1}{y} + \frac {1}{z} - \frac {1}{a}\right).
$$

令

$$
\left\{ \begin{array}{l} L _ {x} = y z - \frac {\lambda}{x ^ {2}} = 0, \\ L _ {y} = x z - \frac {\lambda}{y ^ {2}} = 0, \\ L _ {z} = x y - \frac {\lambda}{z ^ {2}} = 0. \end{array} \right. \tag {8-13}
$$

注意到以上三个方程左端的第一项都是三个变量 $x, y$ 与 $z$ 中某两个变量的乘积，将各方程两端同乘相应缺少的那个变量，使各方程左端的第一项都成为 $xyz$ ，然后将所得的三个方程左、右两端相加，得

$$
3 x y z - \lambda \left(\frac {1}{x} + \frac {1}{y} + \frac {1}{z}\right) = 0,
$$

把(8-12)代入上式,得

$$
x y z = \frac {\lambda}{3 a}.
$$

再把这个结果分别代入(8-13)中各式, 便得 $x = y = z = 3a$ . 由此得到点 $(3a, 3a, 3a)$ 是函数 $u = xyz$ 在条件(8-12)下唯一可能的极值点. 把条件(8-12)确定的隐函数记作 $z = z(x, y)$ , 将目标函数看做 $u = xyz(x, y) = F(x, y)$ , 再应用二元函数极值的充分条件判断, 可知点 $(3a, 3a, 3a)$ 是函数 $u = xyz$ 在条件(8-12)下的极小值点. 因此, 目标函数 $u = xyz$ 在条件(8-12)下在点 $(3a, 3a, 3a)$ 处取得极小值 $27a^3$ .

下面的问题涉及经济学中的一个最优价格的模型.

在生产和销售商品过程中,商品销售量、生产成本与销售价格是相互影响的.厂家要选择合理的销售价格,才能获得最大利润.这个价格称为最优价格.下面的例题就是讨论怎样确定电视机的最优价格.

例 9 设某电视机厂生产一台电视机的成本为 C, 每台电视机的销售价格为 p, 销售量为 x. 假设该厂的生产处于平衡状态, 即电视机的生产量等于销售量. 根据市场预测, 销售量 x 与销售价格 p 之间有下面的关系:

$$
x = M \mathrm{e} ^ {- a p} \quad (M > 0, a > 0), \tag {8-14}
$$

其中 M 为市场最大需求量, a 是价格系数. 同时, 生产部门根据对生产环节的分析, 对每台电视机的生产成本 C 有如下测算:

$$
C = C _ {0} - k \ln x (k > 0, x > 1), \tag {8-15}
$$

其中 $C_{0}$ 是只生产一台电视机时的成本, k 是规模系数.

根据上述条件,应如何确定电视机的售价p,才能使该厂获得最大利润?

解 设厂家获得的利润为 u，每台电视机售价为 p，每台生产成本为 C，销售量为 x，则

$$
u = (p - C) x.
$$

于是问题化为求利润函数 $u = (p - C)x$ 在附加条件(8-14)、(8-15)下的极值问题.

作拉格朗日函数

$$
L (x, p, C) = (p - C) x + \lambda (x - M e ^ {- a p}) + \mu (C - C _ {0} + k \ln x).
$$

令

$$
\left\{ \begin{array}{l} L _ {x} = (p - C) + \lambda + k \frac {\mu}{x} = 0, \\ L _ {p} = x + \lambda a M e ^ {- a p} = 0, \\ L _ {C} = - x + \mu = 0. \end{array} \right.
$$

将(8-14)代入(8-15)，得

$$
C = C _ {0} - k (\ln M - a p). \tag {8-16}
$$

由(8-14)及 $L_{p}=0$ 知 $\lambda a=-1$ ，即

$$
\lambda = - \frac {1}{a}. \tag {8-17}
$$

由 $L_{c} = 0$ 知 $x = \mu$ ，即

$$
\frac {x}{\mu} = 1. \tag {8-18}
$$

将(8-16)、(8-17)和(8-18)代入 $L_{x}=0$ ，得

$$
p - C _ {0} + k (\ln M - a p) - \frac {1}{a} + k = 0,
$$

由此得

$$
p ^ {*} = \frac {C _ {0} - k \ln M + \frac {1}{a} - k}{1 - a k}.
$$

因为由问题本身可知最优价格必定存在,所以这个 $p^{*}$ 就是电视机的最优价格.只要确定了规模系数 k、价格系数 a,电视机的最优价格问题就解决了.

# 习题9-8

1. 已知函数 $f(x, y)$ 在点(0,0)的某个邻域内连续，且

$$
\lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - x y}{(x ^ {2} + y ^ {2}) ^ {2}} = 1,
$$

则下述四个选项中正确的是( ).

(A) 点 $(0,0)$ 不是 $f(x,y)$ 的极值点

(B) 点 $(0,0)$ 是 $f(x,y)$ 的极大值点

(C) 点 $(0,0)$ 是 $f(x,y)$ 的极小值点

(D) 根据所给条件无法判断(0,0)是不是 $f(x,y)$ 的极值点

2. 求函数 $f(x, y) = 4(x - y) - x^2 - y^2$ 的极值.

3. 求函数 $f(x,y)=(6x-x^{2})(4y-y^{2})$ 的极值.

4. 求两直线 $\left\{\begin{aligned} y &= 2x, \\ z &= x+1 \end{aligned}\right.$ 与 $\left\{\begin{aligned} y &= x+3, \\ z &= x \end{aligned}\right.$ 之间的最短距离.

5. 求函数 z = xy 在适合附加条件 $x + y = 1$ 下的极大值.

6. 从斜边长为 l 的一切直角三角形中, 求有最大周长的直角三角形.

7. 要造一个体积等于定数 $k$ 的长方体无盖水池, 应如何选择水池的尺寸, 方可使它的表面积最小.

8. 在平面 $xOy$ 上求一点, 使它到 $x = 0, \gamma = 0$ 及 $x + 2\gamma - 16 = 0$ 三直线的距离平方之和为最小.

9. 将周长为 $2p$ 的矩形绕它的一边旋转而构成一个圆柱体. 问矩形的边长各为多少时, 才可使圆柱体的体积为最大?

10. 求内接于半径为 a 的球且有最大体积的长方体.

11. 抛物面 $z=x^{2}+y^{2}$ 被平面 $x+y+z=1$ 截成一椭圆，求这椭圆上的点到原点的距离的最大值与最小值.

12. 设有一圆板占有平面闭区域 $\{(x,y) \mid x^{2}+y^{2}\leqslant1\}$ . 该圆板被加热, 以致在点 $(x,y)$ 的温度是 $T=x^{2}+2y^{2}-x$ . 求该圆板的最热点和最冷点.

13. 形状为椭球 $4x^{2}+y^{2}+4z^{2}\leqslant16$ 的空间探测器进入地球大气层, 其表面开始受热, 1 h 后在探测器的点 $(x,y,z)$ 处的温度 $T=8x^{2}+4yz-16z+600$ , 求探测器表面最热的点.

# * 第九节 二元函数的泰勒公式

# 一、二元函数的泰勒公式

在上册第三章,我们已经知道:若函数 $f(x)$ 在 $x_{0}$ 的某邻域内具有直到 $(n+1)$ 阶导数,则对该邻域内的任一x,有n阶泰勒公式

$$
\begin{array}{l} f (x) = f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(x - x _ {0}\right) + \frac {f ^ {\prime \prime} \left(x _ {0}\right)}{2 !} \left(x - x _ {0}\right) ^ {2} + \dots + \frac {f ^ {(n)} \left(x _ {0}\right)}{n !} \left(x - x _ {0}\right) ^ {n} + \\ \frac {f ^ {(n + 1)} \left(x _ {0} + \theta \left(x - x _ {0}\right)\right)}{(n + 1) !} \left(x - x _ {0}\right) ^ {n + 1} \quad (0 <   \theta <   1) \\ \end{array}
$$

成立.利用一元函数的泰勒公式,我们可用n次多项式来近似表达函数 $f(x)$ ,且误差是当 $x\rightarrow x_{0}$ 时比 $(x-x_{0})^{n}$ 高阶的无穷小.对于多元函数来说,无论是为了理论的或实际计算的需要,也都有必要考虑用多个变量的多项式来近似表达一个给定的多元函数,并能具体地估算出误差的大小来.今以二元函数为例,设 $z=f(x,y)$ 在点 $(x_{0},y_{0})$ 的某一邻域内连续且有 $(n+1)$ 阶连续偏导数, $(x_{0}+h,y_{0}+k)$ 为此邻域内任一点,我们的问题就是要把函数 $f(x_{0}+h,y_{0}+k)$ 近似地表达为 $h=x-x_{0},k=y-y_{0}$ 的n次多项式,而由此所产生的误差是当 $\rho=\sqrt{h^{2}+k^{2}}\rightarrow0$ 时比 $\rho^{n}$ 高阶的无穷小.为了解决这个问题,就要把一元函数的泰勒中值定理推广到多元函数的情形.

定理 设 $z = f(x, y)$ 在点 $(x_0, y_0)$ 的某一邻域内连续且有 $(n + 1)$ 阶连续偏导数，

$(x_0 + h, y_0 + k)$ 为此邻域内任一点，则有

$$
\begin{array}{l} f \left(x _ {0} + h, y _ {0} + k\right) = f \left(x _ {0}, y _ {0}\right) + \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) f \left(x _ {0}, y _ {0}\right) + \\ \frac {1}{2 !} \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {2} f \left(x _ {0}, y _ {0}\right) + \dots + \frac {1}{n !} \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {n} f \left(x _ {0}, y _ {0}\right) + \\ \frac {1}{(n + 1) !} \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {n + 1} f \left(x _ {0} + \theta h, y _ {0} + \theta k\right) (0 <   \theta <   1). \\ \end{array}
$$

其中记号

$\left(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\right)f(x_{0},y_{0})$ 表示 $hf_{x}(x_{0},y_{0})+kf_{y}(x_{0},y_{0})$ 

$\left(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\right)^{2}f(x_{0},y_{0})$ 表示 $h^{2}f_{xx}(x_{0},y_{0})+2hkf_{xy}(x_{0},y_{0})+k^{2}f_{yy}(x_{0},y_{0})$ 

一般地,记号

$\left(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\right)^{m}f(x_{0},y_{0})$ 表示 $\sum_{p=0}^{m}C_{m}^{p}h^{p}k^{m-p}\frac{\partial^{m}f}{\partial x^{p}\partial y^{m-p}}\bigg|_{(x_{0},y_{0})}.$ 

证 为了利用一元函数的泰勒公式来进行证明,我们引入函数

$$
\Phi (t) = f \left(x _ {0} + h t, y _ {0} + k t\right) \quad (0 \leqslant t \leqslant 1).
$$

显然 $\Phi(0) = f(x_0, y_0), \Phi(1) = f(x_0 + h, y_0 + k)$ . 由 $\Phi(t)$ 的定义及多元复合函数的求导法则, 可得

$$
\Phi^ {\prime} (t) = h f _ {x} \left(x _ {0} + h t, y _ {0} + k t\right) + k f _ {y} \left(x _ {0} + h t, y _ {0} + k t\right) = \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) f \left(x _ {0} + h t, y _ {0} + k t\right),
$$

$$
\begin{array}{l} \Phi^ {\prime \prime} (t) = h ^ {2} f _ {x x} \left(x _ {0} + h t, y _ {0} + k t\right) + 2 h k f _ {x y} \left(x _ {0} + h t, y _ {0} + k t\right) + k ^ {2} f _ {y y} \left(x _ {0} + h t, y _ {0} + k t\right) \\ = \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {2} f \left(x _ {0} + h t, y _ {0} + k t\right), \\ \end{array}
$$

... 

$$
\Phi^ {(n + 1)} (t) = \sum_ {p = 0} ^ {n + 1} C _ {n + 1} ^ {p} h ^ {p} k ^ {n + 1 - p} \frac {\partial^ {n + 1} f}{\partial x ^ {p} \partial y ^ {n + 1 - p}} \Bigg | _ {(x _ {0} + h t, y _ {0} + k t)} = \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {n + 1} f (x _ {0} + h t, y _ {0} + k t).
$$

利用一元函数的麦克劳林公式, 得

$$
\Phi (1) = \Phi (0) + \Phi^ {\prime} (0) + \frac {1}{2 !} \Phi^ {\prime \prime} (0) + \dots + \frac {1}{n !} \Phi^ {(n)} (0) + \frac {1}{(n + 1) !} \Phi^ {(n + 1)} (\theta), \quad (0 <   \theta <   1).
$$

将 $\Phi(0) = f(x_0, y_0), \Phi(1) = f(x_0 + h, y_0 + k)$ 及上面求得的 $\Phi(t)$ 直到 $n$ 阶导数在 $t = 0$ 的值，以及 $\Phi^{(n+1)}(t)$ 在 $t = \theta$ 的值代入上式，即得

$$
f \left(x _ {0} + h, y _ {0} + k\right) = f \left(x _ {0}, y _ {0}\right) + \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) f \left(x _ {0}, y _ {0}\right) + \frac {1}{2 !} \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {2} f \left(x _ {0}, y _ {0}\right) + \dots +
$$

$$
\frac {1}{n !} \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {n} f \left(x _ {0}, y _ {0}\right) + R _ {n}, \tag {9-1}
$$

其中

$$
R _ {n} = \frac {1}{(n + 1) !} \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {n + 1} f \left(x _ {0} + \theta h, y _ {0} + \theta k\right) \quad (0 <   \theta <   1). \tag {9-2}
$$

定理证毕.

公式(9-1)称为二元函数 $f(x,y)$ 在点 $(x_{0},y_{0})$ 的n阶泰勒公式,而 $R_{n}$ 的表达式(9-2)称为拉格朗日余项.

由二元函数的泰勒公式可知，以(9-1)式右端 $h$ 及 $k$ 的 $n$ 次多项式近似表达函数 $f(x_0 + h, y_0 + k)$ 时，其误差为 $\left|R_n\right|$ . 由假设，函数的各 $(n + 1)$ 阶偏导数都连续，故它们的绝对值在点 $(x_0, y_0)$ 的某一邻域内都不超过某一正常数 $M$ . 于是，有下面的误差估计式：

$$
\begin{array}{l} \left| R _ {n} \right| \leqslant \frac {M}{(n + 1) !} (\left| h \right| + \left| k \right|) ^ {n + 1} = \frac {M}{(n + 1) !} \rho^ {n + 1} \left(\frac {| h |}{\rho} + \frac {| k |}{\rho}\right) ^ {n + 1} \\ \leqslant \frac {M}{(n + 1) !} (\sqrt {2}) ^ {n + 1} \rho^ {n + 1} ①, \tag {9-3} \\ \end{array}
$$

其中 $\rho=\sqrt{h^{2}+k^{2}}$ .

由(9-3)式可知,误差 $\left|R_{n}\right|$ 是当 $\rho\rightarrow0$ 时比 $\rho^{n}$ 高阶的无穷小.

当 n=0 时, 公式(9-1)成为

$$
\begin{array}{l} f \left(x _ {0} + h, y _ {0} + k\right) \\ = f \left(x _ {0}, y _ {0}\right) + h f _ {x} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) + k f _ {y} \left(x _ {0} + \theta h, y _ {0} + \theta k\right). \tag {9-4} \\ \end{array}
$$

公式(9-4)称为二元函数的拉格朗日中值公式.由(9-4)式即可推得下述结论：

推论 如果函数 $f(x, y)$ 的偏导数 $f_x(x, y), f_y(x, y)$ 在某一区域内都恒等于零，那么函数 $f(x, y)$ 在该区域内为一常数.

例 求函数 $f(x,y) = \ln (1 + x + y)$ 在点(0,0)的三阶泰勒公式.

解 因为

$$
f _ {x} (x, y) = f _ {y} (x, y) = \frac {1}{1 + x + y},
$$

$$
f _ {x x} (x, y) = f _ {x y} (x, y) = f _ {y y} (x, y) = - \frac {1}{(1 + x + y) ^ {2}},
$$

$$
\frac {\partial^ {3} f}{\partial x ^ {p} \partial y ^ {3 - p}} = \frac {2 !}{(1 + x + y) ^ {3}} \quad (p = 0, 1, 2, 3),
$$

① 令 $\frac{|h|}{\rho} = \cos \alpha, \frac{|k|}{\rho} = \sin \alpha$ ，则 $\cos \alpha + \sin \alpha = \sqrt{2} \sin \left( \alpha + \frac{\pi}{4} \right) \leqslant \sqrt{2}$ .

$$
\frac {\partial^ {4} f}{\partial x ^ {p} \partial y ^ {4 - p}} = - \frac {3 !}{(1 + x + y) ^ {4}} \quad (p = 0, 1, 2, 3, 4),
$$

所以

$$
\begin{array}{l} \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) f (0, 0) = h f _ {x} (0, 0) + k f _ {y} (0, 0) = h + k, \\ \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {2} f (0, 0) = h ^ {2} f _ {x x} (0, 0) + 2 h k f _ {x y} (0, 0) + k ^ {2} f _ {y y} (0, 0) = - (h + k) ^ {2}, \\ \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {3} f (0, 0) = h ^ {3} f _ {x x x} (0, 0) + 3 h ^ {2} k f _ {x x y} (0, 0) + 3 h k ^ {2} f _ {x y y} (0, 0) + k ^ {3} f _ {y y y} (0, 0) = 2 (h + k) ^ {3}. \\ \end{array}
$$

又 $f(0,0)=0$ ，并将h=x，k=y代入，由三阶泰勒公式便得

$$
\ln (1 + x + y) = x + y - \frac {1}{2} (x + y) ^ {2} + \frac {1}{3} (x + y) ^ {3} + R _ {3},
$$

其中

$$
R _ {3} = \frac {1}{4 !} \left[ \left(h \frac {\partial}{\partial x} + k \frac {\partial}{\partial y}\right) ^ {4} f (\theta h, \theta k) \right] _ {h = x, k = y} = - \frac {1}{4} \cdot \frac {(x + y) ^ {4}}{(1 + \theta x + \theta y) ^ {4}} (0 <   \theta <   1).
$$

# 二、极值充分条件的证明

下面来证明第八节中的定理 2.

设函数 $z = f(x,y)$ 在点 $P_0(x_0,y_0)$ 的某邻域 $U_{1}(P_{0})$ 内连续且有一阶及二阶连续偏导数，又 $f_{x}(x_{0},y_{0}) = 0,f_{y}(x_{0},y_{0}) = 0.$ 

依二元函数的泰勒公式,对于任一 $(x_{0}+h,y_{0}+k)\in U_{1}(P_{0})$ 有

$$
\begin{array}{l} \Delta f = f \left(x _ {0} + h, y _ {0} + k\right) - f \left(x _ {0}, y _ {0}\right) \\ = \frac {1}{2} \left[ h ^ {2} f _ {x x} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) + 2 h k f _ {x y} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) + k ^ {2} f _ {y y} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) \right] (0 <   \theta <   1). \tag {9-5} \\ \end{array}
$$

(1) 设 $AC-B^{2}>0$ , 即

$$
f _ {x x} \left(x _ {0}, y _ {0}\right) f _ {y y} \left(x _ {0}, y _ {0}\right) - \left[ f _ {x y} \left(x _ {0}, y _ {0}\right) \right] ^ {2} > 0. \tag {9-6}
$$

因 $f(x,y)$ 的二阶偏导数在 $U_{1}(P_{0})$ 内连续，由不等式(9-6)可知，存在点 $P_{0}$ 的邻域 $U_{2}(P_{0})\subset U_{1}(P_{0})$ ，使得对任一 $(x_0 + h,y_0 + k)\in U_2(P_0)$ 有

$$
f _ {x x} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) f _ {y y} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) - \left[ f _ {x y} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) \right] ^ {2} > 0. \tag {9-7}
$$

为书写简便起见，把 $f_{xx}(x,y), f_{xy}(x,y), f_{yy}(x,y)$ 在点 $(x_0 + \theta h, y_0 + \theta k)$ 处的值依次记为 $f_{xx}, f_{xy}, f_{yy}$ . 由(9-7)式可知，当 $(x_0 + h, y_0 + k) \in U_2(P_0)$ 时， $f_{xx}$ 及 $f_{yy}$ 都不等于零且两者同号. 于是(9-5)式可写成

$$
\Delta f = \frac {1}{2 f _ {x x}} \left[ \left(h f _ {x x} + k f _ {x y}\right) ^ {2} + k ^ {2} \left(f _ {x x} f _ {y y} - f _ {x y} ^ {2}\right) \right].
$$

当 $h, k$ 不同时为零且 $(x_0 + h, y_0 + k) \in U_2(P_0)$ 时，上式右端方括号内的值为正，所以 $\Delta f$ 异于零且与 $f_{xx}$ 同号。又由 $f(x, y)$ 的二阶偏导数的连续性知 $f_{xx}$ 与 $A$ 同号，因此 $\Delta f$ 与 $A$ 同号。所以，当 $A > 0$ 时 $f(x_0, y_0)$ 为极小值，当 $A < 0$ 时 $f(x_0, y_0)$ 为极大值。

(2) 设 $AC - B^{2} < 0$ , 即

$$
f _ {x x} \left(x _ {0}, y _ {0}\right) f _ {y y} \left(x _ {0}, y _ {0}\right) - \left[ f _ {x y} \left(x _ {0}, y _ {0}\right) \right] ^ {2} <   0. \tag {9-8}
$$

先假定 $f_{xx}(x_0, y_0) = f_{yy}(x_0, y_0) = 0$ ，于是由(9-8)式可知这时 $f_{xy}(x_0, y_0) \neq 0$ . 现在分别令 $k = h$ 及 $k = -h$ ，则由(9-5)式分别得

$$
\Delta f = \frac {h ^ {2}}{2} \left[ f _ {x x} (x _ {0} + \theta_ {1} h, y _ {0} + \theta_ {1} h) + 2 f _ {x y} (x _ {0} + \theta_ {1} h, y _ {0} + \theta_ {1} h) + f _ {y y} (x _ {0} + \theta_ {1} h, y _ {0} + \theta_ {1} h) \right]
$$

及

$$
\Delta f = \frac {h ^ {2}}{2} \left[ f _ {x x} \left(x _ {0} + \theta_ {2} h, y _ {0} - \theta_ {2} h\right) - 2 f _ {x y} \left(x _ {0} + \theta_ {2} h, y _ {0} - \theta_ {2} h\right) + f _ {y y} \left(x _ {0} + \theta_ {2} h, y _ {0} - \theta_ {2} h\right) \right],
$$

其中 $0 < \theta_{1}, \theta_{2} < 1$ . 当 $h \to 0$ 时, 以上两式中右端方括号内的式子分别趋于极限

$$
2 f _ {x y} (x _ {0}, y _ {0}) \quad \text {及} \quad - 2 f _ {x y} (x _ {0}, y _ {0}),
$$

从而当 h 充分接近零时,两式中方括号内的值有相反的符号,因此 $\Delta f$ 可取不同符号的值,所以 $f(x_{0},y_{0})$ 不是极值.

再证 $f_{xx}(x_0,y_0)$ 和 $f_{yy}(x_0,y_0)$ 不同时为零的情形.不妨假定 $f_{xx}(x_0,y_0)\neq 0.$ 先取 $k = 0$ ，于是由(9-5)式得

$$
\Delta f = \frac {1}{2} h ^ {2} f _ {x x} (x _ {0} + \theta h, y _ {0}).
$$

由此看出, 当 h 充分接近零时, $\Delta f$ 与 $f_{xx}(x_{0}, y_{0})$ 同号.

但如果取

$$
h = - f _ {x y} \left(x _ {0}, y _ {0}\right) s, \quad k = f _ {x x} \left(x _ {0}, y _ {0}\right) s, \tag {9-9}
$$

其中 s 是异于零但充分接近零的数, 则可发现, 当 $\left| s \right|$ 充分小时, $\Delta f$ 与 $f_{xx}(x_0, y_0)$ 异号. 事实上, 在 (9-5) 式中将 h 及 k 用 (9-9) 式给定的值代入, 得

$$
\Delta f = \frac {1}{2} s ^ {2} \left\{\left[ f _ {x y} \left(x _ {0}, y _ {0}\right) \right] ^ {2} f _ {x x} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) - 2 f _ {x y} \left(x _ {0}, y _ {0}\right) f _ {x x} \left(x _ {0}, y _ {0}\right) f _ {x y} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) + \right.
$$

$$
\left[ f _ {x x} \left(x _ {0}, y _ {0}\right) \right] ^ {2} f _ {y y} \left(x _ {0} + \theta h, y _ {0} + \theta k\right) \}. \tag {9-10}
$$

上式右端花括号内的式子当 $s \to 0$ 时趋于极限

$$
f _ {x x} \left(x _ {0}, y _ {0}\right) \left\{f _ {x x} \left(x _ {0}, y _ {0}\right) f _ {y y} \left(x _ {0}, y _ {0}\right) - \left[ f _ {x y} \left(x _ {0}, y _ {0}\right) \right] ^ {2} \right\}.
$$

由不等式(9-8)，上式花括号内的值为负，因此当 $s$ 充分接近零时，(9-10)式右端（从而 $\Delta f$ )与 $f_{xx}(x_0,y_0)$ 异号.

以上已经证得:在点 $(x_{0},y_{0})$ 的任意邻近, $\Delta f$ 可取不同符号的值,因此 $f(x_{0},y_{0})$ 不是极值.

# (3) 考察函数

$$
f (x, y) = x ^ {2} + y ^ {4} \quad {\text {及}} \quad g (x, y) = x ^ {2} + y ^ {3}.
$$

容易验证, 这两个函数都以 $(0,0)$ 为驻点, 且在点 $(0,0)$ 处都满足 $AC-B^{2}=0$ . 但 $f(x,y)$ 在点 $(0,0)$ 处有极小值, 而 $g(x,y)$ 在点 $(0,0)$ 处却没有极值.

# *习题9-9

1. 求函数 $f(x,y)=2x^{2}-xy-y^{2}-6x-3y+5$ 在点 $(1,-2)$ 的泰勒公式.

2. 求函数 $f(x,y)=\mathrm{e}^{x}\ln(1+y)$ 在点 $(0,0)$ 的三阶泰勒公式.

3. 求函数 $f(x, y) = \sin x \sin y$ 在点 $\left( \frac{\pi}{4}, \frac{\pi}{4} \right)$ 的二阶泰勒公式.

4. 利用函数 $f(x,y)=x^{y}$ 的三阶泰勒公式, 计算 1.1 $^{1.02}$ 的近似值.

5. 求函数 $f(x,y)=\mathrm{e}^{x+y}$ 在点 $(0,0)$ 的 n 阶泰勒公式.

# * 第十节 最小二乘法

许多工程问题,常常需要根据两个变量的几组实验数值——实验数据,来找出这两个变量间的函数关系的近似表达式.通常把这样得到的函数的近似表达式叫做经验公式.经验公式建立以后,就可以把生产或实验中所积累的某些经验,提高到理论上加以分析.下面通过举例介绍常用的一种建立经验公式的方法.

例 1 为了测定刀具的磨损速度,我们做这样的实验:经过一定时间(如每隔1 h),测量一次刀具的厚度,得到一组实验数据如下:

<table><tr><td>顺序编号i</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>时间ti/h</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>刀具厚度yi/mm</td><td>27.0</td><td>26.8</td><td>26.5</td><td>26.3</td><td>26.1</td><td>25.7</td><td>25.3</td><td>24.8</td></tr></table>

试根据上面的实验数据建立 y 和 t 之间的经验公式 $y=f(t)$ . 也就是, 要找出一个能使上述数据大体适合的函数关系 $y=f(t)$ .

解 首先,要确定 $f(t)$ 的类型.为此,可按下面的方法处理.在直角坐标系中取t为横坐标,y为纵坐标,描出上述各对数据的对应点,如图9-12所示.从图上可以看出,这些点的连线大致接近于一条直线.于是,就可以认为 $y=f(t)$ 是线性函数,并设

$$
f (t) = a t + b,
$$

其中 a 和 b 是待定常数.

常数 a 和 b 如何确定呢？最理想的情形是选取这样的 a 和 b，能使直线 $y = at + b$ 经过图 9-12 中所标出的各点。但在实际上这是不可能的。因为这些点本来就不在同一条直线上。因此，只能要求选取这样的 a, b，使得 $f(t) = at + b$ 在 $t_{0}, t_{1}, t_{2}, \cdots, t_{7}$ 处的函数值与实验数据 $y_{0}, y_{1}, y_{2}, \cdots, y_{7}$ 相差都很小，就是要使偏差

$$
y _ {i} - f (t _ {i}) \quad (i = 0, 1, 2, \dots , 7)
$$

都很小.那么如何达到这一要求呢？能否设法使偏差的和

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a4f1b56f060d71e5ef7adf3cca850ca71c43f09d51ea6a587adba38410f97f1e.jpg)



图9-12


$$
\sum_ {i = 0} ^ {7} \left[ y _ {i} - f (t _ {i}) \right]
$$

很小来保证每个偏差都很小呢？不能，因为偏差有正有负，在求和时，可能互相抵消。为了避免这种情形，可对偏差取绝对值再求和，只要

$$
\sum_ {i = 0} ^ {7} \mid y _ {i} - f (t _ {i}) \mid = \sum_ {i = 0} ^ {7} \mid y _ {i} - (a t _ {i} + b) \mid
$$

很小, 就可以保证每个偏差的绝对值都很小. 但是这个式子中有绝对值符号, 不便于进一步分析讨论. 由于任何实数的平方都是正数或零, 因此可以考虑选取常数 $a$ 与 $b$ , 使

$$
M = \sum_ {i = 0} ^ {7} \left[ y _ {i} - (a t _ {i} + b) \right] ^ {2}
$$

最小来保证每个偏差的绝对值都很小.这种根据偏差的平方和为最小的条件来选择常数 $a$ 与 $b$ 的方法叫做最小二乘法.这种确定常数 $a$ 与 $b$ 的方法是通常所采用的.

现在我们来研究,经验公式 $y=at+b$ 中,a 和 b 符合什么条件时,可以使上述的 M 为最小.如果把 M 看成与自变量 a 和 b 相对应的因变量,那么问题就可归结为求函数 $M=M(a,b)$ 在哪些点处取得最小值.由第八节中的讨论可知,上述问题可以通过求方程组

$$
\left\{ \begin{array}{l} M _ {a} (a, b) = 0, \\ M _ {b} (a, b) = 0 \end{array} \right.
$$

的解来解决,即令

$$
\left\{ \begin{array}{l} \frac {\partial M}{\partial a} = - 2 \sum_ {i = 0} ^ {7} [ y _ {i} - (a t _ {i} + b) ] t _ {i} = 0, \\ \frac {\partial M}{\partial b} = - 2 \sum_ {i = 0} ^ {7} [ y _ {i} - (a t _ {i} + b) ] = 0, \end{array} \right.
$$

亦即

$$
\left\{ \begin{array}{l} \sum_ {i = 0} ^ {7} t _ {i} [ y _ {i} - (a t _ {i} + b) ] = 0, \\ \sum_ {i = 0} ^ {7} [ y _ {i} - (a t _ {i} + b) ] = 0. \end{array} \right.
$$

将括号内各项进行整理合并,并把未知数 a 和 b 分离出来,便得

$$
\left\{ \begin{array}{l} a \sum_ {i = 0} ^ {7} t _ {i} ^ {2} + b \sum_ {i = 0} ^ {7} t _ {i} = \sum_ {i = 0} ^ {7} y _ {i} t _ {i}, \\ a \sum_ {i = 0} ^ {7} t _ {i} + 8 b = \sum_ {i = 0} ^ {7} y _ {i}. \end{array} \right. \tag {10-1}
$$

下面通过列表来计算 $\sum_{i=0}^{7} t_i, \sum_{i=0}^{7} t_i^2, \sum_{i=0}^{7} y_i$ 及 $\sum_{i=0}^{7} y_i t_i$ .

<table><tr><td></td><td><eq>t_i</eq></td><td><eq>t_i^2</eq></td><td><eq>y_i</eq></td><td><eq>y_i t_i</eq></td></tr><tr><td rowspan="8"></td><td>0</td><td>0</td><td>27.0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>26.8</td><td>26.8</td></tr><tr><td>2</td><td>4</td><td>26.5</td><td>53.0</td></tr><tr><td>3</td><td>9</td><td>26.3</td><td>78.9</td></tr><tr><td>4</td><td>16</td><td>26.1</td><td>104.4</td></tr><tr><td>5</td><td>25</td><td>25.7</td><td>128.5</td></tr><tr><td>6</td><td>36</td><td>25.3</td><td>151.8</td></tr><tr><td>7</td><td>49</td><td>24.8</td><td>173.6</td></tr><tr><td>合计</td><td>28</td><td>140</td><td>208.5</td><td>717.0</td></tr></table>

代入方程组(10-1)，得到

$$
\left\{ \begin{array}{l} 1 4 0 a + 2 8 b = 7 1 7, \\ 2 8 a + 8 b = 2 0 8. 5. \end{array} \right.
$$

解此方程组,得到 a=-0.3036,b=27.125.这样便得到所求经验公式为

$$
y = f (t) = - 0. 3 0 3 6 t + 2 7. 1 2 5. \tag {10-2}
$$

由(10-2)式算出的函数值 $f(t_{i})$ 与实测的 $y_{i}$ 有一定的偏差.现列表比较如下：

<table><tr><td>ti/h</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>实测的yi/mm</td><td>27.0</td><td>26.8</td><td>26.5</td><td>26.3</td><td>26.1</td><td>25.7</td><td>25.3</td><td>24.8</td></tr><tr><td>算得的f(ti)/mm</td><td>27.125</td><td>26.821</td><td>26.518</td><td>26.214</td><td>25.911</td><td>25.607</td><td>25.303</td><td>25.000</td></tr><tr><td>偏差/mm</td><td>-0.125</td><td>-0.021</td><td>-0.018</td><td>0.086</td><td>0.189</td><td>0.093</td><td>-0.003</td><td>-0.200</td></tr></table>

偏差的平方和 M=0.108165, 它的算术平方根 $\sqrt{M}=0.329$ . $\sqrt{M}$ 称为均方误差, 它的大小在一定程度上反映了用经验公式来近似表达原来函数关系的近似程度的好坏.

在例 1 中, 按实验数据描出的图形接近于一条直线. 在这种情形下, 就可认为函数关系是线性函数类型的, 从而问题可化为求解一个二元一次方程组, 计算比较方便. 还有一些实际问题, 经验公式的类型不是线性函数, 但可以设法把它化成线性函数的类型来讨论. 举例说明于下:

例 2 在研究某单分子化学反应速度时,得到下列数据:

<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td><eq>\tau_i</eq></td><td>3</td><td>6</td><td>9</td><td>12</td><td>15</td><td>18</td><td>21</td><td>24</td></tr><tr><td><eq>y_i</eq></td><td>57.6</td><td>41.9</td><td>31.0</td><td>22.7</td><td>16.6</td><td>12.2</td><td>8.9</td><td>6.5</td></tr></table>

其中 $\tau$ 表示从实验开始算起的时间, y 表示时刻 $\tau$ 反应物的量. 试根据上述数据定出经验公式 $y = f(\tau)$ .

解 由化学反应速度的理论知道, $y=f(\tau)$ 应是指数函数 $y=ke^{m\tau}$ ,其中k和m是待定常数.对这批数据,先来验证这个结论.为此,在 $y=ke^{m\tau}$ 的两端取常用对数,得

$$
\lg y = (m \lg e) \tau + \lg k.
$$

记 $m\lg e$ 即 $0.4343m = a, \lg k = b$ ，则上式可写为

$$
\lg y = a \tau + b,
$$

于是 $\lg y$ 就是 $\tau$ 的线性函数. 所以, 把表中各对数据 $(\tau_i, y_i) (i = 1, 2, \dots, 8)$ 所对应的点描在半对数坐标系上 (半对数坐标系的横轴上各点处所标明的数字与普通的直角坐标系相同, 而纵轴上各点处所标明的数字是这样的, 它的常用对数就是该点到原点的距离), 如图9-13所示. 从图上看出, 这些点的连线非常接近于一条直线, 这说明 $y = f(\tau)$ 确实可以认为是指数函数.

下面来具体定出 $k$ 与 $m$ 的值.由于

$$
\lg y = a \tau + b,
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/27b776ed1e68f0ec9e31176109f54645adc5d7469a8d848c5c041c24097d8273.jpg)



图9-13


所以可仿照例 1 中的讨论,通过求方程组

$$
\left\{ \begin{array}{l} a \sum_ {i = 1} ^ {8} \tau_ {i} ^ {2} + b \sum_ {i = 1} ^ {8} \tau_ {i} = \sum_ {i = 1} ^ {8} \tau_ {i} \lg y _ {i}, \\ a \sum_ {i = 1} ^ {8} \tau_ {i} + 8 b = \sum_ {i = 1} ^ {8} \lg y _ {i} \end{array} \right. \tag {10-3}
$$

的解, 把 a 与 b 确定出来.

下面通过列表来计算 $\sum_{i=1}^{8}\tau_i, \sum_{i=1}^{8}\tau_i^2, \sum_{i=1}^{8}\lg y_i$ 及 $\sum_{i=1}^{8}\tau_i\lg y_i$ .

<table><tr><td></td><td><eq>\tau_i</eq></td><td><eq>\tau_i^2</eq></td><td><eq>y_i</eq></td><td><eq>lg y_i</eq></td><td><eq>\tau_i lg y_i</eq></td></tr><tr><td rowspan="8"></td><td>3</td><td>9</td><td>57.6</td><td>1.760 4</td><td>5.281 2</td></tr><tr><td>6</td><td>36</td><td>41.9</td><td>1.622 2</td><td>9.733 2</td></tr><tr><td>9</td><td>81</td><td>31.0</td><td>1.491 4</td><td>13.422 6</td></tr><tr><td>12</td><td>144</td><td>22.7</td><td>1.356 0</td><td>16.272 0</td></tr><tr><td>15</td><td>225</td><td>16.6</td><td>1.220 1</td><td>18.301 5</td></tr><tr><td>18</td><td>324</td><td>12.2</td><td>1.086 4</td><td>19.555 2</td></tr><tr><td>21</td><td>441</td><td>8.9</td><td>0.949 4</td><td>19.937 4</td></tr><tr><td>24</td><td>576</td><td>6.5</td><td>0.812 9</td><td>19.509 6</td></tr><tr><td>合计</td><td>108</td><td>1 836</td><td></td><td>10.298 8</td><td>122.012 7</td></tr></table>

将它们代入方程组(10-3) $\left(\text{其中取}\sum_{i=1}^{8}\lg y_{i}=10.3,\sum_{i=1}^{8}\tau_{i}\lg y_{i}=122\right)$ ，得

$$
\left\{ \begin{array}{l} 1 8 3 6 a + 1 0 8 b = 1 2 2, \\ 1 0 8 a + 8 b = 1 0. 3. \end{array} \right.
$$

解这个方程组,得

$$
\left\{ \begin{array}{l} a = 0. 4 3 4 3 m = - 0. 0 4 5, \\ b = \lg k = 1. 8 9 6 4, \end{array} \right.
$$

所以

$$
m = - 0. 1 0 3 6, \quad k = 7 8. 7 8.
$$

因此所求的经验公式为

$$
y = 7 8. 7 8 \mathrm{e} ^ {- 0. 1 0 3 6 \tau}.
$$

# * 习题9-10

1. 某种合金的含铅量百分比(%)为p,其熔解温度(℃)为θ,由实验测得p与θ的数据如下表:

<table><tr><td>p/%</td><td>36.9</td><td>46.7</td><td>63.7</td><td>77.8</td><td>84.0</td><td>87.5</td></tr><tr><td>θ/°C</td><td>181</td><td>197</td><td>235</td><td>270</td><td>283</td><td>292</td></tr></table>

试用最小二乘法建立 $\theta$ 与 p 之间的经验公式 $\theta = ap + b$ .

2. 已知一组实验数据为 $(x_{1},y_{1}),(x_{2},y_{2}),\cdots,(x_{n},y_{n})$ . 现若假定经验公式是

$$
y = a x ^ {2} + b x + c.
$$

试按最小二乘法建立 a, b, c 应满足的三元一次方程组.

# 总习题九

1. 在“充分”“必要”和“充分必要”三者中选择一个正确的填入下列空格内：

(1) $f(x, y)$ 在点 $(x, y)$ 可微分是 $f(x, y)$ 在该点连续的 ____ 条件, $f(x, y)$ 在点 $(x, y)$ 连续是 $f(x, y)$ 在该点可微分的 ____ 条件;

(2) $z = f(x, y)$ 在点 $(x, y)$ 的偏导数 $\frac{\partial z}{\partial x}$ 及 $\frac{\partial z}{\partial y}$ 存在是 $f(x, y)$ 在该点可微分的 ____ 条件, $z = f(x, y)$ 在点 $(x, y)$ 可微分是函数在该点的偏导数 $\frac{\partial z}{\partial x}$ 及 $\frac{\partial z}{\partial y}$ 存在的 ____ 条件;

(3) $z = f(x, y)$ 的偏导数 $\frac{\partial z}{\partial x}$ 及 $\frac{\partial z}{\partial y}$ 在点 $(x, y)$ 存在且连续是 $f(x, y)$ 在该点可微分的 ____ 条件；

（4）函数 $z=f(x,y)$ 的两个二阶混合偏导数 $\frac{\partial^{2}z}{\partial x\partial y}$ 及 $\frac{\partial^{2}z}{\partial y\partial x}$ 在区域 D 内连续是这两个二阶混合偏导数在 D 内相等的 ____ 条件.

2. 下题中给出了四个结论,从中选出一个正确的结论:

设函数 $f(x,y)$ 在点(0,0)的某邻域内有定义，且 $f_{x}(0,0)=3,f_{y}(0,0)=-1$ ，则有().

(A) $\mathrm{d}z\mid_{(0,0)}=3\mathrm{d}x-\mathrm{d}y$ 

(B) 曲面 $z = f(x, y)$ 在点 $(0, 0, f(0, 0))$ 的一个法向量为 $(3, -1, 1)$ 

(C) 曲线 $\left\{\begin{aligned}z=f(x,y),\\ y=0\end{aligned}\right.$ 在点 $(0,0,f(0,0))$ 的一个切向量为 $(1,0,3)$ 

(D) 曲线 $\left\{\begin{aligned}z=f(x,y),\\ y=0\end{aligned}\right.$ 在点 $(0,0,f(0,0))$ 的一个切向量为 $(3,0,1)$ 

3. 求函数 $f(x, y) = \frac{\sqrt{4x - y^2}}{\ln(1 - x^2 - y^2)}$ 的定义域，并求 $\lim_{(x, y) \to \left(\frac{1}{2}, 0\right)} f(x, y)$ .

*4. 证明极限 $\lim_{(x,y)\to (0,0)}\frac{xy^2}{x^2 + y^4}$ 不存在.

5. 设 $f(x, y) = \begin{cases} \frac{x^2y}{x^2 + y^2}, & x^2 + y^2 \neq 0, \\ 0, & x^2 + y^2 = 0. \end{cases}$ 求 $f_x(x, y)$ 及 $f_y(x, y)$ .

6. 求下列函数的一阶和二阶偏导数：

(1) $z = \ln (x + y^2)$ ; (2) $z = x^{y}$ . 

7. 求函数 $z = \frac{xy}{x^2 - y^2}$ 当 $x = 2, y = 1, \Delta x = 0.01, \Delta y = 0.03$ 时的全增量和全微分.

*8. 设 $f(x, y) = \begin{cases} \frac{x^2 y^2}{(x^2 + y^2)^{3/2}}, & x^2 + y^2 \neq 0, \\ 0, & x^2 + y^2 = 0. \end{cases}$ 证明： $f(x, y)$ 在点(0,0)处连续且偏导数存在，但不可微分.

9. 设 $u = x^y$ ，而 $x = \varphi(t), y = \psi(t)$ 都是可微函数，求 $\frac{\mathrm{d}u}{\mathrm{d}t}$ .

10. 设 $z=f(u,v,w)$ 具有连续偏导数, 而

$$
u = \eta - \zeta , \quad v = \zeta - \xi , \quad w = \xi - \eta ,
$$

求 $\frac{\partial z}{\partial\xi},\frac{\partial z}{\partial\eta},\frac{\partial z}{\partial\zeta}.$ 

11. 设 $z = f(u, x, y), u = x \mathrm{e}^{y}$ , 其中 $f$ 具有连续的二阶偏导数, 求 $\frac{\partial^2 z}{\partial x \partial y}$ .

12. 设 $x = \mathrm{e}^{u}\cos v, y = \mathrm{e}^{u}\sin v, z = uv$ . 试求 $\frac{\partial z}{\partial x}$ 和 $\frac{\partial z}{\partial y}$ .

13. 求螺旋线 $x=a\cos\theta, y=a\sin\theta, z=b\theta$ 在点 $(a,0,0)$ 处的切线及法平面方程.

14. 在曲面 $z = xy$ 上求一点, 使这点处的法线垂直于平面 $x + 3y + z + 9 = 0$ , 并写出该法线的方程.

15. 设 $e_{l}=(\cos\theta,\sin\theta)$ ，求函数

$$
f (x, y) = x ^ {2} - x y + y ^ {2}
$$

在点(1,1)沿方向 l 的方向导数,并分别确定角 $\theta$ ,使这个方向导数

(1)有最大值;(2)有最小值;(3)等于0.

16. 求函数 $u = x^{2} + y^{2} + z^{2}$ 在椭球面 $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} + \frac{z^{2}}{c^{2}} = 1$ 上点 $M_{0}(x_{0}, y_{0}, z_{0})$ 处沿外法线方向的方向导数.

17. 求平面 $\frac{x}{3} + \frac{y}{4} + \frac{z}{5} = 1$ 和柱面 $x^{2} + y^{2} = 1$ 的交线上与 $xOy$ 面距离最短的点.

18. 在第 I 卦限内作椭球面 $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} + \frac{z^{2}}{c^{2}} = 1$ 的切平面, 使该切平面与三坐标面所围成的四面体的体积最小. 求这切平面的切点, 并求此最小体积.

19. 某厂家生产的一种产品同时在两个市场销售, 售价分别为 $p_{1}$ 和 $p_{2}$ , 销售量分别为 $q_{1}$ 和 $q_{2}$ , 需求函数分别为

$$
q _ {1} = 2 4 - 0. 2 p _ {1}, \quad q _ {2} = 1 0 - 0. 0 5 p _ {2},
$$

总成本函数为

$$
C = 3 5 + 4 0 \left(q _ {1} + q _ {2}\right).
$$

试问:厂家如何确定两个市场的售价,能使其获得的总利润最大,最大总利润为多少?

20. 设有一小山, 取它的底面所在的平面为 $xOy$ 坐标面, 其底部所占的闭区域为 $D = \{(x, y) | x^2 + y^2 - xy \leqslant 75\}$ , 小山的高度函数为 $h = f(x, y) = 75 - x^2 - y^2 + xy$ .

（1）设 $M(x_0,y_0)\in D$ ，问 $f(x,y)$ 在该点沿平面上什么方向的方向导数最大，若记此方向导数的最大值为 $g(x_0,y_0)$ ，试写出 $g(x_0,y_0)$ 的表达式；

（2）现欲利用此小山开展攀岩活动，为此需要在山脚找一上山坡度最大的点作为攀岩的起点.也就是说，要在 $D$ 的边界线 $x^{2} + y^{2} - xy = 75$ 上找出(1)中的 $g(x,y)$ 达到最大值的点.试确定攀岩起点的位置.

# 第十章

# 重积分

本章和下一章是多元函数积分学的内容.在一元函数积分学中我们知道,定积分是某种确定形式的和的极限.这种和的极限的概念推广到定义在区域、曲线及曲面上的多元函数的情形,便得到重积分、曲线积分及曲面积分的概念.本章将介绍重积分(包括二重积分和三重积分)的概念、计算方法以及它们的一些应用.

# 第一节 二重积分的概念与性质

# 一、二重积分的概念

# 1. 曲顶柱体的体积

设有一立体,它的底是 $xOy$ 面上的闭区域 $D①$ , 它的侧面是以 $D$ 的边界曲线为准线而母线平行于 z 轴的柱面, 它的顶是曲面 $z=f(x,y)$ , 这里 $f(x,y) \geqslant 0$ 且在 D 上连续(图 10-1). 这种立体叫做曲顶柱体. 现在我们来讨论如何定义并计算上述曲顶柱体的体积 V.

我们知道,平顶柱体的高是不变的,它的体积可以用公式

$$
\mathrm{体积} = \mathrm{高} \times \mathrm{底面积}
$$

来定义和计算.关于曲顶柱体,当点 $(x,y)$ 在区域D上变动时,高度 $f(x,y)$ 是个变量,因此它的体积不能直接用上式来定义和计算.但如果回忆起第五章中求曲边梯形面积的问题,就不难想到,那里所采用的解决办法,原则上可以用来解决目前的问题.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/227581282f281df3a6dbe773b5b68e00ad1aa276f5ff0ec31f8f4c8913c0df77.jpg)



图10-1


首先,用一组曲线网把 D 分成 n 个小闭区域

$$
\Delta \sigma_ {1}, \Delta \sigma_ {2}, \dots , \Delta \sigma_ {n}.
$$

分别以这些小闭区域的边界曲线为准线,作母线平行于 z 轴的柱面,这些柱面把原来的曲顶柱体分为 n 个细曲顶柱体.当这些小闭区域的直径①很小时,由于 $f(x,y)$ 连续,对同一个小闭区域来说, $f(x,y)$ 变化很小,这时细曲顶柱体可近似看做平顶柱体.我们在每个 $\Delta \sigma_{i}$ （这个小闭区域的面积也记作 $\Delta \sigma_{i}$ ）中任取一点 $(\xi_{i},\eta_{i})$ ，以 $f(\xi_i,\eta_i)$ 为高而底为 $\Delta \sigma_{i}$ 的平顶柱体（图10-2）的体积为

$$
f (\xi_ {i}, \eta_ {i}) \Delta \sigma_ {i} (i = 1, 2, \dots , n).
$$

这 $n$ 个平顶柱体体积之和

$$
\sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}) \Delta \sigma_ {i}
$$

可以认为是整个曲顶柱体体积的近似值.令 $n$ 个小闭区域的直径中的最大值(记作 $\lambda$ ) 趋于零,取上述和的极限,所得的极限便自然地定义为所论曲顶柱体的体积 $V$ ,即

$$
V = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}) \Delta \sigma_ {i}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/04389517ef871fdd9ade9c383a43c071289536122462f06e78a1205a7a5f08c6.jpg)



图10-2


# 2. 平面薄片的质量

设有一平面薄片占有 $xOy$ 面上的闭区域 $D$ , 它在点 $(x, y)$ 处的面密度为 $\mu(x, y)$ , 这里 $\mu(x, y) > 0$ 且在 $D$ 上连续. 现在要计算该薄片的质量 $m$ .

我们知道,如果薄片是均匀的,即面密度是常数,那么薄片的质量可以用公式

$$
\mathrm{质量} = \mathrm{面密度} \times \mathrm{面积}
$$

来计算. 现在面密度 $\mu(x,y)$ 是变量, 薄片的质量就不能直接用上式来计算. 但是上面用来处理曲顶柱体体积问题的方法完全适用于本问题.

由于 $\mu (x,y)$ 连续，把薄片分成许多小块后，只要小块所占的小闭区域 $\Delta \sigma_{i}$ 的直径很小，这些小块就可以近似地看做均匀薄片.在 $\Delta \sigma_{i}$ 上任取一点 $(\xi_i,\eta_i)$ ，则

$$
\mu (\xi_ {i}, \eta_ {i}) \Delta \sigma_ {i} (i = 1, 2, \dots , n)
$$

可看做第 i 个小块的质量的近似值(图 10-3).通过求和、取极限,便得出

$$
m = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} \mu (\xi_ {i}, \eta_ {i}) \Delta \sigma_ {i}.
$$

上面两个问题的实际意义虽然不同,但所求量都归结为同一形式的和的极限.在物理、力学、几何和工程技术中,有许多物理量或几何量都可归结为这一形式的和的极限.因此我们要一般地研究这种和的极限,并抽象出下述二重积分的定义:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/af6ab6a7c0856d0e5bc77c2f293ec241463b190da2d93b65a6d399eda7d96b2a.jpg)



图10-3


定义 设 $f(x, y)$ 是有界闭区域 $D$ 上的有界函数. 将闭区域 $D$ 任意分成 $n$ 个小闭区域

$$
\Delta \sigma_ {1}, \Delta \sigma_ {2}, \dots , \Delta \sigma_ {n},
$$

其中 $\Delta\sigma_{i}$ 表示第 i 个小闭区域,也表示它的面积.在每个 $\Delta\sigma_{i}$ 上任取一点 $(\xi_{i},\eta_{i})$ ,作乘积 $f(\xi_{i},\eta_{i})\Delta\sigma_{i}\quad(i=1,2,\cdots,n)$ ,并作和 $\sum_{i=1}^{n}f(\xi_{i},\eta_{i})\Delta\sigma_{i}$ .如果当各小闭区域的直径中的最大值 $\lambda\to0$ 时,这和的极限总存在,且与闭区域 D 的分法及点 $(\xi_{i},\eta_{i})$ 的取法无关,那么称此极限为函数 $f(x,y)$ 在闭区域 D 上的二重积分,记作 $\iint_{D}f(x,y)\mathrm{d}\sigma$ ,即

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}) \Delta \sigma_ {i}. \tag {1-1}
$$

其中 $f(x,y)$ 叫做被积函数， $f(x,y)\mathrm{d}\sigma$ 叫做被积表达式， $\mathrm{d}\sigma$ 叫做面积元素， $x$ 与 $y$ 叫做积分变量， $D$ 叫做积分区域， $\sum_{i=1}^{n} f(\xi_i, \eta_i) \Delta \sigma_i$ 叫做积分和.

在二重积分的定义中对闭区域 $D$ 的划分是任意的, 如果在直角坐标系中用平行于坐标轴的直线网来划分 $D$ , 那么除了包含边界点的一些小闭区域外①, 其余的小闭区域都是矩形闭区域. 设矩形闭区域 $\Delta \sigma_{i}$ 的边长为 $\Delta x_{j}$ 和 $\Delta y_{k}$ , 则 $\Delta \sigma_{i} = \Delta x_{j} \cdot \Delta y_{k}$ . 因此在直角坐标系中, 有时也把面积元素 $\mathrm{d}\sigma$ 记作 $\mathrm{d}x\mathrm{d}y$ , 而把二重积分记作

$$
\iint_ {D} f (x, y) \mathrm{d} x \mathrm{d} y,
$$

其中 $dxdy$ 叫做直角坐标系中的面积元素.

这里我们要指出,当 $f(x,y)$ 在闭区域D上连续时,(1-1)式右端的和的极限必定存在,也就是说,函数 $f(x,y)$ 在D上的二重积分必定存在,即函数 $f(x,y)$ 在D上必定可积.以后我们总假定函数 $f(x,y)$ 在闭区域D上可积.

由二重积分的定义可知,曲顶柱体的体积是函数 $f(x,y)$ 在底D上的二重积分

$$
V = \iint_ {D} f (x, y) \mathrm{d} \sigma ,
$$

平面薄片的质量是它的面密度 $\mu (x,y)$ 在薄片所占闭区域 $D$ 上的二重积分

$$
m = \iint_ {D} \mu (x, y) \mathrm{d} \sigma .
$$

一般地, 如果 $f(x, y) \geqslant 0$ , 被积函数 $f(x, y)$ 可以解释为曲顶柱体的顶在点 $(x, y)$ 处的竖坐标, 所以二重积分的几何意义就是柱体的体积. 如果 $f(x, y)$ 是负的, 柱体就在 $xOy$ 面的下方, 二重积分的绝对值仍等于柱体的体积, 但二重积分的值是负的. 如果 $f(x, y)$ 在 $D$ 的若干部分区域上是正的, 而在其他的部分区域上是负的, 那么, $f(x, y)$ 在 $D$ 上的二重积分就等于 $xOy$ 面上方的柱体体积减去 $xOy$ 面下方的柱体体积所得之差.

# 二、二重积分的性质

比较定积分与二重积分的定义可以想到,二重积分与定积分有类似的性质,现叙述于下:

性质1 设 $\alpha$ 与 $\beta$ 为常数, 则

$$
\iint_ {D} [ \alpha f (x, y) + \beta g (x, y) ] \mathrm{d} \sigma = \alpha \iint_ {D} f (x, y) \mathrm{d} \sigma + \beta \iint_ {D} g (x, y) \mathrm{d} \sigma .
$$

性质2 如果闭区域 $D$ 被有限条曲线分为有限个部分闭区域, 那么在 $D$ 上的二重积分等于在各部分闭区域上的二重积分的和.

例如 $D$ 分为两个闭区域 $D_{1}$ 与 $D_{2}$ , 则

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma = \iint_ {D _ {1}} f (x, y) \mathrm{d} \sigma + \iint_ {D _ {2}} f (x, y) \mathrm{d} \sigma .
$$

这个性质表示二重积分对于积分区域具有可加性.

性质3 如果在 $D$ 上, $f(x,y) = 1, \sigma$ 为 $D$ 的面积, 那么

$$
\sigma = \iint_ {D} 1 \cdot \mathrm{d} \sigma = \iint_ {D} \mathrm{d} \sigma .
$$

这性质的几何意义是很明显的,因为高为1的平顶柱体的体积在数值上就等于柱体的底面积.

性质4 如果在 $D$ 上， $f(x, y) \leqslant g(x, y)$ ，那么有

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma \leqslant \iint_ {D} g (x, y) \mathrm{d} \sigma .
$$

特殊地,由于

$$
- | f (x, y) | \leqslant f (x, y) \leqslant | f (x, y) |,
$$

又有

$$
\left| \iint_ {D} f (x, y) \mathrm{d} \sigma \right| \leqslant \iint_ {D} | f (x, y) | \mathrm{d} \sigma .
$$

性质5 设 $M$ 和 $m$ 分别是 $f(x, y)$ 在闭区域 $D$ 上的最大值和最小值, $\sigma$ 是 $D$ 的面积, 则有

$$
m \sigma \leqslant \iint_ {D} f (x, y) \mathrm{d} \sigma \leqslant M \sigma .
$$

上述不等式是对于二重积分估值的不等式. 因为 $m \leqslant f(x, y) \leqslant M$ ，所以由性质 4 有

$$
\iint_ {D} m \mathrm{d} \sigma \leqslant \iint_ {D} f (x, y) \mathrm{d} \sigma \leqslant \iint_ {D} M \mathrm{d} \sigma ,
$$

再应用性质 1 和性质 3, 便得此估值不等式.

性质6(二重积分的中值定理) 设函数 $f(x, y)$ 在闭区域 $D$ 上连续, $\sigma$ 是 $D$ 的面积, 则在 $D$ 上至少存在一点 $(\xi, \eta)$ , 使得

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma = f (\xi , \eta) \sigma .
$$

证 显然 $\sigma \neq 0$ . 把性质5中不等式各除以 $\sigma$ , 有

$$
m \leqslant \frac {1}{\sigma} \iint_ {D} f (x, y) \mathrm{d} \sigma \leqslant M.
$$

这就是说,确定的数值 $\frac{1}{\sigma}\iint_{D}f(x,y)\mathrm{d}\sigma$ 是介于函数 $f(x,y)$ 的最大值M与最小值m之间的.根据在闭区域上连续函数的介值定理,在D上至少存在一点 $(\xi,\eta)$ ,使得函数在该点的值与这个确定的数值相等,即

$$
\frac {1}{\sigma} \iint_ {D} f (x, y) \mathrm{d} \sigma = f (\xi , \eta).
$$

上式两端各乘 $\sigma$ ，就得所需要证明的公式.

例1 估计二重积分 $I = \iint_{D} (x + y + 10) \, \mathrm{d}\sigma$ 的值，其中 $D = \{(x, y) | (x - 2)^2 + (y - 1)^2 \leqslant 2\}$ .

解 按照二重积分的性质 5, 估计二重积分的值, 关键是要确定被积函数 $f(x, y)$ 在积分区域 $D$ 上的最大值和最小值. 本例中, 被积函数 $f(x, y) = x + y + 10$ 的图形是一张平面. 容易知道, 它在 $D$ 上的最大值、最小值均在 $D$ 的边界上取得, 所以, 只需考虑它在 $D$ 的边界上的取值情形.

D 的边界曲线 L 的参数方程为

$$
\left\{ \begin{array}{l l} x = 2 + \sqrt {2} \cos t, \\ y = 1 + \sqrt {2} \sin t, \end{array} \right. \quad t \in [ 0, 2 \pi ].
$$

因此在 L 上, 有

$$
f (x, y) = \sqrt {2} (\cos t + \sin t) + 1 3 = 2 \sin \left(t + \frac {\pi}{4}\right) + 1 3,
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a1d5674fbd622810299a8158c9863322f4c9b7f29e7151bdf76fa07fa80ddec5.jpg)


例题精讲

10-1 

便得

$$
1 1 \leqslant f (x, y) \leqslant 1 5.
$$

区域 D 的面积 $\sigma=2\pi$ , 于是

$$
2 2 \pi \leqslant I \leqslant 3 0 \pi .
$$

例2 设 $f(x, y)$ 在闭区域 $D$ 上连续， $D$ 关于 $x$ 轴和 $y$ 轴均对称，记 $D_{1} = \{(x, y) | (x, y) \in D, x \geqslant 0, y \geqslant 0\}$ ，二重积分 $I = \iint_{D} f(x, y) \mathrm{d}\sigma = 4 \iint_{D_{1}} f(x, y) \mathrm{d}\sigma$ 成立的条件是下列条件中的哪一个？

(1) $f(x, y)$ 关于 $x$ 是奇函数, 关于 $y$ 是偶函数, 即

$$
f (- x, y) = - f (x, y), \quad f (x, - y) = f (x, y), \quad (x, y) \in D;
$$

(2) $f(-x,y)=f(x,y),f(x,-y)=f(x,y),(x,y)\in D;$ 

(3) $f(-x,y)=f(x,y),f(x,-y)=-f(x,y),(x,y)\in D;$ 

(4) $f(-x,y) = -f(x,y), f(x, -y) = -f(x,y), (x,y) \in D.$ 

解（2）中的函数 $f(x,y)$ 关于 $x$ 、关于 $y$ 均是偶函数，而积分区域 $D$ 关于 $y$ 轴、 $x$ 轴均对称，由二重积分对于积分区域的可加性和几何意义，可知题中给出的积分等式成立，其余三种条件下，积分等式均不成立。例如条件(1)和(4)， $f(x,y)$ 关于 $x$ 是奇函数，而积分区域 $D$ 关于 $y$ 轴对称，即知 $I = 0$ ；同理，条件(3)， $f(x,y)$ 关于 $y$ 是奇函数，而积分区域 $D$ 关于 $x$ 轴对称，即知 $I = 0$ 。

# 习题10-1

1. 设有一平面薄板(不计其厚度)占有 xOy 面上的闭区域 D，薄板上分布有面密度为 $\mu=\mu(x,y)$ 的电荷，且 $\mu(x,y)$ 在 D 上连续，试用二重积分表达该薄板上的全部电荷 Q.

2. 设 $I_{1} = \iint_{D_{1}} (x^{2} + y^{2})^{3} \mathrm{d}\sigma$ ，其中 $D_{1} = \{(x, y) | -1 \leqslant x \leqslant 1, -2 \leqslant y \leqslant 2\}$ ；又 $I_{2} = \iint_{D_{2}} (x^{2} + y^{2})^{3} \mathrm{d}\sigma$ ，其中 $D_{2} = \{(x, y) | 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant 2\}$ . 试利用二重积分的几何意义说明 $I_{1}$ 与 $I_{2}$ 之间的关系.

3. 利用二重积分定义证明：

(1) $\iint_{D} \mathrm{d}\sigma = \sigma$ (其中 $\sigma$ 为 $D$ 的面积);

(2) $\iint_{D} kf(x, y) \mathrm{d}\sigma = k \iint_{D} f(x, y) \mathrm{d}\sigma$ （其中 $k$ 为常数）；

(3) $\iint_{D} f(x, y) \mathrm{d}\sigma = \iint_{D_1} f(x, y) \mathrm{d}\sigma + \iint_{D_2} f(x, y) \mathrm{d}\sigma$ ，其中 $D = D_1 \cup D_2, D_1, D_2$ 为两个无公共内点的闭区域.

4. 试确定积分区域 D, 使二重积分 $\iint_{D}(1-2x^{2}-y^{2})\mathrm{d}x\mathrm{d}y$ 达到最大值.

5. 根据二重积分的性质, 比较下列积分的大小:

(1) $\iint_{D} (x + y)^2 \mathrm{d}\sigma$ 与 $\iint_{D} (x + y)^3 \mathrm{d}\sigma$ ，其中积分区域 $D$ 是由 $x$ 轴、 $y$ 轴与直线 $x + y = 1$ 所围成；

(2) $\iint_{D} (x + y)^{2} \mathrm{d}\sigma$ 与 $\iint_{D} (x + y)^{3} \mathrm{d}\sigma$ ，其中积分区域 $D$ 是由圆周 $(x - 2)^{2} + (y - 1)^{2} = 2$ 所围成；

(3) $\iint_{D} \ln(x + y) \, \mathrm{d}\sigma$ 与 $\iint_{D} [\ln(x + y)]^2 \, \mathrm{d}\sigma$ , 其中 $D$ 是三角形闭区域, 三顶点分别为 $(1,0), (1,1), (2,0)$ ;

(4) $\iint_{D} \ln(x + y) \, \mathrm{d}\sigma$ 与 $\iint_{D} [\ln(x + y)]^2 \, \mathrm{d}\sigma$ , 其中 $D = \{(x, y) | 3 \leqslant x \leqslant 5, 0 \leqslant y \leqslant 1\}$ .

6. 计算 $\iint_{D} (2 + y \cos x + x y \sin y) \, \mathrm{d}\sigma$ ，其中 $D = \{(x, y) | x^2 + y^2 \leqslant 1\}$ .

7. 利用二重积分的性质估计下列积分的值:

(1) $I = \iint_{D} xy(x + y) \, \mathrm{d}\sigma$ ，其中 $D = \{(x, y) \mid 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1\}$ ;

(2) $I = \iint_{D} \sin^{2} x \sin^{2} y \, \mathrm{d}\sigma$ ，其中 $D = \{(x, y) | 0 \leqslant x \leqslant \pi, 0 \leqslant y \leqslant \pi\}$ ;

(3) $I = \iint_{D} (x + y + 1) \, \mathrm{d}\sigma$ ，其中 $D = \{(x, y) \mid 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant 2\}$ ;

(4) $I = \iint_{D} (x^{2} + 4y^{2} + 9) \, \mathrm{d}\sigma$ ，其中 $D = \{(x, y) | x^{2} + y^{2} \leqslant 4\}$ .

# 第二节 二重积分的计算法

按照二重积分的定义来计算二重积分,对少数特别简单的被积函数和积分区域来说是可行的,但对一般的函数和区域来说,这不是一种切实可行的方法.本节介绍一种计算二重积分的方法,这种方法是把二重积分化为两次定积分来计算.

# 一、利用直角坐标计算二重积分

下面用几何观点来讨论二重积分 $\iint_{D} f(x, y) \mathrm{d}\sigma$ 的计算问题. 在讨论中我们假定 $f(x, y) \geqslant 0$ .

设积分区域 $D$ 可以用不等式

$$
\varphi_ {1} (x) \leqslant y \leqslant \varphi_ {2} (x), \quad a \leqslant x \leqslant b
$$

来表示(图 10-4)，其中函数 $\varphi_{1}(x)$ ， $\varphi_{2}(x)$ 在区间 $[a,b]$ 上连续.

按照二重积分的几何意义,二重积分 $\iint_{D}f(x,y)\mathrm{d}\sigma$ 的值等于以 D 为底,曲面 $z=f(x,y)$ 为顶的曲顶柱体(图 10-5)的体积.下面我们应用第六章中计算“平行截面面积为已知的立体的体积”的方法来计算这个曲顶柱体的体积.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/fcef878f019aba9d3a80fdd7fdc3b2c0e94b41c756479ec07eda947a3aac1606.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a4cbc804c869ac2b3b5f38d8e553e9482d9bb980f2860f22943a16d395437302.jpg)



图10-4


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/684e946fad6290349b6af734685b68f0f970decca3cfa7f4a8200382d2faffb8.jpg)



图10-5


先计算截面面积.为此,在区间 $[a,b]$ 上任意取定一点 $x_{0}$ ,作平行于yOz面的平面 $x=x_{0}$ .这平面截曲顶柱体所得的截面是一个以区间 $\left[\varphi_{1}(x_{0}),\varphi_{2}(x_{0})\right]$ 为底、曲线 $z=f(x_{0},y)$ 为曲边的曲边梯形(图10-5中阴影部分),所以这截面的面积为

$$
A (x _ {0}) = \int_ {\varphi_ {1} (x _ {0})} ^ {\varphi_ {2} (x _ {0})} f (x _ {0}, y) \mathrm{d} y.
$$

一般地, 过区间 $[a, b]$ 上任一点 x 且平行于 yOz 面的平面截曲顶柱体所得截面的面积为

$$
A (x) = \int_ {\varphi_ {1} (x)} ^ {\varphi_ {2} (x)} f (x, y) \mathrm{d} y.
$$

于是,应用计算平行截面面积为已知的立体体积的方法,得曲顶柱体体积为

$$
V = \int_ {a} ^ {b} A (x) \mathrm{d} x = \int_ {a} ^ {b} \left[ \int_ {\varphi_ {1} (x)} ^ {\varphi_ {2} (x)} f (x, y) \mathrm{d} y \right] \mathrm{d} x.
$$

这个体积也就是所求二重积分的值,从而有等式

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma = \int_ {a} ^ {b} \left[ \int_ {\varphi_ {1} (x)} ^ {\varphi_ {2} (x)} f (x, y) \mathrm{d} y \right] \mathrm{d} x. \tag {2-1}
$$

上式右端的积分叫做先对 y、后对 x 的二次积分. 就是说, 先把 x 看做常数, 把 $f(x, y)$ 只看做 y 的函数, 并对 y 计算从 $\varphi_{1}(x)$ 到 $\varphi_{2}(x)$ 的定积分; 然后把算得的结果 (是 x 的函数) 再对 x 计算在区间 $[a, b]$ 上的定积分. 这个先对 y、后对 x 的二次积分也常记作

$$
\int_ {a} ^ {b} \mathrm{d} x \int_ {\varphi_ {1} (x)} ^ {\varphi_ {2} (x)} f (x, y) \mathrm{d} y.
$$

因此,等式(2-1)也写成

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma = \int_ {a} ^ {b} \mathrm{d} x \int_ {\varphi_ {1} (x)} ^ {\varphi_ {2} (x)} f (x, y) \mathrm{d} y, \tag {$2-1^{\prime$}}
$$

这就是把二重积分化为先对 y、后对 x 的二次积分的公式.

在上述讨论中,我们假定 $f(x,y)\geqslant0$ ,但实际上公式(2-1)的成立并不受此条件限制.

类似地,如果积分区域 D 可以用不等式

$$
\psi_ {1} (y) \leqslant x \leqslant \psi_ {2} (y), \quad c \leqslant y \leqslant d
$$

来表示(图 10-6)，其中函数 $\psi_{1}(y)$ ， $\psi_{2}(y)$ 在区间 $[c,d]$ 上连续，那么就有

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma = \int_ {c} ^ {d} \left[ \int_ {\psi_ {1} (y)} ^ {\psi_ {2} (y)} f (x, y) \mathrm{d} x \right] \mathrm{d} y. \tag {2-2}
$$

上式右端的积分叫做先对 $x$ 、后对 $y$ 的二次积分，这个积分也常记作

$$
\int_ {c} ^ {d} \mathrm{d} y \int_ {\psi_ {1} (y)} ^ {\psi_ {2} (y)} f (x, y) \mathrm{d} x.
$$

因此,等式(2-2)也写成

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma = \int_ {c} ^ {d} \mathrm{d} y \int_ {\psi_ {1} (y)} ^ {\psi_ {2} (y)} f (x, y) \mathrm{d} x, \tag {$2-2^{\prime$}}
$$

这就是把二重积分化为先对 x、后对 y 的二次积分的公式.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/fd4a597142aeeca41a4eb5c35256a830e4767d7f8c8990688d1d9b4ef812144f.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/b158ec713ecf364207859c6533e58f5e4566a3b3385db2b8678367d25776cf69.jpg)



(b)



图10-6


以后我们称图 10-4 所示的积分区域为 X 型区域, 图 10-6 所示的积分区域为 Y 型区域. 应用公式(2-1)时, 积分区域必须是 X 型区域, X 型区域 D 的特点是: 穿过 D 内部且平行于 y 轴的直线与 D 的边界相交不多于两点; 而用公式(2-2)时, 积分区域必须是 Y 型区域, Y 型区域 D 的特点是: 穿过 D 内部且平行于 x 轴的直线与 D 的边界相交不多于两点. 如果积分区域 D 如图 10-7 那样, 既有一部分使穿过 D 内部且平行于 y 轴的直线与 D 的边界相交多于两点, 又有一部分使穿过 D 内部且平行于 x 轴的直线与 D 的边界相交多于两点, 那么 D 既不是 X 型区域, 又不是 Y 型区域. 对于这种情形, 可以把 D 分成几部分, 使每个部分是 X 型区域或是 Y 型区域. 例如, 在图 10-7 中, 把 D 分成三部分, 它们都是 X 型区域, 从而在这三部分上的二重积分都可应用公式(2-1). 各部分上的二重积分求得后, 根据二重积分的性质 2, 它们的和就是在 D 上的二重积分.

如果积分区域 $D$ 既是 $X$ 型的, 可用不等式 $\varphi_{1}(x) \leqslant y \leqslant \varphi_{2}(x), a \leqslant x \leqslant b$ 表示, 又是 $Y$ 型的, 可用不等式 $\psi_{1}(y) \leqslant x \leqslant \psi_{2}(y), c \leqslant y \leqslant d$ 表示 (图10-8), 那么由公式(2-1')及(2-2')就得

$$
\int_ {a} ^ {b} \mathrm{d} x \int_ {\varphi_ {1} (x)} ^ {\varphi_ {2} (x)} f (x, y) \mathrm{d} y = \int_ {c} ^ {d} \mathrm{d} y \int_ {\psi_ {1} (y)} ^ {\psi_ {2} (y)} f (x, y) \mathrm{d} x. \tag {2-3}
$$

上式表明,这两个不同次序的二次积分相等,因为它们都等于同一个二重积分

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma .
$$

将二重积分化为二次积分时, 确定积分限是一个关键. 积分限是根据积分区域 D 来确定的, 先画出积分区域 D 的图形. 假如积分区域 D 是 X 型的, 如图10-9所示, 在区间 $[a, b]$ 上任意取定一个 x 值, 积分区域上以这个 x 值为横坐标的点在一段直线上, 这段直线平行于 y 轴, 该线段上点的纵坐标从 $\varphi_{1}(x)$ 变到 $\varphi_{2}(x)$ , 这就是公式 (2-1) 中先把 x 看做常量而对 y 积分时的下限和上限. 因为上面的 x 值是在 $[a, b]$ 上任意取定的, 所以再把 x 看做变量而对 x 积分时, 积分区间就是 $[a, b]$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/547b86435a95f8903198aff0ab1262263e27dc53ae45e679632b95d6910e3a28.jpg)



图10-7


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/6d27a30d915f79983610b1bafc2a18b7bda5daafd9882d600509d60eca4280f9.jpg)



图10-8


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/3c64cb00b8d5512fce2a8a94a114a889d052bd0d87f439a6803fc4a39416878d.jpg)



图10-9


例 1 计算 $\iint_{D} xy \, d\sigma$ ，其中 D 是由直线 y = 1, x = 2 及 y = x 所围成的闭区域.

解法一 首先画出积分区域 $D$ （图10-10). $D$ 是 $X$ 型的， $D$ 上的点的横坐标的变动范围是区间[1,2].在区间[1,2]上任意取定一个 $x$ 值，则 $D$ 上以这个 $x$ 值为横坐标的点在一段直线上，这段直线平行于 $y$ 轴，该线段上点的纵坐标从 $y = 1$ 变到 $y = x$ . 利用公式(2-1)得

$$
\iint_ {D} x y \mathrm{d} \sigma = \int_ {1} ^ {2} \left[ \int_ {1} ^ {x} x y \mathrm{d} y \right] \mathrm{d} x = \int_ {1} ^ {2} \left[ x \cdot \frac {y ^ {2}}{2} \right] _ {1} ^ {x} \mathrm{d} x = \int_ {1} ^ {2} \left(\frac {x ^ {3}}{2} - \frac {x}{2}\right) \mathrm{d} x = \left[ \frac {x ^ {4}}{8} - \frac {x ^ {2}}{4} \right] _ {1} ^ {2} = \frac {9}{8}.
$$

解法二 如图10-11, 积分区域 $D$ 是 $Y$ 型的, $D$ 上的点的纵坐标的变动范围是区间[1,2]. 在区间[1,2]上任意取定一个 $y$ 值, 则 $D$ 上以这个 $y$ 值为纵坐标的点在一段直线上, 这段直线平行于 $x$ 轴, 该线段上点的横坐标从 $x = y$ 变到 $x = 2$ . 于是, 利用公式(2-2)得

$$
\iint_ {D} x y \mathrm{d} \sigma = \int_ {1} ^ {2} \left[ \int_ {y} ^ {2} x y \mathrm{d} x \right] \mathrm{d} y = \int_ {1} ^ {2} \left[ y \cdot \frac {x ^ {2}}{2} \right] _ {y} ^ {2} \mathrm{d} y = \int_ {1} ^ {2} \left(2 y - \frac {y ^ {3}}{2}\right) \mathrm{d} y = \left[ y ^ {2} - \frac {y ^ {4}}{8} \right] _ {1} ^ {2} = \frac {9}{8}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/0310e81fd44c890283c92d347e16e7193be6822e77d0fed3de4cc93e3f571554.jpg)



图10-10


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/8ccc5efa44829af52182539847cf81e7d6f53b4d619e01fcb84468abde4c68ef.jpg)



图10-11


例2 计算 $\iint_{D} y\sqrt{1 + x^2 - y^2} \, \mathrm{d}\sigma$ ，其中 $D$ 是由直线 $y = x, x = -1$ 和 $y = 1$ 所围成的闭区域.

解 画出积分区域 D 如图 10-12 所示. D 既是 X 型的, 又是 Y 型的. 若利用公式 (2-1), 得

$$
\begin{array}{l} \iint_ {D} y \sqrt {1 + x ^ {2} - y ^ {2}} \mathrm{d} \sigma = \int_ {- 1} ^ {1} \left[ \int_ {x} ^ {1} y \sqrt {1 + x ^ {2} - y ^ {2}} \mathrm{d} y \right] \mathrm{d} x = - \frac {1}{3} \int_ {- 1} ^ {1} \left[ (1 + x ^ {2} - y ^ {2}) ^ {\frac {3}{2}} \right] _ {x} ^ {1} \mathrm{d} x \\ = - \frac {1}{3} \int_ {- 1} ^ {1} (| x | ^ {3} - 1) d x = - \frac {2}{3} \int_ {0} ^ {1} (x ^ {3} - 1) d x = \frac {1}{2}. \\ \end{array}
$$

若利用公式(2-2)(图 10-13),就有

$$
\iint_ {D} y \sqrt {1 + x ^ {2} - y ^ {2}} \mathrm{d} \sigma = \int_ {- 1} ^ {1} y \left[ \int_ {- 1} ^ {y} \sqrt {1 + x ^ {2} - y ^ {2}} \mathrm{d} x \right] \mathrm{d} y,
$$

其中关于 x 的积分计算比较麻烦.所以这里用公式(2-1)计算较为方便.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/81ec18bab8707564a0659d3c2a9c64c4bb240f950de6eba66742b08463e6ec60.jpg)



图10-12


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a6ff1876f809d81b012a0f112b3faa804dbf46ad0d4b5c76836a6f2ac51ff4fc.jpg)



图10-13


例3 计算 $\iint_{D} xy \, \mathrm{d}\sigma$ ，其中 $D$ 是由抛物线 $y^{2} = x$ 及直线 $y = x - 2$ 所围成的闭区域.

解 画出积分区域 D 如图 10-14 所示. D 既是 X 型的, 又是 Y 型的. 若利用公式 (2-2), 则得

$$
\iint_ {D} x y \mathrm{d} \sigma = \int_ {- 1} ^ {2} \left[ \int_ {y ^ {2}} ^ {y + 2} x y \mathrm{d} x \right] \mathrm{d} y = \int_ {- 1} ^ {2} \left[ \frac {x ^ {2}}{2} y \right] _ {y ^ {2}} ^ {y + 2} \mathrm{d} y = \frac {1}{2} \int_ {- 1} ^ {2} [ y (y + 2) ^ {2} - y ^ {5} ] \mathrm{d} y
$$

$$
= \frac {1}{2} \left[ \frac {y ^ {4}}{4} + \frac {4}{3} y ^ {3} + 2 y ^ {2} - \frac {y ^ {6}}{6} \right] _ {- 1} ^ {2} = \frac {4 5}{8}.
$$

若利用公式(2-1)来计算,则由于在区间[0,1]及[1,4]上表示 $\varphi_{1}(x)$ 的式子不同,所以要用经过交点(1,-1)且平行于 y 轴的直线 x=1 把区域 D 分成 $D_{1}$ 和 $D_{2}$ 两部分(图 10-15),其中

$$
D _ {1} = \{(x, y) | - \sqrt {x} \leqslant y \leqslant \sqrt {x}, 0 \leqslant x \leqslant 1 \}, D _ {2} = \{(x, y) | x - 2 \leqslant y \leqslant \sqrt {x}, 1 \leqslant x \leqslant 4 \}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/c6c5a24538e5369313b7224e255f56bf74e87babd174b851077be04159b9007c.jpg)



图10-14


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/975b50b84f3583c255cd6d9eb282e764015d265879a3979bb4949157583041d2.jpg)



图10-15


因此,根据二重积分的性质2,就有

$$
\iint_ {D} x y \mathrm{d} \sigma = \iint_ {D _ {1}} x y \mathrm{d} \sigma + \iint_ {D _ {2}} x y \mathrm{d} \sigma = \int_ {0} ^ {1} \left[ \int_ {- \sqrt {x}} ^ {\sqrt {x}} x y \mathrm{d} y \right] \mathrm{d} x + \int_ {1} ^ {4} \left[ \int_ {x - 2} ^ {\sqrt {x}} x y \mathrm{d} y \right] \mathrm{d} x.
$$

由此可见,这里用公式(2-1)来计算需要化为两个二次积分.

上述几个例子说明,在化二重积分为二次积分时,为了计算简便,需要选择恰当的二次积分的次序.这时,既要考虑积分区域D的形状,
又要考虑被积函数 $f(x,y)$ 的特性.

例4 求两个底圆半径都等于 $R$ 的直交圆柱面所围成的立体的体积.

解 设这两个圆柱面的方程分别为

$$
x ^ {2} + y ^ {2} = R ^ {2} \quad {\text {及}} \quad x ^ {2} + z ^ {2} = R ^ {2}.
$$

利用立体关于坐标平面的对称性, 只要算出它在第 I 卦限部分(图 10-16(a)) 的体积 $V_{1}$ , 然后再乘 8 就行了.

所求立体在第Ⅰ卦限部分可以看成是一个曲顶柱体,它的底为

$$
D = \{(x, y) | 0 \leqslant y \leqslant \sqrt {R ^ {2} - x ^ {2}}, 0 \leqslant x \leqslant R \},
$$

如图 10-16(b) 所示. 它的顶是柱面 $z=\sqrt{R^{2}-x^{2}}$ . 于是,

$$
V _ {1} = \iint_ {D} \sqrt {R ^ {2} - x ^ {2}} \mathrm{d} \sigma .
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/5600b6fe4e86926bfc321c9bf77a0241aad33a891493173776f0056232fa58a3.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/5cf40a381715b69b365142957eafb99bb0840acf17956cee0c1a9d25b0bf5ecc.jpg)



(b)



图10-16


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/742b1a58a8c1f60897e047930edadd143d49b95b7543d89f4cf0a29ae882fb84.jpg)


利用公式(2-1)，得

$$
\begin{array}{l} V _ {1} = \iint_ {D} \sqrt {R ^ {2} - x ^ {2}} \mathrm{d} \sigma = \int_ {0} ^ {R} \left[ \int_ {0} ^ {\sqrt {R ^ {2} - x ^ {2}}} \sqrt {R ^ {2} - x ^ {2}} \mathrm{d} y \right] \mathrm{d} x \\ = \int_ {0} ^ {R} \left[ \sqrt {R ^ {2} - x ^ {2}} y \right] _ {0} ^ {\sqrt {R ^ {2} - x ^ {2}}} \mathrm{d} x = \int_ {0} ^ {R} \left(R ^ {2} - x ^ {2}\right) \mathrm{d} x = \frac {2}{3} R ^ {3}. \\ \end{array}
$$

从而所求立体的体积为

$$
V = 8 V _ {1} = \frac {1 6}{3} R ^ {3}.
$$

# 二、利用极坐标计算二重积分

有些二重积分,积分区域 D 的边界曲线用极坐标方程来表示比较方便,且被积函数用极坐标变量 $\rho, \theta$ 表达比较简单.这时,就可以考虑利用极坐标来计算二重积分 $\iint_{D} f(x, y) \, d\sigma$ .

按二重积分的定义

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}) \Delta \sigma_ {i},
$$

下面我们来研究这个和的极限在极坐标系中的形式.

假定从极点 O 出发且穿过闭区域 D 内部的射线与 D 的边界曲线相交不多于两点. 我们用以极点为中心的一族同心圆: $\rho =$ 常数以及从极点出发的一族射线: $\theta =$ 常数,把 D 分成 n 个小闭区域(图10-17).除了包含边界点的一些小闭区域外,小闭区域的面积 $\Delta\sigma_{i}$ 可计算如下:

$$
\begin{array}{l} \Delta \sigma_ {i} = \frac {1}{2} \left(\rho_ {i} + \Delta \rho_ {i}\right) ^ {2} \cdot \Delta \theta_ {i} - \frac {1}{2} \rho_ {i} ^ {2} \cdot \Delta \theta_ {i} \\ = \frac {1}{2} \left(2 \rho_ {i} + \Delta \rho_ {i}\right) \Delta \rho_ {i} \cdot \Delta \theta_ {i} \\ = \frac {\rho_ {i} + (\rho_ {i} + \Delta \rho_ {i})}{2} \cdot \Delta \rho_ {i} \cdot \Delta \theta_ {i} = \overline {{\rho}} _ {i} \cdot \Delta \rho_ {i} \cdot \Delta \theta_ {i}, \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/91d4c2fd0a0947d6e8271213f27370a3cca8faa919bb535c1a3b8b2e8a046fb3.jpg)



图10-17


其中 $\overline{\rho}_i$ 表示相邻两圆弧的半径的平均值. 在这小闭区域内取圆周 $\rho = \overline{\rho}_i$ 上的一点 $(\overline{\rho}_i, \overline{\theta}_i)$ , 设该点的直角坐标为 $(\xi_i, \eta_i)$ , 则由直角坐标与极坐标之间的关系有 $\xi_i = \overline{\rho}_i \cos \overline{\theta}_i$ , $\eta_i = \overline{\rho}_i \sin \overline{\theta}_i$ . 于是

$$
\lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}) \Delta \sigma_ {i} = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\bar {\rho} _ {i} \cos \bar {\theta} _ {i}, \bar {\rho} _ {i} \sin \bar {\theta} _ {i}) \bar {\rho} _ {i} \cdot \Delta \rho_ {i} \cdot \Delta \theta_ {i},
$$

即

$$
\iint_ {D} f (x, y) \mathrm{d} \sigma = \iint_ {D} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho \mathrm{d} \theta .
$$

这里我们把点 $(\rho, \theta)$ 看做是在同一平面上的点 $(x, y)$ 的极坐标表示，所以上式右端的积分区域仍然记作 $D$ 。因为在直角坐标系中 $\iint_{D} f(x, y) \mathrm{d}\sigma$ 也常记作 $\iint_{D} f(x, y) \mathrm{d}x \mathrm{d}y$ ，所以上式又可写成

$$
\iint_ {D} f (x, y) \mathrm{d} x \mathrm{d} y = \iint_ {D} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho \mathrm{d} \theta . \tag {2-4}
$$

这就是二重积分的变量从直角坐标变换为极坐标的变换公式,其中 $\rho d\rho d\theta$ 就是极坐标系中的面积元素.

公式(2-4)表明,要把二重积分中的变量从直角坐标变换为极坐标,只要把被积函数中的x与y分别换成 $\rho\cos\theta$ 与 $\rho\sin\theta$ ,并把直角坐标系中的面积元素dxdy换成极坐标系中的面积元素 $\rho d\rho d\theta$ .

极坐标系中的二重积分,同样可以化为二次积分来计算.

设积分区域 D 可以用不等式

$$
\varphi_ {1} (\theta) \leqslant \rho \leqslant \varphi_ {2} (\theta), \quad \alpha \leqslant \theta \leqslant \beta
$$

来表示(图 10-18)，其中函数 $\varphi_{1}(\theta)$ ， $\varphi_{2}(\theta)$ 在区间 $[\alpha,\beta]$ 上连续.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/fe0bc0c018982cbcad47074320ecdb3223e7546394e62fae8790dc3d68d33506.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/ee0201138f6d5f8050e3619fed53b97fa7e12c444f4d665c125c38e6cc39da4b.jpg)



(b)



图10-18


先在区间 $[\alpha, \beta]$ 上任意取定一个 $\theta$ 值. 对应于这个 $\theta$ 值, $D$ 上的点 (图10-19中这些点在线段 $EF$ 上) 的极径 $\rho$ 从 $\varphi_{1}(\theta)$ 变到 $\varphi_{2}(\theta)$ . 又 $\theta$ 是在 $[\alpha, \beta]$ 上任意取定的, 所以 $\theta$ 的变化范围是区间 $[\alpha, \beta]$ . 这样就可看出, 极坐标系中的二重积分化为二次积分的公式为

$$
\iint_ {D} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho \mathrm{d} \theta = \int_ {\alpha} ^ {\beta} \left[ \int_ {\varphi_ {1} (\theta)} ^ {\varphi_ {2} (\theta)} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho \right] \mathrm{d} \theta . \tag {2-5}
$$

上式也写成

$$
\iint_ {D} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho \mathrm{d} \theta = \int_ {\alpha} ^ {\beta} \mathrm{d} \theta \int_ {\varphi_ {1} (\theta)} ^ {\varphi_ {2} (\theta)} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho . \tag {$2-5^{\prime$}}
$$

如果积分区域 $D$ 是图10-20所示的曲边扇形，那么可以把它看做图10-18(a)中当 $\varphi_{1}(\theta)\equiv 0,\varphi_{2}(\theta) = \varphi (\theta)$ 时的特例.这时闭区域 $D$ 可以用不等式

$$
0 \leqslant \rho \leqslant \varphi (\theta), \quad \alpha \leqslant \theta \leqslant \beta
$$

来表示,而公式 $(2-5')$ 成为

$$
\iint_ {D} f (\rho \cos \theta , \rho \sin \theta) \rho d \rho d \theta = \int_ {\alpha} ^ {\beta} d \theta \int_ {0} ^ {\varphi (\theta)} f (\rho \cos \theta , \rho \sin \theta) \rho d \rho .
$$

如果积分区域 D 如图 10-21 所示, 极点在 D 的内部, 那么可以把它看做图 10-20 中当 $\alpha=0$ 且 $\beta=2\pi$ 时的特例. 这时闭区域 D 可以用不等式

$$
0 \leqslant \rho \leqslant \varphi (\theta), \quad 0 \leqslant \theta \leqslant 2 \pi
$$

来表示,而公式 $(2-5')$ 成为

$$
\iint_ {D} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho \mathrm{d} \theta = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\varphi (\theta)} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho .
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/bb2b0beed29261e1ac22d1f5b9ccf007ceeb53026239ef7ff20990ef86919395.jpg)



图10-19


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/eedb847863e083321abd3200a6411a86c5e4680f64db6e06fcb0485dc7411715.jpg)



图10-20


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/70f220e546e2e91b65ff652081e9f463496df464e0179f5601d515823d4f44f9.jpg)



图10-21


由二重积分的性质3,闭区域D的面积 $\sigma$ 可以表示为

$$
\sigma = \iint_ {D} \mathrm{d} \sigma .
$$

在极坐标系中, 面积元素 $d\sigma = \rho d\rho d\theta$ , 上式成为

$$
\sigma = \iint_ {D} \rho \mathrm{d} \rho \mathrm{d} \theta .
$$

如果闭区域 D 如图 10-18(a) 所示, 那么由公式 $(2-5')$ 有

$$
\sigma = \iint_ {D} \rho \mathrm{d} \rho \mathrm{d} \theta = \int_ {\alpha} ^ {\beta} \mathrm{d} \theta \int_ {\varphi_ {1} (\theta)} ^ {\varphi_ {2} (\theta)} \rho \mathrm{d} \rho = \frac {1}{2} \int_ {\alpha} ^ {\beta} [ \varphi_ {2} ^ {2} (\theta) - \varphi_ {1} ^ {2} (\theta) ] \mathrm{d} \theta .
$$

特别地,如果闭区域 D 如图 10-20 所示,那么 $\varphi_{1}(\theta)=0,\varphi_{2}(\theta)=\varphi(\theta)$ .于是

$$
\sigma = \frac {1}{2} \int_ {\alpha} ^ {\beta} \varphi^ {2} (\theta) \mathrm{d} \theta .
$$

例5 计算 $\iint_{D} e^{-x^2 - y^2} \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $D$ 是由圆心在原点、半径为 $a$ 的圆周所围成的闭区域.

解 在极坐标系中,闭区域 D 可表示为

$$
0 \leqslant \rho \leqslant a, \quad 0 \leqslant \theta \leqslant 2 \pi .
$$

由公式(2-4)及(2-5)有

$$
\begin{array}{l} \iint_ {D} \mathrm{e} ^ {- x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y = \iint_ {D} \mathrm{e} ^ {- \rho^ {2}} \rho \mathrm{d} \rho \mathrm{d} \theta = \int_ {0} ^ {2 \pi} \left[ \int_ {0} ^ {a} \mathrm{e} ^ {- \rho^ {2}} \rho \mathrm{d} \rho \right] \mathrm{d} \theta \\ = \int_ {0} ^ {2 \pi} \left[ - \frac {1}{2} \mathrm{e} ^ {- \rho^ {2}} \right] _ {0} ^ {a} \mathrm{d} \theta = \frac {1}{2} (1 - \mathrm{e} ^ {- a ^ {2}}) \int_ {0} ^ {2 \pi} \mathrm{d} \theta = \pi (1 - \mathrm{e} ^ {- a ^ {2}}). \\ \end{array}
$$

本题如果用直角坐标计算,因为积分 $\int e^{-x^{2}} dx$ 不能用初等函数表示,所以算不出来.现在我们利用上面的结果来计算工程上常用的反常积分 $\int_{0}^{+\infty} e^{-x^{2}} dx$ .

设

$$
D _ {1} = \{(x, y) | x ^ {2} + y ^ {2} \leqslant R ^ {2}, x \geqslant 0, y \geqslant 0 \},
$$

$$
D _ {2} = \{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 2 R ^ {2}, x \geqslant 0, y \geqslant 0 \},
$$

$$
S = \{(x, y) | 0 \leqslant x \leqslant R, 0 \leqslant y \leqslant R \}.
$$

显然 $D_{1} \subset S \subset D_{2}$ (图10-22). 由于 $\mathrm{e}^{-x^2 - y^2} > 0$ ，从而在这些闭区域上的二重积分之间有不等式

$$
\iint_ {D _ {1}} \mathrm{e} ^ {- x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y <   \iint_ {S} \mathrm{e} ^ {- x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y <   \iint_ {D _ {2}} \mathrm{e} ^ {- x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/1d6fb6784329861058411dcfa82eecc16dd4e43d372dc1cab224090da410555a.jpg)



图10-22


因为

$$
\iint_ {S} \mathrm{e} ^ {- x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y = \int_ {0} ^ {R} \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x \cdot \int_ {0} ^ {R} \mathrm{e} ^ {- y ^ {2}} \mathrm{d} y = \left(\int_ {0} ^ {R} \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x\right) ^ {2},
$$

又应用上面已得的结果有

$$
\iint_ {D _ {1}} \mathrm{e} ^ {- x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y = \frac {\pi}{4} (1 - \mathrm{e} ^ {- R ^ {2}}), \quad \iint_ {D _ {2}} \mathrm{e} ^ {- x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y = \frac {\pi}{4} (1 - \mathrm{e} ^ {- 2 R ^ {2}}),
$$

于是上面的不等式可写成

$$
\frac {\pi}{4} (1 - \mathrm{e} ^ {- R ^ {2}}) <   \left(\int_ {0} ^ {R} \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x\right) ^ {2} <   \frac {\pi}{4} (1 - \mathrm{e} ^ {- 2 R ^ {2}}).
$$

令 $R \to +\infty$ ，上式两端趋于同一极限 $\frac{\pi}{4}$ ，从而

$$
\int_ {0} ^ {+ \infty} \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x = \frac {\sqrt {\pi}}{2}.
$$

例6 求球体 $x^{2} + y^{2} + z^{2}\leqslant 4a^{2}$ 被圆柱面 $x^{2} + y^{2} = 2ax$ （ $a > 0$ )所截得的（含在圆柱面内的部分）立体的体积(图10-23).

解 由对称性，

$$
V = 4 \iint_ {D} \sqrt {4 a ^ {2} - x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y,
$$

其中 D 为半圆周 $y=\sqrt{2ax-x^{2}}$ 及 x 轴所围成的闭区域. 在极坐标系中, 闭区域 D 可用不

等式

$$
0 \leqslant \rho \leqslant 2 a \cos \theta , \quad 0 \leqslant \theta \leqslant \frac {\pi}{2}
$$

来表示.于是

$$
\begin{array}{l} V = 4 \iint_ {D} \sqrt {4 a ^ {2} - \rho^ {2}} \rho \mathrm{d} \rho \mathrm{d} \theta = 4 \int_ {0} ^ {\frac {\pi}{2}} \mathrm{d} \theta \int_ {0} ^ {2 a \cos \theta} \sqrt {4 a ^ {2} - \rho^ {2}} \rho \mathrm{d} \rho \\ = \frac {3 2}{3} a ^ {3} \int_ {0} ^ {\frac {\pi}{2}} (1 - \sin^ {3} \theta) \mathrm{d} \theta = \frac {3 2}{3} a ^ {3} \left(\frac {\pi}{2} - \frac {2}{3}\right). \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/74d788076e0771a3432b3e44702cf839bfaffa7c0a2269cda0b7646bf1ef5528.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/9495376f3dc20fcb8d35f1656812c3d9ea507b9f37c06cc7e4f5e17769a2695e.jpg)



(b)



图10-23


# * 三、二重积分的换元法

上一目得到的二重积分的变量从直角坐标变换为极坐标的变换公式, 是二重积分换元法的一种特殊情形. 在那里, 我们把平面上同一个点 M, 既用直角坐标 $(x, y)$ 表示, 又用极坐标 $(\rho, \theta)$ 表示, 它们间的关系为

$$
\left\{ \begin{array}{l} x = \rho \cos \theta , \\ y = \rho \sin \theta . \end{array} \right. \tag {2-6}
$$

也就是说, 由(2-6)式联系的点 $(x, y)$ 和点 $(\rho, \theta)$ 看成是同一个平面上的同一个点, 只是采用不同的坐标罢了. 现在, 我们采用另一种观点来加以解释. 把(2-6)式看成是从直角坐标平面 $\rho O \theta$ 到直角坐标平面 $xOy$ 的一种变换, 即对于 $\rho O \theta$ 平面上的一点 $M'(\rho, \theta)$ , 通过变换(2-6), 变成 $xOy$ 平面上的一点 $M(x, y)$ . 在两个平面各自限定的某个范围内, 这种变换还是一对一的 (即是一一映射). 下面就采用这种观点来讨论二重积分换元法的一般情形.

定理 设 $f(x, y)$ 在 $xOy$ 平面上的闭区域 $D$ 上连续, 若变换

$$
T: x = x (u, v), y = y (u, v) \tag {2-7}
$$

将 $uOv$ 平面上的闭区域 $D'$ 变为 $xOy$ 平面上的 $D$ , 且满足

(1) $x(u, v), y(u, v)$ 在 $D'$ 上具有一阶连续偏导数；

(2) 在 $D'$ 上雅可比式 $J(u,v)=\frac{\partial(x,y)}{\partial(u,v)}\neq0;$ 

(3) 变换 $T: D' \rightarrow D$ 是一对一的，

则有

$$
\iint_ {D} f (x, y) \mathrm{d} x \mathrm{d} y = \iint_ {D ^ {\prime}} f [ x (u, v), y (u, v) ] | J (u, v) | \mathrm{d} u \mathrm{d} v. \tag {2-8}
$$

公式(2-8)称为二重积分的换元公式.

证 显然, 在定理的假设下, (2-8) 式两端的二重积分都存在. 由于二重积分与积分区域的分法无关, 我们用平行于坐标轴的直线网来分割 $D'$ , 使得除去包含边界点的小闭区域外, 其余的小闭区域都为边长是 $h$ 的正方形闭区域. 任取一个这样得到的正方形闭区域, 设其顶点为 $M_1'(u,v), M_2'(u+h,v), M_3'(u+h,v+h), M_4'(u,v+h)$ , 其面积为 $\Delta\sigma' = h^2$ (图 10-24(a)). 正方形闭区域 $M_1'M_2'M_3'M_4'$ 经变换 (2-7) 变成 $xOy$ 平面上的一个曲边四边形 $M_1M_2M_3M_4$ , 它的四个顶点的坐标是

$$
\begin{array}{l} M _ {1}: x _ {1} = x (u, v), y _ {1} = y (u, v); \\ M _ {2}: x _ {2} = x (u + h, v) = x (u, v) + x _ {u} (u, v) h + o (h), \\ \gamma_ {2} = \gamma (u + h, v) = \gamma (u, v) + \gamma_ {u} (u, v) h + o (h); \\ M _ {3}: x _ {3} = x (u + h, v + h) = x (u, v) + x _ {u} (u, v) h + x _ {v} (u, v) h + o (h), \\ \gamma_ {3} = \gamma (u + h, v + h) = \gamma (u, v) + \gamma_ {u} (u, v) h + \gamma_ {v} (u, v) h + o (h); \\ M _ {4}: x _ {4} = x (u, v + h) = x (u, v) + x _ {v} (u, v) h + o (h), \\ y _ {4} = y (u, v + h) = y (u, v) + y _ {v} (u, v) h + o (h), \\ \end{array}
$$

其面积为 $\Delta \sigma$ （图10-24(b)). 可以证明, 曲边四边形 $M_{1}M_{2}M_{3}M_{4}$ 的面积与直边四边形 $M_{1}M_{2}M_{3}M_{4}$ (四个顶点用直线相连) 的面积当 $h \to 0$ 时只相差高阶无穷小. 又由上面这些坐标表示式可知, 若不计高阶无穷小, 则有

$$
x _ {2} - x _ {1} = x _ {3} - x _ {4}, \quad y _ {2} - y _ {1} = y _ {3} - y _ {4}, \quad x _ {4} - x _ {1} = x _ {3} - x _ {2}, \quad y _ {4} - y _ {1} = y _ {3} - y _ {2},
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/4fdf39dbbc3e1fd80fc34401aabc707cefe5c7512082960fc518d7d7d3c7f348.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/67dabc0b778eae41a10e2118f47b8aa2a4a1b57bba71e5c3dc6a749c41a20960.jpg)



(b)



图10-24


这表示, 直边四边形 $M_{1} M_{2} M_{3} M_{4}$ 的对边的长度可看做两两相等. 因此, 若不计高阶无穷小, 曲边四边形 $M_{1} M_{2} M_{3} M_{4}$ 可看做平行四边形, 于是它的面积 $\Delta \sigma$ 近似等于 $\triangle M_{1} M_{2} M_{3}$ 的面积的 2 倍. 根据解析几何, $\triangle M_{1} M_{2} M_{3}$ 的面积的 2 倍等于行列式

$$
\left| \begin{array}{c c} x _ {2} - x _ {1} & x _ {3} - x _ {2} \\ y _ {2} - y _ {1} & y _ {3} - y _ {2} \end{array} \right|
$$

的绝对值,由于

$$
x _ {2} - x _ {1} = x _ {u} (u, v) h + o (h), \quad x _ {3} - x _ {2} = x _ {v} (u, v) h + o (h),
$$

$$
y _ {2} - y _ {1} = y _ {u} (u, v) h + o (h), \quad y _ {3} - y _ {2} = y _ {v} (u, v) h + o (h),
$$

因此上面的行列式与行列式

$$
\left| \begin{array}{l l} x _ {u} (u, v) h & x _ {v} (u, v) h \\ y _ {u} (u, v) h & y _ {v} (u, v) h \end{array} \right| = \left| \begin{array}{l l} x _ {u} (u, v) & x _ {v} (u, v) \\ y _ {u} (u, v) & y _ {v} (u, v) \end{array} \right| h ^ {2}
$$

只相差一个比 $h^2$ 高阶的无穷小.于是

$$
\Delta \sigma = \left| \frac {\partial (x , y)}{\partial (u , v)} \right| \Delta \sigma^ {\prime} + o (\Delta \sigma^ {\prime}) \quad (h \rightarrow 0).
$$

把 $f(x,y) = f[x(u,v),y(u,v)]$ 的两端分别与上式两端相乘，得

$$
f (x, y) \Delta \sigma = f [ x (u, v), y (u, v) ] \left| \frac {\partial (x , y)}{\partial (u , v)} \right| \Delta \sigma^ {\prime} + f [ x (u, v), y (u, v) ] \cdot o (\Delta \sigma^ {\prime}).
$$

上式对一切小正方形闭区域取和并令 $h \to 0$ 求极限, 由于上式右端第二项的和的极限为零, 于是得公式(2-8). 定理证毕.

这里我们指出,如果雅可比式 $J(u,v)$ 只在 $D'$ 内个别点上,或一条曲线上为零,而在其他点上不为零,那么换元公式(2-8)仍成立.

在变换为极坐标 $x=\rho\cos\theta, y=\rho\sin\theta$ 的特殊情形下, 雅可比式

$$
J = \left| \begin{array}{l l} \frac {\partial x}{\partial \rho} & \frac {\partial x}{\partial \theta} \\ \frac {\partial y}{\partial \rho} & \frac {\partial y}{\partial \theta} \end{array} \right| = \left| \begin{array}{l l} \cos \theta & - \rho \sin \theta \\ \sin \theta & \rho \cos \theta \end{array} \right| = \rho ,
$$

它仅在 $\rho = 0$ 处为零，故不论闭区域 $D'$ 是否含有极点，换元公式仍成立.即有

$$
\iint_ {D} f (x, y) \mathrm{d} x \mathrm{d} y = \iint_ {D ^ {\prime}} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho \mathrm{d} \theta ,
$$

这里 $D'$ 是 $D$ 在直角坐标平面 $\rho O\theta$ 上的对应区域. 在上一目内所证得的相同的公式中用的是 $D$ 而不是 $D'$ , 当积分区域 $D$ 用极坐标表示时, 其形式就与上式右端的形式完全等同了.

例7 计算 $\iint_{D} \mathrm{e}^{\frac{y - x}{y + x}} \mathrm{d}x \mathrm{~d}y$ ，其中 $D$ 是由 $x$ 轴、 $y$ 轴和直线 $x + y = 2$ 所围成的闭区域.

解 令 $u = y - x, v = y + x$ ，则 $x = \frac{v - u}{2}, y = \frac{v + u}{2}$ .

作变换 $x = \frac{v - u}{2}, y = \frac{v + u}{2}$ , 则 $xOy$ 平面上的闭区域 $D$ 和它在 $uOv$ 平面上的对应区域 $D'$ 如图10-25所示.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/e039bc197ebcd0c9f7bbbe1061c5466c3922f071f54feed788798390f26b15dd.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/7e8ac0ba238d7ed9ea120b12b20d7033d67331cbc14daf979fa50054da60d4b5.jpg)



(b)



图10-25


雅可比式为

$$
J = \frac {\partial (x , y)}{\partial (u , v)} = \left| \begin{array}{c c} - \frac {1}{2} & \frac {1}{2} \\ \frac {1}{2} & \frac {1}{2} \end{array} \right| = - \frac {1}{2}.
$$

利用公式(2-8)，得

$$
\iint_ {D} \mathrm{e} ^ {\frac {y - x}{y + x}} \mathrm{d} x \mathrm{d} y = \iint_ {D ^ {\prime}} \mathrm{e} ^ {\frac {u}{v}} \left| - \frac {1}{2} \right| \mathrm{d} u \mathrm{d} v = \frac {1}{2} \int_ {0} ^ {2} \mathrm{d} v \int_ {- v} ^ {v} \mathrm{e} ^ {\frac {u}{v}} \mathrm{d} u = \frac {1}{2} \int_ {0} ^ {2} (\bar {\mathrm{e}} - \mathrm{e} ^ {- 1}) v \mathrm{d} v = \mathrm{e} - \mathrm{e} ^ {- 1}.
$$

例8 求由直线 $x + y = c, x + y = d, y = ax, y = bx$ ( $0 < c < d, 0 < a < b$ ) 所围成的闭区域 $D$ (图10-26(a)) 的面积.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/ca99254156a217d44ca6113f34670cce5488c9a613c6a13674fc7a09dce3e9cb.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/58aee51b3f6a5cb13af23628097f6cdb80494fa766b45c91080f2f41f4183a3d.jpg)



(b)



图10-26


解 所求面积为

$$
\iint_ {D} \mathrm{d} x \mathrm{d} y.
$$

上述二重积分直接化为二次积分计算比较麻烦.现采用换元法.令 $u=x+y,v=\frac{y}{x}$ ，则 $x=\frac{u}{1+v},y=\frac{uv}{1+v}$ .在这变换下，D的边界 $x+y=c,x+y=d,y=ax,y=bx$ 依次与u=c,u=d,v=a,v=b对应.后者构成与D对应的闭区域 $D'$ 的边界.于是

$$
D ^ {\prime} = \{(u, v) | c \leqslant u \leqslant d, a \leqslant v \leqslant b \},
$$

如图 10-26(b) 所示. 又雅可比式

$$
J = \frac {\partial (x , y)}{\partial (u , v)} = \frac {u}{(1 + v) ^ {2}} \neq 0, \quad (u, v) \in D ^ {\prime}.
$$

从而所求面积为

$$
\iint_ {D} \mathrm{d} x \mathrm{d} y = \iint_ {D ^ {\prime}} \frac {u}{(1 + v) ^ {2}} \mathrm{d} u \mathrm{d} v = \int_ {a} ^ {b} \frac {\mathrm{d} v}{(1 + v) ^ {2}} \int_ {c} ^ {d} u \mathrm{d} u = \frac {(b - a) (d ^ {2} - c ^ {2})}{2 (1 + a) (1 + b)}.
$$

例9 计算 $\iint_{D} \sqrt{1 - \frac{x^2}{a^2} - \frac{y^2}{b^2}} \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $D$ 为椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ 所围成的闭区域.

解 作广义极坐标变换

$$
\left\{ \begin{array}{l} x = a \rho \cos \theta , \\ y = b \rho \sin \theta , \end{array} \right.
$$

其中 $a > 0, b > 0, \rho \geqslant 0, 0 \leqslant \theta \leqslant 2\pi$ . 在这个变换下，与 $D$ 对应的闭区域为 $D' = \{(\rho, \theta) | 0 \leqslant \rho \leqslant 1, 0 \leqslant \theta \leqslant 2\pi\}$ ，雅可比式

$$
J = \frac {\partial (x , y)}{\partial (\rho , \theta)} = a b \rho .
$$

$J$ 在 $D^{\prime}$ 内仅在 $\rho = 0$ 处为零，故换元公式仍成立，从而有

$$
\iint_ {D} \sqrt {1 - \frac {x ^ {2}}{a ^ {2}} - \frac {y ^ {2}}{b ^ {2}}} \mathrm{d} x \mathrm{d} y = \iint_ {D ^ {\prime}} \sqrt {1 - \rho^ {2}} a b \rho \mathrm{d} \rho \mathrm{d} \theta = \frac {2}{3} \pi a b.
$$

# 习题10-2

1. 计算下列二重积分：

(1) $\iint_{D} (x^{2} + y^{2}) \, \mathrm{d}\sigma$ ，其中 $D = \{(x, y) | | x| \leqslant 1, |y| \leqslant 1\}$ ;

(2) $\iint_{D} (3x + 2y) \, \mathrm{d}\sigma$ ，其中 $D$ 是由两坐标轴及直线 $x + y = 2$ 所围成的闭区域；

(3) $\iint_{D} (x^{3} + 3x^{2}y + y^{3}) \, \mathrm{d}\sigma$ , 其中 $D = \{(x, y) \mid 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1\}$ ;

(4) $\iint_{D} x \cos(x + y) \, \mathrm{d}\sigma$ ，其中 $D$ 是顶点分别为 $(0,0)$ ， $(\pi, 0)$ 和 $(\pi, \pi)$ 的三角形闭区域；

(5) $\iint_{D} \sqrt{|y - x^2|} \, \mathrm{d}x \, \mathrm{d}y$ , 其中 $D = \{(x, y) | 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1\}$ .

2. 画出积分区域,并计算下列二重积分:

(1) $\iint_{D} x\sqrt{y} \, \mathrm{d}\sigma$ ，其中 $D$ 是由两条抛物线 $y = \sqrt{x}, y = x^2$ 所围成的闭区域；

(2) $\iint_{D} xy^{2} \, \mathrm{d}\sigma$ ，其中 $D$ 是由圆周 $x^{2} + y^{2} = 4$ 及 $y$ 轴所围成的右半闭区域；

(3) $\iint_{D} \mathrm{e}^{x + y} \mathrm{d}\sigma$ , 其中 $D = \{(x, y) | | x | + |y| \leqslant 1\}$ ;

(4) $\iint_{D}(x^{2}+y^{2}-x)\mathrm{d}\sigma$ , 其中 D 是由直线 y=2, y=x 及 y=2x 所围成的闭区域.

3. 如果二重积分 $\iint_{D} f(x, y) \, \mathrm{d}x \, \mathrm{d}y$ 的被积函数 $f(x, y)$ 是两个函数 $f_{1}(x)$ 及 $f_{2}(y)$ 的乘积，即 $f(x, y) = f_{1}(x) \cdot f_{2}(y)$ ，积分区域 $D = \{(x, y) \mid a \leqslant x \leqslant b, c \leqslant y \leqslant d\}$ ，证明这个二重积分等于两个定积分的乘积，即

$$
\iint_ {D} f _ {1} (x) \cdot f _ {2} (y) \mathrm{d} x \mathrm{d} y = \left[ \int_ {a} ^ {b} f _ {1} (x) \mathrm{d} x \right] \cdot \left[ \int_ {c} ^ {d} f _ {2} (y) \mathrm{d} y \right].
$$

4. 化二重积分

$$
I = \iint_ {D} f (x, y) \mathrm{d} \sigma
$$

为二次积分(分别列出对两个变量先后次序不同的两个二次积分),其中积分区域 D 是

（1）由直线 y=x 及抛物线 $y^{2}=4x$ 所围成的闭区域；

(2) 由 x 轴及半圆周 $x^{2} + y^{2} = r^{2}$ ( $y \geqslant 0$ ) 所围成的闭区域；

(3) 由直线 y=x, x=2 及双曲线 $y=\frac{1}{x}$ (x>0) 所围成的闭区域；

(4) 环形闭区域 $\{(x,y)\mid1\leqslant x^{2}+y^{2}\leqslant4\}$ .

5. 设 $f(x, y)$ 在 $D$ 上连续，其中 $D$ 是由直线 $y = x, y = a$ 及 $x = b (b > a)$ 所围成的闭区域，证明

$$
\int_ {a} ^ {b} \mathrm{d} x \int_ {a} ^ {x} f (x, y) \mathrm{d} y = \int_ {a} ^ {b} \mathrm{d} y \int_ {y} ^ {b} f (x, y) \mathrm{d} x.
$$

6. 交换下列二次积分的积分次序：

(1) $\int_0^1\mathrm{d}y\int_0^y f(x,y)\mathrm{d}x;$ 

(2) $\int_0^2\mathrm{d}y\int_{y^2}^{2y}f(x,y)\mathrm{d}x;$ 

(3) $\int_{0}^{1}\mathrm{d}y\int_{-\sqrt{1 - y^2}}^{\sqrt{1 - y^2}}f(x,y)\mathrm{d}x;$ 

(4) $\int_{1}^{2}\mathrm{d}x\int_{2 - x}^{\sqrt{2x - x^2}}f(x,y)\mathrm{d}y;$ 

(5) $\int_{1}^{\mathrm{e}}\mathrm{d}x\int_{0}^{\ln x}f(x,y)\mathrm{d}y;$ 

(6) $\int_{0}^{\pi}\mathrm{d}x\int_{-\sin \frac{x}{2}}^{\sin x}f(x,y)\mathrm{d}y.$ 

7. 设平面薄片所占的闭区域 D 由直线 $x + y = 2, y = x$ 和 x 轴所围成，它的面密度 $\mu(x, y) = x^{2} + y^{2}$ ，求该薄片的质量.

8. 计算由四个平面 $x = 0, y = 0, x = 1, y = 1$ 所围成的柱体被平面 $z = 0$ 及 $2x + 3y + z = 6$ 截得的立体

的体积.

9. 求由平面 $x = 0, y = 0, x + y = 1$ 所围成的柱体被平面 $z = 0$ 及抛物面 $x^{2} + y^{2} = 6 - z$ 截得的立体的体积.

10. 求由曲面 $z=x^{2}+2y^{2}$ 及 $z=6-2x^{2}-y^{2}$ 所围成的立体的体积.

11. 画出积分区域, 把积分 $\iint_{D} f(x, y) \mathrm{d}x \mathrm{~d}y$ 表示为极坐标形式的二次积分, 其中积分区域 $D$ 是

(1) $\{(x, y) | x^2 + y^2 \leqslant a^2\} (a > 0)$ ; 

(2) $\{(x, y) | x^2 + y^2 \leqslant 2x\}$ ; 

(3) $\{(x, y) | a^2 \leqslant x^2 + y^2 \leqslant b^2\}$ , 其中 $0 < a < b$ ;

(4) $\{(x,y)\mid 0\leqslant y\leqslant 1 - x,0\leqslant x\leqslant 1\}$ . 

12. 化下列二次积分为极坐标形式的二次积分：

(1) $\int_0^1\mathrm{d}x\int_0^1 f(x,y)\mathrm{d}y;$ 

(2) $\int_0^2\mathrm{d}x\int_x^{\sqrt{3} x}f(\sqrt{x^2 + y^2})\mathrm{d}y;$ 

(3) $\int_0^1\mathrm{d}x\int_{1 - x}^{\sqrt{1 - x^2}}f(x,y)\mathrm{d}y;$ 

(4) $\int_{0}^{1}\mathrm{d}x\int_{0}^{x^{2}}f(x,y)\mathrm{d}y.$ 

13. 把下列积分化为极坐标形式,并计算积分值:

(1) $\int_{0}^{2a}\mathrm{d}x\int_{0}^{\sqrt{2ax - x^2}}(x^2 +y^2)\mathrm{d}y;$ 

(2) $\int_{0}^{a}\mathrm{d}x\int_{0}^{x}\sqrt{x^{2} + y^{2}}\mathrm{d}y;$ 

(3) $\int_0^1\mathrm{d}x\int_{x^2}^x (x^2 +y^2)^{-\frac{1}{2}}\mathrm{d}y;$ 

(4) $\int_{0}^{a}\mathrm{d}y\int_{0}^{\sqrt{a^2 - y^2}}(x^2 +y^2)\mathrm{d}x.$ 

14. 利用极坐标计算下列各题：

(1) $\iint_{D} \mathrm{e}^{x^2 + y^2} \, \mathrm{d}\sigma$ ，其中 $D$ 是由圆周 $x^2 + y^2 = 4$ 所围成的闭区域；

(2) $\iint_{D}\ln(1+x^{2}+y^{2})\mathrm{d}\sigma$ ，其中 D 是由圆周 $x^{2}+y^{2}=1$ 及坐标轴所围成的在第一象限内的闭区域；

(3) $\iint_{D}\arctan\frac{y}{x}d\sigma$ , 其中 D 是由圆周 $x^{2}+y^{2}=4, x^{2}+y^{2}=1$ 及直线 y=0, y=x 所围成的在第一象限内的闭区域.

15. 选用适当的坐标计算下列各题：

(1) $\iint_{D} \frac{x^{2}}{y^{2}} \mathrm{d}\sigma$ ，其中 $D$ 是由直线 $x = 2, y = x$ 及曲线 $xy = 1$ 所围成的闭区域；

(2) $\iint_{D} \sqrt{\frac{1 - x^{2} - y^{2}}{1 + x^{2} + y^{2}}} \mathrm{d}\sigma$ ，其中 $D$ 是由圆周 $x^{2} + y^{2} = 1$ 及坐标轴所围成的在第一象限内的闭区域；

(3) $\iint_{D} (x^{2} + y^{2}) \, \mathrm{d}\sigma$ ，其中 $D$ 是由直线 $y = x, y = x + a, y = a, y = 3a$ ( $a > 0$ ) 所围成的闭区域；

(4) $\iint_{D} \sqrt{x^2 + y^2} \, \mathrm{d}\sigma$ ，其中 $D$ 是圆环形闭区域 $\{(x, y) \mid a^2 \leqslant x^2 + y^2 \leqslant b^2\}$ ；

(5) $\iint_{D} \sqrt{a^2 - x^2 - y^2} \, \mathrm{d}\sigma$ ，其中 $D$ 是圆形闭区域 $\{(x, y) | x^2 + y^2 \leqslant ax\} (a > 0)$ .

16. 设平面薄片所占的闭区域 $D$ 由螺线 $\rho = 2\theta$ 上一段弧 $\left(0 \leqslant \theta \leqslant \frac{\pi}{2}\right)$ 与直线 $\theta = \frac{\pi}{2}$ 所围成, 它的

面密度为 $\mu(x,y)=x^{2}+y^{2}$ . 求这薄片的质量(图 10-27).

17. 求由平面 $y = 0, y = kx (k > 0), z = 0$ 以及球心在原点、半径为 $R$ 的上半球面所围成的在第 I 卦限内的立体的体积(图 10-28).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/cc85f0d1a8f8760b61ada038d55f8ae1c0c12ec1f3403d0e9bf1142af56693cd.jpg)



图10-27


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/d1dca61c52f513283fdc58cc57a870d98d0580c1e59a6b5a4e269da5842bf9df.jpg)



图10-28


18. 计算以 $xOy$ 面上的圆周 $x^{2} + y^{2} = ax (a > 0)$ 围成的闭区域为底, 而以曲面 $z = x^{2} + y^{2}$ 为顶的曲顶柱体的体积.

* 19. 作适当的变换,计算下列二重积分:

(1) $\iint_{D} (x - y)^2 \sin^2(x + y) \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $D$ 是平行四边形闭区域，它的四个顶点是 $(\pi, 0), (2\pi, \pi)$ ， $(\pi, 2\pi)$ 和 $(0, \pi)$ ；

(2) $\iint_{D} x^{2} y^{2} \, dx \, dy$ ，其中 D 是由两条双曲线 xy = 1 和 xy = 2，直线 y = x 和 y = 4x 所围成的在第一象限内的闭区域；

(3) $\iint_{D} \mathrm{e}^{\frac{y}{x + y}} \mathrm{d} x \mathrm{~d} y$ ，其中 $D$ 是由 $x$ 轴、 $y$ 轴和直线 $x + y = 1$ 所围成的闭区域；

(4) $\iint_{D}\left(\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}\right)\mathrm{d}x\mathrm{d}y$ ，其中 $D=\left\{(x,y)\mid\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}\leqslant1\right\}$ .

*20. 求由下列曲线所围成的闭区域 $D$ 的面积:

(1) D 是由曲线 xy=4, xy=8, $xy^{3}=5$ , $xy^{3}=15$ 所围成的第一象限部分的闭区域;

(2) D 是由曲线 $y=x^{3}, y=4x^{3}, x=y^{3}, x=4y^{3}$ 所围成的第一象限部分的闭区域.

* 21. 设闭区域 $D$ 是由直线 $x + y = 1, x = 0, y = 0$ 所围成，求证 $\iint_{D} \cos \left( \frac{x - y}{x + y} \right) \mathrm{d}x \mathrm{d}y = \frac{1}{2} \sin 1.$ 

*22. 选取适当的变换,证明下列等式:

(1) $\iint_{D} f(x + y) \, \mathrm{d}x \, \mathrm{d}y = \int_{-1}^{1} f(u) \, \mathrm{d}u$ ，其中闭区域 $D = \{(x, y) | |x| + |y| \leqslant 1\}$ ;

(2) $\iint_{D} f(ax + by + c) \, \mathrm{d}x \, \mathrm{d}y = 2 \int_{-1}^{1} \sqrt{1 - u^2} f(u \sqrt{a^2 + b^2} + c) \, \mathrm{d}u$ ，其中 $D = \{(x, y) | x^2 + y^2 \leqslant 1\}$ ，且 $a^2 + b^2 \neq 0$ .

# 第三节 三重积分

# 一、三重积分的概念

定积分及二重积分作为和的极限的概念,可以很自然地推广到三重积分.

定义 设 $f(x, y, z)$ 是空间有界闭区域 $\Omega$ 上的有界函数. 将 $\Omega$ 任意分成 $n$ 个小闭区域

$$
\Delta V _ {1}, \Delta V _ {2}, \dots , \Delta V _ {n},
$$

其中 $\Delta V_{i}$ 表示第 i 个小闭区域, 也表示它的体积. 在每个 $\Delta V_{i}$ 上任取一点 $(\xi_{i}, \eta_{i}, \zeta_{i})$ , 作乘积 $f(\xi_{i}, \eta_{i}, \zeta_{i}) \Delta V_{i} (i=1,2,\cdots,n)$ , 并作和 $\sum_{i=1}^{n} f(\xi_{i}, \eta_{i}, \zeta_{i}) \Delta V_{i}$ . 如果当各小闭区域直径中的最大值 $\lambda \to 0$ 时, 这和的极限总存在, 且与闭区域 $\Omega$ 的分法及点 $(\xi_{i}, \eta_{i}, \zeta_{i})$ 的取法无关, 那么称此极限为函数 $f(x, y, z)$ 在闭区域 $\Omega$ 上的三重积分. 记作 $\iiint_{\Omega} f(x, y, z) \, dV$ , 即

$$
\iiint_ {\Omega} f (x, y, z) \mathrm{d} V = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \Delta V _ {i}, \tag {3-1}
$$

其中 $f(x,y,z)$ 叫做被积函数, dV 叫做体积元素, $\Omega$ 叫做积分区域.

在直角坐标系中,如果用平行于坐标面的平面来划分 $\Omega$ ,那么除了包含 $\Omega$ 的边界点的一些不规则小闭区域外,得到的小闭区域 $\Delta V_{i}$ 为长方体.设长方体小闭区域 $\Delta V_{i}$ 的边长为 $\Delta x_{j},\Delta y_{k}$ 与 $\Delta z_{l}$ ,则 $\Delta V_{i}=\Delta x_{j}\Delta y_{k}\Delta z_{l}$ .因此在直角坐标系中,有时也把体积元素 dV 记作 dx dy dz,而把三重积分记作

$$
\iiint_ {\Omega} f (x, y, z) \mathrm{d} x \mathrm{d} y \mathrm{d} z,
$$

其中 dx dy dz 叫做直角坐标系中的体积元素.

当函数 $f(x, y, z)$ 在闭区域 $\Omega$ 上连续时，(3-1)式右端的和的极限必定存在，也就是函数 $f(x, y, z)$ 在闭区域 $\Omega$ 上的三重积分必定存在，即函数 $f(x, y, z)$ 在 $\Omega$ 上必定可积。以后我们总假定函数 $f(x, y, z)$ 在闭区域 $\Omega$ 上是可积的。三重积分的性质与第一节中所叙述的二重积分的性质类似，这里不再重复了。

如果 $f(x, y, z)$ 表示某物体在点 $(x, y, z)$ 处的密度, $\Omega$ 是该物体所占有的空间闭区域, $f(x, y, z)$ 在 $\Omega$ 上连续, 那么 $\sum_{i=1}^{n} f(\xi_i, \eta_i, \zeta_i) \Delta V_i$ 是该物体的质量 $m$ 的近似值, 这个和当 $\lambda \to 0$ 时的极限就是该物体的质量 $m$ , 所以

$$
m = \iiint_ {\Omega} f (x, y, z) \mathrm{d} V.
$$

# 二、三重积分的计算

计算三重积分的基本方法是将三重积分化为三次积分来计算.下面按利用不同的坐标来分别讨论将三重积分化为三次积分的方法,且只限于叙述方法.

# 1. 利用直角坐标计算三重积分

假设平行于 $z$ 轴且穿过闭区域 $\Omega$ 内部的直线与闭区域 $\Omega$ 的边界曲面 $S$ 相交不多

于两点. 把闭区域 $\Omega$ 投影到 xOy 面上, 得一平面闭区域 $D_{xy}$ (图 10-29). 以 $D_{xy}$ 的边界为准线作母线平行于 z 轴的柱面. 这柱面与曲面 S 的交线从 S 中分出上、下两部分, 它们的方程分别为

$$
S _ {1}: z = z _ {1} (x, y), \quad S _ {2}: z = z _ {2} (x, y),
$$

其中 $z_{1}(x,y)$ 与 $z_{2}(x,y)$ 都是 $D_{xy}$ 上的连续函数，且 $z_{1}(x,y)\leqslant z_{2}(x,y)$ .过 $D_{xy}$ 内任一点 $(x,y)$ 作平行于 $z$ 轴的直线，这直线通过曲面 $S_{1}$ 穿入 $\Omega$ 内，然后通过曲面 $S_{2}$ 穿出 $\Omega$ 外，穿入点与穿出点的竖坐标分别为 $z_{1}(x,y)$ 与 $z_{2}(x,y)$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/0ba959976442f0cc85c2d1871e73970f8bc607720ff9e2637fa31c66e1057ee0.jpg)



图10-29


在这种情形下,积分区域 $\Omega$ 可表示为

$$
\Omega = \{(x, y, z) | z _ {1} (x, y) \leqslant z \leqslant z _ {2} (x, y), (x, y) \in D _ {x y} \}.
$$

先将 x, y 看做定值, 将 $f(x, y, z)$ 只看做 z 的函数, 在区间 $[z_{1}(x, y), z_{2}(x, y)]$ 上对 z 积分. 积分的结果是 x, y 的函数, 记为 $F(x, y)$ , 即

$$
F (x, y) = \int_ {z _ {1} (x, y)} ^ {z _ {2} (x, y)} f (x, y, z) \mathrm{d} z.
$$

然后计算 $F(x,y)$ 在闭区域 $D_{xy}$ 上的二重积分

$$
\iint_ {D _ {x y}} F (x, y) \mathrm{d} \sigma = \iint_ {D _ {x y}} \left[ \int_ {z _ {1} (x, y)} ^ {z _ {2} (x, y)} f (x, y, z) \mathrm{d} z \right] \mathrm{d} \sigma .
$$

假如闭区域

$$
D _ {x y} = \{(x, y) | y _ {1} (x) \leqslant y \leqslant y _ {2} (x), a \leqslant x \leqslant b \},
$$

把这个二重积分化为二次积分,于是得到三重积分的计算公式

$$
\iiint_ {\Omega} f (x, y, z) \mathrm{d} V = \int_ {a} ^ {b} \mathrm{d} x \int_ {y _ {1} (x)} ^ {y _ {2} (x)} \mathrm{d} y \int_ {z _ {1} (x, y)} ^ {z _ {2} (x, y)} f (x, y, z) \mathrm{d} z. \tag {3-2}
$$

公式(3-2)把三重积分化为先对 z、次对 y、最后对 x 的三次积分.

如果平行于 $x$ 轴或 $y$ 轴且穿过闭区域 $\Omega$ 内部的直线与 $\Omega$ 的边界曲面 $S$ 相交不多于两点, 也可把闭区域 $\Omega$ 投影到 $yOz$ 面上或 $zOx$ 面上, 这样便可把三重积分化为按其他顺序的三次积分. 如果平行于坐标轴且穿过闭区域 $\Omega$ 内部的直线与边界曲面 $S$ 的交点多于两个, 也可像处理二重积分那样, 把 $\Omega$ 分成若干部分, 使 $\Omega$ 上的三重积分化为各部分闭区域上的三重积分的和.

例1 计算三重积分 $\iiint_{\Omega} x \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z$ ，其中 $\Omega$ 为三个坐标面及平面 $x + 2y + z = 1$ 所围成的闭区域.

解 作闭区域 $\Omega$ 如图10-30所示.

将 $\Omega$ 投影到 $xOy$ 面上，得投影区域 $D_{xy}$ 为三角形闭区域OAB.直线 $OA,OB$ 及 $AB$ 的方程依次为 $y = 0,x = 0$ 及 $x + 2y = 1$ ，所以

$$
D _ {x y} = \left\{(x, y) \mid 0 \leqslant y \leqslant \frac {1 - x}{2}, 0 \leqslant x \leqslant 1 \right\}.
$$

在 $D_{xy}$ 内任取一点 $(x,y)$ ，过此点作平行于 z 轴的直线，该直线通过平面 z=0 穿入 $\Omega$ 内，然后通过平面 z=1-x-2y 穿出 $\Omega$ 外.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/0a19a25db16f73a66edc665fbdae06a554a2c9baa17ae198085e7fb9e113eea8.jpg)



图10-30


于是,由公式(3-2)得

$$
\begin{array}{l} \iiint_ {\Omega} x \mathrm{d} x \mathrm{d} y \mathrm{d} z = \int_ {0} ^ {1} \mathrm{d} x \int_ {0} ^ {\frac {1 - x}{2}} \mathrm{d} y \int_ {0} ^ {1 - x - 2 y} x \mathrm{d} z = \int_ {0} ^ {1} x \mathrm{d} x \int_ {0} ^ {\frac {1 - x}{2}} (1 - x - 2 y) \mathrm{d} y \\ = \frac {1}{4} \int_ {0} ^ {1} (x - 2 x ^ {2} + x ^ {3}) \mathrm{d} x = \frac {1}{4 8}. \\ \end{array}
$$

有时,我们计算一个三重积分也可以化为先计算一个二重积分、再计算一个定积分,即有下述计算公式.

设空间闭区域

$$
\Omega = \{(x, y, z) | (x, y) \in D _ {z}, c _ {1} \leqslant z \leqslant c _ {2} \},
$$

其中 $D_{z}$ 是竖坐标为 $z$ 的平面截闭区域 $\Omega$ 所得到的一个平面闭区域（图10-31），则有

$$
\iiint_ {\Omega} f (x, y, z) \mathrm{d} V = \int_ {c _ {1}} ^ {c _ {2}} \mathrm{d} z \iint_ {D _ {z}} f (x, y, z) \mathrm{d} x \mathrm{d} y. \tag {3-3}
$$

例2 计算三重积分 $\iiint_{\Omega} z^2 \mathrm{d}x \mathrm{d}y \mathrm{d}z$ ，其中 $\Omega$ 是由椭球面 $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ 所围成的空间闭区域.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/2aef4c87be473407ebe9a5ef7ba7c3807a3c32f419960ff6bf0d72738cfa5723.jpg)



图10-31


解 空间闭区域 $\Omega$ 可表示为

$$
\left\{(x, y, z) \left| \frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} \leqslant 1 - \frac {z ^ {2}}{c ^ {2}}, - c \leqslant z \leqslant c \right. \right\},
$$

如图 10-32 所示.由公式(3-3)得

$$
\begin{array}{l} \iiint_ {\Omega} z ^ {2} \mathrm{d} x \mathrm{d} y \mathrm{d} z = \int_ {- c} ^ {c} z ^ {2} \mathrm{d} z \iint_ {D _ {z}} \mathrm{d} x \mathrm{d} y \\ = \pi a b \int_ {- c} ^ {c} \left(1 - \frac {z ^ {2}}{c ^ {2}}\right) z ^ {2} \mathrm{d} z = \frac {4}{1 5} \pi a b c ^ {3}. \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/e1b8ba792920d6160856e84cc8d7a5d71b66c1d377a1b2fc36ff933c52afe8c1.jpg)



图10-32


# 2. 利用柱面坐标计算三重积分

设 $M(x,y,z)$ 为空间内一点，并设点 M 在 xOy 面上的投影 P 的极坐标为 $(\rho,\theta)$ ，则这样的三个数 $\rho,\theta,z$ 就叫做点 M 的柱面坐标（图 10-33），这里规定 $\rho,\theta,z$ 的变化范围为

$$
0 \leqslant \rho <   + \infty ,
$$

$$
0 \leqslant \theta \leqslant 2 \pi ,
$$

$$
- \infty <   z <   + \infty .
$$

三组坐标面分别为

$\rho=$ 常数,即以z轴为轴的圆柱面;

$\theta=$ 常数,即过z轴的半平面;

z=常数,即与xOy面平行的平面.

显然,点 M 的直角坐标与柱面坐标的关系为

$$
\left\{ \begin{array}{l} x = \rho \cos \theta , \\ y = \rho \sin \theta , \\ z = z. \end{array} \right. \tag {3-4}
$$

现在要把三重积分 $\iiint_{\Omega} f(x, y, z) \mathrm{d}V$ 中的变量变换为柱面坐标. 为此, 用三组坐标面 $\rho =$ 常数, $\theta =$ 常数, $z =$ 常数把 $\Omega$ 分成许多小闭区域, 除了含 $\Omega$ 的边界点的一些不规则小闭区域外, 这种小闭区域都是柱体. 今考虑由 $\rho, \theta$ 和 $z$ 各取得微小增量 $\mathrm{d}\rho, \mathrm{d}\theta$ 和 $\mathrm{d}z$ 所成的柱体的体积 (图10-34). 这个体积等于高与底面积的乘积. 现在高为 $\mathrm{d}z$ 、底面积在不计高阶无穷小时为 $\rho \mathrm{d}\rho \mathrm{d}\theta$ (即极坐标系中的面积元素), 于是得

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/25b31bc115acfc7a27a6906585f34acfabbe8a1582f327d90fbaaf9035716778.jpg)



图10-34


$$
\mathrm{d} V = \rho \mathrm{d} \rho \mathrm{d} \theta \mathrm{d} z,
$$

这就是柱面坐标系中的体积元素.再注意到关系式(3-4),就有

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/f0b1aeb42a92117ed326c5f808d22dac411411928427f5771cd3f8d65d1c7bb2.jpg)



图10-33


$$
\iiint_ {\Omega} f (x, y, z) \mathrm{d} x \mathrm{d} y \mathrm{d} z = \iiint_ {\Omega} F (\rho , \theta , z) \rho \mathrm{d} \rho \mathrm{d} \theta \mathrm{d} z, \tag {3-5}
$$

其中 $F(\rho, \theta, z) = f(\rho \cos \theta, \rho \sin \theta, z)$ . (3-5)式就是把三重积分的变量从直角坐标变换为柱面坐标的公式. 至于变量变换为柱面坐标后的三重积分的计算, 则可化为三次积分来进行. 化为三次积分时, 积分限是根据 $\rho, \theta$ 和 $z$ 在积分区域 $\Omega$ 中的变化范围来确定的, 下面通过例子来说明.

例3 利用柱面坐标计算三重积分 $\iiint_{\Omega} z \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z$ ，其中 $\Omega$ 是由曲面 $z = x^2 + y^2$ 与平面 $z = 4$ 所围成的闭区域.

解 把闭区域 $\Omega$ 投影到 xOy 面上, 得半径为 2 的圆形闭区域

$$
D _ {x y} = \left\{\left(\rho , \theta\right) \mid 0 \leqslant \rho \leqslant 2, 0 \leqslant \theta \leqslant 2 \pi \right\}.
$$

在 $D_{xy}$ 内任取一点 $(\rho, \theta)$ , 过此点作平行于 $z$ 轴的直线, 此直线通过曲面 $z = x^{2} + y^{2}$ 穿入 $\Omega$ 内, 然后通过平面 $z = 4$ 穿出 $\Omega$ 外. 因此闭区域 $\Omega$ 可用不等式

$$
\rho^ {2} \leqslant z \leqslant 4, \quad 0 \leqslant \rho \leqslant 2, \quad 0 \leqslant \theta \leqslant 2 \pi
$$

来表示.于是

$$
\begin{array}{l} \iiint_ {\Omega} z \mathrm{d} x \mathrm{d} y \mathrm{d} z = \iiint_ {\Omega} z \rho \mathrm{d} \rho \mathrm{d} \theta \mathrm{d} z = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {2} \rho \mathrm{d} \rho \int_ {\rho^ {2}} ^ {4} z \mathrm{d} z \\ = \frac {1}{2} \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {2} \rho (1 6 - \rho^ {4}) \mathrm{d} \rho = \frac {1}{2} \cdot 2 \pi \left[ 8 \rho^ {2} - \frac {1}{6} \rho^ {6} \right] _ {0} ^ {2} = \frac {6 4}{3} \pi . \\ \end{array}
$$

# *3. 利用球面坐标计算三重积分

设 $M(x,y,z)$ 为空间内一点，则点 $M$ 也可用这样三个有次序的数 $r, \varphi$ 和 $\theta$ 来确定，其中 $r$ 为原点 $O$ 与点 $M$ 间的距离， $\varphi$ 为有向线段 $\overrightarrow{OM}$ 与 $z$ 轴正向所夹的角， $\theta$ 为从 $z$ 轴正向来看自 x 轴按逆时针方向转到有向线段 $\overrightarrow{OP}$ 的角, 这里 P 为点 M 在 xOy 面上的投影(图 10-35). 这样的三个数 r, $\varphi$ 和 $\theta$ 叫做点 M 的球面坐标, 这里 r, $\varphi$ 和 $\theta$ 的变化范围为

$$
0 \leqslant r <   + \infty ,
$$

$$
0 \leqslant \varphi \leqslant \pi ,
$$

$$
0 \leqslant \theta \leqslant 2 \pi .
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/2b1643cf89150a4738a6da95c8882d5b77c8007309041bc878d3af54372c74b9.jpg)



图10-35


三组坐标面分别为

r=常数,即以原点为球心的球面;

$\varphi=$ 常数,即以原点为顶点、z轴为轴的圆锥面;

$\theta=$ 常数,即过z轴的半平面.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/827be66290b003881b56bca2214fba4f2e149a0a58fb54f835e387558b2347b2.jpg)


释疑解难

10-2 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/bac4601d8e8ddc15f729ae377833286094698aac4e83959be1d5df0ed2e3efe8.jpg)


例题精讲

10-3 

设点 M 在 xOy 面上的投影为 P，点 P 在 x 轴上的投影为 A，则 OA = x, AP = y, PM = z. 又

$$
O P = r \sin \varphi , \quad z = r \cos \varphi .
$$

因此,点 M 的直角坐标与球面坐标的关系为

$$
\left\{ \begin{array}{l} x = O P \cos \theta = r \sin \varphi \cos \theta , \\ y = O P \sin \theta = r \sin \varphi \sin \theta , \\ z = r \cos \varphi . \end{array} \right. \tag {3-6}
$$

为了把三重积分中的变量从直角坐标变换为球面坐标,用三组坐标面 r= 常数, $\varphi=$ 常数, $\theta=$ 常数把积分区域 $\Omega$ 分成许多小闭区域.考虑由 r, $\varphi$ 和 $\theta$ 各取得微小增量 dr, $d\varphi$ 和 $d\theta$ 所成的六面体的体积(图 10-36).不计高阶无穷小,可把这个六面体看做长方体,其经线方向的长为 $rd\varphi$ ,纬线方向的宽为 $rsin\varphi d\theta$ ,向径方向的高为 dr,于是得

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a0533d802cba6cd4b33b750181a7be27c8f5fdb4e5bef84eab377e56ef8643ff.jpg)



图10-36


$$
\mathrm{d} V = r ^ {2} \sin \varphi \mathrm{d} r \mathrm{d} \varphi \mathrm{d} \theta ,
$$

这就是球面坐标系中的体积元素.再注意到关系式(3-6),就有

$$
\iiint_ {\Omega} f (x, y, z) \mathrm{d} x \mathrm{d} y \mathrm{d} z = \iiint_ {\Omega} F (r, \varphi , \theta) r ^ {2} \sin \varphi \mathrm{d} r \mathrm{d} \varphi \mathrm{d} \theta , \tag {3-7}
$$

其中 $F(r,\varphi,\theta)=f(r\sin\varphi\cos\theta,r\sin\varphi\sin\theta,r\cos\varphi)$ . (3-7) 式就是把三重积分的变量从直角坐标变换为球面坐标的公式.

要计算变量变换为球面坐标后的三重积分, 可把它化为对 r、对 $\varphi$ 及对 $\theta$ 的三次积分.

若积分区域 $\Omega$ 的边界曲面是一个包围原点在内的闭曲面, 其球面坐标方程为 $r = r(\varphi, \theta)$ , 则

$$
I = \iiint_ {\Omega} F (r, \varphi , \theta) r ^ {2} \sin \varphi \mathrm{d} r \mathrm{d} \varphi \mathrm{d} \theta = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\pi} \mathrm{d} \varphi \int_ {0} ^ {r (\varphi , \theta)} F (r, \varphi , \theta) r ^ {2} \sin \varphi \mathrm{d} r.
$$

当积分区域 $\Omega$ 为球面 r=a 所围成时, 则

$$
I = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\pi} \mathrm{d} \varphi \int_ {0} ^ {a} F (r, \varphi , \theta) r ^ {2} \sin \varphi \mathrm{d} r.
$$

特别地，当 $F(r,\varphi ,\theta) = 1$ 时，由上式即得球的体积

$$
V = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\pi} \sin \varphi \mathrm{d} \varphi \int_ {0} ^ {a} r ^ {2} \mathrm{d} r = 2 \pi \cdot 2 \cdot \frac {a ^ {3}}{3} = \frac {4}{3} \pi a ^ {3},
$$

这是我们所熟知的结果.

例 4 求半径为 a 的球面与半顶角为 $\alpha$ 的内接锥面所围成的立体(图 10-37)的体积.

解 设球面通过原点 O, 球心在 z 轴上, 又内接锥面的顶点在原点 O, 其轴与 z 轴重合,则球面方程为 $r=2a\cos\varphi$ , 锥面方程为 $\varphi=\alpha$ . 因为立体所占有的空间闭区域 $\Omega$ 可用不等式

$$
0 \leqslant r \leqslant 2 a \cos \varphi , \quad 0 \leqslant \varphi \leqslant \alpha , \quad 0 \leqslant \theta \leqslant 2 \pi
$$

来表示,所以

$$
\begin{array}{l} V = \iiint_ {\Omega} r ^ {2} \sin \varphi \mathrm{d} r \mathrm{d} \varphi \mathrm{d} \theta = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\alpha} \mathrm{d} \varphi \int_ {0} ^ {2 a \cos \varphi} r ^ {2} \sin \varphi \mathrm{d} r \\ = 2 \pi \int_ {0} ^ {\alpha} \sin \varphi \mathrm{d} \varphi \int_ {0} ^ {2 a \cos \varphi} r ^ {2} \mathrm{d} r = \frac {1 6 \pi a ^ {3}}{3} \int_ {0} ^ {\alpha} \cos^ {3} \varphi \sin \varphi \mathrm{d} \varphi \\ = \frac {4 \pi a ^ {3}}{3} (1 - \cos^ {4} \alpha). \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/c3289a361fdaf0208002e672f38508e2b9e813242bef23e7fe4373de58ea600c.jpg)



图10-37


# 习题10-3

1. 化三重积分 $I = \iiint_{\Omega} f(x, y, z) \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z$ 为三次积分，其中积分区域 $\Omega$ 分别是

(1) 由双曲抛物面 xy=z 及平面 $x+y-1=0, z=0$ 所围成的闭区域；

(2) 由曲面 $z=x^{2}+y^{2}$ 及平面 z=1 所围成的闭区域；

(3) 由曲面 $z=x^{2}+2y^{2}$ 及 $z=2-x^{2}$ 所围成的闭区域；

(4) 由曲面 cz = xy (c > 0), $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1, z = 0$ 所围成的在第 I 卦限内的闭区域.

2. 设有一物体占有空间闭区域 $\Omega = \{(x, y, z) \mid 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1, 0 \leqslant z \leqslant 1\}$ , 在点 $(x, y, z)$ 处的密度为 $\rho(x, y, z) = x + y + z$ , 计算该物体的质量.

3. 如果三重积分 $\iiint_{\Omega} f(x, y, z) \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z$ 的被积函数 $f(x, y, z)$ 是三个函数 $f_1(x), f_2(y), f_3(z)$ 的乘积，即 $f(x, y, z) = f_1(x)f_2(y)f_3(z)$ ，积分区域 $\Omega = \{(x, y, z) \mid a \leqslant x \leqslant b, c \leqslant y \leqslant d, l \leqslant z \leqslant m\}$ ，证明这个三重积分等于三个定积分的乘积，即

$$
\iiint_ {\Omega} f _ {1} (x) f _ {2} (y) f _ {3} (z) \mathrm{d} x \mathrm{d} y \mathrm{d} z = \int_ {a} ^ {b} f _ {1} (x) \mathrm{d} x \int_ {c} ^ {d} f _ {2} (y) \mathrm{d} y \int_ {l} ^ {m} f _ {3} (z) \mathrm{d} z.
$$

4. 计算 $\iiint_{\Omega} xy^2 z^3 \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z$ ，其中 $\Omega$ 是由曲面 $z = xy$ 与平面 $y = x, x = 1$ 和 $z = 0$ 所围成的闭区域.

5. 计算 $\iiint_{\Omega} \frac{\mathrm{d}x \mathrm{~d}y \mathrm{~d}z}{(1 + x + y + z)^3}$ , 其中 $\Omega$ 为平面 $x = 0, y = 0, z = 0, x + y + z = 1$ 所围成的四面体.

6. 计算 $\iiint_{\Omega} xyz \, dx \, dy \, dz$ ，其中 $\Omega$ 为球面 $x^{2} + y^{2} + z^{2} = 1$ 及三个坐标面所围成的在第 I 卦限内的闭区域.

7. 计算 $\iiint_{\Omega} x z \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z$ ，其中 $\Omega$ 是由平面 $z = 0, z = y, y = 1$ 以及抛物柱面 $y = x^2$ 所围成的闭区域.

8. 计算 $\iiint_{\Omega} z \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z$ ，其中 $\Omega$ 是由锥面 $z = \frac{h}{R} \sqrt{x^2 + y^2}$ 与平面 $z = h (R > 0, h > 0)$ 所围成的闭区域.

9. 利用柱面坐标计算下列三重积分：

(1) $\iiint_{\Omega} z \, dV$ , 其中 $\Omega$ 是由曲面 $z = \sqrt{2 - x^{2} - y^{2}}$ 及 $z = x^{2} + y^{2}$ 所围成的闭区域;

(2) $\iiint_{\Omega}(x^{2}+y^{2})\mathrm{d}V$ , 其中 $\Omega$ 是由曲面 $x^{2}+y^{2}=2z$ 及平面 z=2 所围成的闭区域.

* 10. 利用球面坐标计算下列三重积分:

(1) $\iiint_{\Omega} (x^2 + y^2 + z^2) \, \mathrm{d}V$ ，其中 $\Omega$ 是由球面 $x^2 + y^2 + z^2 = 1$ 所围成的闭区域；

(2) $\iiint_{\Omega} z \mathrm{d}V$ ，其中闭区域 $\Omega = \{(x, y, z) | x^2 + y^2 + (z - a)^2 \leqslant a^2, x^2 + y^2 \leqslant z^2\}$ .

11. 选用适当的坐标计算下列三重积分：

(1) $\iiint_{\Omega} xy \, dV$ ，其中 $\Omega$ 为柱面 $x^{2} + y^{2} = 1$ 及平面 z = 1, z = 0, x = 0, y = 0 所围成的在第 I 卦限内的闭区域；

* (2) $\iiint_{\Omega} \sqrt{x^2 + y^2 + z^2} \mathrm{d}V$ ，其中 $\Omega$ 是由球面 $x^2 + y^2 + z^2 = z$ 所围成的闭区域；

(3) $\iiint_{\Omega} (x^2 + y^2) \, \mathrm{d}V$ ，其中 $\Omega$ 是由曲面 $4z^2 = 25(x^2 + y^2)$ 及平面 $z = 5$ 所围成的闭区域；

* (4) $\iiint_{\Omega} (x^2 + y^2) \, \mathrm{d}V$ ，其中闭区域 $\Omega = \{(x, y, z) | 0 < a \leqslant \sqrt{x^2 + y^2 + z^2} \leqslant A, z \geqslant 0\}$ ;

(5) $\iiint_{\Omega}(y^{2}+z^{2})\mathrm{d}V$ , 其中 $\Omega$ 是由抛物面 $x=y^{2}+z^{2}$ 与圆锥面 $x=2-\sqrt{y^{2}+z^{2}}$ 所围成的闭区域.

12. 利用三重积分计算下列由曲面所围成的立体的体积：

(1) $z = 6 - x^{2} - y^{2}$ 及 $z = \sqrt{x^2 + y^2}$ ;

* (2) $x^{2} + y^{2} + z^{2} = 2az$ ( $a > 0$ ) 及 $x^{2} + y^{2} = z^{2}$ （含有 $z$ 轴的部分）；

(3) $z=\sqrt{x^{2}+y^{2}}$ 及 $z=x^{2}+y^{2}$ ;

(4) $z=\sqrt{5-x^{2}-y^{2}}$ 及 $x^{2}+y^{2}=4z.$ 

* 13. 求球体 $r \leqslant a$ 位于锥面 $\varphi = \frac{\pi}{3}$ 和 $\varphi = \frac{2}{3}\pi$ 之间的部分的体积.

14. 求上、下分别为球面 $x^{2}+y^{2}+z^{2}=2$ 和抛物面 $z=x^{2}+y^{2}$ 所围立体的体积.

* 15. 球心在原点、半径为 $R$ 的球, 在其上任意一点的密度的大小与这点到球心的距离成正比, 求这球的质量.

# 第四节 重积分的应用

由前面的讨论可知,曲顶柱体的体积、平面薄片的质量可用二重积分计算,空间物体的质量可用三重积分计算.本节中我们将把定积分应用中的元素法推广到重积分的应用中,利用重积分的元素法来讨论重积分在几何、物理上的一些其他应用.

# 一、曲面的面积

设曲面 $S$ 由方程

$$
z = f (x, y)
$$

给出，D 为曲面 S 在 xOy 面上的投影区域，函数 $f(x,y)$ 在 D 上具有连续偏导数 $f_{x}(x,y)$ 和 $f_{y}(x,y)$ . 要计算曲面 S 的面积 A.

在闭区域 D 上任取一直径很小的闭区域 $d\sigma$ （这小闭区域的面积也记作 $d\sigma$ ）。在$\mathrm{d}\sigma$ 上取一点 $P(x,y)$ ，曲面 $S$ 上对应地有一点 $M(x,y,f(x,y))$ ，点 $M$ 在 $xOy$ 面上的投影即点 $P$ 。点 $M$ 处曲面 $S$ 的切平面设为 $T$ （图10-38）。以小闭区域 $\mathrm{d}\sigma$ 的边界为准线作母线平行于 $z$ 轴的柱面，这柱面在曲面 $S$ 上截下一小片曲面，在切平面 $T$ 上截下一小片平面。由于 $\mathrm{d}\sigma$ 的直径很小，切平面 $T$ 上的那一小片平面的面积 $\mathrm{d}A$ 可以近似代替相应的那小片曲面的面积。设点 $M$ 处曲面 $S$ 上的法线（方向朝上）与 $z$ 轴所成的角为 $\gamma$ ，则

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a239a45094b7d827e312823013cc46d7a3d0e7f8b8bf4032686278b7e9dc4210.jpg)



图10-38


$$
\mathrm{d} A = \frac {\mathrm{d} \sigma}{\cos \gamma} ①.
$$

因为

① 设两平面 $\Pi_1, \Pi_2$ 的夹角为 $\theta$ （取锐角）， $\Pi_1$ 上的闭区域 $D$ 在 $\Pi_2$ 上的投影区域为 $D_0$ ，则 $D$ 的面积 $A$ 与 $D_0$ 的面积 $\sigma$ 之间有关系

$$
A = \frac {\sigma}{\cos \theta}.
$$

事实上，先假定 $D$ 是矩形闭区域，且其一边平行于平面 $\Pi_1, \Pi_2$ 的交线 $l$ ，边长为 $a$ ，另一边长为 $b$ （图10-39），则 $D_0$ 也是矩形闭区域，且边长分别为 $a$ 及 $b\cos \theta$ ，从而

$$
\sigma = a b \cos \theta = A \cos \theta ,
$$

即

$$
A = \frac {\sigma}{\cos \theta}.
$$

在一般情况, 可把 D 分成上述类型的 m 个小矩形闭区域(不计含边界点的不规则部分), 则小矩形闭区域的面积 $A_{k}$ 及其投影区域的面积 $\sigma_{k}$ 之间符合 $A_{k} = \frac{\sigma_{k}}{\cos \theta} (k = 1, 2, \cdots, m)$ , 从而 $\sum_{k=1}^{m} A_{k} = \frac{\sum_{k=1}^{m} \sigma_{k}}{\cos \theta}$ . 使各小闭区域的直径中的最大者趋于零, 取极限便得 $A = \frac{\sigma}{\cos \theta}$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/6488c676bc91ab966f844b4613ddd8a99dc4ca40d32b71603f9483ff9631e5ea.jpg)



图10-39


$$
\cos \gamma = \frac {1}{\sqrt {1 + f _ {x} ^ {2} (x , y) + f _ {y} ^ {2} (x , y)}},
$$

所以

$$
\mathrm{d} A = \sqrt {1 + f _ {x} ^ {2} (x , y) + f _ {y} ^ {2} (x , y)} \mathrm{d} \sigma .
$$

这就是曲面 S 的面积元素, 以它为被积表达式在闭区域 D 上积分, 得

$$
A = \iint_ {D} \sqrt {1 + f _ {x} ^ {2} (x , y) + f _ {y} ^ {2} (x , y)} \mathrm{d} \sigma .
$$

上式也可写成

$$
A = \iint_ {D} \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm{d} x \mathrm{d} y.
$$

这就是计算曲面面积的公式.

设曲面的方程为 $x = g(y,z)$ 或 $y = h(z,x)$ ，可分别把曲面投影到 $yOz$ 面上（投影区域记作 $D_{yz}$ ）或 $zOx$ 面上（投影区域记作 $D_{zx}$ ），类似地可得

$$
A = \iint_ {D _ {y z}} \sqrt {1 + \left(\frac {\partial x}{\partial y}\right) ^ {2} + \left(\frac {\partial x}{\partial z}\right) ^ {2}} \mathrm{d} y \mathrm{d} z,
$$

或

$$
A = \iint_ {D _ {z x}} \sqrt {1 + \left(\frac {\partial y}{\partial z}\right) ^ {2} + \left(\frac {\partial y}{\partial x}\right) ^ {2}} \mathrm{d} z \mathrm{d} x.
$$

例 1 求半径为 a 的球的表面积.

解 取上半球面方程为 $z = \sqrt{a^2 - x^2 - y^2}$ , 则它在 $xOy$ 面上的投影区域 $D = \{(x, y) | x^2 + y^2 \leqslant a^2\}$ .

由 $\frac{\partial z}{\partial x} = \frac{-x}{\sqrt{a^2 - x^2 - y^2}},\frac{\partial z}{\partial y} = \frac{-y}{\sqrt{a^2 - x^2 - y^2}}$ ，得

$$
\sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} = \frac {a}{\sqrt {a ^ {2} - x ^ {2} - y ^ {2}}}.
$$

因为这函数在闭区域 $D$ 上无界, 我们不能直接应用曲面面积公式. 所以先取区域 $D_{1} = \{(x, y) | x^{2} + y^{2} \leqslant b^{2}\}$ ( $0 < b < a$ ) 为积分区域, 算出相应于 $D_{1}$ 上的球面面积 $A_{1}$ 后, 令 $b \to a$ 取 $A_{1}$ 的极限①就得半球面的面积.

$$
A _ {1} = \iint_ {D _ {1}} \frac {a}{\sqrt {a ^ {2} - x ^ {2} - y ^ {2}}} \mathrm{d} x \mathrm{d} y,
$$

利用极坐标,得

$$
A _ {1} = \iint_ {D _ {1}} \frac {a}{\sqrt {a ^ {2} - \rho^ {2}}} \rho \mathrm{d} \rho \mathrm{d} \theta = a \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {b} \frac {\rho \mathrm{d} \rho}{\sqrt {a ^ {2} - \rho^ {2}}} = 2 \pi a \int_ {0} ^ {b} \frac {\rho \mathrm{d} \rho}{\sqrt {a ^ {2} - \rho^ {2}}} = 2 \pi a (a - \sqrt {a ^ {2} - b ^ {2}}).
$$

于是

$$
\lim _ {b \rightarrow a} A _ {1} = \lim _ {b \rightarrow a} 2 \pi a (a - \sqrt {a ^ {2} - b ^ {2}}) = 2 \pi a ^ {2}.
$$

这就是半个球面的面积,因此整个球面的面积为

$$
A = 4 \pi a ^ {2}.
$$

例 2 设有一颗地球同步轨道通信卫星,距地面的高度为 h=36 000 km,运行的角速度与地球自转的角速度相同.试计算该通信卫星的覆盖面积与地球表面积的比值(地球半径 R=6 400 km).

解 取地心为坐标原点, 地心到通信卫星中心的连线为 z 轴, 建立坐标系, 如图 10-40 所示.

通信卫星覆盖的曲面 $\Sigma$ 是上半球面被半顶角为 $\alpha$ 的圆锥面所截得的部分. $\Sigma$ 的方程为

$$
z = \sqrt {R ^ {2} - x ^ {2} - y ^ {2}}, \quad x ^ {2} + y ^ {2} \leqslant R ^ {2} \sin^ {2} \alpha .
$$

于是通信卫星的覆盖面积为

$$
\begin{array}{l} A = \iint_ {D _ {x y}} \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} d x d y \\ = \iint_ {D _ {x y}} \frac {R}{\sqrt {R ^ {2} - x ^ {2} - y ^ {2}}} \mathrm{d} x \mathrm{d} y. \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/aa638e03109e2b533e815dffef4832f6668d548bc448bdfad1a99a7db73ea2bc.jpg)



图10-40


其中 $D_{xy}$ 是曲面 $\Sigma$ 在 $xOy$ 面上的投影区域， $D_{xy} = \{(x,y) | x^2 + y^2 \leqslant R^2 \sin^2 \alpha\}$ .

利用极坐标,得

$$
A = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {R \sin \alpha} \frac {R}{\sqrt {R ^ {2} - \rho^ {2}}} \rho \mathrm{d} \rho = 2 \pi R \int_ {0} ^ {R \sin \alpha} \frac {\rho}{\sqrt {R ^ {2} - \rho^ {2}}} \mathrm{d} \rho = 2 \pi R ^ {2} (1 - \cos \alpha).
$$

由于 $\cos\alpha=\frac{R}{R+h}$ ，代入上式得

$$
A = 2 \pi R ^ {2} \left(1 - \frac {R}{R + h}\right) = 2 \pi R ^ {2} \cdot \frac {h}{R + h}.
$$

由此得这颗通信卫星的覆盖面积与地球表面积之比为

$$
\frac {A}{4 \pi R ^ {2}} = \frac {h}{2 (R + h)} = \frac {3 6 \times 1 0 ^ {3}}{2 (3 6 + 6 . 4) \times 1 0 ^ {3}} \approx 42.5 \%.
$$

由以上结果可知,卫星覆盖了全球三分之一以上的面积,故使用三颗相隔 $\frac{2}{3}\pi$ 角度的通信卫星就可以覆盖几乎地球全部表面.

* 利用曲面的参数方程求曲面的面积

若曲面 S 由参数方程

$$
\left\{ \begin{array}{l l} x = x (u, v), \\ y = y (u, v), & (u, v) \in D \\ z = z (u, v) \end{array} \right.
$$

给出,其中 D 是一个平面有界闭区域,又 $x(u,v)$ , $y(u,v)$ , $z(u,v)$ 在 D 上具有连续的一阶偏导数,且

$$
\frac {\partial (x , y)}{\partial (u , v)}, \quad \frac {\partial (y , z)}{\partial (u , v)}, \quad \frac {\partial (z , x)}{\partial (u , v)}
$$

不全为零,则曲面 S 的面积

$$
A = \iint_ {D} \sqrt {E G - F ^ {2}} \mathrm{d} u \mathrm{d} v,
$$

其中

$$
E = x _ {u} ^ {2} + y _ {u} ^ {2} + z _ {u} ^ {2}, \quad F = x _ {u} x _ {v} + y _ {u} y _ {v} + z _ {u} z _ {v}, \quad G = x _ {v} ^ {2} + y _ {v} ^ {2} + z _ {v} ^ {2}.
$$

下面我们对例 2 用球面的参数方程按上述公式来进行计算.

$\Sigma$ 的参数方程为

$$
\left\{ \begin{array}{l} x = R \sin \varphi \cos \theta , \\ y = R \sin \varphi \sin \theta , \quad (\varphi , \theta) \in D _ {\varphi \theta}. \\ z = R \cos \varphi , \end{array} \right.
$$

这里 $D_{\varphi \theta} = \{(\varphi, \theta) | 0 \leqslant \varphi \leqslant \alpha, 0 \leqslant \theta \leqslant 2\pi\}$ .

由于 $\sqrt{EG - F^2} = R^2\sin \varphi$ ，于是

$$
\begin{array}{l} A = \iint_ {D _ {\varphi \theta}} \sqrt {E G - F ^ {2}} \mathrm{d} \varphi \mathrm{d} \theta = \iint_ {D _ {\varphi \theta}} R ^ {2} \sin \varphi \mathrm{d} \varphi \mathrm{d} \theta \\ = R ^ {2} \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\alpha} \sin \varphi \mathrm{d} \varphi = 2 \pi R ^ {2} (1 - \cos \alpha) = 2 \pi R ^ {2} \frac {h}{R + h}. \\ \end{array}
$$

# 二、质心

先讨论平面薄片的质心.

设在 xOy 平面上有 n 个质点, 它们分别位于点 $(x_{1}, y_{1}), (x_{2}, y_{2}), \cdots, (x_{n}, y_{n})$ 处, 质量分别为 $m_{1}, m_{2}, \cdots, m_{n}$ . 由力学知道, 该质点系的质心的坐标为

$$
\overline {{x}} = \frac {M _ {y}}{M} = \frac {\sum_ {i = 1} ^ {n} m _ {i} x _ {i}}{\sum_ {i = 1} ^ {n} m _ {i}}, \quad \overline {{y}} = \frac {M _ {x}}{M} = \frac {\sum_ {i = 1} ^ {n} m _ {i} y _ {i}}{\sum_ {i = 1} ^ {n} m _ {i}},
$$

其中 $M = \sum_{i=1}^{n} m_i$ 为该质点系的总质量，

$$
M _ {y} = \sum_ {i = 1} ^ {n} m _ {i} x _ {i}, \quad M _ {x} = \sum_ {i = 1} ^ {n} m _ {i} y _ {i},
$$

分别为该质点系对 y 轴和 x 轴的静矩.

设有一平面薄片,占有 xOy 面上的闭区域 D,在点 $(x,y)$ 处的面密度为 $\mu(x,y)$ ,假定 $\mu(x,y)$ 在 D 上连续.现在要找该薄片的质心的坐标.

在闭区域 $D$ 上任取一直径很小的闭区域 $\mathrm{d}\sigma$ （这小闭区域的面积也记作 $\mathrm{d}\sigma$ ）， $(x, y)$ 是这小闭区域上的一个点。因为 $\mathrm{d}\sigma$ 的直径很小，且 $\mu(x, y)$ 在 $D$ 上连续，所以薄片中相应于 $\mathrm{d}\sigma$ 的部分的质量近似等于 $\mu(x, y) \mathrm{d}\sigma$ ，这部分质量可近似看做集中在点 $(x, y)$ 上，于是可写出静矩元素 $\mathrm{d}M_y$ 及 $\mathrm{d}M_x$ ：

$$
\mathrm{d} M _ {y} = x \mu (x, y) \mathrm{d} \sigma , \quad \mathrm{d} M _ {x} = y \mu (x, y) \mathrm{d} \sigma .
$$

以这些元素为被积表达式,在闭区域 D 上积分,便得

$$
M _ {y} = \iint_ {D} x \mu (x, y) \mathrm{d} \sigma , \quad M _ {x} = \iint_ {D} y \mu (x, y) \mathrm{d} \sigma .
$$

又由第一节知道,薄片的质量为

$$
M = \iint_ {D} \mu (x, y) \mathrm{d} \sigma .
$$

所以,薄片的质心的坐标为

$$
\overline {{{x}}} = \frac {M _ {y}}{M} = \frac {\iint_ {D} x \mu (x , y) \mathrm{d} \sigma}{\iint_ {D} \mu (x , y) \mathrm{d} \sigma}, \quad \overline {{{y}}} = \frac {M _ {x}}{M} = \frac {\iint_ {D} y \mu (x , y) \mathrm{d} \sigma}{\iint_ {D} \mu (x , y) \mathrm{d} \sigma}.
$$

如果薄片是均匀的,即面密度为常量,那么上式中可把 $\mu$ 提到积分记号外面,并从分子、分母中约去,这样便得均匀薄片的质心的坐标为

$$
\bar {x} = \frac {1}{A} \iint_ {D} x \mathrm{d} \sigma , \quad \bar {y} = \frac {1}{A} \iint_ {D} y \mathrm{d} \sigma , \tag {4-1}
$$

其中 $A=\iint_{D}\mathrm{d}\sigma$ 为闭区域 D 的面积.这时薄片的质心完全由闭区域 D 的形状所决定.我们把均匀平面薄片的质心叫做这平面薄片所占的平面图形的形心.因此,平面图形 D 的形心的坐标,就可用公式(4-1)计算.

例 3 求位于两圆 $\rho=2\sin\theta$ 和 $\rho=4\sin\theta$ 之间的均匀薄片的质心(图10-41).

解 因为闭区域 D 关于 y 轴对称, 所以质心 $C(\bar{x}, \bar{y})$ 必位于 y 轴上, 于是 $\bar{x} = 0$ .

再按公式

$$
\bar {y} = \frac {1}{A} \iint_ {D} y \mathrm{d} \sigma
$$

计算 $\bar{y}$ . 由于闭区域 D 位于半径为 1 与半径为 2 的两圆之间, 所以它的面积等于这两个圆的面积之差, 即 $A = 3\pi$ . 再利用极坐标计算积分

$$
\begin{array}{l} \iint_ {D} y \mathrm{d} \sigma = \iint_ {D} \rho^ {2} \sin \theta \mathrm{d} \rho \mathrm{d} \theta = \int_ {0} ^ {\pi} \sin \theta \mathrm{d} \theta \int_ {2 \sin \theta} ^ {4 \sin \theta} \rho^ {2} \mathrm{d} \rho \\ = \frac {5 6}{3} \int_ {0} ^ {\pi} \sin^ {4} \theta \mathrm{d} \theta = 7 \pi . \\ \end{array}
$$

因此 $\bar{y}=\frac{7\pi}{3\pi}=\frac{7}{3}$ ，所求质心是 $C\left(0,\frac{7}{3}\right)$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/0193e9f0ae8aec668d9a282aeeea3f110e02b6d6e7fe2f8eb97d2bef6b969d37.jpg)



图10-41


类似地,占有空间有界闭区域 $\Omega$ 、在点 $(x,y,z)$ 处的密度为 $\rho(x,y,z)$ （假定 $\rho(x,y,z)$ 在 $\Omega$ 上连续）的物体的质心坐标是

$$
\overline {{x}} = \frac {1}{M} \iiint_ {\Omega} x \rho (x, y, z) \mathrm{d} V, \quad \overline {{y}} = \frac {1}{M} \iiint_ {\Omega} y \rho (x, y, z) \mathrm{d} V, \quad \overline {{z}} = \frac {1}{M} \iiint_ {\Omega} z \rho (x, y, z) \mathrm{d} V,
$$

其中 $M=\iiint_{\Omega}\rho(x,y,z)\mathrm{d}V.$ 

* 例 4 求均匀半球体的质心.

解 取半球体的对称轴为 z 轴, 原点取在球心上, 又设球半径为 a, 则半球体所占空间闭区域

$$
\Omega = \{(x, y, z) | x ^ {2} + y ^ {2} + z ^ {2} \leqslant a ^ {2}, z \geqslant 0 \}.
$$

显然,质心在z轴上,故 $\bar{x}=\bar{y}=0$ .

$$
\bar {z} = \frac {1}{M} \iiint_ {\Omega} z \rho \mathrm{d} V = \frac {1}{V} \iiint_ {\Omega} z \mathrm{d} V,
$$

其中 $V=\frac{2}{3}\pi a^{3}$ 为半球体的体积.

$$
\begin{array}{l} \iiint_ {\Omega} z \mathrm{d} V = \iiint_ {\Omega} r \cos \varphi \cdot r ^ {2} \sin \varphi \mathrm{d} r \mathrm{d} \varphi \mathrm{d} \theta = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\frac {\pi}{2}} \cos \varphi \sin \varphi \mathrm{d} \varphi \int_ {0} ^ {a} r ^ {3} \mathrm{d} r \\ = 2 \pi \cdot \left[ \frac {\sin^ {2} \varphi}{2} \right] _ {0} ^ {\frac {\pi}{2}} \cdot \frac {a ^ {4}}{4} = \frac {\pi a ^ {4}}{4}. \\ \end{array}
$$

因此, $\bar{z}=\frac{3}{8}a$ ,质心为 $\left(0,0,\frac{3}{8}a\right)$ .

# 三、转动惯量

先讨论平面薄片的转动惯量.

设在 $xOy$ 平面上有 $n$ 个质点, 它们分别位于点

$$
\left(x _ {1}, y _ {1}\right), \quad \left(x _ {2}, y _ {2}\right), \quad \dots , \quad \left(x _ {n}, y _ {n}\right)
$$

处,质量分别为 $m_{1}, m_{2}, \cdots, m_{n}$ . 由力学知道,该质点系对于 x 轴以及对于 y 轴的转动惯量依次为

$$
I _ {x} = \sum_ {i = 1} ^ {n} y _ {i} ^ {2} m _ {i}, \quad I _ {y} = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} m _ {i}.
$$

设有一薄片, 占有 $xOy$ 面上的闭区域 $D$ , 在点 $(x, y)$ 处的面密度为 $\mu(x, y)$ , 假定 $\mu(x, y)$ 在 $D$ 上连续. 现在要求该薄片对于 $x$ 轴的转动惯量 $I_x$ 以及对于 $y$ 轴的转动惯量 $I_y$ .

应用元素法.在闭区域 $D$ 上任取一直径很小的闭区域 $\mathrm{d}\sigma$ （这小闭区域的面积也记作 $\mathrm{d}\sigma$ ）， $(x, y)$ 是该小闭区域上的一个点.因为 $\mathrm{d}\sigma$ 的直径很小，且 $\mu(x, y)$ 在 $D$ 上连续，所以薄片中相应于 $\mathrm{d}\sigma$ 部分的质量近似等于 $\mu(x, y) \mathrm{d}\sigma$ ，这部分质量可近似看做集中在点 $(x, y)$ 上，于是可写出薄片对于 $x$ 轴以及对于 $y$ 轴的转动惯量元素

$$
\mathrm{d} I _ {x} = y ^ {2} \mu (x, y) \mathrm{d} \sigma , \quad \mathrm{d} I _ {y} = x ^ {2} \mu (x, y) \mathrm{d} \sigma .
$$

以这些元素为被积表达式,在闭区域 D 上积分,便得

$$
I _ {x} = \iint_ {D} y ^ {2} \mu (x, y) \mathrm{d} \sigma , I _ {y} = \iint_ {D} x ^ {2} \mu (x, y) \mathrm{d} \sigma .
$$

例 5 求半径为 a 的均匀半圆薄片(面密度为常量 $\mu$ ) 对于其直径边的转动惯量.

解 取坐标系如图 10-42 所示, 则薄片所占闭区域

$$
D = \{(x, y) | x ^ {2} + y ^ {2} \leqslant a ^ {2}, y \geqslant 0 \},
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/be5f415f1a7f0e8d0745e6da5c15d976d1510623f679f82afc6d05795a757c26.jpg)



图10-42


而所求转动惯量即半圆薄片对于 x 轴的转动惯量 $I_{x}$ .

$$
\begin{array}{l} I _ {x} = \iint_ {D} \mu y ^ {2} \mathrm{d} \sigma = \mu \iint_ {D} \rho^ {3} \sin^ {2} \theta \mathrm{d} \rho \mathrm{d} \theta = \mu \int_ {0} ^ {\pi} \mathrm{d} \theta \int_ {0} ^ {a} \rho^ {3} \sin^ {2} \theta \mathrm{d} \rho \\ = \mu \cdot \frac {a ^ {4}}{4} \int_ {0} ^ {\pi} \sin^ {2} \theta \mathrm{d} \theta = \frac {1}{4} \mu a ^ {4} \cdot \frac {\pi}{2} = \frac {1}{4} M a ^ {2}, \\ \end{array}
$$

其中 $M=\frac{1}{2}\pi a^{2}\mu$ 为半圆薄片的质量.

类似地,占有空间有界闭区域 $\Omega$ 、在点 $(x,y,z)$ 处的密度为 $\rho(x,y,z)$ （假定 $\rho(x,y,z)$ 在 $\Omega$ 上连续）的物体对于 x 轴、y 轴和 z 轴的转动惯量为

$$
\begin{array}{l} I _ {x} = \iiint_ {\Omega} (y ^ {2} + z ^ {2}) \rho (x, y, z) \mathrm{d} V, \\ I _ {y} = \iiint_ {\Omega} (z ^ {2} + x ^ {2}) \rho (x, y, z) \mathrm{d} V, \\ I _ {z} = \iiint_ {\Omega} (x ^ {2} + y ^ {2}) \rho (x, y, z) \mathrm{d} V. \\ \end{array}
$$

* 例6 求密度为 $\rho$ 的均匀球对于过球心的一条轴 $l$ 的转动惯量.

解 取球心为坐标原点, z 轴与轴 l 重合, 又设球的半径为 a, 则球所占空间闭区域

$$
\Omega = \{(x, y, z) | x ^ {2} + y ^ {2} + z ^ {2} \leqslant a ^ {2} \}.
$$

所求转动惯量即球对于 z 轴的转动惯量为

$$
\begin{array}{l} I _ {z} = \iiint_ {\Omega} \left(x ^ {2} + y ^ {2}\right) \rho \mathrm{d} V \\ = \rho \iiint_ {\Omega} \left(r ^ {2} \sin^ {2} \varphi \cos^ {2} \theta + r ^ {2} \sin^ {2} \varphi \sin^ {2} \theta\right) r ^ {2} \sin \varphi d r d \varphi d \theta \\ = \rho \iiint_ {\Omega} r ^ {4} \sin^ {3} \varphi \mathrm{d} r \mathrm{d} \varphi \mathrm{d} \theta = \rho \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\pi} \sin^ {3} \varphi \mathrm{d} \varphi \int_ {0} ^ {a} r ^ {4} \mathrm{d} r \\ = \rho \cdot 2 \pi \cdot \frac {a ^ {5}}{5} \int_ {0} ^ {\pi} \sin^ {3} \varphi \mathrm{d} \varphi = \frac {2}{5} \pi a ^ {5} \rho \cdot \frac {4}{3} = \frac {2}{5} a ^ {2} M, \\ \end{array}
$$

其中 $M=\frac{4}{3}\pi a^{3}\rho$ 为球的质量.

# 四、引力

下面讨论空间一物体对于物体外一点 $P_{0}(x_{0}, y_{0}, z_{0})$ 处单位质量的质点的引力问题.

设物体占有空间有界闭区域 $\Omega$ ，它在点 $(x, y, z)$ 处的密度为 $\rho(x, y, z)$ ，并假定 $\rho(x, y, z)$ 在 $\Omega$ 上连续。在物体内任取一直径很小的闭区域 $\mathrm{d}V$ （这闭区域的体积也记作 $\mathrm{d}V$ ）， $(x, y, z)$ 为这一小块中的一点。把这一小块物体的质量 $\rho \mathrm{d}V$ 近似地看做集中在点 $(x, y, z)$ 处。于是按两质点间的引力公式，可得这一小块物体对位于 $P_0(x_0, y_0, z_0)$ 处的单位质量的质点的引力近似地为

$$
\begin{array}{l} \mathrm{d} F = \left(\mathrm{d} F _ {x}, \mathrm{d} F _ {y}, \mathrm{d} F _ {z}\right) \\ = \left(G \frac {\rho (x , y , z) (x - x _ {0})}{r ^ {3}} \mathrm{d} V, G \frac {\rho (x , y , z) (y - y _ {0})}{r ^ {3}} \mathrm{d} V, G \frac {\rho (x , y , z) (z - z _ {0})}{r ^ {3}} \mathrm{d} V\right), \\ \end{array}
$$

其中 $\mathrm{d}F_{x},\mathrm{d}F_{y},\mathrm{d}F_{z}$ 为引力元素 $\mathrm{d}F$ 在三个坐标轴上的分量， $r =$ $\sqrt{(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2},G$ 为引力常量.将 $\mathrm{d}F_{x},\mathrm{d}F_{y},\mathrm{d}F_{z}$ 在 $\Omega$ 上分别积分，即得

$$
\begin{array}{l} \boldsymbol {F} = \left(F _ {x}, F _ {y}, F _ {z}\right) \\ = \left(\iiint_ {\Omega} \frac {G \rho (x , y , z) (x - x _ {0})}{r ^ {3}} \mathrm{d} V, \iiint_ {\Omega} \frac {G \rho (x , y , z) (y - y _ {0})}{r ^ {3}} \mathrm{d} V, \iiint_ {\Omega} \frac {G \rho (x , y , z) (z - z _ {0})}{r ^ {3}} \mathrm{d} V\right). \\ \end{array}
$$

如果考虑平面薄片对薄片外一点 $P_0(x_0, y_0, z_0)$ 处单位质量的质点的引力，设平面薄片占有 $xOy$ 平面上的有界闭区域 $D$ ，其面密度为 $\mu(x, y)$ ，那么只要将上式中的密度 $\rho(x, y, z)$ 换成面密度 $\mu(x, y)$ ，将 $\Omega$ 上的三重积分换成 $D$ 上的二重积分，就可得到相

应的计算公式.

例 7 设半径为 R 的质量均匀的球占有空间闭区域 $\Omega=\left\{(x,y,z)\mid x^{2}+y^{2}+z^{2}\leqslant R^{2}\right\}$ . 求它对位于 $M_{0}(0,0,a)(a>R)$ 处的单位质量的质点的引力.

解 设球的密度为 $\rho_{0}$ ，由球的对称性及质量分布的均匀性知 $F_{x}=F_{y}=0$ ，所求引力沿 z 轴的分量为

$$
\begin{array}{l} F _ {z} = \iiint_ {\Omega} G \rho_ {0} \frac {z - a}{\left[ x ^ {2} + y ^ {2} + (z - a) ^ {2} \right] ^ {\frac {3}{2}}} \mathrm{d} V \\ = G \rho_ {0} \int_ {- R} ^ {R} (z - a) \mathrm{d} z \iint_ {x ^ {2} + y ^ {2} \leqslant R ^ {2} - z ^ {2}} \frac {\mathrm{d} x \mathrm{d} y}{[ x ^ {2} + y ^ {2} + (z - a) ^ {2} ] ^ {\frac {3}{2}}} \\ = G \rho_ {0} \int_ {- R} ^ {R} (z - a) \mathrm{d} z \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\sqrt {R ^ {2} - z ^ {2}}} \frac {\rho \mathrm{d} \rho}{\left[ \rho^ {2} + (z - a) ^ {2} \right] ^ {\frac {3}{2}}} \\ = 2 \pi G \rho_ {0} \int_ {- R} ^ {R} (z - a) \left(\frac {1}{a - z} - \frac {1}{\sqrt {R ^ {2} - 2 a z + a ^ {2}}}\right) d z \\ = 2 \pi G \rho_ {0} \left[ - 2 R + \frac {1}{a} \int_ {- R} ^ {R} (z - a) \mathrm{d} \sqrt {R ^ {2} - 2 a z + a ^ {2}} \right] \\ = 2 \pi G \rho_ {0} \left(- 2 R + 2 R - \frac {2 R ^ {3}}{3 a ^ {2}}\right) = - G \cdot \frac {4 \pi R ^ {3}}{3} \rho_ {0} \cdot \frac {1}{a ^ {2}} = - G \frac {M}{a ^ {2}}, \\ \end{array}
$$

其中 $M=\frac{4\pi R^{3}}{3}\rho_{0}$ 为球的质量.上述结果表明:质量均匀的球对球外一质点的引力如同球的质量集中于球心时两质点间的引力.

# 习题10-4

1. 求球面 $x^{2}+y^{2}+z^{2}=a^{2}$ 含在圆柱面 $x^{2}+y^{2}=ax$ 内部的那部分面积.

2. 求锥面 $z = \sqrt{x^{2} + y^{2}}$ 被柱面 $z^{2} = 2x$ 所割下部分的曲面面积.

3. 求底圆半径相等的两个直交圆柱面 $x^{2}+y^{2}=R^{2}$ 及 $x^{2}+z^{2}=R^{2}$ 所围立体的表面积.

4. 设 $\Sigma$ 为一确定球面 $x^{2} + y^{2} + z^{2} = R^{2}$ （ $R$ 为正的常数），另有一球心在 $\Sigma$ 上、半径为 $r$ 的球面 $\Sigma_{1}$ ，问 $r$ 取何值时，球面 $\Sigma_{1}$ 在球面 $\Sigma$ 内部的那部分面积最大？

5. 设薄片所占的闭区域 D 如下, 求均匀薄片的质心:

(1) D 由 $y = \sqrt{2px}$ , $x = x_{0}$ , y = 0 所围成;

(2) D 是半椭圆形闭区域 $\left\{(x,y)\left|\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}\leqslant1,y\geqslant0\right.\right\}$ ;

(3) D 是界于两个圆 $\rho = a \cos \theta, \rho = b \cos \theta (0 < a < b)$ 之间的闭区域.

6. 设平面薄片所占的闭区域 D 由抛物线 $y = x^{2}$ 及直线 y = x 所围成，它在点 $(x, y)$ 处的面密度 $\mu(x, y) = x^{2}y$ ，求该薄片的质心.

7. 设有一等腰直角三角形薄片, 腰长为 a, 各点处的面密度等于该点到直角顶点的距离的平方, 求这薄片的质心.

8. 利用三重积分计算下列由曲面所围立体的质心(设密度 $\rho=1$ ):

(1) $z^{2}=x^{2}+y^{2},z=1;$ 

* (2) $z = \sqrt{A^2 - x^2 - y^2}$ , $z = \sqrt{a^2 - x^2 - y^2}$ ( $A > a > 0$ ), $z = 0$ ; 

(3) $z=x^{2}+y^{2},x+y=a,x=0,y=0,z=0.$ 

*9. 设球占有闭区域 $\Omega = \{(x, y, z) | x^2 + y^2 + z^2 \leqslant 2Rz\}$ , 它在内部各点处的密度的大小等于该点到坐标原点的距离的平方. 试求这球的质心.

10. 设均匀薄片(面密度为常数 1)所占闭区域 D 如下, 求指定的转动惯量:

(1) $D = \left\{(x,y)\left|\frac{x^2}{a^2} +\frac{y^2}{b^2}\leqslant 1\right.\right\} ,$ 求 $I_{y}$ 

(2) D 由抛物线 $y^{2}=\frac{9}{2}x$ 与直线 x=2 所围成, 求 $I_{x}$ 和 $I_{y}$ ;

(3) D 为矩形闭区域 $\{(x,y)\mid0\leqslant x\leqslant a,0\leqslant y\leqslant b\}$ ，求 $I_{x}$ 和 $I_{y}$ .

11. 已知均匀矩形板(面密度为常量 $\mu$ ) 的长和宽分别为 b 和 h, 计算此矩形板对于通过其形心且分别与一边平行的两轴的转动惯量.

12. 一均匀物体(密度 $\rho$ 为常量)占有的闭区域 $\Omega$ 由曲面 $z = x^{2} + y^{2}$ 和平面 $z = 0, |x| = a, |y| = a$ 所围成，

(1) 求物体的体积;

(2) 求物体的质心;

(3) 求物体关于 z 轴的转动惯量.

13. 求半径为 a、高为 h 的均匀圆柱体对于过中心而平行于母线的轴的转动惯量(设密度 $\rho=1$ ).

14. 设面密度为常量 $\mu$ 的质量均匀的半圆环形薄片占有闭区域 $D=\left\{(x,y,0)\mid R_{1}\leqslant\sqrt{x^{2}+y^{2}}\leqslant R_{2},x\geqslant0\right\}$ ，求它对位于 z 轴上点 $M_{0}(0,0,a)(a>0)$ 处单位质量的质点的引力 F.

15. 设均匀柱体密度为 $\rho_{0}$ ，占有闭区域 $\Omega=\left\{(x,y,z)\mid x^{2}+y^{2}\leqslant R^{2},0\leqslant z\leqslant h\right\}$ ，求它对位于点 $M_{0}(0,0,a)(a>h)$ 处的单位质量的质点的引力.

# * 第五节 含参变量的积分

设 $f(x,y)$ 是矩形(闭区域) $R=\left[a,b\right]\times\left[c,d\right]$ ①上的连续函数.在 $[a,b]$ 上任意取定x的一个值,于是 $f(x,y)$ 是变量y在 $[c,d]$ 上的一个一元连续函数,从而积分

$$
\int_ {c} ^ {d} f (x, y) \mathrm{d} y
$$

存在, 这个积分的值依赖于取定的 $x$ 值. 当 $x$ 的值改变时, 一般说来这个积分的值也跟着改变. 这个积分确定一个定义在 $[a, b]$ 上的 $x$ 的函数, 把它记作 $\varphi(x)$ , 即

$$
\varphi (x) = \int_ {c} ^ {d} f (x, y) \mathrm{d} y \quad (a \leqslant x \leqslant b). \tag {5-1}
$$

这里变量 x 在积分过程中是一个常量, 通常称它为参变量, 因此(5-1)式右端是一个含参变量 x 的积分, 这积分确定 x 的一个函数 $\varphi(x)$ , 下面讨论关于 $\varphi(x)$ 的一些性质.

定理1 如果函数 $f(x, y)$ 在矩形 $R = [a, b] \times [c, d]$ 上连续，那么由积分(5-1)确定的函数 $\varphi(x)$ 在 $[a, b]$ 上也连续.

证 设 $x$ 和 $x + \Delta x$ 是 $[a, b]$ 上的两点，则

$$
\varphi (x + \Delta x) - \varphi (x) = \int_ {c} ^ {d} [ f (x + \Delta x, y) - f (x, y) ] d y. \tag {5-2}
$$

由于 $f(x,y)$ 在闭区域 $R$ 上连续，从而一致连续.因此对于任意取定的 $\varepsilon >0$ ，存在 $\delta >0$ 使得对于 $R$ 内的任意两点 $(x_{1},y_{1})$ 及 $(x_{2},y_{2})$ ，只要它们之间的距离小于 $\delta$ ，即

$$
\sqrt {\left(x _ {2} - x _ {1}\right) ^ {2} + \left(y _ {2} - y _ {1}\right) ^ {2}} <   \delta ,
$$

就有

$$
\left| f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right) \right| <   \varepsilon .
$$

因为点 $(x + \Delta x, y)$ 与 $(x, y)$ 的距离等于 $|\Delta x|$ ，所以当 $|\Delta x| < \delta$ 时，就有

$$
\left| f (x + \Delta x, y) - f (x, y) \right| <   \varepsilon ,
$$

于是由(5-2)式有

$$
\mid \varphi (x + \Delta x) - \varphi (x) \mid \leqslant \int_ {c} ^ {d} \mid f (x + \Delta x, y) - f (x, y) \mid \mathrm{d} y <   \varepsilon (d - c).
$$

所以 $\varphi(x)$ 在 $[a,b]$ 上连续.

既然函数 $\varphi(x)$ 在 $[a, b]$ 上连续, 那么它在 $[a, b]$ 上的积分存在, 这个积分可以写为

$$
\int_ {a} ^ {b} \varphi (x) \mathrm{d} x = \int_ {a} ^ {b} \left[ \int_ {c} ^ {d} f (x, y) \mathrm{d} y \right] \mathrm{d} x = \int_ {a} ^ {b} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y.
$$

右端积分是函数 $f(x, y)$ 先对 $y$ 后对 $x$ 的二次积分. 当 $f(x, y)$ 在矩形 $R$ 上连续时, $f(x, y)$ 在 $R$ 上的二重积分 $\iint_{R} f(x, y) \mathrm{d} x \mathrm{d} y$ 是存在的, 这个二重积分化为二次积分来计算时, 如果先对 $y$ 后对 $x$ 积分, 就是上面的这个二次积分. 但二重积分 $\iint_{R} f(x, y) \mathrm{d} x \mathrm{d} y$ 也可化为先对 $x$ 后对 $y$ 的二次积分 $\int_{c}^{d} \left[ \int_{a}^{b} f(x, y) \mathrm{d} x \right] \mathrm{d} y$ , 因此有下面的定理2.

定理2 如果函数 $f(x,y)$ 在矩形 $R = [a,b]\times [c,d]$ 上连续，那么

$$
\int_ {a} ^ {b} \left[ \int_ {c} ^ {d} f (x, y) \mathrm{d} y \right] \mathrm{d} x = \int_ {c} ^ {d} \left[ \int_ {a} ^ {b} f (x, y) \mathrm{d} x \right] \mathrm{d} y. \tag {5-3}
$$

公式(5-3)也可写成

$$
\int_ {a} ^ {b} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y = \int_ {c} ^ {d} \mathrm{d} y \int_ {a} ^ {b} f (x, y) \mathrm{d} x. \tag {$5-3^{\prime$}}
$$

下面考虑由积分(5-1)确定的函数 $\varphi(x)$ 的微分问题.

定理3 如果函数 $f(x, y)$ 及其偏导数 $f_x(x, y)$ 都在矩形 $R = [a, b] \times [c, d]$ 上连续，那么由积分(5-1)确定的函数 $\varphi(x)$ 在 $[a, b]$ 上可微分，并且

$$
\varphi^ {\prime} (x) = \frac {\mathrm{d}}{\mathrm{d} x} \int_ {c} ^ {d} f (x, y) \mathrm{d} y = \int_ {c} ^ {d} f _ {x} (x, y) \mathrm{d} y. \tag {5-4}
$$

证 因为 $\varphi'(x) = \lim_{\Delta x \to 0} \frac{\varphi(x + \Delta x) - \varphi(x)}{\Delta x}$ , 为了求 $\varphi'(x)$ , 先利用公式(5-2)作出增量之比

$$
\frac {\varphi (x + \Delta x) - \varphi (x)}{\Delta x} = \int_ {c} ^ {d} \frac {f (x + \Delta x , y) - f (x , y)}{\Delta x} \mathrm{d} y. \tag {5-5}
$$

由拉格朗日中值定理以及 $f_{x}(x,y)$ 的一致连续性，可得

$$
\frac {f (x + \Delta x , y) - f (x , y)}{\Delta x} = f _ {x} (x + \theta \Delta x, y) = f _ {x} (x, y) + \eta (x, y, \Delta x), \tag {5-6}
$$

其中 $0 < \theta < 1, |\eta|$ 可小于任意给定的正数 $\varepsilon$ ，只要 $|\Delta x|$ 小于某个正数 $\delta$ . 因此

$$
\left| \int_ {c} ^ {d} \eta (x, y, \Delta x) \mathrm{d} y \right| <   \int_ {c} ^ {d} \varepsilon \mathrm{d} y = \varepsilon (d - c) \quad (\mid \Delta x \mid <   \delta),
$$

这就是说

$$
\lim _ {\Delta x \rightarrow 0} \int_ {c} ^ {d} \eta (x, y, \Delta x) \mathrm{d} y = 0.
$$

由(5-5)及(5-6)有

$$
\frac {\varphi (x + \Delta x) - \varphi (x)}{\Delta x} = \int_ {c} ^ {d} f _ {x} (x, y) \mathrm{d} y + \int_ {c} ^ {d} \eta (x, y, \Delta x) \mathrm{d} y,
$$

令 $\Delta x \rightarrow 0$ 取上式的极限, 即得公式(5-4).

在积分(5-1)中积分限 c 与 d 都是常数.但在实际应用中还会遇到对于参变量 x 的不同的值,积分限也不同的情形,即以下的积分

$$
\Phi (x) = \int_ {\alpha (x)} ^ {\beta (x)} f (x, y) \mathrm{d} y. \tag {5-7}
$$

下面我们考虑这种更为广泛地依赖于参变量的积分的某些性质.

定理4 如果函数 $f(x, y)$ 在矩形 $R = [a, b] \times [c, d]$ 上连续，函数 $\alpha(x)$ 与 $\beta(x)$ 在区间 $[a, b]$ 上连续，且

$$
c \leqslant \alpha (x) \leqslant d, \quad c \leqslant \beta (x) \leqslant d \quad (a \leqslant x \leqslant b),
$$

那么由积分(5-7)确定的函数 $\Phi(x)$ 在 $[a, b]$ 上也连续.

证 设 $x$ 和 $x + \Delta x$ 是 $[a, b]$ 上的两点，则

$$
\Phi (x + \Delta x) - \Phi (x) = \int_ {\alpha (x + \Delta x)} ^ {\beta (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y - \int_ {\alpha (x)} ^ {\beta (x)} f (x, y) \mathrm{d} y.
$$

因为

$$
\begin{array}{l} \int_ {\alpha (x + \Delta x)} ^ {\beta (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y \\ = \int_ {\alpha (x + \Delta x)} ^ {\alpha (x)} f (x + \Delta x, y) \mathrm{d} y + \int_ {\alpha (x)} ^ {\beta (x)} f (x + \Delta x, y) \mathrm{d} y + \int_ {\beta (x)} ^ {\beta (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y, \\ \end{array}
$$

所以

$$
\begin{array}{l} \Phi (x + \Delta x) - \Phi (x) \\ = \int_ {\alpha (x + \Delta x)} ^ {\alpha (x)} f (x + \Delta x, y) \mathrm{d} y + \int_ {\beta (x)} ^ {\beta (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y + \int_ {\alpha (x)} ^ {\beta (x)} [ f (x + \Delta x, y) - f (x, y) ] \mathrm{d} y. \tag {5-8} \\ \end{array}
$$

当 $\Delta x\to 0$ 时，上式右端最后一个积分的积分限不变，根据证明定理1时同样的理由，这个积分趋于零.又

$$
\begin{array}{l} \left| \int_ {\alpha (x + \Delta x)} ^ {\alpha (x)} f (x + \Delta x, y) \mathrm{d} y \right| \leqslant M | \alpha (x + \Delta x) - \alpha (x) |, \\ \left| \int_ {\beta (x)} ^ {\beta (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y \right| \leqslant M | \beta (x + \Delta x) - \beta (x) |, \\ \end{array}
$$

其中 $M$ 是 $\left|f(x,y)\right|$ 在矩形 $R$ 上的最大值. 根据 $\alpha(x)$ 与 $\beta(x)$ 在 $[a,b]$ 上连续的假定，由以上两式可见，当 $\Delta x \to 0$ 时，(5-8)式右端的前两个积分都趋于零. 于是，当 $\Delta x \to 0$ 时，

$$
\Phi (x + \Delta x) - \Phi (x) \rightarrow 0 \quad (a \leqslant x \leqslant b),
$$

所以函数 $\Phi(x)$ 在 $[a,b]$ 上连续.

关于函数 $\Phi(x)$ 的微分,有下述定理:

定理5 如果函数 $f(x, y)$ 及其偏导数 $f_x(x, y)$ 都在矩形 $R = [a, b] \times [c, d]$ 上连续，函数 $\alpha(x)$ 与 $\beta(x)$ 都在区间 $[a, b]$ 上可微，且

$$
c \leqslant \alpha (x) \leqslant d, \quad c \leqslant \beta (x) \leqslant d \quad (a \leqslant x \leqslant b),
$$

那么由积分(5-7)确定的函数 $\Phi(x)$ 在 $[a, b]$ 上可微，且

$$
\begin{array}{l} \Phi^ {\prime} (x) = \frac {\mathrm{d}}{\mathrm{d} x} \int_ {\alpha (x)} ^ {\beta (x)} f (x, y) \mathrm{d} y \\ = \int_ {\alpha (x)} ^ {\beta (x)} f _ {x} (x, y) \mathrm{d} y + f [ x, \beta (x) ] \beta^ {\prime} (x) - f [ x, \alpha (x) ] \alpha^ {\prime} (x). \tag {5-9} \\ \end{array}
$$

证 由(5-8)式有

$$
\frac {\Phi (x + \Delta x) - \Phi (x)}{\Delta x}
$$

$$
= \int_ {\alpha (x)} ^ {\beta (x)} \frac {f (x + \Delta x , y) - f (x , y)}{\Delta x} \mathrm{d} y + \frac {1}{\Delta x} \int_ {\beta (x)} ^ {\beta (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y - \frac {1}{\Delta x} \int_ {\alpha (x)} ^ {\alpha (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y. \tag {5-10}
$$

当 $\Delta x \rightarrow 0$ 时, 上式右端的第一个积分的积分限不变, 根据证明定理 3 时同样的理由, 有

$$
\int_ {\alpha (x)} ^ {\beta (x)} \frac {f (x + \Delta x , y) - f (x , y)}{\Delta x} \mathrm{d} y \rightarrow \int_ {\alpha (x)} ^ {\beta (x)} f _ {x} (x, y) \mathrm{d} y.
$$

对于(5-10)式右端的第二项,应用积分中值定理得

$$
\frac {1}{\Delta x} \int_ {\beta (x)} ^ {\beta (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y = \frac {1}{\Delta x} [ \beta (x + \Delta x) - \beta (x) ] f (x + \Delta x, \eta),
$$

其中 $\eta$ 在 $\beta(x)$ 与 $\beta(x + \Delta x)$ 之间. 当 $\Delta x \to 0$ 时,

$$
\frac {1}{\Delta x} [ \beta (x + \Delta x) - \beta (x) ] \rightarrow \beta^ {\prime} (x), f (x + \Delta x, \eta) \rightarrow f [ x, \beta (x) ].
$$

于是

$$
\frac {1}{\Delta x} \int_ {\beta (x)} ^ {\beta (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y \longrightarrow f [ x, \beta (x) ] \beta^ {\prime} (x).
$$

类似地可证, 当 $\Delta x \rightarrow 0$ 时,

$$
\frac {1}{\Delta x} \int_ {\alpha (x)} ^ {\alpha (x + \Delta x)} f (x + \Delta x, y) \mathrm{d} y \rightarrow f [ x, \alpha (x) ] \alpha^ {\prime} (x).
$$

因此,令 $\Delta x\rightarrow0$ , 取(5-10)式的极限便得公式(5-9).

公式(5-9)称为莱布尼茨公式.

例1 设 $\Phi(x) = \int_{x}^{x^2} \frac{\sin(xy)}{y} \, \mathrm{d}y$ , 求 $\Phi'(x)$ .

解 应用莱布尼茨公式, 得

$$
\begin{array}{l} \Phi^ {\prime} (x) = \int_ {x} ^ {x ^ {2}} \cos (x y) d y + \frac {\sin x ^ {3}}{x ^ {2}} \cdot 2 x - \frac {\sin x ^ {2}}{x} \cdot 1 \\ = \left[ \frac {\sin (x y)}{x} \right] _ {x} ^ {x ^ {2}} + \frac {2 \sin x ^ {3}}{x} - \frac {\sin x ^ {2}}{x} = \frac {3 \sin x ^ {3} - 2 \sin x ^ {2}}{x}. \\ \end{array}
$$

例2 求 $I = \int_{0}^{1}\frac{x^{b} - x^{a}}{\ln x}\mathrm{d}x$ （ $0 < a < b$ ）.

解 因为

$$
\int_ {a} ^ {b} x ^ {y} \mathrm{d} y = \left[ \frac {x ^ {y}}{\ln x} \right] _ {a} ^ {b} = \frac {x ^ {b} - x ^ {a}}{\ln x},
$$

所以

$$
I = \int_ {0} ^ {1} \mathrm{d} x \int_ {a} ^ {b} x ^ {\gamma} \mathrm{d} y.
$$

这里函数 $f(x,y)=x^{y}$ 在矩形 $R=[0,1]\times[a,b]$ 上连续，根据定理2，可交换积分次序，由此有

$$
I = \int_ {a} ^ {b} \mathrm{d} y \int_ {0} ^ {1} x ^ {y} \mathrm{d} x = \int_ {a} ^ {b} \left[ \frac {x ^ {y + 1}}{y + 1} \right] _ {0} ^ {1} \mathrm{d} y = \int_ {a} ^ {b} \frac {1}{y + 1} \mathrm{d} y = \ln \frac {b + 1}{a + 1}.
$$

例3 计算定积分 $I = \int_{0}^{1}\frac{\ln(1 + x)}{1 + x^{2}}\mathrm{d}x.$ 

解 考虑含参变量 $\alpha$ 的积分所确定的函数

$$
\varphi (\alpha) = \int_ {0} ^ {1} \frac {\ln (1 + \alpha x)}{1 + x ^ {2}} \mathrm{d} x.
$$

显然, $\varphi(0)=0,\varphi(1)=I.$ 根据公式(5-4)得

$$
\varphi^ {\prime} (\alpha) = \int_ {0} ^ {1} \frac {x}{(1 + \alpha x) (1 + x ^ {2})} \mathrm{d} x.
$$

把被积函数分解为部分分式,得到

$$
\frac {x}{(1 + \alpha x) (1 + x ^ {2})} = \frac {1}{1 + \alpha^ {2}} \left(\frac {- \alpha}{1 + \alpha x} + \frac {x}{1 + x ^ {2}} + \frac {\alpha}{1 + x ^ {2}}\right).
$$

于是

$$
\begin{array}{l} \varphi^ {\prime} (\alpha) = \frac {1}{1 + \alpha^ {2}} \left(\int_ {0} ^ {1} \frac {- \alpha \mathrm{d} x}{1 + \alpha x} + \int_ {0} ^ {1} \frac {x \mathrm{d} x}{1 + x ^ {2}} + \int_ {0} ^ {1} \frac {\alpha \mathrm{d} x}{1 + x ^ {2}}\right) \\ = \frac {1}{1 + \alpha^ {2}} \left[ - \ln (1 + \alpha) + \frac {1}{2} \ln 2 + \alpha \cdot \frac {\pi}{4} \right], \\ \end{array}
$$

上式在 $[0,1]$ 上对 $\alpha$ 积分,得到

$$
\varphi (1) - \varphi (0) = - \int_ {0} ^ {1} \frac {\ln (1 + \alpha)}{1 + \alpha^ {2}} \mathrm{d} \alpha + \frac {1}{2} \ln 2 \int_ {0} ^ {1} \frac {\mathrm{d} \alpha}{1 + \alpha^ {2}} + \frac {\pi}{4} \int_ {0} ^ {1} \frac {\alpha}{1 + \alpha^ {2}} \mathrm{d} \alpha ,
$$

即

$$
I = - I + \frac {\ln 2}{2} \cdot \frac {\pi}{4} + \frac {\pi}{4} \cdot \frac {\ln 2}{2} = - I + \frac {\pi}{4} \ln 2.
$$

从而

$$
I = \frac {\pi}{8} \ln 2.
$$

# *习题10-5

1. 求下列含参变量的积分所确定的函数的极限：

(1) $\lim_{x\to 0}\int_{x}^{1 + x}\frac{\mathrm{d}y}{1 + x^2 + y^2};$ 

(2) $\lim_{x\to 0}\int_{-1}^{1}\sqrt{x^2 + y^2}\mathrm{d}y;$ 

(3) $\lim_{x\to0}\int_{0}^{2}y^{2}\cos(xy)\mathrm{d}y.$ 

2. 求下列函数的导数：

(1) $\varphi(x) = \int_{\sin x}^{\cos x} (y^2 \sin x - y^3) \, \mathrm{d}y$ ; 

(2) $\varphi(x) = \int_{0}^{x} \frac{\ln(1 + xy)}{y} \, \mathrm{d}y$ ; 

(3) $\varphi(x)=\int_{x^{2}}^{x^{3}}\arctan\frac{y}{x}\mathrm{d}y;$ 

(4) $\varphi(x) = \int_{x}^{x^2} e^{-xy^2} dy.$ 

3. 设 $F(x) = \int_{0}^{x}(x + y)f(y)\mathrm{d}y$ ，其中 $f(y)$ 为可微的函数，求 $F''(x)$ .

4. 应用对参数的微分法, 计算下列积分:

(1) $I = \int_{0}^{\frac{\pi}{2}}\ln \frac{1 + a\cos x}{1 - a\cos x}\cdot \frac{\mathrm{d}x}{\cos x} (|a| < 1);$ 

(2) $I = \int_{0}^{\frac{\pi}{2}}\ln (\cos^{2}x + a^{2}\sin^{2}x)\mathrm{d}x (a > 0).$ 

5. 计算下列积分：

(1) $\int_0^1\frac{\arctan x}{x}\frac{\mathrm{d}x}{\sqrt{1 - x^2}};$ 

(2) $\int_0^1\sin \left(\ln \frac{1}{x}\right)\frac{x^b - x^a}{\ln x}\mathrm{d}x$ ( $0 <   a <   b$ ). 

# 总习题十

1. 填空：

(1) 积分 $\int_{0}^{2} dx \int_{x}^{2} e^{-y^{2}} dy$ 的值是 ____；

(2) 设闭区域 $D = \{(x, y) \mid x^{2} + y^{2} \leqslant R^{2}\}$ ，则 $\iint_{D} \left( \frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} \right) \, dx \, dy =$ ____ .

2. 以下各题中给出了四个结论,从中选出一个正确的结论:

（1）设有空间闭区域 $\Omega_{1} = \{(x,y,z) | x^{2} + y^{2} + z^{2} \leqslant R^{2}, z \geqslant 0\}$ , $\Omega_{2} = \{(x,y,z) | x^{2} + y^{2} + z^{2} \leqslant R^{2}, x \geqslant 0, y \geqslant 0, z \geqslant 0\}$ , 则有（ ）；

(A) $\iiint_{\Omega_{1}} x \, dV = 4 \iiint_{\Omega_{2}} x \, dV$ 

(B) $\iiint_{\Omega_{1}} y \, dV = 4 \iiint_{\Omega_{2}} y \, dV$ 

(C) $\iiint_{\Omega_{1}} z \, dV = 4 \iiint_{\Omega_{2}} z \, dV$ 

(D) $\iiint_{\Omega_{1}} xyz \, dV = 4 \iiint_{\Omega_{2}} xyz \, dV$ 

（2）设有平面闭区域 $D = \{(x,y)\mid -a\leqslant x\leqslant a,x\leqslant y\leqslant a\} ,D_{1} = \{(x,y)\mid 0\leqslant x\leqslant a,x\leqslant y\leqslant a\}$ ，则 $\iint_{D}(xy + \cos x\sin y)\mathrm{d}x\mathrm{d}y = (\quad)$ 

(A) $2\iint_{D_{1}}\cos x\sin y\,dx dy$ 

(B) $2\iint_{D_{1}}xy\,dx\,dy$ 

(C) $4\iint_{D_{1}}(xy+\cos x\sin y)\mathrm{d}x\mathrm{d}y$ 

(D) 0 

(3) 设 $f(x)$ 为连续函数, $F(t)=\int_{1}^{t}\mathrm{d}y\int_{y}^{t}f(x)\mathrm{d}x$ , 则 $F'(2)=(\quad)$ .

(A) $2f(2)$ 

(B) $f(2)$ 

(C) $-f(2)$ 

(D) 0 

3. 计算下列二重积分：

(1) $\iint_{D} (1 + x) \sin y \, \mathrm{d}\sigma$ , 其中 $D$ 是顶点分别为 $(0,0), (1,0), (1,2)$ 和 $(0,1)$ 的梯形闭区域;

(2) $\iint_{D} (x^{2} - y^{2}) \, \mathrm{d}\sigma$ , 其中 $D = \{(x, y) \mid 0 \leqslant y \leqslant \sin x, 0 \leqslant x \leqslant \pi\}$ ;

(3) $\iint_{D} \sqrt{R^{2} - x^{2} - y^{2}} \, \mathrm{d}\sigma$ ，其中 $D$ 是圆周 $x^{2} + y^{2} = Rx$ 所围成的闭区域；

(4) $\iint_{D} (y^{2} + 3x - 6y + 9)\mathrm{d}\sigma$ ，其中 $D = \{(x, y) | x^{2} + y^{2} \leqslant R^{2}\}$ .

4. 交换下列二次积分的次序：

(1) $\int_0^4\mathrm{d}y\int_{-\sqrt{4 - y}}^{\frac{1}{2} (y - 4)}f(x,y)\mathrm{d}x;$ 

(2) $\int_0^1\mathrm{d}y\int_0^{2y}f(x,y)\mathrm{d}x + \int_1^3\mathrm{d}y\int_0^{3 - y}f(x,y)\mathrm{d}x;$ 

(3) $\int_0^1\mathrm{d}x\int_{\sqrt{x}}^{1 + \sqrt{1 - x^2}}f(x,y)\mathrm{d}y.$ 

5. 证明：

$$
\int_ {0} ^ {a} \mathrm{d} y \int_ {0} ^ {y} \mathrm{e} ^ {m (a - x)} f (x) \mathrm{d} x = \int_ {0} ^ {a} (a - x) \mathrm{e} ^ {m (a - x)} f (x) \mathrm{d} x.
$$

6. 把积分 $\iint_{D} f(x, y) \mathrm{d}x \mathrm{d}y$ 表示为极坐标形式的二次积分, 其中积分区域 $D = \{(x, y) \mid x^2 \leqslant y \leqslant 1, -1 \leqslant x \leqslant 1\}$ .

7. 设 $f(x, y)$ 在闭区域 $D = \{(x, y) | x^2 + y^2 \leqslant y, x \geqslant 0\}$ 上连续，且

$$
f (x, y) = \sqrt {1 - x ^ {2} - y ^ {2}} - \frac {8}{\pi} \iint_ {D} f (x, y) d x d y,
$$

求 $f(x,y)$ .

8. 把积分 $\iiint_{\Omega} f(x, y, z) \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z$ 化为三次积分, 其中积分区域 $\Omega$ 是由曲面 $z = x^2 + y^2, y = x^2$ 及平面 $y = 1, z = 0$ 所围成的闭区域.

9. 计算下列三重积分：

(1) $\iiint_{\Omega} xy^{2} \, dV$ , 其中 $\Omega$ 是由 $z = 0, x + y - z = 0, x - y - z = 0$ 和 x = 1 所围成的闭区域;

(2) $\iiint_{\Omega} z^2 \mathrm{d}x \mathrm{d}y \mathrm{d}z$ ，其中 $\Omega$ 是两个球： $x^2 + y^2 + z^2 \leqslant R^2$ 和 $x^2 + y^2 + z^2 \leqslant 2Rz (R > 0)$ 的公共部分；

(3) $\iiint_{\Omega} \frac{z \ln (x^2 + y^2 + z^2 + 1)}{x^2 + y^2 + z^2 + 1} \mathrm{d}V$ ，其中 $\Omega$ 是由球面 $x^2 + y^2 + z^2 = 1$ 所围成的闭区域；

(4) $\iiint_{\Omega}(y^{2}+z^{2})\mathrm{d}V$ , 其中 $\Omega$ 是由 xOy 面上曲线 $y^{2}=2x$ 绕 x 轴旋转而成的曲面与平面 x=5 所围成的闭区域.

*10. 设函数 $f(x)$ 连续且恒大于零，

$$
F (t) = \frac {\iiint f (x ^ {2} + y ^ {2} + z ^ {2}) \mathrm{d} V}{\iint_ {D (t)} f (x ^ {2} + y ^ {2}) \mathrm{d} \sigma}, \quad G (t) = \frac {\iint_ {D (t)} f (x ^ {2} + y ^ {2}) \mathrm{d} \sigma}{\int_ {- t} ^ {t} f (x ^ {2}) \mathrm{d} x},
$$

其中 $\Omega(t) = \{(x, y, z) \mid x^2 + y^2 + z^2 \leqslant t^2\}$ , $D(t) = \{(x, y) \mid x^2 + y^2 \leqslant t^2\}$ .

(1) 讨论 $F(t)$ 在区间 $(0, +\infty)$ 内的单调性；

(2) 证明当 t>0 时, $F(t)>\frac{2}{\pi}G(t)$ .

11. 求平面 $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$ 被三坐标面所割出的有限部分的面积.

12. 在均匀的半径为 R 的半圆形薄片的直径上, 要接上一个一边与直径等长的同样材料的均匀矩形薄片, 为了使整个均匀薄片的质心恰好落在圆心上, 间接上去的均匀矩形薄片另一边的长度应是多少?

13. 求由抛物线 $y=x^{2}$ 及直线 y=1 所围成的均匀薄片（面密度为常数 $\mu$ ）对于直线 y=-1 的转动惯量.

14. 设在 $xOy$ 面上有一质量为 $M$ 的质量均匀的半圆形薄片，占有平面闭区域 $D = \{(x, y) \mid x^2 + y^2 \leqslant R^2, y \geqslant 0\}$ ，过圆心 $O$ 垂直于薄片的直线上有一质量为 $m$ 的质点 $P, OP = a$ . 求半圆形薄片对质点 $P$ 的引力.

15. 求质量分布均匀的半个旋转椭球体 $\Omega=\left\{(x,y,z)\left|\frac{x^{2}+y^{2}}{a^{2}}+\frac{z^{2}}{b^{2}}\leqslant1,z\geqslant0\right.\right\}$ 的质心.

*16. 一球形行星的半径为 $R$ , 其质量为 $M$ , 其密度呈球对称分布, 并向着球心线性增加. 若行星表面的密度为零, 则行星中心的密度是多少?


第十章释疑解难


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/01ec3af3a23bfd7042467da27b0cebcefe75856de5a11c9334b343d914d17f93.jpg)



第十章例题精讲


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/1e7be591726fc7736c7b870d9a312160338c20b3de9437bd2e520630338ed109.jpg)


# 第十一章

# 曲线积分与曲面积分

上一章已经把积分概念从积分范围为数轴上一个区间的情形推广到积分范围为平面或空间内的一个闭区域的情形.本章将把积分概念推广到积分范围为一段曲线弧或一片曲面①的情形(这样推广后的积分称为曲线积分和曲面积分),并阐明有关这两种积分的一些基本内容.

# 第一节 对弧长的曲线积分

# 一、对弧长的曲线积分的概念与性质

曲线形构件的质量 在设计曲线形构件时,为了合理使用材料,应该根据构件各部分受力情况,把构件上各点处的粗细程度设计得不完全一样.因此,可以认为这构件的线密度(单位长度的质量)是变量.假设这构件所处的位置在xOy面内的一段曲线弧L上,它的端点是A,B,在L上任一点 $(x,y)$ 处,它的线密度为 $\mu(x,y)$ .现在要计算这构件的质量m（图11-1）.

如果构件的线密度为常量,那么这构件的质量就等于它的线密度与长度的乘积.现在构件上各点处的线密度是变量,就不能直接用上述方法来计算.为了克服这个困难,可以用L上的点 $M_{1},M_{2},\cdots,M_{n-1}$ 把L分成n个小

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/249b9a30476b372da2045d1074a4a9719c335bfc9ba565a9564cd3985fe86df8.jpg)



图11-1


段,取其中一小段构件 $\widehat{M_{i-1}M_{i}}$ 来分析.在线密度连续变化的前提下,只要这小段很短,就可以用这小段上任一点 $(\xi_{i},\eta_{i})$ 处的线密度代替这小段上其他各点处的线密度，从而得到这小段构件的质量的近似值为

$$
\mu (\xi_ {i}, \eta_ {i}) \Delta s _ {i},
$$

其中 $\Delta s_{i}$ 表示 $\widehat{M_{i - 1}M_i}$ 的长度，于是整个曲线形构件的质量

$$
m \approx \sum_ {i = 1} ^ {n} \mu (\xi_ {i}, \eta_ {i}) \Delta s _ {i}.
$$

用 $\lambda$ 表示 $n$ 个小弧段的最大长度.为了计算 $m$ 的精确值,取上式右端之和当 $\lambda \to 0$ 时的极限,从而得到

$$
m = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} \mu (\xi_ {i}, \eta_ {i}) \Delta s _ {i}.
$$

这种和的极限在研究其他问题时也会遇到.现在引进下面的定义：

定义 设 L 为 xOy 面内的一条光滑曲线弧, 函数 $f(x,y)$ 在 L 上有界. 在 L 上任意插入一点列 $M_{1}, M_{2}, \cdots, M_{n-1}$ 把 L 分成 n 个小段. 设第 i 个小段的长度为 $\Delta s_{i}$ . 又 $(\xi_{i}, \eta_{i})$ 为第 i 个小段上任意取定的一点, 作乘积 $f(\xi_{i}, \eta_{i}) \Delta s_{i} (i=1,2,\cdots,n)$ , 并作和 $\sum_{i=1}^{n} f(\xi_{i}, \eta_{i}) \Delta s_{i}$ , 如果当各小弧段的长度的最大值 $\lambda \to 0$ 时, 这和的极限总存在, 且与曲线弧 L 的分法及点 $(\xi_{i}, \eta_{i})$ 的取法无关, 那么称此极限为函数 $f(x,y)$ 在曲线弧 L 上对弧长的曲线积分或第一类曲线积分, 记作 $\int_{L} f(x,y) \, ds$ , 即

$$
\int_ {L} f (x, y) \mathrm{d} s = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}) \Delta s _ {i},
$$

其中 $f(x,y)$ 叫做被积函数, L 叫做积分弧段.

在第二目中我们将看到, 当 $f(x,y)$ 在光滑曲线弧 L 上连续时, 对弧长的曲线积分 $\int_{L}f(x,y)\mathrm{d}s$ 是存在的. 以后我们总假定 $f(x,y)$ 在 L 上是连续的.

根据这个定义,前述曲线形构件的质量 m 当线密度 $\mu(x,y)$ 在 L 上连续时,就等于 $\mu(x,y)$ 对弧长的曲线积分,即

$$
m = \int_ {L} \mu (x, y) \mathrm{d} s.
$$

上述定义可以类似地推广到积分弧段为空间曲线弧 $\Gamma$ 的情形, 即函数 $f(x, y, z)$ 在曲线弧 $\Gamma$ 上对弧长的曲线积分

$$
\int_ {\Gamma} f (x, y, z) \mathrm{d} s = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \Delta s _ {i}.
$$

如果 $L$ (或 $\Gamma$ ) 是分段光滑的①, 我们规定函数在 $L$ (或 $\Gamma$ ) 上的曲线积分等于函数在光滑的各段上的曲线积分之和.例如,设 L 可分成两段光滑曲线弧 $L_{1}$ 及 $L_{2}$ （记作 $L=L_{1}+L_{2}$ ），就规定

$$
\int_ {L _ {1} + L _ {2}} f (x, y) \mathrm{d} s = \int_ {L _ {1}} f (x, y) \mathrm{d} s + \int_ {L _ {2}} f (x, y) \mathrm{d} s.
$$

如果 L 是闭曲线, 那么函数 $f(x, y)$ 在闭曲线 L 上对弧长的曲线积分记为 $\oint_{L} f(x, y) \, ds$ .

由对弧长的曲线积分的定义可知,它有以下性质:

性质1 设 $\alpha, \beta$ 为常数, 则

$$
\int_ {L} [ \alpha f (x, y) + \beta g (x, y) ] d s = \alpha \int_ {L} f (x, y) d s + \beta \int_ {L} g (x, y) d s.
$$

性质2 若积分弧段 $L$ 可分成两段光滑曲线弧 $L_{1}$ 和 $L_{2}$ ，则

$$
\int_ {L} f (x, y) \mathrm{d} s = \int_ {L _ {1}} f (x, y) \mathrm{d} s + \int_ {L _ {2}} f (x, y) \mathrm{d} s.
$$

性质3 设在 $L$ 上 $f(x, y) \leqslant g(x, y)$ ，则

$$
\int_ {L} f (x, y) \mathrm{d} s \leqslant \int_ {L} g (x, y) \mathrm{d} s.
$$

特别地,有

$$
\left| \int_ {L} f (x, y) \mathrm{d} s \right| \leqslant \int_ {L} | f (x, y) | \mathrm{d} s.
$$

# 二、对弧长的曲线积分的计算法

定理 设 $f(x, y)$ 在曲线弧 $L$ 上有定义且连续, $L$ 的参数方程为

$$
\left\{ \begin{array}{l l} x = \varphi (t), \\ y = \psi (t) \end{array} \right. (\alpha \leqslant t \leqslant \beta),
$$

若 $\varphi(t), \psi(t)$ 在 $[\alpha, \beta]$ 上具有一阶连续导数，且 $\varphi'^2(t) + \psi'^2(t) \neq 0$ ，则曲线积分 $\int_{L} f(x, y) \mathrm{d}s$ 存在，且

$$
\int_ {L} f (x, y) \mathrm{d} s = \int_ {\alpha} ^ {\beta} f [ \varphi (t), \psi (t) ] \sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)} \mathrm{d} t (\alpha <   \beta). \tag {1-1}
$$

证 假定当参数 $t$ 由 $\alpha$ 变至 $\beta$ 时, $L$ 上的点 $M(x, y)$ 依点 $A$ 至点 $B$ 的方向描出曲线弧 $L$ . 在 $L$ 上取一列点

$$
A = M _ {0}, M _ {1}, M _ {2}, \dots , M _ {n - 1}, M _ {n} = B,
$$

它们对应于一列单调增加的参数值

$$
\alpha = t _ {0} <   t _ {1} <   t _ {2} <   \dots <   t _ {n - 1} <   t _ {n} = \beta .
$$

根据对弧长的曲线积分的定义,有

$$
\int_ {L} f (x, y) \mathrm{d} s = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}) \Delta s _ {i}.
$$

设点 $(\xi_{i},\eta_{i})$ 对应于参数值 $\tau_{i}$ ，即 $\xi_{i} = \varphi (\tau_{i}),\eta_{i} = \psi (\tau_{i})$ ，这里 $t_{i - 1}\leqslant \tau_i\leqslant t_i.$ 由于

$$
\Delta s _ {i} = \int_ {t _ {i - 1}} ^ {t _ {i}} \sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)} \mathrm{d} t,
$$

应用积分中值定理,有

$$
\Delta s _ {i} = \sqrt {\varphi^ {\prime 2} (\tau_ {i} ^ {\prime}) + \psi^ {\prime 2} (\tau_ {i} ^ {\prime})} \Delta t _ {i},
$$

其中 $\Delta t_{i} = t_{i} - t_{i - 1},t_{i - 1}\leqslant \tau_{i}^{\prime}\leqslant t_{i}.$ 于是

$$
\int_ {L} f (x, y) \mathrm{d} s = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f [ \varphi (\tau_ {i}), \psi (\tau_ {i}) ] \sqrt {\varphi^ {\prime 2} (\tau_ {i} ^ {\prime}) + \psi^ {\prime 2} (\tau_ {i} ^ {\prime})} \Delta t _ {i}.
$$

由于函数 $\sqrt{\varphi'^2(t) + \psi'^2(t)}$ 在闭区间 $[\alpha, \beta]$ 上连续，我们可以把上式中的 $\tau_i'$ 换成 $\tau_i①$ ，从而

$$
\int_ {L} f (x, y) \mathrm{d} s = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f [ \varphi (\tau_ {i}), \psi (\tau_ {i}) ] \sqrt {\varphi^ {\prime 2} (\tau_ {i}) + \psi^ {\prime 2} (\tau_ {i})} \Delta t _ {i}.
$$

上式右端的和的极限就是函数 $f[\varphi(t),\psi(t)]\sqrt{\varphi'^{2}(t)+\psi'^{2}(t)}$ 在区间 $[\alpha,\beta]$ 上的定积分，因为这个函数在 $[\alpha,\beta]$ 上连续，所以这个定积分是存在的，因此上式左端的曲线积分 $\int_{L}f(x,y)\mathrm{d}s$ 也存在，并且有

$$
\int_ {L} f (x, y) \mathrm{d} s = \int_ {\alpha} ^ {\beta} f [ \varphi (t), \psi (t) ] \sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)} \mathrm{d} t (\alpha <   \beta). \tag {1-1}
$$

公式(1-1)表明,计算对弧长的曲线积分 $\int_{L}f(x,y)\mathrm{d}s$ 时,只要把 x,y,ds 依次换为 $\varphi(t),\psi(t),\sqrt{\varphi'^{2}(t)+\psi'^{2}(t)}\mathrm{d}t$ ,然后从 $\alpha$ 到 $\beta$ 作定积分就行了,这里必须注意,定积分的下限 $\alpha$ 一定要小于上限 $\beta$ .这是因为,从上述推导中可以看出,由于小弧段的长度 $\Delta s_{i}$ 总是正的,从而 $\Delta t_{i}>0$ ,所以定积分的下限 $\alpha$ 一定小于上限 $\beta$ .

如果曲线弧 $L$ 由方程

$$
y = \psi (x) \quad (x _ {0} \leqslant x \leqslant X)
$$

给出,那么可以把这种情形看做是特殊的参数方程

$$
x = t, \quad y = \psi (t) \quad (x _ {0} \leqslant t \leqslant X)
$$

的情形,从而由公式(1-1)得出

$$
\int_ {L} f (x, y) \mathrm{d} s = \int_ {x _ {0}} ^ {X} f [ x, \psi (x) ] \sqrt {1 + \psi^ {\prime 2} (x)} \mathrm{d} x \quad (x _ {0} <   X). \tag {1-2}
$$

类似地,如果曲线弧 L 由方程

$$
x = \varphi (y) \quad (y _ {0} \leqslant y \leqslant Y)
$$

给出,那么有

$$
\int_ {L} f (x, y) \mathrm{d} s = \int_ {y _ {0}} ^ {Y} f [ \varphi (y), y ] \sqrt {1 + \varphi^ {\prime 2} (y)} \mathrm{d} y \quad (y _ {0} <   Y). \tag {1-3}
$$

公式(1-1)可推广到空间曲线弧 $\Gamma$ 由参数方程

$$
x = \varphi (t), \quad y = \psi (t), \quad z = \omega (t) \quad (\alpha \leqslant t \leqslant \beta)
$$

给出的情形,这时有

$$
\int_ {\Gamma} f (x, y, z) \mathrm{d} s = \int_ {\alpha} ^ {\beta} f [ \varphi (t), \psi (t), \omega (t) ] \sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t) + \omega^ {\prime 2} (t)} \mathrm{d} t \quad (\alpha <   \beta). \tag {1-4}
$$

例 1 计算 $\int_{L}\sqrt{y}ds$ ，其中 L 是抛物线 $y=x^{2}$ 上点 $O(0,0)$ 与点 $B(1,1)$ 之间的一段弧（图 11-2）.

解 由于 $L$ 由方程 $y = x^{2}$ （ $0 \leqslant x \leqslant 1$ ）给出，因此

$$
\int_ {L} \sqrt {y} \mathrm{d} s = \int_ {0} ^ {1} \sqrt {x ^ {2}} \sqrt {1 + (x ^ {2}) ^ {\prime 2}} \mathrm{d} x = \int_ {0} ^ {1} x \sqrt {1 + 4 x ^ {2}} \mathrm{d} x = \left[ \frac {1}{1 2} (1 + 4 x ^ {2}) ^ {3 / 2} \right] _ {0} ^ {1} = \frac {1}{1 2} (5 \sqrt {5} - 1).
$$

例 2 计算半径为 R、中心角为 $2\alpha$ 的圆弧 L 对于它的对称轴的转动惯量 I（设线密度 $\mu=1$ ）.

解 取坐标系如图 11-3 所示, 则

$$
I = \int_ {L} y ^ {2} \mathrm{d} s.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/ab7fac223bb62efcc80814e328ff4369bfc269e1f7ea80bc3b0113829d4dd302.jpg)



图11-2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/6a26f940720336dc58e310cce08707f1a899ae3106a84e8d89f1c4506d60b302.jpg)



图11-3


为了便于计算,利用 L 的参数方程

$$
x = R \cos \theta , \quad y = R \sin \theta \quad (- \alpha \leqslant \theta \leqslant \alpha).
$$

于是

$$
\begin{array}{l} I = \int_ {L} y ^ {2} \mathrm{d} s = \int_ {- \alpha} ^ {\alpha} R ^ {2} \sin^ {2} \theta \sqrt {(- R \sin \theta) ^ {2} + (R \cos \theta) ^ {2}} \mathrm{d} \theta \\ = R ^ {3} \int_ {- \alpha} ^ {\alpha} \sin^ {2} \theta \mathrm{d} \theta = \frac {R ^ {3}}{2} \left[ \theta - \frac {\sin 2 \theta}{2} \right] _ {- \alpha} ^ {\alpha} = \frac {R ^ {3}}{2} (2 \alpha - \sin 2 \alpha) = R ^ {3} (\alpha - \sin \alpha \cos \alpha). \\ \end{array}
$$

例3 计算曲线积分 $\int_{\Gamma} (x^{2} + y^{2} + z^{2}) \, \mathrm{d}s$ ，其中 $\Gamma$ 为螺旋线 $x = a \cos t, y = a \sin t, z = kt$ 上相应于 $t$ 从0到 $2\pi$ 的一段弧.

解 $\int_{\Gamma}\left(x^{2} + y^{2} + z^{2}\right)\mathrm{d}s$ 

$$
\begin{array}{l} = \int_ {0} ^ {2 \pi} [ (a \cos t) ^ {2} + (a \sin t) ^ {2} + (k t) ^ {2} ] \sqrt {(- a \sin t) ^ {2} + (a \cos t) ^ {2} + k ^ {2}} d t \\ = \int_ {0} ^ {2 \pi} \left(a ^ {2} + k ^ {2} t ^ {2}\right) \sqrt {a ^ {2} + k ^ {2}} \mathrm{d} t = \sqrt {a ^ {2} + k ^ {2}} \left[ a ^ {2} t + \frac {k ^ {2}}{3} t ^ {3} \right] _ {0} ^ {2 \pi} \\ = \frac {2}{3} \pi \sqrt {a ^ {2} + k ^ {2}} (3 a ^ {2} + 4 \pi^ {2} k ^ {2}). \\ \end{array}
$$

# 习题11-1

1. 设在 $xOy$ 面内有一分布着质量的曲线弧 $L$ , 在点 $(x, y)$ 处它的线密度为 $\mu(x, y)$ . 用对弧长的曲线积分分别表达:

(1) 这曲线弧对 x 轴、对 y 轴的转动惯量 $I_{x}, I_{y}$ ;

(2) 这曲线弧的质心坐标 $\overline{x}, \overline{y}$ .

2. 利用对弧长的曲线积分的定义证明性质 3.

3. 计算下列对弧长的曲线积分：

(1) $\oint_{L} (x^{2} + y^{2})^{n} \mathrm{d}s$ , 其中 $L$ 为圆周 $x = a \cos t, y = a \sin t (0 \leqslant t \leqslant 2\pi)$ ;

(2) $\int_{L}(x+y)\mathrm{d}s$ ,其中L为连接(1,0)及(0,1)两点的直线段;

(3) $\oint_{L}x\,ds$ ,其中L为由直线y=x及抛物线 $y=x^{2}$ 所围成的区域的整个边界;

(4) $\oint_{L} \mathrm{e}^{\sqrt{x^{2} + y^{2}}} \mathrm{~d}s$ , 其中 $L$ 为圆周 $x^{2} + y^{2} = a^{2}$ , 直线 $y = x$ 及 $x$ 轴在第一象限内所围成的扇形的整个边界;

(5) $\int_{\Gamma} \frac{1}{x^2 + y^2 + z^2} \mathrm{d}s$ ，其中 $\Gamma$ 为曲线 $x = e^t \cos t, y = e^t \sin t, z = e^t$ 上相应于 $t$ 从 0 变到 2 的这段弧；

(6) $\int_{\Gamma} x^{2} y z \mathrm{~ds}$ , 其中 $\Gamma$ 为折线 $ABCD$ , 这里 $A, B, C, D$ 依次为点 $(0,0,0), (0,0,2), (1,0,2), (1,3,2)$ ;

(7) $\int_{L}y^{2}ds$ ,其中L为摆线的一拱 $x=a(t-\sin t)$ , $y=a(1-\cos t)$ ( $0\leqslant t\leqslant2\pi$ );

(8) $\int_{L}(x^{2}+y^{2})\mathrm{d}s$ ，其中L为曲线 $x=a(\cos t+t\sin t)$ ， $y=a(\sin t-t\cos t)$ （ $0\leqslant t\leqslant2\pi$ ）.

4. 求半径为 a、圆心角为 $2\varphi$ 的均匀圆弧（线密度 $\mu=1$ ）的质心.

5. 设螺旋形弹簧一圈的方程为 $x = a\cos t, y = a\sin t, z = kt$ ，其中 $0 \leqslant t \leqslant 2\pi$ ，它的线密度 $\rho(x, y, z) = x^2 + y^2 + z^2$ 。求：

(1) 它关于 z 轴的转动惯量 $I_{z}$ ;

(2) 它的质心.

# 第二节 对坐标的曲线积分

# 一、对坐标的曲线积分的概念与性质

变力沿曲线所做的功 设一个质点在 $xOy$ 面内受到力

$$
\boldsymbol {F} (x, y) = P (x, y) \boldsymbol {i} + Q (x, y) \boldsymbol {j}
$$

的作用,从点 A 沿光滑曲线弧 L 移动到点 B,其中函数 $P(x,y)$ 与 $Q(x,y)$ 在 L 上连续.要计算在上述移动过程中变力 $F(x,y)$ 所做的功(图 11-4).

我们知道,如果力 F 是恒力,且质点从 A 沿直线移动到 B,那么恒力 F 所做的功 W 等于向量 F 与向量 $\overrightarrow{AB}$ 的数量积,即

$$
W = F \cdot \overrightarrow {A B}.
$$

现在 $F(x,y)$ 是变力,且质点沿曲线 L 移动,功 W 不能直接按以上公式计算.然而第一节中用来处理曲线形构件质量问题的方法,原则上也适用于目前的问题.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/314d338cf27b0da8899cd191c7e3eb3cb9e209a8829d62612ffd41c2b6788b69.jpg)



图11-4


先用曲线弧 L 上的点 $M_{1}(x_{1},y_{1}), M_{2}(x_{2},y_{2}), \cdots, M_{n-1}(x_{n-1},y_{n-1})$ 把 L 分成 n 个小弧段，取其中一个有向小弧段 $\widehat{M_{i-1}M_{i}}$ 来分析：由于 $\widehat{M_{i-1}M_{i}}$ 光滑而且很短，可以用有向线段

$$
\overrightarrow {M _ {i - 1} M _ {i}} = (\Delta x _ {i}) i + (\Delta y _ {i}) j
$$

来近似代替它,其中 $\Delta x_{i}=x_{i}-x_{i-1},\Delta y_{i}=y_{i}-y_{i-1}$ . 又由于函数 $P(x,y)$ 与 $Q(x,y)$ 在 L 上连续,可以用 $\widehat{M_{i-1}M_{i}}$ 上任意取定的一点 $(\xi_{i},\eta_{i})$ 处的力

$$
\boldsymbol {F} \left(\xi_ {i}, \eta_ {i}\right) = P \left(\xi_ {i}, \eta_ {i}\right) \boldsymbol {i} + Q \left(\xi_ {i}, \eta_ {i}\right) \boldsymbol {j}
$$

来近似代替这小弧段上各点处的力.这样,变力 $F(x,y)$ 沿有向小弧段 $M_{i-1}M_{i}$ 所做的功 $\Delta W_{i}$ 可以认为近似地等于恒力 $F(\xi_{i},\eta_{i})$ 沿 $\overrightarrow{M_{i-1}M_{i}}$ 所做的功:

$$
\Delta W _ {i} \approx F (\xi_ {i}, \eta_ {i}) \cdot \overrightarrow {M _ {i - 1} M _ {i}},
$$

即

$$
\Delta W _ {i} \approx P (\xi_ {i}, \eta_ {i}) \Delta x _ {i} + Q (\xi_ {i}, \eta_ {i}) \Delta y _ {i}.
$$

于是

$$
W = \sum_ {i = 1} ^ {n} \Delta W _ {i} \approx \sum_ {i = 1} ^ {n} \left[ P (\xi_ {i}, \eta_ {i}) \Delta x _ {i} + Q (\xi_ {i}, \eta_ {i}) \Delta y _ {i} \right].
$$

用 $\lambda$ 表示 $n$ 个小弧段的最大长度, 令 $\lambda \to 0$ 取上述和的极限, 所得到的极限自然地被认作变力 $F$ 沿有向曲线弧所做的功, 即

$$
W = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} [ P (\xi_ {i}, \eta_ {i}) \Delta x _ {i} + Q (\xi_ {i}, \eta_ {i}) \Delta y _ {i} ].
$$

这种和的极限在研究其他问题时也会遇到.现在引进下面的定义:

定义 设 L 为 xOy 面内从点 A 到点 B 的一条有向光滑曲线弧, 函数 $P(x,y)$ 与 $Q(x,y)$ 在 L 上有界. 在 L 上沿 L 的方向任意插入一点列 $M_{1}(x_{1},y_{1}), M_{2}(x_{2},y_{2}), \cdots, M_{n-1}(x_{n-1},y_{n-1})$ , 把 L 分成 n 个有向小弧段

$$
\widehat {M _ {i - 1} M _ {i}} \quad (i = 1, 2, \dots , n; M _ {0} = A, M _ {n} = B).
$$

设 $\Delta x_{i}=x_{i}-x_{i-1},\Delta y_{i}=y_{i}-y_{i-1}$ ，点 $(\xi_{i},\eta_{i})$ 为 $\widehat{M_{i-1}M_{i}}$ 上任意取定的点，作乘积 $P(\xi_{i},\eta_{i})\Delta x_{i}$ $(i=1,2,\cdots,n)$ ，并作和 $\sum_{i=1}^{n}P(\xi_{i},\eta_{i})\Delta x_{i}$ ，如果当各小弧段长度的最大值 $\lambda\to0$ 时，这和的极限总存在，且与曲线弧 L 的分法及点 $(\xi_{i},\eta_{i})$ 的取法无关，那么称此极限为函数 $P(x,y)$ 在有向曲线弧 L 上对坐标 x 的曲线积分，记作 $\int_{L}P(x,y)\mathrm{d}x$ 。类似地，如果 $\lim_{\lambda\to0}\sum_{i=1}^{n}Q(\xi_{i},\eta_{i})\Delta y_{i}$ 总存在，且与曲线弧 L 的分法及点 $(\xi_{i},\eta_{i})$ 的取法无关，那么称此极限为函数 $Q(x,y)$ 在有向曲线弧 L 上对坐标 y 的曲线积分，记作 $\int_{L}Q(x,y)\mathrm{d}y$ 。即

$$
\int_ {L} P (x, y) \mathrm{d} x = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} P (\xi_ {i}, \eta_ {i}) \Delta x _ {i},
$$

$$
\int_ {L} Q (x, y) \mathrm{d} y = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} Q (\xi_ {i}, \eta_ {i}) \Delta y _ {i},
$$

其中 $P(x,y)$ , $Q(x,y)$ 叫做被积函数, L 叫做积分弧段.

以上两个积分也称为第二类曲线积分.

在第二目中我们将看到, 当 $P(x,y)$ 与 $Q(x,y)$ 在有向光滑曲线弧 L 上连续时, 对坐标的曲线积分 $\int_{L} P(x,y) \, dx$ 及 $\int_{L} Q(x,y) \, dy$ 都存在. 以后我们总假定 $P(x,y)$ 与 $Q(x,y)$ 在 L 上连续.

上述定义可以类似地推广到积分弧段为空间有向曲线弧 $\Gamma$ 的情形：

$$
\begin{array}{l} \int_ {\Gamma} P (x, y, z) \mathrm{d} x = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} P (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \Delta x _ {i}, \\ \int_ {\Gamma} Q (x, y, z) \mathrm{d} y = \lim _ {\lambda \to 0} \sum_ {i = 1} ^ {n} Q (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \Delta y _ {i}, \\ \end{array}
$$

$$
\int_ {\Gamma} R (x, y, z) \mathrm{d} z = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} R (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \Delta z _ {i}.
$$

应用上经常出现的是

$$
\int_ {L} P (x, y) \mathrm{d} x + \int_ {L} Q (x, y) \mathrm{d} y
$$

这种合并起来的形式,为简便起见,把上式写成

$$
\int_ {L} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y,
$$

也可写成向量形式

$$
\int_ {L} \boldsymbol {F} (x, y) \cdot \mathrm{d} \boldsymbol {r},
$$

其中 $F(x,y)=P(x,y)i+Q(x,y)j$ 为向量值函数, $dr=dxi+dyj$ .

例如,本目开始时讨论过的变力 F 所做的功可以表达成

$$
W = \int_ {L} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y,
$$

或

$$
W = \int_ {L} \boldsymbol {F} (x, y) \cdot \mathrm{d} \boldsymbol {r}.
$$

类似地, 把

$$
\int_ {\Gamma} P (x, y, z) \mathrm{d} x + \int_ {\Gamma} Q (x, y, z) \mathrm{d} y + \int_ {\Gamma} R (x, y, z) \mathrm{d} z
$$

简写成

$$
\int_ {\Gamma} P (x, y, z) \mathrm{d} x + Q (x, y, z) \mathrm{d} y + R (x, y, z) \mathrm{d} z,
$$

或

$$
\int_ {\Gamma} \boldsymbol {A} (x, y, z) \cdot \mathrm{d} \boldsymbol {r},
$$

其中 $A(x,y,z) = P(x,y,z)i + Q(x,y,z)\pmb {j} + R(x,y,z)\pmb {k},\mathrm{d}\pmb {r} = \mathrm{d}x\pmb {i} + \mathrm{d}y\pmb {j} + \mathrm{d}z\pmb{k}.$ 

如果 $L$ （或 $\Gamma$ )是分段光滑的，我们规定函数在有向曲线弧 $L$ （或 $\Gamma$ )上对坐标的曲线积分等于在光滑的各段上对坐标的曲线积分之和.

根据上述曲线积分的定义,可以导出对坐标的曲线积分的一些性质.为了表达简便起见,我们用向量形式表达,并假定其中的向量值函数在曲线 L 上连续①.

# 性质1 设 $\alpha$ 与 $\beta$ 为常数, 则

$$
\int_ {L} \left[ \alpha F _ {1} (x, y) + \beta F _ {2} (x, y) \right] \cdot \mathrm{d} r = \alpha \int_ {L} F _ {1} (x, y) \cdot \mathrm{d} r + \beta \int_ {L} F _ {2} (x, y) \cdot \mathrm{d} r.
$$

性质2 若有向曲线弧 $L$ 可分成两段光滑的有向曲线弧 $L_{1}$ 和 $L_{2}$ , 则

$$
\int_ {L} \boldsymbol {F} (x, y) \cdot \mathrm{d} \boldsymbol {r} = \int_ {L _ {1}} \boldsymbol {F} (x, y) \cdot \mathrm{d} \boldsymbol {r} + \int_ {L _ {2}} \boldsymbol {F} (x, y) \cdot \mathrm{d} \boldsymbol {r}.
$$

性质3 设 $L$ 是有向光滑曲线弧, $L^{-}$ 是 $L$ 的反向曲线弧, 则

$$
\int_ {L ^ {-}} \boldsymbol {F} (x, y) \cdot \mathrm{d} \boldsymbol {r} = - \int_ {L} \boldsymbol {F} (x, y) \cdot \mathrm{d} \boldsymbol {r}.
$$

证 把 $L$ 分成 $n$ 小段, 相应的 $L^{-}$ 也分成 $n$ 小段. 对于每一个小弧段来说, 当曲线弧的方向改变时, 有向弧段在坐标轴上的投影, 其绝对值不变, 但要改变符号, 因此性质3成立.

性质 3 表示, 当积分弧段的方向改变时, 对坐标的曲线积分要改变符号. 因此关于对坐标的曲线积分, 我们必须注意积分弧段的方向.

这一性质是对坐标的曲线积分所特有的,对弧长的曲线积分不具有这一性质.而对弧长的曲线积分所具有的性质3,对坐标的曲线积分也不具有类似的性质.

# 二、对坐标的曲线积分的计算法

定理 设 $P(x,y)$ 与 $Q(x,y)$ 在有向曲线弧 $L$ 上有定义且连续， $L$ 的参数方程为

$$
\left\{ \begin{array}{l} x = \varphi (t), \\ y = \psi (t), \end{array} \right.
$$

当参数 $t$ 单调地由 $\alpha$ 变到 $\beta$ 时，点 $M(x, y)$ 从 $L$ 的起点 $A$ 沿 $L$ 运动到终点 $B$ ，若 $\varphi(t)$ 与 $\psi(t)$ 在以 $\alpha$ 及 $\beta$ 为端点的闭区间上具有一阶连续导数，且 $\varphi'^2(t) + \psi'^2(t) \neq 0$ 则曲线积分 $\int_{L} P(x, y) \mathrm{d}x + Q(x, y) \mathrm{d}y$ 存在，且

$$
\begin{array}{l} \int_ {L} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y \\ = \int_ {\alpha} ^ {\beta} \left\{P [ \varphi (t), \psi (t) ] \varphi^ {\prime} (t) + Q [ \varphi (t), \psi (t) ] \psi^ {\prime} (t) \right\} d t. \tag {2-1} \\ \end{array}
$$

证 在 $L$ 上取一点列

$$
A = M _ {0}, M _ {1}, M _ {2}, \dots , M _ {n - 1}, M _ {n} = B,
$$

它们对应于一列单调变化的参数值

$$
\alpha = t _ {0}, t _ {1}, t _ {2}, \dots , t _ {n - 1}, t _ {n} = \beta .
$$

根据对坐标的曲线积分的定义,有

$$
\int_ {L} P (x, y) \mathrm{d} x = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} P (\xi_ {i}, \eta_ {i}) \Delta x _ {i}.
$$

设点 $(\xi_{i},\eta_{i})$ 对应于参数值 $\tau_{i}$ ，即 $\xi_{i} = \varphi (\tau_{i}),\eta_{i} = \psi (\tau_{i})$ ，这里 $\tau_{i}$ 在 $t_{i - 1}$ 与 $t_i$ 之间.由于

$$
\Delta x _ {i} = x _ {i} - x _ {i - 1} = \varphi (t _ {i}) - \varphi (t _ {i - 1}),
$$

应用微分中值定理,有

$$
\Delta x _ {i} = \varphi^ {\prime} \left(\tau_ {i} ^ {\prime}\right) \Delta t _ {i},
$$

其中 $\Delta t_{i} = t_{i} - t_{i - 1},\tau_{i}^{\prime}$ 在 $t_{i - 1}$ 与 $t_i$ 之间.于是

$$
\int_ {L} P (x, y) \mathrm{d} x = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} P [ \varphi (\tau_ {i}), \psi (\tau_ {i}) ] \varphi^ {\prime} (\tau_ {i} ^ {\prime}) \Delta t _ {i}.
$$

因为函数 $\varphi'(t)$ 在闭区间 $[\alpha, \beta]$ （或 $[\beta, \alpha]$ ）上连续，我们可以把上式中的 $\tau_i'$ 换成 $\tau_i^{①}$ ，从而

$$
\int_ {L} P (x, y) \mathrm{d} x = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} P [ \varphi (\tau_ {i}), \psi (\tau_ {i}) ] \varphi^ {\prime} (\tau_ {i}) \Delta t _ {i}.
$$

上式右端的和的极限就是定积分 $\int_{\alpha}^{\beta} P[\varphi(t), \psi(t)] \varphi'(t) \mathrm{d}t$ ，由于函数 $P[\varphi(t), \psi(t)] \varphi'(t)$ 连续，这个定积分是存在的，因此上式左端的曲线积分 $\int_{L} P(x, y) \mathrm{d}x$ 也存在，并且有

$$
\int_ {L} P (x, y) \mathrm{d} x = \int_ {\alpha} ^ {\beta} P [ \varphi (t), \psi (t) ] \varphi^ {\prime} (t) \mathrm{d} t.
$$

同理可证

$$
\int_ {L} Q (x, y) \mathrm{d} y = \int_ {\alpha} ^ {\beta} Q [ \varphi (t), \psi (t) ] \psi^ {\prime} (t) \mathrm{d} t,
$$

把以上两式相加,得

$$
\int_ {L} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y = \int_ {\alpha} ^ {\beta} \left\{P [ \varphi (t), \psi (t) ] \varphi^ {\prime} (t) + Q [ \varphi (t), \psi (t) ] \psi^ {\prime} (t) \right\} \mathrm{d} t,
$$

这里下限 $\alpha$ 对应于 L 的起点, 上限 $\beta$ 对应于 L 的终点.

公式(2-1)表明,计算对坐标的曲线积分

$$
\int_ {L} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y
$$

时, 只要把 $x, y, \mathrm{d}x, \mathrm{d}y$ 依次换为 $\varphi(t), \psi(t), \varphi'(t) \mathrm{d}t, \psi'(t) \mathrm{d}t$ , 然后从 $L$ 的起点所对应的参数值 $\alpha$ 到 $L$ 的终点所对应的参数值 $\beta$ 作定积分就行了, 这里必须注意, 下限 $\alpha$ 对应于 $L$ 的起点, 上限 $\beta$ 对应于 $L$ 的终点, $\alpha$ 不一定小于 $\beta$ .

如果 L 由方程 $y=\psi(x)$ 或 $x=\varphi(y)$ 给出, 可以看做参数方程的特殊情形, 例如, 当 L 由 $y=\psi(x)$ 给出时, 公式(2-1) 成为

$$
\int_ {L} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y = \int_ {a} ^ {b} \left\{P [ x, \psi (x) ] + Q [ x, \psi (x) ] \psi^ {\prime} (x) \right\} \mathrm{d} x,
$$

这里下限 a 对应 L 的起点, 上限 b 对应 L 的终点.

公式(2-1)可推广到空间曲线 $\Gamma$ 由参数方程

$$
x = \varphi (t), \quad y = \psi (t), \quad z = \omega (t)
$$

给出的情形,这样便得到

$$
\begin{array}{l} \int_ {\Gamma} P (x, y, z) \mathrm{d} x + Q (x, y, z) \mathrm{d} y + R (x, y, z) \mathrm{d} z \\ = \int_ {\alpha} ^ {\beta} \left\{P [ \varphi (t), \psi (t), \omega (t) ] \varphi^ {\prime} (t) + Q [ \varphi (t), \psi (t), \omega (t) ] \psi^ {\prime} (t) + \right. \\ R [ \varphi (t), \psi (t), \omega (t) ] \omega^ {\prime} (t) \} d t, \\ \end{array}
$$

这里下限 $\alpha$ 对应 $\Gamma$ 的起点, 上限 $\beta$ 对应 $\Gamma$ 的终点.

例1 计算 $\int_{L} xy \, \mathrm{d}x$ ，其中 $L$ 为抛物线 $y^{2} = x$ 上从点 $A(1, -1)$ 到点 $B(1, 1)$ 的一段弧（图11-5）.

解法一 将所给积分化为对 $x$ 的定积分来计算. 由于 $y = \pm \sqrt{x}$ 不是单值函数, 所以要把 $L$ 分为 $AO$ 和 $OB$ 两部分. 在 $AO$ 上, $y = -\sqrt{x}, x$ 从 1 变到 0; 在 $OB$ 上, $y = \sqrt{x}, x$ 从 0 变到 1. 因此

$$
\begin{array}{l} \int_ {L} x y \mathrm{d} x = \int_ {A O} x y \mathrm{d} x + \int_ {O B} x y \mathrm{d} x \\ = \int_ {1} ^ {0} x (- \sqrt {x}) \mathrm{d} x + \int_ {0} ^ {1} x \sqrt {x} \mathrm{d} x = 2 \int_ {0} ^ {1} x ^ {\frac {3}{2}} \mathrm{d} x = \frac {4}{5}. \\ \end{array}
$$

解法二 将所给积分化为对 y 的定积分来计算, 现在 $x = y^{2}$ , y 从 -1 变到 1. 因此

$$
\int_ {L} x y \mathrm{d} x = \int_ {- 1} ^ {1} y ^ {2} y (y ^ {2}) ^ {\prime} \mathrm{d} y = 2 \int_ {- 1} ^ {1} y ^ {4} \mathrm{d} y = 2 \left[ \frac {y ^ {5}}{5} \right] _ {- 1} ^ {1} = \frac {4}{5}.
$$

例2 计算 $\int_{L} y^{2} \mathrm{~d} x$ 其中 $L$ 为（图11-6）：

(1) 半径为 a、圆心为原点、按逆时针方向绕行的上半圆周；

(2) 从点 A(a,0) 沿 x 轴到点 B(-a,0) 的直线段.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/9f4bf65a705d2cb37a22089b576b862148b5f9a2e86b8cf0498bf84a5065a444.jpg)



图11-5


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/952368bd91d64b838cadcf1bb44291c904ff5f97f164ab20b55a791d5f64ff5e.jpg)



图11-6


解 (1) $L$ 是参数方程

$$
x = a \cos \theta , \quad y = a \sin \theta
$$

当参数 $\theta$ 从 0 变到 $\pi$ 的曲线弧. 因此

$$
\begin{array}{l} \int_ {L} y ^ {2} \mathrm{d} x = \int_ {0} ^ {\pi} a ^ {2} \sin^ {2} \theta (- a \sin \theta) \mathrm{d} \theta = a ^ {3} \int_ {0} ^ {\pi} (1 - \cos^ {2} \theta) \mathrm{d} (\cos \theta) \\ = a ^ {3} \left[ \cos \theta - \frac {\cos^ {3} \theta}{3} \right] _ {0} ^ {\pi} = - \frac {4}{3} a ^ {3}. \\ \end{array}
$$

(2) $L$ 的方程为 $y = 0, x$ 从 $a$ 变到 $-a$ . 所以

$$
\int_ {L} y ^ {2} \mathrm{d} x = \int_ {a} ^ {- a} 0 \mathrm{d} x = 0.
$$

从例 2 看出,虽然两个曲线积分的被积函数相同,起点和终点也相同,但沿不同路径得出的积分值并不相等.

例3 计算 $\int_{L} 2xy\mathrm{d}x + x^{2}\mathrm{d}y$ ，其中 $L$ 为（图11-7）：

(1) 抛物线 $y=x^{2}$ 上从 $O(0,0)$ 到 $B(1,1)$ 的一段弧；

(2) 抛物线 $x=y^{2}$ 上从 $O(0,0)$ 到 $B(1,1)$ 的一段弧；

(3) 有向折线 OAB, 这里 O, A, B 依次是点 $(0,0)$ , $(1,0)$ , $(1,1)$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/f1db31f01d81e4cdf615be3d6cf62edcf251f9e896ef6c17bc8d55e6390163b1.jpg)



图11-7


解 （1）化为对 x 的定积分. $L: y = x^{2}$ , x 从 0 变到 1. 所以

$$
\int_ {L} 2 x y \mathrm{d} x + x ^ {2} \mathrm{d} y = \int_ {0} ^ {1} (2 x \cdot x ^ {2} + x ^ {2} \cdot 2 x) \mathrm{d} x = 4 \int_ {0} ^ {1} x ^ {3} \mathrm{d} x = 1.
$$

(2) 化为对 y 的定积分. $L: x = y^{2}, y$ 从 0 变到 1. 所以

$$
\int_ {L} 2 x y \mathrm{d} x + x ^ {2} \mathrm{d} y = \int_ {0} ^ {1} (2 y ^ {2} \cdot y \cdot 2 y + y ^ {4}) \mathrm{d} y = 5 \int_ {0} ^ {1} y ^ {4} \mathrm{d} y = 1.
$$

(3) $\int_{L} 2xy\mathrm{d}x + x^{2}\mathrm{d}y = \int_{OA} 2xy\mathrm{d}x + x^{2}\mathrm{d}y + \int_{AB} 2xy\mathrm{d}x + x^{2}\mathrm{d}y,$ 

在 OA 上, y=0, x 从 0 变到 1, 所以

$$
\int_ {O A} 2 x y \mathrm{d} x + x ^ {2} \mathrm{d} y = \int_ {0} ^ {1} (2 x \cdot 0 + x ^ {2} \cdot 0) \mathrm{d} x = 0.
$$

在 $AB$ 上, $x = 1, y$ 从0变到1, 所以

$$
\int_ {A B} 2 x y \mathrm{d} x + x ^ {2} \mathrm{d} y = \int_ {0} ^ {1} (2 y \cdot 0 + 1) \mathrm{d} y = 1.
$$

从而

[NO TEXT] 

释疑解难

11-2 

$$
\int_ {L} 2 x y \mathrm{d} x + x ^ {2} \mathrm{d} y = 0 + 1 = 1.
$$

从例 3 可以看出,虽然沿不同路径,曲线积分的值可以相等.

例4 计算 $\int_{\Gamma} x^{3} \mathrm{~d} x + 3 z y^{2} \mathrm{~d} y - x^{2} y \mathrm{~d} z$ ，其中 $\Gamma$ 是从点 $A(3,2,1)$ 到点 $B(0,0,0)$ 的直线段 $AB$ .

解 直线段 $AB$ 的方程是

$$
\frac {x}{3} = \frac {y}{2} = \frac {z}{1},
$$

化为参数方程得

$x = 3t$ ， $y = 2t$ ， $z = t$ ， $t$ 从1变到0.

所以

$$
\begin{array}{l} \int_ {\Gamma} x ^ {3} \mathrm{d} x + 3 z y ^ {2} \mathrm{d} y - x ^ {2} y \mathrm{d} z \\ = \int_ {1} ^ {0} [ (3 t) ^ {3} \cdot 3 + 3 t (2 t) ^ {2} \cdot 2 - (3 t) ^ {2} \cdot 2 t ] d t = 8 7 \int_ {1} ^ {0} t ^ {3} d t = - \frac {8 7}{4}. \\ \end{array}
$$

例 5 设一个质点在点 $M(x,y)$ 处受到力 F 的作用, F 的大小与点 M 到原点 O 的距离成正比, F 的方向恒指向原点. 此质点由点 A(a,0) 沿椭圆 $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1$ 按逆时针方向移动到点 B(0,b), 求力 F 所做的功 W.

解

$$
\overrightarrow {O M} = x \boldsymbol {i} + y \boldsymbol {j}, \quad | \overrightarrow {O M} | = \sqrt {x ^ {2} + y ^ {2}}.
$$

由假设有 $F = -k(xi + yj)$ ，其中 k > 0 是比例常数。于是

$$
W = \int_ {\widehat {A B}} \boldsymbol {F} \cdot \mathrm{d} \boldsymbol {r} = \int_ {\widehat {A B}} - k x \mathrm{d} x - k y \mathrm{d} y = - k \int_ {\widehat {A B}} x \mathrm{d} x + y \mathrm{d} y.
$$

利用椭圆的参数方程 $\left\{ \begin{array}{l} x = a\cos t, \\ y = b\sin t, \end{array} \right.$ 起点 $A$ 、终点 $B$ 分别对应参数 $t = 0, t = \frac{\pi}{2}$ . 于是

$$
\begin{array}{l} W = - k \int_ {0} ^ {\frac {\pi}{2}} (- a ^ {2} \cos t \sin t + b ^ {2} \sin t \cos t) d t \\ = k \left(a ^ {2} - b ^ {2}\right) \int_ {0} ^ {\frac {\pi}{2}} \sin t \cos t d t = \frac {k}{2} \left(a ^ {2} - b ^ {2}\right). \\ \end{array}
$$

# 三、两类曲线积分之间的联系

设有向曲线弧 L 的起点为 A, 终点为 B. 曲线弧 L 由参数方程

$$
\left\{ \begin{array}{l} x = \varphi (t), \\ y = \psi (t) \end{array} \right.
$$

给出, 起点 A 与终点 B 分别对应参数 $\alpha$ 与 $\beta$ . 不妨设 $\alpha < \beta$ (若 $\alpha > \beta$ , 可令 s = -t, A, B 对应 $s = -\alpha, s = -\beta$ , 就有 $(-\alpha) < (-\beta)$ , 把下面的讨论对参数 s 进行即可), 并设函数 $\varphi(t)$ 与 $\psi(t)$ 在闭区间 $[\alpha, \beta]$ 上具有一阶连续导数, 且 $\varphi'^{2}(t) + \psi'^{2}(t) \neq 0$ , 又函数 $P(x, y)$ 与 $Q(x, y)$ 在 L 上连续. 于是, 由对坐标的曲线积分计算公式 (2-1) 有

$$
\int_ {L} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y = \int_ {\alpha} ^ {\beta} \left\{P [ \varphi (t), \psi (t) ] \varphi^ {\prime} (t) + Q [ \varphi (t), \psi (t) ] \psi^ {\prime} (t) \right\} \mathrm{d} t.
$$

我们知道,向量 $\tau=\varphi'(t)i+\psi'(t)j$ 是曲线弧 L 在点 $M(\varphi(t),\psi(t))$ 处的一个切向量,它的方向与参数 t 的增长方向一致,当 $\alpha<\beta$ 时,这个方向就是有向曲线弧 L 的方向.以后,我们称这种方向与有向曲线弧的方向一致的切向量为有向曲线弧的切向量.于是,有向曲线弧 L 的切向量为

$$
\boldsymbol {\tau} = \varphi^ {\prime} (t) \boldsymbol {i} + \psi^ {\prime} (t) \boldsymbol {j},
$$

它的方向余弦为

$$
\cos \alpha = \frac {\varphi^ {\prime} (t)}{\sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)}}, \quad \cos \beta = \frac {\psi^ {\prime} (t)}{\sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)}}.
$$

由对弧长的曲线积分的计算公式可得

$$
\begin{array}{l} \int_ {L} [ P (x, y) \cos \alpha + Q (x, y) \cos \beta ] d s \\ = \int_ {\alpha} ^ {\beta} \left\{P [ \varphi (t), \psi (t) ] \frac {\varphi^ {\prime} (t)}{\sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)}} + \right. \\ Q [ \varphi (t), \psi (t) ] \frac {\psi^ {\prime} (t)}{\sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)}} \Bigg \} \sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t)} d t \\ = \int_ {\alpha} ^ {\beta} \left\{P [ \varphi (t), \psi (t) ] \varphi^ {\prime} (t) + Q [ \varphi (t), \psi (t) ] \psi^ {\prime} (t) \right\} d t. \\ \end{array}
$$

由此可见，平面曲线弧 L 上的两类曲线积分之间有如下联系：

$$
\int_ {L} P \mathrm{d} x + Q \mathrm{d} y = \int_ {L} (P \cos \alpha + Q \cos \beta) \mathrm{d} s, \tag {2-2}
$$

其中 $\alpha(x,y)$ 与 $\beta(x,y)$ 为有向曲线弧 L 在点 $(x,y)$ 处的切向量的方向角.

类似地可知,空间曲线弧 $\Gamma$ 上的两类曲线积分之间有如下联系:

$$
\int_ {\Gamma} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z = \int_ {\Gamma} (P \cos \alpha + Q \cos \beta + R \cos \gamma) \mathrm{d} s, \tag {2-3}
$$

其中 $\alpha(x,y,z)$ , $\beta(x,y,z)$ , $\gamma(x,y,z)$ 为有向曲线弧 $\Gamma$ 在点 $(x,y,z)$ 处的切向量的方向角.

两类曲线积分之间的联系也可用向量的形式表达.例如,空间曲线弧 $\Gamma$ 上的两类曲线积分之间的联系可写成如下形式:

$$
\int_ {\Gamma} \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {r} = \int_ {\Gamma} \boldsymbol {A} \cdot \boldsymbol {\tau} \mathrm{d} s \tag {2-4}
$$

或

$$
\int_ {\Gamma} \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {r} = \int_ {\Gamma} A _ {\tau} \mathrm{d} s, \tag {$2-4^{\prime$}}
$$

其中 $A = (P, Q, R)$ , $\tau = (\cos \alpha, \cos \beta, \cos \gamma)$ 为有向曲线弧 $\Gamma$ 在点 $(x, y, z)$ 处的单位切向量, $\mathrm{d}r = \tau \mathrm{d}s = (\mathrm{d}x, \mathrm{d}y, \mathrm{d}z)$ , 称为有向曲线元, $A_{\tau}$ 为向量 $A$ 在向量 $\tau$ 上的投影.

# 习题11-2

1. 设 L 为 xOy 面内直线 x=a 上的一段, 证明: $\int_{L} P(x,y) \, dx = 0$ .

2. 设 L 为 xOy 面内 x 轴上从点 $(a,0)$ 到点 $(b,0)$ 的一段直线，证明： $\int_{L} P(x,y) \, dx = \int_{a}^{b} P(x,0) \, dx$ .

3. 计算下列对坐标的曲线积分：

(1) $\int_{L}(x^{2}-y^{2})\mathrm{d}x$ ,其中L是抛物线 $y=x^{2}$ 上从点(0,0)到点(2,4)的一段弧；

(2) $\oint_{L}xy\,dx$ ，其中L为圆周 $(x-a)^{2}+y^{2}=a^{2}$ （a>0）及x轴所围成的在第一象限内的区域的整个边界（按逆时针方向绕行）；

(3) $\int_{L}ydx+xdy$ ，其中L为圆周 $x=R\cos t,y=R\sin t$ 上对应t从0到 $\frac{\pi}{2}$ 的一段弧；

(4) $\oint_{L} \frac{(x + y) \mathrm{d}x - (x - y) \mathrm{d}y}{x^2 + y^2}$ , 其中 $L$ 为圆周 $x^2 + y^2 = a^2$ （按逆时针方向绕行）；

(5) $\int_{\Gamma} x^{2} \mathrm{d}x + z \mathrm{d}y - y \mathrm{d}z$ ，其中 $\Gamma$ 为曲线 $x = k\theta, y = a\cos \theta, z = a\sin \theta$ 上对应 $\theta$ 从0到 $\pi$ 的一段弧；

(6) $\int_{\Gamma}x\mathrm{d}x+y\mathrm{d}y+(x+y-1)\mathrm{d}z$ ，其中 $\Gamma$ 是从点(1,1,1)到点(2,3,4)的一段直线；

(7) $\oint_{\Gamma} \mathrm{d}x - \mathrm{d}y + y \mathrm{d}z$ ，其中 $\Gamma$ 为有向闭折线 $ABCA$ ，这里的 $A, B, C$ 依次为点 $(1,0,0), (0,1,0), (0,0,1)$ ；

(8) $\int_{L}(x^{2}-2xy)\mathrm{d}x+(y^{2}-2xy)\mathrm{d}y$ ，其中L是抛物线 $y=x^{2}$ 上从点 $(-1,1)$ 到点 $(1,1)$ 的一段弧.

4. 计算 $\int_{L} (x + y) \, \mathrm{d}x + (y - x) \, \mathrm{d}y$ ，其中 $L$ 是

(1) 抛物线 $y^{2}=x$ 上从点 $(1,1)$ 到点 $(4,2)$ 的一段弧；

(2) 从点 $(1,1)$ 到点 $(4,2)$ 的直线段；

(3) 先沿直线从点(1,1)到点(1,2)，然后再沿直线到点(4,2)的折线；

(4) 曲线 $x=2t^{2}+t+1, y=t^{2}+1$ 上从点 $(1,1)$ 到点 $(4,2)$ 的一段弧.

5. 一力场由沿横轴正方向的恒力 F 所构成. 试求当一质量为 m 的质点沿圆周 $x^{2} + y^{2} = R^{2}$ 按逆时针方向移过位于第一象限的那一段弧时场力所做的功.

6. 设 z 轴与重力的方向一致, 求质量为 m 的质点从位置 $(x_{1}, y_{1}, z_{1})$ 沿直线移到 $(x_{2}, y_{2}, z_{2})$ 时重力所做的功.

7. 把对坐标的曲线积分 $\int_{L} P(x, y) \, dx + Q(x, y) \, dy$ 化成对弧长的曲线积分, 其中 L 为

(1) 在 xOy 面内沿直线从点 $(0,0)$ 到点 $(1,1)$ ;

(2) 沿抛物线 $y=x^{2}$ 从点 $(0,0)$ 到点 $(1,1)$ ;

(3) 沿上半圆周 $x^{2}+y^{2}=2x$ 从点 $(0,0)$ 到点 $(1,1)$ .

8. 设 $\Gamma$ 为曲线 $x = t, y = t^2, z = t^3$ 上相应于 $t$ 从0变到1的曲线弧，把对坐标的曲线积分 $\int_{\Gamma} P \mathrm{~d} x +$ 

$Qdy+Rdz$ 化成对弧长的曲线积分.

9. 设曲线 $\Gamma$ 为球面 $x^{2} + y^{2} + z^{2} = a^{2}$ 与平面 $x + y + z = 0$ 的交线，从 $z$ 轴的正向看取逆时针方向，

$$
I = \oint_ {\Gamma} z \mathrm{d} x + x \mathrm{d} y + y \mathrm{d} z,
$$

试利用两类曲线积分之间的关系证明： $|I|\leqslant2\pi a^{2}$ 

# 第三节 格林公式及其应用

# 一、格林公式

在一元函数积分学中,牛顿-莱布尼茨公式

$$
\int_ {a} ^ {b} F ^ {\prime} (x) \mathrm{d} x = F (b) - F (a)
$$

表示: $F'(x)$ 在区间 $[a,b]$ 上的积分可以通过它的原函数 $F(x)$ 在这个区间端点上的值来表达.

下面要介绍的格林(Green)公式告诉我们,在平面闭区域 D 上的二重积分可以通过沿闭区域 D 的边界曲线 L 上的曲线积分来表达.

现在先介绍平面单连通区域的概念.设 D 为平面区域,若 D 内任一闭曲线所围的部分都属于 D,则称 D 为平面单连通区域,否则称为复连通区域.通俗地说,平面单连通区域就是不含有“洞”(包括点“洞”)的区域,复连通区域是含有“洞”(包括点“洞”)的区域.例如,平面上的圆形区域 $\{(x,y)\mid x^{2}+y^{2}<1\}$ 、上半平面 $\{(x,y)\mid y>0\}$ 都是单连通区域,圆环形区域 $\{(x,y)\mid1<x^{2}+y^{2}<4\},\{(x,y)\mid0<x^{2}+y^{2}<2\}$ 都是复连通区域.

对平面区域 D 的边界曲线 L, 我们规定 L 的正向如下: 当观察者沿 L 的这个方向行走时, D 内在他近处的那一部分总在他的左边. 例如, D 是边界曲线 L 及 l 所围成的复连通区域(图 11-8), 作为 D 的正向边界, L 的正向是逆时针方向, 而 l 的正向是顺时针方向.

定理1 设闭区域 $D$ 由分段光滑的曲线 $L$ 围成, 若函数 $P(x, y)$ 及 $Q(x, y)$ 在 $D$ 上具有一阶连续偏导数, 则有

$$
\iint_ {D} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y = \oint_ {L} P \mathrm{d} x + Q \mathrm{d} y, \tag {3-1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/b3fd9e079241bff8e8572471a30e157facc3e64851c5e9638908dccb6e392463.jpg)



图11-8


其中 L 是 D 的取正向的边界曲线.

公式(3-1)叫做格林公式.

证 先假设穿过区域 D 内部且平行于坐标轴的直线与 D 的边界曲线 L 的交点恰好为两点, 即区域 D 既是 X 型又是 Y 型的情形.

图 11-9、图 11-10 所示的区域都属于这种情形.例如,图 11-9 所示的区域 D 显然是 X 型的,事实上 D 又是 Y 型的.若设有向曲线弧 FGAE 为 $L_{1}^{\prime}: x = \psi_{1}(y)$ , EBCF 为 $L_{2}^{\prime}: x = \psi_{2}(y)$ , 则 D 可表达成

$$
D = \{(x, y) | \psi_ {1} (y) \leqslant x \leqslant \psi_ {2} (y), c \leqslant y \leqslant d \},
$$

即 D 又是 Y 型的.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/19c0fdf0c1efce599f111dc8604d95c007360d6db52cb44728ea0f26b4a0d2fb.jpg)



图11-9


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/43fd96a3d412124adf29f5aac63db0c1b5e61f60afdf3ecbcbb41d675e69a246.jpg)



图11-10


设 $D$ 如图11-9所示, 于是 $D = \{(x, y) \mid \varphi_1(x) \leqslant y \leqslant \varphi_2(x), a \leqslant x \leqslant b\}$ . 因为 $\frac{\partial P}{\partial y}$ 连续, 所以由二重积分的计算法有

$$
\iint_ {D} \frac {\partial P}{\partial y} \mathrm{d} x \mathrm{d} y = \int_ {a} ^ {b} \left\{\int_ {\varphi_ {1} (x)} ^ {\varphi_ {2} (x)} \frac {\partial P (x , y)}{\partial y} \mathrm{d} y \right\} \mathrm{d} x = \int_ {a} ^ {b} \left\{P [ x, \varphi_ {2} (x) ] - P [ x, \varphi_ {1} (x) ] \right\} \mathrm{d} x.
$$

另一方面，由对坐标的曲线积分的性质及计算法有

$$
\begin{array}{l} \oint_ {L} P \mathrm{d} x = \int_ {L _ {1}} P \mathrm{d} x + \int_ {B C} P \mathrm{d} x + \int_ {L _ {2}} P \mathrm{d} x + \int_ {G A} P \mathrm{d} x \\ = \int_ {L _ {1}} P \mathrm{d} x + \int_ {L _ {2}} P \mathrm{d} x = \int_ {a} ^ {b} P [ x, \varphi_ {1} (x) ] \mathrm{d} x + \int_ {b} ^ {a} P [ x, \varphi_ {2} (x) ] \mathrm{d} x \\ = \int_ {a} ^ {b} \left\{P [ x, \varphi_ {1} (x) ] - P [ x, \varphi_ {2} (x) ] \right\} d x, \\ \end{array}
$$

因此，

$$
- \iint_ {D} \frac {\partial P}{\partial y} \mathrm{d} x \mathrm{d} y = \oint_ {L} P \mathrm{d} x. \tag {3-2}
$$

又由于 $D = \{(x,y)\mid \psi_1(y)\leqslant x\leqslant \psi_2(y),c\leqslant y\leqslant d\}$ ，故有

$$
\begin{array}{l} \iint_ {D} \frac {\partial Q}{\partial x} \mathrm{d} x \mathrm{d} y = \int_ {c} ^ {d} \left[ \int_ {\psi_ {1} (y)} ^ {\psi_ {2} (y)} \frac {\partial Q}{\partial x} \mathrm{d} x \right] \mathrm{d} y = \int_ {c} ^ {d} \left\{Q [ \psi_ {2} (y), y ] - Q [ \psi_ {1} (y), y ] \right\} \mathrm{d} y \\ = \int_ {L _ {2} ^ {\prime}} Q \mathrm{d} y + \int_ {L _ {1} ^ {\prime}} Q \mathrm{d} y = \oint_ {L} Q \mathrm{d} y. \tag {3-3} \\ \end{array}
$$

由于对区域 $D$ , 式(3-2)与(3-3)同时成立, 合并后即得公式(3-1). 对于如图 11-10

所示的区域 D, 完全类似地可证(3-1)成立.

再考虑一般情形.如果闭区域 D 不满足以上条件,那么可以在 D 内引进一条或几条辅助曲线把 D 分成有限个部分闭区域,使得每个部分闭区域都满足上述条件.例如,就图 11-11 所示的闭区域 D 来说,它的边界曲线 L 为 MNPM,引进一条辅助线 ABC,把 D 分成 $D_{1}, D_{2}, D_{3}$ 三部分. 应用公式(3-1)于每个部分, 得

$$
\iint_ {D _ {1}} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) d x d y = \oint_ {\widehat {M C B A M}} P d x + Q d y,
$$

$$
\iint_ {D _ {2}} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y = \oint_ {\widehat {A B P A}} P \mathrm{d} x + Q \mathrm{d} y,
$$

$$
\iint_ {D _ {3}} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) d x d y = \oint_ {\widehat {B C N B}} P d x + Q d y.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/77d83b456c4f46483878698f74301871619750db853cb92a9aa98c9a8f01bd55.jpg)



图11-11


把这三个等式相加,注意到相加时沿辅助线来回的曲线积分相互抵消,便得

$$
\iint_ {D} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y = \oint_ {L} P \mathrm{d} x + Q \mathrm{d} y,
$$

其中 L 的方向对 D 来说为正方向. 一般地, 公式(3-1)对于由分段光滑曲线围成的闭区域都成立. 证毕.

注意,对于复连通区域 D,格林公式(3-1)右端应包括沿区域 D 的全部边界的曲线积分,且边界的方向对区域 D 来说都是正向.

下面说明格林公式的一个简单应用.

在公式(3-1)中取 $P = -y, Q = x$ ，即得

$$
2 \iint_ {D} \mathrm{d} x \mathrm{d} y = \oint_ {L} x \mathrm{d} y - y \mathrm{d} x.
$$

上式左端是闭区域 D 的面积 A 的 2 倍, 因此有

$$
A = \frac {1}{2} \oint_ {L} x \mathrm{d} y - y \mathrm{d} x. \tag {3-4}
$$

例1 计算 $\oint_{L} x^{2} y \, \mathrm{d}x - xy^{2} \, \mathrm{d}y$ ，其中 $L$ 为正向圆周 $x^{2} + y^{2} = a^{2}$ .

解 令 $P = x^{2}y, Q = -xy^{2}$ , 则

$$
\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y} = - y ^ {2} - x ^ {2}.
$$

因此,由公式(3-1)有

$$
\oint_ {L} x ^ {2} y \mathrm{d} x - x y ^ {2} \mathrm{d} y = - \iint_ {D} (x ^ {2} + y ^ {2}) \mathrm{d} x \mathrm{d} y = - \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {a} \rho^ {3} \mathrm{d} \rho = - \frac {\pi}{2} a ^ {4}.
$$

例 2 计算 $\iint_{D} e^{-y^{2}} dx dy$ ，其中 D 是以 $O(0,0)$ ， $A(1,1)$ ， $B(0,1)$ 为顶点的三角形闭区域（图 11-12）.

解 令 $P = 0, Q = x\mathrm{e}^{-y^2}$ , 则

$$
\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y} = e ^ {- y ^ {2}}.
$$

因此,由公式(3-1)有

$$
\begin{array}{l} \iint_ {D} \mathrm{e} ^ {- y ^ {2}} \mathrm{d} x \mathrm{d} y = \int_ {O A + A B + B O} x \mathrm{e} ^ {- y ^ {2}} \mathrm{d} y = \int_ {O A} x \mathrm{e} ^ {- y ^ {2}} \mathrm{d} y \\ = \int_ {0} ^ {1} x \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x = \frac {1}{2} (1 - \mathrm{e} ^ {- 1}). \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/ceb60301c2d2841bc30424fbf3ecc6760e7354e58451befc16353ae790209ab3.jpg)



图11-12


例 3 求椭圆 $x = a \cos \theta, y = b \sin \theta$ 所围成图形的面积 A.

解 根据公式(3-4)有

$$
A = \frac {1}{2} \oint_ {L} x \mathrm{d} y - y \mathrm{d} x = \frac {1}{2} \int_ {0} ^ {2 \pi} (a b \cos^ {2} \theta + a b \sin^ {2} \theta) \mathrm{d} \theta = \frac {1}{2} a b \int_ {0} ^ {2 \pi} \mathrm{d} \theta = \pi a b.
$$

例 4 计算 $\oint_{L}\frac{xdy-ydx}{x^{2}+y^{2}}$ ，其中 L 为一条不自相交①、分段光滑且不经过原点的连续闭曲线，L 的方向为逆时针方向.

解 令 $P = \frac{-y}{x^2 + y^2}, Q = \frac{x}{x^2 + y^2}$ . 则当 $x^2 + y^2 \neq 0$ 时, 有

$$
\frac {\partial Q}{\partial x} = \frac {y ^ {2} - x ^ {2}}{\left(x ^ {2} + y ^ {2}\right) ^ {2}} = \frac {\partial P}{\partial y}.
$$

记 L 所围成的闭区域为 D. 当 $(0,0) \notin D$ 时, 由公式 $(3-1)$ 便得

$$
\oint_ {L} \frac {x \mathrm{d} y - y \mathrm{d} x}{x ^ {2} + y ^ {2}} = 0;
$$

当 $(0,0)\in D$ 时，选取适当小的 $r > 0$ ，作位于 $D$ 内的圆周 $l$ ： $x^{2} + y^{2} = r^{2}$ .记 $L$ 和 $l$ 所围成的闭区域为 $D_{1}$ （图11-13).对复连通区域 $D_{1}$ 应用格林公式，得

$$
\oint_ {L} \frac {x \mathrm{d} y - y \mathrm{d} x}{x ^ {2} + y ^ {2}} - \oint_ {l} \frac {x \mathrm{d} y - y \mathrm{d} x}{x ^ {2} + y ^ {2}} = 0,
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/8da1dc8d8209a32f77623548fac9d31a609049d3ceec4248f079ca35403319e3.jpg)



图11-13


其中 l 的方向取逆时针方向. 于是

$$
\oint_ {L} \frac {x \mathrm{d} y - y \mathrm{d} x}{x ^ {2} + y ^ {2}} = \oint_ {l} \frac {x \mathrm{d} y - y \mathrm{d} x}{x ^ {2} + y ^ {2}} = \int_ {0} ^ {2 \pi} \frac {r ^ {2} \cos^ {2} \theta + r ^ {2} \sin^ {2} \theta}{r ^ {2}} \mathrm{d} \theta = 2 \pi .
$$

# 二、平面上曲线积分与路径无关的条件

在物理、力学中要研究所谓势场,就是要研究场力所做的功与路径无关的情形.在什么条件下场力所做的功与路径无关？这个问题在数学上就是要研究曲线积分与路径无关的条件。为了研究这个问题，先要明确什么叫做曲线积分 $\int_{L} P \mathrm{~d} x + Q \mathrm{~d} y$ 与路径无关。

设 $G$ 是一个区域, $P(x,y)$ 以及 $Q(x,y)$ 在区域 $G$ 内具有一阶连续偏导数. 如果对于 $G$ 内任意指定的两个点 $A,B$ 以及 $G$ 内从点 $A$ 到点 $B$ 的任意两条曲线 $L_{1}, L_{2}$ (图11-14), 等式

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/a566d76d48b230a08d9f688a52f9c0d2fe5492b338e5e9a96f6f8f5ece7f0065.jpg)



图11-14


$$
\int_ {L _ {1}} P \mathrm{d} x + Q \mathrm{d} y = \int_ {L _ {2}} P \mathrm{d} x + Q \mathrm{d} y
$$

恒成立,就说曲线积分 $\int_{L}Pdx+Qdy$ 在 G 内与路径无关,否则便说与路径有关.

在以上叙述中注意到,如果曲线积分与路径无关,那么

$$
\int_ {L _ {1}} P \mathrm{d} x + Q \mathrm{d} y = \int_ {L _ {2}} P \mathrm{d} x + Q \mathrm{d} y.
$$

由于

$$
\int_ {L _ {2}} P \mathrm{d} x + Q \mathrm{d} y = - \int_ {L _ {2} ^ {-}} P \mathrm{d} x + Q \mathrm{d} y,
$$

所以

$$
\int_ {L _ {1}} P \mathrm{d} x + Q \mathrm{d} y + \int_ {L _ {2} ^ {-}} P \mathrm{d} x + Q \mathrm{d} y = 0,
$$

从而

$$
\oint_ {L _ {1} + L _ {2} ^ {-}} P \mathrm{d} x + Q \mathrm{d} y = 0,
$$

这里 $L_{1} + L_{2}^{-}$ 是一条有向闭曲线. 因此, 在区域 $G$ 内由曲线积分与路径无关可推得在 $G$ 内沿闭曲线的曲线积分为零. 反过来, 如果在区域 $G$ 内沿任意闭曲线的曲线积分为零, 也可推得在 $G$ 内曲线积分与路径无关. 由此得出结论: 曲线积分 $\int_{L} P \mathrm{~d} x + Q \mathrm{~d} y$ 在 $G$ 内与路径无关相当于沿 $G$ 内任意闭曲线 $C$ 的曲线积分 $\oint_{C} P \mathrm{~d} x + Q \mathrm{~d} y$ 等于零.

定理2 设区域 $G$ 是一个单连通区域, 若函数 $P(x, y)$ 与 $Q(x, y)$ 在 $G$ 内具有一阶连续偏导数, 则曲线积分 $\int_{L} P \mathrm{~d} x + Q \mathrm{~d} y$ 在 $G$ 内与路径无关 (或沿 $G$ 内任意闭曲线的曲线积分为零) 的充分必要条件是

$$
\frac {\partial P}{\partial y} = \frac {\partial Q}{\partial x} \tag {3-5}
$$

在 $G$ 内恒成立.

证 先证条件(3-5)是充分的.在 $G$ 内任取一条闭曲线 $C$ , 要证当条件(3-5)成立时有 $\oint_{C} P \mathrm{d}x + Q \mathrm{d}y = 0$ . 因为 $G$ 是单连通的, 所以闭曲线 $C$ 所围成的闭区域 $D$ 全部在 $G$ 内, 于是(3-5)式在 $D$ 上恒成立. 应用格林公式, 有

$$
\iint_ {D} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y = \oint_ {C} P \mathrm{d} x + Q \mathrm{d} y.
$$

上式左端的二重积分等于零（因为被积函数 $\frac{\partial Q}{\partial x} -\frac{\partial P}{\partial y}$ 在 $D$ 上恒为零），从而右端的曲线积分也等于零.

再证条件(3-5)是必要的.现在要证的是:如果沿G内任意闭曲线的曲线积分为零,那么(3-5)式在G内恒成立.用反证法来证.假设上述论断不成立,那么G内至少有一点 $M_{0}$ ,使

$$
\left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) _ {M _ {0}} \neq 0.
$$

不妨假定

$$
\left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) _ {M _ {0}} = \eta > 0.
$$

由于 $\frac{\partial P}{\partial y}$ 与 $\frac{\partial Q}{\partial x}$ 在 $G$ 内连续，可以在 $G$ 内取得一个以 $M_0$ 为圆心、半径足够小的圆形闭区域 $K$ ，使得在 $K$ 上恒有

$$
\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y} \geqslant \frac {\eta}{2}.
$$

于是由格林公式及二重积分的性质就有

$$
\oint_ {\gamma} P \mathrm{d} x + Q \mathrm{d} y = \iint_ {K} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y \geqslant \frac {\eta}{2} \cdot \sigma ,
$$

这里 $\gamma$ 是 K 的正向边界曲线, $\sigma$ 是 K 的面积. 因为 $\eta > 0, \sigma > 0$ , 从而

$$
\oint_ {\gamma} P \mathrm{d} x + Q \mathrm{d} y > 0.
$$

这结果与沿 G 内任意闭曲线的曲线积分为零的假定相矛盾, 可见 G 内使 $(3-5)$ 式不成立的点不可能存在, 即 $(3-5)$ 式在 G 内处处成立. 证毕.

在第二节第二目例3中我们看到，起点与终点相同的三个曲线积分 $\int_{L}2xy\mathrm{d}x + x^{2}\mathrm{d}y$ 相等.由定理2来看,这不是偶然的,因为这里 $\frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y}=2x$ 在整个xOy面内恒成立,而整个xOy面是单连通区域,因此曲线积分 $\int_{L}2xydx+x^{2}dy$ 与路径无关.

在定理2中,要求区域G是单连通区域,且函数 $P(x,y)$ 与 $Q(x,y)$ 在G内具有一阶连续偏导数.如果这两个条件之一不能满足,那么定理的结论不能保证成立.例如,在例4中我们已经看到,当L所围成的区域含有原点时,虽然除去原点外,恒有 $\frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y}$ ,但沿闭曲线的积分 $\oint_{L}Pdx+Qdy\neq0$ ,其原因在于区域内含有破坏函数P,Q及 $\frac{\partial Q}{\partial x}$ , $\frac{\partial P}{\partial y}$ 连续性条件的点O,这种点通常称为奇点.

# 三、二元函数的全微分求积

现在要讨论: 函数 $P(x,y)$ 与 $Q(x,y)$ 满足什么条件时, 表达式 $P(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y$ 才是某个二元函数 $u(x,y)$ 的全微分; 当这样的二元函数存在时把它求出来.

定理3 设区域 $G$ 是一个单连通区域, 若函数 $P(x, y)$ 与 $Q(x, y)$ 在 $G$ 内具有一阶连续偏导数, 则 $P(x, y) \mathrm{d}x + Q(x, y) \mathrm{d}y$ 在 $G$ 内为某一函数 $u(x, y)$ 的全微分的充分必要条件是

$$
\frac {\partial P}{\partial y} = \frac {\partial Q}{\partial x} \tag {3-5}
$$

在 $G$ 内恒成立.

证 先证必要性. 假设存在着某一函数 $u(x, y)$ , 使得

$$
\mathrm{d} u = P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y,
$$

则必有

$$
\frac {\partial u}{\partial x} = P (x, y), \quad \frac {\partial u}{\partial y} = Q (x, y).
$$

从而

$$
\frac {\partial^ {2} u}{\partial x \partial y} = \frac {\partial P}{\partial y}, \quad \frac {\partial^ {2} u}{\partial y \partial x} = \frac {\partial Q}{\partial x}.
$$

由于 $P$ 与 $Q$ 具有一阶连续偏导数, 所以 $\frac{\partial^2 u}{\partial x \partial y}$ 与 $\frac{\partial^2 u}{\partial y \partial x}$ 连续, 因此 $\frac{\partial^2 u}{\partial x \partial y} = \frac{\partial^2 u}{\partial y \partial x}$ , 即 $\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$ . 这就证明了条件(3-5)是必要的.

再证充分性. 设已知条件 (3-5) 在 $G$ 内恒成立, 则由定理 2 可知, 起点为 $M_0(x_0, y_0)$ , 终点为 $M(x, y)$ 的曲线积分在区域 $G$ 内与路径无关, 于是可把这条曲线积

分写作

$$
\int_ {(x _ {0}, y _ {0})} ^ {(x, y)} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y.
$$

当起点 $M_0(x_0, y_0)$ 固定时，这个积分的值取决于终点 $M(x, y)$ ，因此，它与 $x$ 及 $y$ 构成函数关系，把这个函数记作 $u(x, y)$ ，即

$$
u (x, y) = \int_ {(x _ {0}, y _ {0})} ^ {(x, y)} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y ①. \tag {3-6}
$$

下面来证明这个函数 $u(x,y)$ 的全微分就是 $P(x,y)\mathrm{d}x + Q(x,y)\mathrm{d}y.$ 因为 $P(x,y)$ 与 $Q(x,y)$ 都是连续的，因此只要证明

$$
\frac {\partial u}{\partial x} = P (x, y), \quad \frac {\partial u}{\partial y} = Q (x, y).
$$

按偏导数的定义,有

$$
\frac {\partial u}{\partial x} = \lim _ {\Delta x \rightarrow 0} \frac {u (x + \Delta x , y) - u (x , y)}{\Delta x}.
$$

由(3-6)式,得

$$
u (x + \Delta x, y) = \int_ {(x _ {0}, y _ {0})} ^ {(x + \Delta x, y)} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y.
$$

由于这里的曲线积分与路径无关,可以取先从点 $M_{0}$ 到点 M,然后沿平行于 x 轴的直线段从点 M 到点 N 作为上式右端曲线积分的路径(图 11-15).这样就有

$$
\begin{array}{l} u (x + \Delta x, y) \\ = u (x, y) + \int_ {(x, y)} ^ {(x + \Delta x, y)} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y. \\ \end{array}
$$

从而

$$
u (x + \Delta x, y) - u (x, y) = \int_ {(x, y)} ^ {(x + \Delta x, y)} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/8ce5b32e-a303-46e5-9623-7e7f1ba46d7e/8a686a79767399584dc5145d22d4de7fc605fff14a2b59db89ca5839ace7ab4a.jpg)



图11-15


因为直线段 MN 的方程为 y= 常数, 按对坐标的曲线积分的计算法, 上式成为

$$
u (x + \Delta x, y) - u (x, y) = \int_ {x} ^ {x + \Delta x} P (x, y) \mathrm{d} x.
$$

应用定积分中值定理,得

$$
u (x + \Delta x, y) - u (x, y) = P (x + \theta \Delta x, y) \Delta x \quad (0 \leqslant \theta \leqslant 1).
$$

上式两端除以 $\Delta x$ ，并令 $\Delta x \to 0$ 取极限。由于 $P(x, y)$ 的偏导数在 $G$ 内连续， $P(x, y)$ 本身也一定连续，于是得

① 为区别函数的自变量与积分变量,可记

$$
u (x, y) = \int_ {(x _ {0}, y _ {0})} ^ {(x, y)} P (s, t) \mathrm{d} s + Q (s, t) \mathrm{d} t.
$$