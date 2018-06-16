class HorariosDIsponibles:
    disponible=[]
    actividades={}

    def __init__(self, minutoMaximo):
        for x in range(0, minutoMaximo+1):
            self.disponible.append(False)


    def AgregarActivdad(self, juego, inicio, duracion):
        for x in range(inicio, inicio +duracion):
            self.disponible[x]=True

        self.actividades[inicio]=(juego,duracion)

    def EstanDisponiblesMinutos(self, inicio, duracion):
        for x in range(inicio,inicio + duracion):
            if(self.disponible[x]):
                return False
        return True

    def EncontrarMinutoDisponible(self, inicio):
        for x in range(inicio, len(self.disponible)-1):
            if(self.disponible[x]==False):
                return x
        return None

    def MinutosLibres(self):
        list=[]
        for x in range(0, 745):
            if(self.disponible[x]==False):
                list.append(x)
        return list

    def Puntaje(self,puntajes):
        puntaje=0
        minutos_ocupados= self.actividades.keys()
        for m in minutos_ocupados:
            puntaje+=puntajes[self.actividades[m][0]]
        return puntaje


    def contarJuegosNiniosDistintos(self):
        cantNinios=0
        ninios=("Juego1","Juego5","Juego9","Juego11","Juego12","Juego14","Juego18","Juego19","Juego20","Juego22")
        for ninio in ninios:
            for m in self.actividades.keys():
                if self.actividades[m][0] == ninio :
                   cantNinios = cantNinios+1
                   break
        return cantNinios

    def contarMontaniasRusasDistintas(self):
        cantmontanias=0
        montanias=("Juego3","Juego15","Juego16","Juego17")
        for montania in montanias:
            for m in self.actividades.keys():
                if self.actividades[m][0] == montania :
                   cantmontanias = cantmontanias+1
                   break
        return cantmontanias

    def subieronPhilarMagic(self):
        philarMagic=False
        for m in self.actividades.keys():
            if self.actividades[m][0] == "Juego10":
               philarMagic = True
               break
        return philarMagic

    def __str__(self):
        minutos_ocupados=[]
        minutos_ocupados= self.actividades.keys()
        """minutos_ocupados.sort()"""
        resultado=""
        for m in minutos_ocupados:
             resultado+="En el minuto "+ str(m) + " hago fila para " + self.actividades[m][0]+ " durante " + str(self.actividades[m][1]) + " minutos.\n"
        resultado=resultado.replace("Juego1 ","its a small world")
        resultado=resultado.replace("Juego2 ","Astro Orbiter")
        resultado=resultado.replace("Juego3 ","Big Thunder Mountain Railroad")
        resultado=resultado.replace("Juego4 ","Buzz Lightyears Space Ranger Spin")
        resultado=resultado.replace("Juego5 ","Dumbo the Flying Elephant")
        resultado=resultado.replace("Juego6 ","Enchanted Tales with Belle")
        resultado=resultado.replace("Juego7 ","Haunted Mansion")
        resultado=resultado.replace("Juego8 ","Jungle Cruise")
        resultado=resultado.replace("Juego9 ","Mad Tea Party")
        resultado=resultado.replace("Juego10 ","Mickeys PhilharMagic")
        resultado=resultado.replace("Juego11 ","Monsters Inc. Laugh Floor")
        resultado=resultado.replace("Juego12 ","Peter Pans Flight")
        resultado=resultado.replace("Juego13 ","Pirates of the Caribbean")
        resultado=resultado.replace("Juego14 ","Prince Charming Regal Carrousel")
        resultado=resultado.replace("Juego15 ","Seven Dwarfs Mine Train")
        resultado=resultado.replace("Juego16 ","Space Mountain")
        resultado=resultado.replace("Juego17 ","Splash Mountain")
        resultado=resultado.replace("Juego18 ","The Barnstormer")
        resultado=resultado.replace("Juego19 ","The Magic Carpets of Aladdin")
        resultado=resultado.replace("Juego20 ","The Many Adventures of Winnie the Pooh")
        resultado=resultado.replace("Juego21 ","Tomorrowland Speedway")
        resultado=resultado.replace("Juego22 ","Under the Sea - Journey of The Little Mermaid")
        resultado=resultado.replace("Juego23 ","Pizza")
        return  resultado
