from tkinter import *

def addToList():
    equa=equanumVar.get()
    cor=check2Var.get()
    
    if cor=="CORRECT":
        if equa==1:
            equaList.insert(END,"2Mg+O2→2MgO")
        elif equa==2:
            equaList.insert(END,"3Fe+2O2→Fe3O4")
        elif equa==3:
            equaList.insert(END,"2Cu+O2→2CuO")
        elif equa==4:
            equaList.insert(END,"4Al+3O2→2Al2O3")
        elif equa==5:
            equaList.insert(END,"2H2+O2→2H2O")
        elif equa==6:
            equaList.insert(END,"4P+5O2→2P2O5")
        elif equa==7:
            equaList.insert(END,"S+O2→SO2")
        elif equa==8:
            equaList.insert(END,"2C+O2→2CO")
        elif equa==9:
            equaList.insert(END,"2H2O→2H2+O2")
        elif equa==10:
            equaList.insert(END,"2KClO3→2KCl+3O2")
        elif equa==11:
            equaList.insert(END,"H2CO3→H2O+CO2")
        elif equa==12:
            equaList.insert(END,"CaCO3→CaO+CO2")
        elif equa==13:
            equaList.insert(END,"H2+CuO→Cu+H2O")
        elif equa==14:
            equaList.insert(END,"C+2CuO→2Cu+CO2")
        elif equa==15:
            equaList.insert(END,"CO+CuO→Cu+CO2")
        elif equa==16:
            equaList.insert(END,"3Fe2O3+2C→4Fe+3CO2")
        elif equa==17:
            equaList.insert(END,"3CO+Fe2O3→2Fe+3CO2")
        elif equa==18:
            equaList.insert(END,"Fe2O3+3H2SO4→Fe2(SO4)3+3H2O")
        elif equa==19:
            equaList.insert(END,"CuSO4+Fe→FeSO4+Cu")
        elif equa==20:
            equaList.insert(END,"CuSO4+Zn→ZnSO4+Cu")
        elif equa==21:
            equaList.insert(END,"CaO+2HCl→CaCl2+H2O")
        changeVar.set('')
    elif cor=="INCORRECT":
        changeVar.set('please select the correct number and check')
    else:
        changeVar.set('please check your answers first')
        
    

def showMMandNM():
    nmLabelVar.set('')
    mmLabelVar.set('')
    mm=molarMassVar.get()
    nm=numMolesVar.get()
    equ=equanumVar.get()
    
    if mm==1 and nm==1:
        if equ==1:
            nmLabelVar.set('2+2→4')
            mmLabelVar.set('24+32→28')
        elif equ==2:
            nmLabelVar.set('3+4→7')
            mmLabelVar.set('56+32→231')
        elif equ==3:
            nmLabelVar.set('2+2→4')
            mmLabelVar.set('64+32→80')
        elif equ==4:
            nmLabelVar.set('4+6→10')
            mmLabelVar.set('27+32→102')
        elif equ==5:
            nmLabelVar.set('4+2→6')
            mmLabelVar.set('2+32→18')
        elif equ==6:
            nmLabelVar.set('4+10→14')
            mmLabelVar.set('31+32→284')
        elif equ==7:
            nmLabelVar.set('1+2→3')
            mmLabelVar.set('32+32→64')
        elif equ==8:
            nmLabelVar.set('2+2→4')
            mmLabelVar.set('12+32→28')
        elif equ==9:
            nmLabelVar.set('6→4+2')
            mmLabelVar.set('18→2+16')
        elif equ==10:
            nmLabelVar.set('10→4+6')
            mmLabelVar.set('123→75+16')
        elif equ==11:
            nmLabelVar.set('6→3+3')
            mmLabelVar.set('62→18+44')
        elif equ==12:
            nmLabelVar.set('5→2+3')
            mmLabelVar.set('100→56+44')
        elif equ==13:
            nmLabelVar.set('2+2→1+3')
            mmLabelVar.set('2+80→64+18')
        elif equ==14:
            nmLabelVar.set('1+4→2+3')
            mmLabelVar.set('12+80→64+44')
        elif equ==15:
            nmLabelVar.set('2+2→1+3')
            mmLabelVar.set('28+80→64+44')
        elif equ==16:
            nmLabelVar.set('3+10→4+9')
            mmLabelVar.set('12+160→56+44')
        elif equ==17:
            nmLabelVar.set('6+5→2+9')
            mmLabelVar.set('28+160→56+44')
        elif equ==18:
            nmLabelVar.set('5+21→17+9')
            mmLabelVar.set('160+98→400+18')
        elif equ==19:
            nmLabelVar.set('2+4→3+3')
            mmLabelVar.set('56+159→152+64')
        elif equ==20:
            nmLabelVar.set('1+6→6+1')
            mmLabelVar.set('65+159→161+64')
        elif equ==21:
            nmLabelVar.set('2+4→3+3')
            mmLabelVar.set('56+32→111+18')
        else:
            nmLabelVar.set('')
            mmLabelVar.set('')
            
    elif nm==1:
        if equ==1:
            nmLabelVar.set('2+2→4')
        elif equ==2:
            nmLabelVar.set('3+4→7')
        elif equ==3:
            nmLabelVar.set('2+2→4')
        elif equ==4:
            nmLabelVar.set('4+6→10')
        elif equ==5:
            nmLabelVar.set('4+2→6')
        elif equ==6:
            nmLabelVar.set('4+10→14')
        elif equ==7:
            nmLabelVar.set('1+2→3')
        elif equ==8:
            nmLabelVar.set('2+2→4')
        elif equ==9:
            nmLabelVar.set('6→4+2')
        elif equ==10:
            nmLabelVar.set('10→4+6')
        elif equ==11:
            nmLabelVar.set('6→3+3')
        elif equ==12:
            nmLabelVar.set('5→2+3')
        elif equ==13:
            nmLabelVar.set('2+2→1+3')
        elif equ==14:
            nmLabelVar.set('1+4→2+3')
        elif equ==15:
            nmLabelVar.set('2+2→1+3')
        elif equ==16:
            nmLabelVar.set('3+10→4+9')
        elif equ==17:
            nmLabelVar.set('6+5→2+9')
        elif equ==18:
            nmLabelVar.set('5+21→17+9')
        elif equ==19:
            nmLabelVar.set('2+4→3+3')
        elif equ==20:
            nmLabelVar.set('1+6→6+1')
        elif equ==21:
            nmLabelVar.set('2+4→3+3')
        else:
            nmLabelVar.set('')
        
    elif mm==1:
        if equ==1:
            mmLabelVar.set('24+32→28')
        elif equ==2:
            mmLabelVar.set('56+32→231')
        elif equ==3:
            mmLabelVar.set('64+32→80')
        elif equ==4:
            mmLabelVar.set('27+32→102')
        elif equ==5:
            mmLabelVar.set('2+32→18')
        elif equ==6:
            mmLabelVar.set('31+32→284')
        elif equ==7:
            mmLabelVar.set('32+32→64')
        elif equ==8:
            mmLabelVar.set('12+32→28')
        elif equ==9:
            mmLabelVar.set('18→2+16')
        elif equ==10:
            mmLabelVar.set('123→75+16')
        elif equ==11:
            mmLabelVar.set('62→18+44')
        elif equ==12:
            mmLabelVar.set('100→56+44')
        elif equ==13:
            mmLabelVar.set('2+80→64+18')
        elif equ==14:
            mmLabelVar.set('12+80→64+44')
        elif equ==15:
            mmLabelVar.set('28+80→64+44')
        elif equ==16:
            mmLabelVar.set('12+160→56+44')
        elif equ==17:
            mmLabelVar.set('28+160→56+44')
        elif equ==18:
            mmLabelVar.set('160+98→400+18')
        elif equ==19:
            mmLabelVar.set('56+159→152+64')
        elif equ==20:
            mmLabelVar.set('65+159→161+64')
        elif equ==21:
            mmLabelVar.set('56+32→111+18')
        else:
            mmLabelVar.set('')
            
