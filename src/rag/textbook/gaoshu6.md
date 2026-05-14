$$
\begin{array}{l} u (x, y) = \int_ {(1, 0)} ^ {(x, y)} \frac {x \mathrm{d} y - y \mathrm{d} x}{x ^ {2} + y ^ {2}} = \int_ {A B} \frac {x \mathrm{d} y - y \mathrm{d} x}{x ^ {2} + y ^ {2}} + \int_ {B C} \frac {x \mathrm{d} y - y \mathrm{d} x}{x ^ {2} + y ^ {2}} \\ = 0 + \int_ {0} ^ {y} \frac {x \mathrm{d} y}{x ^ {2} + y ^ {2}} = \left[ \arctan \frac {y}{x} \right] _ {0} ^ {y} = \arctan \frac {y}{x}. \\ \end{array}
$$

例 6 验证: 在整个 xOy 面内, $xy^{2}dx + x^{2}ydy$ 是某个函数的全微分, 并求出一个这样的函数.

解 现在 $P = xy^{2}, Q = x^{2}y$ ，且

$$
\frac {\partial P}{\partial y} = 2 x y = \frac {\partial Q}{\partial x}
$$

在整个 $xOy$ 面内恒成立, 因此在整个 $xOy$ 面内, $xy^{2} \mathrm{~d} x + x^{2} y \mathrm{~d} y$ 是某个函数的全微分. 取积分路线如图11-18所示, 利用公式(3-6)得所求函数为

$$
\begin{array}{l} u (x, y) = \int_ {(0, 0)} ^ {(x, y)} x y ^ {2} \mathrm{d} x + x ^ {2} y \mathrm{d} y = \int_ {O A} x y ^ {2} \mathrm{d} x + x ^ {2} y \mathrm{d} y + \int_ {A B} x y ^ {2} \mathrm{d} x + x ^ {2} y \mathrm{d} y \\ = 0 + \int_ {0} ^ {y} x ^ {2} y \mathrm{d} y = x ^ {2} \int_ {0} ^ {y} y \mathrm{d} y = \frac {x ^ {2} y ^ {2}}{2}. \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/324efa4ac9f4b00d44dbcd6ff953da226e564ddb653e7d122457e62de70c239e.jpg)



图11-17


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/bcf821a0fb94ffc3e03a3af9717c5a9767dbba7dec27b58770b950f53db8acb9.jpg)



图11-18


* 全微分方程

利用二元函数的全微分求积,还可以用来求解下面一类一阶微分方程.

一个微分方程写成

$$
P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y = 0 \tag {3-7}
$$

的形式后,如果它的左端恰好是某一个函数 $u(x,y)$ 的全微分:

$$
\mathrm{d} u (x, y) = P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y,
$$

那么方程(3-7)就叫做全微分方程.

容易知道,如果方程(3-7)的左端是函数 $u(x,y)$ 的全微分,那么

$$
u (x, y) = C
$$

就是全微分方程(3-7)的隐式通解,其中C是任意常数.

由定理 3 及公式(3-6)可知, 当 $P(x,y)$ 与 $Q(x,y)$ 在单连通区域 G 内具有一阶连续偏导数时, 方程(3-7)成为全微分方程的充分必要条件是

$$
\frac {\partial P}{\partial y} = \frac {\partial Q}{\partial x}
$$

在区域 G 内恒成立,且当此条件满足时,全微分方程(3-7)的通解为

$$
u (x, y) \equiv \int_ {(x _ {0}, y _ {0})} ^ {(x, y)} P (x, y) \mathrm{d} x + Q (x, y) \mathrm{d} y = C, \tag {3-8}
$$

其中 $x_{0}$ 与 $y_{0}$ 是在区域 G 内适当选定的点 $M_{0}$ 的坐标.

例7 求解方程

$$
\left(5 x ^ {4} + 3 x y ^ {2} - y ^ {3}\right) \mathrm{d} x + \left(3 x ^ {2} y - 3 x y ^ {2} + y ^ {2}\right) \mathrm{d} y = 0.
$$

解 设 $P(x, y) = 5x^4 + 3xy^2 - y^3, Q(x, y) = 3x^2y - 3xy^2 + y^2$ ，则

$$
\frac {\partial P}{\partial y} = 6 x y - 3 y ^ {2} = \frac {\partial Q}{\partial x},
$$

因此,所给方程是全微分方程.

取 $x_0 = 0, y_0 = 0$ ，根据公式(3-8)，有

$$
\begin{array}{l} u (x, y) = \int_ {(0, 0)} ^ {(x, y)} \left(5 x ^ {4} + 3 x y ^ {2} - y ^ {3}\right) d x + \left(3 x ^ {2} y - 3 x y ^ {2} + y ^ {2}\right) d y \\ = \int_ {0} ^ {x} 5 x ^ {4} d x + \int_ {0} ^ {y} \left(3 x ^ {2} y - 3 x y ^ {2} + y ^ {2}\right) d y = x ^ {5} + \frac {3}{2} x ^ {2} y ^ {2} - x y ^ {3} + \frac {1}{3} y ^ {3}. \\ \end{array}
$$

于是,方程的通解为

$$
x ^ {5} + \frac {3}{2} x ^ {2} y ^ {2} - x y ^ {3} + \frac {1}{3} y ^ {3} = C.
$$

除了利用公式(3-8)以外,还可以用下面的方法求解全微分方程.

以上面的方程为例.因为要求的方程通解为 $u(x,y)=C$ , 其中 $u(x,y)$ 满足

$$
\frac {\partial u}{\partial x} = 5 x ^ {4} + 3 x y ^ {2} - y ^ {3},
$$

故

$$
u (x, y) = \int (5 x ^ {4} + 3 x y ^ {2} - y ^ {3}) \mathrm{d} x = x ^ {5} + \frac {3}{2} x ^ {2} y ^ {2} - x y ^ {3} + \varphi (y),
$$

这里 $\varphi(y)$ 是以 y 为自变量的待定函数. 由此, 得

$$
\frac {\partial u}{\partial y} = 3 x ^ {2} y - 3 x y ^ {2} + \varphi^ {\prime} (y).
$$

又 $u(x,y)$ 必须满足

$$
\frac {\partial u}{\partial y} = 3 x ^ {2} y - 3 x y ^ {2} + y ^ {2}.
$$

故

$$
3 x ^ {2} y - 3 x y ^ {2} + \varphi^ {\prime} (y) = 3 x ^ {2} y - 3 x y ^ {2} + y ^ {2}.
$$

从而

$$
\varphi^ {\prime} (y) = y ^ {2}, \quad \varphi (y) = \frac {1}{3} y ^ {3} + C.
$$

所以,所给方程的通解为

$$
x ^ {5} + \frac {3}{2} x ^ {2} y ^ {2} - x y ^ {3} + \frac {1}{3} y ^ {3} = C.
$$

# * 四、曲线积分的基本定理

若曲线积分 $\int_{L} F \cdot \mathrm{d}r$ 在区域 $G$ 内与积分路径无关, 则称向量场 $F$ 为保守场.

下面的定理给出了平面曲线积分与路径无关的另一种形式的条件,并为计算保守场中的曲线积分提供了一种简便的方法.

定理4（曲线积分的基本定理）设 $F(x,y) = P(x,y)i + Q(x,y)j$ 是平面区域 $G$ 内的一个向量场，若 $P(x,y)$ 与 $Q(x,y)$ 都在 $G$ 内连续，且存在一个数量函数 $f(x,y)$ ，使得 $\pmb{F} = \nabla f$ ，则曲线积分 $\int_{L}\pmb {F}\cdot \mathrm{d}\pmb {r}$ 在 $G$ 内与路径无关，且

$$
\int_ {L} \boldsymbol {F} \cdot \mathrm{d} \boldsymbol {r} = f (B) - f (A), \tag {3-9}
$$

其中 L 是位于 G 内起点为 A、终点为 B 的任一分段光滑曲线.

证 设 L 的向量方程为

$$
\boldsymbol {r} = \varphi (t) \boldsymbol {i} + \psi (t) \boldsymbol {j}, \quad t \in [ \alpha , \beta ],
$$

起点 A 对应参数 $t=\alpha$ ，终点 B 对应参数 $t=\beta$ .

由假设, $f_{x}=P,f_{y}=Q,P,Q$ 连续,从而f可微,且

$$
\frac {\mathrm{d} f}{\mathrm{d} t} = f _ {x} \frac {\mathrm{d} x}{\mathrm{d} t} + f _ {y} \frac {\mathrm{d} y}{\mathrm{d} t} = \nabla f \cdot \left(\frac {\mathrm{d} x}{\mathrm{d} t} i + \frac {\mathrm{d} y}{\mathrm{d} t} j\right) = F \cdot \frac {\mathrm{d} r}{\mathrm{d} t},
$$

于是

$$
\int_ {L} \boldsymbol {F} \cdot \mathrm{d} \boldsymbol {r} = \int_ {\alpha} ^ {\beta} \boldsymbol {F} \cdot \frac {\mathrm{d} \boldsymbol {r}}{\mathrm{d} t} \mathrm{d} t = \int_ {\alpha} ^ {\beta} \frac {\mathrm{d} f}{\mathrm{d} t} \mathrm{d} t = f [ \varphi (t), \psi (t) ] \Bigg | _ {\alpha} ^ {\beta} = f (B) - f (A),
$$

证毕.

定理 4 表明, 对于势场 F, 曲线积分 $\int_{L} F \cdot dr$ 的值仅依赖于它的势函数 f 在路径 L 的两端点的值, 而不依赖于两点间的路径, 即积分 $\int_{L} F \cdot dr$ 在 G 内与路径无关. 也就是说: 势场是保守场.

公式(3-9)是与微积分基本公式

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - F (a)
$$

(其中 $F'(x)=f(x)$ ) 完全类似的向量微积分的相应公式, 称为曲线积分的基本公式.

# 习题11-3

1. 计算下列曲线积分,并验证格林公式的正确性:

(1) $\oint_{L} (2xy - x^{2}) \, \mathrm{d}x + (x + y^{2}) \, \mathrm{d}y$ ，其中 $L$ 是由抛物线 $y = x^{2}$ 和 $y^{2} = x$ 所围成的区域的正向边界曲线；

(2) $\oint_{L} (x^{2} - xy^{3}) \, \mathrm{d}x + (y^{2} - 2xy) \, \mathrm{d}y$ ，其中 $L$ 是四个顶点分别为 $(0,0), (2,0), (2,2)$ 和 $(0,2)$ 的正方形区域的正向边界.

2. 利用曲线积分, 求下列曲线所围成的图形的面积:

(1) 星形线 $x = a \cos^{3} t, y = a \sin^{3} t;$ 

(2) 椭圆 $9x^{2}+16y^{2}=144$ ;

(3) 圆 $x^{2}+y^{2}=2ax.$ 

3. 计算曲线积分 $\oint_{L} \frac{y \, \mathrm{d}x - x \, \mathrm{d}y}{2(x^2 + y^2)}$ ，其中 $L$ 为圆周 $(x - 1)^2 + y^2 = 2, L$ 的方向为逆时针方向.

4. 确定正向闭曲线 C，使曲线积分 $\oint_{C}\left(x+\frac{y^{3}}{3}\right)\mathrm{d}x+\left(y+x-\frac{2}{3}x^{3}\right)\mathrm{d}y$ 达到最大值.

5. 设 n 边形的 n 个顶点按逆时针方向依次为 $M_{1}(x_{1}, y_{1}), M_{2}(x_{2}, y_{2}), \cdots, M_{n}(x_{n}, y_{n})$ . 试利用曲线积分证明此 n 边形的面积为

$$
A = \frac {1}{2} \left[ \left(x _ {1} y _ {2} - x _ {2} y _ {1}\right) + \left(x _ {2} y _ {3} - x _ {3} y _ {2}\right) + \dots + \left(x _ {n - 1} y _ {n} - x _ {n} y _ {n - 1}\right) + \left(x _ {n} y _ {1} - x _ {1} y _ {n}\right) \right].
$$

6. 证明下列曲线积分在整个 $xOy$ 面内与路径无关, 并计算积分值:

(1) $\int_{(1,1)}^{(2,3)} (x + y) \mathrm{d}x + (x - y) \mathrm{d}y$ ; 

(2) $\int_{(1,2)}^{(3,4)} (6xy^2 - y^3) \mathrm{d}x + (6x^2y - 3xy^2) \mathrm{d}y$ ; 

(3) $\int_{(1,0)}^{(2,1)} (2xy - y^4 + 3) \mathrm{d}x + (x^2 - 4xy^3) \mathrm{d}y.$ 

7. 利用格林公式, 计算下列曲线积分:

(1) $\oint_{L} (2x - y + 4) \mathrm{d}x + (5y + 3x - 6) \mathrm{d}y$ ，其中 $L$ 是三顶点分别为 $(0,0), (3,0)$ 和 $(3,2)$ 的三角形正向边界；

(2) $\oint_{L} (x^{2}y\cos x + 2xy\sin x - y^{2}e^{x}) \, dx + (x^{2}\sin x - 2ye^{x}) \, dy$ ，其中 $L$ 为正向星形线 $x^{\frac{2}{3}} + y^{\frac{2}{3}} = a^{\frac{2}{3}}$ ( $a > 0$ );

(3) $\int_{L} (2xy^{3} - y^{2}\cos x) \mathrm{d}x + (1 - 2y\sin x + 3x^{2}y^{2}) \mathrm{d}y$ ，其中 $L$ 为在抛物线 $2x = \pi y^{2}$ 上由点 $(0,0)$ 到 $\left(\frac{\pi}{2}, 1\right)$ 的一段弧；

(4) $\int_{L} (x^{2} - y) \, \mathrm{d}x - (x + \sin^{2} y) \, \mathrm{d}y$ ，其中 $L$ 是在圆周 $y = \sqrt{2x - x^{2}}$ 上由点 $(0,0)$ 到点 $(1,1)$ 的一段弧.

8. 设有界闭区域 $D$ 由 $xOy$ 面上的分段光滑曲线 $L$ 所围成, 函数 $u = u(x, y)$ 在 $D$ 上具有连续的二

阶偏导数, $\frac{\partial u}{\partial n}$ 表示 $u(x,y)$ 沿L的外法向量的方向导数,证明

$$
\oint_ {L} \frac {\partial u}{\partial n} \mathrm{d} s = \iint_ {D} \left(\frac {\partial^ {2} u}{\partial x ^ {2}} + \frac {\partial^ {2} u}{\partial y ^ {2}}\right) \mathrm{d} \sigma ,
$$

其中 $L$ 取正向.

9. 验证下列 $P(x, y) \mathrm{d}x + Q(x, y) \mathrm{d}y$ 在整个 $xOy$ 面内是某一函数 $u(x, y)$ 的全微分，并求这样的一个 $u(x, y)$ ：

(1) $(x+2y)\mathrm{d}x+(2x+y)\mathrm{d}y;$ 

(2) $2xydx + x^{2}dy;$ 

(3) $4\sin x\sin 3y\cos xdx-3\cos 3y\cos 2xdy;$ 

(4) $(3x^{2}y + 8xy^{2})\mathrm{d}x + (x^{3} + 8x^{2}y + 12ye^{y})\mathrm{d}y;$ 

(5) $(2x\cos y+y^{2}\cos x)\mathrm{d}x+(2y\sin x-x^{2}\sin y)\mathrm{d}y.$ 

10. 设有一变力在坐标轴上的投影为 $X = x^{2} + y^{2}$ , Y = 2xy - 8, 这变力确定了一个力场. 证明质点在此场内移动时, 场力所做的功与路径无关.

* 11. 判别下列方程中哪些是全微分方程？对于全微分方程，求出它的通解.

(1) $(3x^{2}+6xy^{2})\mathrm{d}x+(6x^{2}y+4y^{2})\mathrm{d}y=0;$ 

(2) $(a^{2}-2xy-y^{2})\mathrm{d}x-(x+y)^{2}\mathrm{d}y=0$ (a为常数);

(3) $e^{y}dx+(xe^{y}-2y)dy=0;$ 

(4) $(x\cos y+\cos x)y'-y\sin x+\sin y=0;$ 

(5) $(x^{2}-y)\mathrm{d}x-x\mathrm{d}y=0;$ 

(6) $y(x-2y)\mathrm{d}x-x^{2}\mathrm{d}y=0;$ 

(7) $(1 + \mathrm{e}^{2\theta})\mathrm{d}\rho + 2\rho \mathrm{e}^{2\theta}\mathrm{d}\theta = 0;$ 

(8) $(x^{2}+y^{2})dx+xydy=0.$ 

12. 确定常数 $\lambda$ ，使在右半平面 $x > 0$ 上的向量 $A(x, y) = 2xy(x^4 + y^2)^{\lambda}i - x^2(x^4 + y^2)^{\lambda}j$ 为某二元函数 $u(x, y)$ 的梯度，并求 $u(x, y)$ .

# 第四节 对面积的曲面积分

# 一、对面积的曲面积分的概念与性质

在本章第一节第一目的质量问题中,如果把曲线改为曲面①,并相应地把线密度 $\mu(x,y)$ 改为面密度 $\mu(x,y,z)$ ,小段曲线的弧长 $\Delta s_{i}$ 改为小块曲面的面积 $\Delta S_{i}$ ,而第 $i$ 小段曲线上的一点 $(\xi_{i},\eta_{i})$ 改为第 $i$ 小块曲面上的一点 $(\xi_{i},\eta_{i},\zeta_{i})$ ,那么,在面密度 $\mu(x,y,z)$ 连续的前提下,所求的质量 $m$ 就是下列和的极限:

$$
m = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} \mu (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \Delta S _ {i},
$$

其中 $\lambda$ 表示 n 小块曲面的直径 $^{②}$ 的最大值.

这样的极限还会在其他问题中遇到.抽去它们的具体意义,就得出对面积的曲面

积分的概念.

定义 设曲面 $\Sigma$ 是光滑的①, 函数 $f(x,y,z)$ 在 $\Sigma$ 上有界. 把 $\Sigma$ 任意分成 n 小块 $\Delta S_{i}$ ( $\Delta S_{i}$ 同时也代表第 i 小块曲面的面积), 设 $(\xi_{i},\eta_{i},\zeta_{i})$ 是 $\Delta S_{i}$ 上任意取定的一点, 作乘积 $f(\xi_{i},\eta_{i},\zeta_{i})\Delta S_{i}$ ( $i=1,2,3,\cdots,n$ ), 并作和 $\sum_{i=1}^{n}f(\xi_{i},\eta_{i},\zeta_{i})\Delta S_{i}$ , 如果当各小块曲面的直径的最大值 $\lambda\to0$ 时, 这和的极限总存在, 且与曲面 $\Sigma$ 的分法及点 $(\xi_{i},\eta_{i},\zeta_{i})$ 的取法无关, 那么称此极限为函数 $f(x,y,z)$ 在曲面 $\Sigma$ 上对面积的曲面积分或第一类曲面积分, 记作 $\iint_{\Sigma}f(x,y,z)\mathrm{d}S$ , 即

$$
\iint_ {\Sigma} f (x, y, z) \mathrm{d} S = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \Delta S _ {i},
$$

其中 $f(x,y,z)$ 叫做被积函数, $\Sigma$ 叫做积分曲面.

我们指出, 当 $f(x,y,z)$ 在光滑曲面 $\Sigma$ 上连续时, 对面积的曲面积分是存在的. 今后总假定 $f(x,y,z)$ 在 $\Sigma$ 上连续.

根据上述定义, 面密度为连续函数 $\mu(x,y,z)$ 的光滑曲面 $\Sigma$ 的质量 m, 可表示为 $\mu(x,y,z)$ 在 $\Sigma$ 上对面积的曲面积分

$$
m = \iint_ {\Sigma} \mu (x, y, z) \mathrm{d} S.
$$

如果 $\Sigma$ 是分片光滑的②, 我们规定函数在 $\Sigma$ 上对面积的曲面积分等于函数在光滑的各片曲面上对面积的曲面积分之和. 例如, 设 $\Sigma$ 可分成两片光滑曲面 $\Sigma_{1}$ 及 $\Sigma_{2}$ (记作 $\Sigma = \Sigma_{1} + \Sigma_{2}$ ), 就规定

$$
\iint_ {\Sigma_ {1} + \Sigma_ {2}} f (x, y, z) \mathrm{d} S = \iint_ {\Sigma_ {1}} f (x, y, z) \mathrm{d} S + \iint_ {\Sigma_ {2}} f (x, y, z) \mathrm{d} S.
$$

由对面积的曲面积分的定义可知,它具有与对弧长的曲线积分相类似的性质,这里不再赘述.

# 二、对面积的曲面积分的计算法

设积分曲面 $\Sigma$ 由方程 $z = z(x, y)$ 给出， $\Sigma$ 在 $xOy$ 面上的投影区域为 $D_{xy}$ （图11-19），函数 $z = z(x, y)$ 在 $D_{xy}$ 上具有连续偏导数，被积函数 $f(x, y, z)$ 在 $\Sigma$ 上连续.

按对面积的曲面积分的定义,有

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/3bb45da6a87ff6a3244cc056dc53ddeb523201656b8aac6cd73366d342e378f8.jpg)



图11-19


$$
\iint_ {\Sigma} f (x, y, z) \mathrm{d} S = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \Delta S _ {i}. \tag {4-1}
$$

设 $\Sigma$ 上第 i 小块曲面 $\Delta S_{i}$ （它的面积也记作 $\Delta S_{i}$ ）在 xOy 面上的投影区域为 $(\Delta\sigma_{i})_{xy}$ （它的面积也记作 $(\Delta\sigma_{i})_{xy}$ ），则 (4-1) 式中的 $\Delta S_{i}$ 可表示为二重积分

$$
\Delta S _ {i} = \iint_ {(\Delta \sigma_ {i}) _ {x y}} \sqrt {1 + z _ {x} ^ {2} (x , y) + z _ {y} ^ {2} (x , y)} d x d y.
$$

利用二重积分的中值定理,上式又可写成

$$
\Delta S _ {i} = \sqrt {1 + z _ {x} ^ {2} \left(\xi_ {i} ^ {\prime} , \eta_ {i} ^ {\prime}\right) + z _ {y} ^ {2} \left(\xi_ {i} ^ {\prime} , \eta_ {i} ^ {\prime}\right)} \left(\Delta \sigma_ {i}\right) _ {x y},
$$

其中 $(\xi_i', \eta_i', 0)$ 是小闭区域 $(\Delta \sigma_i)_{xy}$ 上的一点. 又因 $(\xi_i, \eta_i, \zeta_i)$ 是 $\Sigma$ 上的一点, 故 $\zeta_i = z(\xi_i, \eta_i)$ , 这里 $(\xi_i, \eta_i, 0)$ 也是小闭区域 $(\Delta \sigma_i)_{xy}$ 上的点. 于是

$$
\sum_ {i = 1} ^ {n} f \left(\xi_ {i}, \eta_ {i}, \zeta_ {i}\right) \Delta S _ {i} = \sum_ {i = 1} ^ {n} f \left[ \xi_ {i}, \eta_ {i}, z \left(\xi_ {i}, \eta_ {i}\right) \right] \sqrt {1 + z _ {x} ^ {2} \left(\xi_ {i} ^ {\prime} , \eta_ {i} ^ {\prime}\right) + z _ {y} ^ {2} \left(\xi_ {i} ^ {\prime} , \eta_ {i} ^ {\prime}\right)} (\Delta \sigma_ {i}) _ {x y}.
$$

由于函数 $f[x,y,z(x,y)]$ 以及函数 $\sqrt{1 + z_x^2(x,y) + z_y^2(x,y)}$ 都在闭区域 $D_{xy}$ 上连续，可以证明，当 $\lambda \to 0$ 时，上式右端的极限与

$$
\sum_ {i = 1} ^ {n} f \left[ \xi_ {i}, \eta_ {i}, z \left(\xi_ {i}, \eta_ {i}\right) \right] \sqrt {1 + z _ {x} ^ {2} \left(\xi_ {i} , \eta_ {i}\right) + z _ {y} ^ {2} \left(\xi_ {i} , \eta_ {i}\right)} (\Delta \sigma_ {i}) _ {x y}
$$

的极限相等.这个极限在本目开始所给的条件下是存在的,它等于二重积分

$$
\iint_ {D _ {x y}} f [ x, y, z (x, y) ] \sqrt {1 + z _ {x} ^ {2} (x , y) + z _ {y} ^ {2} (x , y)} d x d y,
$$

因此左端的极限即曲面积分 $\iint_{\Sigma} f(x, y, z) \mathrm{d}S$ 也存在，且有

$$
\iint_ {\Sigma} f (x, y, z) \mathrm{d} S = \iint_ {D _ {z y}} f [ x, y, z (x, y) ] \sqrt {1 + z _ {x} ^ {2} (x , y) + z _ {y} ^ {2} (x , y)} \mathrm{d} x \mathrm{d} y. \tag {4-2}
$$

这就是把对面积的曲面积分化为二重积分的公式. 这公式是容易记忆的, 因为曲面 $\Sigma$ 的方程是 $z = z(x, y)$ , 而曲面积分记号中的 $\mathrm{d}S$ 就是 $\sqrt{1 + z_x^2(x, y) + z_y^2(x, y)} \mathrm{d}x \mathrm{~d}y$ . 在计算时, 只要把变量 $z$ 换为 $z(x, y)$ , $\mathrm{d}S$ 换为 $\sqrt{1 + z_x^2 + z_y^2} \mathrm{d}x \mathrm{~d}y$ , 再确定 $\Sigma$ 在 $xOy$ 面上的投影区域 $D_{xy}$ , 这样就把对面积的曲面积分化为二重积分了.

如果积分曲面 $\Sigma$ 由方程 $x=x(y,z)$ 或 $y=y(z,x)$ 给出, 也可类似地把对面积的曲面积分化为相应的二重积分.

例1 计算曲面积分 $\iint_{\Sigma} \frac{\mathrm{d}S}{z}$ , 其中 $\Sigma$ 是球面 $x^{2} + y^{2} + z^{2} = a^{2}$ 被平面 $z = h (0 < h < a)$ 截出的顶部(图11-20).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/bdfe364bf8d523cd91ae1b1cad79a269d614362325da1123b31ea234aaf23b11.jpg)



图11-20


解 $\Sigma$ 的方程为

$$
z = \sqrt {a ^ {2} - x ^ {2} - y ^ {2}},
$$

$\Sigma$ 在 $xOy$ 面上的投影区域 $D_{xy}$ 为圆形闭区域 $\{(x,y)\mid x^2 +y^2\leqslant a^2 -h^2\}$ . 又

$$
\sqrt {1 + z _ {x} ^ {2} + z _ {y} ^ {2}} = \frac {a}{\sqrt {a ^ {2} - x ^ {2} - y ^ {2}}}.
$$

根据公式(4-2)，有

$$
\iint_ {\Sigma} \frac {\mathrm{d} S}{z} = \iint_ {D _ {x y}} \frac {a \mathrm{d} x \mathrm{d} y}{a ^ {2} - x ^ {2} - y ^ {2}}.
$$

利用极坐标,得

$$
\iint_ {\Sigma} \frac {\mathrm{d} S}{z} = \iint_ {D _ {x y}} \frac {a \rho \mathrm{d} \rho \mathrm{d} \theta}{a ^ {2} - \rho^ {2}} = a \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {\sqrt {a ^ {2} - h ^ {2}}} \frac {\rho \mathrm{d} \rho}{a ^ {2} - \rho^ {2}} = 2 \pi a \left[ - \frac {1}{2} \ln (a ^ {2} - \rho^ {2}) \right] _ {0} ^ {\sqrt {a ^ {2} - h ^ {2}}} = 2 \pi a \ln \frac {a}{h}.
$$

例 2 计算 $\oiint_{\Sigma} xyz \, dS^{①}$ ，其中 $\Sigma$ 是由平面 x = 0, y = 0, z = 0 及 $x + y + z = 1$ 所围成的四面体的整个边界曲面（图 11-21）.

解 整个边界曲面 $\Sigma$ 在平面 $x = 0, y = 0, z = 0$ 及 $x + y + z = 1$ 上的部分依次记为 $\Sigma_1, \Sigma_2, \Sigma_3$ 及 $\Sigma_4$ , 于是

$$
\iint_ {\Sigma} x y z \mathrm{d} S = \iint_ {\Sigma_ {1}} x y z \mathrm{d} S + \iint_ {\Sigma_ {2}} x y z \mathrm{d} S + \iint_ {\Sigma_ {3}} x y z \mathrm{d} S + \iint_ {\Sigma_ {4}} x y z \mathrm{d} S.
$$

因为在 $\Sigma_{1}, \Sigma_{2}, \Sigma_{3}$ 上，被积函数 $f(x, y, z) = xyz$ 均为零，
所以

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/cdb750990267738356c0fbfc4c60e9c72e71794dc0a008ff7e7c5c2d1d734242.jpg)



图11-21


$$
\iint_ {\Sigma_ {1}} x y z \mathrm{d} S = \iint_ {\Sigma_ {2}} x y z \mathrm{d} S = \iint_ {\Sigma_ {3}} x y z \mathrm{d} S = 0.
$$

在 $\Sigma_4$ 上， $z = 1 - x - y$ ，所以

$$
\sqrt {1 + z _ {x} ^ {2} + z _ {y} ^ {2}} = \sqrt {1 + (- 1) ^ {2} + (- 1) ^ {2}} = \sqrt {3},
$$

从而

$$
\iint_ {\Sigma} x y z \mathrm{d} S = \iint_ {\Sigma_ {4}} x y z \mathrm{d} S = \iint_ {D _ {x y}} \sqrt {3} x y (1 - x - y) \mathrm{d} x \mathrm{d} y,
$$

其中 $D_{xy}$ 是 $\Sigma_4$ 在 $xOy$ 面上的投影区域, 即由直线 $x = 0, y = 0$ 及 $x + y = 1$ 所围成的闭区域. 因此

$$
\iint_ {\Sigma} x y z \mathrm{d} S = \sqrt {3} \int_ {0} ^ {1} x \mathrm{d} x \int_ {0} ^ {1 - x} y (1 - x - y) \mathrm{d} y = \sqrt {3} \int_ {0} ^ {1} x \left[ (1 - x) \frac {y ^ {2}}{2} - \frac {y ^ {3}}{3} \right] _ {0} ^ {1 - x} \mathrm{d} x
$$

① 记号 $\oint_{\Sigma}$ 表示在闭曲面 $\Sigma$ 上积分.

$$
= \sqrt {3} \int_ {0} ^ {1} x \cdot \frac {(1 - x) ^ {3}}{6} \mathrm{d} x = \frac {\sqrt {3}}{6} \int_ {0} ^ {1} (x - 3 x ^ {2} + 3 x ^ {3} - x ^ {4}) \mathrm{d} x = \frac {\sqrt {3}}{1 2 0}.
$$

# 习题11-4

1. 设有一分布着质量的曲面 $\Sigma$ ，在点 $(x, y, z)$ 处它的面密度为 $\mu(x, y, z)$ ，用对面积的曲面积分表示这曲面对于 $x$ 轴的转动惯量。

2. 按对面积的曲面积分的定义证明公式

$$
\iint_ {\Sigma} f (x, y, z) \mathrm{d} S = \iint_ {\Sigma_ {1}} f (x, y, z) \mathrm{d} S + \iint_ {\Sigma_ {2}} f (x, y, z) \mathrm{d} S,
$$

其中 $\Sigma$ 是由 $\Sigma_{1}$ 和 $\Sigma_{2}$ 组成的.

3. 当 $\Sigma$ 是 $xOy$ 面内的一个闭区域时, 曲面积分 $\iint_{\Sigma} f(x, y, z) \mathrm{d}S$ 与二重积分有什么关系?

4. 计算曲面积分 $\iint_{\Sigma} f(x, y, z) \mathrm{d}S$ ，其中 $\Sigma$ 为抛物面 $z = 2 - (x^2 + y^2)$ 在 $xOy$ 面上方的部分， $f(x, y, z)$ 分别如下：

(1) $f(x,y,z)=1;$ 

(2) $f(x,y,z)=x^{2}+y^{2};$ 

(3) $f(x,y,z)=3z.$ 

5. 计算 $\iint_{\Sigma} (x^2 + y^2) \, \mathrm{d}S$ ，其中 $\Sigma$ 是

（1）锥面 $z=\sqrt{x^{2}+y^{2}}$ 及平面 z=1 所围成的区域的整个边界曲面；

(2) 锥面 $z^{2}=3(x^{2}+y^{2})$ 被平面 z=0 和 z=3 所截得的部分.

6. 计算下列对面积的曲面积分：

(1) $\iint_{\Sigma}\left(z + 2x + \frac{4}{3} y\right)\mathrm{d}S$ ，其中 $\Sigma$ 为平面 $\frac{x}{2} +\frac{y}{3} +\frac{z}{4} = 1$ 在第I卦限中的部分；

(2) $\iint_{\Sigma} (2xy - 2x^2 - x + z) \, \mathrm{d}S$ ，其中 $\Sigma$ 为平面 $2x + 2y + z = 6$ 在第 I 卦限中的部分；

(3) $\iint_{\Sigma} (x + y + z) \, \mathrm{d}S$ ，其中 $\Sigma$ 为球面 $x^2 + y^2 + z^2 = a^2$ 上 $z \geqslant h (0 < h < a)$ 的部分；

(4) $\iint_{\Sigma} (xy + yz + zx) \, \mathrm{d}S$ ，其中 $\Sigma$ 为锥面 $z = \sqrt{x^2 + y^2}$ 被柱面 $x^2 + y^2 = 2ax$ 所截得的有限部分.

7. 求抛物面壳 $z = \frac{1}{2} (x^2 + y^2) (0 \leqslant z \leqslant 1)$ 的质量, 此壳的面密度为 $\mu = z$ .

8. 求面密度为 $\mu_{0}$ 的均匀半球壳 $x^{2}+y^{2}+z^{2}=a^{2}$ ( $z\geqslant0$ ) 对于 z 轴的转动惯量.

# 第五节 对坐标的曲面积分

# 一、对坐标的曲面积分的概念与性质

我们对曲面作一些说明,这里假定曲面是光滑的.

通常我们遇到的曲面都是双侧的.例如由方程 $z = z(x, y)$ 表示的曲面,有上侧与下侧之分①;又例如,一张包围某一空间区域的闭曲面,有外侧与内侧之分.以后我们总假定所考虑的曲面是双侧的.

在讨论对坐标的曲面积分时,需要指定曲面的侧.我们可以通过曲面上法向量的方向来定出曲面的侧.例如,对于曲面 $z=z(x,y)$ ,如果取它的法向量n的方向朝上,我们就认为取定曲面的上侧;又如,对于闭曲面如果取它的法向量的方向朝外,我们就认为取定曲面的外侧.这种取定了法向量亦即选定了侧的曲面,就称为有向曲面.

设 $\Sigma$ 是有向曲面. 在 $\Sigma$ 上取一小块曲面 $\Delta S$ , 把 $\Delta S$ 投影到 $xOy$ 面上得一投影区域, 这投影区域的面积记为 $(\Delta \sigma)_{xy}$ . 假定 $\Delta S$ 上各点处的法向量与 $z$ 轴的夹角 $\gamma$ 的余弦 $\cos \gamma$ 有相同的符号 (即 $\cos \gamma$ 都是正的或都是负的). 我们规定 $\Delta S$ 在 $xOy$ 面上的投影 $(\Delta S)_{xy}$ 为

$$
(\Delta S) _ {x y} = \left\{ \begin{array}{l l} (\Delta \sigma) _ {x y}, & \cos \gamma > 0, \\ - (\Delta \sigma) _ {x y}, & \cos \gamma <   0, \\ 0, & \cos \gamma \equiv 0. \end{array} \right.
$$

其中 $\cos \gamma \equiv 0$ 也就是 $(\Delta \sigma)_{xy} = 0$ 的情形. $\Delta S$ 在 $xOy$ 面上的投影 $(\Delta S)_{xy}$ 实际就是 $\Delta S$ 在 $xOy$ 面上的投影区域的面积附以一定的正负号. 类似地可以定义 $\Delta S$ 在 $yOz$ 面及 $zOx$ 面上的投影 $(\Delta S)_{yz}$ 及 $(\Delta S)_{zx}$ .

下面讨论一个例子,然后引进对坐标的曲面积分的概念.

流向曲面一侧的流量 设稳定流动②的不可压缩流体(假定密度为1)的速度场由

$$
\boldsymbol {v} (x, y, z) = P (x, y, z) \boldsymbol {i} + Q (x, y, z) \boldsymbol {j} + R (x, y, z) \boldsymbol {k}
$$

给出, $\Sigma$ 是速度场中的一片有向曲面,函数 $P(x,y,z)$ , $Q(x,y,z)$ 与 $R(x,y,z)$ 都在 $\Sigma$ 上连续,求在单位时间内流向 $\Sigma$ 指定侧的流体的质量,即流量 $\Phi$ .

如果流体流过平面上面积为 $A$ 的一个闭区域，且流体在这闭区域上各点处的流速为（常向量） $\pmb{v}$ ，又设 $\pmb{n}$ 为该平面的单位法向量（图11-22(a))，那么在单位时间内流过这个闭区域的流体组成一个底面积为 $A$ 、斜高为 $|\pmb{v}|$ 的斜柱体（图11-22(b)）。

当 $(\widehat{\pmb{v},\pmb{n}}) = \theta <  \frac{\pi}{2}$ 时，斜柱体的体积为

$$
A \mid \boldsymbol {v} \mid \cos \theta = A \boldsymbol {v} \cdot \boldsymbol {n}.
$$

这也就是通过闭区域 $A$ 流向 $\pmb{n}$ 所指一侧的流量 $\Phi$ ;

当 $(\widehat{\pmb{v},\pmb{n}}) = \frac{\pi}{2}$ 时，显然流体通过闭区域 $A$ 流向 $\pmb{n}$ 所指一侧的流量 $\Phi$ 为零，而 $Av\cdot$ 

$$
\pmb {n} = 0, \text {   故   } \Phi = A \pmb {v} \cdot \pmb {n} = 0;
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/30bd0f9aab872153bacbb266654f32a3594fc16b94cef0d7970cfcb2e6f5fbe7.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/5f6839c01f6890f09fac0c02c0af885d958f48efa99709448844f55c7e6c2336.jpg)



(b)



图11-22


当 $(\widehat{v,n}) > \frac{\pi}{2}$ 时， $Av \cdot n < 0$ ，这时我们仍把 $Av \cdot n$ 称为流体通过闭区域 $A$ 流向 $n$ 所指一侧的流量，它表示流体通过闭区域 $A$ 实际上流向 $-n$ 所指一侧，且流向 $-n$ 所指一侧的流量为 $-Av \cdot n$ . 因此，不论 $(\widehat{v,n})$ 为何值，流体通过闭区域 $A$ 流向 $n$ 所指一侧的流量 $\Phi$ 均为 $Av \cdot n$ .

由于现在所考虑的不是平面闭区域而是一片曲面,且流速 v 也不是常向量,因此所求流量不能直接用上述方法计算.然而过去在引出各类积分概念的例子中一再使用过的方法,也可用来解决目前的问题.

把曲面 $\Sigma$ 分成 $n$ 小块 $\Delta S_{i}$ ( $\Delta S_{i}$ 同时也代表第 $i$ 小块曲面的面积). 在 $\Sigma$ 是光滑的和 $\pmb{v}$ 是连续的前提下, 只要 $\Delta S_{i}$ 的直径很小, 我们就可以用 $\Delta S_{i}$ 上任一点 $(\xi_{i}, \eta_{i}, \zeta_{i})$ 处的流速

$$
\boldsymbol {v} _ {i} = \boldsymbol {v} \left(\xi_ {i}, \eta_ {i}, \zeta_ {i}\right) = P \left(\xi_ {i}, \eta_ {i}, \zeta_ {i}\right) i + Q \left(\xi_ {i}, \eta_ {i}, \zeta_ {i}\right) j + R \left(\xi_ {i}, \eta_ {i}, \zeta_ {i}\right) k
$$

代替 $\Delta S_{i}$ 上其他各点处的流速, 以该点 $(\xi_{i}, \eta_{i}, \zeta_{i})$ 处曲面 $\Sigma$ 的单位法向量

$$
\boldsymbol {n} _ {i} = \cos \alpha_ {i} \boldsymbol {i} + \cos \beta_ {i} \boldsymbol {j} + \cos \gamma_ {i} \boldsymbol {k}
$$

代替 $\Delta S_{i}$ 上其他各点处的单位法向量（图11-23).从而得到通过 $\Delta S_{i}$ 流向指定侧的流量的近似值为

$$
\boldsymbol {v} _ {i} \cdot \boldsymbol {n} _ {i} \Delta S _ {i} (i = 1, 2, \dots , n).
$$

于是,通过 $\Sigma$ 流向指定侧的流量

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/3d72fa83137bed5d8c8e9a30ab0398210a7c52038548023a0899423ae2fad60f.jpg)



图11-23


$$
\begin{array}{l} \Phi \approx \sum_ {i = 1} ^ {n} \boldsymbol {v} _ {i} \cdot \boldsymbol {n} _ {i} \Delta S _ {i} \\ = \sum_ {i = 1} ^ {n} \left[ P (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \cos \alpha_ {i} + Q (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \cos \beta_ {i} + R (\xi_ {i}, \eta_ {i}, \zeta_ {i}) \cos \gamma_ {i} \right] \Delta S _ {i}, \\ \end{array}
$$

但

$$
\cos \alpha_ {i} \cdot \Delta S _ {i} \approx (\Delta S _ {i}) _ {y z}, \quad \cos \beta_ {i} \cdot \Delta S _ {i} \approx (\Delta S _ {i}) _ {z x}, \quad \cos \gamma_ {i} \cdot \Delta S _ {i} \approx (\Delta S _ {i}) _ {x y},
$$

因此上式可以写成

$$
\Phi \approx \sum_ {i = 1} ^ {n} \left[ P \left(\xi_ {i}, \eta_ {i}, \zeta_ {i}\right) (\Delta S _ {i}) _ {\gamma z} + Q \left(\xi_ {i}, \eta_ {i}, \zeta_ {i}\right) (\Delta S _ {i}) _ {z x} + R \left(\xi_ {i}, \eta_ {i}, \zeta_ {i}\right) (\Delta S _ {i}) _ {x y} \right].
$$

当各小块曲面的直径的最大值 $\lambda\rightarrow0$ 取上述和的极限, 就得到流量 $\Phi$ 的精确值. 这样的极限还会在其他问题中遇到. 抽去它们的具体意义, 就得出下列对坐标的曲面积分的概念:

定义 设 $\Sigma$ 为光滑的有向曲面, 函数 $R(x,y,z)$ 在 $\Sigma$ 上有界. 把 $\Sigma$ 任意分成 n 块小曲面 $\Delta S_{i}$ ( $\Delta S_{i}$ 同时又表示第 i 块小曲面的面积), $\Delta S_{i}$ 在 xOy 面上的投影为 $(\Delta S_{i})_{xy}$ , $(\xi_{i},\eta_{i},\zeta_{i})$ 是 $\Delta S_{i}$ 上任意取定的一点, 作乘积 $R(\xi_{i},\eta_{i},\zeta_{i})(\Delta S_{i})_{xy}$ ( $i=1,2,\cdots,n$ ), 并作和 $\sum_{i=1}^{n}R(\xi_{i},\eta_{i},\zeta_{i})(\Delta S_{i})_{xy}$ , 如果当各小块曲面的直径的最大值 $\lambda\to0$ 时, 这和的极限总存在, 且与曲面 $\Sigma$ 的分法及点 $(\xi_{i},\eta_{i},\zeta_{i})$ 的取法无关, 那么称此极限为函数 $R(x,y,z)$ 在有向曲面 $\Sigma$ 上对坐标 x,y 的曲面积分, 记作 $\iint_{\Sigma}R(x,y,z)\mathrm{d}x\mathrm{d}y$ , 即

$$
\iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} R (\xi_ {i}, \eta_ {i}, \zeta_ {i}) (\Delta S _ {i}) _ {x y},
$$

其中 $R(x,y,z)$ 叫做被积函数, $\Sigma$ 叫做积分曲面.

类似地可以定义函数 $P(x, y, z)$ 在有向曲面 $\Sigma$ 上对坐标 $y, z$ 的曲面积分 $\iint_{\Sigma} P(x, y, z) \mathrm{d}y \mathrm{d}z$ 及函数 $Q(x, y, z)$ 在有向曲面 $\Sigma$ 上对坐标 $z, x$ 的曲面积分 $\iint_{\Sigma} Q(x, y, z) \mathrm{d}z \mathrm{d}x$ 分别为

$$
\begin{array}{l} \iint_ {\Sigma} P (x, y, z) \mathrm{d} y \mathrm{d} z = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} P (\xi_ {i}, \eta_ {i}, \zeta_ {i}) (\Delta S _ {i}) _ {y z}, \\ \iint_ {S} Q (x, y, z) \mathrm{d} z \mathrm{d} x = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} Q (\xi_ {i}, \eta_ {i}, \zeta_ {i}) (\Delta S _ {i}) _ {z x} \\ \end{array}
$$

以上三个曲面积分也称为第二类曲面积分.

我们指出, 当 $P(x, y, z), Q(x, y, z)$ 与 $R(x, y, z)$ 在有向光滑曲面 $\Sigma$ 上连续时, 对坐标的曲面积分是存在的, 以后总假定 $P, Q$ 与 $R$ 在 $\Sigma$ 上连续.

在应用上出现较多的是

$$
\iint_ {\Sigma} P (x, y, z) \mathrm{d} y \mathrm{d} z + \iint_ {\Sigma} Q (x, y, z) \mathrm{d} z \mathrm{d} x + \iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y
$$

这种合并起来的形式.为简便起见,我们把它写成

$$
\iint_ {\Sigma} P (x, y, z) \mathrm{d} y \mathrm{d} z + Q (x, y, z) \mathrm{d} z \mathrm{d} x + R (x, y, z) \mathrm{d} x \mathrm{d} y.
$$

例如,上述流向 $\Sigma$ 指定侧的流量 $\Phi$ 可表示为

$$
\Phi = \iint_ {\Sigma} P (x, y, z) \mathrm{d} y \mathrm{d} z + Q (x, y, z) \mathrm{d} z \mathrm{d} x + R (x, y, z) \mathrm{d} x \mathrm{d} y.
$$

如果 $\Sigma$ 是分片光滑的有向曲面, 我们规定函数在 $\Sigma$ 上对坐标的曲面积分等于函数在各片光滑曲面上对坐标的曲面积分之和.

对坐标的曲面积分具有与对坐标的曲线积分相类似的一些性质.例如：

(1) 如果把 $\Sigma$ 分成 $\Sigma_{1}$ 和 $\Sigma_{2}$ ，那么

$$
\begin{array}{l} \iint_ {\Sigma} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y \\ = \iint_ {\Sigma_ {1}} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y + \iint_ {\Sigma_ {2}} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y. \tag {5-1} \\ \end{array}
$$

公式(5-1)可以推广到 $\Sigma$ 分成 $\Sigma_{1}, \Sigma_{2}, \cdots, \Sigma_{n}$ 几部分的情形.

(2) 设 $\Sigma$ 是有向曲面, $\Sigma^{-}$ 表示与 $\Sigma$ 取相反侧的有向曲面, 则

$$
\begin{array}{l} \iint_ {\Sigma^ {-}} P (x, y, z) \mathrm{d} y \mathrm{d} z = - \iint_ {\Sigma} P (x, y, z) \mathrm{d} y \mathrm{d} z, \\ \iint_ {\Sigma^ {-}} Q (x, y, z) \mathrm{d} z \mathrm{d} x = - \iint_ {\Sigma} Q (x, y, z) \mathrm{d} z \mathrm{d} x, \tag {5-2} \\ \iint_ {\Sigma^ {-}} R (x, y, z) \mathrm{d} x \mathrm{d} y = - \iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y. \\ \end{array}
$$

(5-2)式表示,当积分曲面改变为相反侧时,对坐标的曲面积分要改变符号.因此关于对坐标的曲面积分,我们必须注意积分曲面所取的侧.

这些性质的证明从略.

# 二、对坐标的曲面积分的计算法

设积分曲面 $\Sigma$ 是由方程 $z = z(x, y)$ 所给出的曲面上侧， $\Sigma$ 在 $xOy$ 面上的投影区域为 $D_{xy}$ ，函数 $z = z(x, y)$ 在 $D_{xy}$ 上具有一阶连续偏导数，被积函数 $R(x, y, z)$ 在 $\Sigma$ 上连续。

按对坐标的曲面积分的定义,有

$$
\iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} R (\xi_ {i}, \eta_ {i}, \zeta_ {i}) (\Delta S _ {i}) _ {x y}.
$$

因为 $\Sigma$ 取上侧， $\cos \gamma > 0$ ，所以

$$
\left(\Delta S _ {i}\right) _ {x y} = \left(\Delta \sigma_ {i}\right) _ {x y}.
$$

又因 $(\xi_{i},\eta_{i},\zeta_{i})$ 是 $\Sigma$ 上的一点，故 $\zeta_{i} = z(\xi_{i},\eta_{i})$ .从而有

$$
\sum_ {i = 1} ^ {n} R \left(\xi_ {i}, \eta_ {i}, \zeta_ {i}\right) (\Delta S _ {i}) _ {x y} = \sum_ {i = 1} ^ {n} R \left[ \xi_ {i}, \eta_ {i}, z (\xi_ {i}, \eta_ {i}) \right] (\Delta \sigma_ {i}) _ {x y}.
$$

令各小块曲面的直径的最大值 $\lambda\rightarrow0$ 取上式两端的极限, 就得到

$$
\iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y = \iint_ {D _ {x y}} R [ x, y, z (x, y) ] \mathrm{d} x \mathrm{d} y. \tag {5-3}
$$

这就是把对坐标的曲面积分化为二重积分的公式.公式(5-3)表明,计算曲面积分 $\iint_{\Sigma}R(x,y,z)\mathrm{d}x\mathrm{d}y$ 时,只需将其中变量z换为表示 $\Sigma$ 的函数 $z(x,y)$ ,然后在 $\Sigma$ 的投影区域 $D_{xy}$ 上计算二重积分即可.

必须注意,公式(5-3)的曲面积分是取在曲面 $\Sigma$ 上侧的,如果曲面积分取在 $\Sigma$ 的下侧,这时 $\cos \gamma < 0$ ,那么

$$
\left(\Delta S _ {i}\right) _ {x y} = - \left(\Delta \sigma_ {i}\right) _ {x y},
$$

从而有

$$
\iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y = - \iint_ {D _ {x y}} R [ x, y, z (x, y) ] \mathrm{d} x \mathrm{d} y. \tag {$5-3^{\prime$}}
$$

类似地,如果 $\Sigma$ 由 $x=x(y,z)$ 给出,那么有

$$
\iint_ {\Sigma} P (x, y, z) \mathrm{d} y \mathrm{d} z = \pm \iint_ {D _ {y z}} P [ x (y, z), y, z ] \mathrm{d} y \mathrm{d} z, \tag {5-4}
$$

等式右端的符号这样决定:积分曲面 $\Sigma$ 是由方程 $x=x(y,z)$ 所给出的曲面前侧,即 $\cos\alpha>0$ , 应取正号; 反之, $\Sigma$ 取后侧, 即 $\cos\alpha<0$ , 应取负号.

如果 $\Sigma$ 由 $y=y(z,x)$ 给出,那么有

$$
\iint_ {\Sigma} Q (x, y, z) \mathrm{d} z \mathrm{d} x = \pm \iint_ {D _ {z x}} Q [ x, y (z, x), z ] \mathrm{d} z \mathrm{d} x, \tag {5-5}
$$

等式右端的符号这样决定:积分曲面 $\Sigma$ 是由方程 $y=y(z,x)$ 所给出的曲面右侧,即 $\cos\beta>0$ , 应取正号; 反之, $\Sigma$ 取左侧, 即 $\cos\beta<0$ , 应取负号.

例 1 计算曲面积分

$$
\iint_ {\Sigma} x ^ {2} \mathrm{d} y \mathrm{d} z + y ^ {2} \mathrm{d} z \mathrm{d} x + z ^ {2} \mathrm{d} x \mathrm{d} y,
$$

其中 $\Sigma$ 是长方体 $\Omega$ 的整个表面的外侧， $\Omega = \{(x, y, z) | 0 \leqslant x \leqslant a, 0 \leqslant y \leqslant b, 0 \leqslant z \leqslant c\}$ .

解 把有向曲面 $\Sigma$ 分成以下六部分：

$\Sigma_{1}:z=c\ (0\leqslant x\leqslant a,0\leqslant y\leqslant b)$ 的上侧，

$\Sigma_{2}:z = 0(0 \leqslant x \leqslant a, 0 \leqslant y \leqslant b)$ 的下侧，

$\Sigma_{3}:x=a(0\leqslant y\leqslant b,0\leqslant z\leqslant c)$ 的前侧，

$\Sigma_{4}:x = 0(0\leqslant y\leqslant b,0\leqslant z\leqslant c)$ 的后侧，

$\Sigma_{5}:y=b\ (0\leqslant x\leqslant a,0\leqslant z\leqslant c)$ 的右侧，

$\Sigma_{6}:y = 0(0\leqslant x\leqslant a,0\leqslant z\leqslant c)$ 的左侧.

除 $\Sigma_3, \Sigma_4$ 外，其余四片曲面在 $yOz$ 面上的投影为零，因此

$$
\iint_ {\Sigma} x ^ {2} \mathrm{d} y \mathrm{d} z = \iint_ {\Sigma_ {3}} x ^ {2} \mathrm{d} y \mathrm{d} z + \iint_ {\Sigma_ {4}} x ^ {2} \mathrm{d} y \mathrm{d} z.
$$

应用公式(5-4)就有

$$
\iint_ {\Sigma} x ^ {2} \mathrm{d} y \mathrm{d} z = \iint_ {D _ {y z}} a ^ {2} \mathrm{d} y \mathrm{d} z - \iint_ {D _ {y z}} 0 ^ {2} \mathrm{d} y \mathrm{d} z = a ^ {2} b c.
$$

类似地可得

$$
\iint_ {\Sigma} y ^ {2} \mathrm{d} z \mathrm{d} x = b ^ {2} a c, \iint_ {\Sigma} z ^ {2} \mathrm{d} x \mathrm{d} y = c ^ {2} a b.
$$

于是所求曲面积分为 $(a+b+c)abc.$ 

例2 计算曲面积分 $\iint_{\Sigma} xyz \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $\Sigma$ 是球面 $x^2 + y^2 + z^2 = 1$ 外侧在 $x \geqslant 0, y \geqslant 0$ 的部分.

解 把 $\Sigma$ 分为 $\Sigma_{1}$ 和 $\Sigma_{2}$ 两部分(图 11-24), $\Sigma_{1}$ 的方程为

$$
z _ {1} = - \sqrt {1 - x ^ {2} - y ^ {2}},
$$

$\Sigma_{2}$ 的方程为

$$
z _ {2} = \sqrt {1 - x ^ {2} - y ^ {2}}.
$$

$$
\iint_ {\Sigma} x y z \mathrm{d} x \mathrm{d} y = \iint_ {\Sigma_ {2}} x y z \mathrm{d} x \mathrm{d} y + \iint_ {\Sigma_ {1}} x y z \mathrm{d} x \mathrm{d} y.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/c594bd3ca147bb3ed4d240ab78eb232eee56f04b674f2d461fa9939a3b271ca4.jpg)



图11-24


上式右端的第一个积分的积分曲面 $\Sigma_{2}$ 取上侧, 第二个积分的积分曲面 $\Sigma_{1}$ 取下侧, 因此分别应用公式(5-3)及(5-3'), 就有

$$
\begin{array}{l} \iint_ {\Sigma} x y z \mathrm{d} x \mathrm{d} y = \iint_ {D _ {x y}} x y \sqrt {1 - x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y - \iint_ {D _ {x y}} x y (- \sqrt {1 - x ^ {2} - y ^ {2}}) \mathrm{d} x \mathrm{d} y \\ = 2 \iint_ {D _ {x y}} x y \sqrt {1 - x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y. \\ \end{array}
$$

其中 $D_{xy}$ 是 $\Sigma_1$ 及 $\Sigma_2$ 在 $xOy$ 面上的投影区域，就是位于第一象限内的扇形 $x^{2} + y^{2} \leqslant 1$ ( $x \geqslant 0, y \geqslant 0$ ). 利用极坐标计算这个二重积分如下：

$$
\begin{array}{l} 2 \iint_ {D _ {x y}} x y \sqrt {1 - x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y = 2 \iint_ {D _ {x y}} \rho^ {2} \sin \theta \cos \theta \sqrt {1 - \rho^ {2}} \rho \mathrm{d} \rho \mathrm{d} \theta \\ = \int_ {0} ^ {\frac {\pi}{2}} \sin 2 \theta \mathrm{d} \theta \int_ {0} ^ {1} \rho^ {3} \sqrt {1 - \rho^ {2}} \mathrm{d} \rho = 1 \times \frac {2}{1 5} = \frac {2}{1 5}, \\ \end{array}
$$

从而

$$
\iint_ {\Sigma} x y z \mathrm{d} x \mathrm{d} y = \frac {2}{1 5}.
$$

# 三、两类曲面积分之间的联系

设有向曲面 $\Sigma$ 由方程 $z = z(x, y)$ 给出， $\Sigma$ 在 $xOy$ 面上的投影区域为 $D_{xy}$ ，函数 $z = z(x, y)$ 在 $D_{xy}$ 上具有一阶连续偏导数， $R(x, y, z)$ 在 $\Sigma$ 上连续。如果 $\Sigma$ 取上侧，那么由对坐标的曲面积分计算公式(5-3)有

$$
\iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y = \iint_ {D _ {x y}} R [ x, y, z (x, y) ] \mathrm{d} x \mathrm{d} y.
$$

另一方面,因上述有向曲面 $\Sigma$ 的法向量的方向余弦为

$$
\cos \alpha = \frac {- z _ {x}}{\sqrt {1 + z _ {x} ^ {2} + z _ {y} ^ {2}}}, \quad \cos \beta = \frac {- z _ {y}}{\sqrt {1 + z _ {x} ^ {2} + z _ {y} ^ {2}}}, \quad \cos \gamma = \frac {1}{\sqrt {1 + z _ {x} ^ {2} + z _ {y} ^ {2}}},
$$

故由对面积的曲面积分计算公式有

$$
\iint_ {\Sigma} R (x, y, z) \cos \gamma \mathrm{d} S = \iint_ {D _ {x y}} R [ x, y, z (x, y) ] \mathrm{d} x \mathrm{d} y.
$$

由此可见,有

$$
\iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y = \iint_ {\Sigma} R (x, y, z) \cos \gamma \mathrm{d} S. \tag {5-6}
$$

如果 $\Sigma$ 取下侧,那么由式(5-3')有

$$
\iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y = - \iint_ {D _ {x y}} R [ x, y, z (x, y) ] \mathrm{d} x \mathrm{d} y.
$$

但这时 $\cos \gamma = \frac{-1}{\sqrt{1 + z_{x}^{2} + z_{y}^{2}}}$ ，因此(5-6)式仍成立.

类似地可推得

$$
\iint_ {\Sigma} P (x, y, z) \mathrm{d} y \mathrm{d} z = \iint_ {\Sigma} P (x, y, z) \cos \alpha \mathrm{d} S, \tag {5-7}
$$

$$
\iint_ {\Sigma} Q (x, y, z) \mathrm{d} z \mathrm{d} x = \iint_ {\Sigma} Q (x, y, z) \cos \beta \mathrm{d} S. \tag {5-8}
$$

合并(5-6)、(5-7)、(5-8)三式,得两类曲面积分之间的如下联系:

$$
\iint_ {\Sigma} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y = \iint_ {\Sigma} (P \cos \alpha + Q \cos \beta + R \cos \gamma) \mathrm{d} S, \tag {5-9}
$$

其中 $\cos\alpha,\cos\beta$ 与 $\cos\gamma$ 是有向曲面 $\Sigma$ 在点 $(x,y,z)$ 处的法向量的方向余弦.

两类曲面积分之间的联系也可写成如下的向量形式：

$$
\iint_ {\Sigma} \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {S} = \iint_ {\Sigma} \boldsymbol {A} \cdot \boldsymbol {n} \mathrm{d} S \tag {5-10}
$$

或

$$
\iint_ {\Sigma} \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {S} = \iint_ {\Sigma} A _ {n} \mathrm{d} S, \tag {$5-10^{\prime$}}
$$

其中 $A = (P, Q, R)$ , $n = (\cos \alpha, \cos \beta, \cos \gamma)$ 为有向曲面 $\Sigma$ 在点 $(x, y, z)$ 处的单位法向量, $\mathrm{d}S = n\mathrm{d}S = (\mathrm{dydz}, \mathrm{dzdx}, \mathrm{dxdy})$ 称为有向曲面元, $A_{n}$ 为向量 $A$ 在向量 $n$ 上的投影.

例3 计算曲面积分 $\iint_{\Sigma} (z^2 + x) \, \mathrm{d}y \, \mathrm{d}z - z \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $\Sigma$ 是旋转抛物面 $z = \frac{1}{2} (x^2 + y^2)$ 介于平面 $z = 0$ 及 $z = 2$ 之间的部分的下侧.

解法一 把 $\Sigma$ 分为 $\Sigma_{前}, \Sigma_{后}$ 两部分, 它们在 yOz 面上的投影区域为 $D_{yz}$ ,

$$
\begin{array}{l} \iint_ {\Sigma} \left(z ^ {2} + x\right) \mathrm{d} y \mathrm{d} z = \iint_ {\Sigma_ {\text {前}}} \left(z ^ {2} + x\right) \mathrm{d} y \mathrm{d} z + \iint_ {\Sigma_ {\text {后}}} \left(z ^ {2} + x\right) \mathrm{d} y \mathrm{d} z \\ = \iint_ {D _ {y z}} \left(z ^ {2} + \sqrt {2 z - y ^ {2}}\right) d y d z - \iint_ {D _ {y z}} \left(z ^ {2} - \sqrt {2 z - y ^ {2}}\right) d y d z \\ = 2 \iint_ {D _ {y z}} \sqrt {2 z - y ^ {2}} \mathrm{d} y \mathrm{d} z = 2 \int_ {- 2} ^ {2} \mathrm{d} y \int_ {\frac {1}{2} y ^ {2}} ^ {2} \sqrt {2 z - y ^ {2}} \mathrm{d} z = 4 \pi . \\ \end{array}
$$

$$
\iint_ {\Sigma} z \mathrm{d} x \mathrm{d} y = - \iint_ {D _ {x y}} \frac {1}{2} \left(x ^ {2} + y ^ {2}\right) \mathrm{d} x \mathrm{d} y = - \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {2} \frac {1}{2} \rho^ {2} \cdot \rho \mathrm{d} \rho = - 4 \pi .
$$

故

$$
\iint_ {\Sigma} (z ^ {2} + x) \mathrm{d} y \mathrm{d} z - z \mathrm{d} x \mathrm{d} y = 4 \pi - (- 4 \pi) = 8 \pi .
$$

解法二 利用两类曲面积分之间的联系(5-9)，将对坐标 $y, z$ 的曲面积分转化为对坐标 $x, y$ 的曲面积分

$$
\iint_ {\Sigma} (z ^ {2} + x) \mathrm{d} y \mathrm{d} z = \iint_ {\Sigma} (z ^ {2} + x) \cos \alpha \mathrm{d} S = \iint_ {\Sigma} (z ^ {2} + x) \frac {\cos \alpha}{\cos \gamma} \mathrm{d} x \mathrm{d} y.
$$

在曲面 $\Sigma$ 上，有

$$
\cos \alpha = \frac {x}{\sqrt {1 + x ^ {2} + y ^ {2}}}, \quad \cos \gamma = \frac {- 1}{\sqrt {1 + x ^ {2} + y ^ {2}}}.
$$

故

$$
\iint_ {\Sigma} \left(z ^ {2} + x\right) \mathrm{d} y \mathrm{d} z - z \mathrm{d} x \mathrm{d} y = \iint_ {\Sigma} \left[ \left(z ^ {2} + x\right) (- x) - z \right] \mathrm{d} x \mathrm{d} y.
$$

再按对坐标的曲面积分的计算法,便得

$$
\iint_ {\Sigma} (z ^ {2} + x) \mathrm{d} y \mathrm{d} z - z \mathrm{d} x \mathrm{d} y = - \iint_ {D _ {x y}} \left\{\left[ \frac {1}{4} (x ^ {2} + y ^ {2}) ^ {2} + x \right] \cdot (- x) - \frac {1}{2} (x ^ {2} + y ^ {2}) \right\} \mathrm{d} x \mathrm{d} y.
$$

利用积分区域及被积函数的对称性可知

$$
\iint_ {D _ {x y}} \frac {1}{4} x (x ^ {2} + y ^ {2}) ^ {2} \mathrm{d} x \mathrm{d} y = 0,
$$

故

$$
\begin{array}{l} \iint_ {\Sigma} \left(z ^ {2} + x\right) \mathrm{d} y \mathrm{d} z - z \mathrm{d} x \mathrm{d} y = \iint_ {D _ {x y}} \left[ x ^ {2} + \frac {1}{2} (x ^ {2} + y ^ {2}) \right] \mathrm{d} x \mathrm{d} y \\ = \int_ {0} ^ {2 \pi} \mathrm{d} \theta \int_ {0} ^ {2} \left(\rho^ {2} \cos^ {2} \theta + \frac {1}{2} \rho^ {2}\right) \rho \mathrm{d} \rho = 8 \pi . \\ \end{array}
$$

# 习题11-5

1. 按对坐标的曲面积分的定义证明公式

$$
\iint_ {\Sigma} \left[ P _ {1} (x, y, z) \pm P _ {2} (x, y, z) \right] \mathrm{d} y \mathrm{d} z = \iint_ {\Sigma} P _ {1} (x, y, z) \mathrm{d} y \mathrm{d} z \pm \iint_ {\Sigma} P _ {2} (x, y, z) \mathrm{d} y \mathrm{d} z.
$$

2. 当 $\Sigma$ 为 $xOy$ 面内的一个闭区域时, 曲面积分 $\iint_{\Sigma} R(x, y, z) \mathrm{d} x \mathrm{d} y$ 与二重积分有什么关系?

3. 计算下列对坐标的曲面积分：

(1) $\iint_{\Sigma} x^{2} y^{2} z \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $\Sigma$ 是球面 $x^{2} + y^{2} + z^{2} = R^{2}$ 的下半部分的下侧；

(2) $\iint_{\Sigma} z \, \mathrm{d}x \, \mathrm{d}y + x \, \mathrm{d}y \, \mathrm{d}z + y \, \mathrm{d}z \, \mathrm{d}x$ ，其中 $\Sigma$ 是柱面 $x^2 + y^2 = 1$ 被平面 $z = 0$ 及 $z = 3$ 所截得的在第 I 卦限内的部分的前侧；

(3) $\iint_{\Sigma}[f(x,y,z)+x]\mathrm{d}y\mathrm{d}z+[2f(x,y,z)+y]\mathrm{d}z\mathrm{d}x+[f(x,y,z)+z]\mathrm{d}x\mathrm{d}y$ ，其中 $f(x,y,z)$ 为连续函数， $\Sigma$ 是平面 $x-y+z=1$ 在第IV卦限部分的上侧；

(4) $\oint_{\Sigma} xz dx dy + xy dy dz + yz dz dx$ ，其中 $\Sigma$ 是平面 x = 0, y = 0, z = 0, $x + y + z = 1$ 所围成的空间区域的整个边界曲面的外侧.

4. 把对坐标的曲面积分

$$
\iint_ {\Sigma} P (x, y, z) \mathrm{d} y \mathrm{d} z + Q (x, y, z) \mathrm{d} z \mathrm{d} x + R (x, y, z) \mathrm{d} x \mathrm{d} y
$$

化成对面积的曲面积分,其中

(1) $\Sigma$ 是平面 $3x + 2y + 2\sqrt{3}z = 6$ 在第 I 卦限的部分的上侧；

(2) $\Sigma$ 是抛物面 $z=8-(x^{2}+y^{2})$ 在 xOy 面上方的部分的上侧.

5. 计算

$$
\iint_ {\Sigma} (3 z + 1) x \mathrm{d} y \mathrm{d} z - \mathrm{d} z \mathrm{d} x + z \mathrm{d} x \mathrm{d} y,
$$

其中 $\Sigma$ 是由曲线 $\left\{\begin{aligned}z&=\sqrt{y-1},\\ x&=0\end{aligned}\right.$ $(1\leqslant y\leqslant3)$ 绕 y 轴旋转一周所成的旋转曲面的左侧.

# 第六节 高斯公式 * 通量与散度

# 一、高斯公式

格林公式表达了平面闭区域上的二重积分与其边界曲线上的曲线积分之间的关系,而高斯(Gauss)公式表达了空间闭区域上的三重积分与其边界曲面上的曲面积分之间的关系,这个关系可陈述如下:

定理1 设空间闭区域 $\Omega$ 是由分片光滑的闭曲面 $\Sigma$ 所围成, 若函数 $P(x, y, z)$ , $Q(x, y, z)$ 与 $R(x, y, z)$ 在 $\Omega$ 上具有一阶连续偏导数, 则有

$$
\iiint_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm{d} V = \iint_ {\Sigma} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y, \tag {6-1}
$$

或

$$
\iiint_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm{d} V = \oiint_ {\Sigma} (P \cos \alpha + Q \cos \beta + R \cos \gamma) \mathrm{d} S, \tag {$6-1^{\prime$}}
$$

这里 $\Sigma$ 是 $\Omega$ 的整个边界曲面的外侧, $\cos \alpha, \cos \beta$ 与 $\cos \gamma$ 是 $\Sigma$ 在点 $(x, y, z)$ 处的法向量的方向余弦. 公式 (6-1) 或 (6-1') 叫做高斯公式.证 由公式(5-9)可知, 公式(6-1)及(6-1')的右端是相等的, 因此这里只要证明公式(6-1)就可以了.

设闭区域 $\Omega$ 在 $xOy$ 面上的投影区域为 $D_{xy}$ . 假定穿过 $\Omega$ 内部且平行于 $z$ 轴的直线与 $\Omega$ 的边界曲面 $\Sigma$ 的交点恰好是两个. 这样, 可设 $\Sigma$ 由 $\Sigma_1, \Sigma_2$ 和 $\Sigma_3$ 三部分组成 (图11-25), 其中 $\Sigma_1$ 和 $\Sigma_2$ 分别由方程 $z = z_1(x, y)$ 和 $z = z_2(x, y)$ 给定, 这里 $z_1(x, y) \leqslant z_2(x, y), \Sigma_1$ 取下侧, $\Sigma_2$ 取上侧, $\Sigma_3$ 是以$D_{xy}$ 的边界曲线为准线而母线平行于 z 轴的柱面上的一部分, 取外侧.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/d7f3a69d7316357712b32f9f6225926e348d09c49fc38188077923f60942bec4.jpg)



图11-25


根据三重积分的计算法,有

$$
\begin{array}{l} \iiint_ {\Omega} \frac {\partial R}{\partial z} \mathrm{d} V = \iint_ {D _ {x y}} \left\{\int_ {z _ {1} (x, y)} ^ {z _ {2} (x, y)} \frac {\partial R}{\partial z} \mathrm{d} z \right\} \mathrm{d} x \mathrm{d} y \\ = \iint_ {D _ {x y}} \left\{R [ x, y, z _ {2} (x, y) ] - R [ x, y, z _ {1} (x, y) ] \right\} \mathrm{d} x \mathrm{d} y. \tag {6-2} \\ \end{array}
$$

根据曲面积分的计算法,有

$$
\begin{array}{l} \iint_ {\Sigma_ {1}} R (x, y, z) \mathrm{d} x \mathrm{d} y = - \iint_ {D _ {x y}} R [ x, y, z _ {1} (x, y) ] \mathrm{d} x \mathrm{d} y. \\ \iint_ {\Sigma_ {2}} R (x, y, z) \mathrm{d} x \mathrm{d} y = \iint_ {D _ {x y}} R [ x, y, z _ {2} (x, y) ] \mathrm{d} x \mathrm{d} y. \\ \end{array}
$$

因为 $\Sigma_{3}$ 上任意一块曲面在 xOy 面上的投影为零, 所以直接根据对坐标的曲面积分的定义可知

$$
\iint_ {\Sigma_ {3}} R (x, y, z) \mathrm{d} x \mathrm{d} y = 0.
$$

把以上三式相加,得

$$
\iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y = \iint_ {D _ {x y}} \left\{R [ x, y, z _ {2} (x, y) ] - R [ x, y, z _ {1} (x, y) ] \right\} \mathrm{d} x \mathrm{d} y. \tag {6-3}
$$

比较(6-2)与(6-3)两式,得

$$
\iiint_ {\Omega} \frac {\partial R}{\partial z} \mathrm{d} V = \iint_ {\Sigma} R (x, y, z) \mathrm{d} x \mathrm{d} y.
$$

如果穿过 $\Omega$ 内部且平行于 x 轴的直线以及平行于 y 轴的直线与 $\Omega$ 的边界曲面 $\Sigma$ 的交点也都恰好是两个,那么类似地可得

$$
\iiint_ {\Omega} \frac {\partial P}{\partial x} \mathrm{d} V = \oiint_ {\Sigma} P (x, y, z) \mathrm{d} y \mathrm{d} z, \quad \iiint_ {\Omega} \frac {\partial Q}{\partial y} \mathrm{d} V = \oiint_ {\Sigma} Q (x, y, z) \mathrm{d} z \mathrm{d} x,
$$

把以上三式两端分别相加,即得高斯公式(6-1).

在上述证明中,我们对闭区域 $\Omega$ 作了这样的限制,即穿过 $\Omega$ 内部且平行于坐标轴的直线与 $\Omega$ 的边界曲面 $\Sigma$ 的交点恰好是两点.如果 $\Omega$ 不满足这样的条件,可以引进几张辅助曲面把 $\Omega$ 分为有限个闭区域,使得每个闭区域满足这样的条件,并注意到沿辅助曲面相反两侧的两个曲面积分的绝对值相等而符号相反,相加时正好抵消,因此公式(6-1)对于这样的闭区域仍然是正确的.

例 1 利用高斯公式计算曲面积分

$$
\iint_ {\Sigma} (x - y) \mathrm{d} x \mathrm{d} y + (y - z) x \mathrm{d} y \mathrm{d} z,
$$

其中 $\Sigma$ 为柱面 $x^{2}+y^{2}=1$ 及平面 z=0, z=3 所围成的空间闭区域 $\Omega$ 的整个边界曲面的外侧(图 11-26).

解 因 $P = (y - z)x, Q = 0, R = x - y,$ 

$$
\frac {\partial P}{\partial x} = y - z, \quad \frac {\partial Q}{\partial y} = 0, \quad \frac {\partial R}{\partial z} = 0,
$$

利用高斯公式把所给曲面积分化为三重积分,得

$$
\oiint_ {\Sigma} (x - y) \mathrm{d} x \mathrm{d} y + (y - z) x \mathrm{d} y \mathrm{d} z = \iiint_ {\Omega} (y - z) \mathrm{d} x \mathrm{d} y \mathrm{d} z = 0 - \iiint_ {\Omega} z \mathrm{d} x \mathrm{d} y \mathrm{d} z = - \frac {9 \pi}{2},
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/452ac7b451d8d5843c828b324eb879c0e7b883c9c9917fbd7c50c459f1847705.jpg)



图11-26


其中 $\iiint_{\Omega} y \, \mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z = 0$ 由积分区域及被积函数的对称性得出.

例 2 利用高斯公式计算曲面积分

$$
\iint_ {\Sigma} \left(x ^ {2} \cos \alpha + y ^ {2} \cos \beta + z ^ {2} \cos \gamma\right) \mathrm{d} S,
$$

其中 $\Sigma$ 为锥面 $x^{2}+y^{2}=z^{2}$ 介于平面 z=0 及平面 z=h (h>0) 之间的部分的下侧, $\cos \alpha$ , $\cos \beta$ 与 $\cos \gamma$ 是 $\Sigma$ 在点 $(x,y,z)$ 处的法向量的方向余弦.

解 因曲面 $\Sigma$ 不是封闭曲面, 故不能直接利用高斯公式. 若设 $\Sigma_{1}$ 为 $z = h(x^{2} + y^{2} \leqslant h^{2})$ 的上侧, 则 $\Sigma$ 与 $\Sigma_{1}$ 一起构成一个封闭曲面, 记它们围成的空间闭区域为 $\Omega$ , 利用高斯公式, 便得

$$
\begin{array}{l} \oiint_ {\Sigma + \Sigma_ {1}} \left(x ^ {2} \cos \alpha + y ^ {2} \cos \beta + z ^ {2} \cos \gamma\right) d S \\ = 2 \iiint_ {\Omega} (x + y + z) \mathrm{d} V = 2 \iint_ {D _ {x y}} \mathrm{d} x \mathrm{d} y \int_ {\sqrt {x ^ {2} + y ^ {2}}} ^ {h} (x + y + z) \mathrm{d} z, \\ \end{array}
$$

其中 $D_{xy} = \{(x,y) | x^2 + y^2 \leqslant h^2\}$ . 注意到

$$
\iint_ {D _ {x y}} \mathrm{d} x \mathrm{d} y \int_ {\sqrt {x ^ {2} + y ^ {2}}} ^ {h} (x + y) \mathrm{d} z = 0,
$$

即得

$$
\oiint_ {\Sigma + \Sigma_ {1}} \left(x ^ {2} \cos \alpha + y ^ {2} \cos \beta + z ^ {2} \cos \gamma\right) d S = \iint_ {D _ {x y}} \left(h ^ {2} - x ^ {2} - y ^ {2}\right) d x d y = \frac {1}{2} \pi h ^ {4}.
$$

而

$$
\iint_ {\Sigma_ {1}} \left(x ^ {2} \cos \alpha + y ^ {2} \cos \beta + z ^ {2} \cos \gamma\right) \mathrm{d} S = \iint_ {\Sigma_ {1}} z ^ {2} \mathrm{d} S = \iint_ {D _ {x y}} h ^ {2} \mathrm{d} x \mathrm{d} y = \pi h ^ {4}.
$$

因此

$$
\iint_ {\Sigma} \left(x ^ {2} \cos \alpha + y ^ {2} \cos \beta + z ^ {2} \cos \gamma\right) \mathrm{d} S = \frac {1}{2} \pi h ^ {4} - \pi h ^ {4} = - \frac {1}{2} \pi h ^ {4}.
$$

例3 设函数 $u(x,y,z)$ 和 $v(x,y,z)$ 在闭区域 $\Omega$ 上具有一阶及二阶连续偏导数，证明

$$
\iiint_ {\Omega} u \Delta v \mathrm{d} x \mathrm{d} y \mathrm{d} z = \iint_ {\Sigma} u \frac {\partial v}{\partial n} \mathrm{d} S - \iiint_ {\Omega} \left(\frac {\partial u}{\partial x} \frac {\partial v}{\partial x} + \frac {\partial u}{\partial y} \frac {\partial v}{\partial y} + \frac {\partial u}{\partial z} \frac {\partial v}{\partial z}\right) \mathrm{d} x \mathrm{d} y \mathrm{d} z,
$$

其中 $\Sigma$ 是闭区域 $\Omega$ 的整个边界曲面, $\frac{\partial v}{\partial n}$ 为函数 $v(x,y,z)$ 沿 $\Sigma$ 的外法向量的方向导数, 符号 $\Delta = \frac{\partial^{2}}{\partial x^{2}} + \frac{\partial^{2}}{\partial y^{2}} + \frac{\partial^{2}}{\partial z^{2}}$ 称为拉普拉斯 (Laplace) 算子. 这个公式叫做格林第一公式.

证 因为方向导数

$$
\frac {\partial v}{\partial n} = \frac {\partial v}{\partial x} \cos \alpha + \frac {\partial v}{\partial y} \cos \beta + \frac {\partial v}{\partial z} \cos \gamma ,
$$

其中 $\cos \alpha, \cos \beta$ 与 $\cos \gamma$ 是 $\Sigma$ 在点 $(x, y, z)$ 处的外法向量的方向余弦. 于是曲面积分

$$
\begin{array}{l} \oiint_ {\Sigma} u \frac {\partial v}{\partial n} \mathrm{d} S = \oiint_ {\Sigma} u \left(\frac {\partial v}{\partial x} \cos \alpha + \frac {\partial v}{\partial y} \cos \beta + \frac {\partial v}{\partial z} \cos \gamma\right) \mathrm{d} S \\ = \iint_ {\Sigma} \left[ \left(u \frac {\partial v}{\partial x}\right) \cos \alpha + \left(u \frac {\partial v}{\partial y}\right) \cos \beta + \left(u \frac {\partial v}{\partial z}\right) \cos \gamma \right] d S. \\ \end{array}
$$

利用高斯公式,即得

$$
\begin{array}{l} \iint_ {S} u \frac {\partial v}{\partial n} \mathrm{d} S = \iiint_ {Q} \left[ \frac {\partial}{\partial x} \left(u \frac {\partial v}{\partial x}\right) + \frac {\partial}{\partial y} \left(u \frac {\partial v}{\partial y}\right) + \frac {\partial}{\partial z} \left(u \frac {\partial v}{\partial z}\right) \right] \mathrm{d} x \mathrm{d} y \mathrm{d} z \\ = \iiint_ {\Omega} u \Delta v \mathrm{d} x \mathrm{d} y \mathrm{d} z + \iiint_ {\Omega} \left(\frac {\partial u}{\partial x} \frac {\partial v}{\partial x} + \frac {\partial u}{\partial y} \frac {\partial v}{\partial y} + \frac {\partial u}{\partial z} \frac {\partial v}{\partial z}\right) \mathrm{d} x \mathrm{d} y \mathrm{d} z, \\ \end{array}
$$

将上式右端第二个积分移至左端便得所要证明的等式.

# * 二、沿任意闭曲面的曲面积分为零的条件

现在提出与第三节第二目所讨论的问题相类似的问题,这就是:在怎样的条件下,曲面积分

$$
\iint_ {\Sigma} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y
$$

与曲面 $\Sigma$ 无关而只取决于 $\Sigma$ 的边界曲线？这问题相当于在怎样的条件下，沿任意闭曲面的曲面积分为零？这问题可用高斯公式来解决.

先介绍空间二维单连通区域及一维单连通区域的概念.对空间区域G,如果G内任一闭曲面所围成的区域全属于G,则称G是空间二维单连通区域;如果G内任一闭曲线总可以张成一片完全属于G的曲面,则称G为空间一维单连通区域.例如球面所围成的区域既是空间二维单连通的,又是空间一维单连通的;环面所围成的区域是空间二维单连通的,但不是空间一维单连通的;两个同心球面之间的区域是空间一维单连通的,但不是空间二维单连通的.

对于沿任意闭曲面的曲面积分为零的条件,我们有以下结论:

定理2 设 $G$ 是空间二维单连通区域, 若 $P(x, y, z), Q(x, y, z)$ 与 $R(x, y, z)$ 在 $G$ 内具有一阶连续偏导数, 则曲面积分

$$
\iint_ {\Sigma} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y
$$

在 $G$ 内与所取曲面 $\Sigma$ 无关而只取决于 $\Sigma$ 的边界曲线（或沿 $G$ 内任一闭曲面的曲面积分为零）的充分必要条件是

$$
\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z} = 0 \tag {6-4}
$$

在 $G$ 内恒成立.

证 若等式(6-4)在 G 内恒成立,则由高斯公式(6-1)立即可看出沿 G 内的任意闭曲面的曲面积分为零,因此条件(6-4)是充分的.反之,设沿 G 内的任一闭曲面的曲面积分为零,若等式(6-4)在 G 内不恒成立,就是说在 G 内至少有一点 $M_{0}$ 使得

$$
\left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) _ {M _ {0}} \neq 0,
$$

仿照第三节第二目中所用的方法,就可得出 G 内存在着闭曲面使得沿该闭曲面的曲面积分不等于零,这与假设相矛盾.因此条件(6-4)是必要的.证毕.

# *三、通量与散度

设有向量场

$$
\boldsymbol {A} (x, y, z) = P (x, y, z) \boldsymbol {i} + Q (x, y, z) \boldsymbol {j} + R (x, y, z) \boldsymbol {k},
$$

其中函数 P, Q 与 R 均具有一阶连续偏导数, $\Sigma$ 是场内的一片有向曲面, n 是 $\Sigma$ 在点 $(x, y, z)$ 处的单位法向量, 则积分

$$
\iint_ {\Sigma} \boldsymbol {A} \cdot \boldsymbol {n} \mathrm{d} S
$$

称为向量场 A 通过曲面 $\Sigma$ 向着指定侧的通量(或流量).

由两类曲面积分的关系,通量又可表达为

$$
\iint_ {\Sigma} \boldsymbol {A} \cdot \boldsymbol {n} \mathrm{d} S = \iint_ {\Sigma} \boldsymbol {A} \cdot \mathrm{d} S = \iint_ {\Sigma} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y.
$$

例 4 求向量场 $A = yzj + z^{2}k$ 穿过曲面 $\Sigma$ 流向上侧的通量, 其中 $\Sigma$ 为柱面 $y^{2} + z^{2} = 1 (z \geqslant 0)$ 被平面 x = 0 及 x = 1 截下的有限部分(图 11-27).

解 曲面 $\Sigma$ 上侧的法向量可以由

$$
f (x, y, z) = y ^ {2} + z ^ {2}
$$

的梯度 $\nabla f$ 得出，即

$$
\boldsymbol {n} = \frac {\nabla f}{| \nabla f |} = \frac {2 y \boldsymbol {j} + 2 z \boldsymbol {k}}{\sqrt {(2 y) ^ {2} + (2 z) ^ {2}}} = y \boldsymbol {j} + z \boldsymbol {k} \quad (y ^ {2} + z ^ {2} = 1).
$$

在曲面 $\Sigma$ 上，

$$
\boldsymbol {A} \cdot \boldsymbol {n} = y ^ {2} z + z ^ {3} = z (y ^ {2} + z ^ {2}) = z.
$$

因此，A 穿过 $\Sigma$ 流向上侧的通量为

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/be90bd593abb36fe11d2f8f1e34ff6b7f0a52d5fe48d29590513ff399991ab4a.jpg)



图11-27


$$
\iint_ {\Sigma} \boldsymbol {A} \cdot \boldsymbol {n} \mathrm{d} S = \iint_ {\Sigma} z \mathrm{d} S = \iint_ {D _ {x y}} \sqrt {1 - y ^ {2}} \cdot \frac {1}{\sqrt {1 - y ^ {2}}} \mathrm{d} x \mathrm{d} y = \iint_ {D _ {x y}} \mathrm{d} x \mathrm{d} y = 2.
$$

下面我们来解释高斯公式

$$
\iiint_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm{d} V = \iint_ {\Sigma} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y \tag {6-1}
$$

的物理意义.

设在闭区域 $\Omega$ 上有稳定流动的、不可压缩的流体（假定流体的密度为1）的速度场

$$
\boldsymbol {v} (x, y, z) = P (x, y, z) \boldsymbol {i} + Q (x, y, z) \boldsymbol {j} + R (x, y, z) \boldsymbol {k},
$$

其中函数 $P, Q$ 与 $R$ 均具有一阶连续偏导数， $\Sigma$ 是闭区域 $\Omega$ 的边界曲面的外侧， $n$ 是曲面 $\Sigma$ 在点 $(x, y, z)$ 处的单位法向量，则由第五节第一目知道，单位时间内流体经过曲面 $\Sigma$ 流向指定侧的流体总质量就是

$$
\iint_ {\Sigma} \boldsymbol {v} \cdot \boldsymbol {n} \mathrm{d} S = \iint_ {\Sigma} v _ {n} \mathrm{d} S = \iint_ {\Sigma} P \mathrm{d} y \mathrm{d} z + Q \mathrm{d} z \mathrm{d} x + R \mathrm{d} x \mathrm{d} y.
$$

因此,高斯公式(6-1)的右端可解释为速度场 v 通过闭曲面 $\Sigma$ 流向外侧的通量,即流体在单位时间内离开闭区域 $\Omega$ 的总质量.由于我们假定流体是不可压缩且流动是稳定的,因此在流体离开 $\Omega$ 的同时, $\Omega$ 内部必须有产生流体的“源头”产生出同样多的流体来进行补充.所以高斯公式(6-1)的左端可解释为分布在 $\Omega$ 内的源头在单位时间内所产生的流体的总质量.

为简便起见,把高斯公式(6-1)改写成

$$
\iiint_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm{d} V = \iint_ {\Sigma} v _ {n} \mathrm{d} S.
$$

以闭区域 $\Omega$ 的体积 V 除上式两端, 得

$$
\frac {1}{V} \iiint_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm{d} V = \frac {1}{V} \iint_ {\Sigma} v _ {n} \mathrm{d} S.
$$

上式左端表示 $\Omega$ 内的源头在单位时间单位体积内所产生的流体质量的平均值.应用积分中值定理于上式左端,得

$$
\left. \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \right| _ {(\xi , \eta , \zeta)} = \frac {1}{V} \iint_ {\Sigma} v _ {n} \mathrm{d} S,
$$

这里 $(\xi, \eta, \zeta)$ 是 $\Omega$ 内的某个点. 令 $\Omega$ 缩向一点 $M(x, y, z)$ , 取上式的极限, 得

$$
\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z} = \lim _ {\Omega \rightarrow M} \frac {1}{V} \iint_ {\Sigma} v _ {n} \mathrm{d} S.
$$

上式左端称为速度场 v 在点 M 的通量密度或散度, 记作 div $v(M)$ , 即

$$
\operatorname{div} \boldsymbol {v} (M) = \frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}.
$$

$\operatorname{div} \boldsymbol{v}(M)$ 在这里可看做稳定流动的不可压缩流体在点 $M$ 的源头强度. 在 $\operatorname{div} \boldsymbol{v}(M) > 0$ 的点处,流体从该点向外发散,表示流体在该点处有正源;在 $\mathrm{div}\boldsymbol{v}(M)<0$ 的点处,流体向该点汇聚,表示流体在该点处有吸收流体的负源(又称为汇或洞);在 $\mathrm{div}\boldsymbol{v}(M)=0$ 的点处,表示流体在该点处无源.

对于一般的向量场

$$
\boldsymbol {A} (x, y, z) = P (x, y, z) \boldsymbol {i} + Q (x, y, z) \boldsymbol {j} + R (x, y, z) \boldsymbol {k},
$$

$\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$ 叫做向量场A的散度，记作divA，即

$$
\operatorname{div} A = \frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}.
$$

利用向量微分算子 $\nabla, A$ 的散度 $\operatorname{div} A$ 也可表达为 $\nabla \cdot A$ , 即

$$
\operatorname{div} \boldsymbol {A} = \nabla \cdot \boldsymbol {A}.
$$

如果向量场 A 的散度 div A 处处为零,那么称向量场 A 为无源场.

例 5 求例 4 中的向量场 A 的散度.

解 $\operatorname{div} A = \nabla \cdot A = \frac{\partial}{\partial y}(yz) + \frac{\partial}{\partial z}(z^2) = z + 2z = 3z.$ 

利用向量场的通量和散度,高斯公式可以写成下面的向量形式

$$
\iiint_ {\Omega} \mathrm{div} A \mathrm{d} V = \iint_ {\Sigma} A _ {n} \mathrm{d} S \tag {6-5}
$$

或

$$
\iiint_ {\Omega} \nabla \cdot A \mathrm{d} V = \iint_ {\Sigma} A _ {n} \mathrm{d} S. \tag {$6-5^{\prime$}}
$$

高斯公式(6-5)表示:向量场 A 通过闭曲面 $\Sigma$ 流向外侧的通量等于向量场 A 的散度在闭曲面 $\Sigma$ 所围闭区域 $\Omega$ 上的积分.

# 习题11-6

1. 利用高斯公式计算曲面积分：

(1) $\iint_{\Sigma} x^{2} dy dz + y^{2} dz dx + z^{2} dx dy$ ，其中 $\Sigma$ 为平面 x = 0, y = 0, z = 0, x = a, y = a, z = a 所围成的立体的表面的外侧；

* (2) $\iint_{\Sigma} x^{3} \mathrm{d}y \mathrm{d}z + y^{3} \mathrm{d}z \mathrm{d}x + z^{3} \mathrm{d}x \mathrm{d}y$ ，其中 $\Sigma$ 为球面 $x^{2} + y^{2} + z^{2} = a^{2}$ 的外侧；

$^{*}$ (3) $\oiint_{\Sigma}xz^{2}\mathrm{d}y\mathrm{d}z+(x^{2}y-z^{3})\mathrm{d}z\mathrm{d}x+(2xy+y^{2}z)\mathrm{d}x\mathrm{d}y$ ，其中 $\Sigma$ 为上半球体 $0\leqslant z\leqslant\sqrt{a^{2}-x^{2}-y^{2}}$ ， $x^{2}+y^{2}\leqslant a^{2}$ 的表面的外侧；

(4) $\iint_{\Sigma} x \, \mathrm{d}y \, \mathrm{d}z + y \, \mathrm{d}z \, \mathrm{d}x + z \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $\Sigma$ 是界于 $z = 0$ 和 $z = 3$ 之间的圆柱体 $x^2 + y^2 \leqslant 9$ 的整个表面的

外侧；

(5) $\oiint_{\Sigma} 4xz \mathrm{~d} y \mathrm{~d} z - y^2 \mathrm{~d} z \mathrm{~d} x + y z \mathrm{~d} x \mathrm{~d} y$ ，其中 $\Sigma$ 是平面 $x = 0, y = 0, z = 0, x = 1, y = 1, z = 1$ 所围成的立方体的全表面的外侧.

*2. 求下列向量 $A$ 穿过曲面 $\Sigma$ 流向指定侧的通量:

(1) $A = yzi + xzj + xyk, \Sigma$ 为圆柱 $x^{2} + y^{2} \leqslant a^{2}$ $(0 \leqslant z \leqslant h)$ 的全表面，流向外侧；

(2) $A=(2x-z)i+x^{2}yj-xz^{2}k,\Sigma$ 为立方体 $0\leqslant x\leqslant a,0\leqslant y\leqslant a,0\leqslant z\leqslant a$ 的全表面，流向外侧；

(3) $A=(2x+3z)i-(xz+y)j+(y^{2}+2z)k,\Sigma$ 是以点 $(3,-1,2)$ 为球心，半径R=3的球面，流向外侧.

*3. 求下列向量场 $A$ 的散度:

(1) $A=(x^{2}+yz)i+(y^{2}+xz)j+(z^{2}+xy)k;$ 

(2) $A = e^{xy}i + \cos(xy)j + \cos(xz^2)k;$ 

(3) $A=y^{2}i+xyj+xzk.$ 

4. 设 $u(x, y, z), v(x, y, z)$ 是两个定义在闭区域 $\Omega$ 上的具有二阶连续偏导数的函数， $\frac{\partial u}{\partial n}, \frac{\partial v}{\partial n}$ 依次表示 $u(x, y, z), v(x, y, z)$ 沿 $\Sigma$ 的外法线方向的方向导数。证明：

$$
\iiint_ {\Omega} (u \Delta v - v \Delta u) \mathrm{d} x \mathrm{d} y \mathrm{d} z = \iint_ {\Sigma} \left(u \frac {\partial v}{\partial n} - v \frac {\partial u}{\partial n}\right) \mathrm{d} S,
$$

其中 $\Sigma$ 是空间闭区域 $\Omega$ 的整个边界曲面. 这个公式叫做格林第二公式.

*5. 利用高斯公式推证阿基米德原理: 浸没在液体中的物体所受液体的压力的合力(即浮力)的方向铅直向上, 其大小等于该物体所排开的液体所受的重力.

# 第七节 斯托克斯公式 * 环流量与旋度

# 一、斯托克斯公式

斯托克斯(Stokes)公式是格林公式的推广.格林公式表达了平面闭区域上的二重积分与其边界曲线上的曲线积分间的关系,而斯托克斯公式则把曲面 $\Sigma$ 上的曲面积分与沿着 $\Sigma$ 的边界曲线的曲线积分联系起来.这个联系可陈述如下:

定理1 设 $\Gamma$ 为分段光滑的空间有向闭曲线, $\Sigma$ 是以 $\Gamma$ 为边界的分片光滑的有向曲面, $\Gamma$ 的正向与 $\Sigma$ 的侧符合右手规则①, 若函数 $P(x,y,z), Q(x,y,z)$ 与 $R(x,y,z)$ 在曲面 $\Sigma$ (连同边界 $\Gamma$ ) 上具有一阶连续偏导数, 则有

$$
\iint_ {\Sigma} \left(\frac {\partial R}{\partial y} - \frac {\partial Q}{\partial z}\right) \mathrm{d} y \mathrm{d} z + \left(\frac {\partial P}{\partial z} - \frac {\partial R}{\partial x}\right) \mathrm{d} z \mathrm{d} x + \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y = \oint_ {r} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z. (7 - 1)
$$

公式(7-1)叫做斯托克斯公式.

证 先假定 $\Sigma$ 与平行于 $z$ 轴的直线相交不多于一点，并设 $\Sigma$ 为曲面 $z = f(x, y)$ 的上侧， $\Sigma$ 的正向边界曲线 $\Gamma$ 在 $xOy$ 面上的投影为平面有向曲线 $C, C$ 所围成的闭区域为 $D_{xy}$ （图11-28）.

我们设法把曲面积分

$$
\iint_ {\Sigma} \frac {\partial P}{\partial z} \mathrm{d} z \mathrm{d} x - \frac {\partial P}{\partial y} \mathrm{d} x \mathrm{d} y
$$

化为闭区域 $D_{xy}$ 上的二重积分, 然后通过格林公式使它与曲线积分相联系.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/16705cd061e355c09ffde701052473ea1c8db0fde871f8d395debba2e03f27bb.jpg)



图11-28


根据对面积的和对坐标的曲面积分间的关系,有

$$
\iint_ {\Sigma} \frac {\partial P}{\partial z} \mathrm{d} z \mathrm{d} x - \frac {\partial P}{\partial y} \mathrm{d} x \mathrm{d} y = \iint_ {\Sigma} \left(\frac {\partial P}{\partial z} \cos \beta - \frac {\partial P}{\partial y} \cos \gamma\right) \mathrm{d} S. \tag {7-2}
$$

由第九章第六节知道,有向曲面 $\Sigma$ 的法向量的方向余弦为

$$
\cos \alpha = \frac {- f _ {x}}{\sqrt {1 + f _ {x} ^ {2} + f _ {y} ^ {2}}}, \quad \cos \beta = \frac {- f _ {y}}{\sqrt {1 + f _ {x} ^ {2} + f _ {y} ^ {2}}}, \quad \cos \gamma = \frac {1}{\sqrt {1 + f _ {x} ^ {2} + f _ {y} ^ {2}}},
$$

因此 $\cos\beta=-f_{y}\cos\gamma$ ，把它代入(7-2)式得

$$
\iint_ {\Sigma} \frac {\partial P}{\partial z} \mathrm{d} z \mathrm{d} x - \frac {\partial P}{\partial y} \mathrm{d} x \mathrm{d} y = - \iint_ {\Sigma} \left(\frac {\partial P}{\partial y} + \frac {\partial P}{\partial z} f _ {y}\right) \cos \gamma \mathrm{d} S,
$$

即

$$
\iint_ {\Sigma} \frac {\partial P}{\partial z} \mathrm{d} z \mathrm{d} x - \frac {\partial P}{\partial y} \mathrm{d} x \mathrm{d} y = - \iint_ {\Sigma} \left(\frac {\partial P}{\partial y} + \frac {\partial P}{\partial z} f _ {y}\right) \mathrm{d} x \mathrm{d} y. \tag {7-3}
$$

上式右端的曲面积分化为二重积分时,应把 $P(x,y,z)$ 中的 z 用 $f(x,y)$ 来代替.因为由复合函数的微分法,有

$$
\frac {\partial}{\partial y} P [ x, y, f (x, y) ] = \frac {\partial P}{\partial y} + \frac {\partial P}{\partial z} f _ {y}.
$$

所以，(7-3)式可写成

$$
\iint_ {\Sigma} \frac {\partial P}{\partial z} \mathrm{d} z \mathrm{d} x - \frac {\partial P}{\partial y} \mathrm{d} x \mathrm{d} y = - \iint_ {D _ {x y}} \frac {\partial}{\partial y} P [ x, y, f (x, y) ] \mathrm{d} x \mathrm{d} y.
$$

根据格林公式,上式右端的二重积分可化为沿闭区域 $D_{xy}$ 的边界 C 的曲线积分

$$
- \iint_ {D _ {x y}} \frac {\partial}{\partial y} P [ x, y, f (x, y) ] \mathrm{d} x \mathrm{d} y = \oint_ {C} P [ x, y, f (x, y) ] \mathrm{d} x,
$$

于是

$$
\iint_ {\Sigma} \frac {\partial P}{\partial z} \mathrm{d} z \mathrm{d} x - \frac {\partial P}{\partial y} \mathrm{d} x \mathrm{d} y = \oint_ {c} P [ x, y, f (x, y) ] \mathrm{d} x.
$$

因为函数 $P[x, y, f(x, y)]$ 在曲线 $C$ 上点 $(x, y)$ 处的值与函数 $P(x, y, z)$ 在曲线 $\Gamma$ 上对应点 $(x, y, z)$ 处的值是一样的，并且两曲线上的对应小弧段在 $x$ 轴上的投影也一样，根据曲线积分的定义，上式右端的曲线积分等于曲线 $\Gamma$ 上的曲线积分 $\int_{\Gamma} P(x, y, z) \mathrm{d}x$ 。因此，我们证得

$$
\iint_ {\Sigma} \frac {\partial P}{\partial z} \mathrm{d} z \mathrm{d} x - \frac {\partial P}{\partial y} \mathrm{d} x \mathrm{d} y = \oint_ {\Gamma} P (x, y, z) \mathrm{d} x. \tag {7-4}
$$

如果 $\Sigma$ 取下侧, $\Gamma$ 也相应地改成相反的方向, 那么(7-4)式两端同时改变符号, 因此(7-4)式仍成立.

其次,如果曲面与平行于 $z$ 轴的直线的交点多于一个,那么可作辅助曲线把曲面分成几部分,然后应用公式(7-4)并相加.因为沿辅助曲线而方向相反的两个曲线积分相加时正好抵消,所以对于这一类曲面公式(7-4)也成立.

同样可证

$$
\iint_ {\Sigma} \frac {\partial Q}{\partial x} \mathrm{d} x \mathrm{d} y - \frac {\partial Q}{\partial z} \mathrm{d} y \mathrm{d} z = \oint_ {\Gamma} Q \mathrm{d} y,
$$

$$
\iint_ {\Sigma} \frac {\partial R}{\partial y} \mathrm{d} y \mathrm{d} z - \frac {\partial R}{\partial x} \mathrm{d} z \mathrm{d} x = \oint_ {r} R \mathrm{d} z.
$$

把它们与公式(7-4)相加即得公式(7-1).证毕.

为了便于记忆,利用行列式记号把斯托克斯公式(7-1)写成

$$
\iint_ {\Sigma} \left| \begin{array}{c c c} \mathrm{d} y \mathrm{d} z & \mathrm{d} z \mathrm{d} x & \mathrm{d} x \mathrm{d} y \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ P & Q & R \end{array} \right| = \oint_ {r} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z,
$$

把其中的行列式按第一行展开,并把 $\frac{\partial}{\partial y}$ 与R的“积”理解为 $\frac{\partial R}{\partial y},\frac{\partial}{\partial z}$ 与Q的“积”理解为 $\frac{\partial Q}{\partial z}$ ,等等,于是这个行列式就“等于”

$$
\left(\frac {\partial R}{\partial y} - \frac {\partial Q}{\partial z}\right) \mathrm{d} y \mathrm{d} z + \left(\frac {\partial P}{\partial z} - \frac {\partial R}{\partial x}\right) \mathrm{d} z \mathrm{d} x + \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y.
$$

这恰好是公式(7-1)左端的被积表达式.

利用两类曲面积分间的联系,可得斯托克斯公式的另一形式

$$
\iint_ {\Sigma} \left| \begin{array}{c c c} \cos \alpha & \cos \beta & \cos \gamma \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ P & Q & R \end{array} \right| \mathrm{d} S = \oint_ {\Gamma} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z,
$$

其中 $n=(\cos\alpha,\cos\beta,\cos\gamma)$ 为有向曲面 $\Sigma$ 在点 $(x,y,z)$ 处的单位法向量.

如果 $\Sigma$ 是 xOy 面上的一块平面闭区域, 斯托克斯公式就变成格林公式. 因此, 格林公式是斯托克斯公式的一种特殊情形.

例1 利用斯托克斯公式计算曲线积分 $\oint_{\Gamma} z \mathrm{d}x + x \mathrm{d}y + y \mathrm{d}z$ ，其中 $\Gamma$ 为平面 $x + y + z = 1$ 被三个坐标面所截成的三角形的整个边界，它的正向与这个平面三角形 $\Sigma$ 上侧的法向量之间符合右手规则（图11-29）.

解 按斯托克斯公式,有

$$
\oint_ {\Gamma} z \mathrm{d} x + x \mathrm{d} y + y \mathrm{d} z = \iint_ {\Sigma} \mathrm{d} y \mathrm{d} z + \mathrm{d} z \mathrm{d} x + \mathrm{d} x \mathrm{d} y.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/3b1e50648f2e0abe95b26612ac84cc873f3e5918e08d883ef9b3d1a6c5ee989a.jpg)



图11-29


而

$$
\iint_ {\Sigma} \mathrm{d} y \mathrm{d} z = \iint_ {D _ {y z}} \mathrm{d} \sigma = \frac {1}{2},
$$

$$
\iint_ {\Sigma} \mathrm{d} z \mathrm{d} x = \iint_ {D _ {z x}} \mathrm{d} \sigma = \frac {1}{2},
$$

$$
\iint_ {\Sigma} \mathrm{d} x \mathrm{d} y = \iint_ {D _ {x y}} \mathrm{d} \sigma = \frac {1}{2},
$$

其中 $D_{yz}, D_{zx}$ 与 $D_{xy}$ 分别为 $\Sigma$ 在 $yOz, zOx$ 与 $xOy$ 面上的投影区域，因此

$$
\oint_ {\Gamma} z \mathrm{d} x + x \mathrm{d} y + y \mathrm{d} z = \frac {3}{2}.
$$

例2 利用斯托克斯公式计算曲线积分

$$
I = \oint_ {\Gamma} (y ^ {2} - z ^ {2}) \mathrm{d} x + (z ^ {2} - x ^ {2}) \mathrm{d} y + (x ^ {2} - y ^ {2}) \mathrm{d} z,
$$

其中 $\Gamma$ 是用平面 $x + y + z = \frac{3}{2}$ 截立方体 $\{(x,y,z) | 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1, 0 \leqslant z \leqslant 1\}$ 的表面所得的截痕，若从 $x$ 轴的正向看去，取逆时针方向（图11-30(a)).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/6997325f2bd723ae95b4d538210d4e4491ffcbd5b3b0fcb13ab339589db96ba3.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/ac3778abd14cf7b10e6857ec28b0339569888402dc4fbca9a599524be202acf3.jpg)



(b)



图11-30


解 取 $\Sigma$ 为平面 $x+y+z=\frac{3}{2}$ 的上侧被 $\Gamma$ 所围成的部分, $\Sigma$ 的单位法向量 $n=\frac{1}{\sqrt{3}}(1,1,1)$ , 即 $\cos\alpha=\cos\beta=\cos\gamma=\frac{1}{\sqrt{3}}$ . 按斯托克斯公式, 有

$$
I = \iint_ {\Sigma} \left| \begin{array}{c c c} \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {3}} \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ y ^ {2} - z ^ {2} & z ^ {2} - x ^ {2} & x ^ {2} - y ^ {2} \end{array} \right| \mathrm{d} S = - \frac {4}{\sqrt {3}} \iint_ {\Sigma} (x + y + z) \mathrm{d} S.
$$

因为在 $\Sigma$ 上 $x + y + z = \frac{3}{2}$ , 故

$$
I = - \frac {4}{\sqrt {3}} \times \frac {3}{2} \iint_ {\Sigma} \mathrm{d} S = - 2 \sqrt {3} \iint_ {D _ {x y}} \sqrt {3} \mathrm{d} x \mathrm{d} y = - 6 \sigma_ {x y},
$$

其中 $D_{xy}$ 为 $\Sigma$ 在 $xOy$ 平面上的投影区域（图11-30(b))， $\sigma_{xy}$ 为 $D_{xy}$ 的面积，因

$$
\sigma_ {x y} = 1 - 2 \times \frac {1}{8} = \frac {3}{4}
$$

故

$$
I = - \frac {9}{2}.
$$

# * 二、空间曲线积分与路径无关的条件

在第三节中,利用格林公式推得了平面曲线积分与路径无关的条件.完全类似地,利用斯托克斯公式,可推得空间曲线积分与路径无关的条件.

首先我们指出,空间曲线积分与路径无关相当于沿任意闭曲线的曲线积分为零.关于空间曲线积分在什么条件下与路径无关的问题,有以下结论:

定理2 设空间区域 $G$ 是一维单连通区域, 若函数 $P(x, y, z), Q(x, y, z)$ 与 $R(x, y, z)$ 在 $G$ 内具有一阶连续偏导数, 则空间曲线积分 $\int_{\Gamma} P \mathrm{d}x + Q \mathrm{d}y + R \mathrm{d}z$ 在 $G$ 内与路径无关 (或沿 $G$ 内任意闭曲线的曲线积分为零) 的充分必要条件是

$$
\frac {\partial P}{\partial y} = \frac {\partial Q}{\partial x}, \quad \frac {\partial Q}{\partial z} = \frac {\partial R}{\partial y}, \quad \frac {\partial R}{\partial x} = \frac {\partial P}{\partial z} \tag {7-5}
$$

在 $G$ 内恒成立.

证 如果等式(7-5)在 $G$ 内恒成立, 那么由斯托克斯公式(7-1)立即可看出, 沿闭曲线的曲线积分为零, 因此条件是充分的. 反之, 设沿 $G$ 内任意闭曲线的曲线积分为零, 若 $G$ 内有一点 $M_0$ 使(7-5)式中的三个等式不完全成立, 例如 $\frac{\partial P}{\partial y} \neq \frac{\partial Q}{\partial x}$ . 不妨假定

$$
\left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) _ {M _ {0}} = \eta > 0.
$$

过点 $M_0(x_0, y_0, z_0)$ 作平面 $z = z_0$ ，并在这个平面上取一个以 $M_0$ 为圆心、半径足够小的圆形闭区域 $K$ ，使得在 $K$ 上恒有

$$
\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y} \geqslant \frac {\eta}{2}.
$$

设 $\gamma$ 是 $K$ 的正向边界曲线. 因为 $\gamma$ 在平面 $z = z_0$ 上, 所以按定义有

$$
\oint_ {\gamma} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z = \oint_ {\gamma} P \mathrm{d} x + Q \mathrm{d} y.
$$

又由(7-1)式有

$$
\oint_ {\gamma} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z = \iint_ {K} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm{d} x \mathrm{d} y \geqslant \frac {\eta}{2} \cdot \sigma ,
$$

其中 $\sigma$ 是 K 的面积, 因为 $\eta > 0, \sigma > 0$ , 从而

$$
\oint_ {\gamma} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z > 0.
$$

这结果与假设矛盾,从而(7-5)式在 G 内恒成立.证毕.

应用定理 2 并仿照第三节定理 3 的证法,便可以得到

定理3 设区域 $G$ 是空间一维单连通区域，若函数 $P(x, y, z), Q(x, y, z)$ 与 $R(x, y, z)$ 在 $G$ 内具有一阶连续偏导数，则表达式 $P \mathrm{d}x + Q \mathrm{d}y + R \mathrm{d}z$ 在 $G$ 内成为某一函数 $u(x, y, z)$ 的全微分的充分必要条件是等式(7-5)在 $G$ 内恒成立；当条件(7-5)满足时,这个函数(不计一常数之差)可用下式求出:

$$
u (x, y, z) = \int_ {(x _ {0}, y _ {0}, z _ {0})} ^ {(x, y, z)} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z \tag {7-6}
$$

或用定积分表示为(按图 11-31 取积分路径,且此积分路径在 G 内)

$$
\begin{array}{l} u (x, y, z) = \int_ {x _ {0}} ^ {x} P (x, y _ {0}, z _ {0}) \mathrm{d} x + \int_ {y _ {0}} ^ {y} Q (x, y, z _ {0}) \mathrm{d} y + \\ \int_ {z _ {0}} ^ {z} R (x, y, z) \mathrm{d} z. \tag {$7-6^{\prime$}} \\ \end{array}
$$

其中 $M_0(x_0,y_0,z_0)$ 为 $G$ 内某一定点，点 $M(x,y,z)\in G$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/33270ca941f81344b18eaafd0bbd937971696d7f266b6b4e47b020c52b685a38.jpg)



图11-31


# * 三、环流量与旋度

设有向量场

$$
A (x, y, z) = P (x, y, z) i + Q (x, y, z) j + R (x, y, z) k,
$$

其中函数 P, Q 与 R 均连续, $\Gamma$ 是 A 的定义域内的一条分段光滑的有向闭曲线, $\tau$ 是 $\Gamma$ 在点 $(x, y, z)$ 处的单位切向量, 则积分

$$
\oint_ {\Gamma} \boldsymbol {A} \cdot \boldsymbol {\tau} d s
$$

称为向量场 A 沿有向闭曲线 $\Gamma$ 的环流量.

由两类曲线积分的关系,环流量又可表达为

$$
\oint_ {\Gamma} \boldsymbol {A} \cdot \boldsymbol {\tau} \mathrm{d} s = \oint_ {\Gamma} \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {r} = \oint_ {\Gamma} P \mathrm{d} x + Q \mathrm{d} y + R \mathrm{d} z.
$$

例3 求向量场 $A = (x^{2} - y)i + 4zj + x^{2}k$ 沿闭曲线 $\Gamma$ 的环流量, 其中 $\Gamma$ 为锥面 $z = \sqrt{x^2 + y^2}$ 和平面 $z = 2$ 的交线, 从 $z$ 轴正向看 $\Gamma$ 为逆时针方向.

解 $\Gamma$ 的向量方程为

$$
r = 2 \cos \theta i + 2 \sin \theta j + 2 k, \quad 0 \leqslant \theta \leqslant 2 \pi .
$$

于是

$$
\boldsymbol {A} = (x ^ {2} - y) \boldsymbol {i} + 4 z \boldsymbol {j} + x ^ {2} \boldsymbol {k} = (4 \cos^ {2} \theta - 2 \sin \theta) \boldsymbol {i} + 8 \boldsymbol {j} + 4 \cos^ {2} \theta \boldsymbol {k},
$$

$$
\mathrm{d} \boldsymbol {r} = (- 2 \sin \theta \mathrm{d} \theta) \boldsymbol {i} + (2 \cos \theta \mathrm{d} \theta) \boldsymbol {j},
$$

$$
\oint_ {\Gamma} \boldsymbol {A} \cdot \boldsymbol {\tau} \mathrm{d} s = \oint_ {\Gamma} \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {r} = \int_ {0} ^ {2 \pi} (- 8 \cos^ {2} \theta \sin \theta + 4 \sin^ {2} \theta + 1 6 \cos \theta) \mathrm{d} \theta = 4 \pi .
$$

类似于由向量场 A 的通量可以引出向量场 A 在一点的通量密度(即散度)一样, 由向量场 A 沿一闭曲线的环流量可引出向量场 A 在一点的环量密度或旋度. 它是一个向量, 定义如下:

设有一向量场

$$
\boldsymbol {A} (x, y, z) = P (x, y, z) \boldsymbol {i} + Q (x, y, z) \boldsymbol {j} + R (x, y, z) \boldsymbol {k},
$$

其中函数 $P, Q$ 与 $R$ 均具有一阶连续偏导数, 则向量

$$
\left(\frac {\partial R}{\partial y} - \frac {\partial Q}{\partial z}\right) i + \left(\frac {\partial P}{\partial z} - \frac {\partial R}{\partial x}\right) j + \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) k
$$

称为向量场 A 的旋度, 记作 rot A, 即

$$
\mathbf {r o t} \boldsymbol {A} = \left(\frac {\partial R}{\partial y} - \frac {\partial Q}{\partial z}\right) \boldsymbol {i} + \left(\frac {\partial P}{\partial z} - \frac {\partial R}{\partial x}\right) \boldsymbol {j} + \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \boldsymbol {k}. \tag {7-7}
$$

利用向量微分算子 $\nabla$ ，向量场 $A$ 的旋度 $\operatorname{rot} A$ 可表示为 $\nabla \times A$ ，即

$$
\mathbf {r o t} \boldsymbol {A} = \nabla \times \boldsymbol {A} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ P & Q & R \end{array} \right|.
$$

若向量场 A 的旋度 rot A 处处为零, 则称向量场 A 为无旋场. 而一个无源且无旋的向量场称为调和场. 调和场是物理学中另一类重要的向量场, 这种场与调和函数有密切的关系.

例 4 求例 3 中的向量场 A 的旋度.

解

$$
\operatorname{rot} A = \nabla \times A = \left| \begin{array}{c c c} i & j & k \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ x ^ {2} - y & 4 z & x ^ {2} \end{array} \right| = - 4 i - 2 x j + k.
$$

设斯托克斯公式中的有向曲面 $\Sigma$ 在点 $(x, y, z)$ 处的单位法向量为

$$
\boldsymbol {n} = \cos \alpha i + \cos \beta j + \cos \gamma k,
$$

则

$$
\operatorname{rot} \boldsymbol {A} \cdot \boldsymbol {n} = \nabla \times \boldsymbol {A} \cdot \boldsymbol {n} = \left| \begin{array}{c c c} \cos \alpha & \cos \beta & \cos \gamma \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ P & Q & R \end{array} \right|.
$$

于是,斯托克斯公式可以写成下面的向量形式

$$
\iint_ {\Sigma} \mathbf {r o t} \boldsymbol {A} \cdot \boldsymbol {n} \mathrm{d} S = \oint_ {\Gamma} \boldsymbol {A} \cdot \boldsymbol {\tau} \mathrm{d} s \tag {7-8}
$$

或

$$
\iint_ {\Sigma} (\mathbf {r o t} A) _ {n} \mathrm{d} S = \oint_ {\Gamma} A _ {\tau} \mathrm{d} s. \tag {$7-8^{\prime$}}
$$

斯托克斯公式(7-8)表示:向量场A沿有向闭曲线 $\Gamma$ 的环流量等于向量场A的旋度通过曲面 $\Sigma$ 的通量,这里 $\Gamma$ 的正向与 $\Sigma$ 的侧应符合右手规则.

最后,我们从力学角度来对 rot A 的含义作些解释.

设有刚体绕定轴 l 转动, 角速度为 $\omega, M$ 为刚体内任意一点. 在定轴 l 上任取一点 O 为坐标原点, 作空间直角坐标系, 使 z 轴与定轴 l 重合, 则 $\omega = \omega k$ , 而点 M 可用向量 $r = \overrightarrow{OM} = (x, y, z)$ 来确定. 由力学知道, 点 M 的线速度 v 可表示为

$$
v = \omega \times r.
$$

由此有

$$
\boldsymbol {v} = \left| \begin{array}{c c c} {\boldsymbol {i}} & {\boldsymbol {j}} & {\boldsymbol {k}} \\ {0} & {0} & {\omega} \\ {x} & {\gamma} & {z} \end{array} \right| = (- \omega y, \omega x, 0) ,
$$

而

$$
\operatorname{rot} \boldsymbol {v} = \left| \begin{array}{c c c} i & j & k \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ - \omega y & \omega x & 0 \end{array} \right| = (0, 0, 2 \omega) = 2 \omega .
$$

从速度场 v 的旋度与旋转角速度的这个关系, 可见“旋度”这一名词的由来.

# 习题11-7

1. 试对曲面 $\Sigma: z = x^2 + y^2, x^2 + y^2 \leqslant 1, P = y^2, Q = x, R = z^2$ 验证斯托克斯公式.

*2. 利用斯托克斯公式,计算下列曲线积分:

(1) $\oint_{\Gamma} y \mathrm{~d} x + z \mathrm{~d} y + x \mathrm{~d} z$ ，其中 $\Gamma$ 为圆周 $x^{2} + y^{2} + z^{2} = a^{2}, x + y + z = 0$ ，若从 $x$ 轴的正向看去，这圆周是取逆时针方向；

(2) $\oint_{\Gamma}(y - z)\mathrm{d}x + (z - x)\mathrm{d}y + (x - y)\mathrm{d}z$ ，其中 $\Gamma$ 为椭圆 $x^{2} + y^{2} = a^{2}, \frac{x}{a} + \frac{z}{b} = 1 (a > 0, b > 0)$ ，若从 $x$ 轴正向看去，这椭圆取逆时针方向；

(3) $\oint_{\Gamma} 3y \mathrm{~d} x - x z \mathrm{~d} y + y z^{2} \mathrm{~d} z$ ，其中 $\Gamma$ 是圆周 $x^{2} + y^{2} = 2z, z = 2$ ，若从 $z$ 轴正向看去，这圆周取逆时针方向；

(4) $\oint_{\Gamma} 2y \mathrm{~d} x + 3x \mathrm{~d} y - z^2 \mathrm{~d} z$ ，其中 $\Gamma$ 是圆周 $x^2 + y^2 + z^2 = 9, z = 0$ ，若从 $z$ 轴正向看去，这圆周取逆时针方向.

*3. 求下列向量场 A 的旋度:

(1) $A=(2z-3y)i+(3x-z)j+(y-2x)k;$ 

(2) $A=(z+\sin y)i-(z-x\cos y)j;$ 

(3) $A = x^{2} \sin y i + y^{2} \sin (xz) j + x y \sin (\cos z) k.$ 

*4. 利用斯托克斯公式把曲面积分 $\iint_{\Sigma} \operatorname{rot} A \cdot n \, \mathrm{d}S$ 化为曲线积分, 并计算积分值, 其中 $A, \Sigma$ 及 $n$ 分别如下:

(1) $A=y^{2}i+xyj+xzk,\Sigma$ 为上半球面 $z=\sqrt{1-x^{2}-y^{2}}$ 的上侧,n是 $\Sigma$ 的单位法向量；

(2) $A = (y - z)i + yzj - xzk, \Sigma$ 为立方体 $\{(x,y,z) | 0 \leqslant x \leqslant 2, 0 \leqslant y \leqslant 2, 0 \leqslant z \leqslant 2\}$ 的表面外侧去掉 $xOy$ 面上的那个底面， $n$ 是 $\Sigma$ 的单位法向量.

*5. 求下列向量场 $A$ 沿闭曲线 $\Gamma$ (从 $z$ 轴正向看 $\Gamma$ 依逆时针方向) 的环流量:

(1) $A = -yi + xj + ck$ (c 为常量), $\Gamma$ 为圆周 $x^{2} + y^{2} = 1, z = 0$ ;

(2) $A=(x-z)i+(x^{3}+yz)j-3xy^{2}k$ ，其中 $\Gamma$ 为圆周 $z=2-\sqrt{x^{2}+y^{2}}$ ,z=0.

* 6. 证明 $\operatorname{rot}(a + b) = \operatorname{rot} a + \operatorname{rot} b$ .

*7. 设 $u = u(x, y, z)$ 具有二阶连续偏导数, 求 $\operatorname{rot}(\operatorname{grad} u)$ .

# 总习题十一

1. 填空：

(1) 第二类曲线积分 $\int_{\Gamma} P dx + Q dy + R dz$ 化成第一类曲线积分是 ____，其中 $\alpha, \beta, \gamma$ 为有向曲线弧 $\Gamma$ 在点 $(x, y, z)$ 处的 ____ 的方向角；

(2) 第二类曲面积分 $\iint_{\Sigma} P \mathrm{d} y \mathrm{~d} z + Q \mathrm{~d} z \mathrm{~d} x + R \mathrm{~d} x \mathrm{~d} y$ 化成第一类曲面积分是 ____, 其中 $\alpha, \beta$ 与 $\gamma$ 为有向曲面 $\Sigma$ 在点 $(x, y, z)$ 处的 ____ 的方向角.

2. 下题中给出了四个结论,从中选出一个正确的结论:

设曲面 $\Sigma$ 是上半球面: $x^{2} + y^{2} + z^{2} = R^{2}$ ( $z \geqslant 0$ ), 曲面 $\Sigma_{1}$ 是曲面 $\Sigma$ 在第 I 卦限中的部分, 则有 ( ).

(A) $\iint_{\Sigma} x \, \mathrm{d}S = 4 \iint_{\Sigma_1} x \, \mathrm{d}S$ 

(B) $\iint_{\Sigma} y \, \mathrm{d}S = 4 \iint_{\Sigma_1} x \, \mathrm{d}S$ 

(C) $\iint_{\Sigma} z \, \mathrm{d}S = 4 \iint_{\Sigma_1} x \, \mathrm{d}S$ 

(D) $\iint_{\Sigma} xyz \, \mathrm{d}S = 4 \iint_{\Sigma_1} xyz \, \mathrm{d}S$ 

3. 计算下列曲线积分：

(1) $\oint_{L} \sqrt{x^{2} + y^{2}} \mathrm{~d}s$ , 其中 $L$ 为圆周 $x^{2} + y^{2} = ax$ ;

(2) $\int_{\Gamma} z \mathrm{~ds}$ , 其中 $\Gamma$ 为曲线 $x = t \cos t, y = t \sin t, z = t (0 \leqslant t \leqslant t_0)$ ;

(3) $\int_{L} (2a - y) \mathrm{d}x + x \mathrm{d}y$ ，其中 $L$ 为摆线 $x = a(t - \sin t), y = a(1 - \cos t)$ 上对应 $t$ 从 0 到 $2\pi$ 的一段弧；

(4) $\int_{\Gamma}(y^{2} - z^{2})\mathrm{d}x + 2yz\mathrm{d}y - x^{2}\mathrm{d}z$ ，其中 $\Gamma$ 是曲线 $x = t,y = t^2,z = t^3$ 上由 $t_1 = 0$ 到 $t_2 = 1$ 的一段弧；

(5) $\int_{L} (\mathrm{e}^{x} \sin y - 2y) \, \mathrm{d}x + (\mathrm{e}^{x} \cos y - 2) \, \mathrm{d}y$ ，其中 $L$ 为上半圆周 $(x - a)^{2} + y^{2} = a^{2}, y \geqslant 0$ ，沿逆时针方向；

(6) $\oint_{\Gamma} xyz \, dz$ ，其中 $\Gamma$ 是用平面 $y = z$ 截球面 $x^{2} + y^{2} + z^{2} = 1$ 所得的截痕，从 $z$ 轴的正向看去，沿逆时针方向.

4. 已知函数 $f(x)$ 具有连续导数, $f(0) = 1$ , 且曲线积分

$$
\int_ {L} \left[ e ^ {x} + f (x) \right] y d x - f (x) d y
$$

与路径无关,试确定 $f(x)$ ,并计算 $\int_{(0,0)}^{(1,1)}\left[e^{x}+f(x)\right]ydx-f(x)dy$ 的值.

5. 计算下列曲面积分：

(1) $\iint_{\Sigma} \frac{\mathrm{d}S}{x^2 + y^2 + z^2}$ , 其中 $\Sigma$ 是界于平面 $z = 0$ 及 $z = H$ 之间的圆柱面 $x^2 + y^2 = R^2$ ;

(2) $\iint_{\Sigma} (y^2 - z) \, \mathrm{d}y \, \mathrm{d}z + (z^2 - x) \, \mathrm{d}z \, \mathrm{d}x + (x^2 - y) \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $\Sigma$ 为锥面 $z = \sqrt{x^2 + y^2}$ （ $0 \leqslant z \leqslant h$ ）的外侧；

(3) $\iint_{\Sigma} x \, \mathrm{d}y \, \mathrm{d}z + y \, \mathrm{d}z \, \mathrm{d}x + z \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $\Sigma$ 为半球面 $z = \sqrt{R^2 - x^2 - y^2}$ 的上侧；

(4) $\iint_{\Sigma} xyz \, \mathrm{d}x \, \mathrm{d}y$ ，其中 $\Sigma$ 为球面 $x^2 + y^2 + z^2 = 1 (x \geqslant 0, y \geqslant 0)$ 的外侧；

(5) $\oiint_{\Sigma} f(x) \, \mathrm{d}y \, \mathrm{d}z - [2f(y) + y^2] \, \mathrm{d}z \, \mathrm{d}x + [f(z) + z^3] \, \mathrm{d}x \, \mathrm{d}y$ ，其中函数 $f(x)$ 具有连续导数， $\Sigma$ 是立方体 $\Omega$ ：

$0 \leqslant x \leqslant a, 0 \leqslant y \leqslant a, 0 \leqslant z \leqslant a$ 的表面，并取外侧.

6. 证明: $\frac{x \mathrm{~d} x + y \mathrm{~d} y}{x^2 + y^2}$ 在整个 $x O y$ 面除去 $y$ 的负半轴及原点的区域 $G$ 内是某个二元函数的全微分, 并求出一个这样的二元函数.

7. 设在半平面 $x > 0$ 内有力 $\pmb{F} = -\frac{k}{\rho^3} (xi + yj)$ 构成力场, 其中 $k$ 为常数, $\rho = \sqrt{x^2 + y^2}$ . 证明在此力场中场力所做的功与所取的路径无关.

8. 设函数 $f(x)$ 在 $(- \infty, + \infty)$ 内具有一阶连续导数， $L$ 是上半平面 $(y > 0)$ 内的有向分段光滑曲线，其起点为 $(a, b)$ ，终点为 $(c, d)$ . 记

$$
I = \int_ {L} \frac {1}{y} [ 1 + y ^ {2} f (x y) ] d x + \frac {x}{y ^ {2}} [ y ^ {2} f (x y) - 1 ] d y,
$$

(1) 证明曲线积分 I 与路径无关;

(2) 当 ab=cd 时, 求 I 的值.

9. 求均匀曲面 $z = \sqrt{a^{2} - x^{2} - y^{2}}$ 的质心的坐标.

10. 设 $u(x,y)$ 与 $v(x,y)$ 在闭区域 D 上都具有二阶连续偏导数, 分段光滑的曲线 L 为 D 的正向边界曲线. 证明:

(1) $\iint_{D} v \Delta u \, \mathrm{d}x \, \mathrm{d}y = -\iint_{D} (\text{grad } u \cdot \text{grad } v) \, \mathrm{d}x \, \mathrm{d}y + \oint_{L} v \frac{\partial u}{\partial n} \, \mathrm{d}s$ ; 

(2) $\iint_{D} (u \Delta v - v \Delta u) \, \mathrm{d}x \, \mathrm{d}y = \oint_{L} \left(u \frac{\partial v}{\partial n} - v \frac{\partial u}{\partial n}\right) \, \mathrm{d}s,$ 

其中 $\frac{\partial u}{\partial n}$ 与 $\frac{\partial v}{\partial n}$ 分别是u与v沿L的外法向量n的方向导数,符号 $\Delta=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}$ 称为二维拉普拉斯算子.

* 11. 求向量 $A = x i + y j + z k$ 通过闭区域 $\Omega = \{(x, y, z) | 0 \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1, 0 \leqslant z \leqslant 1\}$ 的边界曲面流向外侧的通量.

12. 求力 $F = y i + z j + x k$ 沿有向闭曲线 $\Gamma$ 所做的功, 其中 $\Gamma$ 为平面 $x + y + z = 1$ 被三个坐标面所截成的三角形的整个边界, 从 $z$ 轴正向看去, 沿顺时针方向.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/711f6d303b59411dfc0eb9048a2ef9ee8fa0214226213b89de36f615b78f87bd.jpg)



第十一章释疑解难


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/95aa4e3c096a65d3f72e3ef2a12cd7ad7c3b7b22a3e431b454deda11ae6377bf.jpg)



第十一章例题精讲


# 第十二章

# 无穷级数

无穷级数是高等数学的一个重要组成部分,它是表示函数、研究函数的性质以及进行数值计算的一种工具.本章先讨论常数项级数,介绍无穷级数的一些基本内容,然后讨论函数项级数,着重讨论如何将函数展开成幂级数和三角级数的问题.

# 第一节 常数项级数的概念和性质

# 一、常数项级数的概念

人们认识事物在数量方面的特性,往往有一个由近似到精确的过程.在这种认识过程中,会遇到由有限个数量相加到无穷多个数量相加的问题.

例如计算半径为 R 的圆面积 A, 具体做法如下: 作圆的内接正六边形, 算出这六边

形的面积 $a_1$ ，它是圆面积 $A$ 的一个粗糙的近似值。为了比较准确地计算出 $A$ 的值，我们以这个正六边形的每一边为底分别作一个顶点在圆周上的等腰三角形（图12-1），算出这六个等腰三角形的面积之和 $a_2$ 。那么 $a_1 + a_2$ （即内接正十二边形的面积）就是 $A$ 的一个较好的近似值。同样地，在这正十二边形的每一边上分别作一个顶点在圆周上的等腰三角形，算出这十二个等腰三角形的面积之和 $a_3$ 。那么 $a_1 + a_2 + a_3$ （即内接正二

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/1ff9943472927e95b518a870c7f705b6e9e2205008fae48bb46a00a7bd4250d0.jpg)



图12-1


十四边形的面积)是 A 的一个更好的近似值. 如此继续下去, 内接正 $3 \times 2^{n}$ 边形的面积就逐步逼近圆面积:

$$
A \approx a _ {1}, A \approx a _ {1} + a _ {2}, A \approx a _ {1} + a _ {2} + a _ {3}, \dots , A \approx a _ {1} + a _ {2} + \dots + a _ {n}.
$$

如果内接正多边形的边数无限增多,即 n 无限增大,那么和 $a_{1}+a_{2}+\cdots+a_{n}$ 的极限就是所要求的圆面积 A.这时和式中的项数无限增多,于是出现了无穷多个数量依次相加

的数学式子.

一般地,如果给定一个数列

$$
u _ {1}, u _ {2}, u _ {3}, \dots , u _ {n}, \dots ,
$$

那么由这数列构成的表达式

$$
u _ {1} + u _ {2} + u _ {3} + \dots + u _ {n} + \dots \tag {1-1}
$$

叫做(常数项)无穷级数,简称(常数项)级数,记为 $\sum_{i=1}^{\infty}u_{i}$ ,即

$$
\sum_ {i = 1} ^ {\infty} u _ {i} = u _ {1} + u _ {2} + u _ {3} + \dots + u _ {i} + \dots ,
$$

其中第 n 项 $u_{n}$ 叫做级数的一般项.

上述级数的定义只是一个形式上的定义,怎样理解无穷级数中无穷多个数量相加呢?联系上面关于计算圆面积的例子,我们可以从有限项的和出发,观察它们的变化趋势,由此来理解无穷多个数量相加的含义.

作(常数项)级数(1-1)的前 $n$ 项的和

$$
s _ {n} = u _ {1} + u _ {2} + \dots + u _ {n} = \sum_ {i = 1} ^ {n} u _ {i}, \tag {1-2}
$$

$s_{n}$ 称为级数(1-1)的部分和. 当 n 依次取 1,2,3,…时, 它们构成一个新的数列

$$
s _ {1} = u _ {1}, s _ {2} = u _ {1} + u _ {2}, s _ {3} = u _ {1} + u _ {2} + u _ {3}, \dots , s _ {n} = u _ {1} + u _ {2} + \dots + u _ {n}, \dots .
$$

根据这个数列有没有极限,我们引进无穷级数(1-1)的收敛与发散的概念.

定义 如果级数 $\sum_{i=1}^{\infty} u_i$ 的部分和数列 $\{s_n\}$ 有极限 $s$ , 即

$$
\lim _ {n \rightarrow \infty} s _ {n} = s,
$$

那么称无穷级数 $\sum_{i=1}^{\infty} u_i$ 收敛, 这时极限 $s$ 叫做这级数的和, 并写成

$$
s = u _ {1} + u _ {2} + \dots + u _ {i} + \dots ;
$$

如果 $\{s_n\}$ 没有极限, 那么称无穷级数 $\sum_{i=1}^{\infty} u_i$ 发散.

显然,当级数收敛时,其部分和 $s_n$ 是级数的和 $s$ 的近似值,它们之间的差值

$$
r _ {n} = s - s _ {n} = u _ {n + 1} + u _ {n + 2} + \dots
$$

叫做级数的余项. 用近似值 $s_n$ 代替和 $s$ 所产生的误差是这个余项的绝对值, 即误差是 $\left|r_n\right|$ .

从上述定义可知,级数与数列极限有着紧密的联系.给定级数 $\sum_{i=1}^{\infty}u_{i}$ , 就有部分和数列 $\{s_{n}\}$ ; 反之, 给定数列 $\{s_{n}\}$ , 就有以 $\{s_{n}\}$ 为部分和数列的级数

$$
s _ {1} + \left(s _ {2} - s _ {1}\right) + \dots + \left(s _ {i} - s _ {i - 1}\right) + \dots = s _ {1} + \sum_ {i = 2} ^ {\infty} \left(s _ {i} - s _ {i - 1}\right) = \sum_ {i = 1} ^ {\infty} u _ {i},
$$

其中 $u_{1} = s_{1}, u_{n} = s_{n} - s_{n - 1}(n \geqslant 2)$ . 按定义, 级数 $\sum_{i=1}^{\infty} u_{i}$ 与数列 $\{s_{n}\}$ 同时收敛或同时发散, 且在收敛时, 有

$$
\sum_ {i = 1} ^ {\infty} u _ {i} = \lim _ {n \rightarrow \infty} s _ {n},
$$

即

$$
\sum_ {i = 1} ^ {\infty} u _ {i} = \lim _ {n \rightarrow \infty} \sum_ {i = 1} ^ {n} u _ {i}.
$$

例1 无穷级数

$$
\sum_ {i = 0} ^ {\infty} a q ^ {i} = a + a q + a q ^ {2} + \dots + a q ^ {i} + \dots \tag {1-3}
$$

叫做等比级数(又称为几何级数),其中 $a \neq 0, q$ 叫做级数的公比.试讨论级数(1-3)的收敛性.

解 如果 $q \neq 1$ ，那么部分和

$$
s _ {n} = a + a q + \dots + a q ^ {n - 1} = \frac {a - a q ^ {n}}{1 - q} = \frac {a}{1 - q} - \frac {a q ^ {n}}{1 - q}.
$$

当 $|q| < 1$ 时，由于 $\lim_{n\to \infty}q^n = 0$ ，从而 $\lim_{n\to \infty}s_n = \frac{a}{1 - q}$ 因此这时级数(1-3)收敛，其和为 $\frac{a}{1 - q}$ .当 $|q| > 1$ 时，由于 $\lim_{n\to \infty}q^n = \infty$ ，从而 $\lim_{n\to \infty}s_n = \infty$ ，这时级数(1-3)发散.

如果 $|q| = 1$ ，那么当 $q = 1$ 时， $s_n = na \to \infty$ ，因此级数(1-3)发散；当 $q = -1$ 时，级数(1-3)成为

$$
a - a + a - a + \dots ,
$$

显然 $s_n$ 随着 $n$ 为奇数或为偶数而等于 $a$ 或等于0，从而 $s_n$ 的极限不存在，这时级数(1-3)也发散.

综合上述结果,我们得到:如果等比级数(1-3)的公比的绝对值 $|q|<1$ ,那么级数收敛;如果 $|q|\geqslant1$ ,那么级数发散.

例 2 证明级数 $1+2+3+\cdots+n+\cdots$ 是发散的.

证 这级数的部分和为

$$
s _ {n} = 1 + 2 + 3 + \dots + n = \frac {n (n + 1)}{2}.
$$

显然， $\lim_{n\to \infty}s_n = \infty$ ，因此所给级数是发散的

例 3 判定无穷级数 $\frac{1}{1\times2}+\frac{1}{2\times3}+\cdots+\frac{1}{n(n+1)}+\cdots$ 

的收敛性.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/979502dd61dadfb07b695fb1b46901fc724448909f2b59bb311583a7f4738cfb.jpg)


例题精讲

12-1 

解 由于

$$
u _ {n} = \frac {1}{n (n + 1)} = \frac {1}{n} - \frac {1}{n + 1},
$$

因此

$$
s _ {n} = \frac {1}{1 \times 2} + \frac {1}{2 \times 3} + \dots + \frac {1}{n (n + 1)} = \left(1 - \frac {1}{2}\right) + \left(\frac {1}{2} - \frac {1}{3}\right) + \dots + \left(\frac {1}{n} - \frac {1}{n + 1}\right) = 1 - \frac {1}{n + 1}.
$$

从而

$$
\lim _ {n \rightarrow \infty} s _ {n} = \lim _ {n \rightarrow \infty} \left(1 - \frac {1}{n + 1}\right) = 1,
$$

所以这级数收敛,它的和是1.

# 二、收敛级数的基本性质

根据无穷级数收敛、发散以及和的概念,可以得出收敛级数的几个基本性质.

性质1 如果级数 $\sum_{n=1}^{\infty} u_n$ 收敛于和 $s$ , 那么级数 $\sum_{n=1}^{\infty} ku_n$ 也收敛, 且其和为 $ks$ .

证 设级数 $\sum_{n=1}^{\infty} u_n$ 与级数 $\sum_{n=1}^{\infty} k u_n$ 的部分和分别为 $s_n$ 与 $\sigma_n$ , 则

$$
\sigma_ {n} = k u _ {1} + k u _ {2} + \dots + k u _ {n} = k s _ {n},
$$

于是

$$
\lim _ {n \rightarrow \infty} \sigma_ {n} = \lim _ {n \rightarrow \infty} k s _ {n} = k \lim _ {n \rightarrow \infty} s _ {n} = k s.
$$

这就表明级数 $\sum_{n=1}^{\infty}ku_{n}$ 收敛,且和为 ks.

由关系式 $\sigma_{n} = ks_{n}$ 知道，如果 $\{s_n\}$ 没有极限且 $k \neq 0$ ，那么 $\{\sigma_{n}\}$ 也不可能有极限.因此我们得到如下结论：级数的每一项同乘一个不为零的常数后，它的收敛性不会改变.

性质2 如果级数 $\sum_{n=1}^{\infty} u_n$ 与 $\sum_{n=1}^{\infty} v_n$ 分别收敛于和 $s$ 与 $\sigma$ , 那么级数 $\sum_{n=1}^{\infty} (u_n \pm v_n)$ 也收敛, 且其和为 $s \pm \sigma$ .

证 设级数 $\sum_{n=1}^{\infty} u_n$ 与 $\sum_{n=1}^{\infty} v_n$ 的部分和分别为 $s_n$ 与 $\sigma_n$ , 则级数 $\sum_{n=1}^{\infty} (u_n \pm v_n)$ 的部分和

$$
\tau_ {n} = \left(u _ {1} \pm v _ {1}\right) + \left(u _ {2} \pm v _ {2}\right) + \dots + \left(u _ {n} \pm v _ {n}\right) = \left(u _ {1} + u _ {2} + \dots + u _ {n}\right) \pm \left(v _ {1} + v _ {2} + \dots + v _ {n}\right) = s _ {n} \pm \sigma_ {n},
$$

于是

$$
\lim _ {n \rightarrow \infty} \tau_ {n} = \lim _ {n \rightarrow \infty} (s _ {n} \pm \sigma_ {n}) = s \pm \sigma .
$$

这就表明级数 $\sum_{n=1}^{\infty}\left(u_n\pm v_n\right)$ 收敛，且其和为 $s\pm \sigma$ 

性质 2 也说成:两个收敛级数可以逐项相加与逐项相减.

性质 3 在级数中去掉、加上或改变有限项,不会改变级数的收敛性.

证 我们只需证明“在级数的前面部分去掉或加上有限项,不会改变级数的收敛性”,因为其他情形(即在级数中任意去掉、加上或改变有限项的情形)都可以看成在级数的前面部分先去掉有限项,然后再加上有限项的结果.

设将级数

$$
u _ {1} + u _ {2} + \dots + u _ {k} + u _ {k + 1} + \dots + u _ {k + n} + \dots
$$

的前 k 项去掉,则得级数

$$
u _ {k + 1} + u _ {k + 2} + \dots + u _ {k + n} + \dots ,
$$

于是新得的级数的部分和为

$$
\sigma_ {n} = u _ {k + 1} + u _ {k + 2} + \dots + u _ {k + n} = s _ {k + n} - s _ {k},
$$

其中 $s_{k+n}$ 是原来级数的前 $k+n$ 项的和. 因为 $s_{k}$ 是常数, 所以当 $n\to\infty$ 时, $\sigma_{n}$ 与 $s_{k+n}$ 或者同时具有极限, 或者同时没有极限.

类似地,可以证明在级数的前面加上有限项,不会改变级数的收敛性.

性质 4 如果级数 $\sum_{n=1}^{\infty} u_{n}$ 收敛, 那么对这级数的项任意加括号后所成的级数

$$
\left(u _ {1} + u _ {2} + \dots + u _ {n _ {1}}\right) + \left(u _ {n _ {1} + 1} + u _ {n _ {1} + 2} + \dots + u _ {n _ {2}}\right) + \dots + \left(u _ {n _ {k - 1} + 1} + u _ {n _ {k - 1} + 2} + \dots + u _ {n _ {k}}\right) + \dots \tag {1-4}
$$

仍收敛,且其和不变.

证 设级数 $\sum_{n=1}^{\infty} u_n$ 的部分和数列为 $\{s_n\}$ , 加括号后所成的级数 (1-4) 的部分和数列为 $\{A_k\}$ , 则

$$
A _ {1} = u _ {1} + u _ {2} + \dots + u _ {n _ {1}} = s _ {n _ {1}},
$$

$$
A _ {2} = \left(u _ {1} + u _ {2} + \dots + u _ {n _ {1}}\right) + \left(u _ {n _ {1} + 1} + u _ {n _ {1} + 2} + \dots + u _ {n _ {2}}\right) = s _ {n _ {2}},
$$

$$
\dots
$$

$$
A _ {k} = \left(u _ {1} + u _ {2} \dots + u _ {n _ {1}}\right) + \left(u _ {n _ {1} + 1} + u _ {n _ {1} + 2} + \dots + u _ {n _ {2}}\right) + \dots + \left(u _ {n _ {k - 1} + 1} + u _ {n _ {k - 1} + 2} + \dots + u _ {n _ {k}}\right) = s _ {n _ {k}},
$$

$$
\dots
$$

可见, 数列 $\{A_{k}\}$ 是数列 $\{s_{n}\}$ 的一个子数列. 由数列 $\{s_{n}\}$ 的收敛性以及收敛数列与其子数列的关系可知, 数列 $\{A_{k}\}$ 必定收敛, 且有

$$
\lim _ {k \rightarrow \infty} A _ {k} = \lim _ {n \rightarrow \infty} s _ {n},
$$

即加括号后所成的级数收敛,且其和不变.

注意 如果加括号后所成的级数收敛,那么不能断定去括号后原来的级数也收敛.例如,级数

$$
(1 - 1) + (1 - 1) + \dots
$$

收敛于零,但级数

$$
1 - 1 + 1 - 1 + \dots
$$

却是发散的.

根据性质 4 可得如下推论: 如果加括号后所成的级数发散, 那么原来级数也发散. 事实上, 倘若原来级数收敛, 则根据性质 4 知道, 加括号后的级数就应该收敛了.

性质5(级数收敛的必要条件) 如果级数 $\sum_{n=1}^{\infty} u_n$ 收敛, 那么它的一般项 $u_n$ 趋于零, 即

$$
\lim _ {n \rightarrow \infty} u _ {n} = 0.
$$

证 设级数 $\sum_{n=1}^{\infty} u_n$ 的部分和为 $s_n$ , 且 $s_n \to s$ ( $n \to \infty$ ), 则

$$
\lim _ {n \rightarrow \infty} u _ {n} = \lim _ {n \rightarrow \infty} (s _ {n} - s _ {n - 1}) = \lim _ {n \rightarrow \infty} s _ {n} - \lim _ {n \rightarrow \infty} s _ {n - 1} = s - s = 0.
$$

由性质 5 可知,如果级数的一般项不趋于零,那么该级数必定发散.例如,级数

$$
\frac {1}{2} - \frac {2}{3} + \frac {3}{4} - \dots + (- 1) ^ {n - 1} \frac {n}{n + 1} + \dots ,
$$

它的一般项 $u_{n} = (-1)^{n - 1}\frac{n}{n + 1}$ 当 $n\to \infty$ 时不趋于零，因此该级数是发散的

注意 级数的一般项趋于零并不是级数收敛的充分条件.有些级数虽然一般项趋于零,但仍然是发散的.例如,调和级数

$$
1 + \frac {1}{2} + \frac {1}{3} + \dots + \frac {1}{n} + \dots , \tag {1-5}
$$

虽然它的一般项 $u_{n} = \frac{1}{n}\rightarrow 0 (n\to \infty)$ ，但是它是发散的.现在我们用反证法证明如下：

假若级数(1-5)收敛,设它的部分和为 $s_{n}$ , 且 $s_{n} \rightarrow s (n \rightarrow \infty)$ . 显然,对级数(1-5)的部分和 $s_{2n}$ ,也有 $s_{2n} \rightarrow s (n \rightarrow \infty)$ . 于是

$$
s _ {2 n} - s _ {n} \longrightarrow s - s = 0 \quad (n \longrightarrow \infty).
$$

但另一方面

$$
s _ {2 n} - s _ {n} = \frac {1}{n + 1} + \frac {1}{n + 2} + \dots + \frac {1}{2 n} > \underbrace {\frac {1}{2 n} + \frac {1}{2 n} + \cdots + \frac {1}{2 n}} _ {n \text {项}} = \frac {1}{2},
$$

故

$$
s _ {2 n} - s _ {n} \not \to 0 (n \rightarrow \infty),
$$

与假设级数(1-5)收敛矛盾.这矛盾说明级数(1-5)必定发散.

# *三、柯西审敛原理

怎样判定一个级数的收敛性呢？我们有下述的柯西审敛原理。

定理(柯西审敛原理) 级数 $\sum_{n=1}^{\infty}u_{n}$ 收敛的充分必要条件为:对于任意给定的正数 $\varepsilon$ , 总存在正整数 N, 使得当 n>N 时, 对于任意的正整数 p, 都有

$$
\left| u _ {n + 1} + u _ {n + 2} + \dots + u _ {n + p} \right| <   \varepsilon
$$

成立.

证 设级数 $\sum_{n=1}^{\infty} u_n$ 的部分和为 $s_n$ , 因为

$$
\left| u _ {n + 1} + u _ {n + 2} + \dots + u _ {n + p} \right| = \left| s _ {n + p} - s _ {n} \right|,
$$

所以由数列的柯西极限存在准则(第一章第六节),即得本定理结论.

例4 利用柯西审敛原理判定级数 $\sum_{n=1}^{\infty} \frac{1}{n^2}$ 的收敛性.

解 因为对任何正整数 p，

$$
\begin{array}{l} \left| u _ {n + 1} + u _ {n + 2} + \dots + u _ {n + p} \right| = \frac {1}{(n + 1) ^ {2}} + \frac {1}{(n + 2) ^ {2}} + \dots + \frac {1}{(n + p) ^ {2}} \\ <   \frac {1}{n (n + 1)} + \frac {1}{(n + 1) (n + 2)} + \dots + \frac {1}{(n + p - 1) (n + p)} \\ = \left(\frac {1}{n} - \frac {1}{n + 1}\right) + \left(\frac {1}{n + 1} - \frac {1}{n + 2}\right) + \dots + \left(\frac {1}{n + p - 1} - \frac {1}{n + p}\right) \\ = \frac {1}{n} - \frac {1}{n + p} <   \frac {1}{n}, \\ \end{array}
$$

所以对于任意给定的正数 $\varepsilon$ ，取正整数 $N\geqslant \frac{1}{\varepsilon}$ 则当 $n > N$ 时，对任何正整数 $p$ ，都有

$$
\left| u _ {n + 1} + u _ {n + 2} + \dots + u _ {n + p} \right| <   \varepsilon
$$

成立.按柯西审敛原理,级数 $\sum_{n=1}^{\infty}\frac{1}{n^{2}}$ 收敛.

# 习题12-1

1. 写出下列级数的前五项：

(1) $\sum_{n=1}^{\infty} \frac{1+n}{1+n^2}$ ; 

(2) $\sum_{n=1}^{\infty} \frac{1 \times 3 \times \cdots \times (2n-1)}{2 \times 4 \times \cdots \times (2n)}$ ; 

(3) $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{5^n}$ ; 

(4) $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ . 

2. 根据级数收敛与发散的定义判定下列级数的收敛性：

(1) $\sum_{n=1}^{\infty} (\sqrt{n+1} - \sqrt{n})$ ; 

(2) $\frac{1}{1\times3}+\frac{1}{3\times5}+\frac{1}{5\times7}+\cdots+\frac{1}{(2n-1)(2n+1)}+\cdots;$ 

(3) $\sin \frac{\pi}{6} + \sin \frac{2\pi}{6} + \cdots + \sin \frac{n\pi}{6} + \cdots;$ 

(4) $\sum_{n=1}^{\infty} \ln \left(1 + \frac{1}{n}\right)$ . 

3. 设级数 $\sum_{n=1}^{\infty} u_n$ 满足条件: (1) $\lim_{n \to \infty} u_n = 0$ ; (2) $\sum_{k=1}^{\infty} (u_{2k-1} + u_{2k})$ 收敛. 证明: 级数 $\sum_{n=1}^{\infty} u_n$ 收敛.

4. 判定下列级数的收敛性：

(1) $-\frac{8}{9}+\frac{8^{2}}{9^{2}}-\frac{8^{3}}{9^{3}}+\cdots+(-1)^{n}\frac{8^{n}}{9^{n}}+\cdots;$ 

(2) $\frac{1}{3}+\frac{1}{6}+\frac{1}{9}+\cdots+\frac{1}{3n}+\cdots;$ 

(3) $\frac{1}{3}+\frac{1}{\sqrt{3}}+\frac{1}{\sqrt[3]{3}}+\cdots+\frac{1}{\sqrt[n]{3}}+\cdots;$ 

(4) $\frac{3}{2}+\frac{3^{2}}{2^{2}}+\frac{3^{3}}{2^{3}}+\cdots+\frac{3^{n}}{2^{n}}+\cdots;$ 

(5) $\left(\frac{1}{2}+\frac{1}{3}\right)+\left(\frac{1}{2^{2}}+\frac{1}{3^{2}}\right)+\left(\frac{1}{2^{3}}+\frac{1}{3^{3}}\right)+\cdots+\left(\frac{1}{2^{n}}+\frac{1}{3^{n}}\right)+\cdots.$ 

* 5. 利用柯西审敛原理判定下列级数的收敛性：

(1) $\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$ ; 

(2) $1+\frac{1}{2}-\frac{1}{3}+\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\cdots+\frac{1}{3n-2}+\frac{1}{3n-1}-\frac{1}{3n}+\cdots;$ 

(3) $\sum_{n=1}^{\infty} \frac{\sin nx}{2^n}$ ; 

(4) $\sum_{n=0}^{\infty}\left(\frac{1}{3n+1}+\frac{1}{3n+2}-\frac{1}{3n+3}\right)$ . 

# 第二节 常数项级数的审敛法

# 一、正项级数及其审敛法

一般的常数项级数,它的各项可以是正数、负数或零.现在我们先讨论各项都是正数或零的级数,这种级数称为正项级数.这种级数特别重要,以后将看到许多级数的收敛性问题可归结为正项级数的收敛性问题.

设级数

$$
u _ {1} + u _ {2} + \dots + u _ {n} + \dots \tag {2-1}
$$

是一个正项级数 $(u_{n}\geqslant 0)$ ，它的部分和为 $s_n$ .显然，数列 $\{s_n\}$ 是一个单调增加数列

$$
s _ {1} \leqslant s _ {2} \leqslant \dots \leqslant s _ {n} \leqslant \dots .
$$

如果数列 $\{s_n\}$ 有界，即 $s_n$ 总不大于某一常数 $M$ ，根据单调有界的数列必有极限的准则，级数(2-1)必收敛于和 $s$ ，且 $s_n \leqslant s \leqslant M$ 。反之，如果正项级数(2-1)收敛于和 $s$ ，即 $\lim_{n \to \infty} s_n = s$ ，根据有极限的数列是有界数列的性质可知，数列 $\{s_n\}$ 有界。因此，我们得到如下重要的结论：

定理1 正项级数 $\sum_{n=1}^{\infty} u_n$ 收敛的充分必要条件是: 它的部分和数列 $\{s_n\}$ 有界.

由定理1可知,如果正项级数 $\sum_{n=1}^{\infty}u_{n}$ 发散,那么它的部分和数列 $s_{n}\rightarrow+\infty(n\rightarrow\infty)$ , 即 $\sum_{n=1}^{\infty}u_{n}=+\infty$ .

根据定理 1, 可得关于正项级数的一个基本的审敛法.

定理 2(比较审敛法) 设 $\sum_{n=1}^{\infty}u_{n}$ 和 $\sum_{n=1}^{\infty}v_{n}$ 都是正项级数, 且 $u_{n}\leqslant v_{n}\quad(n=1,2,\cdots)$ . 若级数 $\sum_{n=1}^{\infty}v_{n}$ 收敛, 则级数 $\sum_{n=1}^{\infty}u_{n}$ 收敛; 反之, 若级数 $\sum_{n=1}^{\infty}u_{n}$ 发散, 则级数 $\sum_{n=1}^{\infty}v_{n}$ 发散.

证 设级数 $\sum_{n=1}^{\infty} v_n$ 收敛于和 $\sigma$ , 则级数 $\sum_{n=1}^{\infty} u_n$ 的部分和

$$
s _ {n} = u _ {1} + u _ {2} + \dots + u _ {n} \leqslant v _ {1} + v _ {2} + \dots + v _ {n} \leqslant \sigma \quad (n = 1, 2, \dots),
$$

即部分和数列 $\{s_n\}$ 有界，由定理1知级数 $\sum_{n=1}^{\infty} u_n$ 收敛.

反之, 设级数 $\sum_{n=1}^{\infty} u_n$ 发散, 则级数 $\sum_{n=1}^{\infty} v_n$ 必发散. 因为若级数 $\sum_{n=1}^{\infty} v_n$ 收敛, 由上面已证明的结论, 将有级数 $\sum_{n=1}^{\infty} u_n$ 也收敛, 与假设矛盾.

注意到级数的每一项同乘不为零的常数 $k$ 以及去掉级数前面部分的有限项不会影响级数的收敛性, 我们可得如下推论:

推论 设 $\sum_{n=1}^{\infty} u_n$ 和 $\sum_{n=1}^{\infty} v_n$ 都是正项级数, 如果级数 $\sum_{n=1}^{\infty} v_n$ 收敛, 且存在正整数 $N$ , 使当 $n \geqslant N$ 时有 $u_n \leqslant kv_n (k > 0)$ 成立, 那么级数 $\sum_{n=1}^{\infty} u_n$ 收敛; 如果级数 $\sum_{n=1}^{\infty} v_n$ 发散, 且当 $n \geqslant N$ 时有 $u_n \geqslant kv_n (k > 0)$ 成立, 那么级数 $\sum_{n=1}^{\infty} u_n$ 发散.

例1 讨论 $p$ 级数

$$
1 + \frac {1}{2 ^ {p}} + \frac {1}{3 ^ {p}} + \frac {1}{4 ^ {p}} + \dots + \frac {1}{n ^ {p}} + \dots \tag {2-2}
$$

的收敛性,其中常数p>0.

解 设 $p \leqslant 1$ . 这时级数的各项不小于调和级数的对应项, 即 $\frac{1}{n^p} \geqslant \frac{1}{n}$ , 但调和级数发散, 因此根据比较审敛法可知, 当 $p \leqslant 1$ 时级数(2-2)发散.

设 $p > 1$ .因为当 $k - 1\leqslant x\leqslant k$ 时，有 $\frac{1}{k^p}\leqslant \frac{1}{x^p}$ ，所以

$$
\frac {1}{k ^ {p}} = \int_ {k - 1} ^ {k} \frac {1}{k ^ {p}} \mathrm{d} x \leqslant \int_ {k - 1} ^ {k} \frac {1}{x ^ {p}} \mathrm{d} x (k = 2, 3, \dots),
$$

从而级数(2-2)的部分和

$$
\begin{array}{l} s _ {n} = 1 + \sum_ {k = 2} ^ {n} \frac {1}{k ^ {p}} \leqslant 1 + \sum_ {k = 2} ^ {n} \int_ {k - 1} ^ {k} \frac {1}{x ^ {p}} d x = 1 + \int_ {1} ^ {n} \frac {1}{x ^ {p}} d x \\ = 1 + \frac {1}{p - 1} \left(1 - \frac {1}{n ^ {p - 1}}\right) <   1 + \frac {1}{p - 1} (n = 2, 3, \dots), \\ \end{array}
$$

这表明数列 $\{s_n\}$ 有界，因此级数(2-2)收敛.

综合上述结果,我们得到:p 级数(2-2)当 p>1 时收敛,当 $p \leqslant 1$ 时发散.

例2 证明级数 $\sum_{n=1}^{\infty} \frac{1}{\sqrt{n(n+1)}}$ 是发散的.

证 因为 $n(n + 1) < (n + 1)^2$ ，所以 $\frac{1}{\sqrt{n(n + 1)}} > \frac{1}{n + 1}$ . 而级数

$$
\sum_ {n = 1} ^ {\infty} \frac {1}{n + 1} = \frac {1}{2} + \frac {1}{3} + \dots + \frac {1}{n + 1} + \dots
$$

是发散的.根据比较审敛法可知所给级数也是发散的.

为应用上的方便,下面我们给出比较审敛法的极限形式.

定理3（比较审敛法的极限形式）设 $\sum_{n = 1}^{\infty}u_n$ 和 $\sum_{n = 1}^{\infty}v_{n}$ 都是正项级数，

（1）如果 $\lim_{n\to \infty}\frac{u_n}{v_n} = l$ （ $0\leqslant l <   + \infty$ ），且级数 $\sum_{n = 1}^{\infty}v_n$ 收敛，那么级数 $\sum_{n = 1}^{\infty}u_n$ 收敛；

(2) 如果 $\lim_{n\to\infty}\frac{u_{n}}{v_{n}}=l>0$ 或 $\lim_{n\to\infty}\frac{u_{n}}{v_{n}}=+\infty$ , 且级数 $\sum_{n=1}^{\infty}v_{n}$ 发散, 那么级数 $\sum_{n=1}^{\infty}u_{n}$ 发散.

证（1）由极限定义可知，对 $\varepsilon = 1$ ，存在正整数 $N$ ，当 $n > N$ 时，有

$$
\frac {u _ {n}}{v _ {n}} <   l + 1,
$$

即 $u_{n} < (l + 1)v_{n}$ . 而级数 $\sum_{n=1}^{\infty} v_{n}$ 收敛, 根据比较审敛法的推论, 知级数 $\sum_{n=1}^{\infty} u_{n}$ 收敛.

（2）按已知条件知极限 $\lim_{n\to \infty}\frac{v_n}{u_n}$ 存在，如果级数 $\sum_{n = 1}^{\infty}u_n$ 收敛，那么由结论(1)必有级数 $\sum_{n = 1}^{\infty}v_n$ 收敛，但已知级数 $\sum_{n = 1}^{\infty}v_n$ 发散，因此级数 $\sum_{n = 1}^{\infty}u_n$ 不可能收敛，即级数 $\sum_{n = 1}^{\infty}u_n$ 发散.对于 $\lim_{n\to \infty}\frac{u_n}{v_n} = +\infty$ 的情形，留给读者证明.

极限形式的比较审敛法,在两个正项级数的一般项均趋于零的情况下,其实是比较它们的一般项作为无穷小量的阶. 定理表明, 当 $n \to \infty$ 时, 如果 $u_{n}$ 是与 $v_{n}$ 同阶或是比 $v_{n}$ 高阶的无穷小, 而级数 $\sum_{n=1}^{\infty} v_{n}$ 收敛, 那么级数 $\sum_{n=1}^{\infty} u_{n}$ 收敛; 如果 $u_{n}$ 是与 $v_{n}$ 同阶或是比 $v_{n}$ 低阶的无穷小, 而级数 $\sum_{n=1}^{\infty} v_{n}$ 发散, 那么级数 $\sum_{n=1}^{\infty} u_{n}$ 发散.

例3 判定级数 $\sum_{n=1}^{\infty} \sin \frac{1}{n}$ 的收敛性.

解 因为

$$
\lim _ {n \rightarrow \infty} \frac {\sin \frac {1}{n}}{\frac {1}{n}} = 1 > 0,
$$

而级数 $\sum_{n=1}^{\infty} \frac{1}{n}$ 发散, 根据定理 3 知此级数发散.

用比较审敛法审敛时,需要适当地选取一个已知其收敛性的级数 $\sum_{n=1}^{\infty}v_{n}$ 作为比较的基准.最常选作基准级数的是等比级数和 p 级数.

将所给正项级数与等比级数比较,我们能得到在实用上很方便的比值审敛法和根值审敛法.

定理 4(比值审敛法, 达朗贝尔(d'Alembert)判别法) 设 $\sum_{n=1}^{\infty}u_{n}$ 为正项级数, 如果

$$
\lim _ {n \rightarrow \infty} \frac {u _ {n + 1}}{u _ {n}} = \rho ,
$$

那么当 $\rho < 1$ 时级数收敛, $\rho > 1$ (或 $\lim_{n \to \infty} \frac{u_{n+1}}{u_n} = \infty$ ) 时级数发散, $\rho = 1$ 时级数可能收敛也可能发散.

证（1）当 $\rho < 1$ 时.取一个适当小的正数 $\varepsilon$ ，使得 $\rho +\varepsilon = r < 1$ ，根据极限定义，存在正整数 $m$ ，当 $n\geqslant m$ 时有不等式

$$
\frac {u _ {n + 1}}{u _ {n}} <   \rho + \varepsilon = r.
$$

因此

$$
u _ {m + 1} <   r u _ {m}, u _ {m + 2} <   r u _ {m + 1} <   r ^ {2} u _ {m}, \dots , u _ {m + k} <   r ^ {k} u _ {m}, \dots .
$$

而级数 $\sum_{k=1}^{\infty} r^{k} u_{m}$ 收敛(公比 $r<1$ ), 根据定理 2 的推论, 知级数 $\sum_{n=1}^{\infty} u_{n}$ 收敛.

(2) 当 $\rho > 1$ 时. 取一个适当小的正数 $\varepsilon$ , 使得 $\rho - \varepsilon > 1$ . 根据极限定义, 当 $n \geqslant m$ 时有

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/9809d02452e325b1e7b50445c829f5ea28f8a3593f6a91cc04787f3eea02d98c.jpg)


例题精讲

12-2 

不等式

$$
\frac {u _ {n + 1}}{u _ {n}} > \rho - \varepsilon > 1,
$$

也就是

$$
u _ {n + 1} > u _ {n}.
$$

所以当 $n \geqslant m$ 时, 级数的一般项 $u_{n}$ 是逐渐增大的, 从而 $\lim_{n \to \infty} u_{n} \neq 0$ . 根据级数收敛的必要条件可知级数 $\sum_{n=1}^{\infty} u_{n}$ 发散.

类似地,可以证明当 $\lim_{n\to\infty}\frac{u_{n+1}}{u_n}=\infty$ 时,级数 $\sum_{n=1}^{\infty}u_n$ 发散.

(3) 当 $\rho=1$ 时. 级数可能收敛也可能发散. 例如 p 级数 (2-2), 不论 p 为何值都有

$$
\lim _ {n \to \infty} \frac {u _ {n + 1}}{u _ {n}} = \lim _ {n \to \infty} \frac {\frac {1}{(n + 1) ^ {p}}}{\frac {1}{n ^ {p}}} = 1.
$$

但我们知道, 当 p>1 时级数收敛, 当 $p \leqslant 1$ 时级数发散, 因此只根据 $\rho=1$ 不能判定级数的收敛性.

例4 证明级数

$$
1 + \frac {1}{1} + \frac {1}{1 \times 2} + \frac {1}{1 \times 2 \times 3} + \dots + \frac {1}{(n - 1) !} + \dots
$$

是收敛的,并估计以级数的部分和 $s_n$ 近似代替和 $s$ 所产生的误差.

解 因为

$$
\lim _ {n \rightarrow \infty} \frac {u _ {n + 1}}{u _ {n}} = \lim _ {n \rightarrow \infty} \frac {(n - 1) !}{n !} = \lim _ {n \rightarrow \infty} \frac {1}{n} = 0 <   1,
$$

根据比值审敛法可知所给级数收敛.

以这级数的部分和 $s_{n}$ 近似代替和 s 所产生的误差为

$$
\begin{array}{l} \mid r _ {n} \mid = \frac {1}{n !} + \frac {1}{(n + 1) !} + \frac {1}{(n + 2) !} + \dots \\ = \frac {1}{n !} \left[ 1 + \frac {1}{n + 1} + \frac {1}{(n + 1) (n + 2)} + \dots \right] \\ <   \frac {1}{n !} \left(1 + \frac {1}{n} + \frac {1}{n ^ {2}} + \dots\right) \\ = \frac {1}{n !} \frac {1}{1 - \frac {1}{n}} = \frac {1}{(n - 1) (n - 1) !}. \\ \end{array}
$$

例5 判定级数

$$
\frac {1}{1 0} + \frac {1 \times 2}{1 0 ^ {2}} + \frac {1 \times 2 \times 3}{1 0 ^ {3}} + \dots + \frac {n !}{1 0 ^ {n}} + \dots
$$

的收敛性.

解 因为

$$
\frac {u _ {n + 1}}{u _ {n}} = \frac {(n + 1) !}{1 0 ^ {n + 1}} \times \frac {1 0 ^ {n}}{n !} = \frac {n + 1}{1 0},
$$

$$
\lim _ {n \rightarrow \infty} \frac {u _ {n + 1}}{u _ {n}} = \lim _ {n \rightarrow \infty} \frac {n + 1}{1 0} = \infty .
$$

根据比值审敛法可知所给级数发散.

* 定理 5(根值审敛法,柯西判别法) 设 $\sum_{n=1}^{\infty} u_n$ 为正项级数,如果

$$
\lim _ {n \rightarrow \infty} \sqrt [ n ]{u _ {n}} = \rho ,
$$

那么当 $\rho < 1$ 时级数收敛, $\rho > 1$ (或 $\lim_{n \to \infty} \sqrt[n]{u_n} = +\infty$ ) 时级数发散, $\rho = 1$ 时级数可能收敛也可能发散.

定理 5 的证明与定理 4 相仿, 这里从略.

例6 判定级数 $\sum_{n=1}^{\infty} \frac{2 + (-1)^n}{2^n}$ 的收敛性.

证 $\lim_{n\to \infty}\sqrt[n]{u_n} = \lim_{n\to \infty}\frac{1}{2}\sqrt[n]{2 + (-1)^n} = \lim_{n\to \infty}\frac{1}{2}\mathrm{e}^{\frac{1}{n}\ln [2 + (-1)^n ]},$ 

因 $\ln [2 + (-1)^n ]$ 有界，故 $\lim_{n\to \infty}\frac{1}{n}\ln [2 + (-1)^n ] = 0$ ，从而

$$
\lim _ {n \rightarrow \infty} \sqrt [ n ]{u _ {n}} = \frac {1}{2}.
$$

因此,根据根值审敛法知所给级数收敛.

将所给正项级数与 p 级数作比较, 可得在实用上较方便的极限审敛法.

定理6（极限审敛法）设 $\sum_{n = 1}^{\infty}u_n$ 为正项级数，

（1）如果 $\lim_{n\to \infty}nu_n = l > 0$ （或 $\lim_{n\to \infty}nu_n = +\infty$ ），那么级数 $\sum_{n = 1}^{\infty}u_n$ 发散；

(2) 如果 p>1，而 $\lim_{n\to\infty}n^{p}u_{n}=l\quad(0\leqslant l<+\infty)$ ，那么级数 $\sum_{n=1}^{\infty}u_{n}$ 收敛.

证（1）在极限形式的比较审敛法中，取 $v_{n} = \frac{1}{n}$ ，由调和级数 $\sum_{n=1}^{\infty} \frac{1}{n}$ 发散，知结论成立.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/145f8003a231538389279d19548cb56df6157a0d218571d8e49eee3ced7c0678.jpg)


例题精讲 12-3

(2) 在极限形式的比较审敛法中, 取 $v_{n} = \frac{1}{n^{p}}$ , 当 $p > 1$ 时, $p$ 级数 $\sum_{n=1}^{\infty} \frac{1}{n^{p}}$ 收敛, 故结论成立.

例7 判定级数 $\sum_{n=1}^{\infty} \ln \left(1 + \frac{1}{n^2}\right)$ 的收敛性.

解 因 $\ln \left(1 + \frac{1}{n^2}\right) \sim \frac{1}{n^2} (n \to \infty)$ , 故

$$
\lim _ {n \rightarrow \infty} n ^ {2} u _ {n} = \lim _ {n \rightarrow \infty} n ^ {2} \ln \left(1 + \frac {1}{n ^ {2}}\right) = \lim _ {n \rightarrow \infty} n ^ {2} \times \frac {1}{n ^ {2}} = 1,
$$

根据极限审敛法,知所给级数收敛.

例8 判定级数 $\sum_{n=1}^{\infty} \sqrt{n+1}\left(1 - \cos \frac{\pi}{n}\right)$ 的收敛性.

解 因为

$$
\lim _ {n \rightarrow \infty} n ^ {\frac {3}{2}} u _ {n} = \lim _ {n \rightarrow \infty} n ^ {\frac {3}{2}} \sqrt {n + 1} \left(1 - \cos \frac {\pi}{n}\right) = \lim _ {n \rightarrow \infty} n ^ {2} \sqrt {\frac {n + 1}{n}} \times \frac {1}{2} \left(\frac {\pi}{n}\right) ^ {2} = \frac {1}{2} \pi^ {2},
$$

根据极限审敛法,知所给级数收敛.

# 二、交错级数及其审敛法

所谓交错级数是这样的级数,它的各项是正负交错的,从而可以写成下面的形式:

$$
u _ {1} - u _ {2} + u _ {3} - u _ {4} + \dots , \tag {2-3}
$$

或

$$
- u _ {1} + u _ {2} - u _ {3} + u _ {4} - \dots , \tag {2-4}
$$

其中 $u_{1}, u_{2}, \cdots$ 都是正数. 我们按级数 (2-3) 的形式来证明关于交错级数的一个审敛法.

定理7（莱布尼茨定理）如果交错级数 $\sum_{n=1}^{\infty} (-1)^{n-1} u_n$ 满足条件：

(1) $u_{n}\geqslant u_{n+1}\quad(n=1,2,3,\cdots);$ 

(2) $\lim_{n\to \infty}u_n = 0,$ 

那么级数收敛,且其和 $s \leqslant u_{1}$ , 其余项 $r_{n}$ 的绝对值 $\left|r_{n}\right| \leqslant u_{n+1}$ .

证 先证明前 $2n$ 项的和 $s_{2n}$ 的极限存在.为此把 $s_{2n}$ 写成两种形式：

$$
s _ {2 n} = \left(u _ {1} - u _ {2}\right) + \left(u _ {3} - u _ {4}\right) + \dots + \left(u _ {2 n - 1} - u _ {2 n}\right)
$$

及

$$
s _ {2 n} = u _ {1} - \left(u _ {2} - u _ {3}\right) - \left(u _ {4} - u _ {5}\right) - \dots - \left(u _ {2 n - 2} - u _ {2 n - 1}\right) - u _ {2 n}.
$$

根据条件(1)知道所有括号中的差都是非负的.由第一种形式可见数列 $\{s_{2n}\}$ 是单调增加的,由第二种形式可见 $s_{2n}<u_{1}$ .于是,根据单调有界数列必有极限的准则知道,当n无

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/65c1dfccd33658cc7c0683e33fca6210accaa6a2e87a3afd8c147e94a622d751.jpg)


释疑解难

12-2 

限增大时, $s_{2n}$ 趋于一个极限s,并且s不大于 $u_{1}$ :

$$
\lim _ {n \rightarrow \infty} s _ {2 n} = s \leqslant u _ {1}.
$$

再证明前 $2n + 1$ 项的和 $s_{2n + 1}$ 的极限也是 $s$ . 事实上, 我们有

$$
s _ {2 n + 1} = s _ {2 n} + u _ {2 n + 1}.
$$

由条件(2)知 $\lim_{n\to\infty}u_{2n+1}=0$ ，因此

$$
\lim _ {n \rightarrow \infty} s _ {2 n + 1} = \lim _ {n \rightarrow \infty} (s _ {2 n} + u _ {2 n + 1}) = s.
$$

由于级数的前偶数项的和与奇数项的和趋于同一极限 $s$ ，故级数 $\sum_{n=1}^{\infty} (-1)^{n-1} u_n$ 的部分和 $s_n$ 当 $n \to \infty$ 时具有极限 $s$ . 这就证明了级数 $\sum_{n=1}^{\infty} (-1)^{n-1} u_n$ 收敛于和 $s$ ，且 $s \leqslant u_1$ .

最后,不难看出余项 $r_{n}$ 可以写成

$$
r _ {n} = \pm \left(u _ {n + 1} - u _ {n + 2} + \dots\right),
$$

其绝对值

$$
\mid r _ {n} \mid = u _ {n + 1} - u _ {n + 2} + \dots ,
$$

上式右端也是一个交错级数,它也满足收敛的两个条件,所以其和小于级数的第一项,也就是说

$$
\left| r _ {n} \right| \leqslant u _ {n + 1}.
$$

证明完毕.

例如,交错级数

$$
1 - \frac {1}{2} + \frac {1}{3} - \frac {1}{4} + \dots + (- 1) ^ {n - 1} \frac {1}{n} + \dots
$$

满足条件

(1) $u_{n} = \frac{1}{n} > \frac{1}{n+1} = u_{n+1} (n=1,2,\cdots)$ 

及

(2) $\lim_{n\to \infty}u_n = \lim_{n\to \infty}\frac{1}{n} = 0,$ 

所以它是收敛的,且其和 s<1. 如果取前 n 项的和

$$
s _ {n} = 1 - \frac {1}{2} + \frac {1}{3} - \dots + (- 1) ^ {n - 1} \frac {1}{n}
$$

作为 $s$ 的近似值，所产生的误差 $\left|r_n\right| \leqslant \frac{1}{n + 1} (= u_{n + 1})$ 

# 三、绝对收敛与条件收敛

现在我们讨论一般的级数

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/e0dbdbd199c33adf05eb0288acf90702b22e6afce5436a00533c618312b54bea.jpg)


例题精讲

$$
u _ {1} + u _ {2} + \dots + u _ {n} + \dots ,
$$

它的各项为任意实数.如果级数 $\sum_{n=1}^{\infty} u_n$ 各项的绝对值所构成的正项级数 $\sum_{n=1}^{\infty} |u_n|$ 收敛,那么称级数 $\sum_{n=1}^{\infty} u_n$ 绝对收敛;如果级数 $\sum_{n=1}^{\infty} u_n$ 收敛,而级数 $\sum_{n=1}^{\infty} |u_n|$ 发散,那么称级数 $\sum_{n=1}^{\infty} u_n$ 条件收敛.容易知道,级数 $\sum_{n=1}^{\infty} (-1)^{n-1} \frac{1}{n^2}$ 是绝对收敛级数,而级数 $\sum_{n=1}^{\infty} (-1)^{n-1} \frac{1}{n}$ 是条件收敛级数.

级数绝对收敛与级数收敛有以下重要关系：

定理8 如果级数 $\sum_{n=1}^{\infty} u_n$ 绝对收敛, 那么级数 $\sum_{n=1}^{\infty} u_n$ 必定收敛.

证令

$$
v _ {n} = \frac {1}{2} (u _ {n} + | u _ {n} |) \quad (n = 1, 2, \dots).
$$

显然 $v_{n}\geqslant0$ 且 $v_{n}\leqslant\left|u_{n}\right|\quad(n=1,2,\cdots)$ .因级数 $\sum_{n=1}^{\infty}\left|u_{n}\right|$ 收敛,故由比较审敛法知道,级数 $\sum_{n=1}^{\infty}v_{n}$ 收敛,从而级数 $\sum_{n=1}^{\infty}2v_{n}$ 也收敛.而 $u_{n}=2v_{n}-\left|u_{n}\right|$ ,由收敛级数的基本性质可知

$$
\sum_ {n = 1} ^ {\infty} u _ {n} = \sum_ {n = 1} ^ {\infty} 2 v _ {n} - \sum_ {n = 1} ^ {\infty} | u _ {n} |,
$$

所以级数 $\sum_{n=1}^{\infty} u_n$ 收敛. 定理证毕.

上述证明中引入的级数 $\sum_{n=1}^{\infty} v_n$ ，其一般项

$$
v _ {n} = \frac {1}{2} (u _ {n} + | u _ {n} |) = \left\{ \begin{array}{l l} u _ {n}, & u _ {n} > 0, \\ 0, & u _ {n} \leqslant 0, \end{array} \right.
$$

可见级数 $\sum_{n=1}^{\infty} v_n$ 是把级数 $\sum_{n=1}^{\infty} u_n$ 中的负项换成 0 而得的, 它也就是级数 $\sum_{n=1}^{\infty} u_n$ 中的全体正项所构成的级数. 类似可知, 令

$$
w _ {n} = \frac {1}{2} (\mid u _ {n} \mid - u _ {n}),
$$

则 $\sum_{n=1}^{\infty} w_n$ 为级数 $\sum_{n=1}^{\infty} u_n$ 中全体负项的绝对值所构成的级数. 如果级数 $\sum_{n=1}^{\infty} u_n$ 绝对收敛, 那么级数 $\sum_{n=1}^{\infty} v_n$ 与 $\sum_{n=1}^{\infty} w_n$ 都收敛; 如果级数条件收敛 (即 $\sum_{n=1}^{\infty} u_n$ 收敛, 而 $\sum_{n=1}^{\infty} |u_n|$ 发

散），那么级数 $\sum_{n=1}^{\infty} v_n$ 与 $\sum_{n=1}^{\infty} w_n$ 都发散.

定理8说明,对于一般的级数 $\sum_{n=1}^{\infty} u_n$ , 如果我们用正项级数的审敛法判定级数 $\sum_{n=1}^{\infty} |u_n|$ 收敛, 那么此级数收敛. 这就使得一大类级数的收敛性判定问题, 转化成正项级数的收敛性判定问题.

一般说来,如果级数 $\sum_{n=1}^{\infty}|u_n|$ 发散,我们不能断定级数 $\sum_{n=1}^{\infty}u_n$ 也发散.但是,如果我们用比值审敛法或根值审敛法根据 $\lim_{n\to \infty}\left|\frac{u_{n+1}}{u_n}\right| = \rho >1$ 或 $\lim_{n\to \infty}\sqrt[n]{|u_n|} = \rho >1$ 判定级数 $\sum_{n=1}^{\infty}|u_n|$ 发散,那么我们可以断定级数 $\sum_{n=1}^{\infty}u_n$ 必定发散.这是因为从 $\rho >1$ 可推知 $|u_n|\not\to 0 (n\to \infty)$ ,从而 $u_n\not\to 0 (n\to \infty)$ ,因此级数 $\sum_{n=1}^{\infty}u_n$ 是发散的.

例9 判定级数 $\sum_{n=1}^{\infty} \frac{\sin n\alpha}{n^2}$ 的收敛性.

解 因为 $\left|\frac{\sin n\alpha}{n^{2}}\right| \leqslant \frac{1}{n^{2}}$ ，而级数 $\sum_{n=1}^{\infty}\frac{1}{n^{2}}$ 收敛，所以级数 $\sum_{n=1}^{\infty}\left|\frac{\sin n\alpha}{n^{2}}\right|$ 也收敛。由定理8知，级数 $\sum_{n=1}^{\infty}\frac{\sin n\alpha}{n^{2}}$ 收敛。

例10 判定级数 $\sum_{n=1}^{\infty} (-1)^{n} \frac{1}{2^{n}} \left(1 + \frac{1}{n}\right)^{n^{2}}$ 的收敛性.

解 这是交错级数. 记 $u_{n} = \frac{1}{2^{n}}\left(1 + \frac{1}{n}\right)^{n^{2}}$ ，有

$$
\sqrt [ n ]{u _ {n}} = \frac {1}{2} \left(1 + \frac {1}{n}\right) ^ {n} \rightarrow \frac {1}{2} \mathrm{e} (n \rightarrow \infty),
$$

而 $\frac{1}{2}\mathrm{e} > 1$ ，可知 $u_{n}\not\to 0(n\rightarrow \infty)$ ，因此所给级数发散.

# 四、绝对收敛级数的性质

绝对收敛级数有很多性质是条件收敛级数所没有的,下面给出关于绝对收敛级数的两个性质.

定理 9 绝对收敛级数经改变项的位置后构成的级数也收敛,且与原级数有相同的和(即绝对收敛级数具有可交换性).

证 （1）先证定理对于收敛的正项级数是正确的.

设级数

$$
u _ {1} + u _ {2} + \dots + u _ {n} + \dots
$$

为收敛的正项级数,其部分和为 $s_{n}$ , 和为 s. 并设级数

$$
u _ {1} ^ {*} + u _ {2} ^ {*} + \dots + u _ {n} ^ {*} + \dots
$$

为改变项的位置后构成的级数,其部分和为 $s_{n}^{*}$ .

对于任何 n，当它固定后，取 m 足够大，使 $u_{1}^{*}, u_{2}^{*}, \cdots, u_{n}^{*}$ 各项都出现在 $s_{m} = u_{1} + u_{2} + \cdots + u_{m}$ 中，于是得

$$
s _ {n} ^ {*} \leqslant s _ {m} \leqslant s,
$$

所以,单调增加的数列 $\{s_{n}^{*}\}$ 不超过定数s,根据单调有界数列必有极限的准则(第一章第六节),可知 $\lim_{n\to\infty}s_{n}^{*}$ 存在,即级数 $\sum_{n=1}^{\infty}u_{n}^{*}$ 收敛,且

$$
\lim _ {n \rightarrow \infty} s _ {n} ^ {*} = s ^ {*} \leqslant s.
$$

另一方面,如果把原来级数 $\sum_{n=1}^{\infty}u_{n}$ 看成是级数 $\sum_{n=1}^{\infty}u_{n}^{*}$ 改变项的位置以后所成的级数,那么应用刚才证得的结论,又有

$$
s \leqslant s ^ {*}
$$

要使得上面两个不等式同时成立,必定有

$$
s ^ {*} = s.
$$

(2) 再证定理对一般的绝对收敛级数是正确的.

设级数 $\sum_{n=1}^{\infty}|u_n|$ 收敛.在定理8的证明中已得

$$
u _ {n} = 2 v _ {n} - \left| u _ {n} \right|,
$$

而 $\sum_{n=1}^{\infty} v_n$ 是收敛的正项级数. 故有

$$
\sum_ {n = 1} ^ {\infty} u _ {n} = \sum_ {n = 1} ^ {\infty} (2 v _ {n} - | u _ {n} |) = \sum_ {n = 1} ^ {\infty} 2 v _ {n} - \sum_ {n = 1} ^ {\infty} | u _ {n} |.
$$

若级数 $\sum_{n=1}^{\infty} u_n$ 改变项的位置后的级数为 $\sum_{n=1}^{\infty} u_n^*$ ，则相应的 $\sum_{n=1}^{\infty} v_n$ 改变为 $\sum_{n=1}^{\infty} v_n^*$ ， $\sum_{n=1}^{\infty} |u_n|$ 改变为 $\sum_{n=1}^{\infty} |u_n^*|$ ，由(1)证得的结论可知

$$
\sum_ {n = 1} ^ {\infty} v _ {n} = \sum_ {n = 1} ^ {\infty} v _ {n} ^ {*}, \quad \sum_ {n = 1} ^ {\infty} | u _ {n} | = \sum_ {n = 1} ^ {\infty} | u _ {n} ^ {*} |.
$$

所以

$$
\sum_ {n = 1} ^ {\infty} u _ {n} ^ {*} = \sum_ {n = 1} ^ {\infty} 2 v _ {n} ^ {*} - \sum_ {n = 1} ^ {\infty} | u _ {n} ^ {*} | = \sum_ {n = 1} ^ {\infty} 2 v _ {n} - \sum_ {n = 1} ^ {\infty} | u _ {n} | = \sum_ {n = 1} ^ {\infty} u _ {n}.
$$

证毕.

在给出绝对收敛级数的另一个性质以前,我们先来讨论级数的乘法运算.

设级数 $\sum_{n=1}^{\infty}u_{n}$ 和 $\sum_{n=1}^{\infty}v_{n}$ 都收敛,仿照有限项之和相乘的规则,作出这两个级数的项所有可能的乘积 $u_{i}v_{k}\quad(i,k=1,2,3,\cdots)$ ,这些乘积是

$$
\begin{array}{l} u _ {1} v _ {1}, u _ {1} v _ {2}, u _ {1} v _ {3}, \dots , u _ {1} v _ {i}, \dots , \\ u _ {2} v _ {1}, u _ {2} v _ {2}, u _ {2} v _ {3}, \dots , u _ {2} v _ {i}, \dots , \\ u _ {3} v _ {1}, u _ {3} v _ {2}, u _ {3} v _ {3}, \dots , u _ {3} v _ {i}, \dots , \\ u _ {k} v _ {1}, u _ {k} v _ {2}, u _ {k} v _ {3}, \dots , u _ {k} v _ {i}, \dots , \\ \end{array}
$$

... 

... 

这些乘积可以用很多方式将它们排列成一个数列.例如可以按“对角线法”或按“正方形法”将它们排列成下面形状的数列(图12-2):

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/4b64dd82e820985a13ef36064ee3902d04d6afb9a97c8e8f13c3338ddb618c47.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/b514ce01e2c1c62d59925523dbaed5a9a6de067a5072647bc8d297a23433eac0.jpg)



图12-2


（对角线法） $u_{1}v_{1};u_{1}v_{2},u_{2}v_{1};\cdots;u_{1}v_{n},u_{2}v_{n-1},\cdots,u_{n}v_{1};\cdots.$ 

（正方形法） $u_{1}v_{1};u_{1}v_{2},u_{2}v_{2},u_{2}v_{1};\cdots;u_{1}v_{n},u_{2}v_{n},\cdots,u_{n}v_{n},u_{n}v_{n-1},\cdots,u_{n}v_{1};\cdots.$ 

把上面排列好的数列用加号相连,就组成无穷级数.我们称按“对角线法”排列所组成的级数

$$
u _ {1} v _ {1} + \left(u _ {1} v _ {2} + u _ {2} v _ {1}\right) + \dots + \left(u _ {1} v _ {n} + u _ {2} v _ {n - 1} + \dots + u _ {n} v _ {1}\right) + \dots .
$$

为两级数 $\sum_{n=1}^{\infty}u_{n}$ 和 $\sum_{n=1}^{\infty}v_{n}$ 的柯西乘积.

定理10（绝对收敛级数的乘法）设级数 $\sum_{n=1}^{\infty} u_n$ 和 $\sum_{n=1}^{\infty} v_n$ 都绝对收敛，其和分别为 $s$ 和 $\sigma$ ，则它们的柯西乘积

$$
u _ {1} v _ {1} + \left(u _ {1} v _ {2} + u _ {2} v _ {1}\right) + \dots + \left(u _ {1} v _ {n} + u _ {2} v _ {n - 1} + \dots + u _ {n} v _ {1}\right) + \dots \tag {2-5}
$$

也是绝对收敛的,且其和为 $s\sigma$ .

证 考虑把级数(2-5)的括号去掉后所成的级数

$$
u _ {1} v _ {1} + u _ {1} v _ {2} + u _ {2} v _ {1} + \dots + u _ {1} v _ {n} + \dots . \tag {2-6}
$$

如果级数(2-6)绝对收敛且其和为 $w$ ，那么由收敛级数的基本性质4及比较审敛法可知，级数(2-5)也绝对收敛且其和为 $w$ 。因此只要证明级数(2-6)绝对收敛且其和 $w = s\sigma$ 就行了。

(1) 先证级数(2-6)绝对收敛.

设 $w_{m}$ 为级数(2-6)的前 $m$ 项分别取绝对值后所作成的和，又设

$$
\sum_ {n = 1} ^ {\infty} \mid u _ {n} \mid = A, \quad \sum_ {n = 1} ^ {\infty} \mid v _ {n} \mid = B,
$$

则显然有

$$
w _ {m} \leqslant \sum_ {n = 1} ^ {\infty} | u _ {n} | \cdot \sum_ {n = 1} ^ {\infty} | v _ {n} | \leqslant A B.
$$

由此可见单调增加数列 $\{w_{m}\}$ 不超过定数AB,所以级数(2-6)绝对收敛.

(2) 再证级数(2-6)的和 $w = s\sigma$ .

把级数(2-6)的各项位置重新排列并加上括号使它成为按“正方形法”排列所组成的级数

$$
u _ {1} v _ {1} + \left(u _ {1} v _ {2} + u _ {2} v _ {2} + u _ {2} v _ {1}\right) + \dots + \left(u _ {1} v _ {n} + u _ {2} v _ {n} + \dots + u _ {n} v _ {n} + u _ {n} v _ {n - 1} + \dots + u _ {n} v _ {1}\right) + \dots . \tag {2-7}
$$

根据定理 9 及收敛级数的基本性质 4 可知,对于绝对收敛级数(2-6) 这样做法是不会改变其和的.容易看出,级数(2-7) 的前 n 项的和恰好为

$$
\left(u _ {1} + u _ {2} + \dots + u _ {n}\right) \cdot \left(v _ {1} + v _ {2} + \dots + v _ {n}\right) = s _ {n} \sigma_ {n},
$$

因此

$$
w = \lim _ {n \rightarrow \infty} (s _ {n} \sigma_ {n}) = s \sigma .
$$

# 习题12-2

1. 以下各题中给出了四个结论,从中选出一个正确的结论:

(1) 设 $\sum_{n=1}^{\infty}a_{n}$ 是收敛的正项级数, $b_{n}=\frac{1-\cos a_{n}}{a_{n}}, c_{n}=\frac{1-\cos\sqrt{a_{n}}}{\sqrt{a_{n}}}$ . 则有() ;

(A) $\sum_{n=1}^{\infty} b_n$ 和 $\sum_{n=1}^{\infty} c_n$ 均收敛

(B) $\sum_{n=1}^{\infty} b_n$ 收敛, $\sum_{n=1}^{\infty} c_n$ 敛散性不确定

(C) $\sum_{n=1}^{\infty} b_n$ 和 $\sum_{n=1}^{\infty} c_n$ 均发散

(D) $\sum_{n=1}^{\infty} b_n$ 发散, $\sum_{n=1}^{\infty} c_n$ 敛散性不确定

(2) 设有两个数列 $\{a_{n}\}$ 和 $\{b_{n}\}$ ，若 $\lim_{n\to\infty}a_{n}=0$ ，则有（）.

(A) 当 $\sum_{n=1}^{\infty} b_n$ 收敛时, $\sum_{n=1}^{\infty} a_n b_n$ 收敛

(B) 当 $\sum_{n=1}^{\infty} b_n$ 发散时, $\sum_{n=1}^{\infty} a_n b_n$ 发散

(C) 当 $\sum_{n=1}^{\infty}|b_n|$ 收敛时, $\sum_{n=1}^{\infty}|a_nb_n|$ 收敛(D) 当 $\sum_{n=1}^{\infty}|b_n|$ 发散时, $\sum_{n=1}^{\infty}|a_nb_n|$ 发散

2. 用比较审敛法或极限形式的比较审敛法判定下列级数的收敛性：

(1) $1+\frac{1}{3}+\frac{1}{5}+\cdots+\frac{1}{2n-1}+\cdots;$ 

(2) $1 + \frac{1 + 2}{1 + 2^2} +\frac{1 + 3}{1 + 3^2} +\dots +\frac{1 + n}{1 + n^2} +\dots ;$ 

(3) $\frac{1}{2 \times 5} + \frac{1}{3 \times 6} + \cdots + \frac{1}{(n+1)(n+4)} + \cdots$ ; 

(4) $\sin\frac{\pi}{2}+\sin\frac{\pi}{2^{2}}+\sin\frac{\pi}{2^{3}}+\cdots+\sin\frac{\pi}{2^{n}}+\cdots;$ 

(5) $\sum_{n=1}^{\infty} \frac{1}{1 + a^n} (a > 0)$ . 

3. 用比值审敛法判定下列级数的收敛性：

(1) $\frac{3}{1\times2}+\frac{3^{2}}{2\times2^{2}}+\frac{3^{3}}{3\times2^{3}}+\cdots+\frac{3^{n}}{n\times2^{n}}+\cdots;$ 

(2) $\sum_{n=1}^{\infty} \frac{n^{2}}{3^{n}}$ ; 

(3) $\sum_{n=1}^{\infty} \frac{2^n \times n!}{n^n}$ ; 

(4) $\sum_{n=1}^{\infty} n \tan \frac{\pi}{2^{n+1}}$ . 

* 4. 用根值审敛法判定下列级数的收敛性：

(1) $\sum_{n=1}^{\infty}\left(\frac{n}{2n+1}\right)^{n}$ ; 

(2) $\sum_{n=1}^{\infty} \frac{1}{[\ln(n+1)]^{n}}$ ; 

(3) $\sum_{n=1}^{\infty}\left(\frac{n}{3n-1}\right)^{2n-1}$ ; 

(4) $\sum_{n=1}^{\infty}\left(\frac{b}{a_n}\right)^n$ , 其中 $a_n \to a (n \to \infty)$ , $a_n, b, a$ 均为正数.

5. 判定下列级数的收敛性：

(1) $\frac{3}{4}+2\left(\frac{3}{4}\right)^{2}+3\left(\frac{3}{4}\right)^{3}+\cdots+n\left(\frac{3}{4}\right)^{n}+\cdots;$ 

(2) $\frac{1^{4}}{1!}+\frac{2^{4}}{2!}+\frac{3^{4}}{3!}+\cdots+\frac{n^{4}}{n!}+\cdots;$ 

(3) $\sum_{n=1}^{\infty} \frac{n+1}{n(n+2)}$ ; 

(4) $\sum_{n=1}^{\infty} 2^{n} \sin \frac{\pi}{3^{n}}$ ; 

(5) $\sqrt{2} + \sqrt{\frac{3}{2}} + \cdots + \sqrt{\frac{n+1}{n}} + \cdots$ ; 

(6) $\frac{1}{a+b}+\frac{1}{2a+b}+\cdots+\frac{1}{na+b}+\cdots\quad(a>0,b>0).$ 

6. 判定下列级数是否收敛,如果是收敛的,是绝对收敛还是条件收敛?

(1) $1-\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{3}}-\frac{1}{\sqrt{4}}+\cdots+\frac{(-1)^{n-1}}{\sqrt{n}}+\cdots;$ 

(2) $\sum_{n=1}^{\infty} (-1)^{n-1} \frac{n}{3^{n-1}}$ ; 

(3) $\frac{1}{3} \times \frac{1}{2} - \frac{1}{3} \times \frac{1}{2^2} + \frac{1}{3} \times \frac{1}{2^3} - \frac{1}{3} \times \frac{1}{2^4} + \cdots + (-1)^{n-1} \frac{1}{3} \times \frac{1}{2^n} + \cdots$ ; 

(4) $\frac{1}{\ln2}-\frac{1}{\ln3}+\frac{1}{\ln4}-\frac{1}{\ln5}+\cdots+(-1)^{n-1}\frac{1}{\ln(n+1)}+\cdots;$ 

(5) $\sum_{n=1}^{\infty} (-1)^{n+1} \frac{2^{n^2}}{n!}$ . 

# 第三节 幂级数

# 一、函数项级数的概念

如果给定一个定义在区间 $I$ 上的函数列

$$
u _ {1} (x), u _ {2} (x), u _ {3} (x), \dots , u _ {n} (x), \dots ,
$$

那么由这函数列构成的表达式

$$
u _ {1} (x) + u _ {2} (x) + u _ {3} (x) + \dots + u _ {n} (x) + \dots \tag {3-1}
$$

称为定义在区间 I 上的(函数项)无穷级数,简称(函数项)级数.

对于每一个确定的值 $x_0 \in I$ ，函数项级数(3-1)成为常数项级数

$$
u _ {1} (x _ {0}) + u _ {2} (x _ {0}) + u _ {3} (x _ {0}) + \dots + u _ {n} (x _ {0}) + \dots . \tag {3-2}
$$

这个级数(3-2)可能收敛也可能发散.如果级数(3-2)收敛,就称点 $x_{0}$ 是函数项级数(3-1)的收敛点;如果级数(3-2)发散,就称点 $x_{0}$ 是函数项级数(3-1)的发散点.函数项级数(3-1)的收敛点的全体称为它的收敛域,发散点的全体称为它的发散域.

对应于收敛域内的任意一个数 $x$ ，函数项级数成为一收敛的常数项级数，因而有一确定的和 $s$ . 这样，在收敛域上，函数项级数的和是 $x$ 的函数 $s(x)$ ，通常称 $s(x)$ 为函数项级数的和函数，这个函数的定义域就是级数的收敛域，并写成

$$
s (x) = u _ {1} (x) + u _ {2} (x) + u _ {3} (x) + \dots + u _ {n} (x) + \dots = \sum_ {i = 1} ^ {\infty} u _ {i} (x).
$$

把函数项级数(3-1)的前 n 项的部分和记作 $s_{n}(x)$ ，则在收敛域上有

$$
\lim _ {n \rightarrow \infty} s _ {n} (x) = s (x).
$$

记 $r_n(x) = s(x) - s_n(x), r_n(x)$ 叫做函数项级数的余项（当然，只有 $x$ 在收敛域上 $r_n(x)$ 才有意义），并有

$$
\lim _ {n \rightarrow \infty} r _ {n} (x) = 0.
$$

# 二、幂级数及其收敛性

函数项级数中简单而常见的一类级数就是各项都是常数乘幂函数的函数项级数, 即所谓幂级数, 它的形式是①

$$
\sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n} = a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \dots + a _ {n} x ^ {n} + \dots , \tag {3-3}
$$

其中常数 $a_{0}, a_{1}, a_{2}, \cdots, a_{n}, \cdots$ 叫做幂级数的系数.例如

$$
1 + x + x ^ {2} + \dots + x ^ {n} + \dots ,
$$

$$
1 + x + \frac {1}{2 !} x ^ {2} + \dots + \frac {1}{n !} x ^ {n} + \dots
$$

都是幂级数.

现在我们来讨论:对于一个给定的幂级数,它的收敛域与发散域是怎样的?即x取数轴上哪些点时幂级数收敛,取哪些点时幂级数发散?这就是幂级数的收敛性问题.

先看一个例子.考察幂级数

$$
1 + x + x ^ {2} + \dots + x ^ {n} + \dots
$$

的收敛性.由第一节例1知道,当 $|x|<1$ 时,这级数收敛于和 $\frac{1}{1-x}$ ;当 $|x|\geqslant1$ 时,这级数发散.因此,这幂级数的收敛域是开区间 $(-1,1)$ ,发散域是 $(-∞,-1]$ 及 $[1,+∞)$ ,并有

$$
\frac {1}{1 - x} = 1 + x + x ^ {2} + \dots + x ^ {n} + \dots \quad (- 1 <   x <   1).
$$

在这个例子中我们看到,这个幂级数的收敛域是一个区间.事实上,这个结论对于一般的幂级数也是成立的.我们有如下定理:

定理1（阿贝尔（Abel）定理）如果级数 $\sum_{n=0}^{\infty} a_n x^n$ 当 $x = x_0$ ( $x_0 \neq 0$ ) 时收敛，那么适合不等式 $|x| < |x_0|$ 的一切 $x$ 使这幂级数绝对收敛。反之，如果级数 $\sum_{n=0}^{\infty} a_n x^n$ 当 $x = x_0$ 时发散，那么适合不等式 $|x| > |x_0|$ 的一切 $x$ 使这幂级数发散。

证 先设 $x_0$ 是幂级数(3-3)的收敛点, 即级数

$$
a _ {0} + a _ {1} x _ {0} + a _ {2} x _ {0} ^ {2} + \dots + a _ {n} x _ {0} ^ {n} + \dots
$$

收敛.根据级数收敛的必要条件,这时有

$$
\lim _ {n \rightarrow \infty} a _ {n} x _ {0} ^ {n} = 0,
$$

于是存在一个常数 M, 使得

$$
\mid a _ {n} x _ {0} ^ {n} \mid \leqslant M (n = 0, 1, 2, \dots).
$$

这样级数(3-3)的一般项的绝对值

$$
\mid a _ {n} x ^ {n} \mid = \left| a _ {n} x _ {0} ^ {n} \cdot \frac {x ^ {n}}{x _ {0} ^ {n}} \right| = \mid a _ {n} x _ {0} ^ {n} \mid \cdot \left| \frac {x}{x _ {0}} \right| ^ {n} \leqslant M \left| \frac {x}{x _ {0}} \right| ^ {n}.
$$

因为当 $|x| < |x_0|$ 时，等比级数 $\sum_{n=0}^{\infty} M \left| \frac{x}{x_0} \right|^n$ 收敛（公比 $\left| \frac{x}{x_0} \right| < 1$ ），所以级数 $\sum_{n=0}^{\infty} |a_n x^n|$ 收敛，也就是级数 $\sum_{n=0}^{\infty} a_n x^n$ 绝对收敛.

定理的第二部分可用反证法证明. 假设幂级数当 $x = x_0$ 时发散而有一点 $x_1$ 适合 $|x_1| > |x_0|$ 使级数收敛, 则根据本定理的第一部分, 级数当 $x = x_0$ 时应收敛, 这与假设矛盾. 定理得证.

定理1表明,如果幂级数在 $x = x_0$ 处收敛,那么对于开区间 $(-|x_0|, |x_0|)$ 内的任何 $x$ , 幂级数都收敛; 如果幂级数在 $x = x_0$ 处发散, 那么对于闭区间 $[-|x_0|, |x_0|]$ 外的任何 $x$ , 幂级数都发散.

设已给幂级数在数轴上既有收敛点(不仅是原点)也有发散点.现在从原点沿数轴向右方走,最初只遇到收敛点,然后就只遇到发散点.这两部分的界点可能是收敛点也可能是发散点.从原点沿数轴向左方走情形也是如此.两个界点P与 $P'$ 在原点的两侧,

且由定理1可以证明它们到原点的距离是一样的(图12-3).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/cb51b9474cfe51df7cafde2ee35d3143eb95530e5a88522c5e773e435bc12f60.jpg)



图12-3


从上面的几何说明,得到下述重要推论:

推论 如果幂级数 $\sum_{n=0}^{\infty} a_n x^n$ 不是仅在 $x = 0$ 一点收敛, 也不是在整个数轴上都收敛, 那么必有一个确定的正数 $R$ 存在, 使得

当 $|x| < R$ 时，幂级数绝对收敛；

当 $\left|x\right|>R$ 时, 幂级数发散;

当 x=R 与 x=-R 时, 幂级数可能收敛也可能发散.

正数 R 通常叫做幂级数(3-3)的收敛半径. 开区间 $(-R, R)$ 叫做幂级数(3-3)的收敛区间. 再由幂级数在 $x = \pm R$ 处的收敛性就可以决定它的收敛域是 $(-R, R)$ ， $[-R, R)$ ， $(-R, R]$ 或 $[-R, R]$ 这四个区间之一.

如果幂级数(3-3)只在 $x = 0$ 处收敛, 这时收敛域只有一点 $x = 0$ , 但为了方便起见, 规定这时收敛半径 $R = 0$ ; 如果幂级数(3-3)对一切 $x$ 都收敛, 则规定收敛半径 $R = +\infty$ , 这时收敛域是 $(- \infty, + \infty)$ . 这两种情形确实都是存在的, 见下面的例2及例3.

关于幂级数的收敛半径的求法,有下面的定理.

定理2 如果

$$
\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \rho ,
$$

其中 $a_{n}, a_{n+1}$ 是幂级数 $\sum_{n=0}^{\infty} a_{n} x^{n}$ 的相邻两项的系数, 那么这幂级数的收敛半径

$$
R = \left\{ \begin{array}{l l} \frac {1}{\rho}, & \rho \neq 0, \\ + \infty , & \rho = 0, \\ 0, & \rho = + \infty . \end{array} \right.
$$

证 考察幂级数(3-3)的各项取绝对值所成的级数

$$
\left| a _ {0} \right| + \left| a _ {1} x \right| + \left| a _ {2} x ^ {2} \right| + \dots + \left| a _ {n} x ^ {n} \right| + \dots , \tag {3-4}
$$

这级数相邻两项之比为

$$
\frac {\left| a _ {n + 1} x ^ {n + 1} \right|}{\left| a _ {n} x ^ {n} \right|} = \left| \frac {a _ {n + 1}}{a _ {n}} \right| | x |.
$$

（1）如果 $\lim_{n\to \infty}\left|\frac{a_{n + 1}}{a_n}\right| = \rho (\rho \neq 0)$ 存在，根据比值审敛法，那么当 $\rho |x| < 1$ 即 $|x| < \frac{1}{\rho}$ 时，级数(3-4)收敛，从而级数(3-3)绝对收敛；当 $\rho |x| > 1$ 即 $|x| > \frac{1}{\rho}$ 时，级数(3-4)发散并且从某一个 $n$ 开始

$$
\left| a _ {n + 1} x ^ {n + 1} \right| > \left| a _ {n} x ^ {n} \right|,
$$

因此一般项 $\left|a_{n}x^{n}\right|$ 不能趋于零, 所以 $a_{n}x^{n}$ 也不能趋于零, 从而级数 (3-3) 发散. 于是收敛半径 $R=\frac{1}{\rho}$ .

(2) 如果 $\rho = 0$ , 那么对任何 $x \neq 0$ , 有 $\frac{|a_{n+1}x^{n+1}|}{|a_n x^n|} \to 0 (n \to \infty)$ , 所以级数 (3-4) 收敛, 从而级数 (3-3) 绝对收敛. 于是 $R = +\infty$ .

（3）如果 $\rho=+\infty$ ，那么对于除 x=0 外的其他一切 x 值，级数（3-3）必发散，否则由定理 1 知道将有点 $x\neq0$ 使级数（3-4）收敛。于是 R=0。

例1 求幂级数 $x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots + (-1)^{n-1} \frac{x^n}{n} + \cdots$ 的收敛半径与收敛域.

解 因为

$$
\rho = \lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {\frac {1}{n + 1}}{\frac {1}{n}} = 1,
$$

所以收敛半径

$$
R = \frac {1}{\rho} = 1.
$$

对于端点 x = -1，级数成为

# 

例题精讲

12-5 

$$
- 1 - \frac {1}{2} - \frac {1}{3} - \dots - \frac {1}{n} - \dots ,
$$

此级数发散；

对于端点 x=1，级数成为交错级数

$$
1 - \frac {1}{2} + \frac {1}{3} - \dots + (- 1) ^ {n - 1} \frac {1}{n} + \dots ,
$$

此级数收敛.因此,收敛域是 $(-1,1]$ .

例 2 求幂级数 $1 + x + \frac{1}{2!}x^{2} + \cdots + \frac{1}{n!}x^{n} + \cdots$ 的收敛域.

解 因为

$$
\rho = \lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {\frac {1}{(n + 1) !}}{\frac {1}{n !}} = \lim _ {n \rightarrow \infty} \frac {1}{n + 1} = 0,
$$

所以收敛半径 $R=+\infty$ ，从而收敛域是 $(-∞,+∞)$ .

例3 求幂级数 $\sum_{n=0}^{\infty} n! x^n$ 的收敛半径（规定 $0! = 1$ ）.

解 因为

$$
\rho = \lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {(n + 1) !}{n !} = + \infty ,
$$

所以收敛半径 R=0，即级数仅在点 x=0 处收敛.

例4 求幂级数 $\sum_{n=0}^{\infty} \frac{(2n)!}{(n!)^2} x^{2n}$ 的收敛半径.

解 级数缺少奇次幂的项,定理 2 不能直接应用.我们根据比值审敛法来求收敛半径:

$$
\lim _ {n \rightarrow \infty} \left| \frac {\frac {[ 2 (n + 1) ] !}{[ (n + 1) ! ] ^ {2}} x ^ {2 (n + 1)}}{\frac {(2 n) !}{(n !) ^ {2}} x ^ {2 n}} \right| = 4 | x | ^ {2}.
$$

当 $4|x|^{2} < 1$ 即 $|x| < \frac{1}{2}$ 时，级数收敛；当 $4|x|^{2} > 1$ 即 $|x| > \frac{1}{2}$ 时，级数发散.所以收敛半径 $R = \frac{1}{2}$ .

例5 求幂级数 $\sum_{n=1}^{\infty} \frac{(x-1)^n}{2^n \cdot n}$ 的收敛域.

解 令 t=x-1，上述级数变为

$$
\sum_ {n = 1} ^ {\infty} \frac {t ^ {n}}{2 ^ {n} \cdot n}.
$$

因为

$$
\rho = \lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {2 ^ {n} \cdot n}{2 ^ {n + 1} (n + 1)} = \frac {1}{2},
$$

所以收敛半径 R=2 。收敛区间为 $\left| t \right| < 2$ ，即 -1 < x < 3 。

当 $x = -1$ 时，级数成为 $\sum_{n=1}^{\infty} \frac{(-1)^n}{n}$ ，这级数收敛；当 $x = 3$ 时，级数成为 $\sum_{n=1}^{\infty} \frac{1}{n}$ ，这级数发散。因此原级数的收敛域为 $[-1,3)$ 。

# 三、幂级数的运算

设幂级数

$$
a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \dots + a _ {n} x ^ {n} + \dots
$$

及

$$
b _ {0} + b _ {1} x + b _ {2} x ^ {2} + \dots + b _ {n} x ^ {n} + \dots
$$

分别在区间 $(-R, R)$ 及 $(-R', R')$ 内收敛，对于这两个幂级数，可以进行下列四则运算：

加法

$$
\begin{array}{l} \left(a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \dots + a _ {n} x ^ {n} + \dots\right) + \left(b _ {0} + b _ {1} x + b _ {2} x ^ {2} + \dots + b _ {n} x ^ {n} + \dots\right) \\ = \left(a _ {0} + b _ {0}\right) + \left(a _ {1} + b _ {1}\right) x + \left(a _ {2} + b _ {2}\right) x ^ {2} + \dots + \left(a _ {n} + b _ {n}\right) x ^ {n} + \dots . \\ \end{array}
$$

减法

$$
\begin{array}{l} \left(a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \dots + a _ {n} x ^ {n} + \dots\right) - \left(b _ {0} + b _ {1} x + b _ {2} x ^ {2} + \dots + b _ {n} x ^ {n} + \dots\right) \\ = \left(a _ {0} - b _ {0}\right) + \left(a _ {1} - b _ {1}\right) x + \left(a _ {2} - b _ {2}\right) x ^ {2} + \dots + \left(a _ {n} - b _ {n}\right) x ^ {n} + \dots . \\ \end{array}
$$

根据收敛级数的基本性质2,上面两式在 $(-R,R)$ 与 $(-R',R')$ 中较小的区间内成立.

乘法

$$
\begin{array}{l} \left(a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \dots + a _ {n} x ^ {n} + \dots\right) \left(b _ {0} + b _ {1} x + b _ {2} x ^ {2} + \dots + b _ {n} x ^ {n} + \dots\right) \\ = a _ {0} b _ {0} + \left(a _ {0} b _ {1} + a _ {1} b _ {0}\right) x + \left(a _ {0} b _ {2} + a _ {1} b _ {1} + a _ {2} b _ {0}\right) x ^ {2} + \dots + \left(a _ {0} b _ {n} + a _ {1} b _ {n - 1} + \dots + a _ {n} b _ {0}\right) x ^ {n} + \dots . \\ \end{array}
$$

这是两个幂级数的柯西乘积. 可以证明上式在 $(-R, R)$ 与 $(-R', R')$ 中较小的区间内成立.

除法

$$
\frac {a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \cdots + a _ {n} x ^ {n} + \cdots}{b _ {0} + b _ {1} x + b _ {2} x ^ {2} + \cdots + b _ {n} x ^ {n} + \cdots} = c _ {0} + c _ {1} x + c _ {2} x ^ {2} + \dots + c _ {n} x ^ {n} + \dots ,
$$

这里假设 $b_{0} \neq 0$ . 为了决定系数 $c_{0}, c_{1}, c_{2}, \cdots, c_{n}, \cdots$ , 可以将级数 $\sum_{n=0}^{\infty} b_{n} x^{n}$ 与 $\sum_{n=0}^{\infty} c_{n} x^{n}$ 相

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/30cddf6682dc232b87ab2421425136cbc39c08f323a414ba54d167cade1b0f59.jpg)


释疑解难

12-3 

乘,并令乘积中各项的系数分别等于级数 $\sum_{n=0}^{\infty}a_{n}x^{n}$ 中同次幂的系数,即得

$$
a _ {0} = b _ {0} c _ {0},
$$

$$
a _ {1} = b _ {1} c _ {0} + b _ {0} c _ {1},
$$

$$
a _ {2} = b _ {2} c _ {0} + b _ {1} c _ {1} + b _ {0} c _ {2},
$$

... 

由这些方程就可以顺序地求出 $c_{0}, c_{1}, c_{2}, \cdots, c_{n}, \cdots$ 

相除后所得的幂级数 $\sum_{n=0}^{\infty} c_n x^n$ 的收敛区间可能比原来两级数的收敛区间小得多①.

关于幂级数的和函数有下列重要性质②:

性质1 幂级数 $\sum_{n=0}^{\infty} a_n x^n$ 的和函数 $s(x)$ 在其收敛域 $I$ 上连续.

性质2 幂级数 $\sum_{n=0}^{\infty} a_n x^n$ 的和函数 $s(x)$ 在其收敛域 $I$ 上可积, 并有逐项积分公式

$$
\int_ {0} ^ {x} s (t) \mathrm{d} t = \int_ {0} ^ {x} \left[ \sum_ {n = 0} ^ {\infty} a _ {n} t ^ {n} \right] \mathrm{d} t = \sum_ {n = 0} ^ {\infty} \int_ {0} ^ {x} a _ {n} t ^ {n} \mathrm{d} t = \sum_ {n = 0} ^ {\infty} \frac {a _ {n}}{n + 1} x ^ {n + 1} \quad (x \in I), \tag {3-5}
$$

逐项积分后所得到的幂级数和原级数有相同的收敛半径.

性质3 幂级数 $\sum_{n=0}^{\infty} a_n x^n$ 的和函数 $s(x)$ 在其收敛区间 $(-R, R)$ 内可导，且有逐项求导公式

$$
s ^ {\prime} (x) = \left(\sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}\right) ^ {\prime} = \sum_ {n = 0} ^ {\infty} \left(a _ {n} x ^ {n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1} \quad (\mid x \mid <   R), \tag {3-6}
$$

逐项求导后所得到的幂级数和原级数有相同的收敛半径.

反复应用上述结论可得:幂级数 $\sum_{n=0}^{\infty}a_{n}x^{n}$ 的和函数 $s(x)$ 在其收敛区间 $(-R,R)$ 内具有任意阶导数.

例6 求幂级数 $\sum_{n=0}^{\infty} \frac{x^n}{n+1}$ 的和函数.

解 先求收敛域.由

① 例如

$$
\frac {1}{1 - x} = 1 + x + x ^ {2} + \dots + x ^ {n} + \dots .
$$

级数 $\sum_{n=0}^{\infty}a_{n}x^{n}=1+0x+\cdots+0x^{n}+\cdots$ 与 $\sum_{n=0}^{\infty}b_{n}x^{n}=1-x+0x^{2}+\cdots+0x^{n}+\cdots$ 在整个数轴上收敛，但级数 $\sum_{n=0}^{\infty}c_{n}x^{n}=\sum_{n=0}^{\infty}x^{n}$ 仅在区间 $(-1,1)$ 内收敛.

② 证明见本章第六节第二目.

$$
\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {n + 1}{n + 2} = 1,
$$

得收敛半径 R=1.

在端点 $x = -1$ 处，幂级数成为 $\sum_{n=0}^{\infty} \frac{(-1)^n}{n+1}$ ，是收敛的交错级数；在端点 $x = 1$ 处，幂级数成为 $\sum_{n=0}^{\infty} \frac{1}{n+1}$ ，是发散的。因此收敛域为 $I = [-1, 1)$ 。

设和函数为 $s(x)$ ，即

$$
s (x) = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n + 1}, \quad x \in [ - 1, 1).
$$

于是

$$
x s (x) = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n + 1}}{n + 1}.
$$

利用性质 3, 逐项求导, 并由

$$
\frac {1}{1 - x} = 1 + x + x ^ {2} + \dots + x ^ {n} + \dots (- 1 <   x <   1),
$$

得

$$
[ x s (x) ] ^ {\prime} = \sum_ {n = 0} ^ {\infty} \left(\frac {x ^ {n + 1}}{n + 1}\right) ^ {\prime} = \sum_ {n = 0} ^ {\infty} x ^ {n} = \frac {1}{1 - x} \quad (\mid x \mid <   1).
$$

对上式从 0 到 x 积分, 得

$$
x s (x) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm{d} t = - \ln (1 - x) (- 1 \leqslant x <   1).
$$

于是, 当 $x \neq 0$ 时, 有 $s(x) = -\frac{1}{x} \ln(1 - x)$ . 而 $s(0)$ 可由 $s(0) = a_{0} = 1$ 得出, 也可由和函数的连续性得到

$$
s (0) = \lim _ {x \rightarrow 0} s (x) = \lim _ {x \rightarrow 0} \left[ - \frac {1}{x} \ln (1 - x) \right] = 1.
$$

故

$$
s (x) = \left\{ \begin{array}{l l} - \frac {1}{x} \ln (1 - x), & x \in [ - 1, 0) \cup (0, 1), \\ 1, & x = 0. \end{array} \right.
$$

# 习题12-3

1. 下题中给出了四个结论,从中选出一个正确的结论:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/376f8b21d4a226f2bdc6823db2185cdaa3d8bf95c53c9aa33c3657cf3a702c3f.jpg)


例题精讲

12-6 

已知 $\alpha > 0$ ，若幂级数 $\sum_{n=1}^{\infty} a_n(x + \alpha)^n$ 在 $x = 0$ 处发散，在 $x = -2\alpha$ 处收敛，则幂级数 $\sum_{n=1}^{\infty} a_n(x - \alpha)^n$ 的收敛域为（ ）.

(A) $[-2\alpha, 0)$ 

(B) $[0,2\alpha)$ 

(C) $(-2\alpha, 0]$ 

(D) $(0,2\alpha ]$ 

2. 求下列幂级数的收敛区间：

(1) $x+2x^{2}+3x^{3}+\cdots+nx^{n}+\cdots;$ 

(2) $1-x+\frac{x^{2}}{2^{2}}+\cdots+(-1)^{n}\frac{x^{n}}{n^{2}}+\cdots;$ 

(3) $\frac{x}{2} + \frac{x^2}{2 \times 4} + \frac{x^3}{2 \times 4 \times 6} + \cdots + \frac{x^n}{2 \times 4 \times \cdots \times (2n)} + \cdots$ ; 

(4) $\frac{x}{1\times3}+\frac{x^{2}}{2\times3^{2}}+\frac{x^{3}}{3\times3^{3}}+\cdots+\frac{x^{n}}{n\times3^{n}}+\cdots;$ 

(5) $\frac{2}{2}x+\frac{2^{2}}{5}x^{2}+\frac{2^{3}}{10}x^{3}+\cdots+\frac{2^{n}}{n^{2}+1}x^{n}+\cdots;$ 

(6) $\sum_{n=1}^{\infty} (-1)^{n} \frac{x^{2n+1}}{2n+1}$ ; 

(7) $\sum_{n=1}^{\infty} \frac{2n-1}{2^n} x^{2n-2}$ ; 

(8) $\sum_{n=1}^{\infty} \frac{(x-5)^n}{\sqrt{n}}$ . 

3. 利用逐项求导或逐项积分, 求下列级数的和函数:

(1) $\sum_{n=1}^{\infty} nx^{n-1}$ ; 

(2) $\sum_{n=1}^{\infty} \frac{x^{4n+1}}{4n+1}$ ; 

(3) $x+\frac{x^{3}}{3}+\frac{x^{5}}{5}+\cdots+\frac{x^{2n-1}}{2n-1}+\cdots;$ 

(4) $\sum_{n=1}^{\infty}(n+2)x^{n+3}$ . 

# 第四节 函数展开成幂级数

前面讨论了幂级数的收敛域及其和函数的性质.但在许多应用中,我们遇到的却是相反的问题:给定函数 $f(x)$ ,要考虑它是否能在某个区间内“展开成幂级数”,就是说,是否能找到这样一个幂级数,它在某区间内收敛,且其和恰好就是给定的函数 $f(x)$ .如果能找到这样的幂级数,我们就说,函数 $f(x)$ 在该区间内能展开成幂级数,而这个幂级数在该区间内就表达了函数 $f(x)$ .

假设函数 $f(x)$ 在点 $x_0$ 的某邻域 $U(x_0)$ 内能展开成幂级数，即有

$$
f (x) = a _ {0} + a _ {1} \left(x - x _ {0}\right) + a _ {2} \left(x - x _ {0}\right) ^ {2} + \dots + a _ {n} \left(x - x _ {0}\right) ^ {n} + \dots , \quad x \in U \left(x _ {0}\right), \tag {4-1}
$$

则根据和函数的性质, 可知 $f(x)$ 在 $U(x_{0})$ 内应具有任意阶导数, 且

$$
f ^ {(n)} (x) = n! a _ {n} + (n + 1)! a _ {n + 1} (x - x _ {0}) + \frac {(n + 2) !}{2 !} a _ {n + 2} (x - x _ {0}) ^ {2} + \dots ,
$$

由此可得

$$
f ^ {(n)} (x _ {0}) = n! a _ {n},
$$

于是

$$
a _ {n} = \frac {1}{n !} f ^ {(n)} \left(x _ {0}\right) (n = 0, 1, 2, \dots). \tag {4-2}
$$

这就表明,如果函数 $f(x)$ 有幂级数展开式(4-1),那么该幂级数的系数 $a_{n}$ 由公式(4-2)确定,即该幂级数必为

$$
f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(x - x _ {0}\right) + \dots + \frac {1}{n !} f ^ {(n)} \left(x _ {0}\right) \left(x - x _ {0}\right) ^ {n} + \dots = \sum_ {n = 0} ^ {\infty} \frac {1}{n !} f ^ {(n)} \left(x _ {0}\right) \left(x - x _ {0}\right) ^ {n}, \tag {4-3}
$$

而展开式必为

$$
f (x) = \sum_ {n = 0} ^ {\infty} \frac {1}{n !} f ^ {(n)} \left(x _ {0}\right) \left(x - x _ {0}\right) ^ {n}, \quad x \in U \left(x _ {0}\right). \tag {4-4}
$$

幂级数(4-3)叫做函数 $f(x)$ 在点 $x_{0}$ 处的泰勒级数. 展开式(4-4)叫做函数 $f(x)$ 在点 $x_{0}$ 处的泰勒展开式.

由以上讨论可知,函数 $f(x)$ 在 $U(x_{0})$ 内能展开成幂级数的充分必要条件是泰勒展开式(4-4)成立,也就是泰勒级数(4-3)在 $U(x_{0})$ 内收敛,且收敛到 $f(x)$ .

下面讨论泰勒展开式(4-4)成立的条件.

定理 设函数 $f(x)$ 在点 $x_0$ 的某一邻域 $U(x_0)$ 内具有各阶导数，则 $f(x)$ 在该邻域内能展开成泰勒级数的充分必要条件是在该邻域内 $f(x)$ 的泰勒公式中的余项 $R_{n}(x)$ 当 $n \to \infty$ 时的极限为零，即

$$
\lim _ {n \to \infty} R _ {n} (x) = 0, \quad x \in U (x _ {0}).
$$

证 $f(x)$ 的 $n$ 阶泰勒公式为（见第三章第三节）

$$
f (x) = p _ {n} (x) + R _ {n} (x),
$$

其中

$$
p _ {n} (x) = f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(x - x _ {0}\right) + \dots + \frac {1}{n !} f ^ {(n)} \left(x _ {0}\right) \left(x - x _ {0}\right) ^ {n}
$$

叫做函数 $f(x)$ 的n次泰勒多项式,而

$$
R _ {n} (x) = f (x) - p _ {n} (x)
$$

就是定理中所指的余项.

由于 n 次泰勒多项式 $p_{n}(x)$ 就是级数 (4-3) 的前 $n+1$ 项部分和, 根据级数收敛的定义, 即有

$$
\begin{array}{l} \sum_ {n = 0} ^ {\infty} \frac {1}{n !} f ^ {(n)} \left(x _ {0}\right) \left(x - x _ {0}\right) ^ {n} = f (x), \quad x \in U \left(x _ {0}\right) \\ \Leftrightarrow \lim _ {n \rightarrow \infty} p _ {n} (x) = f (x), \quad x \in U \left(x _ {0}\right) \\ \Leftrightarrow \lim _ {n \rightarrow \infty} [ f (x) - p _ {n} (x) ] = 0, \quad x \in U \left(x _ {0}\right) \\ \Leftrightarrow \lim _ {n \rightarrow \infty} R _ {n} (x) = 0, \quad x \in U \left(x _ {0}\right). \\ \end{array}
$$

下面着重讨论 $x_{0}=0$ 的情形. 在(4-3)式中, 取 $x_{0}=0$ , 得

$$
f (0) + f ^ {\prime} (0) x + \dots + \frac {1}{n !} f ^ {(n)} (0) x ^ {n} + \dots = \sum_ {n = 0} ^ {\infty} \frac {1}{n !} f ^ {(n)} (0) x ^ {n}, \tag {4-5}
$$

级数(4-5)称为函数 $f(x)$ 的麦克劳林级数.若 $f(x)$ 能在 $(-r,r)$ 内展开成x的幂级数,则有

$$
f (x) = \sum_ {n = 0} ^ {\infty} \frac {1}{n !} f ^ {(n)} (0) x ^ {n} \quad (\mid x \mid <   r), \tag {4-6}
$$

(4-6)式称为函数 $f(x)$ 的麦克劳林展开式.

要把函数 $f(x)$ 展开成x的幂级数,可以按照下列步骤进行:

第一步 求出 $f(x)$ 的各阶导数 $f'(x)$ , $f''(x)$ , $\cdots$ , $f^{(n)}(x)$ , $\cdots$ , 如果在 x=0 处某阶导数不存在, 就停止进行, 例如在 x=0 处, $f(x)=x^{7/3}$ 的三阶导数不存在, 它就不能展开为 x 的幂级数.

第二步 求出函数及其各阶导数在 $x = 0$ 处的值

$$
f (0), f ^ {\prime} (0), f ^ {\prime \prime} (0), \dots , f ^ {(n)} (0), \dots .
$$

第三步 写出幂级数

$$
f (0) + f ^ {\prime} (0) x + \frac {f ^ {\prime \prime} (0)}{2 !} x ^ {2} + \dots + \frac {f ^ {(n)} (0)}{n !} x ^ {n} + \dots ,
$$

并求出收敛半径 R.

第四步 利用余项 $R_{n}(x)$ 的表达式 $R_{n}(x) = \frac{1}{(n + 1)!} f^{(n + 1)}(\theta x)x^{n + 1}(0 < \theta < 1)$ ，考察当 $x$ 在区间 $(-R, R)$ 内时余项 $R_{n}(x)$ 的极限是不是零。如果为零，那么函数 $f(x)$ 在区间 $(-R, R)$ 内的幂级数展开式为

$$
f (x) = f (0) + f ^ {\prime} (0) x + \frac {f ^ {\prime \prime} (0)}{2 !} x ^ {2} + \dots + \frac {f ^ {(n)} (0)}{n !} x ^ {n} + \dots (- R <   x <   R).
$$

例 1 将函数 $f(x)=\mathrm{e}^{x}$ 展开成 x 的幂级数.

解 所给函数的各阶导数为 $f^{(n)}(x)=\mathrm{e}^{x}\quad(n=1,2,\cdots)$ ，因此 $f^{(n)}(0)=1\quad(n=0,1,2,\cdots)$ ，这里 $f^{(0)}(0)=f(0)$ 。于是得级数

$$
1 + x + \frac {x ^ {2}}{2 !} + \dots + \frac {x ^ {n}}{n !} + \dots ,
$$

它的收敛半径 $R=+\infty$ .

对于任何有限的数 x 与 $\xi$ ( $\xi$ 在 0 与 x 之间), 余项的绝对值为

$$
\left| R _ {n} (x) \right| = \left| \frac {\mathrm{e} ^ {\xi}}{(n + 1) !} x ^ {n + 1} \right| <   \mathrm{e} ^ {| x |} \cdot \frac {| x | ^ {n + 1}}{(n + 1) !}.
$$

因 $\mathrm{e}^{|x|}$ 为有限值，而 $\frac{|x|^{n + 1}}{(n + 1)!}$ 是收敛级数 $\sum_{n = 0}^{\infty}\frac{|x|^{n + 1}}{(n + 1)!}$ 的一般项，所以当 $n\to \infty$ 时，

$$
\mathrm{e} ^ {| x |} \cdot \frac {| x | ^ {n + 1}}{(n + 1) !} \rightarrow 0,
$$

即当 $n \to \infty$ 时，有 $|R_n(x)| \to 0$ . 于是得展开式

$$
\begin{array}{l} \mathrm{e} ^ {x} = 1 + x + \frac {x ^ {2}}{2 !} + \dots + \frac {x ^ {n}}{n !} + \dots \\ (- \infty <   x <   + \infty). \tag {4-7} \\ \end{array}
$$

如果在 x=0 处附近, 用级数的部分和 (即多项式) 来近似代替 $e^{x}$ , 那么随着项数的增加, 它们就越来越接近于 $e^{x}$ , 如图 12-4 所示.

例 2 将函数 $f(x)=\sin x$ 展开成 x 的幂级数.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/310d6aea8ca0390e6ebd594ded91e23b829280360b8d6e4963623f094fb586da.jpg)



图12-4


解 所给函数的各阶导数为

$$
f ^ {(n)} (x) = \sin \left(x + n \cdot \frac {\pi}{2}\right) \quad (n = 1, 2, \dots),
$$

$f^{(n)}(0)$ 顺序循环地取0,1,0,-1, $\cdots$ ( $n=0,1,2,3,\cdots$ ),于是得级数

$$
x - \frac {x ^ {3}}{3 !} + \frac {x ^ {5}}{5 !} - \dots + (- 1) ^ {n} \frac {x ^ {2 n + 1}}{(2 n + 1) !} + \dots ,
$$

它的收敛半径 $R=+\infty$ .

对于任何有限的数 $x$ 与 $\xi$ （ $\xi$ 在0与 $x$ 之间），余项的绝对值当 $n \to \infty$ 时的极限为零：

$$
\mid R _ {n} (x) \mid = \left| \frac {\sin \left[ \xi + \frac {(n + 1) \pi}{2} \right]}{(n + 1) !} x ^ {n + 1} \right| \leqslant \frac {\mid x \mid^ {n + 1}}{(n + 1) !} \rightarrow 0 \quad (n \rightarrow \infty).
$$

因此得展开式

$$
\sin x = x - \frac {x ^ {3}}{3 !} + \frac {x ^ {5}}{5 !} - \dots + (- 1) ^ {n} \frac {x ^ {2 n + 1}}{(2 n + 1) !} + \dots \quad (- \infty <   x <   + \infty). \tag {4-8}
$$

以上将函数展开成幂级数的例子, 是直接按公式 $a_{n} = \frac{f^{(n)}(0)}{n!}$ 计算幂级数的系数, 最后考察余项 $R_{n}(x)$ 是否趋于零. 这种直接展开的方法计算量较大, 而且研究余项即使在初等函数中也不是一件容易的事. 下面介绍间接展开的方法, 这就是利用一些已知的函数展开式, 通过幂级数的运算 (如四则运算、逐项求导、逐项积分) 以及变量代换等, 将所给函数展开成幂级数. 这样做不但计算简单, 而且可以避免研究余项.

前面我们已经求得的幂级数展开式有

$$
\mathrm{e} ^ {x} = \sum_ {n = 0} ^ {\infty} \frac {1}{n !} x ^ {n} \quad (- \infty <   x <   + \infty), \tag {4-7}
$$

$$
\sin x = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{(2 n + 1) !} x ^ {2 n + 1} (- \infty <   x <   + \infty), \tag {4-8}
$$

$$
\frac {1}{1 + x} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {n} (- 1 <   x <   1). \tag {4-9}
$$

利用这三个展开式,可以求得许多函数的幂级数展开式.例如

对(4-9)式两端从0到x积分,可得

$$
\ln (1 + x) = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{n + 1} x ^ {n + 1} = \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} x ^ {n} (- 1 <   x \leqslant 1), \tag {4-10}
$$

对(4-8)式两端求导,即得

$$
\cos x = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{(2 n) !} x ^ {2 n} (- \infty <   x <   + \infty), \tag {4-11}
$$

把(4-7)式中的 $x$ 换成 $x \ln a$ , 可得

$$
a ^ {x} = \mathrm{e} ^ {x \ln a} = \sum_ {n = 0} ^ {\infty} \frac {(\ln a) ^ {n}}{n !} x ^ {n} \quad (- \infty <   x <   + \infty),
$$

把(4-9)式中的 $x$ 换成 $x^{2}$ , 可得

$$
\frac {1}{1 + x ^ {2}} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {2 n} \quad (- 1 <   x <   1),
$$

对上式从 0 到 x 积分, 可得

$$
\arctan x = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} x ^ {2 n + 1} \quad (- 1 \leqslant x \leqslant 1).
$$

(4-7)、(4-8)、(4-9)、(4-10)、(4-11)等五个幂级数展开式是最常用的,记住前三个,后两个也就掌握了.

下面再举几个用间接法把函数展开成幂级数的例子.

例 3 把函数 $f(x)=(1-x)\ln(1+x)$ 展开成 x 的幂级数.

解 由 $\ln (1 + x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} x^n (-1 < x \leqslant 1)$ 得

$$
\begin{array}{l} f (x) = (1 - x) \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} x ^ {n} = \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} x ^ {n} - \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} x ^ {n + 1} \\ = \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} x ^ {n} - \sum_ {n = 2} ^ {\infty} \frac {(- 1) ^ {n}}{n - 1} x ^ {n} = x + \sum_ {n = 2} ^ {\infty} \frac {(- 1) ^ {n - 1} (2 n - 1)}{n (n - 1)} x ^ {n} (- 1 <   x \leqslant 1). \\ \end{array}
$$

例4 将函数 $\sin x$ 展开成 $\left(x - \frac{\pi}{4}\right)$ 的幂级数.

解 因为

$$
\begin{array}{l} \sin x = \sin \left[ \frac {\pi}{4} + \left(x - \frac {\pi}{4}\right) \right] = \sin \frac {\pi}{4} \cos \left(x - \frac {\pi}{4}\right) + \cos \frac {\pi}{4} \sin \left(x - \frac {\pi}{4}\right) \\ = \frac {1}{\sqrt {2}} \left[ \cos \left(x - \frac {\pi}{4}\right) + \sin \left(x - \frac {\pi}{4}\right) \right], \\ \sin x = \sin \left[ \frac {\pi}{4} + \left(x - \frac {\pi}{4}\right) \right] = \sin \frac {\pi}{4} \cos \left(x - \frac {\pi}{4}\right) + \cos \frac {\pi}{4} \sin \left(x - \frac {\pi}{4}\right) \\ = \frac {1}{\sqrt {2}} \left[ \cos \left(x - \frac {\pi}{4}\right) + \sin \left(x - \frac {\pi}{4}\right) \right], \\ \end{array}
$$

并且有

$$
\cos \left(x - \frac {\pi}{4}\right) = 1 - \frac {\left(x - \frac {\pi}{4}\right) ^ {2}}{2 !} + \frac {\left(x - \frac {\pi}{4}\right) ^ {4}}{4 !} - \dots + \frac {(- 1) ^ {n}}{(2 n) !} \left(x - \frac {\pi}{4}\right) ^ {2 n} + \dots (- \infty <   x <   + \infty),
$$

$$
\sin \left(x - \frac {\pi}{4}\right) = \left(x - \frac {\pi}{4}\right) - \frac {\left(x - \frac {\pi}{4}\right) ^ {3}}{3 !} + \frac {\left(x - \frac {\pi}{4}\right) ^ {5}}{5 !} - \dots + \frac {(- 1) ^ {n}}{(2 n + 1) !} \left(x - \frac {\pi}{4}\right) ^ {2 n + 1} + \dots . (- \infty <   x <   + \infty),
$$

所以

$$
\sin x = \frac {1}{\sqrt {2}} \left[ 1 + \left(x - \frac {\pi}{4}\right) - \frac {\left(x - \frac {\pi}{4}\right) ^ {2}}{2 !} - \frac {\left(x - \frac {\pi}{4}\right) ^ {3}}{3 !} + \dots + \right.
$$

$$
\frac {(- 1) ^ {n}}{(2 n) !} \left(x - \frac {\pi}{4}\right) ^ {2 n} + \frac {(- 1) ^ {n}}{(2 n + 1) !} \left(x - \frac {\pi}{4}\right) ^ {2 n + 1} + \dots ] (- \infty <   x <   + \infty).
$$

例5 将函数 $f(x) = \frac{1}{x^2 + 4x + 3}$ 展开成 $(x - 1)$ 的幂级数.

解 因为

$$
\begin{array}{l} f (x) = \frac {1}{x ^ {2} + 4 x + 3} = \frac {1}{(x + 1) (x + 3)} = \frac {1}{2 (1 + x)} - \frac {1}{2 (3 + x)} \\ = \frac {1}{4 \left(1 + \frac {x - 1}{2}\right)} - \frac {1}{8 \left(1 + \frac {x - 1}{4}\right)}, \\ \end{array}
$$

而

$$
\frac {1}{4 \left(1 + \frac {x - 1}{2}\right)} = \frac {1}{4} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 ^ {n}} (x - 1) ^ {n} (- 1 <   x <   3),
$$

$$
\frac {1}{8 \left(1 + \frac {x - 1}{4}\right)} = \frac {1}{8} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{4 ^ {n}} (x - 1) ^ {n} (- 3 <   x <   5),
$$

所以

$$
f (x) = \frac {1}{x ^ {2} + 4 x + 3} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {1}{2 ^ {n + 2}} - \frac {1}{2 ^ {2 n + 3}}\right) (x - 1) ^ {n} (- 1 <   x <   3).
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/406eb8bc2bf1064fc2e0a0005e02309402902d2e00bd914292b50f86034f8885.jpg)


例题精讲

12-7 

最后,再举一个用直接法展开的例子.

例6 将函数 $f(x) = (1 + x)^m$ 展开成 $x$ 的幂级数, 其中 $m$ 为任意实数.

解 $f(x)$ 的各阶导数为

$$
\begin{array}{l} f ^ {\prime} (x) = m (1 + x) ^ {m - 1}, \\ f ^ {\prime \prime} (x) = m (m - 1) (1 + x) ^ {m - 2}, \\ \dots \\ f ^ {(n)} (x) = m (m - 1) (m - 2) \dots (m - n + 1) (1 + x) ^ {m - n}, \\ \dots \\ \end{array}
$$

所以

$$
f (0) = 1, \quad f ^ {\prime} (0) = m, \quad f ^ {\prime \prime} (0) = m (m - 1), \quad \dots ,
$$

$$
f ^ {(n)} (0) = m (m - 1) \dots (m - n + 1), \quad \dots
$$

于是得级数

$$
1 + m x + \frac {m (m - 1)}{2 !} x ^ {2} + \dots + \frac {m (m - 1) \cdots (m - n + 1)}{n !} x ^ {n} + \dots .
$$

这级数相邻两项的系数之比的绝对值

$$
\left| \frac {a _ {n + 1}}{a _ {n}} \right| = \left| \frac {m - n}{n + 1} \right|\rightarrow 1 (n \rightarrow \infty),
$$

因此,对于任何实数 m 这级数在开区间 $(-1,1)$ 内收敛.

为了避免直接研究余项,设这级数在开区间 $(-1,1)$ 内收敛到函数 $F(x)$ :

$$
F (x) = 1 + m x + \frac {m (m - 1)}{2 !} x ^ {2} + \dots + \frac {m (m - 1) \cdots (m - n + 1)}{n !} x ^ {n} + \dots (- 1 <   x <   1),
$$

下面证明 $F(x)=(1+x)^{m}$ (-1<x<1).

逐项求导,得

$$
F ^ {\prime} (x) = m \left[ 1 + \frac {m - 1}{1} x + \dots + \frac {(m - 1) \cdots (m - n + 1)}{(n - 1) !} x ^ {n - 1} + \dots \right],
$$

两端各乘 $(1+x)$ ，并把含有 $x^{n}(n=1,2,\cdots)$ 的两项合并起来。根据恒等式

$$
\frac {(m - 1) \cdots (m - n + 1)}{(n - 1) !} + \frac {(m - 1) \cdots (m - n)}{n !} = \frac {m (m - 1) \cdots (m - n + 1)}{n !} \quad (n = 1, 2, \dots),
$$

可得

$$
\begin{array}{l} (1 + x) F ^ {\prime} (x) = m \left[ 1 + m x + \frac {m (m - 1)}{2 !} x ^ {2} + \dots + \frac {m (m - 1) \cdots (m - n + 1)}{n !} x ^ {n} + \dots \right] \\ = m F (x) \quad (- 1 <   x <   1). \\ \end{array}
$$

现在令 $\varphi(x) = \frac{F(x)}{(1 + x)^m}$ , 于是 $\varphi(0) = F(0) = 1$ , 且

$$
\begin{array}{l} \varphi^ {\prime} (x) = \frac {(1 + x) ^ {m} F ^ {\prime} (x) - m (1 + x) ^ {m - 1} F (x)}{(1 + x) ^ {2 m}} \\ = \frac {(1 + x) ^ {m - 1} [ (1 + x) F ^ {\prime} (x) - m F (x) ]}{(1 + x) ^ {2 m}} = 0, \\ \end{array}
$$

所以 $\varphi(x) = c$ （常数）.但是 $\varphi(0) = 1$ ，从而 $\varphi(x) = 1$ ，即

$$
F (x) = (1 + x) ^ {m}.
$$

因此在区间 $(-1,1)$ 内有展开式

$$
(1 + x) ^ {m} = 1 + m x + \frac {m (m - 1)}{2 !} x ^ {2} + \dots + \frac {m (m - 1) \cdots (m - n + 1)}{n !} x ^ {n} + \dots (- 1 <   x <   1). \tag {4-12}
$$

在区间的端点,展开式是否成立要看 m 的数值而定.

公式(4-12)叫做二项展开式.特殊地,当m为正整数时,级数为x的m次多项式,这就是代数学中的二项式定理.

对应于 $m$ 为 $\frac{1}{2}$ 与 $-\frac{1}{2}$ 的二项展开式分别为

$$
\begin{array}{l} \sqrt {1 + x} = 1 + \frac {1}{2} x - \frac {1}{2 \times 4} x ^ {2} + \frac {1 \times 3}{2 \times 4 \times 6} x ^ {3} - \frac {1 \times 3 \times 5}{2 \times 4 \times 6 \times 8} x ^ {4} + \dots + \\ (- 1) ^ {n - 1} \frac {1 \times 3 \times 5 \times \cdots \times (2 n - 3)}{2 \times 4 \times 6 \times \cdots \times (2 n)} x ^ {n} + \dots (- 1 \leqslant x \leqslant 1), \\ \frac {1}{\sqrt {1 + x}} = 1 - \frac {1}{2} x + \frac {1 \times 3}{2 \times 4} x ^ {2} - \frac {1 \times 3 \times 5}{2 \times 4 \times 6} x ^ {3} + \frac {1 \times 3 \times 5 \times 7}{2 \times 4 \times 6 \times 8} x ^ {4} - \dots + \\ (- 1) ^ {n} \frac {1 \times 3 \times 5 \times \cdots \times (2 n - 1)}{2 \times 4 \times 6 \times \cdots \times (2 n)} x ^ {n} + \dots (- 1 <   x \leqslant 1). \\ \end{array}
$$

# 习题12-4

1. 求函数 $f(x)=\cos x$ 的泰勒级数，并验证它在整个数轴上收敛于这函数.

2. 将下列函数展开成 $x$ 的幂级数, 并求展开式成立的区间:

(1) sh $x=\frac{e^{x}-e^{-x}}{2}$ ; 

(2) $\ln(a+x)$ $(a>0)$ ; 

(3) $a^x$ （ $a > 0$ 且 $a \neq 1$ );

(4) $\sin^2 x$ ; 

(5) $(1 + x)\ln (1 + x)$ ; 

(6) $\frac{x}{\sqrt{1 + x^2}}.$ 

3. 将下列函数展开成 $(x-1)$ 的幂级数, 并求展开式成立的区间:

(1) $\sqrt{x^3}$ ; 

(2) $\lg x$ ; 

(3) $xe^{x}$ . 

4. 将函数 $f(x)=\cos x$ 展开成 $\left(x+\frac{\pi}{3}\right)$ 的幂级数.

5. 将函数 $f(x) = \frac{1}{x}$ 展开成 $(x - 3)$ 的幂级数.

6. 将函数 $f(x) = \frac{1}{x^2 + 3x + 2}$ 展开成 $(x + 4)$ 的幂级数.

# 第五节 函数的幂级数展开式的应用

# 一、近似计算

有了函数的幂级数展开式,就可用它来进行近似计算,即在展开式有效的区间上,函数值可以近似地利用这个级数按精确度要求计算出来.

例 1 计算 $\sqrt[5]{240}$ 的近似值, 要求误差不超过 0.0001.

解 因为

$$
\sqrt [ 5 ]{2 4 0} = \sqrt [ 5 ]{2 4 3 - 3} = 3 \left(1 - \frac {1}{3 ^ {4}}\right) ^ {1 / 5},
$$

所以在二项展开式(4-12)中取 $m=\frac{1}{5},x=-\frac{1}{3^{4}}$ ，即得

$$
\sqrt [ 5 ]{2 4 0} = 3 \left(1 - \frac {1}{5} \times \frac {1}{3 ^ {4}} - \frac {1 \times 4}{5 ^ {2} \times 2 !} \times \frac {1}{3 ^ {8}} - \frac {1 \times 4 \times 9}{5 ^ {3} \times 3 !} \times \frac {1}{3 ^ {1 2}} - \dots - \frac {1 \times 4 \times 9 \times \cdots \times (5 n - 6)}{5 ^ {n} \times n !} \times \frac {1}{3 ^ {4 n}} - \dots\right).
$$

这个级数收敛很快.取前两项的和作为 $\sqrt[5]{240}$ 的近似值,其误差(也叫做截断误差)为

$$
\begin{array}{l} \left| r _ {2} \right| = 3 \left(\frac {1 \times 4}{5 ^ {2} \times 2 !} \times \frac {1}{3 ^ {8}} + \frac {1 \times 4 \times 9}{5 ^ {3} \times 3 !} \times \frac {1}{3 ^ {1 2}} + \frac {1 \times 4 \times 9 \times 1 4}{5 ^ {4} \times 4 !} \times \frac {1}{3 ^ {1 6}} + \dots\right) \\ <   3 \times \frac {1 \times 4}{5 ^ {2} \times 2 !} \times \frac {1}{3 ^ {8}} \left[ 1 + \frac {1}{8 1} + \left(\frac {1}{8 1}\right) ^ {2} + \dots \right] \\ = \frac {6}{2 5} \times \frac {1}{3 ^ {8}} \times \frac {1}{1 - \frac {1}{8 1}} = \frac {1}{2 5 \times 2 7 \times 4 0} <   \frac {1}{2 0 0 0 0}, \\ \end{array}
$$

于是取近似式为

$$
\sqrt [ 5 ]{2 4 0} \approx 3 \left(1 - \frac {1}{5} \times \frac {1}{3 ^ {4}}\right).
$$

为了使“四舍五入”引起的误差(叫做舍入误差)与截断误差之和不超过 $10^{-4}$ ，计算时应取五位小数，然后再四舍五入。因此最后得

$$
\sqrt [ 5 ]{2 4 0} \approx 2. 9 9 2 6.
$$

例 2 计算 ln 2 的近似值, 要求误差不超过 0.0001.

解 在公式(4-10)中, 令 x=1 可得

$$
\ln 2 = 1 - \frac {1}{2} + \frac {1}{3} - \dots + (- 1) ^ {n - 1} \frac {1}{n} + \dots .
$$

取这级数前 n 项的和作为 $\ln 2$ 的近似值, 其误差为

$$
\mid r _ {n} \mid \leqslant \frac {1}{n + 1}
$$

(见第二节第二目).为了保证误差不超过 $10^{-4}$ ,就需要取级数的前10 000项进行计算.这样做计算量太大了,我们必须用收敛较快的级数来代替它.

把公式(4-10)

$$
\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} - \frac {x ^ {4}}{4} + \dots + (- 1) ^ {n - 1} \frac {x ^ {n}}{n} + \dots \quad (- 1 <   x \leqslant 1)
$$

中将 $x$ 换成 $-x$ ，得

$$
\ln (1 - x) = - x - \frac {x ^ {2}}{2} - \frac {x ^ {3}}{3} - \frac {x ^ {4}}{4} - \dots + (- 1) ^ {n - 1} \frac {(- x) ^ {n}}{n} + \dots \quad (- 1 \leqslant x <   1),
$$

两式相减,得到不含有偶次幂的展开式

$$
\ln \frac {1 + x}{1 - x} = \ln (1 + x) - \ln (1 - x) = 2 \left(x + \frac {1}{3} x ^ {3} + \frac {1}{5} x ^ {5} + \dots + \frac {1}{2 n + 1} x ^ {2 n + 1} + \dots\right) (- 1 <   x <   1).
$$

令 $\frac{1 + x}{1 - x} = 2$ ，解出 $x = \frac{1}{3}$ .以 $x = \frac{1}{3}$ 代入最后一个展开式，得

$$
\ln 2 = 2 \left(\frac {1}{3} + \frac {1}{3} \times \frac {1}{3 ^ {3}} + \frac {1}{5} \times \frac {1}{3 ^ {5}} + \frac {1}{7} \times \frac {1}{3 ^ {7}} + \dots + \frac {1}{2 n + 1} \times \frac {1}{3 ^ {2 n + 1}} + \dots\right).
$$

取前四项作为 $\ln 2$ 的近似值, 其误差为

$$
\begin{array}{l} \left| r _ {4} \right| = 2 \left(\frac {1}{9} \times \frac {1}{3 ^ {9}} + \frac {1}{1 1} \times \frac {1}{3 ^ {1 1}} + \frac {1}{1 3} \times \frac {1}{3 ^ {1 3}} + \dots + \frac {1}{2 n + 1} \times \frac {1}{3 ^ {2 n + 1}} + \dots\right) \\ <   \frac {2}{3 ^ {1 1}} \left[ 1 + \frac {1}{9} + \left(\frac {1}{9}\right) ^ {2} + \dots + \left(\frac {1}{9}\right) ^ {n} + \dots \right] \\ = \frac {2}{3 ^ {1 1}} \times \frac {1}{1 - \frac {1}{9}} = \frac {1}{4 \times 3 ^ {9}} <   \frac {1}{7 0 0 0 0}. \\ \end{array}
$$

于是取

$$
\ln 2 \approx 2 \left(\frac {1}{3} + \frac {1}{3} \times \frac {1}{3 ^ {3}} + \frac {1}{5} \times \frac {1}{3 ^ {5}} + \frac {1}{7} \times \frac {1}{3 ^ {7}}\right).
$$

同样地,考虑到舍入误差,计算时应取五位小数:

$$
\frac {1}{3} \approx 0. 3 3 3 3 3, \quad \frac {1}{3} \times \frac {1}{3 ^ {3}} \approx 0. 0 1 2 3 5, \quad \frac {1}{5} \times \frac {1}{3 ^ {5}} \approx 0. 0 0 0 8 2, \quad \frac {1}{7} \times \frac {1}{3 ^ {7}} \approx 0. 0 0 0 0 7.
$$

因此得

$$
\ln 2 \approx 0. 6 9 3 1.
$$

例 3 利用 $\sin x \approx x - \frac{x^{3}}{3!}$ 求 $\sin 9^{\circ}$ 的近似值, 并估计误差.

解 首先把角度化成弧度，

$$
9 ^ {\circ} = \frac {\pi}{1 8 0} \times 9 \text {弧度} = \frac {\pi}{2 0} \text {弧度},
$$

从而

$$
\sin \frac {\pi}{2 0} \approx \frac {\pi}{. 2 0} - \frac {1}{3 !} \left(\frac {\pi}{2 0}\right) ^ {3}.
$$

其次估计这个近似值的精确度.在 $\sin x$ 的幂级数展开式(4-8)中令 $x = \frac{\pi}{20}$ , 得

$$
\sin \frac {\pi}{2 0} = \frac {\pi}{2 0} - \frac {1}{3 !} \left(\frac {\pi}{2 0}\right) ^ {3} + \frac {1}{5 !} \left(\frac {\pi}{2 0}\right) ^ {5} - \frac {1}{7 !} \left(\frac {\pi}{2 0}\right) ^ {7} + \dots + \frac {(- 1) ^ {n}}{(2 n + 1) !} \left(\frac {\pi}{2 0}\right) ^ {2 n + 1} + \dots ,
$$

等式右端是一个收敛的交错级数,且各项的绝对值单调减少.取它的前两项之和作为 $\sin\frac{\pi}{20}$ 的近似值,其误差为

$$
\mid r _ {2} \mid \leqslant \frac {1}{5 !} \left(\frac {\pi}{2 0}\right) ^ {5} <   \frac {1}{1 2 0} \times 0. 2 ^ {5} <   \frac {1}{3 0 0 0 0 0}.
$$

因此取

$$
\frac {\pi}{2 0} \approx 0. 1 5 7 0 8 0, \quad \frac {1}{3 !} \left(\frac {\pi}{2 0}\right) ^ {3} \approx 0. 0 0 0 6 4 6,
$$

于是得

$$
\sin 9 ^ {\circ} \approx 0. 1 5 6 4 3,
$$

这时误差不超过 $10^{-5}$ .

利用幂级数不仅可计算一些函数值的近似值,而且可计算一些定积分的近似值.具体地说,如果被积函数在积分区间上能展开成幂级数,那么把这个幂级数逐项积分,用积分后的级数就可算出定积分的近似值.

例4 计算定积分

$$
\frac {2}{\sqrt {\pi}} \int_ {0} ^ {\frac {1}{2}} \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x
$$

的近似值,要求误差不超过0.0001（取 $\frac{1}{\sqrt{\pi}}\approx0.56419$ ）.

解 将 $e^{x}$ 的幂级数展开式(4-7)中的 x 换成 $-x^{2}$ ，就得到被积函数的幂级数展开式

$$
\begin{array}{l} \mathrm{e} ^ {- x ^ {2}} = 1 + \frac {\left(- x ^ {2}\right)}{1 !} + \frac {\left(- x ^ {2}\right) ^ {2}}{2 !} + \frac {\left(- x ^ {2}\right) ^ {3}}{3 !} + \dots + \frac {\left(- x ^ {2}\right) ^ {n}}{n !} + \dots \\ = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \frac {x ^ {2 n}}{n !} (- \infty <   x <   + \infty). \\ \end{array}
$$

于是,根据幂级数在收敛区间内逐项可积,得

$$
\frac {2}{\sqrt {\pi}} \int_ {0} ^ {\frac {1}{2}} \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x = \frac {2}{\sqrt {\pi}} \int_ {0} ^ {\frac {1}{2}} \left[ \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{n !} x ^ {2 n} \right] \mathrm{d} x = \frac {2}{\sqrt {\pi}} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{n !} \int_ {0} ^ {\frac {1}{2}} x ^ {2 n} \mathrm{d} x
$$

$$
= \frac {1}{\sqrt {\pi}} \left[ 1 - \frac {1}{2 ^ {2} \times 3} + \frac {1}{2 ^ {4} \times 5 \times 2 !} - \frac {1}{2 ^ {6} \times 7 \times 3 !} + \dots + (- 1) ^ {n} \frac {1}{2 ^ {2 n} (2 n + 1) n !} + \dots \right].
$$

取前四项的和作为近似值,其误差为

$$
\mid r _ {4} \mid \leqslant \frac {1}{\sqrt {\pi}} \frac {1}{2 ^ {8} \times 9 \times 4 !} <   \frac {1}{9 0 0 0 0},
$$

所以

$$
\frac {2}{\sqrt {\pi}} \int_ {0} ^ {\frac {1}{2}} \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x \approx \frac {1}{\sqrt {\pi}} \left(1 - \frac {1}{2 ^ {2} \times 3} + \frac {1}{2 ^ {4} \times 5 \times 2 !} - \frac {1}{2 ^ {6} \times 7 \times 3 !}\right),
$$

算得

$$
\frac {2}{\sqrt {\pi}} \int_ {0} ^ {\frac {1}{2}} \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x \approx 0. 5 2 0 5.
$$

例5 计算积分

$$
\int_ {0} ^ {1} \frac {\sin x}{x} \mathrm{d} x
$$

的近似值,要求误差不超过 0.0001.

解 由于 $\lim_{x\to 0}\frac{\sin x}{x} = 1$ ，因此所给积分不是反常积分.若定义被积函数在 $x = 0$ 处的值为1，则它在积分区间[0,1]上连续.

展开被积函数,有

$$
\frac {\sin x}{x} = 1 - \frac {x ^ {2}}{3 !} + \frac {x ^ {4}}{5 !} - \frac {x ^ {6}}{7 !} + \dots + (- 1) ^ {n} \frac {x ^ {2 n}}{(2 n + 1) !} + \dots (- \infty <   x <   + \infty).
$$

在区间[0,1]上逐项积分,得

$$
\int_ {0} ^ {1} \frac {\sin x}{x} \mathrm{d} x = 1 - \frac {1}{3 \times 3 !} + \frac {1}{5 \times 5 !} - \frac {1}{7 \times 7 !} + \dots + (- 1) ^ {n} \frac {1}{(2 n + 1) (2 n + 1) !} + \dots .
$$

因为第四项的绝对值

$$
\frac {1}{7 \times 7 !} <   \frac {1}{3 0 0 0 0},
$$

所以取前三项的和作为积分的近似值：

$$
\int_ {0} ^ {1} \frac {\sin x}{x} \mathrm{d} x \approx 1 - \frac {1}{3 \times 3 !} + \frac {1}{5 \times 5 !},
$$

算得

$$
\int_ {0} ^ {1} \frac {\sin x}{x} \mathrm{d} x \approx 0. 9 4 6 1.
$$

# 二、微分方程的幂级数解法

这里,我们简单介绍一阶微分方程和二阶齐次线性微分方程的幂级数解法.

为求一阶微分方程

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = f (x, y) \tag {5-1}
$$

满足初值条件 $y|_{x = x_0} = y_0$ 的特解，如果其中函数 $f(x,y)$ 是 $(x - x_0),(y - y_0)$ 的多项式

$$
f (x, y) = a _ {0 0} + a _ {1 0} \left(x - x _ {0}\right) + a _ {0 1} \left(y - y _ {0}\right) + \dots + a _ {l m} \left(x - x _ {0}\right) ^ {l} \left(y - y _ {0}\right) ^ {m}.
$$

那么可以设所求特解可展开为 $x - x_0$ 的幂级数：

$$
y = y _ {0} + a _ {1} (x - x _ {0}) + a _ {2} (x - x _ {0}) ^ {2} + \dots + a _ {n} (x - x _ {0}) ^ {n} + \dots , \tag {5-2}
$$

其中 $a_{1}, a_{2}, \cdots, a_{n}, \cdots$ 是待定的系数. 把 (5-2) 代入 (5-1) 中, 便得一恒等式, 比较所得恒等式两端 $x - x_{0}$ 的同次幂的系数, 就可定出常数 $a_{1}, a_{2}, \cdots$ , 以这些常数为系数的级数 (5-2) 在其收敛区间内就是方程 (5-1) 满足初值条件 $y \mid_{x = x_{0}} = y_{0}$ 的特解.

例6 求方程 $\frac{\mathrm{dy}}{\mathrm{dx}} = -y - x$ 满足 $y|_{x = 0} = 2$ 的特解.

解 这时, $x_{0}=0,y_{0}=2$ .故设方程的特解为

$$
y = 2 + a _ {1} x + a _ {2} x ^ {2} + \dots + a _ {n} x ^ {n} + \dots .
$$

由此，得 $y' = a_{1} + 2a_{2}x + \cdots + na_{n}x^{n-1} + \cdots$ 

将 y 及 $y'$ 的幂级数展开式代入方程, 得

$$
a _ {1} + 2 a _ {2} x + \dots + n a _ {n} x ^ {n - 1} + \dots = - 2 - (a _ {1} + 1) x - a _ {2} x ^ {2} - \dots - a _ {n} x ^ {n} - \dots .
$$

上式为恒等式, 比较上式两端 x 的同次幂的系数, 得

$$
a _ {1} = - 2, \quad 2 a _ {2} = - (a _ {1} + 1), \quad 3 a _ {3} = - a _ {2}, \quad \dots , \quad n a _ {n} = - a _ {n - 1}, \quad \dots .
$$

故 $a_1 = -2, a_2 = \frac{1}{2}, a_3 = -\frac{1}{3!}, \cdots$ 由数学归纳法可得

$$
a _ {n} = (- 1) ^ {n} \frac {1}{n !} (n \geqslant 2).
$$

于是,得

$$
y = 2 - 2 x + \frac {1}{2 !} x ^ {2} - \frac {1}{3 !} x ^ {3} + \dots + (- 1) ^ {n} \frac {1}{n !} x ^ {n} + \dots
$$

$$
\begin{array}{l} = 1 - x + \left[ 1 - x + \frac {1}{2 !} x ^ {2} - \frac {1}{3 !} x ^ {3} + \dots + (- 1) ^ {n} \frac {1}{n !} x ^ {n} + \dots \right] \\ = 1 - x + \mathrm{e} ^ {- x}. \\ \end{array}
$$

这就是所求的特解.

事实上,所给方程是一阶线性的,容易求得它的通解为 $y = C e^{-x} + 1 - x$ , 由条件 $y \mid_{x=0} = 2$ 确定常数 C = 1, 即得方程的特解 $y = e^{-x} + 1 - x$ .

关于二阶齐次线性方程

$$
y ^ {\prime \prime} + P (x) y ^ {\prime} + Q (x) y = 0 \tag {5-3}
$$

用幂级数求解的问题,我们先叙述一个定理:

定理 如果方程(5-3)中的系数 $P(x)$ 与 $Q(x)$ 可在 $-R < x < R$ 内展开为 $x$ 的幂级数, 那么在 $-R < x < R$ 内方程(5-3)必有形如

$$
y = \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}
$$

的解.

这定理的证明从略.

例7 求微分方程

$$
y ^ {\prime \prime} - x y = 0
$$

满足初值条件

$$
y \mid_ {x = 0} = 0, \quad y ^ {\prime} \mid_ {x = 0} = 1
$$

的特解.

解 这里 $P(x) = 0, Q(x) = -x$ 在整个数轴上满足定理的条件. 因此所求的解可在整个数轴上展开成 $x$ 的幂级数

$$
y = a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \dots + a _ {n} x ^ {n} + \dots = \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}. \tag {5-4}
$$

由条件 $y|_{x = 0} = 0$ ，得 $a_0 = 0.$ 对级数(5-4)逐项求导，有

$$
y ^ {\prime} = a _ {1} + 2 a _ {2} x + 3 a _ {3} x ^ {2} + \dots + n a _ {n} x ^ {n - 1} + \dots = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1},
$$

由条件 $y^{\prime}\mid_{x = 0} = 1$ ，得 $a_1 = 1.$ 于是所求特解 $\gamma$ 及 $y^\prime$ 的展开式成为

$$
y = x + a _ {2} x ^ {2} + a _ {3} x ^ {3} + \dots + a _ {n} x ^ {n} + \dots = x + \sum_ {n = 2} ^ {\infty} a _ {n} x ^ {n}, \tag {5-5}
$$

$$
y ^ {\prime} = 1 + 2 a _ {2} x + 3 a _ {3} x ^ {2} + \dots + n a _ {n} x ^ {n - 1} + \dots = 1 + \sum_ {n = 2} ^ {\infty} n a _ {n} x ^ {n - 1}. \tag {5-6}
$$

对级数(5-6)逐项求导,得

$$
y ^ {\prime \prime} = 2 a _ {2} + 3 \times 2 a _ {3} x + \dots + n (n - 1) a _ {n} x ^ {n - 2} + \dots = \sum_ {n = 2} ^ {\infty} n (n - 1) a _ {n} x ^ {n - 2}. \tag {5-7}
$$

把(5-5)和(5-7)代入所给方程,并按x的升幂集项,得

$$
2 a _ {2} + 3 \times 2 a _ {3} x + (4 \times 3 a _ {4} - 1) x ^ {2} + (5 \times 4 a _ {5} - a _ {2}) x ^ {3} +
$$

$$
(6 \times 5 a _ {6} - a _ {3}) x ^ {4} + \dots + [ (n + 2) (n + 1) a _ {n + 2} - a _ {n - 1} ] x ^ {n} + \dots = 0.
$$

因为上式是恒等式,所以上式左端各项的系数必全为零,于是有

$$
a _ {2} = 0, \quad a _ {3} = 0, \quad a _ {4} = \frac {1}{4 \times 3}, \quad a _ {5} = 0, \quad a _ {6} = 0, \quad \dots ,
$$

一般地

$$
a _ {n + 2} = \frac {a _ {n - 1}}{(n + 2) (n + 1)} \quad (n = 3, 4, \dots).
$$

从这递推公式可以推得

$$
a _ {7} = \frac {a _ {4}}{7 \times 6} = \frac {1}{7 \times 6 \times 4 \times 3}, \quad a _ {8} = \frac {a _ {5}}{8 \times 7} = 0, \quad a _ {9} = \frac {a _ {6}}{9 \times 8} = 0,
$$

$$
a _ {1 0} = \frac {a _ {7}}{1 0 \times 9} = \frac {1}{1 0 \times 9 \times 7 \times 6 \times 4 \times 3}, \dots ,
$$

一般地

$$
a _ {3 m - 1} = a _ {3 m} = 0,
$$

$$
a _ {3 m + 1} = \frac {1}{(3 m + 1) \times (3 m) \times \cdots \times 7 \times 6 \times 4 \times 3} \quad (m = 1, 2, \dots).
$$

于是所求的特解为

$$
\begin{array}{l} y = x + \frac {x ^ {4}}{4 \times 3} + \frac {x ^ {7}}{7 \times 6 \times 4 \times 3} + \frac {x ^ {1 0}}{1 0 \times 9 \times 7 \times 6 \times 4 \times 3} + \dots + \\ \frac {x ^ {3 m + 1}}{(3 m + 1) \times (3 m) \times \cdots \times 1 0 \times 9 \times 7 \times 6 \times 4 \times 3} + \dots . \\ \end{array}
$$

# 三、欧拉公式

设有复数项级数为

$$
\left(u _ {1} + v _ {1} \mathrm{i}\right) + \left(u _ {2} + v _ {2} \mathrm{i}\right) + \dots + \left(u _ {n} + v _ {n} \mathrm{i}\right) + \dots , \tag {5-8}
$$

其中 $u_{n}$ 与 $v_{n}$ ( $n=1,2,3,\cdots$ ) 为实常数或实函数. 如果实部所成的级数

$$
u _ {1} + u _ {2} + \dots + u _ {n} + \dots \tag {5-9}
$$

收敛于和 u, 并且虚部所成的级数

$$
v _ {1} + v _ {2} + \dots + v _ {n} + \dots \tag {5-10}
$$

收敛于和 v, 那么就说级数(5-8)收敛且其和为 $u + vi$ .

如果级数(5-8)各项的模所构成的级数

$$
\sqrt {u _ {1} ^ {2} + v _ {1} ^ {2}} + \sqrt {u _ {2} ^ {2} + v _ {2} ^ {2}} + \dots + \sqrt {u _ {n} ^ {2} + v _ {n} ^ {2}} + \dots
$$

收敛,那么称级数(5-8)绝对收敛.如果级数(5-8)绝对收敛,由于

$$
\mid u _ {n} \mid \leqslant \sqrt {u _ {n} ^ {2} + v _ {n} ^ {2}}, \mid v _ {n} \mid \leqslant \sqrt {u _ {n} ^ {2} + v _ {n} ^ {2}} (n = 1, 2, 3, \dots),
$$

那么级数(5-9)与(5-10)绝对收敛,从而级数(5-8)收敛.

考察复数项级数

$$
1 + z + \frac {1}{2 !} z ^ {2} + \dots + \frac {1}{n !} z ^ {n} + \dots \quad (z = x + y i). \tag {5-11}
$$

可以证明级数(5-11)在整个复平面上是绝对收敛的.在 $x$ 轴上 $(z = x)$ 它表示指数函数 $\mathbf{e}^{\mathbf{x}}$ ，在整个复平面上我们用它来定义复变量指数函数，记作 $\mathbf{e}^{\mathbf{z}}$ .于是 $\mathbf{e}^{\mathbf{z}}$ 定义为

$$
e ^ {z} = 1 + z + \frac {1}{2 !} z ^ {2} + \dots + \frac {1}{n !} z ^ {n} + \dots \quad (| z | <   \infty). \tag {5-12}
$$

当 $x = 0$ 时， $z$ 为纯虚数 $y\mathrm{i}, (5 - 12)$ 式成为

$$
\begin{array}{l} \mathrm{e} ^ {y \mathrm{i}} = 1 + y \mathrm{i} + \frac {1}{2 !} (y \mathrm{i}) ^ {2} + \frac {1}{3 !} (y \mathrm{i}) ^ {3} + \dots + \frac {1}{n !} (y \mathrm{i}) ^ {n} + \dots \\ = 1 + y \mathrm{i} - \frac {1}{2 !} y ^ {2} - \frac {1}{3 !} y ^ {3} \mathrm{i} + \frac {1}{4 !} y ^ {4} + \frac {1}{5 !} y ^ {5} \mathrm{i} - \dots \\ = \left(1 - \frac {1}{2 !} y ^ {2} + \frac {1}{4 !} y ^ {4} - \dots\right) + \left(y - \frac {1}{3 !} y ^ {3} + \frac {1}{5 !} y ^ {5} - \dots\right) i \\ = \cos y + \text { i   s   i   n } y. \\ \end{array}
$$

把 $y$ 换写为 $x$ , 上式变为

$$
\mathrm{e} ^ {x \mathrm{i}} = \cos x + \mathrm{i} \sin x, \tag {5-13}
$$

这就是欧拉(Euler)公式.

应用公式(5-13)，复数 $z$ 可以表示为指数形式：

$$
z = \rho (\cos \theta + \mathrm{i} \sin \theta) = \rho \mathrm{e} ^ {\mathrm{i} \theta}, \tag {5-14}
$$

其中 $\rho = |z|$ 是 z 的模, $\theta = \arg z$ 是 z 的辐角(图 12-5).

在(5-13)式中把 $x$ 换成 $-x$ ，又有

$$
\mathrm{e} ^ {- x \mathrm{i}} = \cos x - \mathrm{i} \sin x.
$$

把上式与(5-13)相加或相减,得

$$
\left\{ \begin{array}{l} \cos x = \frac {\mathrm{e} ^ {x \mathrm{i}} + \mathrm{e} ^ {- x \mathrm{i}}}{2}, \\ \sin x = \frac {\mathrm{e} ^ {x \mathrm{i}} - \mathrm{e} ^ {- x \mathrm{i}}}{2 \mathrm{i}}. \end{array} \right. \tag {5-15}
$$

这两个式子也叫做欧拉公式.(5-13)式或(5-15)式揭示了三角函数与复变量指数函数之间的一种联系.

最后,根据定义式(5-12),并利用幂级数的乘法,我们不难验证

$$
\mathrm{e} ^ {z _ {1} + z _ {2}} = \mathrm{e} ^ {z _ {1}} \cdot \mathrm{e} ^ {z _ {2}}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/58cd4a465b62599b26ea804db4443116d0c1a7350e02031d2d04cb4353e53cb2.jpg)



图12-5


特殊地, 取 $z_{1}$ 为实数 $x, z_{2}$ 为纯虚数 yi, 则有

$$
\mathrm{e} ^ {x + y \mathrm{i}} = \mathrm{e} ^ {x} \cdot \mathrm{e} ^ {y \mathrm{i}} = \mathrm{e} ^ {x} (\cos y + \mathrm{i} \sin y).
$$

这就是说,复变量指数函数 $e^{z}$ 在 $z=x+yi$ 处的值是模为 $e^{x}$ 、辐角为 y 的复数.

# 习题12-5

1. 利用函数的幂级数展开式求下列各数的近似值：

(1) $\ln 3$ (误差不超过 0.000 1);

(2) $\sqrt{\mathrm{e}}$ （误差不超过0.001）；

(3) $\sqrt[9]{522}$ （误差不超过 0.000 01）;

(4) $\cos 2^{\circ}$ (误差不超过 0.0001).

2. 利用被积函数的幂级数展开式求下列定积分的近似值：

(1) $\int_{0}^{0.5}\frac{1}{1+x^{4}}dx$ （误差不超过0.0001）；

(2) $\int_{0}^{0.5}\frac{\arctan x}{x}dx$ （误差不超过0.001）.

3. 试用幂级数求下列各微分方程的解：

(1) $y' - xy - x = 1$ ; 

(2) $y'' + xy' + y = 0$ ; 

(3) $(1-x)y'=x^{2}-y.$ 

4. 试用幂级数求下列方程满足所给初值条件的特解：

(1) $y' = y^2 + x^3, y \big|_{x=0} = \frac{1}{2};$ 

(2) $(1-x)y'+y=1+x,y\big|_{x=0}=0.$ 

5. 验证函数 $y(x)=1+\frac{x^{3}}{3!}+\frac{x^{6}}{6!}+\cdots+\frac{x^{3n}}{(3n)!}+\cdots$ ( $-\infty<x<+\infty$ ) 满足微分方程 $y''+y'+y=e^{x}$ ，并利用此结果求幂级数 $\sum_{n=0}^{\infty}\frac{x^{3n}}{(3n)!}$ 的和函数.

6. 利用欧拉公式将函数 $e^{x}\cos x$ 展开成 x 的幂级数.

# * 第六节 函数项级数的一致收敛性及一致收敛级数的基本性质

# 一、函数项级数的一致收敛性

我们知道,有限个连续函数的和仍然是连续函数,有限个函数的和的导数及积分也分别等于它们的导数及积分的和.但是对于无穷多个函数的和是否也具有这些性质呢?换句话说,无穷多个连续函数的和 $s(x)$ 是否仍然是连续函数?无穷多个函数的导数及积分的和是否仍然分别等于它们的和函数的导数及积分呢?我们曾经指出,对于幂级数来说,回答是肯定的.但是,对于一般的函数项级数是否都是如此呢?下面来看一个例子.

例 1 函数项级数

$$
x + \left(x ^ {2} - x\right) + \left(x ^ {3} - x ^ {2}\right) + \dots + \left(x ^ {n} - x ^ {n - 1}\right) + \dots
$$

的每一项都在[0,1]上连续，其前 $n$ 项之和为 $s_n(x) = x^n$ ，因此和函数为

$$
s (x) = \lim _ {n \to \infty} s _ {n} (x) = \left\{ \begin{array}{l l} 0, & 0 \leqslant x <   1, \\ 1, & x = 1. \end{array} \right.
$$

这和函数 $s(x)$ 在 $x = 1$ 处间断.由此可见，函数项级数的每一项在 $[a,b]$ 上连续，并且级数在 $[a,b]$ 上收敛，其和函数不一定在 $[a,b]$ 上连续.也可以举出这样的例子，函数项级数的每一项的导数及积分所成的级数的和并不等于它们的和函数的导数及积分.这就提出了这样一个问题：对什么级数，能够从级数每一项的连续性得出它的和函数的连续性，从级数的每一项的导数及积分所成的级数之和得出原来级数的和函数的导数及积分呢？要回答这个问题，就需要引入下面的函数项级数的一致收敛性概念.

设函数项级数

$$
u _ {1} (x) + u _ {2} (x) + \dots + u _ {n} (x) + \dots
$$

在区间 $I$ 上收敛于和 $s(x)$ . 也就是对于区间 $I$ 上的每一个值 $x_0$ , 数项级数 $\sum_{n=1}^{\infty} u_n(x_0)$ 收敛于 $s(x_0)$ , 即级数的部分和所成的数列

$$
s _ {n} (x _ {0}) = \sum_ {i = 1} ^ {n} u _ {i} (x _ {0}) \rightarrow s (x _ {0}) \quad (n \rightarrow \infty).
$$

按数列极限的定义,对于任意给定的正数 $\varepsilon$ 以及区间 I 上的每一个值 $x_{0}$ , 都存在着一个正整数 N, 使得当 n > N 时, 有不等式

$$
\mid s (x _ {0}) - s _ {n} (x _ {0}) \mid <   \varepsilon ,
$$

即

$$
\mid r _ {n} (x _ {0}) \mid = \left| \sum_ {i = n + 1} ^ {\infty} u _ {i} (x _ {0}) \right| <   \varepsilon .
$$

这个数 $N$ 一般说来不仅依赖于 $\varepsilon$ , 而且也依赖于 $x_0$ , 我们记它为 $N(x_0, \varepsilon)$ . 如果对于某一函数项级数能够找到这样一个正整数 $N$ , 它只依赖于 $\varepsilon$ 而不依赖于 $x_0$ , 也就是对区间 $I$ 上的每一个值 $x_0$ 都能适用的 $N(\varepsilon)$ , 对这类级数我们给一个特殊的名称以区别于一般的收敛级数, 这就是下面的一致收敛的定义.

定义 设有函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ . 如果对于任意给定的正数 $\varepsilon$ , 都存在着一个只依赖于 $\varepsilon$ 的正整数 $N$ , 使得当 $n > N$ 时, 对区间 $I$ 上的一切 $x$ , 都有不等式

$$
\mid r _ {n} (x) \mid = \mid s (x) - s _ {n} (x) \mid <   \varepsilon
$$

成立,那么称函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ 在区间 $I$ 上一致收敛于和 $s(x)$ ,也称函数序列

$\{s_{n}(x)\}$ 在区间 I 上一致收敛于 $s(x)$ .

以上函数项级数一致收敛的定义在几何上可解释为: 只要 n 充分大 $(n > N)$ ，在区间 I 上的所有曲线 $y = s_{n}(x)$ 将位于曲线

$$
y = s (x) + \varepsilon \quad \text {与} \quad y = s (x) - \varepsilon
$$

之间(图 12-6).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/63e0cbd2fc34ca2eb486f2c4346400027402f5884c24c8fa3ef78e28ea0d9a08.jpg)



图12-6


例2 研究级数

$$
\frac {1}{x + 1} + \left(\frac {1}{x + 2} - \frac {1}{x + 1}\right) + \dots + \left(\frac {1}{x + n} - \frac {1}{x + n - 1}\right) + \dots
$$

在区间 $[0, +\infty)$ 上的一致收敛性.

解 级数的前 $n$ 项和 $s_n(x) = \frac{1}{x + n}$ , 因此级数的和

$$
s (x) = \lim _ {n \to \infty} s _ {n} (x) = \lim _ {n \to \infty} \frac {1}{x + n} = 0 \quad (0 \leqslant x <   + \infty).
$$

于是,余项的绝对值

$$
\mid r _ {n} (x) \mid = \mid s (x) - s _ {n} (x) \mid = \frac {1}{x + n} \leqslant \frac {1}{n} \quad (0 \leqslant x <   + \infty).
$$

对于任给 $\varepsilon > 0$ ，取正整数 $N \geqslant \frac{1}{\varepsilon}$ ，则当 $n > N$ 时，对于区间 $[0, +\infty)$ 上的一切 $x$ ，有

$$
\left| r _ {n} (x) \right| <   \varepsilon .
$$

根据定义,所给级数在区间 $[0,+\infty)$ 上一致收敛于 $s(x)\equiv0$ .

例3 研究例1中的级数

$$
x + \left(x ^ {2} - x\right) + \dots + \left(x ^ {n} - x ^ {n - 1}\right) + \dots
$$

在区间(0,1)内的一致收敛性.

解 这级数在区间(0,1)内处处收敛于和 $s(x) \equiv 0$ ，但并不一致收敛。事实上，这个级数的部分和 $s_n(x) = x^n$ ，对于任意一个正整数 $n$ ，取 $x_n = \frac{1}{\sqrt[n]{2}}$ ，于是

$$
s _ {n} (x _ {n}) = x _ {n} ^ {n} = \frac {1}{2},
$$

但 $s(x_{n}) = 0$ ，从而

$$
\mid r _ {n} (x _ {n}) \mid = \mid s (x _ {n}) - s _ {n} (x _ {n}) \mid = \frac {1}{2}.
$$

所以, 只要取 $\varepsilon < \frac{1}{2}$ , 不论 $n$ 多么大, 在 $(0,1)$ 内总存在这样的点 $x_{n}$ , 使得 $|r_{n}(x_{n})| > \varepsilon$ , 因此所给级数在 $(0,1)$ 内不一致收敛. 这表明虽然函数序列 $s_{n}(x) = x^{n}$ 在 $(0,1)$ 内处处收敛于 $s(x) \equiv 0$ ，但 $s_n(x)$ 在 $(0,1)$ 内各点处收敛于零的“快慢”程度是不一致的，从图12-7中我们也可以看出这一情形.

可是对于任意正数 $r < 1$ ，这级数在 $[0, r]$ 上一致收敛。这是因为当 $x = 0$ 时，显然

$$
\mid r _ {n} (x) \mid = x ^ {n} <   \varepsilon ;
$$

当 $0 < x \leqslant r$ 时，要使 $x^n < \varepsilon$ （不妨设 $\varepsilon < 1$ ），只要 $n \ln x < \ln \varepsilon$ 或 $n > \frac{\ln \varepsilon}{\ln x}$ ，而 $\frac{\ln \varepsilon}{\ln x}$ 在 $(0, r]$ 上的最大值为$\frac{\ln \varepsilon}{\ln r}$ , 故取正整数 $N \geqslant \frac{\ln \varepsilon}{\ln r}$ , 则当 $n > N$ 时, 对 $[0, r]$ 上的一切 $x$ 都有 $x^n < \varepsilon$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/c1b361a9b39f5c343d98e6c0b7f61ac98e54197e03baf7f121ab8b7d310a3827.jpg)



图12-7


上述例子也说明了一致收敛性与所讨论的区间有关.以上两例都是直接根据定义来判定级数的一致收敛性的,现在介绍一个在实用上较方便的判别法.

定理(魏尔斯特拉斯(Weierstrass)判别法) 如果函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ 在区间 $I$ 上满足条件:

(1) $\left|u_{n}(x)\right|\leqslant a_{n}\quad(n=1,2,3,\cdots);$ 

(2) 正项级数 $\sum_{n=1}^{\infty}a_{n}$ 收敛,

那么函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ 在区间 $I$ 上一致收敛.

证 由条件(2)，对任意给定的 $\varepsilon > 0$ ，根据柯西审敛原理（第一节第三目）存在正整数 $N$ ，使得当 $n > N$ 时，对任意的正整数 $p$ ，都有

$$
a _ {n + 1} + a _ {n + 2} + \dots + a _ {n + p} <   \frac {\varepsilon}{2}.
$$

由条件(1)，对任何 $x\in I$ ，都有

$$
\left| u _ {n + 1} (x) + u _ {n + 2} (x) + \dots + u _ {n + p} (x) \right| \leqslant \left| u _ {n + 1} (x) \right| + \left| u _ {n + 2} (x) \right| + \dots + \left| u _ {n + p} (x) \right|
$$

$$
\leqslant a _ {n + 1} + a _ {n + 2} + \dots + a _ {n + p} <   \frac {\varepsilon}{2},
$$

令 $p \to \infty$ ，则由上式得

$$
\mid r _ {n} (x) \mid \leqslant \frac {\varepsilon}{2} <   \varepsilon .
$$

因此函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ 在区间 $I$ 上一致收敛.

例4 证明级数

$$
\frac {\sin x}{1 ^ {2}} + \frac {\sin 2 ^ {2} x}{2 ^ {2}} + \dots + \frac {\sin n ^ {2} x}{n ^ {2}} + \dots
$$

在 $(-∞,+∞)$ 内一致收敛.

证 因为在 $(-\infty, +\infty)$ 内

$$
\left| \frac {\sin n ^ {2} x}{n ^ {2}} \right| \leqslant \frac {1}{n ^ {2}} (n = 1, 2, 3, \dots),
$$

而 $\sum_{n=1}^{\infty} \frac{1}{n^2}$ 收敛, 故由魏尔斯特拉斯判别法, 所给级数在 $(- \infty, +\infty)$ 内一致收敛.

# 二、一致收敛级数的基本性质

一致收敛级数有如下基本性质：

定理1 如果级数 $\sum_{n=1}^{\infty} u_n(x)$ 的各项 $u_n(x)$ 在区间 $[a, b]$ 上都连续，且 $\sum_{n=1}^{\infty} u_n(x)$ 在区间 $[a, b]$ 上一致收敛于 $s(x)$ ，那么 $s(x)$ 在 $[a, b]$ 上也连续.

证 设 $x_0, x$ 为 $[a, b]$ 上任意两点. 由等式

$$
s (x) = s _ {n} (x) + r _ {n} (x), \quad s (x _ {0}) = s _ {n} (x _ {0}) + r _ {n} (x _ {0})
$$

得

$$
\begin{array}{l} \left| s (x) - s \left(x _ {0}\right) \right| = \left| s _ {n} (x) - s _ {n} \left(x _ {0}\right) + r _ {n} (x) - r _ {n} \left(x _ {0}\right) \right| \\ \leqslant \left| s _ {n} (x) - s _ {n} \left(x _ {0}\right) \right| + \left| r _ {n} (x) \right| + \left| r _ {n} \left(x _ {0}\right) \right|. \tag {6-1} \\ \end{array}
$$

因为级数 $\sum_{n=1}^{\infty} u_n(x)$ 一致收敛于 $s(x)$ , 所以对任意给定的正数 $\varepsilon$ , 必有正整数 $N = N(\varepsilon)$ , 使得当 $n > N$ 时, 对 $[a, b]$ 上的一切 $x$ , 都有

$$
\left| r _ {n} (x) \right| <   \frac {\varepsilon}{3}. \tag {6-2}
$$

当然,也有 $\left|r_{n}(x_{0})\right|<\frac{\varepsilon}{3}$ .选定满足大于N的n之后, $s_{n}(x)$ 是有限项连续函数之和,故 $s_{n}(x)$ 在点 $x_{0}$ 连续,从而必有一个 $\delta>0$ 存在,当 $\left|x-x_{0}\right|<\delta$ 时,总有

$$
\mid s _ {n} (x) - s _ {n} \left(x _ {0}\right) \mid <   \frac {\varepsilon}{3}. \tag {6-3}
$$

由(6-1)、(6-2)、(6-3)式可见，对任给 $\varepsilon > 0$ ，必有 $\delta > 0$ ，当 $|x - x_0| < \delta$ 时，有

$$
\mid s (x) - s \left(x _ {0}\right) \mid <   \varepsilon .
$$

所以 $s(x)$ 在点 $x_{0}$ 处连续，而 $x_{0}$ 在 $[a,b]$ 上是任意的，因此 $s(x)$ 在 $[a,b]$ 上连续.

定理2 如果级数 $\sum_{n=1}^{\infty} u_n(x)$ 的各项 $u_n(x)$ 在区间 $[a, b]$ 上连续，且 $\sum_{n=1}^{\infty} u_n(x)$ 在 $[a, b]$ 上一致收敛于 $s(x)$ ，那么级数 $\sum_{n=1}^{\infty} u_n(x)$ 在 $[a, b]$ 上可以逐项积分，即

$$
\int_ {x _ {0}} ^ {x} s (x) \mathrm{d} x = \int_ {x _ {0}} ^ {x} u _ {1} (x) \mathrm{d} x + \int_ {x _ {0}} ^ {x} u _ {2} (x) \mathrm{d} x + \dots + \int_ {x _ {0}} ^ {x} u _ {n} (x) \mathrm{d} x + \dots , \tag {6-4}
$$

其中 $a \leqslant x_0 < x \leqslant b$ ，并且上式右端的级数在 $[a, b]$ 上也一致收敛。

证 因为级数 $\sum_{n=1}^{\infty} u_n(x)$ 在 $[a, b]$ 上一致收敛，由定理 $1, s(x), r_n(x)$ 都在 $[a, b]$ 上连续，所以积分 $\int_{x_0}^{x} s(x) \mathrm{d}x, \int_{x_0}^{x} r_n(x) \mathrm{d}x$ 存在，从而有

$$
\left| \int_ {x _ {0}} ^ {x} s (x) \mathrm{d} x - \int_ {x _ {0}} ^ {x} s _ {n} (x) \mathrm{d} x \right| = \left| \int_ {x _ {0}} ^ {x} r _ {n} (x) \mathrm{d} x \right| \leqslant \int_ {x _ {0}} ^ {x} | r _ {n} (x) | \mathrm{d} x.
$$

又由级数的一致收敛性,对任给正数 $\varepsilon$ , 必有 $N=N(\varepsilon)$ , 使得当 n>N 时, 对 $[a,b]$ 上的一切 x, 都有

$$
\mid r _ {n} (x) \mid <   \frac {\varepsilon}{b - a}.
$$

于是, 当 n > N 时有

$$
\left| \int_ {x _ {0}} ^ {x} s (x) \mathrm{d} x - \int_ {x _ {0}} ^ {x} s _ {n} (x) \mathrm{d} x \right| \leqslant \int_ {x _ {0}} ^ {x} | r _ {n} (x) | \mathrm{d} x <   \frac {\varepsilon}{b - a} (x - x _ {0}) \leqslant \varepsilon .
$$

根据极限的定义,有

$$
\int_ {x _ {0}} ^ {x} s (x) \mathrm{d} x = \lim _ {n \rightarrow \infty} \int_ {x _ {0}} ^ {x} s _ {n} (x) \mathrm{d} x = \lim _ {n \rightarrow \infty} \sum_ {i = 1} ^ {n} \int_ {x _ {0}} ^ {x} u _ {i} (x) \mathrm{d} x,
$$

即

$$
\int_ {x _ {0}} ^ {x} s (x) \mathrm{d} x = \sum_ {i = 1} ^ {\infty} \int_ {x _ {0}} ^ {x} u _ {i} (x) \mathrm{d} x.
$$

由于 $N$ 只依赖于 $\varepsilon$ 而与 $x_0, x$ 无关，所以级数 $\sum_{i=1}^{\infty} \int_{x_0}^{x} u_i(x) \mathrm{d}x$ 在 $[a, b]$ 上一致收敛.

定理3 如果级数 $\sum_{n=1}^{\infty} u_n(x)$ 在区间 $[a, b]$ 上收敛于和 $s(x)$ , 它的各项 $u_n(x)$ 都具有连续导数 $u_n'(x)$ , 并且级数 $\sum_{n=1}^{\infty} u_n'(x)$ 在 $[a, b]$ 上一致收敛, 那么级数 $\sum_{n=1}^{\infty} u_n(x)$ 在 $[a, b]$ 上也一致收敛, 且可逐项求导, 即

$$
s ^ {\prime} (x) = u _ {1} ^ {\prime} (x) + u _ {2} ^ {\prime} (x) + \dots + u _ {n} ^ {\prime} (x) + \dots . \tag {6-5}
$$

证 先证等式(6-5). 由于 $\sum_{n=1}^{\infty} u_n'(x)$ 在 $[a, b]$ 上一致收敛, 设其和为 $\varphi(x)$ , 即 $\sum_{n=1}^{\infty} u_n'(x) = \varphi(x)$ , 欲证(6-5), 只需证 $\varphi(x) = s'(x)$ 就可以了.

根据定理1知, $\varphi(x)$ 在 $[a,b]$ 上连续,根据定理2,级数 $\sum_{n=1}^{\infty}u_{n}^{\prime}(x)$ 可逐项积分,故有

$$
\int_ {x _ {0}} ^ {x} \varphi (x) \mathrm{d} x = \sum_ {n = 1} ^ {\infty} \int_ {x _ {0}} ^ {x} u _ {n} ^ {\prime} (x) \mathrm{d} x = \sum_ {n = 1} ^ {\infty} [ u _ {n} (x) - u _ {n} (x _ {0}) ],
$$

而

$$
\sum_ {n = 1} ^ {\infty} u _ {n} (x) = s (x), \quad \sum_ {n = 1} ^ {\infty} u _ {n} (x _ {0}) = s (x _ {0}),
$$

故

$$
\sum_ {n = 1} ^ {\infty} \left[ u _ {n} (x) - u _ {n} (x _ {0}) \right] = s (x) - s (x _ {0}),
$$

从而有

$$
\int_ {x _ {0}} ^ {x} \varphi (x) \mathrm{d} x = s (x) - s (x _ {0}),
$$

其中 $a \leqslant x_0 < x \leqslant b$ . 上式两端求导, 即得关系式

$$
\varphi (x) = s ^ {\prime} (x).
$$

再证级数 $\sum_{n=1}^{\infty} u_n(x)$ 在 $[a, b]$ 上也一致收敛.

根据定理2,级数 $\sum_{n=1}^{\infty}\int_{x_0}^{x}u_n'(x)\mathrm{d}x$ 在 $[a,b]$ 上一致收敛，而

$$
\sum_ {n = 1} ^ {\infty} \int_ {x _ {0}} ^ {x} u _ {n} ^ {\prime} (x) \mathrm{d} x = \sum_ {n = 1} ^ {\infty} u _ {n} (x) - \sum_ {n = 1} ^ {\infty} u _ {n} (x _ {0}),
$$

所以

$$
\sum_ {n = 1} ^ {\infty} u _ {n} (x) = \sum_ {n = 1} ^ {\infty} \int_ {x _ {0}} ^ {x} u _ {n} ^ {\prime} (x) \mathrm{d} x + \sum_ {n = 1} ^ {\infty} u _ {n} (x _ {0}),
$$

由此即得所要证的结论.

必须注意,级数一致收敛并不能保证可以逐项求导.例如,在例4中我们已证明了级数

$$
\frac {\sin x}{1 ^ {2}} + \frac {\sin 2 ^ {2} x}{2 ^ {2}} + \dots + \frac {\sin n ^ {2} x}{n ^ {2}} + \dots
$$

在任何区间 $[a, b]$ 上都是一致收敛的，但逐项求导后的级数

$$
\cos x + \cos 2 ^ {2} x + \dots + \cos n ^ {2} x + \dots ,
$$

其一般项不趋于零,所以对任意值 x 都是发散的,因此原级数不可以逐项求导.

下面我们来讨论幂级数的一致收敛性.

定理4 如果幂级数 $\sum_{n=0}^{\infty} a_n x^n$ 的收敛半径为 $R > 0$ , 那么此级数在 $(-R, R)$ 内的任一闭区间 $[a, b]$ 上一致收敛.

证 记 $r = \max \{|a|, |b|\}$ ，则对 $[a, b]$ 上的一切 $x$ ，都有

$$
\mid a _ {n} x ^ {n} \mid \leqslant \mid a _ {n} r ^ {n} \mid \quad (n = 0, 1, 2, \dots),
$$

而 0<r<R, 根据第三节定理 1 级数 $\sum_{n=0}^{\infty}a_{n}r^{n}$ 绝对收敛, 由魏尔斯特拉斯判别法即得所要证的结论.

进一步还可证明,如果幂级数 $\sum_{n=0}^{\infty}a_{n}x^{n}$ 在收敛区间的端点收敛,那么一致收敛的区间可扩大到包含端点.

下面我们来证明在第三节中指出的关于幂级数在其收敛区间内的和函数的连续性、逐项可导、逐项可积的结论.

关于和函数的连续性及逐项可积的结论,由定理4和定理1、定理2立即可得.关于逐项可导的结论,我们重新叙述成如下定理并给出证明.

定理5 如果幂级数 $\sum_{n=0}^{\infty} a_n x^n$ 的收敛半径为 $R > 0$ , 那么其和函数 $s(x)$ 在 $(-R, R)$ 内可导, 且有逐项求导公式

$$
s ^ {\prime} (x) = \left(\sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1},
$$

逐项求导后所得到的幂级数与原级数有相同的收敛半径.

证 先证级数 $\sum_{n=1}^{\infty} na_n x^{n-1}$ 在 $(-R, R)$ 内收敛.

在 $(-R, R)$ 内任意取定 $x$ , 再选定 $x_{1}$ , 使得 $|x| < x_{1} < R$ . 记 $q = \frac{|x|}{x_{1}} < 1$ , 则

$$
\left| n a _ {n} x ^ {n - 1} \right| = n \left| \frac {x}{x _ {1}} \right| ^ {n - 1} \cdot \frac {1}{x _ {1}} \left| a _ {n} x _ {1} ^ {n} \right| = n q ^ {n - 1} \cdot \frac {1}{x _ {1}} \left| a _ {n} x _ {1} ^ {n} \right|,
$$

由比值审敛法可知级数 $\sum_{n=1}^{\infty} nq^{n-1}$ 收敛, 于是

$$
n q ^ {n - 1} \rightarrow 0 \quad (n \rightarrow \infty),
$$

故数列 $\{nq^{n - 1}\}$ 有界，必有 $M > 0$ ，使得

$$
n q ^ {n - 1} \cdot \frac {1}{x _ {1}} \leqslant M (n = 1, 2, \dots).
$$

又 $0 < x_{1} < R$ ，级数 $\sum_{n=1}^{\infty}|a_nx_1^n|$ 收敛，由比较审敛法的推论即得级数 $\sum_{n=1}^{\infty}na_nx^{n-1}$ 收敛.

由定理4,级数 $\sum_{n=1}^{\infty} na_n x^{n-1}$ 在 $(-R, R)$ 内的任一闭区间 $[a, b]$ 上一致收敛,故幂级数 $\sum_{n=1}^{\infty} a_n x^n$ 在 $[a, b]$ 上符合定理3的条件,从而可逐项求导.再由 $[a, b]$ 在 $(-R, R)$ 内的任意性,即得幂级数 $\sum_{n=1}^{\infty} a_n x^n$ 在 $(-R, R)$ 内可逐项求导.

设幂级数 $\sum_{n=1}^{\infty} na_n x^{n-1}$ 的收敛半径为 $R'$ ，上面已证得 $R \leqslant R'$ . 将此幂级数在 $[0, x]$ ( $|x| < R'$ ) 上逐项积分即得 $\sum_{n=1}^{\infty} a_n x^n$ ，因逐项积分所得级数的收敛半径不会缩小，所以

$R'\leqslant R$ , 于是 $R'=R$ . 定理 5 证毕.

# *习题12-6

1. 已知函数序列 $s_{n}(x)=\sin\frac{x}{n}\quad(n=1,2,3,\cdots)$ 在 $(-∞,+∞)$ 上收敛于 0，

(1) 问 $N(\varepsilon, x)$ 取多大, 能使当 $n > N$ 时, $s_n(x)$ 与其极限之差的绝对值小于正数 $\varepsilon$ ;

(2) 证明 $s_n(x)$ 在任一有限区间 $[a, b]$ 上一致收敛.

2. 已知级数 $x^{2}+\frac{x^{2}}{1+x^{2}}+\frac{x^{2}}{(1+x^{2})^{2}}+\cdots$ 在 $(-∞,+∞)$ 上收敛.

(1) 求出该级数的和;

(2) 问 $N(\varepsilon, x)$ 取多大, 能使当 n > N 时, 级数的余项 $r_{n}$ 的绝对值小于正数 $\varepsilon$ ;

(3) 分别讨论级数在区间 $[0,1]$ , $\left[\frac{1}{2},1\right]$ 上的一致收敛性.

3. 按定义讨论下列级数在所给区间上的一致收敛性：

(1) $\sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^2}{(1 + x^2)^n}, (-\infty, +\infty)$ ; 

(2) $\sum_{n=0}^{\infty}(1-x)x^{n}, (0,1)$ . 

4. 利用魏尔斯特拉斯判别法证明下列级数在所给区间上的一致收敛性：

(1) $\sum_{n=1}^{\infty} \frac{\cos nx}{2^n}, (-\infty, +\infty)$ ; 

(2) $\sum_{n=1}^{\infty} \frac{\sin nx}{\sqrt[3]{n^4 + x^4}}, (-\infty, +\infty)$ ; 

(3) $\sum_{n=1}^{\infty} x^{2} e^{-nx}, [0, +\infty)$ ; 

(4) $\sum_{n=1}^{\infty} \frac{e^{-nx}}{n!}, (-10, 10)$ ; 

(5) $\sum_{n=1}^{\infty} \frac{(-1)^n (1 - e^{-nx})}{n^2 + x^2}, [0, +\infty)$ . 

# 第七节 傅里叶级数

从本节开始,我们讨论由三角函数组成的函数项级数,即所谓三角级数,着重研究如何把函数展开成三角级数.

# 一、三角级数 三角函数系的正交性

在第一章中,我们介绍过周期函数的概念,周期函数反映了客观世界中的周期运动.

正弦函数是一种常见而简单的周期函数.例如描述简谐振动的函数

$$
y = A \sin (\omega t + \varphi)
$$

就是一个以 $\frac{2\pi}{\omega}$ 为周期的正弦函数,其中y表示动点的位置,t表示时间,A为振幅, $\omega$ 为角频率, $\varphi$ 为初相.

在实际问题中,除了正弦函数外,还会遇到非正弦函数的周期函数,它们反映了较

复杂的周期运动. 如电子技术中常用的周期为 T 的矩形波(图 12-8), 就是一个非正弦周期函数的例子.

如何深入研究非正弦周期函数呢？联系到前面介绍过的用函数的幂级数展开式表示与讨论函数，我们也

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/836478312c5a75dc53c0edac9020a676deeb338cb58a3ffb9fee3c93b0fc28d3.jpg)



图12-8


想将周期函数展开成由简单的周期函数例如三角函数组成的级数.具体地说,将周期为 $T\left(T=\frac{2\pi}{\omega}\right)$ 的周期函数用一系列以 T 为周期的正弦函数 $A_{n}\sin(n\omega t+\varphi_{n})$ 组成的级数来表示,记为

$$
f (t) = A _ {0} + \sum_ {n = 1} ^ {\infty} A _ {n} \sin \left(n \omega t + \varphi_ {n}\right), \tag {7-1}
$$

其中 $A_{0}, A_{n}, \varphi_{n}$ ( $n=1,2,3,\cdots$ ) 都是常数.

将周期函数按上述方式展开,它的物理意义是很明确的,这就是把一个比较复杂的周期运动看成是许多不同频率的简谐振动的叠加.在电工学上,这种展开称为谐波分析,其中常数项 $A_{0}$ 称为 $f(t)$ 的直流分量, $A_{1}\sin(\omega t+\varphi_{1})$ 称为一次谐波(又叫做基波), $A_{2}\sin(2\omega t+\varphi_{2}),A_{3}\sin(3\omega t+\varphi_{3}),\cdots$ 依次称为二次谐波,三次谐波,等等.

为了以后讨论方便起见,我们将正弦函数 $A_{n}\sin(n\omega t+\varphi_{n})$ 按三角公式变形,得

$$
A _ {n} \sin (n \omega t + \varphi_ {n}) = A _ {n} \sin \varphi_ {n} \cos n \omega t + A _ {n} \cos \varphi_ {n} \sin n \omega t,
$$

并且令 $\frac{a_{0}}{2}=A_{0},a_{n}=A_{n}\sin\varphi_{n},b_{n}=A_{n}\cos\varphi_{n},\omega=\frac{\pi}{l}$ （即T=2l），则(7-1)式右端的级数就可以改写为

$$
\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi t}{l} + b _ {n} \sin \frac {n \pi t}{l}\right). \tag {7-2}
$$

形如(7-2)式的级数叫做三角级数,其中 $a_0, a_n, b_n (n=1,2,3,\cdots)$ 都是常数.

令 $\frac{\pi t}{l}=x,(7-2)$ 式成为

$$
\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right), \tag {7-3}
$$

这就把以 2l 为周期的三角级数转换成以 $2\pi$ 为周期的三角级数.

下面我们讨论以 $2 \pi$ 为周期的三角级数(7-3).

如同讨论幂级数时一样,我们必须讨论三角级数(7-3)的收敛问题,以及给定周期为 $2\pi$ 的周期函数如何把它展开成三角级数(7-3).为此,我们首先介绍三角函数系的正交性.

所谓三角函数系

$$
1, \cos x, \sin x, \cos 2 x, \sin 2 x, \dots , \cos n x, \sin n x, \dots \tag {7-4}
$$

在区间 $\left[-\pi,\pi\right]$ 上正交,就是指在三角函数系(7-4)中任何不同的两个函数的乘积在区间 $\left[-\pi,\pi\right]$ 上的积分等于零,即

$$
\int_ {- \pi} ^ {\pi} \cos n x d x = 0 \quad (n = 1, 2, 3, \dots),
$$

$$
\int_ {- \pi} ^ {\pi} \sin n x \mathrm{d} x = 0 \quad (n = 1, 2, 3, \dots),
$$

$$
\int_ {- \pi} ^ {\pi} \sin k x \cos n x d x = 0 (k, n = 1, 2, 3, \dots),
$$

$$
\int_ {- \pi} ^ {\pi} \cos k x \cos n x d x = 0 (k, n = 1, 2, 3, \dots , k \neq n),
$$

$$
\int_ {- \pi} ^ {\pi} \sin k x \sin n x d x = 0 (k, n = 1, 2, 3, \dots , k \neq n).
$$

以上等式,都可以通过计算定积分来验证,现将第四式验证如下:

利用三角函数中积化和差的公式

$$
\cos k x \cos n x = \frac {1}{2} [ \cos (k + n) x + \cos (k - n) x ],
$$

当 $k \neq n$ 时, 有

$$
\begin{array}{l} \int_ {- \pi} ^ {\pi} \cos k x \cos n x d x = \frac {1}{2} \int_ {- \pi} ^ {\pi} [ \cos (k + n) x + \cos (k - n) x ] d x \\ = \frac {1}{2} \left[ \frac {\sin (k + n) x}{k + n} + \frac {\sin (k - n) x}{k - n} \right] _ {- \pi} ^ {\pi} \\ = 0 \quad (k, n = 1, 2, 3, \dots , k \neq n). \\ \end{array}
$$

其余等式请读者自行验证.

在三角函数系(7-4)中,两个相同函数的乘积在区间 $\left[-\pi,\pi\right]$ 上的积分不等于零,即

$$
\int_ {- \pi} ^ {\pi} 1 ^ {2} \mathrm{d} x = 2 \pi , \quad \int_ {- \pi} ^ {\pi} \sin^ {2} n x \mathrm{d} x = \pi , \quad \int_ {- \pi} ^ {\pi} \cos^ {2} n x \mathrm{d} x = \pi (n = 1, 2, 3, \dots).
$$

# 二、函数展开成傅里叶级数

设 $f(x)$ 是周期为 $2\pi$ 的周期函数,且能展开成三角级数

$$
f (x) = \frac {a _ {0}}{2} + \sum_ {k = 1} ^ {\infty} \left(a _ {k} \cos k x + b _ {k} \sin k x\right). \tag {7-5}
$$

我们自然要问:系数 $a_{0},a_{1},b_{1},\cdots$ 与函数 $f(x)$ 之间存在着怎样的关系?换句话说,如何利用 $f(x)$ 把 $a_{0},a_{1},b_{1},\cdots$ 表达出来?为此,我们进一步假设(7-5)式右端的级数可以逐项积分.

先求 $a_0$ . 对(7-5)式从 $-\pi$ 到 $\pi$ 积分, 由于假设(7-5)式右端级数可逐项积分, 因此有

$$
\int_ {- \pi} ^ {\pi} f (x) \mathrm{d} x = \int_ {- \pi} ^ {\pi} \frac {a _ {0}}{2} \mathrm{d} x + \sum_ {k = 1} ^ {\infty} \left[ a _ {k} \int_ {- \pi} ^ {\pi} \cos k x \mathrm{d} x + b _ {k} \int_ {- \pi} ^ {\pi} \sin k x \mathrm{d} x \right].
$$

根据三角函数系(7-4)的正交性,等式右端除第一项外,其余各项均为零,所以

$$
\int_ {- \pi} ^ {\pi} f (x) \mathrm{d} x = \frac {a _ {0}}{2} \cdot 2 \pi ,
$$

于是得

$$
a _ {0} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \mathrm{d} x.
$$

其次求 $a_{n}$ . 用 $\cos nx$ 乘(7-5)式两端, 再从 $-\pi$ 到 $\pi$ 积分, 我们得到

$$
\int_ {- \pi} ^ {\pi} f (x) \cos n x \mathrm{d} x = \frac {a _ {0}}{2} \int_ {- \pi} ^ {\pi} \cos n x \mathrm{d} x + \sum_ {k = 1} ^ {\infty} \left[ a _ {k} \int_ {- \pi} ^ {\pi} \cos k x \cos n x \mathrm{d} x + b _ {k} \int_ {- \pi} ^ {\pi} \sin k x \cos n x \mathrm{d} x \right].
$$

根据三角函数系(7-4)的正交性,等式右端除 k=n 的一项外,其余各项均为零,所以

$$
\int_ {- \pi} ^ {\pi} f (x) \cos n x \mathrm{d} x = a _ {n} \int_ {- \pi} ^ {\pi} \cos^ {2} n x \mathrm{d} x = a _ {n} \pi ,
$$

于是得

$$
a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos n x \mathrm{d} x \quad (n = 1, 2, 3, \dots).
$$

类似地,用 $\sin nx$ 乘(7-5)式的两端,再从 $-\pi$ 到 $\pi$ 积分,可得

$$
b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \sin n x \mathrm{d} x \quad (n = 1, 2, 3, \dots).
$$

由于当 $n = 0$ 时， $a_{n}$ 的表达式正好给出 $a_0$ ，因此，已得结果可以合并写成

$$
\left. \begin{array}{l} a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos n x \mathrm{d} x \quad (n = 0, 1, 2, 3, \dots), \\ b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \sin n x \mathrm{d} x \quad (n = 1, 2, 3, \dots). \end{array} \right\} \tag {7-6}
$$

如果公式(7-6)中的积分都存在,这时它们定出的系数 $a_0, a_1, b_1, \cdots$ 叫做函数 $f(x)$ 的傅里叶(Fourier)系数,将这些系数代入(7-5)式右端,所得的三角级数

$$
\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos n x + b _ {n} \sin n x)
$$

叫做函数 $f(x)$ 的傅里叶级数.

一个定义在 $(-\infty, +\infty)$ 上周期为 $2\pi$ 的函数 $f(x)$ , 如果它在一个周期上可积, 那么一定可以作出 $f(x)$ 的傅里叶级数. 然而, 函数 $f(x)$ 的傅里叶级数是否一定收敛? 如果它收敛, 它是否一定收敛于函数 $f(x)$ ? 一般说来, 这两个问题的答案都不是肯定的. 那么, $f(x)$ 在怎样的条件下, 它的傅里叶级数不仅收敛, 而且收敛于 $f(x)$ ? 也就是说, $f(x)$ 满足什么条件可以展开成傅里叶级数? 这是我们面临的一个基本问题.

下面我们叙述一个收敛定理(不加证明),它给出关于上述问题的一个重要结论.

定理(收敛定理,狄利克雷(Dirichlet)充分条件) 设 $f(x)$ 是周期为 $2\pi$ 的周期函数,如果它满足

(1) 在一个周期内连续或只有有限个第一类间断点,

(2) 在一个周期内至多只有有限个极值点,

那么 $f(x)$ 的傅里叶级数收敛，并且

当 $x$ 是 $f(x)$ 的连续点时，级数收敛于 $f(x)$ ；

当 $x$ 是 $f(x)$ 的间断点时，级数收敛于 $\frac{1}{2} [f(x^{-}) + f(x^{+})]$ 

收敛定理告诉我们: 只要函数在 $\left[-\pi,\pi\right]$ 上至多有有限个第一类间断点, 并且不做无限次振动, 函数的傅里叶级数在连续点处就收敛于该点的函数值, 在间断点处收敛于该点左极限与右极限的算术平均值. 可见, 函数展开成傅里叶级数的条件比展开成幂级数的条件低得多. 记

$$
C = \left\{x \mid f (x) = \frac {1}{2} [ f (x ^ {-}) + f (x ^ {+}) ] \right\},
$$

在 $C$ 上就成立 $f(x)$ 的傅里叶级数展开式

$$
f (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right), \quad x \in C. \tag {7-7}
$$

例 1 设 $f(x)$ 是周期为 $2\pi$ 的周期函数, 它在 $[-π, π)$ 上的表达式为

$$
f (x) = \left\{ \begin{array}{l l} - 1, & - \pi \leqslant x <   0, \\ 1, & 0 \leqslant x <   \pi . \end{array} \right.
$$

将 $f(x)$ 展开成傅里叶级数,并作出级数的和函数的图形.

解 所给函数满足收敛定理的条件, 它在点 $x = k\pi$ ( $k = 0, \pm1, \pm2, \cdots$ ) 处不连续, 在其他点处连续, 从而由收敛定理知道 $f(x)$ 的傅里叶级数收敛, 并且当 $x = k\pi$ 时级数收敛于

$$
\frac {- 1 + 1}{2} = \frac {1 + (- 1)}{2} = 0,
$$

当 $x \neq k\pi$ 时级数收敛于 $f(x)$ .

计算傅里叶系数如下：

$$
\begin{array}{l} a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos n x \mathrm{d} x = \frac {1}{\pi} \int_ {- \pi} ^ {0} (- 1) \cos n x \mathrm{d} x + \frac {1}{\pi} \int_ {0} ^ {\pi} 1 \cdot \cos n x \mathrm{d} x \\ = 0 \quad (n = 0, 1, 2, \dots); \\ b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \sin n x \mathrm{d} x = \frac {1}{\pi} \int_ {- \pi} ^ {0} (- 1) \sin n x \mathrm{d} x + \frac {1}{\pi} \int_ {0} ^ {\pi} 1 \cdot \sin n x \mathrm{d} x \\ = \frac {1}{\pi} \left[ \frac {\cos n x}{n} \right] _ {- \pi} ^ {0} + \frac {1}{\pi} \left[ - \frac {\cos n x}{n} \right] _ {0} ^ {\pi} \\ = \frac {1}{n \pi} [ 1 - \cos n \pi - \cos n \pi + 1 ] = \frac {2}{n \pi} [ 1 - (- 1) ^ {n} ] \\ = \left\{ \begin{array}{l l} \frac {4}{n \pi}, & n = 1, 3, 5, \dots , \\ 0, & n = 2, 4, 6, \dots . \end{array} \right. \\ \end{array}
$$

将求得的系数代入(7-7)式,就得到 $f(x)$ 的傅里叶级数展开式为

$$
\begin{array}{l} f (x) = \frac {4}{\pi} \left[ \sin x + \frac {1}{3} \sin 3 x + \dots + \frac {1}{2 k - 1} \sin (2 k - 1) x + \dots \right] \\ = \frac {4}{\pi} \sum_ {k = 1} ^ {\infty} \frac {1}{2 k - 1} \sin (2 k - 1) x \quad (- \infty <   x <   + \infty ; x \neq 0, \pm \pi , \pm 2 \pi , \dots). \\ \end{array}
$$

级数的和函数的图形如图 12-9 所示：

如果把例 1 中的函数理解为矩形波的波形函数(周期 $T=2\pi$ , 振幅 E=1, 自变量 x 表示时间), 那么上面所得到的展开式表明: 矩形波是由一系列不同频率的正弦波叠加而成的, 这些正弦波的频率依次为基波频率的奇数倍.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/4f1878eaeec4f0e2e33e43a38156aea5ff81119fe058dff4c021b5db6d174fbc.jpg)



图12-9


例 2 设 $f(x)$ 是周期为 $2\pi$ 的周期函数, 它在 $[-π, π)$ 上的表达式为

$$
f (x) = \left\{ \begin{array}{l l} x, & - \pi \leqslant x <   0, \\ 0, & 0 \leqslant x <   \pi . \end{array} \right.
$$

将 $f(x)$ 展开成傅里叶级数,并作出级数的和函数的图形.

解 所给函数满足收敛定理的条件, 它在点 $x=(2k+1)\pi$ ( $k=0,\pm1,\pm2,\cdots$ ) 处不连续. 因此, $f(x)$ 的傅里叶级数在 $x=(2k+1)\pi$ 处收敛于

$$
\frac {f (\pi^ {-}) + f (- \pi^ {+})}{2} = \frac {0 - \pi}{2} = - \frac {\pi}{2}.
$$

在连续点 $x (x \neq (2k + 1)\pi)$ 处收敛于 $f(x)$ .

计算傅里叶系数如下：

# 

例题精讲

12-8 

$$
\begin{array}{l} a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos n x \mathrm{d} x = \frac {1}{\pi} \int_ {- \pi} ^ {0} x \cos n x \mathrm{d} x \\ = \frac {1}{\pi} \left[ \frac {x \sin n x}{n} + \frac {\cos n x}{n ^ {2}} \right] _ {- \pi} ^ {0} = \frac {1}{n ^ {2} \pi} (1 - \cos n \pi) \\ = \left\{ \begin{array}{l l} \frac {2}{n ^ {2} \pi}, & n = 1, 3, 5, \dots , \\ 0, & n = 2, 4, 6, \dots ; \end{array} \right. \\ a _ {0} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \mathrm{d} x = \frac {1}{\pi} \int_ {- \pi} ^ {0} x \mathrm{d} x = \frac {1}{\pi} \left[ \frac {x ^ {2}}{2} \right] _ {- \pi} ^ {0} = - \frac {\pi}{2}; \\ b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \sin n x \mathrm{d} x = \frac {1}{\pi} \int_ {- \pi} ^ {0} x \sin n x \mathrm{d} x \\ = \frac {1}{\pi} \left[ - \frac {x \cos n x}{n} + \frac {\sin n x}{n ^ {2}} \right] _ {- \pi} ^ {0} \\ = - \frac {\cos n \pi}{n} = \frac {(- 1) ^ {n + 1}}{n} (n = 1, 2, 3, \dots). \\ \end{array}
$$

将求得的系数代入(7-7)式,得到 $f(x)$ 的傅里叶级数展开式为

$$
f (x) = - \frac {\pi}{4} + \left(\frac {2}{\pi} \cos x + \sin x\right) - \frac {1}{2} \sin 2 x + \left(\frac {2}{3 ^ {2} \pi} \cos 3 x + \frac {1}{3} \sin 3 x\right) -
$$

$$
\frac {1}{4} \sin 4 x + \left(\frac {2}{5 ^ {2} \pi} \cos 5 x + \frac {1}{5} \sin 5 x\right) - \dots
$$

$$
= - \frac {\pi}{4} + \frac {2}{\pi} \sum_ {k = 1} ^ {\infty} \frac {1}{(2 k - 1) ^ {2}} \cos (2 k - 1) x + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} \sin n x
$$

$$
(- \infty <   x <   + \infty ; x \neq \pm \pi , \pm 3 \pi , \dots).
$$

级数的和函数的图形如图 12-10 所示：

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/ab0573f1bd2784cd98c0f940d3899c5c8c627b000136c6dfd2eb043003795537.jpg)



图12-10


应该注意,如果函数 $f(x)$ 只在 $[-π,π]$ 上有定义,并且满足收敛定理的条件,那么 $f(x)$ 也可以展开成傅里叶级数.事实上,我们可在 $[-π,π)$ 或 $(-π,π]$ 外补充函数 $f(x)$ 的定义,使它拓广成周期为 $2π$ 的周期函数 $F(x)$ .按这种方式拓广函数的定义域的过程称为周期延拓.再将 $F(x)$ 展开成傅里叶级数.最后限制x在 $(-π,π)$ 内,此时 $F(x)\equiv f(x)$ ,这样便得到 $f(x)$ 的傅里叶级数展开式.根据收敛定理,这级数在区间端点 $x=\pm\pi$ 处收敛于 $\frac{f(\pi^{-})+f(-\pi^{+})}{2}$ .

例 3 将函数

$$
u (t) = E \left| \sin {\frac {t}{2}} \right|, - \pi \leqslant t \leqslant \pi
$$

展开成傅里叶级数,其中 E 是正的常数.

解 所给函数在区间 $\left[-\pi,\pi\right]$ 上满足收敛定理的条件,并且拓广为周期函数时,它在每一点 x 处都连续(图 12-11)，因此拓广的周期函数的傅里叶级数在 $[-π, π]$ 上收敛于 $u(t)$ .

计算傅里叶系数如下：

$$
\begin{array}{l} a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} u (t) \cos n t d t \\ = \frac {E}{\pi} \int_ {- \pi} ^ {\pi} \left| \sin \frac {t}{2} \right| \cos n t d t, \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/4908fbe29dfa88e3fc0bb451e7ac341753e0f9b649457d8acfcef44c8e6d1316.jpg)



图12-11


因为上列积分中被积函数为偶函数,所以

$$
\begin{array}{l} a _ {n} = \frac {2 E}{\pi} \int_ {0} ^ {\pi} \sin \frac {t}{2} \cos n t \mathrm{d} t = \frac {E}{\pi} \int_ {0} ^ {\pi} \left[ \sin \left(n + \frac {1}{2}\right) t - \sin \left(n - \frac {1}{2}\right) t \right] \mathrm{d} t \\ = \frac {E}{\pi} \left[ - \frac {\cos \left(n + \frac {1}{2}\right) t}{n + \frac {1}{2}} + \frac {\cos \left(n - \frac {1}{2}\right) t}{n - \frac {1}{2}} \right] _ {0} ^ {\pi} \\ = \frac {E}{\pi} \left(\frac {1}{n + \frac {1}{2}} - \frac {1}{n - \frac {1}{2}}\right) = - \frac {4 E}{(4 n ^ {2} - 1) \pi} (n = 0, 1, 2, \dots). \\ b _ {n} = \frac {E}{\pi} \int_ {- \pi} ^ {\pi} \left| \sin \frac {t}{2} \right| \sin n t \mathrm{d} t = 0 (n = 1, 2, 3, \dots). \\ \end{array}
$$

上式等于零是因为被积函数是奇函数.

将求得的系数代入(7-7)式, 得 $u(t)$ 的傅里叶级数展开式为

$$
u (t) = \frac {4 E}{\pi} \left(\frac {1}{2} - \sum_ {n = 1} ^ {\infty} \frac {1}{4 n ^ {2} - 1} \cos n t\right) (- \pi \leqslant t \leqslant \pi).
$$

# 三、正弦级数和余弦级数

一般说来,一个函数的傅里叶级数既含有正弦项,又含有余弦项(见例2).但是,也有一些函数的傅里叶级数只含有正弦项(见例1)或者只含有常数项和余弦项(见例3).这是什么原因呢？实际上,这些情况是与所给函数 $f(x)$ 的奇偶性有密切关系的.对于周期为 $2\pi$ 的函数 $f(x)$ ，它的傅里叶系数计算公式为

$$
a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos n x d x \quad (n = 0, 1, 2, \dots),
$$

$$
b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \sin n x d x \quad (n = 1, 2, 3, \dots).
$$

由于奇函数在对称区间上的积分为零,偶函数在对称区间上的积分等于半区间上积分的2倍,因此,

当 $f(x)$ 为奇函数时， $f(x)\cos nx$ 是奇函数， $f(x)\sin nx$ 是偶函数，故

$$
\left. \begin{array}{l} a _ {n} = 0 \quad (n = 0, 1, 2, \dots), \\ b _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \sin n x \mathrm{d} x \quad (n = 1, 2, 3, \dots). \end{array} \right\} \tag {7-8}
$$

即知奇函数的傅里叶级数是只含有正弦项的正弦级数

$$
\sum_ {n = 1} ^ {\infty} b _ {n} \sin n x. \tag {7-9}
$$

当 $f(x)$ 为偶函数时， $f(x)\cos nx$ 是偶函数， $f(x)\sin nx$ 是奇函数，故

$$
\left. \begin{array}{l} a _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \cos n x \mathrm{d} x \quad (n = 0, 1, 2, \dots), \\ b _ {n} = 0 \quad (n = 1, 2, 3, \dots). \end{array} \right\} \tag {7-10}
$$

即知偶函数的傅里叶级数是只含常数项和余弦项的余弦级数

$$
\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} a _ {n} \cos n x. \tag {7-11}
$$

例4 设 $f(x)$ 是周期为 $2\pi$ 的周期函数, 它在 $[- \pi, \pi)$ 上的表达式为 $f(x) = x$ . 将 $f(x)$ 展开成傅里叶级数, 并作出级数的和函数的图形.

解 首先,所给函数满足收敛定理的条件,它在点

$$
x = (2 k + 1) \pi \quad (k = 0, \pm 1, \pm 2, \dots)
$$

处不连续,因此 $f(x)$ 的傅里叶级数在点 $x=(2k+1)\pi$ 处收敛于

$$
\frac {f (\pi^ {-}) + f (- \pi^ {+})}{2} = \frac {\pi + (- \pi)}{2} = 0,
$$

在连续点 $x$ ( $x \neq (2k + 1)\pi$ ) 处收敛于 $f(x)$ .

其次,若不计 $x = (2k + 1)\pi$ （ $k = 0, \pm 1, \pm 2, \dots$ ), 则 $f(x)$ 是周期为 $2\pi$ 的奇函数. 显然, 此时(7-8)式仍成立. 按公式(7-8)有 $a_n = 0$ ( $n = 0, 1, 2, \dots$ ), 而

$$
b _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \sin n x \mathrm{d} x = \frac {2}{\pi} \int_ {0} ^ {\pi} x \sin n x \mathrm{d} x = \frac {2}{\pi} \left[ - \frac {x \cos n x}{n} + \frac {\sin n x}{n ^ {2}} \right] _ {0} ^ {\pi}
$$

$$
= - \frac {2}{n} \cos n \pi = \frac {2}{n} (- 1) ^ {n + 1} (n = 1, 2, 3, \dots).
$$

将求得的 $b_{n}$ 代入正弦级数(7-9)，得 $f(x)$ 的傅里叶级数展开式为

$$
\begin{array}{l} f (x) = 2 \left(\sin x - \frac {1}{2} \sin 2 x + \frac {1}{3} \sin 3 x - \dots + \frac {(- 1) ^ {n + 1}}{n} \sin n x + \dots\right) \\ = 2 \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n + 1}}{n} \sin n x \quad (- \infty <   x <   + \infty ; x \neq \pm \pi , \pm 3 \pi , \dots). \\ \end{array}
$$

级数的和函数的图形如图 12-12 所示：

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/1759662a438eb7d145caa277f2016aa9e6cc1086eabfd73d68cb301475416c08.jpg)



图12-12


例 5 设 $f(x)$ 是周期为 $2\pi$ 的周期函数, 它在 $[-π, π)$ 上的表达式为 $f(x) = |x|$ , 将 $f(x)$ 展开成傅里叶级数.

解 所给函数满足收敛定理的条件, 它在整个数轴上连续, 因此 $f(x)$ 的傅里叶级数处处收敛于 $f(x)$ .

因为 $f(x)$ 是偶函数,所以按公式(7-10),有 $b_{n}=0\quad(n=1,2,3,\cdots)$ ,而

$$
\begin{array}{l} a _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \cos n x \mathrm{d} x = \frac {2}{\pi} \int_ {0} ^ {\pi} x \cos n x \mathrm{d} x \\ = \frac {2}{\pi} \left[ \frac {x \sin n x}{n} + \frac {\cos n x}{n ^ {2}} \right] _ {0} ^ {\pi} = \frac {2}{\pi n ^ {2}} (\cos n \pi - 1) \\ = \left\{ \begin{array}{l} - \frac {4}{\pi n ^ {2}}, \quad n = 1, 3, 5, \dots , \\ 0, \quad n = 2, 4, 6, \dots ; \end{array} \right. \\ a _ {0} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \mathrm{d} x = \frac {2}{\pi} \int_ {0} ^ {\pi} x \mathrm{d} x = \pi . \\ \end{array}
$$

将求得的系数 $a_{n}$ 代入余弦级数(7-11)，得 $f(x)$ 的傅里叶级数展开式为

$$
\begin{array}{l} f (x) = \frac {\pi}{2} - \frac {4}{\pi} \left(\cos x + \frac {1}{3 ^ {2}} \cos 3 x + \frac {1}{5 ^ {2}} \cos 5 x + \dots + \frac {1}{(2 k - 1) ^ {2}} \cos (2 k - 1) x + \dots\right) \\ = \frac {\pi}{2} - \frac {4}{\pi} \sum_ {k = 1} ^ {\infty} \frac {1}{(2 k - 1) ^ {2}} \cos (2 k - 1) x (- \infty <   x <   + \infty). \\ \end{array}
$$

在实际应用(如研究某种波动问题,热的传导、扩散问题)中,有时还需要把定义

在区间 $[0, \pi]$ 上的函数 $f(x)$ 展开成正弦级数或余弦级数.

根据前面讨论的结果,这类展开问题可以按如下的方法解决:设函数 $f(x)$ 定义在区间 $[0,\pi]$ 上并且满足收敛定理的条件,我们在开区间 $(-\pi,0)$ 内补充函数 $f(x)$ 的定义,得到定义在 $(-\pi,\pi]$ 上的函数 $F(x)$ ,使它在 $(-\pi,\pi)$ 上成为奇函数①(偶函数).按这种方式拓广函数定义域的过程称为奇延拓(偶延拓).然后将奇延拓(偶延拓)后的函数展开成傅里叶级数,这个级数必定是正弦级数(余弦级数).再限制x在 $(0,\pi]$ 上,此时 $F(x)\equiv f(x)$ ,这样便得到 $f(x)$ 的正弦级数(余弦级数)展开式.

例如将函数

$$
\varphi (x) = x \quad (0 \leqslant x \leqslant \pi)
$$

作奇延拓,再作周期延拓,便成例4中的函数,按例4的结果,有

$$
x = 2 \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n + 1}}{n} \sin n x (0 \leqslant x <   \pi);
$$

将 $\varphi(x)$ 作偶延拓, 再作周期延拓, 便成例 5 中的函数, 按例 5 的结果, 有

$$
x = \frac {\pi}{2} - \frac {4}{\pi} \sum_ {k = 1} ^ {\infty} \frac {1}{(2 k - 1) ^ {2}} \cos (2 k - 1) x \quad (0 \leqslant x \leqslant \pi).
$$

例6 将函数

$$
f (x) = \left\{ \begin{array}{l l} \cos x, & 0 \leqslant x <   \frac {\pi}{2}, \\ 0, & \frac {\pi}{2} \leqslant x \leqslant \pi \end{array} \right.
$$

分别展开成正弦级数和余弦级数.

解 先展开成正弦级数.为此对函数 $f(x)$ 作奇延拓(图12-13).按公式(7-8)有

$$
b _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \sin n x \mathrm{d} x = \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} \cos x \sin n x \mathrm{d} x
$$

$$
= \frac {1}{\pi} \int_ {0} ^ {\frac {\pi}{2}} [ \sin (n - 1) x + \sin (n + 1) x ] d x
$$

$$
= \frac {1}{\pi} \left[ - \frac {1}{n - 1} \cos (n - 1) x - \frac {1}{n + 1} \cos (n + 1) x \right] _ {0} ^ {\frac {\pi}{2}}
$$

$$
= \frac {1}{\pi} \left(\frac {1}{n - 1} + \frac {1}{n + 1} - \frac {1}{n - 1} \cos \frac {n - 1}{2} \pi - \frac {1}{n + 1} \cos \frac {n + 1}{2} \pi\right)
$$

$$
= \frac {1}{\pi} \left(\frac {2 n}{n ^ {2} - 1} - \frac {1}{n - 1} \sin \frac {n \pi}{2} + \frac {1}{n + 1} \sin \frac {n \pi}{2}\right)
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/ea877dc68babbe50db15544c484ec9725680470d0d1f50e5b1b51d407321cf44.jpg)



图12-13


$$
= \frac {2}{\pi (n ^ {2} - 1)} (n - \sin \frac {n \pi}{2}).
$$

以上计算对 n=1 不适合, $b_{1}$ 需另行计算:

$$
b _ {1} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \sin x \mathrm{d} x = \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} \cos x \sin x \mathrm{d} x = \frac {1}{\pi}.
$$

将求得的 $b_{n}$ 代入(7-9)式，得 $f(x)$ 的正弦级数展开式为

$$
f (x) = \frac {1}{\pi} [ \sin x + 2 \sum_ {n = 2} ^ {\infty} \frac {1}{n ^ {2} - 1} (n - \sin \frac {n \pi}{2}) \sin n x ] \quad (0 <   x \leqslant \pi).
$$

在端点 x=0 处级数收敛到零, 它不等于 $f(0)$ .

再展开成余弦级数.为此对函数 $f(x)$ 作偶延拓(图12-14).

按公式(7-10)有

$$
\begin{array}{l} a _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \cos n x \mathrm{d} x = \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} \cos x \cos n x \mathrm{d} x \\ = \frac {1}{\pi} \int_ {0} ^ {\frac {\pi}{2}} [ \cos (n - 1) x + \cos (n + 1) x ] d x \\ = \frac {1}{\pi} \left[ \frac {1}{n - 1} \sin \frac {n - 1}{2} \pi + \frac {1}{n + 1} \sin \frac {n + 1}{2} \pi \right] \\ = \frac {2}{\pi (n ^ {2} - 1)} \sin \frac {n - 1}{2} \pi = \left\{ \begin{array}{l l} 0, & n = 2 k - 1, \\ \frac {2 (- 1) ^ {k - 1}}{\pi (4 k ^ {2} - 1)}, & n = 2 k. \end{array} \right. \\ \end{array}
$$

以上计算对 n=1 不适合, $a_{1}$ 需另行计算:

$$
a _ {1} = \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} x \mathrm{d} x = \frac {1}{\pi} \int_ {0} ^ {\frac {\pi}{2}} (1 + \cos 2 x) \mathrm{d} x = \frac {1}{2}.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/332abc700d85fbede284a3162b1d3fd3e28f385512f74503f8bf34c4ca1aeca9.jpg)



图12-14


将求得的 $a_{n}$ 代入(7-11)式, 得 $f(x)$ 的余弦级数展开式为

$$
f (x) = \frac {1}{\pi} + \frac {1}{2} \cos x + \frac {2}{\pi} \sum_ {k = 1} ^ {\infty} \frac {(- 1) ^ {k - 1}}{4 k ^ {2} - 1} \cos 2 k x \quad (0 \leqslant x \leqslant \pi).
$$

利用函数的傅里叶级数展开式,有时可得一些特殊级数的和,例如按例5的结果,有

$$
\mid x \mid = \frac {\pi}{2} - \frac {4}{\pi} \sum_ {k = 1} ^ {\infty} \frac {1}{(2 k - 1) ^ {2}} \cos (2 k - 1) x \quad (- \pi \leqslant x \leqslant \pi),
$$

在上式中令 x=0，便得

$$
\sum_ {k = 1} ^ {\infty} \frac {1}{(2 k - 1) ^ {2}} = \frac {\pi^ {2}}{8}.
$$

设

$$
\sigma = 1 + \frac {1}{2 ^ {2}} + \frac {1}{3 ^ {2}} + \frac {1}{4 ^ {2}} + \dots + \frac {1}{n ^ {2}} + \dots ,
$$

$$
\sigma_ {1} = 1 + \frac {1}{3 ^ {2}} + \frac {1}{5 ^ {2}} + \dots + \frac {1}{(2 n - 1) ^ {2}} + \dots \left(= \frac {\pi^ {2}}{8}\right),
$$

$$
\sigma_ {2} = \frac {1}{2 ^ {2}} + \frac {1}{4 ^ {2}} + \frac {1}{6 ^ {2}} + \dots + \frac {1}{(2 n) ^ {2}} + \dots ,
$$

$$
\sigma_ {3} = 1 - \frac {1}{2 ^ {2}} + \frac {1}{3 ^ {2}} - \frac {1}{4 ^ {2}} + \dots + (- 1) ^ {n - 1} \frac {1}{n ^ {2}} + \dots .
$$

因为

$$
\sigma_ {2} = \frac {\sigma}{4} = \frac {\sigma_ {1} + \sigma_ {2}}{4},
$$

所以

$$
\sigma_ {2} = \frac {\sigma_ {1}}{3} = \frac {\pi^ {2}}{2 4}, \quad \sigma = \sigma_ {1} + \sigma_ {2} = \frac {\pi^ {2}}{8} + \frac {\pi^ {2}}{2 4} = \frac {\pi^ {2}}{6},
$$

又

$$
\sigma_ {3} = 2 \sigma_ {1} - \sigma = \frac {\pi^ {2}}{4} - \frac {\pi^ {2}}{6} = \frac {\pi^ {2}}{1 2}.
$$

# 习题12-7

1. 下列周期函数 $f(x)$ 的周期为 $2\pi$ ，试将 $f(x)$ 展开成傅里叶级数，如果 $f(x)$ 在 $[-\pi, \pi)$ 上的表达式为

(1) $f(x)=3x^{2}+1$ ( $-\pi\leqslant x<\pi$ ); 

(2) $f(x) = \mathrm{e}^{2x}(-\pi \leqslant x <   \pi)$ 

(3) $f(x)=\left\{\begin{aligned}&bx,-\pi \leqslant x<0,\\&ax,0\leqslant x<\pi(a,b\text{为常数，且}a>b>0).\end{aligned}\right.$ 

2. 将下列函数 $f(x)$ 展开成傅里叶级数：

(1) $f(x)=2\sin\frac{x}{3}\quad(-\pi\leqslant x\leqslant\pi)$ ; 

(2) $f(x) = \begin{cases} e^x, & -\pi \leqslant x < 0, \\ 1, & 0 \leqslant x \leqslant \pi; \end{cases}$ 

(3) $f(x) = x \sin x (-\pi \leqslant x \leqslant \pi).$ 

3. 将函数 $f(x) = \cos \frac{x}{2} (-\pi \leqslant x \leqslant \pi)$ 展开成傅里叶级数.

4. 设 $f(x)$ 是周期为 $2\pi$ 的周期函数, 它在 $[- \pi, \pi)$ 上的表达式为

$$
f (x) = \left\{ \begin{array}{l l} - \frac {\pi}{2}, & - \pi \leqslant x <   - \frac {\pi}{2}, \\ x, & - \frac {\pi}{2} \leqslant x <   \frac {\pi}{2}, \\ \frac {\pi}{2}, & \frac {\pi}{2} \leqslant x <   \pi , \end{array} \right.
$$

将 $f(x)$ 展开成傅里叶级数.

5. 将函数 $f(x) = \frac{\pi - x}{2} (0 \leqslant x \leqslant \pi)$ 展开成正弦级数.

6. 将函数 $f(x)=2x^{2}$ ( $0 \leqslant x \leqslant \pi$ ) 分别展开成正弦级数和余弦级数.

7. 设周期函数 $f(x)$ 的周期为 $2\pi$ . 证明：

(1) 若 $f(x-\pi)=-f(x)$ ，则 $f(x)$ 的傅里叶系数 $a_{0}=0, a_{2k}=0, b_{2k}=0 (k=1,2,\cdots)$ ;

(2) 若 $f(x-\pi)=f(x)$ ，则 $f(x)$ 的傅里叶系数 $a_{2k+1}=0, b_{2k+1}=0 (k=0,1,2,\cdots)$ .

# 第八节 一般周期函数的傅里叶级数

# 一、周期为 $2l$ 的周期函数的傅里叶级数

上节所讨论的周期函数都是以 $2\pi$ 为周期的,但是实际问题中所遇到的周期函数,它的周期不一定是 $2\pi$ .例如上节中提到的矩形波,它的周期是 $T=\frac{2\pi}{\omega}$ .因此,本节我们讨论周期为 2l 的周期函数的傅里叶级数.根据上节讨论的结果,经过自变量的变量代换,可得下面的定理:

定理 设周期为 $2l$ 的周期函数 $f(x)$ 满足收敛定理的条件, 则它的傅里叶级数展开式为

$$
f (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi x}{l} + b _ {n} \sin \frac {n \pi x}{l}\right) \quad (x \in C), \tag {8-1}
$$

其中

$$
\left. \begin{array}{l l} a _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm{d} x & (n = 0, 1, 2, \dots), \\ b _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm{d} x & (n = 1, 2, 3, \dots), \end{array} \right\} \tag {8-2}
$$

$$
C = \left\{x \mid f (x) = \frac {1}{2} [ f (x ^ {-}) + f (x ^ {+}) ] \right\}.
$$

当 $f(x)$ 为奇函数时，

$$
f (x) = \sum_ {n = 1} ^ {\infty} b _ {n} \sin \frac {n \pi x}{l} \quad (x \in C), \tag {8-3}
$$

其中

$$
b _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm{d} x \quad (n = 1, 2, 3, \dots). \tag {8-4}
$$

当 $f(x)$ 为偶函数时，

$$
f (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} a _ {n} \cos \frac {n \pi x}{l} \quad (x \in C), \tag {8-5}
$$

其中

$$
a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm{d} x \quad (n = 0, 1, 2, \dots). \tag {8-6}
$$

证 作变量代换 $z = \frac{\pi x}{l}$ , 于是区间 $-l \leqslant x \leqslant l$ 就变换成 $-\pi \leqslant z \leqslant \pi$ . 设函数 $f(x) = f\left(\frac{lz}{\pi}\right) = F(z)$ , 从而 $F(z)$ 是周期为 $2\pi$ 的周期函数, 并且它满足收敛定理的条件, 将 $F(z)$ 展开成傅里叶级数

$$
F (z) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n z + b _ {n} \sin n z\right),
$$

其中

$$
a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} F (z) \cos n z \mathrm{d} z, b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} F (z) \sin n z \mathrm{d} z.
$$

在以上式子中令 $z = \frac{\pi x}{l}$ 并注意到 $F(z) = f(x)$ ，于是有

$$
f (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi x}{l} + b _ {n} \sin \frac {n \pi x}{l}\right),
$$

而且

$$
a _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm{d} x, b _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm{d} x.
$$

类似地,可以证明定理的其余部分.

例 1 设 $f(x)$ 是周期为 4 的周期函数, 它在 $[-2,2)$ 上的表达式为

$$
f (x) = \left\{ \begin{array}{l l} 0, & - 2 \leqslant x <   0, \\ h, & 0 \leqslant x <   2 \end{array} \right. (\text {常数} h \neq 0).
$$

将 $f(x)$ 展开成傅里叶级数,并作出级数的和函数的图形.

解 这时 l=2, 按公式(8-2)有

$$
a _ {n} = \frac {1}{2} \int_ {0} ^ {2} h \cos \frac {n \pi x}{2} \mathrm{d} x = \left[ \frac {h}{n \pi} \sin \frac {n \pi x}{2} \right] _ {0} ^ {2} = 0 (n \neq 0);
$$

$$
a _ {0} = \frac {1}{2} \int_ {- 2} ^ {0} 0 \mathrm{d} x + \frac {1}{2} \int_ {0} ^ {2} h \mathrm{d} x = h;
$$

$$
b _ {n} = \frac {1}{2} \int_ {0} ^ {2} h \sin \frac {n \pi x}{2} \mathrm{d} x = \left[ - \frac {h}{n \pi} \cos \frac {n \pi x}{2} \right] _ {0} ^ {2}
$$

$$
= \frac {h}{n \pi} (1 - \cos n \pi) = \left\{ \begin{array}{l l} \frac {2 h}{n \pi}, & n = 1, 3, 5, \dots , \\ 0, & n = 2, 4, 6, \dots . \end{array} \right.
$$

将求得的系数 $a_{n}, b_{n}$ 代入(8-1)式, 得

$$
\begin{array}{l} f (x) = \frac {h}{2} + \frac {2 h}{\pi} \left(\sin \frac {\pi x}{2} + \frac {1}{3} \sin \frac {3 \pi x}{2} + \frac {1}{5} \sin \frac {5 \pi x}{2} + \dots + \frac {1}{2 n - 1} \sin \frac {(2 n - 1) \pi x}{2} + \dots\right) \\ (- \infty <   x <   + \infty ; x \neq 0, \pm 2, \pm 4, \dots) \\ \end{array}
$$

级数的和函数的图形如图 12-15 所示.

例 2 将如图 12-16 所示的函数

$$
M (x) = \left\{ \begin{array}{l l} \frac {p x}{2}, & 0 \leqslant x <   \frac {l}{2}, \\ \frac {p (l - x)}{2}, & \frac {l}{2} \leqslant x \leqslant l \end{array} \right.
$$

分别展开成正弦级数和余弦级数.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/b369d0302d14f362682ba300782d3e6f6f6d89feddc8e225957bdfc6381585ef.jpg)



图12-15


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/e4213d16fdbbf48e3f722f7f052e5c3b4990e3c1a0b52ab29f79dcef34eae508.jpg)



图12-16


解 $M(x)$ 是定义在 $[0, l]$ 上的函数, 要将它展开成正弦级数, 必须对 $M(x)$ 进行奇延拓. 按公式(8-4)计算延拓后的函数的傅里叶系数

$$
\begin{array}{l} b _ {n} = \frac {2}{l} \int_ {0} ^ {l} M (x) \sin \frac {n \pi x}{l} \mathrm{d} x \\ = \frac {2}{l} \left[ \int_ {0} ^ {\frac {l}{2}} \frac {p x}{2} \sin \frac {n \pi x}{l} \mathrm{d} x + \int_ {\frac {l}{2}} ^ {l} \frac {p (l - x)}{2} \sin \frac {n \pi x}{l} \mathrm{d} x \right]. \\ \end{array}
$$

对上式右端的第二项,令 t=l-x,则

$$
\begin{array}{l} b _ {n} = \frac {p}{l} \left[ \int_ {0} ^ {\frac {l}{2}} x \sin \frac {n \pi x}{l} \mathrm{d} x + \int_ {\frac {l}{2}} ^ {0} t \sin \frac {n \pi (l - t)}{l} (- \mathrm{d} t) \right] \\ = \frac {p}{l} \left[ \int_ {0} ^ {\frac {l}{2}} x \sin \frac {n \pi x}{l} \mathrm{d} x + (- 1) ^ {n + 1} \int_ {0} ^ {\frac {l}{2}} t \sin \frac {n \pi t}{l} \mathrm{d} t \right]. \\ \end{array}
$$

当 $n = 2k$ 为偶数时， $b_{2k} = 0$ ；当 $n = 2k - 1$ 为奇数时，

$$
b _ {2 k - 1} = \frac {2 p}{l} \int_ {0} ^ {\frac {l}{2}} x \sin \frac {(2 k - 1) \pi x}{l} \mathrm{d} x = \frac {2 p l}{(2 k - 1) ^ {2} \pi^ {2}} \sin \frac {2 k - 1}{2} \pi .
$$

$$
= \frac {2 p l (- 1) ^ {k - 1}}{(2 k - 1) ^ {2} \pi^ {2}}.
$$

将求得的 $b_{n}$ 代入(8-3)式，得 $M(x)$ 的正弦级数展开式为

$$
M (x) = \frac {2 p l}{\pi^ {2}} \sum_ {k = 1} ^ {\infty} \frac {(- 1) ^ {k - 1}}{(2 k - 1) ^ {2}} \sin \frac {(2 k - 1) \pi x}{l} \quad (0 \leqslant x \leqslant l).
$$

再求 $M(x)$ 的余弦级数展开式.为此对 $M(x)$ 作偶延拓，再作周期延拓.注意到延拓所得周期函数的周期为 $l$ ，知 $M(x)$ 可展开成周期为 $l$ 的余弦级数.按公式(8-6）将(8-6)中的 $l$ 换成 $\frac{l}{2}$ 计算傅里叶系数：

$$
\begin{array}{l} a _ {n} = \frac {4}{l} \int_ {0} ^ {\frac {l}{2}} M (x) \cos \frac {2 n \pi x}{l} \mathrm{d} x = \frac {4}{l} \int_ {0} ^ {\frac {l}{2}} \frac {p x}{2} \cos \frac {2 n \pi x}{l} \mathrm{d} x \\ = \frac {2 p}{l} \left[ \frac {l}{2 n \pi} x \sin \frac {2 n \pi x}{l} + \left(\frac {l}{2 n \pi}\right) ^ {2} \cos \frac {2 n \pi x}{l} \right] _ {0} ^ {\frac {l}{2}} \\ = \frac {p l}{2 n ^ {2} \pi^ {2}} (\cos n \pi - 1) = \left\{ \begin{array}{l l} - \frac {p l}{n ^ {2} \pi^ {2}}, & n = 1, 3, 5, \dots , \\ 0, & n = 2, 4, 6, \dots . \end{array} \right. \\ a _ {0} = \frac {4}{l} \int_ {0} ^ {\frac {l}{2}} \frac {p x}{2} \mathrm{d} x = \frac {p l}{4}. \\ \end{array}
$$

将求得的 $a_{n}$ 代入(8-5)式, 得

$$
M (x) = \frac {p l}{8} - \frac {p l}{\pi^ {2}} \sum_ {k = 1} ^ {\infty} \frac {1}{(2 k - 1) ^ {2}} \cos \frac {2 (2 k - 1) \pi x}{l} \quad (0 \leqslant x \leqslant l).
$$

# *二、傅里叶级数的复数形式

傅里叶级数还可以用复数形式表示.在电子技术中,经常应用这种形式.

设周期为 2l 的周期函数 $f(x)$ 的傅里叶级数为

$$
\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi x}{l} + b _ {n} \sin \frac {n \pi x}{l}\right), \tag {8-7}
$$

其中系数 $a_{n}$ 与 $b_{n}$ 为

$$
\left. \begin{array}{l} a _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm{d} x \quad (n = 0, 1, 2, \dots), \\ b _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm{d} x \quad (n = 1, 2, 3, \dots). \end{array} \right\} \tag {8-8}
$$

利用欧拉公式

$$
\cos t = \frac {\mathrm{e} ^ {t i} + \mathrm{e} ^ {- t i}}{2}, \quad \sin t = \frac {\mathrm{e} ^ {t i} - \mathrm{e} ^ {- t i}}{2 \mathrm{i}},
$$

把(8-7)式化为

$$
\begin{array}{l} \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left[ \frac {a _ {n}}{2} \left(\mathrm{e} ^ {\frac {n \pi x}{l} \mathrm{i}} + \mathrm{e} ^ {- \frac {n \pi x}{l} \mathrm{i}}\right) - \frac {b _ {n} \mathrm{i}}{2} \left(\mathrm{e} ^ {\frac {n \pi x}{l} \mathrm{i}} - \mathrm{e} ^ {- \frac {n \pi x}{l} \mathrm{i}}\right) \right] \\ = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left[ \frac {a _ {n} - b _ {n} \mathrm{i}}{2} \mathrm{e} ^ {\frac {n \pi x}{l} \mathrm{i}} + \frac {a _ {n} + b _ {n} \mathrm{i}}{2} \mathrm{e} ^ {- \frac {n \pi x}{l} \mathrm{i}} \right]. \tag {8-9} \\ \end{array}
$$

记

$$
\frac {a _ {0}}{2} = c _ {0}, \quad \frac {a _ {n} - b _ {n} \mathrm{i}}{2} = c _ {n}, \quad \frac {a _ {n} + b _ {n} \mathrm{i}}{2} = c _ {- n} \quad (n = 1, 2, 3, \dots), \tag {8-10}
$$

则(8-9)式就表示为

$$
c _ {0} + \sum_ {n = 1} ^ {\infty} \left(c _ {n} \mathrm{e} ^ {\frac {n \pi x}{l} \mathrm{i}} + c _ {- n} \mathrm{e} ^ {- \frac {n \pi x}{l} \mathrm{i}}\right) = \left(c _ {n} \mathrm{e} ^ {\frac {n \pi x}{l} \mathrm{i}}\right) _ {n = 0} + \sum_ {n = 1} ^ {\infty} \left(c _ {n} \mathrm{e} ^ {\frac {n \pi x}{l} \mathrm{i}} + c _ {- n} \mathrm{e} ^ {- \frac {n \pi x}{l} \mathrm{i}}\right).
$$

即得傅里叶级数的复数形式为

$$
\sum_ {n = - \infty} ^ {\infty} c _ {n} \mathrm{e} ^ {\frac {n \pi x}{l} \mathrm{i}}. \tag {8-11}
$$

为得出系数 $c_{n}$ 的表达式，把(8-8)式代入(8-10)式，得

$$
\begin{array}{l} c _ {0} = \frac {a _ {0}}{2} = \frac {1}{2 l} \int_ {- l} ^ {l} f (x) \mathrm{d} x; \\ c _ {n} = \frac {a _ {n} - b _ {n} \mathrm{i}}{2} = \frac {1}{2} \left[ \frac {1}{l} \int_ {- l} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm{d} x - \frac {\mathrm{i}}{l} \int_ {- l} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm{d} x \right] \\ = \frac {1}{2 l} \int_ {- l} ^ {l} f (x) \left(\cos \frac {n \pi x}{l} - i \sin \frac {n \pi x}{l}\right) d x \\ = \frac {1}{2 l} \int_ {- l} ^ {l} f (x) \mathrm{e} ^ {- \frac {n \pi x}{l} \mathrm{i}} \mathrm{d} x \quad (n = 1, 2, 3, \dots); \\ c _ {- n} = \frac {a _ {n} + b _ {n} \mathrm{i}}{2} = \frac {1}{2 l} \int_ {- l} ^ {l} f (x) \mathrm{e} ^ {\frac {n \pi x}{l} \mathrm{i}} \mathrm{d} x \quad (n = 1, 2, 3, \dots). \\ \end{array}
$$

将已得的结果合并写为

$$
c _ {n} = \frac {1}{2 l} \int_ {- l} ^ {l} f (x) \mathrm{e} ^ {- \frac {n \pi x}{l} \mathrm{i}} \mathrm{d} x \quad (n = 0, \pm 1, \pm 2, \dots). \tag {8-12}
$$

这就是傅里叶系数的复数形式.

傅里叶级数的两种形式本质上是一样的,但复数形式比较简洁,且只用一个算式计算系数.

例 3 把宽为 $\tau$ 、高为 h、周期为 T 的矩形波(图 12-17)展开成复数形式的傅里叶级数.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/213f2974d04b7edcb0b22acc98a4afcf9f98a5855a1b739f4291542ab7e0bff0.jpg)



图12-17


解 在一个周期 $\left[-\frac{T}{2}, \frac{T}{2}\right)$ 内矩形波的函数表达式为

$$
u (t) = \left\{ \begin{array}{l l} 0, & - \frac {T}{2} \leqslant t <   - \frac {\tau}{2}, \\ h, & - \frac {\tau}{2} \leqslant t <   \frac {\tau}{2}, \\ 0, & \frac {\tau}{2} \leqslant t <   \frac {T}{2}. \end{array} \right.
$$

按公式(8-12)有

$$
\begin{array}{l} c _ {n} = \frac {1}{T} \int_ {- T / 2} ^ {T / 2} u (t) \mathrm{e} ^ {- \frac {2 n \pi t}{T} \mathrm{i}} \mathrm{d} t = \frac {1}{T} \int_ {- \tau / 2} ^ {\tau / 2} h \mathrm{e} ^ {- \frac {2 n \pi t}{T} \mathrm{i}} \mathrm{d} t \\ = \frac {h}{T} \left[ \frac {- T}{2 n \pi \mathrm{i}} \mathrm{e} ^ {- \frac {2 n \pi t}{T} \mathrm{i}} \right] _ {- \tau / 2} ^ {\tau / 2} = \frac {h}{n \pi} \sin \frac {n \pi \tau}{T} (n = \pm 1, \pm 2, \dots), \\ c _ {0} = \frac {1}{T} \int_ {- T / 2} ^ {T / 2} u (t) \mathrm{d} t = \frac {1}{T} \int_ {- \tau / 2} ^ {\tau / 2} h \mathrm{d} t = \frac {h \tau}{T}, \\ \end{array}
$$

将求得的 $c_{n}$ 代入级数(8-11)，得

$$
u(t) = \frac{h\tau}{T} +\frac{h}{\pi}\sum_{\substack{n = -\infty \\ n\neq 0}}^{\infty}\frac{1}{n}\sin \frac{n\pi\tau}{T}\mathrm{e}^{\frac{2n\pi t}{T}\mathrm{i}}\quad \left(-\infty <  t <   + \infty ;t\neq n T\pm \frac{\tau}{2},n = 0,\pm 1, \pm 2,\dots\right).
$$

# 习题12-8

1. 将下列各周期函数展开成傅里叶级数(下面给出函数在一个周期内的表达式):

(1) $f(x) = 1 - x^{2}\left(-\frac{1}{2} \leqslant x < \frac{1}{2}\right)$ ; 

(2) $f(x) = \left\{ \begin{array}{ll}x, & -1\leqslant x <   0,\\ 1, & 0\leqslant x <   \frac{1}{2},\\ -1 & \frac{1}{2}\leqslant x <   1; \end{array} \right.$ 

(3) $f(x)=\left\{\begin{aligned}&2x+1,&-3\leqslant x<0,\\ &1,&0\leqslant x<3.\end{aligned}\right.$ 

2. 将下列函数分别展开成正弦级数和余弦级数：

(1) $f(x)=\left\{\begin{aligned}&x,\quad0\leqslant x<\frac{l}{2},\\&l-x,\quad\frac{l}{2}\leqslant x\leqslant l;\end{aligned}\right.$ 

(2) $f(x) = x^{2}$ (0≤x≤2). 

*3. 设 $f(x)$ 是周期为 2 的周期函数, 它在 $[-1, 1)$ 上的表达式为 $f(x) = e^{-x}$ . 试将 $f(x)$ 展开成复数形式的傅里叶级数.

*4. 设 $u(t)$ 是周期为 $T$ 的周期函数. 已知它的傅里叶级数的复数形式为 (参阅本节例题)

$$
u(t) = \frac{h\tau}{T} +\frac{h}{\pi}\sum_{\substack{n = -\infty \\ n\neq 0}}^{\infty}\frac{1}{n}\sin \frac{n\pi\tau}{T}\mathrm{e}^{\frac{2n\pi t}{T}\mathrm{i}}\quad (-\infty <  t <   + \infty),
$$

试写出 $u(t)$ 的傅里叶级数的实数形式(即三角形式).

# 总习题十二

1. 填空：

（1）对级数 $\sum_{n=1}^{\infty} u_n, \lim_{n \to \infty} u_n = 0$ 是它收敛的 ____ 条件，不是它收敛的 ____ 条件；

(2) 部分和数列 $\{s_{n}\}$ 有界是正项级数 $\sum_{n=1}^{\infty} u_{n}$ 收敛的 ____ 条件；

(3) 若级数 $\sum_{n=1}^{\infty} u_n$ 绝对收敛, 则级数 $\sum_{n=1}^{\infty} u_n$ 必定____; 若级数 $\sum_{n=1}^{\infty} u_n$ 条件收敛, 则级数 $\sum_{n=1}^{\infty} |u_n|$ 必定____.

2. 下题中给出了四个结论,从中选出一个正确的结论:

设 $f(x)$ 是以 $2\pi$ 为周期的周期函数, 它在 $[- \pi, \pi)$ 上的表达式为 $|x|$ , 则 $f(x)$ 的傅里叶级数为 ( ).

(A) $\frac{\pi}{2}-\frac{4}{\pi}\left[\cos x+\frac{1}{3^{2}}\cos 3x+\frac{1}{5^{2}}\cos 5x+\cdots+\frac{1}{(2n-1)^{2}}\cos(2n-1)x+\cdots\right]$ 

(B) $\frac{2}{\pi}\left[\frac{1}{2^2}\sin 2x + \frac{1}{4^2}\sin 4x + \frac{1}{6^2}\sin 6x + \cdots + \frac{1}{(2n)^2}\sin 2nx + \cdots\right]$ 

(C) $\frac{4}{\pi}\left[\cos x+\frac{1}{3^{2}}\cos 3x+\frac{1}{5^{2}}\cos 5x+\cdots+\frac{1}{(2n-1)^{2}}\cos(2n-1)x+\cdots\right]$ 

(D) $\frac{1}{\pi}\left[\frac{1}{2^{2}}\cos2x+\frac{1}{4^{2}}\cos4x+\frac{1}{6^{2}}\cos6x+\cdots+\frac{1}{(2n)^{2}}\cos2nx+\cdots\right]$ 

3. 判定下列级数的收敛性：

(1) $\sum_{n=1}^{\infty} \frac{1}{n\sqrt[n]{n}}$ ; 

(2) $\sum_{n=1}^{\infty} \frac{(n!)^{2}}{2n^{2}}$ ; 

(3) $\sum_{n=1}^{\infty} \frac{n \cos^{2} \frac{n \pi}{3}}{2^{n}}$ ; 

(4) $\sum_{n=2}^{\infty} \frac{1}{\ln^{10} n}$ ; 

(5) $\sum_{n=1}^{\infty} \frac{a^n}{n^s} (a > 0, s > 0)$ . 

4. 设正项级数 $\sum_{n=1}^{\infty} u_n$ 和 $\sum_{n=1}^{\infty} v_n$ 都收敛, 证明级数 $\sum_{n=1}^{\infty} (u_n + v_n)^2$ 也收敛.

5. 设级数 $\sum_{n=1}^{\infty} u_n$ 收敛, 且 $\lim_{n \to \infty} \frac{v_n}{u_n} = 1$ . 问级数 $\sum_{n=1}^{\infty} v_n$ 是否也收敛? 试说明理由.

6. 讨论下列级数的绝对收敛性与条件收敛性：

(1) $\sum_{n=1}^{\infty} (-1)^{n} \frac{1}{n^{p}}$ ; 

(2) $\sum_{n=1}^{\infty} (-1)^{n+1} \frac{\sin \frac{\pi}{n+1}}{\pi^{n+1}}$ ; 

(3) $\sum_{n=1}^{\infty} (-1)^{n} \ln \frac{n+1}{n}$ ; 

(4) $\sum_{n=1}^{\infty} (-1)^{n} \frac{(n+1)!}{n^{n+1}}$ . 

7. 求下列极限：

(1) $\lim_{n\to \infty}\frac{1}{n}\sum_{k = 1}^{n}\frac{1}{3^k}\left(1 + \frac{1}{k}\right)^{k^2};$ 

(2) $\lim_{n\to\infty}\left[2^{\frac{1}{3}}\times4^{\frac{1}{9}}\times8^{\frac{1}{27}}\times\cdots\times(2^{n})^{\frac{1}{3^{n}}}\right].$ 

8. 求下列幂级数的收敛区间：

(1) $\sum_{n=1}^{\infty} \frac{3^n + 5^n}{n} x^n$ ; 

(2) $\sum_{n=1}^{\infty}\left(1+\frac{1}{n}\right)^{n^{2}}x^{n}$ ; 

(3) $\sum_{n=1}^{\infty} n(x+1)^{n}$ ; 

(4) $\sum_{n=1}^{\infty} \frac{n}{2^n} x^{2n}$ . 

9. 求下列幂级数的和函数：

(1) $\sum_{n=1}^{\infty} \frac{2n-1}{2^n} x^{2(n-1)}$ ; 

* (2) $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{2n-1} x^{2n-1}$ ; 

(3) $\sum_{n=1}^{\infty} n(x-1)^{n}$ ; 

* (4) $\sum_{n=1}^{\infty} \frac{x^n}{n(n+1)}$ . 

10. 设幂级数 $\sum_{n=1}^{\infty} a_n x^n$ 的系数 $a_1 = 1, a_2 = 0$ , 且满足 $a_n = \frac{-1}{(n-1)(n-2)} a_{n-2}$ ( $n \geqslant 3, n \in \mathbb{N}$ ). 试求该幂级数的收敛域与和函数 $f(x)$ .

11. 求下列数项级数的和：

(1) $\sum_{n=1}^{\infty} \frac{n^{2}}{n!}$ ; 

(2) $\sum_{n=0}^{\infty} (-1)^{n} \frac{n+1}{(2n+1)!}$ . 

12. 将下列函数展开成 x 的幂级数：

(1) $\ln(x+\sqrt{x^{2}+1})$ ; 

(2) $\frac{1}{(2-x)^{2}}.$ 

13. 设 $f(x)$ 是周期为 $2\pi$ 的函数, 它在 $[-π, π)$ 上的表达式为

$$
f (x) = \left\{ \begin{array}{l l} 0, & x \in [ - \pi , 0), \\ e ^ {x}, & x \in [ 0, \pi). \end{array} \right.
$$

将 $f(x)$ 展开成傅里叶级数.

14. 将函数

$$
f (x) = \left\{ \begin{array}{l l} 1, & 0 \leqslant x \leqslant h, \\ 0, & h <   x \leqslant \pi \end{array} \right.
$$

分别展开成正弦级数和余弦级数.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/2fea031474bbd658c22d8316093a1479f694f4511183e97d60380ffe23544928.jpg)



第十二章释疑解难


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/f3f8b866c390b4aad52260c5e9a5583bfe1ade657ae9095437e6cdd5e8fc2923.jpg)



第十二章例题精讲


# 部分习题参考答案与提示

# 第八章

# 习题8-1（第13页）

1. 5a-11b+7c. 

2. 略.

3. $\overrightarrow{D_1A} = -\left(c + \frac{1}{5} a\right),\overrightarrow{D_2A} = -\left(c + \frac{2}{5} a\right),\overrightarrow{D_3A} = -\left(c + \frac{3}{5} a\right),\overrightarrow{D_4A} = -\left(c + \frac{4}{5} a\right).$ 

4. $(1,-2,-2),(-2,4,4)$ . 

5. $\left(\frac{6}{11},\frac{7}{11},-\frac{6}{11}\right)$ 或 $\left(-\frac{6}{11},-\frac{7}{11},\frac{6}{11}\right)$ .

6. A: IV, B: V, C: VIII, D: III. 

7. A 在 xOy 面上, B 在 yOz 面上, C 在 x 轴上, D 在 y 轴上.

8. (1) $(a, b, -c), (-a, b, c), (a, -b, c)$ ; 

(2) $(a, -b, -c), (-a, b, -c), (-a, -b, c)$ ; 

(3) $(-a,-b,-c)$ . 

9. $xOy$ 面： $(x_0, y_0, 0), yOz$ 面： $(0, y_0, z_0), zOx$ 面： $(x_0, 0, z_0)$ ;

x 轴: $(x_{0},0,0)$ , y 轴: $(0,y_{0},0)$ , z 轴: $(0,0,z_{0})$ .

10. 略.

11. $\left(\frac{\sqrt{2}}{2} a,0,0\right),\left(-\frac{\sqrt{2}}{2} a,0,0\right),\left(0,\frac{\sqrt{2}}{2} a,0\right),\left(0,-\frac{\sqrt{2}}{2} a,0\right),\left(\frac{\sqrt{2}}{2} a,0,a\right),$ 

$$
\left(- \frac {\sqrt {2}}{2} a, 0, a\right), \left(0, \frac {\sqrt {2}}{2} a, a\right), \left(0, - \frac {\sqrt {2}}{2} a, a\right).
$$

12. $x$ 轴： $\sqrt{34}$ ， $y$ 轴： $\sqrt{41}$ ， $z$ 轴：5.

13. $(0,1,-2)$ . 

14. 略.

15. 模:2;方向余弦: $-\frac{1}{2},-\frac{\sqrt{2}}{2},\frac{1}{2}$ ;方向角: $\frac{2\pi}{3},\frac{3\pi}{4},\frac{\pi}{3}$ .

16.（1）垂直于 $x$ 轴，平行于 $yOz$ 平面；

(2) 指向与 y 轴正向一致, 垂直于 zOx 平面;

(3) 平行于 z 轴, 垂直于 xOy 平面.

17.2. 

18. $A(-2,3,0)$ . 

19. 13,7j. 

20. 略.

# 习题8-2（第22页）

1. (1) $3,5i+j+7k$ ; (2) $-18,10i+2j+14k$ ; (3) $\cos(\widehat{a,b})=\frac{3}{2\sqrt{21}}$ . 

2. $-\frac{3}{2}.$ 

3. $\pm\frac{1}{\sqrt{17}}(3i-2j-2k)$ . 

4.5 880 J. 

5. $|\mathbf{F}_1|x_1\sin \theta_1 = |\mathbf{F}_2|x_2\sin \theta_2.$ 

6.2. 

7. $\lambda = 2\mu$ 

8. 略.

9. (1) $-8j - 24k$ ; (2) $-j - k$ ; (3) 2. 

10.5. 

11—13. 略.

# 习题8-3（第29页）

1. $3x-7y+5z-4=0.$ 

2. $2x + 9y - 6z - 121 = 0.$ 

3. x-3y-2z=0. 

4. 图略.(1) yOz 面; (2) 平行于 zOx 面的平面; (3) 平行于 z 轴的平面;

(4) 通过 z 轴的平面；(5) 平行于 x 轴的平面；(6) 通过 y 轴的平面；

(7) 通过原点的平面.

5. $\frac{1}{3},\frac{2}{3},-\frac{2}{3}.$ 

6. $4x + 7y + 16z - 2 = 0.$ 

7. $(1,-1,3)$ . 

8. (1) $y+5=0$ ; (2) $x+3y=0$ ; (3) 9y-z-2=0. 

9.1. 

# 习题8-4（第35页）

1. $\frac{x - 4}{2} = \frac{y + 1}{1} = \frac{z - 3}{5}$ . 

2. $\frac{x - 3}{-4} = \frac{y + 2}{2} = \frac{z - 1}{1}$ . 

3. \(\frac{x - 1}{-2} = \frac{y - 1}{1} = \frac{z - 1}{3},\) \(\left\{ \begin{array}{l}x = 1 - 2t,\\ y = 1 + t,(t\) 为任意常数).\\ z = 1 + 3t \end{array} \right.\)

4. 16x-14y-11z-65=0. 

5. cos φ = 0. 

6. 略.

7. $\frac{x - 1}{2} = \frac{y}{-1} = \frac{z + 2}{2}$ . 

8. 8x-9y-22z-59=0. 

9. $\varphi = 0$ . 

10.（1）平行；（2）垂直；（3）直线在平面上.

11. $x-y+z=0.$ 

12. $\left(-\frac{5}{3},\frac{2}{3},\frac{2}{3}\right)$ . 

13. $\frac{3\sqrt{2}}{2}$ . 

14. 略.

15. $\left\{ \begin{array}{l} 17x + 31y - 37z - 117 = 0, \\ 4x - y + z - 1 = 0. \end{array} \right.$ 

16. 略.

# 习题8-5（第43页）

1. $x^{2} + y^{2} + z^{2} - 4x - 2y + 4z = 0$ ，球心为 $(2,1, - 2)$ ， $R = 3$ 

2. $(x - 3)^{2} + (y + 5)^{2} + (z - 2)^{2} = \frac{338}{7}$ . 

3. 以点 $(1, -2, -1)$ 为球心, 半径为 $\sqrt{6}$ 的球面.

4. $\left(x + \frac{2}{3}\right)^2 + (y + 1)^2 + \left(z + \frac{4}{3}\right)^2 = \frac{116}{9}$ , 它表示一球面, 球心为 $\left(-\frac{2}{3}, -1, -\frac{4}{3}\right)$ , 半径为 $\frac{2}{3} \sqrt{29}$ .

5. $y^{2}+z^{2}=5x.$ 

6. $x^{2}+y^{2}+z^{2}=9.$ 

7. 绕 x 轴: $4x^{2}-9(y^{2}+z^{2})=36$ , 绕 y 轴: $4(x^{2}+z^{2})-9y^{2}=36$ .

8—9. 略.

10.（1） $xOy$ 面上的椭圆 $\frac{x^2}{4} +\frac{y^2}{9} = 1$ 绕 $x$ 轴旋转一周；

(2) xOy 面上的双曲线 $x^{2}-\frac{y^{2}}{4}=1$ 绕 y 轴旋转一周；

(3) xOy 面上的双曲线 $x^{2}-y^{2}=1$ 绕 x 轴旋转一周；

(4) yOz 面上的直线 $z=y+a$ 绕 z 轴旋转一周.

注:本题各小题均有多个答案,以上给出的均是其中一个答案.

11—12. 略.

# 习题8-6（第49页）

1—2. 略.

3. 母线平行于 $x$ 轴的柱面方程为 $3y^{2} - z^{2} = 16$ ,

母线平行于 y 轴的柱面方程为 $3x^{2}+2z^{2}=16$ .

4. (1) $\left\{ \begin{array}{l} 2x^{2} - 2x + y^{2} = 8, \\ z = 0; \end{array} \right.$ (2) $\left\{ \begin{array}{l} x^{2} + y^{2} = \frac{1}{5}, \\ z = 0. \end{array} \right.$ 

5. (1) $\left\{ \begin{array}{l} x = \frac{3}{\sqrt{2}} \cos t, \\ y = \frac{3}{\sqrt{2}} \cos t, (0 \leqslant t \leqslant 2\pi); \\ z = 3 \sin t \end{array} \right.$ (2) $\left\{ \begin{array}{l} x = 1 + \sqrt{3} \cos \theta, \\ y = \sqrt{3} \sin \theta, \\ z = 0 \end{array} \right.$ ( $0 \leqslant \theta \leqslant 2\pi$ ). 

6. $\left\{ \begin{array}{l} x^{2} + y^{2} = a^{2}, \\ z = 0, \end{array} \right.$ $\left\{ \begin{array}{l} y = a\sin \frac{z}{b}, \\ x = 0, \end{array} \right.$ $\left\{ \begin{array}{l} x = a\cos \frac{z}{b}, \\ y = 0. \end{array} \right.$ 

7. $x^{2} + y^{2}\leqslant ax;x^{2} + z^{2}\leqslant a^{2},x\geqslant 0,z\geqslant 0.$ 

8. $x^{2} + y^{2}\leqslant 4,x^{2}\leqslant z\leqslant 4,y^{2}\leqslant z\leqslant 4.$ 

# 总习题八（第50页）

1. (1) $M(x - x_0, y - y_0, z - z_0), \overrightarrow{OM} = (x, y, z)$ ; (2) 共面; (3) 3; (4) 36.

2. (1) (A); (2) (B). 

3. $(0,2,0)$ . 

4. $\sqrt{30}$ . 

5. $\overrightarrow{AD} = c + \frac{1}{2} a, \overrightarrow{BE} = a + \frac{1}{2} b, \overrightarrow{CF} = b + \frac{1}{2} c.$ 

6. 略.

7.1. 

8. $\arccos \frac{2}{\sqrt{7}}$ 

9. $\frac{\pi}{3}.$ 

10. $c = (x,2 - 2x,2x - 1)$ ，其中 $x$ 为参数；模为最小的 $c = \left(\frac{2}{3},\frac{2}{3},\frac{1}{3}\right)$ 

11. 30. 

12. (14,10,2). 

13. $c=5a+b.$ 

14. $4(z - 1) = (x - 1)^2 +(y + 1)^2.$ 

15. (1) $\left\{ \begin{array}{l} x = 0, \\ z = 2y^{2}, \end{array} \right.$ $z$ 轴； (2) $\left\{ \begin{array}{l} x = 0, \\ \frac{y^2}{9} + \frac{z^2}{36} = 1, \end{array} \right.$ $y$ 轴；

(3) $\left\{ \begin{array}{l} x = 0, \\ z = \sqrt{3} y, \end{array} \right.$ $z$ 轴； (4) $\left\{ \begin{array}{l} z = 0, \\ x^2 - \frac{y^2}{4} = 1, \end{array} \right.$ $x$ 轴.

16. $x + \sqrt{26} y + 3z - 3 = 0$ 或 $x - \sqrt{26} y + 3z - 3 = 0.$ 

17. $x+2y+1=0.$ 

18. $\frac{x + 1}{16} = \frac{y}{19} = \frac{z - 4}{28}$ . 

19. $\frac{x + 3}{1} = \frac{y - 5}{22} = \frac{z + 9}{2}$ . 

20. $\left(0,0,\frac{1}{5}\right)$ . 

21. $\left\{ \begin{array}{l} x^{2} + y^{2} = x + y, \\ z = 0, \end{array} \right.$ $\left\{ \begin{array}{l} 2y^{2} + 2yz + z^{2} - 4y - 3z + 2 = 0, \\ x = 0, \end{array} \right.$ $\left\{ \begin{array}{l} 2x^{2} + 2xz + z^{2} - 4x - 3z + 2 = 0, \\ y = 0. \end{array} \right.$ 

22. $\left\{ \begin{array}{l}(x - 1)^2 +y^2\leqslant 1,\\ z = 0, \end{array} \right.$ $\left\{ \begin{array}{ll}\left(\frac{z^2}{2} -1\right)^2 +y^2\leqslant 1,z\geqslant 0, & \left\{ \begin{array}{ll}x\leqslant z\leqslant \sqrt{2x},\\ y = 0. \end{array} \right. \end{array} \right.$ 

23. 略.

# 第九章

# 习题9-1（第62页）

1.（1）开集，无界集，导集： $\mathbb{R}^2$ ，边界： $\{(x,y)\mid x = 0$ 或 $y = 0\}$ 

(2) 既非开集, 又非闭集, 有界集, 导集: $\{(x, y) \mid 1 \leqslant x^2 + y^2 \leqslant 4\}$ ,

边界： $\{(x,y)\mid x^{2}+y^{2}=1\}\cup\{(x,y)\mid x^{2}+y^{2}=4\}$ ;

(3) 开集, 区域, 无界集, 导集: $\{(x,y) \mid y \geqslant x^{2}\}$ , 边界: $\{(x,y) \mid y = x^{2}\}$ ;

(4) 闭集,有界集,导集:集合本身,

边界： $\{(x,y)\mid x^2 +(y - 1)^2 = 1\} \cup \{(x,y)\mid x^2 +(y - 2)^2 = 4\}$ 

2. $t^{2}f(x,y)$ . 

3. 略.

4. $(x+y)^{xy}+(xy)^{2x}.$ 

5. (1) $\{(x,y)\mid y^{2}-2x+1>0\}$ ; 

(2) $\{(x,y)\mid x+y>0,x-y>0\}$ ; 

(3) $\{(x, y) | x \geqslant 0, y \geqslant 0, x^2 \geqslant y\}$ ; 

(4) $\{(x, y) | y - x > 0, x \geqslant 0, x^2 + y^2 < 1\}$ ; 

(5) $\{(x, y, z) | r^2 < x^2 + y^2 + z^2 \leqslant R^2\}$ ; 

(6) $\{(x,y,z)\mid x^2 +y^2 -z^2\geqslant 0,x^2 +y^2\neq 0\}$ . 

6. (1) 1; (2) $\ln 2$ ; (3) $-\frac{1}{4}$ ; (4) -2; (5) 2; (6) 0. 

*7. 略.

8. $\{(x,y)\mid y^{2}-2x=0\}$ . 

*9. 提示： $|xy| \leqslant \frac{x^{2} + y^{2}}{2}$ 

*10. 略.

# 习题9-2（第68页）

1. $f_{x}(0,0)$ 不存在， $f_{y}(0,0) = 0$ .

2. (1) $\frac{\partial z}{\partial x} = 3x^{2}y - y^{3}, \frac{\partial z}{\partial y} = x^{3} - 3xy^{2}$ ; 

(2) $\frac{\partial s}{\partial u} = \frac{1}{v} - \frac{v}{u^2}, \frac{\partial s}{\partial v} = \frac{1}{u} - \frac{u}{v^2};$ 

(3) $\frac{\partial z}{\partial x} = \frac{1}{2x\sqrt{\ln(xy)}}$ , $\frac{\partial z}{\partial y} = \frac{1}{2y\sqrt{\ln(xy)}}$ ; 

(4) $\frac{\partial z}{\partial x} = y[\cos (xy) - \sin (2xy)]$ ， $\frac{\partial z}{\partial y} = x[\cos (xy) - \sin (2xy)]$ ； 

(5) $\frac{\partial z}{\partial x} = \frac{2}{y}\csc \frac{2x}{y},\frac{\partial z}{\partial y} = -\frac{2x}{y^2}\csc \frac{2x}{y};$ 

(6) $\frac{\partial z}{\partial x} = y^2 (1 + xy)^{y - 1},\frac{\partial z}{\partial y} = (1 + xy)^y\left[\ln (1 + xy) + \frac{xy}{1 + xy}\right];$ 

(7) $\frac{\partial u}{\partial x} = \frac{y}{z} x^{\frac{y}{z} - 1}, \frac{\partial u}{\partial y} = \frac{1}{z} x^{\frac{y}{z}} \cdot \ln x, \frac{\partial u}{\partial z} = -\frac{y}{z^2} x^{\frac{y}{z}} \cdot \ln x;$ 

(8) $\frac{\partial u}{\partial x} = \frac{z(x - y)^{z - 1}}{1 + (x - y)^{2z}}, \frac{\partial u}{\partial y} = -\frac{z(x - y)^{z - 1}}{1 + (x - y)^{2z}}, \frac{\partial u}{\partial z} = \frac{(x - y)^z \ln(x - y)}{1 + (x - y)^{2z}}.$ 

3—4. 略.

5. $f_{x}(x,1) = 1$ 

6. $\frac{\pi}{4}.$ 

7. (1) $\frac{\partial^2z}{\partial x^2} = 12x^2 - 8y^2, \frac{\partial^2z}{\partial y^2} = 12y^2 - 8x^2, \frac{\partial^2z}{\partial x\partial y} = -16xy;$ 

(2) $\frac{\partial^2z}{\partial x^2} = \frac{2xy}{(x^2 + y^2)^2}, \frac{\partial^2z}{\partial y^2} = -\frac{2xy}{(x^2 + y^2)^2}, \frac{\partial^2z}{\partial x\partial y} = \frac{y^2 - x^2}{(x^2 + y^2)^2};$ 

(3) $\frac{\partial^2z}{\partial x^2} = y^x\ln^2 y, \frac{\partial^2z}{\partial y^2} = x(x - 1)y^{x - 2}, \frac{\partial^2z}{\partial x\partial y} = y^{x - 1}(1 + x\ln y).$ 

8. $f_{xx}(0,0,1) = 2,f_{xz}(1,0,2) = 2,f_{yz}(0, - 1,0) = 0,f_{zzx}(2,0,1) = 0.$ 

9. $\frac{\partial^3z}{\partial x^2\partial y} = 0,\frac{\partial^3z}{\partial x\partial y^2} = -\frac{1}{y^2}.$ 

10. 略.

# 习题9-3（第75页）

1. (1) $\left(y + \frac{1}{y}\right)\mathrm{d}x + x\left(1 - \frac{1}{y^2}\right)\mathrm{d}y;$ 

(2) $-\frac{1}{x}\mathrm{e}^{\frac{x}{x}}\left(\frac{y}{x}\mathrm{d}x - \mathrm{d}y\right)$ ; 

(3) $-\frac{x}{\left(x^{2}+y^{2}\right)^{3/2}}(ydx-xdy)$ ; 

(4) $yzx^{yz-1}dx + zx^{yz}\ln xdy + yx^{yz}\ln xdz.$ 

2. $\frac{1}{3}dx+\frac{2}{3}dy.$ 

3. $\Delta z = -0.119$ , dz = -0.125. 

4. 0.25e. 

5. (A). 

*6. 2.95. 

*7. 2.039. 

*8. -5 cm. 

*9. 55.3 cm $^{3}$ . 

*10. 0.124 cm. 

*11. 2 128 m², 27.6 m², 1.30%. 

*12—*13. 略.

# 习题9-4（第81页）

1. $\frac{\partial z}{\partial x} = 4x, \frac{\partial z}{\partial y} = 4y.$ 

2. $\frac{\partial z}{\partial x} = \frac{2x}{y^2}\ln (3x - 2y) + \frac{3x^2}{(3x - 2y)y^2},\quad \frac{\partial z}{\partial y} = -\frac{2x^2}{y^3}\ln (3x - 2y) - \frac{2x^2}{(3x - 2y)y^2}.$ 

3. $e^{\sin t-2t^{3}}(\cos t-6t^{2})$ . 

4. $\frac{3(1 - 4t^2)}{\sqrt{1 - (3t - 4t^3)^2}}.$ 

5. $\frac{e^{x}(1+x)}{1+x^{2}e^{2x}}$ . 

6. $e^{ax}\sin x.$ 

7. 略.

8. (1) $\frac{\partial u}{\partial x} = 2xf_1' + y\mathrm{e}^{xy}f_2'$ , $\frac{\partial u}{\partial y} = -2yf_1' + x\mathrm{e}^{xy}f_2'$ ; 

(2) $\frac{\partial u}{\partial x} = \frac{1}{y} f_1'$ , $\frac{\partial u}{\partial y} = -\frac{x}{y^2} f_1' + \frac{1}{z} f_2'$ , $\frac{\partial u}{\partial z} = -\frac{y}{z^2} f_2'$ ; 

(3) $\frac{\partial u}{\partial x} = f_1' + yf_2' + yzf_3'$ , $\frac{\partial u}{\partial y} = xf_2' + xzf_3'$ , $\frac{\partial u}{\partial z} = xyf_3'$ . 

9—11. 略.

12. $\frac{\partial^2z}{\partial x^2} = 2f' + 4x^2 f'', \frac{\partial^2z}{\partial x\partial y} = 4xyf'', \frac{\partial^2z}{\partial y^2} = 2f' + 4y^2 f''.$ 

* 13. (1) $\frac{\partial^2z}{\partial x^2} = y^2 f_{11}''$ , $\frac{\partial^2z}{\partial x\partial y} = f_1' + y(xf_{11}' + f_{12}'')$ , $\frac{\partial^2z}{\partial y^2} = x^2 f_{11}'' + 2xf_{12}' + f_{22}''$ ; 

(2) $\frac{\partial^2z}{\partial x^2} = f_{11}'' + \frac{2}{y} f_{12}'' + \frac{1}{y^2} f_{22}''$ ， $\frac{\partial^2z}{\partial x\partial y} = -\frac{x}{y^2}\left(f_{12}'' + \frac{1}{y} f_{22}''\right) - \frac{1}{y^2} f_2'$ ， 

$$
\frac {\partial^ {2} z}{\partial y ^ {2}} = \frac {2 x}{y ^ {3}} f _ {2} ^ {\prime} + \frac {x ^ {2}}{y ^ {4}} f _ {2 2} ^ {\prime \prime};
$$

(3) $\frac{\partial^2z}{\partial x^2} = 2yf'_2 + y^4f''_{11} + 4xy^3f''_{12} + 4x^2y^2f''_{22}$ , 

$$
\frac {\partial^ {2} z}{\partial x \partial y} = 2 y f _ {1} ^ {\prime} + 2 x f _ {2} ^ {\prime} + 2 x y ^ {3} f _ {1 1} ^ {\prime \prime} + 2 x ^ {3} y f _ {2 2} ^ {\prime \prime} + 5 x ^ {2} y ^ {2} f _ {1 2} ^ {\prime \prime},
$$

$$
\frac {\partial^ {2} z}{\partial y ^ {2}} = 2 x f _ {1} ^ {\prime} + 4 x ^ {2} y ^ {2} f _ {1 1} ^ {\prime \prime} + 4 x ^ {3} y f _ {1 2} ^ {\prime \prime} + x ^ {4} f _ {2 2} ^ {\prime \prime};
$$

(4) $\frac{\partial^2z}{\partial x^2} = e^{x + y}f_3' - \sin xf_1' + \cos^2 xf_{11}' + 2e^{x + y}\cos xf_{13}' + e^{2(x + y)}f_{33}'$ 

$$
\frac {\partial^ {2} z}{\partial x \partial y} = e ^ {x + y} f _ {3} ^ {\prime} - \cos x \sin y f _ {1 2} ^ {\prime \prime} + e ^ {x + y} \cos x f _ {1 3} ^ {\prime \prime} - e ^ {x + y} \sin y f _ {3 2} ^ {\prime \prime} + e ^ {2 (x + y)} f _ {3 3} ^ {\prime \prime},
$$

$$
\frac {\partial^ {2} z}{\partial y ^ {2}} = \mathrm{e} ^ {x + y} f _ {3} ^ {\prime} - \cos \gamma f _ {2} ^ {\prime} + \sin^ {2} \gamma f _ {2 2} ^ {\prime \prime} - 2 \mathrm{e} ^ {x + y} \sin \gamma f _ {2 3} ^ {\prime \prime} + \mathrm{e} ^ {2 (x + y)} f _ {3 3} ^ {\prime \prime}.
$$

*14. 略.

# 习题9-5（第88页）

1. $\frac{y^2 - e^x}{\cos y - 2xy}$ 

2. $\frac{x+y}{x-y}.$ 

3. $\frac{\partial z}{\partial x} = \frac{yz - \sqrt{xyz}}{\sqrt{xyz} - xy}, \frac{\partial z}{\partial y} = \frac{xz - 2\sqrt{xyz}}{\sqrt{xyz} - xy}$ . 

4. $\frac{\partial z}{\partial x} = \frac{z}{x + z}, \frac{\partial z}{\partial y} = \frac{z^2}{y(x + z)}.$ 

5—7. 略.

8. $\mathrm{dz} = -\frac{z}{x}\mathrm{dx} + \frac{z(2xyz - 1)}{y(2xz - 2xyz + 1)}\mathrm{dy}.$ 

*9. $\frac{2y^{2}ze^{z}-2xy^{3}z-y^{2}z^{2}e^{z}}{(e^{z}-xy)^{3}}$ . 

*10. $\frac{z(z^4 - 2xyz^2 - x^2y^2)}{(z^2 - xy)^3}$ . 

11. (1) $\frac{\mathrm{dy}}{\mathrm{dx}} = -\frac{x(6z + 1)}{2y(3z + 1)}, \frac{\mathrm{dz}}{\mathrm{dx}} = \frac{x}{3z + 1}$ ; 

(2) $\frac{\mathrm{d}x}{\mathrm{d}z} = \frac{y - z}{x - y}, \frac{\mathrm{d}y}{\mathrm{d}z} = \frac{z - x}{x - y};$ 

(3) $\frac{\partial u}{\partial x} = \frac{-uf_1'(2yvg_2' - 1) - f_2'g_1'}{(xf_1' - 1)(2yvg_2' - 1) - f_2'g_1'}$ 

$$
\frac {\partial v}{\partial x} = \frac {g _ {1} ^ {\prime} (x f _ {1} ^ {\prime} + u f _ {1} ^ {\prime} - 1)}{(x f _ {1} ^ {\prime} - 1) (2 y v g _ {2} ^ {\prime} - 1) - f _ {2} ^ {\prime} g _ {1} ^ {\prime}};
$$

(4) $\frac{\partial u}{\partial x} = \frac{\sin v}{e^u (\sin v - \cos v) + 1}, \frac{\partial u}{\partial y} = \frac{-\cos v}{e^u (\sin v - \cos v) + 1},$ 

$$
\frac {\partial v}{\partial x} = \frac {\cos v - e ^ {u}}{u [ e ^ {u} (\sin v - \cos v) + 1 ]}, \frac {\partial v}{\partial y} = \frac {\sin v + e ^ {u}}{u [ e ^ {u} (\sin v - \cos v) + 1 ]}.
$$

12. 略.

# 习题9-6（第99页）

1. 略.

2. (1) $\boldsymbol{v}_0 = i + 2j + 2k, a_0 = 2j, |\boldsymbol{v}(t)| = \sqrt{5 + 4t^2}$ ; 

(2) $v_{0}=-2i+4k,a_{0}=-3j,\left|v(t)\right|=\sqrt{20+5\cos^{2}t};$ 

(3) $v_{0}=i+2j+k, a_{0}=-\frac{1}{2}i+2j+k, |v(t)|=\sqrt{5t^{2}+\frac{4}{(t+1)^{2}}}$ . 

3. 切线方程: $\frac{x - \left(\frac{\pi}{2} - 1\right)}{1} = \frac{y - 1}{1} = \frac{z - 2\sqrt{2}}{\sqrt{2}}$ ,

法平面方程: $x+y+\sqrt{2}z=\frac{\pi}{2}+4.$ 

4. 切线方程: $\frac{x - \frac{1}{2}}{1} = \frac{y - 2}{-4} = \frac{z - 1}{8}$ , 法平面方程: $2x - 8y + 16z - 1 = 0$ .

5. 切线方程: $\frac{x - x_0}{1} = \frac{y - y_0}{\frac{m}{y_0}} = \frac{z - z_0}{- \frac{1}{2z_0}}$ ,

法平面方程： $(x - x_0) + \frac{m}{y_0} (y - y_0) - \frac{1}{2z_0} (z - z_0) = 0.$ 

6. 切线方程: $\frac{x-1}{16}=\frac{y-1}{9}=\frac{z-1}{-1}$ ，法平面方程: $16x+9y-z-24=0$ .

7. $P_{1}(-1,1, - 1)$ 及 $P_{2}\left(-\frac{1}{3},\frac{1}{9}, - \frac{1}{27}\right).$ 

8. 切平面方程: $x+2y-4=0$ , 法线方程: $\left\{\begin{aligned}\frac{x-2}{1}&=\frac{y-1}{2},\\ z&=0.\end{aligned}\right.$ 

9. 切平面方程: $ax_{0}x + by_{0}y + cz_{0}z = 1$ , 法线方程: $\frac{x - x_{0}}{ax_{0}} = \frac{y - y_{0}}{by_{0}} = \frac{z - z_{0}}{cz_{0}}$ .

10. 切平面方程: $x-y+2z=\pm\sqrt{\frac{11}{2}}$ .

11. 切平面方程: $9x + y - z - 27 = 0$ 或 $9x + 17y - 17z + 27 = 0$ .

12. 切线的参数方程: $x=2+t, y=1, z=9+12t, t$ 为参数.

13. $\cos \gamma = \frac{3}{\sqrt{22}}.$ 

14—15. 略.

# 习题9-7（第107页）

1. $1 + 2\sqrt{3}$ . 

2. $\frac{\sqrt{2}}{3}$ . 

3. $\frac{1}{ab}\sqrt{2(a^2 + b^2)}$ 

4.5. 

5. $\frac{98}{13}$ 

6. $\frac{6}{7}\sqrt{14}$ . 

7. $x_{0}+y_{0}+z_{0}.$ 

8. $\text{grad } f(0,0,0)=3i-2j-6k$ , $\text{grad } f(1,1,1)=6i+3j$ . 

9. 略.

10. 增加最快的方向为 $n = \frac{1}{\sqrt{21}} (2i - 4j + k)$ , 方向导数为 $\sqrt{21}$ ;

减少最快的方向为 $-n=\frac{1}{\sqrt{21}}(-2i+4j-k)$ ，方向导数为 $-\sqrt{21}$ .

# 习题9-8（第117页）

1. (A). 

2. 极大值: $f(2,-2)=8$ .

3. 极大值: $f(3,2)=36$ .

4. 最短距离为 $\frac{\sqrt{2}}{2}$ .

5. 极大值: $z\left(\frac{1}{2}, \frac{1}{2}\right) = \frac{1}{4}$ .

6. 当两直角边都是 $\frac{l}{\sqrt{2}}$ 时, 可得最大的周长.

7. 当长、宽都是 $\sqrt[3]{2k}$ ，而高为 $\frac{1}{2}\sqrt[3]{2k}$ 时，水池的表面积最小.

8. $\left(\frac{8}{5},\frac{16}{5}\right)$ . 

9. 当矩形的边长分别为 $\frac{2p}{3}$ 及 $\frac{p}{3}$ 时, 绕短边旋转所得圆柱体的体积最大.

10. 当长、宽、高都是 $\frac{2a}{\sqrt{3}}$ 时,可得最大的体积.

11. 最大值为 $\sqrt{9 + 5\sqrt{3}}$ ，最小值为 $\sqrt{9 - 5\sqrt{3}}$ .

12. 最热点在 $\left(-\frac{1}{2}, \pm \frac{\sqrt{3}}{2}\right)$ , 最冷点在 $\left(\frac{1}{2}, 0\right)$ .

13. 最热点在 $\left(\pm \frac{4}{3}, -\frac{4}{3}, -\frac{4}{3}\right)$ .

# *习题9-9（第123页）

$$
f (x, y) = 5 + 2 (x - 1) ^ {2} - (x - 1) (y + 2) - (y + 2) ^ {2}.
$$

2. $\mathrm{e}^x\ln (1 + y) = y + \frac{1}{2!} (2xy - y^2) + \frac{1}{3!} (3x^2y - 3xy^2 + 2y^3) + R_3$ ，其中

$$
R _ {3} = \frac {\mathrm{e} ^ {\theta x}}{2 4} \left[ x ^ {4} \ln (1 + \theta y) + \frac {4 x ^ {3} y}{1 + \theta y} - \frac {6 x ^ {2} y ^ {2}}{(1 + \theta y) ^ {2}} + \frac {8 x y ^ {3}}{(1 + \theta y) ^ {3}} - \frac {6 y ^ {4}}{(1 + \theta y) ^ {4}} \right] (0 <   \theta <   1).
$$

3. $\sin x\sin y = \frac{1}{2} +\frac{1}{2}\left(x - \frac{\pi}{4}\right) + \frac{1}{2}\left(y - \frac{\pi}{4}\right) - \frac{1}{4}\left[\left(x - \frac{\pi}{4}\right)^2 -2\left(x - \frac{\pi}{4}\right)\left(y - \frac{\pi}{4}\right) + \left(y - \frac{\pi}{4}\right)^2\right] + R_2,$ 

其中 $R_{2} = -\frac{1}{6}\left[\cos \xi \sin \eta \left(x - \frac{\pi}{4}\right)^{3} + 3\sin \xi \cos \eta \left(x - \frac{\pi}{4}\right)^{2}\left(y - \frac{\pi}{4}\right) + \right.$ 

$$
3 \cos \xi \sin \eta \left(x - \frac {\pi}{4}\right) \left(y - \frac {\pi}{4}\right) ^ {2} + \sin \xi \cos \eta \left(y - \frac {\pi}{4}\right) ^ {3} ],
$$

且 $\xi=\frac{\pi}{4}+\theta\left(x-\frac{\pi}{4}\right)$ , $\eta=\frac{\pi}{4}+\theta\left(y-\frac{\pi}{4}\right)$ (0<θ<1).

4. $x^{y}=1+(x-1)+(x-1)(y-1)+\frac{1}{2}(x-1)^{2}(y-1)+R_{3},1.1^{1.02}\approx1.102$ 

5. $\mathrm{e}^{x+y}=1+(x+y)+\frac{1}{2!}(x^{2}+2xy+y^{2})+\cdots+\frac{1}{n!}(x^{n}+\mathrm{C}_{n}^{1}x^{n-1}y+\cdots+y^{n})+R_{n}$ 

其中 $R_{n}=\frac{\mathrm{e}^{\theta(x+y)}}{(n+1)!}(x^{n+1}+\mathrm{C}_{n+1}^{1}x^{n}y+\cdots+y^{n+1})$ ， $0<\theta<1$ .

# *习题9-10（第127页）

1. $\theta = 2.234p + 95.33$ . 

$$
2. \left\{ \begin{array}{l} a \sum_ {i = 1} ^ {n} x _ {i} ^ {4} + b \sum_ {i = 1} ^ {n} x _ {i} ^ {3} + c \sum_ {i = 1} ^ {n} x _ {i} ^ {2} = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} y _ {i}, \\ a \sum_ {i = 1} ^ {n} x _ {i} ^ {3} + b \sum_ {i = 1} ^ {n} x _ {i} ^ {2} + c \sum_ {i = 1} ^ {n} x _ {i} = \sum_ {i = 1} ^ {n} x _ {i} y _ {i}, \\ a \sum_ {i = 1} ^ {n} x _ {i} ^ {2} + b \sum_ {i = 1} ^ {n} x _ {i} + n c = \sum_ {i = 1} ^ {n} y _ {i}. \end{array} \right.
$$

# 总习题九（第127页）

1.（1）充分，必要；（2）必要，充分；（3）充分；（4）充分.

2. (C). 

3. $\{(x,y) | 0 < x^2 + y^2 < 1, y^2 \leqslant 4x\}$ , $\frac{\sqrt{2}}{\ln \frac{3}{4}}$ . 

*4. 略.

$$
f _ {x} (x, y) = \left\{ \begin{array}{l l} \frac {2 x y ^ {3}}{(x ^ {2} + y ^ {2}) ^ {2}}, & x ^ {2} + y ^ {2} \neq 0, \\ 0, & x ^ {2} + y ^ {2} = 0; \end{array} \right.
$$

$$
f _ {y} (x, y) = \left\{ \begin{array}{l l} \frac {x ^ {2} (x ^ {2} - y ^ {2})}{(x ^ {2} + y ^ {2}) ^ {2}}, & x ^ {2} + y ^ {2} \neq 0, \\ 0, & x ^ {2} + y ^ {2} = 0. \end{array} \right.
$$

$$
\frac {\partial z}{\partial x} = \frac {1}{x + y ^ {2}}, \frac {\partial z}{\partial y} = \frac {2 y}{x + y ^ {2}}, \frac {\partial^ {2} z}{\partial x ^ {2}} = - \frac {1}{(x + y ^ {2}) ^ {2}}, \tag {6.(1)}
$$

$$
\frac {\partial^ {2} z}{\partial x \partial y} = - \frac {2 y}{(x + y ^ {2}) ^ {2}}, \frac {\partial^ {2} z}{\partial y ^ {2}} = \frac {2 (x - y ^ {2})}{(x + y ^ {2}) ^ {2}};
$$

$$
\frac {\partial z}{\partial x} = y x ^ {y - 1}, \frac {\partial z}{\partial y} = x ^ {y} \ln x, \frac {\partial^ {2} z}{\partial x ^ {2}} = y (y - 1) x ^ {y - 2}, \tag {2}
$$

$$
\frac {\partial^ {2} z}{\partial x \partial y} = x ^ {y - 1} (1 + y \ln x), \frac {\partial^ {2} z}{\partial y ^ {2}} = x ^ {y} (\ln x) ^ {2}.
$$

$$
7. \Delta z = 0. 0 3, \mathrm{d} z = 0. 0 3.
$$

*8. 略.

$$
\frac {\mathrm{d} u}{\mathrm{d} t} = y x ^ {y - 1} \varphi^ {\prime} (t) + x ^ {y} \ln x \psi^ {\prime} (t). \tag {9}
$$

$$
\frac {\partial z}{\partial \xi} = - \frac {\partial z}{\partial v} + \frac {\partial z}{\partial w}, \quad \frac {\partial z}{\partial \eta} = \frac {\partial z}{\partial u} - \frac {\partial z}{\partial w}, \quad \frac {\partial z}{\partial \zeta} = - \frac {\partial z}{\partial u} + \frac {\partial z}{\partial v},
$$

$$
\frac {\partial^ {2} z}{\partial x \partial y} = x \mathrm{e} ^ {2 y} f _ {u u} ^ {\prime \prime} + \mathrm{e} ^ {y} f _ {u y} ^ {\prime \prime} + x \mathrm{e} ^ {y} f _ {x u} ^ {\prime \prime} + f _ {x y} ^ {\prime \prime} + \mathrm{e} ^ {y} f _ {u} ^ {\prime},
$$

$$
\frac {\partial z}{\partial x} = (v \cos v - u \sin v) e ^ {- u}, \frac {\partial z}{\partial y} = (u \cos v + v \sin v) e ^ {- u}.
$$

$$
1 3. \text { 切线方程: } \left\{ \begin{array}{l l} x = a, \\ b y - a z = 0, \end{array} \right. \quad \text { 法平面方程: } a y + b z = 0.
$$

$$
(- 3, - 1, 3), \frac {x + 3}{1} = \frac {y + 1}{3} = \frac {z - 3}{1}.
$$

$$
\frac {\partial f}{\partial l} = \cos \theta + \sin \theta , (1) \theta = \frac {\pi}{4}; (2) \theta = \frac {5 \pi}{4}; (3) \theta = \frac {3 \pi}{4} \text {或} \frac {7 \pi}{4}. \tag {15}
$$

$$
\frac {2}{\sqrt {\frac {x _ {0} ^ {2}}{a ^ {4}} + \frac {y _ {0} ^ {2}}{b ^ {4}} + \frac {z _ {0} ^ {2}}{c ^ {4}}}}.
$$

$$
1 7. \left(\frac {4}{5}, \frac {3}{5}, \frac {3 5}{1 2}\right).
$$

18. 切点 $\left(\frac{a}{\sqrt{3}}, \frac{b}{\sqrt{3}}, \frac{c}{\sqrt{3}}\right), V_{\min} = \frac{\sqrt{3}}{2} abc.$ 

19. 当 $p_{1}=80, p_{2}=120$ 时, 总利润最大, 最大总利润为 605.

20. (1) $g(x_0, y_0) = \sqrt{5x_0^2 + 5y_0^2 - 8x_0y_0}$ ; 

(2) 攀岩的起点可取为 $M_{1}(5,-5)$ 或 $M_{2}(-5,5)$ .

# 第十章

# 习题10-1（第135页）

1. $\iint_{D}\mu(x,y)\mathrm{d}\sigma.$ 

2. $I_{1} = 4I_{2}$ 

3. 略.

4. $D = \{(x,y)\mid 2x^{2} + y^{2}\leqslant 1\}$ 

5. (1) $\iint_{D} (x + y)^2 \, \mathrm{d}\sigma \geqslant \iint_{D} (x + y)^3 \, \mathrm{d}\sigma$ ; 

(2) $\iint_{D} (x + y)^{3} \mathrm{d}\sigma \geqslant \iint_{D} (x + y)^{2} \mathrm{d}\sigma$ ; 

(3) $\iint_{D} \ln (x + y) \, \mathrm{d}\sigma \geqslant \iint_{D} [\ln (x + y)]^2 \, \mathrm{d}\sigma$ ; 

(4) $\iint_{D} [\ln (x + y)]^2 \, \mathrm{d}\sigma \geqslant \iint_{D} \ln (x + y) \, \mathrm{d}\sigma.$ 

6. $2\pi$ . 

7. (1) $0 \leqslant I \leqslant 2$ ; (2) $0 \leqslant I \leqslant \pi^2$ ; (3) $2 \leqslant I \leqslant 8$ ; (4) $36\pi \leqslant I \leqslant 100\pi$ . 

# 习题10-2（第150页）

1. (1) $\frac{8}{3}$ ; (2) $\frac{20}{3}$ ; (3) 1; (4) $-\frac{3\pi}{2}$ ; (5) $\frac{\pi}{8} + \frac{1}{6}$ . 

2. (1) $\frac{6}{55}$ ; (2) $\frac{64}{15}$ ; (3) $e - e^{-1}$ ; (4) $\frac{13}{6}$ . 

3. 略.

4. (1) $\int_{0}^{4}\mathrm{d}x\int_{x}^{2\sqrt{x}}f(x,y)\mathrm{d}y$ 或 $\int_0^4\mathrm{d}y\int_{\frac{y^2}{4}}^y f(x,y)\mathrm{d}x;$ 

(2) $\int_{-r}^{r}\mathrm{d}x\int_{0}^{\sqrt{r^2 - x^2}}f(x,y)\mathrm{d}y$ 或 $\int_0^r\mathrm{d}y\int_{-\sqrt{r^2 - y^2}}^{\sqrt{r^2 - y^2}}f(x,y)\mathrm{d}x;$ 

(3) $\int_{1}^{2}\mathrm{d}x\int_{\frac{1}{x}}^{x}f(x,y)\mathrm{d}y$ 或 $\int_{\frac{1}{2}}^{1}\mathrm{d}y\int_{\frac{1}{y}}^{2}f(x,y)\mathrm{d}x + \int_{1}^{2}\mathrm{d}y\int_{y}^{2}f(x,y)\mathrm{d}x;$ 

(4) $\int_{-1}^{1}\mathrm{d}x\int_{\sqrt{1 - x^2}}^{\sqrt{4 - x^2}}f(x,y)\mathrm{d}y + \int_{-1}^{1}\mathrm{d}x\int_{-\sqrt{4 - x^2}}^{-\sqrt{1 - x^2}}f(x,y)\mathrm{d}y+$ 

$$
\int_ {- 2} ^ {- 1} \mathrm{d} x \int_ {- \sqrt {4 - x ^ {2}}} ^ {\sqrt {4 - x ^ {2}}} f (x, y) \mathrm{d} y + \int_ {1} ^ {2} \mathrm{d} x \int_ {- \sqrt {4 - x ^ {2}}} ^ {\sqrt {4 - x ^ {2}}} f (x, y) \mathrm{d} y
$$

或 $\int_{1}^{2}\mathrm{d}y\int_{-\sqrt{4 - y^2}}^{\sqrt{4 - y^2}}f(x,y)\mathrm{d}x + \int_{-2}^{-1}\mathrm{d}y\int_{-\sqrt{4 - y^2}}^{\sqrt{4 - y^2}}f(x,y)\mathrm{d}x+$ 

$$
\int_ {- 1} ^ {1} \mathrm{d} y \int_ {- \sqrt {4 - y ^ {2}}} ^ {- \sqrt {1 - y ^ {2}}} f (x, y) \mathrm{d} x + \int_ {- 1} ^ {1} \mathrm{d} y \int_ {\sqrt {1 - y ^ {2}}} ^ {\sqrt {4 - y ^ {2}}} f (x, y) \mathrm{d} x.
$$

5. 略.

6. (1) $\int_{0}^{1}\mathrm{d}x\int_{x}^{1}f(x,y)\mathrm{d}y;$ (2) $\int_0^4\mathrm{d}x\int_{\frac{x}{2}}^{\sqrt{x}}f(x,y)\mathrm{d}y;$ (3) $\int_{-1}^{1}\mathrm{d}x\int_{0}^{\sqrt{1 - x^2}}f(x,y)\mathrm{d}y;$ 

(4) $\int_0^1\mathrm{d}y\int_{2 - y}^{1 + \sqrt{1 - y^2}}f(x,y)\mathrm{d}x;$ (5) $\int_0^1\mathrm{d}y\int_{e^y}^e f(x,y)\mathrm{d}x;$ 

(6) $\int_{-1}^{0}\mathrm{d}y\int_{-2\arcsin y}^{\pi}f(x,y)\mathrm{d}x + \int_0^1\mathrm{d}y\int_{\arcsin y}^{\pi -\arcsin y}f(x,y)\mathrm{d}x.$ 

7. $\frac{4}{3}.$ 

8. $\frac{7}{2}.$ 

9. $\frac{17}{6}$ 

10. $6\pi$ . 

11. 图略.(1) $\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{a}f(\rho\cos\theta,\rho\sin\theta)\rho\mathrm{d}\rho;$ 

(2) $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_0^{2\cos \theta}f(\rho \cos \theta ,\rho \sin \theta)\rho \mathrm{d}\rho ;$ 

(3) $\int_{0}^{2\pi}\mathrm{d}\theta \int_{a}^{b}f(\rho \cos \theta ,\rho \sin \theta)\rho \mathrm{d}\rho ;$ 

(4) $\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{(\cos \theta +\sin \theta)^{-1}}f(\rho \cos \theta ,\rho \sin \theta)\rho \mathrm{d}\rho .$ 

12. (1) $\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{\sec \theta}f(\rho \cos \theta ,\rho \sin \theta)\rho \mathrm{d}\rho +\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{\csc \theta}f(\rho \cos \theta ,\rho \sin \theta)\rho \mathrm{d}\rho ;$ 

(2) $\int_{\frac{\pi}{4}}^{\frac{\pi}{3}}\mathrm{d}\theta \int_{0}^{2\sec \theta}f(\rho)\rho \mathrm{d}\rho ;$ (3) $\int_0^{\frac{\pi}{2}}\mathrm{d}\theta \int_{(\cos \theta +\sin \theta)^{-1}}^1 f(\rho \cos \theta ,\rho \sin \theta)\rho \mathrm{d}\rho ;$ 

(4) $\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{\sec \theta \tan \theta}^{\sec \theta}f(\rho \cos \theta ,\rho \sin \theta)\rho \mathrm{d}\rho .$ 

13. (1) $\frac{3}{4}\pi a^4$ ; (2) $\frac{1}{6}a^3[\sqrt{2} + \ln(1 + \sqrt{2})]$ ; (3) $\sqrt{2} - 1$ ; (4) $\frac{1}{8}\pi a^4$ . 

14. (1) $\pi(e^4 - 1)$ ; (2) $\frac{\pi}{4}(2\ln 2 - 1)$ ; (3) $\frac{3}{64}\pi^2$ . 

15. (1) $\frac{9}{4}$ ; (2) $\frac{\pi}{8} (\pi - 2)$ ; (3) $14a^4$ ; (4) $\frac{2}{3}\pi (b^3 - a^3)$ ; (5) $\frac{3\pi - 4}{9} a^3$ . 

16. $\frac{1}{40}\pi^{5}$ . 

17. $\frac{1}{3} R^3\arctan k.$ 

18. $\frac{3}{32}\pi a^4$ 

*19. (1) $\frac{\pi^4}{3}$ ; (2) $\frac{7}{3} \ln 2$ ; (3) $\frac{e-1}{2}$ ; (4) $\frac{1}{2} \pi ab$ , 提示: 作变换 $x = a\rho \cos \theta, y = b\rho \sin \theta$ .

*20. (1) $2 \ln 3$ ; (2) $\frac{1}{8}$ . 

*21. 略.

*22.（1）略；（2）提示：作变换 $x = \frac{au - bv}{\sqrt{a^2 + b^2}}$ ， $y = \frac{bu + av}{\sqrt{a^2 + b^2}}$ 

# 习题10-3（第160页）

1. (1) $\int_0^1\mathrm{d}x\int_0^{1 - x}\mathrm{d}y\int_0^{xy}f(x,y,z)\mathrm{d}z;$ 

(2) $\int_{-1}^{1}\mathrm{d}x\int_{-\sqrt{1 - x^2}}^{\sqrt{1 - x^2}}\mathrm{d}y\int_{x^2 + y^2}^1 f(x,y,z)\mathrm{d}z;$ 

(3) $\int_{-1}^{1}\mathrm{d}x\int_{-\sqrt{1 - x^2}}^{\sqrt{1 - x^2}}\mathrm{d}y\int_{x^2 + 2y^2}^{2 - x^2}f(x,y,z)\mathrm{d}z;$ 

(4) $\int_0^a\mathrm{d}x\int_0^{b\sqrt{1 - x^2 / a^2}}\mathrm{d}y\int_0^{xy / c}f(x,y,z)\mathrm{d}z.$ 

2. $\frac{3}{2}.$ 

3. 略.

4. $\frac{1}{364}$ . 

5. $\frac{1}{2}\left(\ln 2-\frac{5}{8}\right)$ . 

6. $\frac{1}{48}$ . 

7.0. 

8. $\frac{\pi}{4} h^2 R^2$ . 

9. (1) $\frac{7\pi}{12}$ ; (2) $\frac{16}{3}\pi$ . 

*10. (1) $\frac{4\pi}{5}$ ; (2) $\frac{7}{6}\pi a^4$ . 

11. (1) $\frac{1}{8}$ ; ${}^{*}(2)\frac{\pi}{10}$ ; (3) $8\pi$ ; ${}^{*}(4)\frac{4\pi}{15}(A^{5}-a^{5})$ ; (5) $\frac{4}{15}\pi$ . 

12. (1) $\frac{32}{3}\pi$ ; * (2) $\pi a^3$ ; (3) $\frac{\pi}{6}$ ; (4) $\frac{2}{3}\pi(5\sqrt{5}-4)$ . 

*13. $\frac{2}{3}\pi a^{3}$ . 

14. $\frac{8\sqrt{2}-7}{6}\pi.$ 

*15. $k\pi R^4$ 

# 习题10-4（第170页）

1. $2a^{2}(\pi-2)$ . 

2. $\sqrt{2}\pi$ . 

3. $16R^{2}$ 

4. $\frac{4}{3}R.$ 

5. (1) $\overline{x} = \frac{3}{5} x_0, \overline{y} = \frac{3}{8} y_0$ ; (2) $\overline{x} = 0, \overline{y} = \frac{4b}{3\pi}$ ; (3) $\overline{x} = \frac{b^2 + ab + a^2}{2(a + b)}, \overline{y} = 0.$ 

6. $\bar{x}=\frac{35}{48}$ , $\bar{y}=\frac{35}{54}$ . 

7. $\bar{x}=\frac{2}{5}a,\quad\bar{y}=\frac{2}{5}a.$ 

8. (1) $\left(0,0,\frac{3}{4}\right)$ ; * (2) $\left(0,0,\frac{3(A^4 - a^4)}{8(A^3 - a^3)}\right)$ ; (3) $\left(\frac{2}{5} a, \frac{2}{5} a, \frac{7}{30} a^2\right)$ . 

*9. $\left(0,0,\frac{5}{4} R\right)$ . 

10. (1) $I_{y} = \frac{1}{4}\pi a^{3}b$ ; (2) $I_{x} = \frac{72}{5}, I_{y} = \frac{96}{7}$ ; (3) $I_{x} = \frac{1}{3}ab^{3}, I_{y} = \frac{1}{3}ba^{3}$ . 

11. $\frac{1}{12} M h^{2}, \frac{1}{12} M b^{2}$ ( $M = b h \mu$ 为矩形板的质量).

12. (1) $\frac{8}{3} a^4$ ; (2) $\overline{x} = \overline{y} = 0, \overline{z} = \frac{7}{15} a^2$ ; (3) $\frac{112}{45} a^6\rho$ . 

13. $\frac{1}{2} a^2 M$ ( $M = \pi a^2 h\rho$ 为圆柱体的质量).

14. $F = \left(2G\mu \left(\ln \frac{R_2 + \sqrt{R_2^2 + a^2}}{R_1 + \sqrt{R_1^2 + a^2}} -\frac{R_2}{\sqrt{R_2^2 + a^2}} +\frac{R_1}{\sqrt{R_1^2 + a^2}}\right),0,\pi Ga\mu \left(\frac{1}{\sqrt{R_2^2 + a^2}} -\frac{1}{\sqrt{R_1^2 + a^2}}\right)\right).$ 

15. $F_{x} = F_{y} = 0, F_{z} = -2\pi G\rho_{0}\left[\sqrt{(h - a)^{2} + R^{2}} -\sqrt{R^{2} + a^{2}} +h\right].$ 

# *习题10-5（第176页）

1. (1) $\frac{\pi}{4}$ ; (2) 1; (3) $\frac{8}{3}$ . 

2. (1) $\frac{1}{3}\cos x (\cos x - \sin x)(1 + 2\sin 2x)$ ; (2) $\frac{2}{x} \ln (1 + x^2)$ ; 

(3) $\ln \sqrt{\frac{x^2 + 1}{x^4 + 1}} + 3x^2\arctan x^2 - 2x\arctan x;$ (4) $2xe^{-x^5} - e^{-x^3} - \int_x^{x^2}y^2e^{-xy^2}dy.$ 

3. $3f(x) + 2xf'(x)$ . 

4. (1) $\pi\arcsin a;$ 

(2) $\pi \ln \frac{1 + a}{2}$ , 提示: 设 $\varphi(\alpha) = \int_{0}^{\frac{\pi}{2}} \ln (\cos^2 x + \alpha^2 \sin^2 x) \, \mathrm{d}x, I = \varphi(a)$ .

5. (1) $\frac{\pi}{2} \ln(1 + \sqrt{2})$ , 提示: 利用公式 $\frac{\arctan x}{x} = \int_{0}^{1} \frac{dy}{1 + x^2 y^2}$ ;

(2) $\arctan(1+b)-\arctan(1+a)$ ，提示：利用公式 $\frac{x^{b}-x^{a}}{\ln x}=\int_{a}^{b}x^{y}dy.$ 

# 总习题十（第177页）

1. (1) $\frac{1}{2} (1 - \mathrm{e}^{-4})$ ; (2) $\frac{\pi}{4} R^4\left(\frac{1}{a^2} +\frac{1}{b^2}\right)$ . 

2. (1) (C); (2) (A); (3) (B). 

3. (1) $\frac{3}{2} + \cos 1 + \sin 1 - \cos 2 - 2\sin 2$ ; (2) $\pi^2 - \frac{40}{9}$ ; (3) $\frac{1}{3} R^3\left(\pi - \frac{4}{3}\right)$ ; 

(4) $\frac{\pi}{4} R^4 + 9\pi R^2$ . 

4. (1) $\int_{-2}^{0}\mathrm{d}x\int_{2x + 4}^{4 - x^2}f(x,y)\mathrm{d}y;$ (2) $\int_0^2\mathrm{d}x\int_{\frac{1}{2} x}^{3 - x}f(x,y)\mathrm{d}y;$ 

(3) $\int_0^1\mathrm{d}y\int_0^{y^2}f(x,y)\mathrm{d}x + \int_1^2\mathrm{d}y\int_0^{\sqrt{2y - y^2}}f(x,y)\mathrm{d}x.$ 

5. 略.

6. $\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{\sec \theta \tan \theta}f(\rho \cos \theta ,\rho \sin \theta)\rho \mathrm{d}\rho +\int_{\frac{\pi}{4}}^{\frac{3\pi}{4}}\mathrm{d}\theta \int_{0}^{\csc \theta}f(\rho \cos \theta ,\rho \sin \theta)\rho \mathrm{d}\rho +$ 

$$
\int_ {\frac {3 \pi}{4}} ^ {\pi} \mathrm{d} \theta \int_ {0} ^ {\sec \theta \tan \theta} f (\rho \cos \theta , \rho \sin \theta) \rho \mathrm{d} \rho .
$$

7. $f(x,y) = \sqrt{1 - x^2 - y^2} +\frac{8}{9\pi} -\frac{2}{3}.$ 

8. $\int_{-1}^{1}\mathrm{d}x\int_{x^2}^{1}\mathrm{d}y\int_{0}^{x^2 + y^2}f(x,y,z)\mathrm{d}z.$ 

9. (1) $\frac{1}{36}$ ; (2) $\frac{59}{480}\pi R^5$ ; (3) 0; (4) $\frac{250}{3}\pi$ . 

*10. (1) $F(t)$ 在 $(0, +\infty)$ 内单调增加；（2）略.

11. $\frac{1}{2}\sqrt{a^2b^2 + b^2c^2 + c^2a^2}$ . 

12. $\sqrt{\frac{2}{3}}R$ (R 为圆的半径).

13. $I = \frac{368}{105}\mu .$ 

14. $F = (F_{x}, F_{y}, F_{z})$ ，其中 $F_{x} = 0, F_{y} = \frac{4GmM}{\pi R^{2}} \left( \ln \frac{R + \sqrt{R^{2} + a^{2}}}{a} - \frac{R}{\sqrt{R^{2} + a^{2}}} \right)$ ，

$$
F _ {z} = - \frac {2 G m M}{R ^ {2}} \left(1 - \frac {a}{\sqrt {R ^ {2} + a ^ {2}}}\right).
$$

15. $\left(0,0,\frac{3}{8}b\right)$ . 

*16. $\mu|_{r=0}=\frac{3M}{\pi R^{3}}.$ 

# 第十一章

# 习题11-1（第185页）

1. (1) $I_{x} = \int_{L} y^{2} \mu(x, y) \, \mathrm{d}s$ , $I_{y} = \int_{L} x^{2} \mu(x, y) \, \mathrm{d}s$ ; 

(2) $\overline{x} = \frac{\int_{L} x \mu(x, y) \mathrm{d}s}{\int_{L} \mu(x, y) \mathrm{d}s}, \overline{y} = \frac{\int_{L} y \mu(x, y) \mathrm{d}s}{\int_{L} \mu(x, y) \mathrm{d}s}$ . 

2. 略.

3. (1) $2\pi a^{2n + 1}$ ; (2) $\sqrt{2}$ ; (3) $\frac{1}{12} (5\sqrt{5} +6\sqrt{2} -1)$ ; (4) $\mathrm{e}^a\left(2 + \frac{\pi}{4} a\right) - 2;$ 

(5) $\frac{\sqrt{3}}{2} (1 - \mathrm{e}^{-2})$ ; (6) 9; (7) $\frac{256}{15} a^3$ ; (8) $2\pi^2 a^3 (1 + 2\pi^2)$ . 

4. 质心在扇形的对称轴上且与圆心距离 $\frac{a\sin\varphi}{\varphi}$ 处.

5. (1) $I_{z} = \frac{2}{3}\pi a^{2}\sqrt{a^{2} + k^{2}}(3a^{2} + 4\pi^{2}k^{2})$ ; 

(2) $\overline{x} = \frac{6ak^2}{3a^2 + 4\pi^2k^2}, \overline{y} = \frac{-6\pi ak^2}{3a^2 + 4\pi^2k^2}, \overline{z} = \frac{3k(\pi a^2 + 2\pi^3k^2)}{3a^2 + 4\pi^2k^2}$ . 

# 习题11-2（第195页）

1—2. 略.

3. (1) $-\frac{56}{15}$ ; (2) $-\frac{\pi}{2}a^3$ ; (3) 0; (4) $-2\pi$ ; (5) $\frac{k^3\pi^3}{3} - a^2\pi$ ; (6) 13; 

(7) $\frac{1}{2}$ ; (8) $-\frac{14}{15}$ . 

4. (1) $\frac{34}{3}$ ; (2) 11; (3) 14; (4) $\frac{32}{3}$ . 

5. - | F | R. 

6. $mg(z_{2}-z_{1})$ . 

7. (1) $\int_{L} \frac{P(x, y) + Q(x, y)}{\sqrt{2}} \mathrm{d}s$ ; (2) $\int_{L} \frac{P(x, y) + 2xQ(x, y)}{\sqrt{1 + 4x^2}} \mathrm{d}s$ ; 

(3) $\int_{L} \left[ \sqrt{2x - x^{2}} P(x, y) + (1 - x) Q(x, y) \right] \mathrm{d}s.$ 

8. $\int_{\Gamma} \frac{P + 2xQ + 3yR}{\sqrt{1 + 4x^2 + 9y^2}} \, \mathrm{d}s.$ 

9. 略.

# 习题11-3（第208页）

1. (1) $\frac{1}{30}$ ; (2) 8. 

2. (1) $\frac{3}{8}\pi a^2$ ; (2) $12\pi$ ; (3) $\pi a^2$ . 

3. -π. 

4. C 为椭圆 $2x^{2}+y^{2}=1$ ，沿逆时针方向.

5. 提示: 利用面积公式 $A = \frac{1}{2} \oint_{c} x \, dy - y \, dx$ ，再逐条边地计算此曲线积分.

6. (1) $\frac{5}{2}$ ; (2) 236; (3) 5. 

7. (1) 12; (2) 0; (3) $\frac{\pi^2}{4}$ ; (4) $\frac{\sin 2}{4} - \frac{7}{6}$ . 

8. 略.

9. (1) $\frac{1}{2} x^2 + 2xy + \frac{1}{2} y^2$ ; (2) $x^2y$ ; (3) $-\cos 2x\sin 3y$ ; 

(4) $x^{3}y+4x^{2}y^{2}-12e^{y}+12ye^{y};$ (5) $y^{2}\sin x+x^{2}\cos y.$ 

10. 略.

*11. (1) $x^{3} + 3x^{2}y^{2} + \frac{4}{3} y^{3} = C$ ; (2) $a^{2}x - x^{2}y - xy^{2} - \frac{1}{3} y^{3} = C$ ; (3) $xe^{y} - y^{2} = C$ ; 

(4) $x \sin y + y \cos x = C;$ (5) $xy - \frac{1}{3}x^{3} = C;$ (6) 不是全微分方程；

(7) $\rho(1+e^{2\theta})=C;$ (8) 不是全微分方程.

12. $\lambda = -1, u(x, y) = -\arctan \frac{y}{x^2} + C.$ 

# 习题11-4（第213页）

1. $I_{x} = \iint_{\Sigma}(y^{2} + z^{2})\mu (x,y,z)\mathrm{d}S.$ 

2—3. 略.

4. (1) $\frac{13}{3}\pi$ ; (2) $\frac{149}{30}\pi$ ; (3) $\frac{111}{10}\pi$ . 

5. (1) $\frac{1+\sqrt{2}}{2}\pi$ ; (2) $9\pi$ . 

6. (1) $4\sqrt{61}$ ; (2) $-\frac{27}{4}$ ; (3) $\pi a(a^2 - h^2)$ ; (4) $\frac{64}{15}\sqrt{2} a^4$ . 

7. $\frac{2\pi}{15}(6\sqrt{3}+1)$ . 

8. $\frac{4}{3}\mu_0\pi a^4$ 

# 习题11-5（第222页）

1—2. 略.

3. (1) $\frac{2}{105}\pi R^7$ ; (2) $\frac{3}{2}\pi$ ; (3) $\frac{1}{2}$ ; (4) $\frac{1}{8}$ . 

4. (1) $\iint_{\Sigma} \left( \frac{3}{5} P + \frac{2}{5} Q + \frac{2\sqrt{3}}{5} R \right) \mathrm{d}S$ ; (2) $\iint_{\Sigma} \frac{2xP + 2yQ + R}{\sqrt{1 + 4x^2 + 4y^2}} \mathrm{d}S.$ 

5. $6\pi$ . 

# 习题11-6（第229页）

1. (1) $3a^4$ ; ${}^{*}(2)\frac{12}{5}\pi a^5$ ; ${}^{*}(3)\frac{2}{5}\pi a^5$ ; (4) $81\pi$ ; (5) $\frac{3}{2}$ . 

*2. (1) 0; (2) $a^3\left(2 - \frac{a^2}{6}\right)$ ; (3) $108\pi$ . 

*3. (1) div $A = 2x + 2y + 2z$ ; (2) div $A = y\mathrm{e}^{xy} - x\sin (xy) - 2xz\sin (xz^2)$ ; (3) div $A = 2x$ . 

4. 略.

*5. 提示: 取液面为 $xOy$ 面, $z$ 轴铅直向下. 该物体表面 $\Sigma$ 上点 $(x, y, z)$ 处单位面积上所受液体的压力为 $(- \nu_{0} z \cos \alpha, - \nu_{0} z \cos \beta, - \nu_{0} z \cos \gamma)$ , 其中 $\nu_{0}$ 为液体单位体积所受的重力, $\cos \alpha, \cos \beta, \cos \gamma$ 为点 $(x, y, z)$ 处 $\Sigma$ 的外法线的方向余弦.

# 习题11-7（第238页）

1. 略.

*2. (1) $-\sqrt{3}\pi a^2$ ; (2) $-2\pi a(a + b)$ ; (3) $-20\pi$ ; (4) $9\pi$ . 

*3. (1) rot A = 2i + 4j + 6k; (2) rot A = i + j; 

(3) rot $A = \left[ x \sin(\cos z) - xy^{2} \cos(xz) \right] i - y \sin(\cos z) j + \left[ y^{2} z \cos(xz) - x^{2} \cos y \right] k.$ 

*4. (1) 0; (2) -4. 

*5. (1) $2\pi$ ; (2) $12\pi$ . 

*6. 略.

*7.0. 

# 总习题十一（第238页）

1. (1) $\int_{\Gamma} (P \cos \alpha + Q \cos \beta + R \cos \gamma) \, \mathrm{d}s$ ，切向量；

(2) $\iint_{\Sigma} (P \cos \alpha + Q \cos \beta + R \cos \gamma) \, \mathrm{d}S$ ，法向量.

2. (C). 

3. (1) $2a^{2}$ ; (2) $\frac{(2 + t_{0}^{2})^{\frac{3}{2}} - 2\sqrt{2}}{3}$ ; (3) $-2\pi a^{2}$ ; (4) $\frac{1}{35}$ ; (5) $\pi a^{2}$ ; (6) $\frac{\sqrt{2}}{16}\pi$ . 

4. $\frac{1}{2}\mathrm{e} - \frac{3}{2}\mathrm{e}^{-1}$ . 

5. (1) $2\pi \arctan \frac{H}{R}$ ; (2) $-\frac{\pi}{4} h^4$ ; (3) $2\pi R^3$ ; (4) $\frac{2}{15}$ ; (5) $a^4(a - 1)$ . 

6. $\frac{1}{2}\ln\left(x^{2}+y^{2}\right)$ . 

7. 略.

8. (1) 略; (2) $\frac{c}{d} - \frac{a}{b}$ .

9. $\left(0,0,\frac{a}{2}\right)$ . 

10. 略.

*11. 3. 

12. $\frac{3}{2}$ . 

# 第十二章

# 习题12-1（第247页）

1. (1) $\frac{1 + 1}{1 + 1^2} + \frac{1 + 2}{1 + 2^2} + \frac{1 + 3}{1 + 3^2} + \frac{1 + 4}{1 + 4^2} + \frac{1 + 5}{1 + 5^2} + \cdots$ ; 

(2) $\frac{1}{2} + \frac{1 \times 3}{2 \times 4} + \frac{1 \times 3 \times 5}{2 \times 4 \times 6} + \frac{1 \times 3 \times 5 \times 7}{2 \times 4 \times 6 \times 8} + \frac{1 \times 3 \times 5 \times 7 \times 9}{2 \times 4 \times 6 \times 8 \times 10} + \cdots$ ; 

(3) $\frac{1}{5} - \frac{1}{5^2} + \frac{1}{5^3} - \frac{1}{5^4} + \frac{1}{5^5} - \cdots$ ; 

(4) $\frac{1!}{1^1} + \frac{2!}{2^2} + \frac{3!}{3^3} + \frac{4!}{4^4} + \frac{5!}{5^5} + \cdots$ . 

2.（1）发散；（2）收敛；（3）发散，提示：先乘 $2\sin\frac{\pi}{12}$ ，再将一般项分解为两个余弦函数之差；（4）发散.

3. 略.

4.（1）收敛；（2）发散；（3）发散；（4）发散；（5）收敛.

*5. (1) 收敛; (2) 发散; (3) 收敛; (4) 发散.

# 习题12-2（第260页）

1. (1) (B); (2) (C). 

2.（1）发散；（2）发散；（3）收敛；（4）收敛；（5）a>1时收敛， $a \leqslant 1$ 时发散.

3. (1) 发散；(2) 收敛；(3) 收敛；(4) 收敛.

*4.（1）收敛；（2）收敛；（3）收敛；

(4) 当 b<a 时收敛, 当 b>a 时发散, 当 b=a 时不能肯定.

5.（1）收敛；（2）收敛；（3）发散；（4）收敛；（5）发散；（6）发散.

6.（1）条件收敛；（2）绝对收敛；（3）绝对收敛；（4）条件收敛；（5）发散.

# 习题12-3（第269页）

1. (B). 

2. (1) $(-1, 1)$ ; (2) $(-1, 1)$ ; (3) $(- \infty, +\infty)$ ; (4) $(-3, 3)$ ; 

(5) $\left(-\frac{1}{2},\frac{1}{2}\right)$ ; (6) $(-1,1)$ ; (7) $(- \sqrt{2},\sqrt{2})$ ; (8) $(4,6)$ . 

3. (1) $\frac{1}{(1 - x)^2} (-1 < x < 1)$ ; (2) $\frac{1}{4}\ln \frac{1 + x}{1 - x} + \frac{1}{2}\arctan x - x (-1 < x < 1)$ ; 

(3) $\frac{1}{2} \ln \frac{1 + x}{1 - x} (-1 < x < 1)$ ; (4) $\frac{x^2}{(1 - x)^2} - x^2 - 2x^3 (-1 < x < 1)$ . 

# 习题12-4（第277页）

1. $\cos x = \cos x_{0} + \cos\left(x_{0} + \frac{\pi}{2}\right)(x - x_{0}) + \cdots + \frac{\cos\left(x_{0} + \frac{n\pi}{2}\right)}{n!}(x - x_{0})^{n} + \cdots (-\infty, +\infty)$ . 

2. (1) $\frac{\mathrm{e}^x - \mathrm{e}^{-x}}{2} = \sum_{n=1}^{\infty} \frac{x^{2n-1}}{(2n-1)!}, (-\infty, +\infty)$ ; 

(2) $\ln (a + x) = \ln a + \sum_{n=1}^{\infty} (-1)^{n-1} \frac{1}{n} \left( \frac{x}{a} \right)^n, (-a, a]$ ; 

(3) $a^x = \sum_{n=0}^{\infty} \frac{(x \ln a)^n}{n!}, (-\infty, +\infty)$ ; 

(4) $\sin^2 x = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{(2x)^{2n}}{2(2n)!}, (-\infty, +\infty)$ ; 

(5) $(1 + x)\ln (1 + x) = x + \sum_{n = 2}^{\infty}\frac{(-1)^{n}x^{n}}{n(n - 1)}, (-1,1];$ 

(6) $\frac{x}{\sqrt{1 + x^2}} = x + \sum_{n=1}^{\infty} (-1)^n \frac{2(2n)!}{(n!)^2} \left( \frac{x}{2} \right)^{2n+1}, [-1, 1]$ . 

3. (1) $\sqrt{x^3} = 1 + \frac{3}{2} (x - 1) + \sum_{n=0}^{\infty} (-1)^n \frac{(2n)!}{(n!)^2} \frac{3}{(n+1)(n+2)2^n} \left(\frac{x-1}{2}\right)^{n+2}, [0,2]$ ; 

(2) $\lg x = \frac{1}{\ln 10} \sum_{n=1}^{\infty} (-1)^{n-1} \frac{(x-1)^n}{n}, (0,2]$ ; 

(3) $x\mathrm{e}^{x} = \mathrm{e} + \sum_{n = 1}^{\infty}\left[\frac{\mathrm{e}}{(n - 1)!} +\frac{\mathrm{e}}{n!}\right](x - 1)^{n},(-\infty , + \infty)$ . 

4. $\cos x = \frac{1}{2} \sum_{n=0}^{\infty} (-1)^n \left[ \frac{(x + \frac{\pi}{3})^{2n}}{(2n)!} + \sqrt{3} \frac{(x + \frac{\pi}{3})^{2n+1}}{(2n+1)!} \right], (-\infty, +\infty)$ . 

5. $\frac{1}{x} = \frac{1}{3}\sum_{n = 0}^{\infty}(-1)^{n}\frac{(x - 3)^{n}}{3^{n}},(0,6).$ 

6. $\frac{1}{x^2 + 3x + 2} = \sum_{n=0}^{\infty}\left(\frac{1}{2^{n+1}} - \frac{1}{3^{n+1}}\right)(x + 4)^n, (-6, -2)$ . 

# 习题12-5（第286页）

1. (1) 1.0986; (2) 1.648; (3) 2.00430; (4) 0.9994. 

2. (1) 0.494 0; (2) 0.487. 

3. (1) $y = C\mathrm{e}^{\frac{x^2}{2}} + \left[-1 + x + \frac{1}{1\times 3} x^3 +\dots +\frac{x^{2n - 1}}{1\times 3\times 5\times\cdots\times(2n - 1)} +\dots \right]$ ; 

(2) $y = a_{0}e^{-\frac{x^{2}}{2}} + a_{1}\left[x - \frac{x^{3}}{1\times 3} +\frac{x^{5}}{1\times 3\times 5} -\dots +(-1)^{n - 1}\frac{x^{2n - 1}}{1\times 3\times 5\times\cdots\times(2n - 1)} +\dots\right];$ 

(3) $y = C(1 - x) + x^3 \left[ \frac{1}{3} + \frac{1}{6}x + \frac{1}{10}x^2 + \cdots + \frac{2}{(n+2)(n+3)}x^n + \cdots \right]$ . 

4. (1) $y=\frac{1}{2}+\frac{1}{4}x+\frac{1}{8}x^{2}+\frac{1}{16}x^{3}+\frac{9}{32}x^{4}+\cdots;$ 

(2) $y = x + \frac{1}{1 \times 2} x^2 + \frac{1}{2 \times 3} x^3 + \frac{1}{3 \times 4} x^4 + \cdots + \frac{1}{n(n - 1)} x^n + \cdots.$ 

5. 和函数为 $y(x) = \frac{2}{3} e^{-\frac{x}{2}} \cos \frac{\sqrt{3}}{2} x + \frac{1}{3} e^x (-\infty < x < +\infty)$ .

6. $\mathrm{e}^x\cos x = \sum_{n=0}^{\infty} 2^{\frac{n}{2}}\cos \frac{n\pi}{4} \cdot \frac{x^n}{n!} (-\infty, +\infty)$ , 提示: $\mathrm{e}^x\cos x = \mathrm{Re}\mathrm{e}^{(1+\mathrm{i})x} = \mathrm{Re}\mathrm{e}^{\sqrt{2}\left(\cos \frac{\pi}{4} + \mathrm{i}\sin \frac{\pi}{4}\right)x}$ .

# *习题12-6（第294页）

1.（1）取正整数 $N \geqslant \frac{|x|}{\varepsilon}$ ；（2）略.

2. (1) $s(x) = \begin{cases} 0, & x = 0, \\ 1 + x^2, & x \neq 0; \end{cases}$ 

(2) 当 $x \neq 0$ 时取正整数 $N \geqslant \frac{\ln \frac{1}{\varepsilon}}{\ln (1 + x^{2})}$ ，当 x = 0 时取 N = 1；

(3) 在 $[0,1]$ 上不一致收敛, 在 $\left[\frac{1}{2}, 1\right]$ 上一致收敛.

3.（1）一致收敛；（2）不一致收敛.

4. 略.

# 习题12-7（第306页）

1. (1) $f(x) = \pi^2 + 1 + 12 \sum_{n=1}^{\infty} \frac{(-1)^n}{n^2} \cos nx, (-\infty, +\infty)$ ; 

(2) $f(x)=\frac{e^{2\pi}-e^{-2\pi}}{\pi}\left[\frac{1}{4}+\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{2}+4}(2\cos nx-n\sin nx)\right]$ 

$$
(x \neq (2 n + 1) \pi , n = 0, \pm 1, \pm 2, \dots);
$$

(3) $f(x)=\frac{a-b}{4}\pi+\sum_{n=1}^{\infty}\left\{\frac{\left[1-(-1)^{n}\right](b-a)}{n^{2}\pi}\cos nx+\frac{(-1)^{n-1}(a+b)}{n}\sin nx\right\},$ 

$$
(x \neq (2 n + 1) \pi , n = 0, \pm 1, \pm 2, \dots).
$$

2. (1) $2\sin \frac{x}{3} = \frac{18\sqrt{3}}{\pi} \sum_{n=1}^{\infty} (-1)^{n-1} \frac{n\sin nx}{9n^2 - 1}, (-\pi, \pi)$ ; 

(2) $f(x)=\frac{1+\pi-\mathrm{e}^{-\pi}}{2\pi}+\frac{1}{\pi}\sum_{n=1}^{\infty}\left\{\frac{1-(-1)^{n}\mathrm{e}^{-\pi}}{1+n^{2}}\cos nx+\right.$ 

$$
\left[ \frac {- n + (- 1) ^ {n} n e ^ {- \pi}}{1 + n ^ {2}} + \frac {1}{n} (1 - (- 1) ^ {n}) \right] \sin n x \Bigg \}, (- \pi , \pi);
$$

(3) $x \sin x = 1 - \frac{1}{2} \cos x + 2 \sum_{n=2}^{\infty} \frac{(-1)^{n-1}}{n^2 - 1} \cos nx, (-\pi, \pi)$ . 

3. $\cos \frac{x}{2} = \frac{2}{\pi} + \frac{4}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{4n^2 - 1} \cos nx, [-\pi, \pi]$ . 

4. $f(x)=\frac{2}{\pi}\sum_{n=1}^{\infty}\left[\frac{1}{n^{2}}\sin\frac{n\pi}{2}+(-1)^{n+1}\frac{\pi}{2n}\right]\sin nx$ $(x\neq(2n+1)\pi,n=0,\pm1,\pm2,\cdots)$ 

5. $\frac{\pi - x}{2} = \sum_{n=1}^{\infty} \frac{1}{n} \sin nx, (0, \pi]$ . 

6. $2x^{2} = \frac{4}{\pi}\sum_{n = 1}^{\infty}\left[-\frac{2}{n^{3}} +(-1)^{n}\left(\frac{2}{n^{3}} -\frac{\pi^{2}}{n}\right)\right]\sin nx,[0,\pi);$ 

$$
2 x ^ {2} = \frac {2}{3} \pi^ {2} + 8 \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n}}{n ^ {2}} \cos n x, [ 0, \pi ].
$$

7. 略.

习题12-8（第312页）

1. (1) $f(x) = \frac{11}{12} + \frac{1}{\pi^2} \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^2} \cos 2n\pi x, (-\infty, +\infty)$ ; 

(2) $f(x) = -\frac{1}{4} + \sum_{n=1}^{\infty} \left\{ \left[ \frac{1 - (-1)^n}{n^2 \pi^2} + \frac{2 \sin \frac{n \pi}{2}}{n \pi} \right] \cos n \pi x + \frac{1 - 2 \cos \frac{n \pi}{2}}{n \pi} \sin n \pi x \right\}$ , 

$$
\left(x \neq 2 k, 2 k + \frac {1}{2}, k = 0, \pm 1, \pm 2, \dots\right);
$$

(3) $f(x) = -\frac{1}{2} + \sum_{n=1}^{\infty} \left\{ \frac{6}{n^2 \pi^2} [1 - (-1)^n] \cos \frac{n \pi x}{3} + \frac{6}{n \pi} (-1)^{n+1} \sin \frac{n \pi x}{3} \right\}$ , 

$$
(x \neq 3 (2 k + 1), k = 0, \pm 1, \pm 2, \dots).
$$

2. (1) $f(x) = \frac{4l}{\pi^2} \sum_{k=1}^{\infty} \frac{(-1)^{k-1}}{(2k-1)^2} \sin \frac{(2k-1)\pi x}{l}, [0, l]$ , 

$$
f (x) = \frac {l}{4} - \frac {2 l}{\pi^ {2}} \sum_ {k = 1} ^ {\infty} \frac {1}{(2 k - 1) ^ {2}} \cos \frac {2 (2 k - 1) \pi x}{l}, [ 0, l ];
$$

(2) $f(x)=\frac{8}{\pi}\sum_{n=1}^{\infty}\left\{\frac{(-1)^{n+1}}{n}+\frac{2}{n^{3}\pi^{2}}\left[(-1)^{n}-1\right]\right\}\sin\frac{n\pi x}{2},[0,2),$ 

$$
f (x) = \frac {4}{3} + \frac {1 6}{\pi^ {2}} \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n}}{n ^ {2}} \cos \frac {n \pi x}{2}, [ 0, 2 ].
$$

*3. $f(x) = \operatorname{sh} 1 \sum_{n=-\infty}^{\infty} \frac{(-1)^n (1-n\pi i)}{1 + (n\pi)^2} e^{n\pi xi}$ ( $x \neq 2k+1, k=0, \pm 1, \pm 2, \cdots$ ). 

*4. $u(t) = \frac{h\tau}{T} +\frac{2h}{\pi}\sum_{n = 1}^{\infty}\frac{1}{n}\sin \frac{n\tau\pi}{T}\cos \frac{2n\pi t}{T} (-\infty , + \infty)$ . 

# 总习题十二（第313页）

1.（1）必要，充分；（2）充分必要；（3）收敛，发散.

2. (A). 

3. (1) 发散；(2) 发散；(3) 收敛；(4) 发散；

(5) a<1 时收敛, a>1 时发散, a=1 时, s>1 收敛, $s \leqslant 1$ 发散.

4. 略.

5. 不一定. 考虑级数 $\sum_{n=1}^{\infty} (-1)^{n} \frac{1}{\sqrt{n}}$ 及 $\sum_{n=1}^{\infty} \left((-1)^{n} \frac{1}{\sqrt{n}} + \frac{1}{n}\right)$ .

6.（1） $p > 1$ 时绝对收敛， $0 < p \leqslant 1$ 时条件收敛， $p \leqslant 0$ 时发散；

(2) 绝对收敛; (3) 条件收敛; (4) 绝对收敛.

7. (1) 0; (2) $\sqrt[4]{8}$ , 提示: 化成 $2^{\frac{1}{3} + \frac{2}{3^2} + \cdots + \frac{n}{3^n} + \cdots}$ .

8. (1) $\left(-\frac{1}{5}, \frac{1}{5}\right)$ ; (2) $\left(-\frac{1}{e}, \frac{1}{e}\right)$ ; (3) $(-2, 0)$ ; (4) $(- \sqrt{2}, \sqrt{2})$ . 

9. (1) $s(x) = \frac{2 + x^2}{(2 - x^2)^2}, (-\sqrt{2}, \sqrt{2})$ ; $^* (2) s(x) = \arctan x, [-1, 1]$ ; 

(3) $s(x) = \frac{x - 1}{(2 - x)^2}, (0,2)$ ; 

* (4) $s(x) = \begin{cases} 1 + \left(\frac{1}{x} - 1\right)\ln (1 - x), & x \in [-1,0) \cup (0,1), \\ 0, & x = 0, \\ 1, & x = 1. \end{cases}$ 

10. 收敛域 $(- \infty, + \infty)$ , 和函数 $f(x) = x \cos x, x \in (-\infty, + \infty)$ .

11. (1) 2e; (2) $\frac{1}{2} (\cos 1 + \sin 1)$ , 提示: 利用 $\cos 1$ 和 $\sin 1$ 的展开式.

12. (1) $\ln (x + \sqrt{x^2 + 1}) = x + \sum_{n=1}^{\infty} (-1)^n \frac{(2n - 1)!!}{(2n)!!} \frac{x^{2n+1}}{2n + 1}, x \in [-1, 1]$ , 

提示:利用积分 $\int_{0}^{x}\frac{dt}{\sqrt{t^{2}+1}}$ ;

(2) $\frac{1}{(2 - x)^2} = \sum_{n=1}^{\infty} \frac{n}{2^{n+1}} x^{n-1}, x \in (-2, 2)$ . 

13. $f(x)=\frac{e^{\pi}-1}{2\pi}+\frac{1}{\pi}\sum_{n=1}^{\infty}\left\{\frac{(-1)^{n}e^{\pi}-1}{n^{2}+1}\cos nx+\frac{n[(-1)^{n+1}e^{\pi}+1]}{n^{2}+1}\sin nx\right\},$ $-\infty<x<+\infty$ 且 $x\neq n\pi,\ n=0,\pm1,\pm2,\cdots.$ 

14. $f(x) = \frac{2}{\pi}\sum_{n = 1}^{\infty}\frac{1 - \cos nh}{n}\sin nx,x\in (0,h)\cup (h,\pi ];$ 

$$
f (x) = \frac {h}{\pi} + \frac {2}{\pi} \sum_ {n = 1} ^ {\infty} \frac {\sin n h}{n} \cos n x, x \in [ 0, h) \cup (h, \pi ].
$$

（一）公司董事会、监事会和经理层对董事会负责，行使下列职权：

(1) $\frac{1}{2}$ (2) $\frac{1}{3}$ (3) $\frac{1}{4}$ (4) $\frac{1}{5}$ (5) $\frac{1}{6}$ (6) $\frac{1}{7}$ (7) $\frac{1}{8}$ (8) $\frac{1}{9}$ (9) $\frac{1}{10}$ (10) 

（一）公司董事会会议召开情况

(1) 本报告书的摘要、修订稿和补充材料

The Ground Truth image displays a single, solid horizontal line. According to Rule 2 (UNDERSCORE & LINE RULES), this is a stylistic or background line, not a placeholder underscore. Therefore, the OCR result must ignore it. The provided OCR content is "____", which consists of four underscores. This is an incorrect interpretation of the line as a placeholder, violating the rule that stylistic lines must be ignored. The OCR has hallucinated text (underscores) where none should exist based on the GT's visual context. Hence, the OCR result is inconsistent with the Ground Truth. 

The Ground Truth image displays a single, solid horizontal line. According to Rule 2 (UNDERSCORE & LINE RULES), this is a stylistic or background line, not a placeholder underscore. Therefore, the OCR result must ignore it. The provided OCR content is "____", which consists of four underscores. This is an incorrect interpretation of the line as a placeholder, violating the rule that stylistic lines must be ignored. The OCR has hallucinated text (underscores) where none should exist, violating the rule to ignore such lines. Hence, the OCR result is inconsistent with the Ground Truth. 

The Ground Truth image displays a single, solid horizontal line. According to Rule 2 (UNDERSCORE & LINE RULES), if the GT contains lines used for stylistic emphasis or as background elements (like ruled paper), the OCR result must ignore them. The line in the GT is clearly a stylistic or background line, not a placeholder for text. Therefore, the OCR should not have output any underscores. Outputting `____` constitutes an error under Rule 2, as it hallucinates placeholder symbols where none are semantically intended. Hence, the OCR result is inconsistent with the Ground Truth. 

The Ground Truth image displays a single, solid horizontal line. According to Rule 2 (UNDERSCORE & LINE RULES), this is a stylistic or background line, not a placeholder underscore. Therefore, the OCR result must ignore it. The provided OCR content is "____", which consists of four underscores. This is an incorrect interpretation of the line as a placeholder, violating the rule that stylistic lines must be ignored. The OCR has hallucinated text (underscores) where none should exist, violating the rule to ignore such lines. Hence, the OCR result is inconsistent with the Ground Truth. 

# 郑重声明

高等教育出版社依法对本书享有专有出版权。任何未经许可的复制、销售行为均违反《中华人民共和国著作权法》，其行为人将承担相应的民事责任和行政责任；构成犯罪的，将被依法追究刑事责任。为了维护市场秩序，保护读者的合法权益，避免读者误用盗版书造成不良后果，我社将配合行政执法部门和司法机关对违法犯罪的单位和个人进行严厉打击。社会各界人士如发现上述侵权行为，希望及时举报，我社将奖励举报有功人员。

反盗版举报电话 (010) 58581999 58582371

反盗版举报邮箱 dd@hep.com.cn

通信地址 北京市西城区德外大街4号 高等教育出版社法律事务部

邮政编码 100120

# 读者意见反馈

为收集对教材的意见建议,进一步完善教材编写并做好服务工作,读者可将对本教材的意见建议通过如下渠道反馈至我社。

咨询电话 400-810-0598

反馈邮箱 hepsci@pub.hep.cn

通信地址 北京市朝阳区惠新东街4号富盛大厦1座

高等教育出版社理科事业部

邮政编码 100029

# 防伪查询说明

用户购书后刮开封底防伪涂层,使用手机微信等软件扫描二维码,会跳转至防伪查询网页,获得所购图书详细信息。

防伪客服电话 (010) 58582300

2008 年度普通高等教育精品教材

1997 年普通高等学校国家级教学成果一等奖

高等数学 第八版 上册

高等数学 第八版 下册

高等数学附册 学习辅导与习题选解 同济·第八版

高等数学习题全解指导 上册 同济·第八版

高等数学习题全解指导 下册 同济·第八版

工程数学——线性代数 第七版

线性代数附册 学习辅导与习题全解 同济·第七版

工程数学——概率统计简明教程 第三版

概率统计简明教程附册 学习辅导与习题全解 同济·第三版

概率论与数理统计

工程数学——新编统计学教程

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-14/04100f38-96d1-42af-af62-40f283be46df/1a5de22e67dcd1e00908ff7a9b0f3cb87d319337367ad31c3205942595fda64e.jpg)



定价 46.50 元
