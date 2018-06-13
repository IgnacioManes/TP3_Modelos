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

    def __str__(self):
        minutos_ocupados=[]
        minutos_ocupados= self.actividades.keys()
        minutos_ocupados.sort()
        resultado=""
        for m in minutos_ocupados:
             resultado+="En el minuto "+ str(m) + " hago fila para " + self.actividades[m][0]+ " durante " + str(self.actividades[m][1]) + " minutos.\n"
        return  resultado