def defineType():

    equaType=equationTypeVar.get()
    changeVar.set('')
    check1Var.set("")
    correct1Var.set("")
    correct1Var2.set("")
    numMolesVar.set(0)
    molarMassVar.set(0)
    
    global synthesisOption
    global synLabel
    global syn3Label
    global syndashLabel
    global synEntry
    global decOption
    global decdashLabel
    global dec1Entry
    global decPlusLabel
    global dec2Entry
    global disdashLabel
    global dis1Entry
    global dis2Entry
    global disPlus1Label
    global disPlus2Label
    global dis1Option
    global dis2Option
    global synthesisOptionVar
    global synEntryVar
    global decOptionVar
    global dec1EntryVar
    global dec2EntryVar
    global dis1EntryVar
    global dis2EntryVar
    global dis1OptionVar
    global dis2OptionVar

    
    if equaLabelVar2.get()==1:
        synspin1.grid_forget()
        labelplus.grid_forget()
        labeldash.grid_forget()
        synlabel1.grid_forget()
        synspin2.grid_forget()
        synlabel2.grid_forget()
        synspin3.grid_forget()
        synlabel3.grid_forget()
    elif equaLabelVar2.get() == 2:
        labelplus.grid_forget()
        labeldash.grid_forget()
        decspin1.grid_forget()
        declabel1.grid_forget()
        decspin1.grid_forget()
        declabel1.grid_forget()
        decspin2.grid_forget()
        declabel2.grid_forget()
        decspin3.grid_forget()
        declabel3.grid_forget()
    elif equaLabelVar2.get()==3:
        labelplus.grid_forget()
        labeldash.grid_forget()
        labelplus1.grid_forget()
        disspin1.grid_forget()
        dislabel1.grid_forget()
        disspin2.grid_forget()
        dislabel2.grid_forget()
        disspin3.grid_forget()
        dislabel3.grid_forget()
        disspin4.grid_forget()
        dislabel4.grid_forget()
                
    if equaType=='synthesis':
        clearLabel.grid(row=2,column=10,ipadx=100)
        importEquation.grid(row=7,column=5,sticky=E)
        
        if equaLabelVar.get() == 2:
            decOption.grid_forget()
            decdashLabel.grid_forget()
            dec1Entry.grid_forget()
            decPlusLabel.grid_forget()
            dec2Entry.grid_forget()
        elif equaLabelVar.get()==3:
            disdashLabel.grid_forget()
            dis1Entry.grid_forget()
            dis2Entry.grid_forget()
            disPlus1Label.grid_forget()
            disPlus2Label.grid_forget()
            dis1Option.grid_forget()
            dis2Option.grid_forget()

        syn = ['Mg','Fe','Cu','Al','H2','P','S','C']
        synthesisOptionVar=StringVar()
        synthesisOptionVar.set('Mg')
        synthesisOption = OptionMenu(mainframe, synthesisOptionVar, *syn)
        synLabel = Label(mainframe, text="+",padx=40)
        syn3Label = Label(mainframe, text="O2")
        syndashLabel = Label(mainframe,text="→",padx=40)
        synEntryVar=StringVar()
        synEntry=Entry(mainframe,text="",textvariable=synEntryVar)
        synthesisOption.grid(row=6,column=1)
        synLabel.grid(row=6,column=2)
        syn3Label.grid(row=6,column=3)
        syndashLabel.grid(row=6,column=4)
        synEntry.grid(row=6,column=5)
        equaLabelVar.set(1)
    
    elif equaType=='decomposition':
        clearLabel.grid(row=2,column=10,ipadx=100)
        importEquation.grid(row=7,column=5,sticky=E)

        if equaLabelVar.get() == 1:
            synthesisOption.grid_forget()
            synLabel.grid_forget()
            syn3Label.grid_forget()
            syndashLabel.grid_forget()
            synEntry.grid_forget()
        elif equaLabelVar.get()==3:
            disdashLabel.grid_forget()
            dis1Entry.grid_forget()
            dis2Entry.grid_forget()
            disPlus1Label.grid_forget()
            disPlus2Label.grid_forget()
            dis1Option.grid_forget()
            dis2Option.grid_forget()

        dec = ['H2O','KClO3','H2CO3','CaCO3']
        decOptionVar=StringVar()
        decOptionVar.set('H2O')
        decOption = OptionMenu(mainframe, decOptionVar, *dec)
        decdashLabel = Label(mainframe,text="→",padx=40)
        dec1EntryVar=StringVar()
        dec1Entry=Entry(mainframe,text="",textvariable=dec1EntryVar)
        decPlusLabel = Label(mainframe, text="+",padx=40)
        dec2EntryVar=StringVar()
        dec2Entry=Entry(mainframe,text="",textvariable=dec2EntryVar)
        decOption.grid(row=6,column=1)
        decdashLabel.grid(row=6,column=2)
        dec1Entry.grid(row=6,column=3)
        decPlusLabel.grid(row=6,column=4)
        dec2Entry.grid(row=6,column=5)
        equaLabelVar.set(2)
     
    elif equaType=='displacement':
        clearLabel.grid_forget()
        importEquation.grid(row=7,column=7,sticky=E)

        if equaLabelVar.get() == 1:
            synthesisOption.grid_forget()
            synLabel.grid_forget()
            syn3Label.grid_forget()
            syndashLabel.grid_forget()
            synEntry.grid_forget()
        elif equaLabelVar.get() == 2:
            decOption.grid_forget()
            decdashLabel.grid_forget()
            dec1Entry.grid_forget()
            decPlusLabel.grid_forget()
            dec2Entry.grid_forget()

        dis1 = ['H2','C','CO','Fe','Zn','CaO','H2SO4']
        dis2 = ['Fe2O3','CuSO4','HCl','CuO']
        dis1OptionVar=StringVar()
        dis1OptionVar.set('H2')
        dis1Option = OptionMenu(mainframe, dis1OptionVar, *dis1)
        dis2OptionVar=StringVar()
        dis2OptionVar.set('CuO')
        dis2Option = OptionMenu(mainframe,dis2OptionVar,*dis2)
            
        disdashLabel = Label(mainframe,text="→",padx=40)
        dis1EntryVar=StringVar()
        dis1Entry=Entry(mainframe,text="",textvariable=dis1EntryVar)
        dis2EntryVar=StringVar()
        dis2Entry=Entry(mainframe,text="",textvariable=dis2EntryVar)
        disPlus1Label = Label(mainframe, text="+",padx=40)
        disPlus2Label = Label(mainframe, text="+",padx=40)
        dis1Option.grid(row=6,column=1)
        disPlus1Label.grid(row=6,column=2)
        dis2Option.grid(row=6,column=3)
        disdashLabel.grid(row=6,column=4)
        dis1Entry.grid(row=6,column=5)
        disPlus2Label.grid(row=6,column=6)
        dis2Entry.grid(row=6,column=7)
        equaLabelVar.set(3)

