class SeleccionadorJuegos:
    mejoresValores={}
    mejoresJuegos={}
    puntajes={}

    def __init__(self, dic_juegos, puntajes, minutos):
        self.puntajes=puntajes

        for min in minutos:
            self.mejoresValores[min]=0
            self.mejoresJuegos[min] = []

        for juego in dic_juegos.keys():
            for min in minutos:
                valor = float(puntajes[juego])/float(dic_juegos[juego][min].duracion)
                if valor >= self.mejoresValores[min]:
                    self.mejoresValores[min]= valor
                    self.mejoresJuegos[min]=[(juego,dic_juegos[juego][min].duracion)]
        print "a"
   # def ObtenerMejorJuego(self):


   # def EliminarMinuto(self):
