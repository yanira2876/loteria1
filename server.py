from flask import Flask, render_template
import random #importamos la libreria random para el nivel 4

app = Flask(__name__)

# Lista es de cartas para el nivel 4 

cartas = ["1  El Gallo","2  El Diablito","3  La Dama","4  El catrín","5  El paraguas",
        "6  La sirena","7  La escalera","8  La botella","9  El barril","10 El árbol",
        "11 El melón","12 El valiente","13 El gorrito","14 La muerte","15 La pera","16 La bandera",
        "17 El bandolón","18 El violoncello","19 La garza","20 El pájaro","21 La mano",
        "22 La bota","23 La luna","24 El cotorro","25 El borracho","26 El negrito","27 El corazón","28 La sandía","29 El tambor",
        "30 El camarón","31 Las jaras","32 El músico","33 La araña","34 El soldado",
        "35 La estrella","36 El cazo","37 El mundo","38 El apache","39 El nopal","40 El alacrán","41 La rosa","42 La calavera",
        "43 La campana","44 El cantarito","45 El venado","46 El sol","47 La corona","48 La chalupa","49 El pino","50 El pescado","51 La palma","52 La maceta","53 El arpa","54 La rana"]

#Definir los colores para el tablero

COLORES_TABLERO = ["#287fe4", "#eadb00", "#dda8c4"]

# Funcíon auxiliar para generar el tablero
def generar_tablero(filas, columnas):
        total_celdas = filas * columnas
        # Asegurarse de que no pidamos mas cartas de las ya tenemos
        if total_celdas > len(cartas):
                cartas_para_tablero = random.sample(cartas, len(cartas))# usamos todas las 
                #que tenemos y luego rellenamos repitiendo si necesitamos más
                while len(cartas_para_tablero) < total_celdas:
                        cartas_para_tablero.append(random.choice(cartas))
        else:
                cartas_para_tablero = random.sample(cartas, total_celdas)
        # barajamos las listas para asegurarnos de 
        # que el orden sea aleatorio para cada tablero
        random.shuffle(cartas_para_tablero)

        tablero = []
        carta_index = 0
        for r in range (filas):
                fila_actual = []
                for c in range (columnas):
                        color_index = (r + c) % len(COLORES_TABLERO)
                        color = COLORES_TABLERO[color_index]

                        #asignamos la carta aleatoria a la celda
                        nombre_carta = cartas_para_tablero[carta_index]
                        carta_index +=1

                        fila_actual.append({'color': color, 'nombre': nombre_carta})
                tablero.append(fila_actual)
        return tablero

@app.route('/loteria')
def loteria_default():
        filas = 4
        columnas = 4
        tablero = generar_tablero(filas, columnas)
        return render_template('tablero.html', filas=filas, 
                                columnas=columnas, 
                                tablero=tablero)

# 2. Ruta para el nivel 2: tablero 4 x X

@app.route('/loteria/<int:x>')
def loteria_filas_dinamicas(x):
        filas = x
        columnas = 4
        tablero = generar_tablero (filas, columnas)
        return render_template('tablero.html', filas=filas,
                                columnas=columnas, 
                                tablero=tablero)

# Ruta 3 tablero X y Y
@app.route ('/loteria/<int:x>/<int:y>')
def loteria_filas_columnas_dinamicas(x,y):
        filas = x
        columnas = y
        tablero = generar_tablero(filas, columnas)
        return render_template('tablero.html', filas = filas, 
                               columnas= columnas, 
                               tablero =tablero )
                
                

if __name__ == '__main__':
        app.run(debug=True)