def check1():
    equaType=equaLabelVar.get()
    
    if equaType==1:
        syn1=synthesisOptionVar.get()
        synE=synEntryVar.get()
        if syn1=='Mg':
            if synE=='MgO':
                check1Var.set("CORRECT")
            else:
                check1Var.set("INCORRECT")
        elif syn1=='Fe':
            if synE=='Fe3O4':
                check1Var.set("CORRECT")
            else:
                check1Var.set("INCORRECT")
        elif syn1=='Cu':
            if synE=='CuO':
                check1Var.set("CORRECT")
            else:
                check1Var.set("INCORRECT")
        elif syn1=='Al':
            if synE=='Al2O3':
                check1Var.set("CORRECT")
            else:
                check1Var.set("INCORRECT")
        elif syn1=='H2':
            if synE=='H2O':
                check1Var.set("CORRECT")
            else:
                check1Var.set("INCORRECT")
        elif syn1=='P':
            if synE=='P2O5':
                check1Var.set("CORRECT")
            else:
                check1Var.set("INCORRECT")
        elif syn1=='S':
            if synE=='SO2':
                check1Var.set("CORRECT")
            else:
                check1Var.set("INCORRECT")
        elif syn1=='C':
            if synE=='C2O':
                check1Var.set("CORRECT")
            else:
                check1Var.set("INCORRECT")
    elif equaType==2:
        dec=decOptionVar.get()
        decE1=dec1EntryVar.get()
        decE2=dec2EntryVar.get()
        if dec=='H2O':
            if decE1=='H2':
                if decE2=='O2':
                    check1Var.set("CORRECT")
                else:
                    check1Var.set("INCORRECT")
            elif decE1=='O2':
                if decE2=='H2':
                    check1Var.set("CORRECT")
                else:
                    check1Var.set("INCORRECT")
            else:
                check1Var.set("INCORRECT")
        elif dec=='KClO3':
            if decE1=='KCl':
                if decE2=='O2':
                    check1Var.set("CORRECT")
                else:
                    check1Var.set("INCORRECT")
            elif decE1=='O2':
                if decE2=='KCl':
                    check1Var.set("CORRECT")
                else:
                    check1Var.set("INCORRECT")
            else:
                check1Var.set("INCORRECT")
        elif dec=='H2CO3':
            if decE1=='H2O':
                if decE2=='CO2':
                    check1Var.set("CORRECT")
                else:
                    check1Var.set("INCORRECT")
            elif decE1=='CO2':
                if decE2=='H2O':
                    check1Var.set("CORRECT")
                else:
                    check1Var.set("INCORRECT")
            else:
                check1Var.set("INCORRECT")
        elif dec=='CaCO3':
            if decE1=='CaO':
                if decE2=='CO2':
                    check1Var.set("CORRECT")
                else:
                    check1Var.set("INCORRECT")
            elif decE1=='CO2':
                if decE2=='CaO':
                    check1Var.set("CORRECT")
                else:
                    check1Var.set("INCORRECT")
            else:
                check1Var.set("INCORRECT")
    elif equaType==3:
        dis1=dis1OptionVar.get()
        dis2=dis2OptionVar.get()
        disE1=dis1EntryVar.get()
        disE2=dis2EntryVar.get()
        if dis2=='CuO':
            if dis1=='H2':
                if disE1=='H2O':
                    if disE2=='Cu':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                elif disE1=='Cu':
                    if disE2=='H2O':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                else:
                    check1Var.set("INCORRECT")
            elif dis1=='C':
                if disE1=='CO2':
                    if disE2=='Cu':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                elif disE1=='Cu':
                    if disE2=='CO2':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                else:
                    check1Var.set("INCORRECT")
            elif dis1=='CO':
                if disE1=='CO2':
                    if disE2=='Cu':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                elif disE1=='Cu':
                    if disE2=='CO2':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                else:
                    check1Var.set("INCORRECT")
            else:
                check1Var.set("DON'T REACT")
        elif dis2=='Fe2O3':
            if dis1=='C':
                if disE1=='CO2':
                    if disE2=='Fe':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                elif disE1=='Fe':
                    if disE2=='CO2':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                else:
                    check1Var.set("INCORRECT")
            elif dis1=='CO':
                if disE1=='CO2':
                    if disE2=='Fe':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                elif disE1=='Fe':
                    if disE2=='CO2':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                else:
                    check1Var.set("INCORRECT")
            elif dis1=='H2SO4':
                if disE1=='Fe2(SO4)3':
                    if disE2=='H2O':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                elif disE1=='H2O':
                    if disE2=='Fe2(SO4)3':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                else:
                    check1Var.set("INCORRECT")
            else:
                check1Var.set("DON'T REACT")
        elif dis2=='CuSO4':
            if dis1=='Fe':
                if disE1=='FeSO4':
                    if disE2=='Cu':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                elif disE1=='Cu':
                    if disE2=='FeSO4':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                else:
                    check1Var.set("INCORRECT")
            elif dis1=='Zn':
                if disE1=='ZnSO4':
                    if disE2=='Cu':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                elif disE1=='Cu':
                    if disE2=='ZnSO4':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                else:
                    check1Var.set("INCORRECT")
            else:
                check1Var.set("DON'T REACT")
        elif dis2=='HCl':
            if dis1=='CaO':
                if disE1=='CaCl2':
                    if disE2=='H2O':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                elif disE1=='H2O':
                    if disE2=='CaCl2':
                        check1Var.set("CORRECT")
                    else:
                        check1Var.set("INCORRECT")
                else:
                    check1Var.set("INCORRECT")
            else:
                check1Var.set("DON'T REACT") 

