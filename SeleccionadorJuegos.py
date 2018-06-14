class SeleccionadorJuegos:
    mejoresValores={}
    mejoresJuegos={}
    puntajes={}

    def __init__(self, dic_juegos, puntajes, minutos):
        self.puntajes=puntajes

        for min in minutos.MinutosLibres():
            self.mejoresValores[min]=0
            self.mejoresJuegos[min] = []
        #print(minutos)
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


   # def ObtenerMejorJuego(self):


   # def EliminarMinuto(self):
