class SeleccionadorJuegos:
    mejoresValores={}
    mejoresJuegos={}
    puntajes={}

    def __init__(self, dic_juegos, puntajes, minutos):
        self.puntajes=puntajes

        for min in minutos.MinutosLibres():
            self.mejoresValores[min]=0
            self.mejoresJuegos[min] = []
        
        for juego in dic_juegos.keys():
            for min in minutos.MinutosLibres():
                valor = float(puntajes[juego])/float(dic_juegos[juego][min].duracion)
                if valor >= self.mejoresValores[min]:
                    self.mejoresValores[min]= valor
                    self.mejoresJuegos[min]=[juego,dic_juegos[juego][min].duracion]

        minutos_libres=minutos.MinutosLibres()
        while(len(self.mejoresValores)!=0):
            for min in minutos_libres:             
                if(min in self.mejoresValores.keys() and max(self.mejoresValores.values())==self.mejoresValores[min]):
                    if(minutos.EstanDisponiblesMinutos(min , self.mejoresJuegos[min][1])):
                        minutos.AgregarActivdad((self.mejoresJuegos[min][0]), min, self.mejoresJuegos[min][1])
                    self.mejoresValores.pop(min)

    def chequearResticciones(self,horarios_disponibles):
        cantMontaniasDistintas = horarios_disponibles.contarMontaniasRusasDistintas()
        cantJuegoNiniosDistintos = horarios_disponibles.contarJuegosNiniosDistintos()
        subieronAlPhillar = horarios_disponibles.subieronPhilarMagic()
        cumpleTodasLasRestricciones=True
        if(cantMontaniasDistintas>=4 and not subieronAlPhillar):
            print "No se cumple la resticcion del Mickeys PhilharMagic"
            cumpleTodasLasRestricciones=False
        else:
            print "La cantidad de montanias rusas distintas es: "+str(cantMontaniasDistintas)+" y se subio al Mickeys PhilharMagic"
        if(cantMontaniasDistintas<3):
            print "No se cumple la resticcion de la cantidad minima de montanias"
            cumpleTodasLasRestricciones=False
        if(cantJuegoNiniosDistintos>=10):
            print "No se cumple la resticcion de la cantidad maxima de juegos para ninios"
            cumpleTodasLasRestricciones=False
        else:
            print "La cantidad de juegos para ninios distintos visitados es: "+str(cantJuegoNiniosDistintos)
        return cumpleTodasLasRestricciones
   # def ObtenerMejorJuego(self):


   # def EliminarMinuto(self):