def correct1():
    equaType=equaLabelVar.get()
    if equaType==1:
        syn1=synthesisOptionVar.get()
        if syn1=="Mg":
            correct1Var.set("Mg+O2→MgO")
        elif syn1=="Fe":
            correct1Var.set("Fe+O2→Fe3O4")
        elif syn1=="Cu":
            correct1Var.set("Cu+O2→CuO")
        elif syn1=="Al":
            correct1Var.set("Al+O2→Al2O3")
        elif syn1=="H2":
            correct1Var.set("H2+O2→H2O")
        elif syn1=="P":
            correct1Var.set("P+O2→P2O5")
        elif syn1=="S":
            correct1Var.set("S+O2→SO2")
        elif syn1=="C":
            correct1Var.set("C+O2→CO")
    elif equaType==2:
        dec=decOptionVar.get()
        if dec=="H2O":
            correct1Var.set("H2O→H2+O2")
        elif dec=="KClO3":
            correct1Var.set("KClO3→KCl+O2")
        elif dec=="H2CO3":
            correct1Var.set("H2CO3→H2O+CO2")
        elif dec=="CaCO3":
            correct1Var.set("CaCO3→CaO+CO2")
    elif equaType==3:
        dis1=dis1OptionVar.get()
        dis2=dis2OptionVar.get()
        if dis2=='CuO':
            if dis1=='H2':
                correct1Var.set("H2+CuO→Cu+H2O")
                correct1Var2.set("")
            elif dis1=='C':
                correct1Var.set("C+CuO→Cu+CO2")
                correct1Var2.set("")
            elif dis1=='CO':
                correct1Var.set("CO+CuO→Cu+CO2")
                correct1Var2.set("")
            else:
                correct1Var.set("Please select a valid reaction")
                correct1Var2.set(":CuO can be reacted with H2,C,CO")
        elif dis2=='Fe2O3':
            if dis1=='C':
                correct1Var.set("Fe2O3+C→CO2+Fe")
                correct1Var2.set("")
            elif dis1=='CO':
                correct1Var.set("Fe2O3+CO→CO2+Fe")
                correct1Var2.set("")
            elif dis1=='H2SO4':
                correct1Var.set("Fe2O3+H2SO4→Fe2(SO4)3+H2O")
                correct1Var2.set("")
            else:
                correct1Var.set("Please select a valid reaction")
                correct1Var2.set(":Fe2O3 can be reacted with H2SO4,C,CO")
        elif dis2=='CuSO4':
            if dis1=='Fe':
                correct1Var.set("CuSO4+Fe→FeSO4+Cu")
                correct1Var2.set("")
            elif dis1=='Zn':
                correct1Var.set("CuSO4+Zn→ZnSO4+Cu")
                correct1Var2.set("")
            else:
                correct1Var.set("Please select a valid reaction")
                correct1Var2.set(":CuSO4 can be reacted with Fe,Zn")
        elif dis2=='HCl':
            if dis1=="CaO":
                correct1Var.set("HCl+CaO→CaCl2+H2O")
                correct1Var2.set("")
            else:
                correct1Var.set("Please select a valid reaction")
                correct1Var2.set(":HCl can be reacted with CaO")

