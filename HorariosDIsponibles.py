class HorariosDisponibles:
    disponible=[]
    actividades={}

    def __init__(self, minutoMaximo):
        for x in range(0, minutoMaximo+1):
            self.disponible.append(False)


    def AgregarActivdad(self, juego, inicio, duracion):
        for x in range(inicio, duracion):
            self.disponible[x]=True

        self.actividades[inicio]=(juego,duracion)

    def EstanDisponiblesMinutos(self, inicio, duracion):
        for x in range(inicio, duracion):
            if(self.disponible[x]==True):
                return False
        return True

    def __str__(self):
        minutos_ocupados=[]
        minutos_ocupados= self.disponible.keys()
        minutos_ocupados.sort()
        for m in minutos_ocupados:
            print "En el minuto "+ m + "hago fila para " + self.actividades[m][0]+ " durante " + self.actividades[m][1] + " minutos."


