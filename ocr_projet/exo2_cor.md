\begin{exercise}{
Title_exo: % Nom de l'exercice
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: % NameID des chapitres
Involved_Concepts: % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
}
{

\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
from sympy import *
from src.scripts.Mes_fctions.Mes_fctions_d_alg_lineaire import *

A = Matrix([[1,4,4],[-1,-3,-3],[0,2,3]])
A_latex = latex(A.copy(), mat_delim='', mat_str='pmatrix')

P = Matrix([[1,2,2],[-1,-1,-2],[1,1,1]])
P_latex = latex(P.copy(), mat_delim='', mat_str='pmatrix')

R = Matrix([[1,0,0],[0,0,-1],[0,1,0]])
R_latex = latex(R.copy(), mat_delim='', mat_str='pmatrix')

P_inv = P.copy().inv()
P_inv_latex = latex(P_inv, mat_delim='', mat_str='pmatrix')

Q = P_inv*A*P
Q_latex = latex(Q, mat_delim='', mat_str='pmatrix')

T = ((P.inv())**4)*((A)**4)*(P**4) 
T_latex = latex(T, mat_delim='', mat_str='pmatrix')

S = ((P.inv())**4)* A *(P**4) 
S_latex = latex(S, mat_delim='', mat_str='pmatrix')


AP = A*P
AP_latex = latex(AP, mat_delim='', mat_str='pmatrix')
PA = P*A
PA_latex = latex(PA, mat_delim='', mat_str='pmatrix')


\end{python}







\begin{python}
A= Matrix([[-7,6,6,6],[0,2,0,0],[-3,3,2,3],[-6,3,6,5]])
C_1=A.col(0)
C_2=A.col(1)
C_3=A.col(2)
C_4=A.col(3)
e_1=Matrix([[1],[0],[0],[0]])
e_2=Matrix([[0],[1],[0],[0]])
e_3=Matrix([[0],[0],[1],[0]])
e_4=Matrix([[0],[0],[0],[1]])
a=-2*(e_1)- e_2- e_3- e_4
b=e_2-e_4
c=2*e_1+e_3+e_4
d=3*e_1+e_3+2*e_4
P=Matrix([[a[0],b[0],c[0],d[0]],[a[1],b[1],c[1],d[1]],[a[2],b[2],c[2],d[2]],[a[3],b[3],c[3],d[3]]])
D=(P.inv())*A*P
n =Symbol('n')
c10=C_1[0]
c11=C_1[1]
c12=C_1[2]
c13=C_1[3]
c20=C_2[0]
c21=C_2[1]
c22=C_2[2]
c23=C_2[3]
c30=C_3[0]
c31=C_3[1]
c32=C_3[2]
c33=C_3[3]
c40=C_4[0]
c41=C_4[1]
c42=C_4[2]
c43=C_4[3]
ab=c40-c30
ac=c42-c32
ad=c43-c33
C1=latex(C_1, mat_delim='', mat_str='pmatrix')
C2=latex(C_2, mat_delim='', mat_str='pmatrix')
C3=latex(C_3, mat_delim='', mat_str='pmatrix')
C4=latex(C_4, mat_delim='', mat_str='pmatrix')
ae=-2*C_1 -C_2 -C_3 -C_4
ae=latex(ae, mat_delim='', mat_str='pmatrix')
aa=C_2 - C_4
aa=latex(aa, mat_delim='', mat_str='pmatrix')
az=2*C_1 +C_3 +C_4
az=latex(az, mat_delim='', mat_str='pmatrix')
aq=3*C_1 +C_3 +2*C_4
aq=latex(aq, mat_delim='', mat_str='pmatrix')
aaa=3*C_1 +C_3 +2*C_4
aaa=latex(aaa, mat_delim='', mat_str='pmatrix')
\end{python}

(ques1)=
\qcm{\fr{Soit }\en{Let } $\boldsymbol a, \boldsymbol b, \boldsymbol c, \boldsymbol d$, \fr{ et }\en{and }$\boldsymbol f$\fr{les $5$ vecteurs définis par:}\en{ be the five vectors defined by setting:}
\begin{equation*}
\begin{align*}
&\boldsymbol a:=-2\boldsymbol e_{1}- \boldsymbol e_{2}-\boldsymbol e_{3}-\boldsymbol e_{4}; \hspace{1.5ex}
\boldsymbol b:= \boldsymbol e_{2}-\boldsymbol e_{4}; \hspace{1.5ex}
%
\boldsymbol c:=2\boldsymbol e_{1}+\boldsymbol e_{3}+\boldsymbol e_{4}; \hspace{1.5ex}\\
%
&\boldsymbol d:=3\boldsymbol e_{1}+\boldsymbol e_{3}+2\boldsymbol e_{4}; \hspace{1.5ex} \text{ \fr{ et }
 \en{  and }}
\boldsymbol f:=3\boldsymbol e_{1}-\boldsymbol e_{2}+\boldsymbol e_{3}-\boldsymbol e_{4}.
\end{align*}
\end{equation*}
 \fr{On pose:} \en{ Define:
}$\boldsymbol \beta':=(\boldsymbol a, \boldsymbol b, \boldsymbol c, \boldsymbol d)$
 \fr{ et } \en{  and 
}$\widehat{\boldsymbol \beta'}:=(\boldsymbol a, \boldsymbol b, \boldsymbol c, \boldsymbol d, \boldsymbol f)$.

 \fr{On peut écrire:}
 \en{ One can say that:}
}
{
\right{ $\widehat{\boldsymbol \beta'}$
 \fr{n'est pas une base $\bfR^{4}$.}
 \en{is not a basis of $\bfR^{4}$.}
      }
%
\right{$\boldsymbol{\beta'}$
 \fr{est une base de $\bfR^{4}$.}
 \en{is a basis of $\bfR^{4}$.}
     }

%
\wrong{ $\widehat{\boldsymbol \beta'}$
 \fr{est une base $\bfR^{4}$.}
 \en{ is a basis of $\bfR^{4}$.}
      }
%
\wrong{$\boldsymbol{\beta'}$
\fr{n'est pas une base de $\bfR^{4}$.
  }
 \en{is not a basis of $\bfR^{4}$.}
  }
%
\wronger
} 
{%Hint: 
}
{
 \fr{L'égalité suivante:}
 \en{The following equality:}
\begin{equation*}
\begin{align*}
 \det(\boldsymbol a,\boldsymbol b,\boldsymbol c,\boldsymbol d)
&=
\left|\begin{matrix}
&\sympy{c10} &\sympy{c20} &\sympy{c30} &\sympy{c40}\\
%
&\sympy{c11} &\sympy{c21} &\sympy{c31} &\sympy{c41}\\
%
&\sympy{c12} &\sympy{c22} &\sympy{c32} &\sympy{c42}\\
%
&\sympy{c13} &\sympy{c23} &\sympy{c33} &\sympy{c43}\\
\end{matrix}\right|
=
2\left|\begin{matrix}
&\sympy{c11}  &\sympy{c30} &\sympy{c40}\\
%
&\sympy{c12}   &\sympy{c32} &\sympy{c42}\\
%
&\sympy{c13}   &\sympy{c33} &\sympy{c43}\\
\end{matrix}\right|
=
2\left|\begin{matrix}
&\sympy{c10}  &\sympy{c30} &\sympy{ab}\\
%
&\sympy{c12}   &\sympy{c32} &\sympy{ac}\\
%
&\sympy{c13}   &\sympy{c33} &\sympy{ad}\\
\end{matrix}\right|\\
&=2\left(
-\left|\begin{matrix}
&\sympy{c10}  &\sympy{c30} \\
%
&\sympy{c13}   &\sympy{c33}\\
\end{matrix}\right|
-
\left|\begin{matrix}
&\sympy{c10}  &\sympy{c30} \\
%
&\sympy{c12}   &\sympy{c32} \\
%
\end{matrix}\right|
\right)
%
=
-2 (-42+36 + -14+18)
=
4\neq 0.
\end{align*}
\end{equation*}
 \fr{établit clairement que la famille $(\boldsymbol a, \boldsymbol b,\boldsymbol c,\boldsymbol d)$ est une base de $\bfR^{4}$ puisque c'est une famille libre de $4$ vecteurs de $\bfR^{4}$.}
 \en{clearly shows that  $(\boldsymbol a, \boldsymbol b,\boldsymbol c,\boldsymbol d)$ is a basis of $\bfR^{4}$ since it is a linearly independent family of vectors of $4$ vectors of $\bfR^{4}$.}%
 \fr{Par ailleurs, si $\widehat{\boldsymbol \beta'}$ était une base de $\bfR^{4}$, ce serait une famille de vecteurs linéairement indépendants de $\bfR^{4}$. Par conséquent, on aurait $\dim(\spn\{\boldsymbol a, \boldsymbol b,\boldsymbol c,\boldsymbol d, \boldsymbol f\})=5$. Ceci est absurde puisque $\spn\{\boldsymbol a, \boldsymbol b,\boldsymbol c,\boldsymbol d, \boldsymbol f\}\subset \bfR^{4}$. Par conséquent, $\widehat{\boldsymbol \beta'}$ ne peut pas être une base de $\bfR^{4}$.}
 \en{Besides, if $\widehat{\boldsymbol \beta'}$ is a basis of $\bfR^{4}$, then it is a linearly independent family of $\bfR^{4}$ and therefore $\dim(\spn\{\boldsymbol a, \boldsymbol b,\boldsymbol c,\boldsymbol d, \boldsymbol f\})=5$. This is absurd since $\spn\{\boldsymbol a, \boldsymbol b,\boldsymbol c,\boldsymbol d, \boldsymbol f\}\subset \bfR^{4}$. Therefore $\widehat{\boldsymbol \beta'}$ can not be a basis of $\bfR^{4}$.

}
}

{
logic: 30
abstraction: 20
reasoning: 20
calculation: 30
}

\begin{python}

A4= Matrix([[-7,6,6,6],[0,2,0,0],[-3,3,2,3],[-6,3,6,5]])
A4=latex(A4, mat_delim='', mat_str='pmatrix')
\end{python}
(ques2)=
\qcm{ \fr{On conserve les notations de la }
 \en{We keep the notations from }[\fr{question}\en{Question} $1$](#ques1).%
 \fr{ Soit $u$ l'endomorphisme dont la representation matricielle, dans la base canonique est donnée par :}
  \en{Let $u$ be the endomorphism, the matrix representation of which, in the standard basis, is given by :}
 \begin{equation*}
A:= \sympy{A4}.
\end{equation*}
 \fr{On souhaite déterminer $u(\boldsymbol a), u(\boldsymbol b), u(\boldsymbol c)$ et $u(\boldsymbol d)$ et les exprimer dans la base $\boldsymbol \beta'$.}
 \en{One wants to compute  $u(\boldsymbol a), u(\boldsymbol b), u(\boldsymbol c)$ and $u(\boldsymbol d)$ and write them in the basis $\boldsymbol \beta'$.}
 \fr{ On peut écrire :}\en{ One can say that :}


}
{
\right{ $\vcenter {\displaystyle u(\boldsymbol a)=2\boldsymbol a,\ u(\boldsymbol b)=2\boldsymbol b,\ u(\boldsymbol c)=-\boldsymbol c\  \text{ \fr{
et }
 \en{  and 
}} \ u(\boldsymbol d)=-\boldsymbol d.}$}
%
\wrong{ $\vcenter{\displaystyle u(\boldsymbol a)=\boldsymbol a,\ u(\boldsymbol b)=\boldsymbol b,\ u(\boldsymbol c)=-2\boldsymbol c\  \text{ \fr{
et }
 \en{  and }} \ u(\boldsymbol d)=2\boldsymbol d.}$}
%
\wrong{ $\vcenter{\displaystyle u(\boldsymbol a)=-\boldsymbol a,\ u(\boldsymbol b)=\boldsymbol b,\ u(\boldsymbol c)=2\boldsymbol c\  \text{ \fr{
et }
 \en{  and }} \ u(\boldsymbol d)=2\boldsymbol d.}$}
%
\wrong{ $\vcenter{\displaystyle u(\boldsymbol a)=2\boldsymbol a,\ u(\boldsymbol b)=-\boldsymbol b,\ u(\boldsymbol c)=-2\boldsymbol c\  \text{ \fr{
et } \en{  and }} \ u(\boldsymbol d)=\boldsymbol d.}$}
%
\wronger
} 

{%Hint: 
}

{\fr{Pour tout $i$ de $\lb  1,4\rb $, le vecteur $u(\boldsymbol e_{i})$ est la $i^{\text{ème}}$ colonne de la matrice $A$.
Par ailleurs, puisque $u$ est linéaire, on peut écrire :}
\en{For every $i$ in $\lb  1,4\rb $, the vector $u(\boldsymbol e_{i})$ is the $i^{\text{th}}$ column of Matrix $A$.
Besides, since $u$ is linear, one can write :}
\begin{equation*}
\begin{align*}
\bullet\hspace{3ex} u(\boldsymbol a) &= -2u(\boldsymbol e_{1})- u(\boldsymbol e_{2})-u(\boldsymbol e_{3})-u(\boldsymbol e_{4})\\
 &= -2\sympy{C1}-\sympy{C2}-\sympy{C3}-\sympy{C4}%\\
 %&
 =\sympy{ae}\\
 &=-4\boldsymbol e_{1}-2\boldsymbol e_{2}-2\boldsymbol e_{3}-2\boldsymbol e_{4}
 =2\left(-2\boldsymbol e_{1}-\boldsymbol e_{2}-\boldsymbol e_{3}-\boldsymbol e_{4}\right)\\
&=2\boldsymbol a.
\end{align*}
\end{equation*}

Likewise, one can write:
\begin{equation*}
\begin{align*}
\bullet\hspace{3ex} u(\boldsymbol b) &= u(\boldsymbol e_{2})- u(\boldsymbol e_{4})\\
 &= \sympy{C2}-\sympy{C4}
 =\sympy{aa}
 =2\left(\boldsymbol e_{2}-\boldsymbol e_{4}\right)
 =2\boldsymbol b.
\end{align*}
\end{equation*}
and

\begin{equation*}
\begin{align*}
\bullet\hspace{3ex} u(\boldsymbol c) &= 2u(\boldsymbol e_{1}) + u(\boldsymbol e_{3}) + u(\boldsymbol e_{4})\\
 &= 2\sympy{C1}+\sympy{C3}+\sympy{C4}%\\
 %&
 =\sympy{az}\\
 & =-\left(2\boldsymbol e_{1}+\boldsymbol e_{3}+\boldsymbol e_{4}\right)
 =-\boldsymbol c.
\end{align*}
\end{equation*}
%
and finally,
%
\begin{equation*}
\begin{align*}
\bullet\hspace{3ex} u(\boldsymbol d) &= 3u(\boldsymbol e_{1})+u(\boldsymbol e_{3})+2u(\boldsymbol e_{4})\\
 &= 3\sympy{C1}+\sympy{C3}+2\sympy{C4}%\\
 %&
 =\sympy{aaa}\\
 &=-\left(3\boldsymbol e_{1}+\boldsymbol e_{3}+2\boldsymbol e_{4}\right)
 =-\boldsymbol d.
\end{align*}
\end{equation*}


}

{
logic: 30
abstraction: 20
reasoning: 20
calculation: 30
}




\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python

WPD=Matrix([[2,0,0,0],[0,2,0,0],[0,0,-1,0],[0,0,0,-1]])
WPDbis=Matrix([[1,0,0,0],[0,2,0,0],[0,0,-1,0],[0,0,0,-1]])
WPDter=Matrix([[2,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]])
WPDquart=Matrix([[2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]])
WPD=latex(WPD, mat_delim='', mat_str='pmatrix')
WPDbis=latex(WPDbis, mat_delim='', mat_str='pmatrix')
WPDter=latex(WPDter, mat_delim='', mat_str='pmatrix')
WPDquart=latex(WPDquart, mat_delim='', mat_str='pmatrix')
\end{python}


(ques3)=
\qcm{ \fr{On conserve les notations de la }
 \en{We keep the notations from }[\fr{question}\en{Question} $1$](#ques1) \fr{à }\en{to } [\fr{question}\en{Question} $2$](#ques2).%
 \fr{ Soit $u$ l'endomorphisme dont la representation matricielle, dans la base canonique,  est donnée par $A$. }
  \en{Let $u$ be the endomorphism, the matrix representation of which, in the standard basis, is given by $A$. }%
%
 \fr{On souhaite déterminer la matrice, notée $D$, représentant l'endomorphisme $u$ entre les bases $\boldsymbol \beta'$ à $\boldsymbol \beta'$.}
 \en{One wants to determine the matrix, denoted $D$, which represents $u$ between basis  $\boldsymbol \beta'$ and $\boldsymbol \beta'$.}%
 \fr{On peut écrire :}\en{ One can write that :}
}
{
\right{ $\displaystyle D:=\sympy{WPD}$.}
%
\wrong{ $\displaystyle D:=\sympy{WPDbis}$.}
%
\wrong{ $\displaystyle D:=\sympy{WPDter}$.}
%
\wrong{ $\displaystyle D:=\sympy{WPDquart}$.}
%
\wronger
} 

{%Hint: 
}
{ \fr{Par définition de la matrice $D$, on a l'égalité :}
 \en{By very definition of $D$, one has the equality :}
 $D=\left[ u \right]^{\boldsymbol \beta'}_{\boldsymbol \beta'}$.
 %
 \fr{Compte-tenu des résultats obtenus à la  [question $2$](#ques2), on put écrire :}%
 \en{In view of the results obtained at  [Question $2$](#ques2), one can write :}


\begin{equation*}
\begin{align*}
D
=
\left[ u \right]^{\boldsymbol \beta}_{\boldsymbol \beta'}
=
%
\begin{array}{rrrrr}
\begin{array}{r}
&\\
\left(\begin{array}{r}
&\\
&\\
&
\end{array}\right. 
\end{array}
\hspace{-13ex} 
&  \begin{array}{r}
&\textcolor{red}{u(\bs a)}\\
&\py{D[0,0]}\\
&\py{D[1,0]}\\
&\py{D[2,0]}\\
&\py{D[3,0]}
\end{array} &  \begin{array}{r}
&\textcolor{red}{u(\bs b)}\\
&\py{D[0,1]}\\
&\py{D[1,1]}\\
&\py{D[2,1]}\\
&\py{D[3,1]}
\end{array} & \begin{array}{r}
&\textcolor{red}{u(\bs c)}\\
&\py{D[0,2]}\\
&\py{D[1,2]}\\
&\py{D[2,2]}\\
&\py{D[3,2]}
\end{array} & \begin{array}{r}
&\textcolor{red}{u(\bs d)}\\
&\py{D[0,3]}\\
&\py{D[1,3]}\\
&\py{D[2,3]}\\
&\py{D[3,3]}
\end{array} \hspace{-8ex}  & \begin{array}{r}
& \\
\left.\begin{array}{r}
&\\
&\\
&
\end{array}\right) 
\end{array}  &\hspace{-9ex} \begin{array}{r}
& \\
&\textcolor{purple}{\bs a}\\
&\textcolor{purple}{\bs b}\\
&\textcolor{purple}{\bs c}\\
&\textcolor{purple}{\bs d}
\end{array} 
\end{array}
%
\end{align*}
\end{equation*}

}
{
logic: 30
abstraction: 20
reasoning: 20
calculation: 30
}

\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
Psecpnew= Matrix([[-2,0,2,3],[-1,1,0,0],[-1,0,1,1],[-1,-1,1,2]])
Psecpnewinv= Psecpnew.inv()
Psecpnewtrafiquee= trafiquematricerestantinversible(Matrix([[-2,0,2,3],[-1,1,0,0],[-1,0,1,1],[-1,-1,1,2]]))
Psecpnewtrafiqueeinv= Psecpnewtrafiquee.inv()
ced=Psecpnew.inv()
Pinvsectrafiquee= trafiquematricerestantinversible(ced)
Pezdezdpnewtrafiqueeinv= Pinvsectrafiquee.inv()
Psecpnew=latex(Psecpnew, mat_delim='', mat_str='pmatrix')
Psecpnewinv=latex(Psecpnewinv, mat_delim='', mat_str='pmatrix')
Psecpnewtrafiquee=latex(Psecpnewtrafiquee, mat_delim='', mat_str='pmatrix')
Psecpnewtrafiqueeinv=latex(Psecpnewtrafiqueeinv, mat_delim='', mat_str='pmatrix')
ced=latex(ced, mat_delim='', mat_str='pmatrix')
Pinvsectrafiquee=latex(Pinvsectrafiquee, mat_delim='', mat_str='pmatrix')
Pezdezdpnewtrafiqueeinv=latex(Pezdezdpnewtrafiqueeinv, mat_delim='', mat_str='pmatrix')

\end{python}






(ques4)=
\qcm{ \fr{On conserve les notations de la }
 \en{We keep the notations from }[\fr{question}\en{Question} $1$](#ques1) \fr{à }\en{to } [\fr{question}\en{Question} $3$](#ques3).%
%
 \fr{On souhaite déterminer la matrice, notée $P$, de changement de base de
$\boldsymbol \beta$ à $\boldsymbol \beta'$.}
 \en{One wants to determine the change of basis matrix, denoted $P$, from $\boldsymbol \beta$ to $\boldsymbol \beta'$.}%
 \fr{On peut écrire :}
 \en{One can write that :}
}
{
\right{$\displaystyle P:=\sympy{Psecpnew}$ $\hspace{10ex}$ $\&\hspace{10ex}$ $\displaystyle P^{-1}=\sympy{Psecpnewinv}$,}%\bareme{1}

\wrong{$\displaystyle P:=\sympy{Psecpnewtrafiquee}$ $\hspace{10ex} \&\hspace{10ex}$ $\displaystyle P^{-1}=\sympy{Psecpnewtrafiqueeinv}$,}%\bareme{-0.25}

\wrong{$\displaystyle P:=\sympy{Pezdezdpnewtrafiqueeinv}$ $\hspace{10ex} \&\hspace{10ex}$ $\displaystyle P^{-1}=\sympy{Pinvsectrafiquee}$.}%\bareme{-0.25}

%Pezdezdpnewtrafiqueeinv
%Pinvsectrafiquee
\wronger 

% Ajoutez autant de réponses que nécessaire

}
{ % Indice: Vous pouvez écrire une indication ci-dessous.

}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 \fr{Par définition, on a:}
 \en{ By definition, one can write:}
%
\begin{equation*}
\begin{align*}
 P:=[{\mathrm{Id}}_{\bfR^{4}}]_{\boldsymbol \beta'}^{\boldsymbol e}
 =
[{[\boldsymbol a]}^{\boldsymbol e}, {[\boldsymbol b]}^{\boldsymbol e}, {[\boldsymbol c]}^{\boldsymbol e}, {[\boldsymbol d]}^{\boldsymbol e}]
=
\sympy{Psecpnew}.
\end{align*}
\end{equation*}
 \fr{De la question précédente, on déduite aisément que $P$ est inversible. On a alors :}
 \en{ From the previous question, we easily deduce that $P$ is invertible and that :}
\begin{equation*}
\begin{align*}
 P^{-1}
 =
\sympy{Psecpnewinv}.
\end{align*}
\end{equation*}

}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}







\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
A4= Matrix([[1,4,4],[-1,-3,-3],[0,2,3]])
A4= Matrix([[-7,6,6,6],[0,2,0,0],[-3,3,2,3],[-6,3,6,5]])
A4=latex(A4, mat_delim='', mat_str='pmatrix')
\end{python}





(ques5)=
\qcm{ \fr{On conserve les notations de la }
 \en{We keep the notations from }[\fr{question}\en{Question} $1$](#ques1) \fr{à }\en{to } [\fr{question}\en{Question} $4$](#ques4).%
%
\fr{On souhaite déterminer le lien reliant les matrices $A$ et $D$, si tant est qu'un tel lien existe. On peut écrire:}%
 \en{One wants to determine, if it exists, the link between matrices $A$ and $D$. One can write:}
%
}
{
\right{$\displaystyle D=P^{-1}AP$,}
%
\wrong{$\displaystyle D=PAP^{-1}$,}
%
\wrong{$\displaystyle D=APP^{-1}$,}
%
\wrong{$\displaystyle D=PP^{-1}A$.}
%
\wronger

% Ajoutez autant de réponses que nécessaire

}
{ % Indice: Vous pouvez écrire une indication ci-dessous.

}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
\fr{ Les matrices $A$ et $D$ représentent le même endormorphisme $u$. $A$ est la matrice représentative de $u$, de la base $\boldsymbol{\beta}$ dans elle même, tandis que $D$  est la matrice représentative de $u$, de la base $\boldsymbol{\beta'}$ dans elle même. On a donc  :}
 \en{ Both $A$ and $D$ represent the same endomorphism $u$. $A$ represents $u$ from basis $\boldsymbol e$ to $\boldsymbol{\beta}$, while $D$ represents $u$ from basis $\boldsymbol \beta'$ to basis $\boldsymbol \beta'$. We hence know that :}
\begin{equation*}
 D=
 \left[ u \right]^{\boldsymbol \beta'}_{\boldsymbol \beta'}
 =
  [{\mathrm{Id}}_{\bfR^{4}}]_{\boldsymbol{\beta}}^{\boldsymbol \beta'}
 \left[ u \right]^{\boldsymbol{\beta}}_{\boldsymbol{\beta}}
 [{\mathrm{Id}}_{\bfR^{4}}]_{\boldsymbol \beta'}^{\boldsymbol{\beta}}
 =
 P^{-1}AP.
\end{equation*}
Note that one can easily verify that:
\begin{equation*}
\begin{align*}
P^{-1}AP
&=\sympy{Psecpnewinv}\cdot \sympy{A4}\cdot \sympy{Psecpnew}\\
&=
\sympy{WPD}
=
D.
\end{align*}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}




\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
Psecpnew= Matrix([[-2,0,2,3],[-1,1,0,0],[-1,0,1,1],[-1,-1,1,2]])
Psecpnewinv= Psecpnew.inv()
Psecpnewtrafiquee= trafiquematricerestantinversible(Matrix([[-2,0,2,3],[-1,1,0,0],[-1,0,1,1],[-1,-1,1,2]]))
Psecpnewtrafiqueeinv= Psecpnewtrafiquee.inv()
ced=Psecpnew.inv()
Pinvsectrafiquee= trafiquematricerestantinversible(ced)
Pezdezdpnewtrafiqueeinv= Pinvsectrafiquee.inv()
pinv=P.inv()
n =Symbol('n')
A4= Matrix([[1,4,4],[-1,-3,-3],[0,2,3]])
A4= Matrix([[-7,6,6,6],[0,2,0,0],[-3,3,2,3],[-6,3,6,5]])
FDS=Psecpnew*((Psecpnewinv*A4*Psecpnew)**n)*Psecpnewinv
FDSU=FDS+mat_element(FDS.rows,FDS.cols,2,1)
FDSV=FDS+mat_element(FDS.rows,FDS.cols,2,3)
FDSW=FDS+mat_element(FDS.rows,FDS.cols,2,4)
a=Psecpnew*((Psecpnewinv*A4*Psecpnew)**n)*Psecpnewinv
a=latex(a, mat_delim='', mat_str='pmatrix')
FDSW=latex(FDSW, mat_delim='', mat_str='pmatrix')
FDSV=latex(FDSV, mat_delim='', mat_str='pmatrix')
FDSU=latex(FDSU, mat_delim='', mat_str='pmatrix')
h=P*(D**n)*P.inv()

Pi=latex(P, mat_delim='', mat_str='pmatrix')
dn=D**n
dn=latex(dn, mat_delim='', mat_str='pmatrix')

h=latex(h, mat_delim='', mat_str='pmatrix')
pinv=latex(pinv, mat_delim='', mat_str='pmatrix')
\end{python}






(ques6)=
\qcm{ \fr{On conserve les notations de la }
 \en{We keep the notations from }[\fr{question}\en{Question} $1$](#ques1) \fr{à }\en{to } [\fr{question}\en{Question} $5$](#ques5).%
%
 \fr{On souhaite à présent calculer, pour tout entier natural $n$, $A^{n}$:}
 \en{One now wants to determine, for every integer $n$ in $\fN$, $A^{n}$:}%
 \fr{On a :}
 \en{One can write :}
}
{
\right{$\displaystyle A^{n}=\sympy{a}.$}%\bareme{2}



\wrong{$\displaystyle A^{n}=\sympy{FDSU}.$}%\bareme{-0.5}



\wrong{$\displaystyle A^{n}=\sympy{FDSV}.$}%\bareme{-0.5}



\wrong{$\displaystyle A^{n}=\sympy{FDSW}.$}%\bareme{-0.5}



\wronger

% Ajoutez autant de réponses que nécessaire

}
{ % Indice: Vous pouvez écrire une indication ci-dessous.

}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
It is clear that $A^{0}=I_{4}$ and that $A^{1}=A$. For every $n$ in $\fN\backslash\{0,1\}$, we can write:
\begin{equation*}
\begin{align*}
 A^{n}&={\left(P\cdot D\cdot P^{-1}\right)}^{n}=\left(P\cdot D\cdot P^{-1}\right) \cdot \left(P\cdot D\cdot P^{-1}\right) \cdots \left(P\cdot D\cdot P^{-1}\right)
 =
 P \cdot D^{n} \cdot P^{-1}\\
 &=
 \sympy{Pi}\cdot \sympy{dn}\cdot \sympy{pinv}\\
 &=
  \sympy{h}.
\end{align*}
\end{equation*}
\fr{Finalement, nous voyons que la formume précedente est aussie vraie lorsque $n$ appartient à $\{0,1\}$. On a ainsi prouvé que :}
\en{Finally, we see that the previous formula holds also for $n$ in $\{0,1\}$. Thus, we have proved that :}

\begin{equation*}
\begin{align*}
\fbox{
$
 A^{n}
 =
  \sympy{h}
$, for all $n$ in $\fN$.
}
\end{align*}
\end{equation*}


}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}



}

\end{exercise}