def impEqua():
    changeVar.set('')
    numMolesVar.set(0)
    molarMassVar.set(0)
    check2Var.set("")
    correct2Var.set("")
    nmLabelVar.set('')
    mmLabelVar.set('')
    global synspin1Var
    global synspin2Var
    global synspin3Var
    global decspin1Var
    global decspin2Var
    global decspin3Var
    global disspin1Var
    global disspin2Var
    global disspin3Var
    global disspin4Var
    global synspin1
    global synlabel1
    global synspin2
    global synlabel2
    global synspin3
    global synlabel3
    global decspin1
    global declabel1
    global decspin2
    global declabel2
    global decspin3
    global declabel3
    global disspin1
    global dislabel1
    global disspin2
    global dislabel2
    global disspin3
    global dislabel3
    global disspin4
    global dislabel4
    global labelplus
    global labeldash
    global labelplus1

    labelplus=Label(secondstepframe,text="+")
    labelplus1=Label(secondstepframe,text="+")
    labeldash=Label(secondstepframe,text="→")
    equaType=equaLabelVar.get()
    incorrectVar.set("")
    check=check1Var.get()
    if check=="CORRECT":
        #I'm not putting the strings directly from optionmenu and entry boxes because it would be more work if the user select the checkbottons OR use the spinboxes
        incorrectVar.set("")
        if equaType==1:
            if equaLabelVar2.get() == 2:
                decspin1Var.set('')
                decspin2Var.set('')
                decspin3Var.set('')
                decspin1.grid_forget()
                declabel1.grid_forget()
                decspin1.grid_forget()
                declabel1.grid_forget()
                decspin2.grid_forget()
                declabel2.grid_forget()
                decspin3.grid_forget()
                declabel3.grid_forget()
            elif equaLabelVar2.get()==3:
                disspin1Var.set('')
                disspin2Var.set('')
                disspin3Var.set('')
                disspin4Var.set('')
                disspin1.grid_forget()
                dislabel1.grid_forget()
                disspin2.grid_forget()
                dislabel2.grid_forget()
                disspin3.grid_forget()
                dislabel3.grid_forget()
                disspin4.grid_forget()
                dislabel4.grid_forget()
            
            syn1=synthesisOptionVar.get()
            synspin1Var=IntVar()
            synspin1=Spinbox(secondstepframe, textvariable=synspin1Var, values=[1,2,3,4,5])
            synlabel1Var=StringVar()
            synlabel1=Label(secondstepframe,textvariable=synlabel1Var)
            synspin2Var=IntVar()
            synspin2=Spinbox(secondstepframe, textvariable=synspin2Var, values=[1,2,3,4,5])
            synlabel2=Label(secondstepframe,text="O2")
            synspin3Var=IntVar()
            synspin3=Spinbox(secondstepframe, textvariable=synspin3Var, values=[1,2,3,4,5])            
            synlabel3Var=StringVar()
            synlabel3=Label(secondstepframe,textvariable=synlabel3Var)
            if syn1=="Mg":
                synlabel1Var.set("Mg")
                synlabel3Var.set("MgO")
                equanumVar.set(1)
            elif syn1=="Fe":
                synlabel1Var.set("Fe")
                synlabel3Var.set("Fe3O4")
                equanumVar.set(2)
            elif syn1=="Cu":
                synlabel1Var.set("Cu")
                synlabel3Var.set("CuO")
                equanumVar.set(3)
            elif syn1=="Al":
                synlabel1Var.set("Al")
                synlabel3Var.set("Al2O3")
                equanumVar.set(4)
            elif syn1=="H2":
                synlabel1Var.set("H2")
                synlabel3Var.set("H2O")
                equanumVar.set(5)
            elif syn1=="P":
                synlabel1Var.set("P")
                synlabel3Var.set("P2O5")
                equanumVar.set(6)
            elif syn1=="S":
                synlabel1Var.set("S")
                synlabel3Var.set("SO2")
                equanumVar.set(7)
            elif syn1=="C":
                synlabel1Var.set("C")
                synlabel3Var.set("CO")
                equanumVar.set(8)
            synspin1.grid(row=9,column=1,sticky=W)
            synlabel1.grid(row=9,column=2,sticky=W)
            labelplus.grid(row=9,column=3)
            synspin2.grid(row=9,column=4,sticky=E)
            synlabel2.grid(row=9,column=5,sticky=W)
            labeldash.grid(row=9,column=6)
            synspin3.grid(row=9,column=7,sticky=E)
            synlabel3.grid(row=9,column=8,sticky=W)
            equaLabelVar2.set(1)
        elif equaType==2:
            if equaLabelVar2.get()==1:
                synspin1Var.set('')
                synspin2Var.set('')
                synspin3Var.set('')
                synspin1.grid_forget()
                synlabel1.grid_forget()
                synspin2.grid_forget()
                synlabel2.grid_forget()
                synspin3.grid_forget()
                synlabel3.grid_forget()
            elif equaLabelVar2.get()==3:
                disspin1Var.set('')
                disspin2Var.set('')
                disspin3Var.set('')
                disspin4Var.set('')
                disspin1.grid_forget()
                dislabel1.grid_forget()
                disspin2.grid_forget()
                dislabel2.grid_forget()
                disspin3.grid_forget()
                dislabel3.grid_forget()
                disspin4.grid_forget()
                dislabel4.grid_forget()
            
            dec=decOptionVar.get()
            decspin1Var=IntVar()
            decspin1=Spinbox(secondstepframe, textvariable=decspin1Var, values=[1,2,3,4,5])
            declabel1Var=StringVar()
            declabel1=Label(secondstepframe,textvariable=declabel1Var)
            decspin2Var=IntVar()
            decspin2=Spinbox(secondstepframe, textvariable=decspin2Var, values=[1,2,3,4,5])
            declabel2Var=StringVar()
            declabel2=Label(secondstepframe,textvariable=declabel2Var)
            decspin3Var=IntVar()
            decspin3=Spinbox(secondstepframe, textvariable=decspin3Var, values=[1,2,3,4,5])            
            declabel3Var=StringVar()
            declabel3=Label(secondstepframe,textvariable=declabel3Var)
            if dec=="H2O":
                declabel1Var.set("H2O")
                declabel2Var.set("H2")
                declabel3Var.set("O2")
                equanumVar.set(9)
            elif dec=="KClO3":
                declabel1Var.set("KClO3")
                declabel2Var.set("KCl")
                declabel3Var.set("O2")
                equanumVar.set(10)
            elif dec=="H2CO3":
                declabel1Var.set("H2CO3")
                declabel2Var.set("H2O")
                declabel3Var.set("CO2")
                equanumVar.set(11)
            elif dec=="CaCO3":
                declabel1Var.set("CaCO3")
                declabel2Var.set("CaO")
                declabel3Var.set("CO2")
                equanumVar.set(12)
            decspin1.grid(row=9,column=1,ipadx=10,sticky=E)
            declabel1.grid(row=9,column=2,sticky=W)
            labeldash.grid(row=9,column=3)
            decspin2.grid(row=9,column=4,ipadx=10,sticky=E)
            declabel2.grid(row=9,column=5,sticky=W)
            labelplus.grid(row=9,column=6)
            decspin3.grid(row=9,column=7,ipadx=10,sticky=E)
            declabel3.grid(row=9,column=8,sticky=W)
            equaLabelVar2.set(2)
        elif equaType==3:
            if equaLabelVar2.get()==1:
                synspin1Var.set('')
                synspin2Var.set('')
                synspin3Var.set('')
                synspin1.grid_forget()
                synlabel1.grid_forget()
                synspin2.grid_forget()
                synlabel2.grid_forget()
                synspin3.grid_forget()
                synlabel3.grid_forget()
            elif equaLabelVar2.get() == 2:
                decspin1Var.set('')
                decspin2Var.set('')
                decspin3Var.set('')
                decspin1.grid_forget()
                declabel1.grid_forget()
                decspin1.grid_forget()
                declabel1.grid_forget()
                decspin2.grid_forget()
                declabel2.grid_forget()
                decspin3.grid_forget()
                declabel3.grid_forget()
            
            dis1=dis1OptionVar.get()
            dis2=dis2OptionVar.get()
            disspin1Var=IntVar()
            disspin1=Spinbox(secondstepframe, textvariable=disspin1Var, values=[1,2,3,4,5])
            dislabel1Var=StringVar()
            dislabel1=Label(secondstepframe,textvariable=dislabel1Var)
            disspin2Var=IntVar()
            disspin2=Spinbox(secondstepframe, textvariable=disspin2Var, values=[1,2,3,4,5])
            dislabel2Var=StringVar()
            dislabel2=Label(secondstepframe,textvariable=dislabel2Var)
            disspin3Var=IntVar()
            disspin3=Spinbox(secondstepframe, textvariable=disspin3Var, values=[1,2,3,4,5])            
            dislabel3Var=StringVar()
            dislabel3=Label(secondstepframe,textvariable=dislabel3Var)
            disspin4Var=IntVar()
            disspin4=Spinbox(secondstepframe, textvariable=disspin4Var, values=[1,2,3,4,5])            
            dislabel4Var=StringVar()
            dislabel4=Label(secondstepframe,textvariable=dislabel4Var)
            if dis2=='CuO':
                if dis1=='H2':
                    dislabel1Var.set("H2")
                    dislabel2Var.set("CuO")
                    dislabel3Var.set("Cu")
                    dislabel4Var.set("H2O")
                    equanumVar.set(13)
                elif dis1=='C':
                    dislabel1Var.set("C")
                    dislabel2Var.set("CuO")
                    dislabel3Var.set("Cu")
                    dislabel4Var.set("CO2")
                    equanumVar.set(14)
                elif dis1=='CO':
                    dislabel1Var.set("CO")
                    dislabel2Var.set("CuO")
                    dislabel3Var.set("Cu")
                    dislabel4Var.set("CO2")
                    equanumVar.set(15)
            elif dis2=='Fe2O3':
                if dis1=='C':
                    dislabel2Var.set("Fe2O3")
                    dislabel1Var.set("C")
                    dislabel4Var.set("CO2")
                    dislabel3Var.set("Fe")
                    equanumVar.set(16)
                elif dis1=='CO':
                    dislabel2Var.set("Fe2O3")
                    dislabel1Var.set("CO")
                    dislabel4Var.set("CO2")
                    dislabel3Var.set("Fe")
                    equanumVar.set(17)
                elif dis1=='H2SO4':
                    dislabel1Var.set("Fe2O3")
                    dislabel2Var.set("H2SO4")
                    dislabel3Var.set("Fe2(SO4)3")
                    dislabel4Var.set("H2O")
                    equanumVar.set(18)
            elif dis2=='CuSO4':
                if dis1=='Fe':
                    dislabel2Var.set("CuSO4")
                    dislabel1Var.set("Fe")
                    dislabel4Var.set("Cu")
                    dislabel3Var.set("FeSO4")
                    equanumVar.set(19)
                elif dis1=='Zn':
                    dislabel2Var.set("CuSO4")
                    dislabel1Var.set("Zn")
                    dislabel4Var.set("Cu")
                    dislabel3Var.set("ZnSO4")
                    equanumVar.set(20)
            elif dis2=='HCl':
                if dis1=="CaO":
                    dislabel2Var.set("HCl")
                    dislabel1Var.set("CaO")
                    dislabel3Var.set("CaCl2")
                    dislabel4Var.set("H2O")
                    equanumVar.set(21)
            disspin1.grid(row=9,column=1,ipadx=10,sticky=E)
            dislabel1.grid(row=9,column=2,sticky=W)
            labelplus1.grid(row=9,column=3)
            disspin2.grid(row=9,column=4,ipadx=10,sticky=E)
            dislabel2.grid(row=9,column=5,sticky=W)
            labeldash.grid(row=9,column=6)
            disspin3.grid(row=9,column=7,ipadx=10,sticky=E)
            dislabel3.grid(row=9,column=8,sticky=W)
            labelplus.grid(row=9,column=9)
            disspin4.grid(row=9,column=10,ipadx=10,sticky=E)
            dislabel4.grid(row=9,column=11,sticky=W)
            equaLabelVar2.set(3)
    elif check=="INCORRECT":
        if equaLabelVar2.get()==1:
            synspin1.grid_forget()
            labelplus.grid_forget()
            labeldash.grid_forget()
            synlabel1.grid_forget()
            synspin2.grid_forget()
            synlabel2.grid_forget()
            synspin3.grid_forget()
            synlabel3.grid_forget()
        elif equaLabelVar2.get() == 2:
            labelplus.grid_forget()
            labeldash.grid_forget()
            decspin1.grid_forget()
            declabel1.grid_forget()
            decspin1.grid_forget()
            declabel1.grid_forget()
            decspin2.grid_forget()
            declabel2.grid_forget()
            decspin3.grid_forget()
            declabel3.grid_forget()
        elif equaLabelVar2.get()==3:
            labelplus.grid_forget()
            labeldash.grid_forget()
            labelplus1.grid_forget()
            disspin1.grid_forget()
            dislabel1.grid_forget()
            disspin2.grid_forget()
            dislabel2.grid_forget()
            disspin3.grid_forget()
            dislabel3.grid_forget()
            disspin4.grid_forget()
            dislabel4.grid_forget()
        incorrectVar.set("Please enter a correct equation first and check")
    else:
        if equaLabelVar2.get()==1:
            labelplus.grid_forget()
            labeldash.grid_forget()
            synspin1.grid_forget()
            synlabel1.grid_forget()
            synspin2.grid_forget()
            synlabel2.grid_forget()
            synspin3.grid_forget()
            synlabel3.grid_forget()
        elif equaLabelVar2.get() == 2:
            labelplus.grid_forget()
            labeldash.grid_forget()
            decspin1.grid_forget()
            declabel1.grid_forget()
            decspin1.grid_forget()
            declabel1.grid_forget()
            decspin2.grid_forget()
            declabel2.grid_forget()
            decspin3.grid_forget()
            declabel3.grid_forget()
        elif equaLabelVar2.get()==3:
            labelplus1.grid_forget()
            labelplus.grid_forget()
            labeldash.grid_forget()
            disspin1.grid_forget()
            dislabel1.grid_forget()
            disspin2.grid_forget()
            dislabel2.grid_forget()
            disspin3.grid_forget()
            dislabel3.grid_forget()
            disspin4.grid_forget()
            dislabel4.grid_forget()
        incorrectVar.set("Please check your answer first")
        
                
