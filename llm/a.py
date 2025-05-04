def pxsl_pow(x, n=1, opt=0, displaystyle=True):
    """
    Fonction permettant d'écrire le nombre x entouré de parenthèses 
    lorsqu'il est négatif ou irrationnel avec deux termes (par ex : 1+sqrt(2) ou 3sqrt(2))
    Ne fonctionne pas pour des valeurs numériques non simplifiées (par ex : 1+3 ou 3*3/2)

    Version
    -------
    13/02/25
    
    Paramètres
    ----------
    x : nombre ou expression
        La base à élever à la puissance n
    n : int, optional
        L'exposant (défaut: 1)
    opt : int, optional
        Option de formatage (défaut: 0)
        0: formatage standard
        1: simplifie l'affichage pour x=1, x=0 ou n=1
        2: simplifie davantage et renvoie une chaîne vide pour x=0
    displaystyle : bool, optional
        Si True, utilise \displaystyle pour les fractions (défaut: False)
    
    Retour
    ------
    str
        retourne l'expression en latex
    """
    
    # Préparation de l'expression LaTeX selon le mode displaystyle
    if displaystyle:
        latex_x = r"\displaystyle " + latex(x)
        print("latex\n")
    else:
        latex_x = latex(x)
        print("no_latex\n")
    
    # Cas où x est une expression (Add ou Mul) ou nombre négatif:
    if isinstance(x, Add) or isinstance(x, Mul) :
        if n == 1 :
            return myst(r"""\left(\py{latex_x}\right)""", globals(), locals())
        else:
            return myst(r"""\left(\py{latex_x}\right)^{\py{n}}""", globals(), locals())
    # Cas où x est un Rational
    elif isinstance(x,Rational) and x.q!=1:
        if n == 1 : # Pas de parenthèses quand n=1
            return myst(r"""\py{latex_x}""", globals(), locals())
        else: # Parenthèses quand n différent de 1
            print("rational")
            return myst(r"""\left(\py{latex_x}\right)^{\py{n}}""", globals(), locals())
    # Cas où x est un Symbol:
    elif isinstance(x,Symbol):
        if n == 1:
            return myst(r"""\py{latex_x}""", globals(), locals())
        else:
            return myst(r"""\py{latex_x}^{\py{n}}""", globals(), locals())
    # Cas où x est strictement négatif
    elif x<0:
        if n == 1:
            return myst(r"""\left(\py{latex_x}\right)""", globals(), locals())
        else:
            return myst(r"""\left(\py{latex_x}\right)^{\py{n}}""", globals(), locals())
    # Cas où x est un nombre positif ou nul
    else:
        # Option 0: formatage standard
        if opt == 0:
            if n == 1:
                return myst(r"""\py{latex_x}""", globals(), locals())
            else:
                return myst(r"""\py{latex_x}^{\py{n}}""", globals(), locals())
        
        # Option 1: simplifie pour x=0, x=1 ou n=1
        elif opt == 1:
            if x == 1 or x == 0 or n == 1:
                return myst(r"""\py{latex_x}""", globals(), locals())
            else:
                return myst(r"""\py{latex_x}^{\py{n}}""", globals(), locals())
        
        # Option 2: simplifie davantage, chaîne vide pour x=0
        else:  # opt == 2 ou autres valeurs
            if x == 0:
                return myst(r""" """, globals(), locals())
            elif x == 1 or n == 1:
                return myst(r"""\py{latex_x}""", globals(), locals())
            else:
                return myst(r"""\py{latex_x}^{\py{n}}""", globals(), locals())