def check2():

    equanum=equanumVar.get()
    equaType=equaLabelVar.get()
    if equaType==1:
        synspin11=synspin1Var.get()
        synspin22=synspin2Var.get()
        synspin33=synspin3Var.get()
        if equanum==1 and synspin11==2 and synspin22==1 and synspin33==2:
            check2Var.set("CORRECT")
        elif equanum==2 and synspin11==3 and synspin22==2 and synspin33==1:
            check2Var.set("CORRECT")
        elif equanum==3 and synspin11==2 and synspin22==1 and synspin33==2:
            check2Var.set("CORRECT")
        elif equanum==4 and synspin11==4 and synspin22==3 and synspin33==2:
            check2Var.set("CORRECT")
        elif equanum==5 and synspin11==2 and synspin22==1 and synspin33==2:
            check2Var.set("CORRECT")
        elif equanum==6 and synspin11==4 and synspin22==5 and synspin33==2:
            check2Var.set("CORRECT")
        elif equanum==7 and synspin11==1 and synspin22==1 and synspin33==1:
            check2Var.set("CORRECT")
        elif equanum==8 and synspin11==2 and synspin22==1 and synspin33==2:
            check2Var.set("CORRECT")
        else:
            check2Var.set("INCORRECT")
    elif equaType==2:
        decspin11=decspin1Var.get()
        decspin22=decspin2Var.get()
        decspin33=decspin3Var.get()
        if equanum==9 and decspin11==2 and decspin22==2 and decspin33==1:
            check2Var.set("CORRECT")
        elif equanum==10 and decspin11==2 and decspin22==2 and decspin33==3:
            check2Var.set("CORRECT")
        elif equanum==11 and decspin11==1 and decspin22==1 and decspin33==1:
            check2Var.set("CORRECT")
        elif equanum==12 and decspin11==1 and decspin22==1 and decspin33==1:
            check2Var.set("CORRECT")
        else:
            check2Var.set("INCORRECT")    
    elif equaType==3:
        disspin11=disspin1Var.get()
        disspin22=disspin2Var.get()
        disspin33=disspin3Var.get()
        disspin44=disspin4Var.get()
    
        if equanum==13 and disspin11==1 and disspin22==1 and disspin33==1 and disspin44==1:
            check2Var.set("CORRECT")
        elif equanum==14 and disspin11==1 and disspin22==2 and disspin33==2 and disspin44==1:
            check2Var.set("CORRECT")
        elif equanum==15 and disspin11==1 and disspin22==1 and disspin33==1 and disspin44==1:
            check2Var.set("CORRECT")
        elif equanum==16 and disspin11==3 and disspin22==2 and disspin33==4 and disspin44==3:
            check2Var.set("CORRECT")
        elif equanum==17 and disspin11==3 and disspin22==1 and disspin33==2 and disspin44==3:
            check2Var.set("CORRECT")
        elif equanum==18 and disspin11==1 and disspin22==3 and disspin33==1 and disspin44==3:
            check2Var.set("CORRECT")
        elif equanum==19 and disspin11==1 and disspin22==1 and disspin33==1 and disspin44==1:
            check2Var.set("CORRECT")
        elif equanum==20 and disspin11==1 and disspin22==1 and disspin33==1 and disspin44==1:
            check2Var.set("CORRECT")
        elif equanum==21 and disspin11==1 and disspin22==2 and disspin33==1 and disspin44==1:
            check2Var.set("CORRECT")
        else:
            check2Var.set("INCORRECT")

def correct2():
    num=equanumVar.get()
    if num==1:
        correct2Var.set("2Mg+O2→2MgO")
    elif num==2:
        correct2Var.set("3Fe+2O2→Fe3O4")
    elif num==3:
        correct2Var.set("2Cu+O2→2CuO")
    elif num==4:
        correct2Var.set("4Al+3O2→2Al2O3")
    elif num==5:
        correct2Var.set("2H2+O2→2H2O")
    elif num==6:
        correct2Var.set("4P+5O2→2P2O5")
    elif num==7:
        correct2Var.set("S+O2→SO2")
    elif num==8:
        correct2Var.set("2C+O2→2CO")
    elif num==9:
        correct2Var.set("2H2O→2H2+O2")
    elif num==10:
        correct2Var.set("2KClO3→2KCl+3O2")
    elif num==11:
        correct2Var.set("H2CO3→H2O+CO2")
    elif num==12:
        correct2Var.set("CaCO3→CaO+CO2")
    elif num==13:
        correct2Var.set("H2+CuO→Cu+H2O")
    elif num==14:
        correct2Var.set("C+2CuO→2Cu+CO2")
    elif num==15:
        correct2Var.set("CO+CuO→Cu+CO2")
    elif num==16:
        correct2Var.set("3Fe2O3+2C→4Fe+3CO2")
    elif num==17:
        correct2Var.set("3CO+Fe2O3→2Fe+3CO2")
    elif num==18:
        correct2Var.set("Fe2O3+3H2SO4→Fe2(SO4)3+3H2O")
    elif num==19:
        correct2Var.set("CuSO4+Fe→FeSO4+Cu")
    elif num==20:
        correct2Var.set("CuSO4+Zn→ZnSO4+Cu")
    elif num==21:
        correct2Var.set("CaO+2HCl→CaCl2+H2O")
        
def delete():
    equaList.delete(END)

       


#MAIN   
root = Tk()
mainframe = Frame(root)

#CREATE THE WIDGETS
titleLabel = Label(mainframe,text="Chemistry Equations", font=("Geneva", 20))

firststepframe=LabelFrame(mainframe)
secondstepframe= LabelFrame(mainframe)
equationTypeFrame = LabelFrame(mainframe, text="Type of equations")
equationTypeVar = StringVar()
equationTypeVar.set('synthesis')
synthesisRadio = Radiobutton(equationTypeFrame, text="Synthesis", variable = equationTypeVar, value='synthesis')
decompositionRadio = Radiobutton(equationTypeFrame, text="Decomposition", variable = equationTypeVar, value='decomposition')
displacementRadio = Radiobutton(equationTypeFrame, text="Displacement", variable = equationTypeVar, value='displacement')
defineButton = Button(equationTypeFrame, text="Enter", command=defineType)

equaLabelVar=IntVar()
equaLabelVar.set(0)
equaLabelVar2=IntVar()
equaLabelVar2.set(0)

check1Button=Button(mainframe, text="Check",command=check1)
check1Var=StringVar()
check1Label=Label(mainframe,textvariable=check1Var)
correct1Button=Button(mainframe, text="Correct Answer",command=correct1)
correct1Var=StringVar()
correct1Label=Label(mainframe,textvariable=correct1Var)
correct1Var2=StringVar()
correct12Label=Label(mainframe,textvariable=correct1Var2)

check2Button=Button(mainframe, text="Check",command=check2)
check2Var=StringVar()
check2Label=Label(mainframe,textvariable=check2Var)
correct2Button=Button(mainframe, text="Correct Answer",command=correct2)
correct2Var=StringVar()
correct2Label=Label(mainframe,textvariable=correct2Var)

equanumVar=IntVar()

spaceLabel1=Label(mainframe)
spaceLabel2=Label(mainframe)

importEquation=Button(mainframe, text="Import equation to next step",command=impEqua)
incorrectVar=StringVar()
incorrectVar.set("")
incorrectLabel=Label(mainframe,textvariable=incorrectVar)


thingsToShowFrame = LabelFrame(mainframe, text="Things to show after you import equation")
molarMassVar = IntVar()
molarMassVar.set(0)
molarMassCheck=Checkbutton(thingsToShowFrame, text = "Show molar mass", variable=molarMassVar, onvalue=1,offvalue=0)
numMolesVar = IntVar()
numMolesVar.set(0)
numMolesCheck=Checkbutton(thingsToShowFrame, text = "Show # of moles of ions/atoms", variable=numMolesVar, onvalue=1,offvalue=0)
showButton = Button(thingsToShowFrame, text="Enter", command=showMMandNM)

mmLabelVar=StringVar()
mmshow=Label(mainframe,text="Molar Mass:")
molarMassLabel=Label(mainframe,textvariable=mmLabelVar)
nmLabelVar=StringVar()
nmshow=Label(mainframe,text="Number of moles:") 
numofMolesLabel=Label(mainframe,textvariable=nmLabelVar)

firstLabel=Label(mainframe,font=("Geneva, bold", 13),text="First select to create equation and CHECK:")
secondLabel=Label(mainframe,font=("Geneva bold", 13),text="Now select how many moles for each chemical and CHECK:")


priceVar = StringVar()
priceLabel = Label(mainframe, textvariable=priceVar)

listButton=Button(mainframe,text="Add it to the list",command=addToList)
equaList=Listbox(mainframe)

changeVar=StringVar()
changeVar.set('')
changeLabel=Label(mainframe,textvariable=changeVar)

listLabel=Label(mainframe,font=("Geneva bold", 13),text="Equation List:")
deleteItem=Button(mainframe,text="delete last item",command=delete)

clearLabel=Label(mainframe)


#GRID
mainframe.grid(padx=20, pady=20)
titleLabel.grid(row = 1, column = 1, columnspan = 3, pady=20, sticky=W)
secondstepframe.grid(row=9,column=1,columnspan=6)

equationTypeFrame.grid(row=2, column=1, columnspan=3, sticky=W)
synthesisRadio.grid(row=1,sticky=W)
decompositionRadio.grid(row=2,sticky=W)
displacementRadio.grid(row=3,sticky=W)
defineButton.grid(row=4,sticky=E)
firstLabel.grid(row=5, column=1, sticky=W)

spaceLabel1.grid(row=6,column=1)
spaceLabel2.grid(row=6,column=2,ipadx=50)

check1Button.grid(row=7, column=1,sticky=E)
check1Label.grid(row=7, column=2,sticky=W)
correct1Button.grid(row=7,column=3,sticky=W)
correct1Label.grid(row=7,column=4,sticky=W)
correct12Label.grid(row=7,column=5,sticky=W)

secondLabel.grid(row=8,column=1,sticky=W)
incorrectLabel.grid(row=10,column=1,columnspan=3,sticky=W)

thingsToShowFrame.grid(row=2,column=4,columnspan=3, sticky=W)
molarMassCheck.grid(row=2, sticky=W)
numMolesCheck.grid(row=1, sticky=W)
showButton.grid(row=3, sticky=E)

nmshow.grid(row=10,column=2)
molarMassLabel.grid(row=10,column=5,sticky=W)
mmshow.grid(row=10,column=4)
numofMolesLabel.grid(row=10,column=3,sticky=W)

check2Button.grid(row=12, column=1,sticky=E)
check2Label.grid(row=12, column=2,sticky=W)
correct2Button.grid(row=12,column=3,sticky=W)
correct2Label.grid(row=12,column=4,sticky=W)

listButton.grid(row=12,column=5)
equaList.grid(row=15,column=1,sticky=W)
changeLabel.grid(row=13,column=5,sticky=NW)

listLabel.grid(row=13,column=1,sticky=NW)
deleteItem.grid(row=14,column=1,sticky=NW)

clearLabel.grid(row=2,column=10,ipadx=100)

root.mainloop()
