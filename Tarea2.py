import psycopg2

# Configura tu conexión a la base de datos
conn = psycopg2.connect(
    dbname="proyectos",
    user="postgres",
    password="FCbarcelona",
    host="localhost",
    port="5432"
)

def insertar_estudiante(Nombre, carné):
    try:
        with conn.cursor() as cursor:
            # Usar comillas dobles para nombres de tabla y columnas en SQL
            cursor.execute(
                'INSERT INTO "201904222" (Nombre, carné) VALUES (%s, %s)',
                (Nombre, carné)
            )
            conn.commit()
            print("Estudiante insertado correctamente.")
    except Exception as e:
        print("Ocurrió un error:", e)
        conn.rollback()

def main():
    nombre = input("Ingrese el nombre del estudiante: ")
    carné = input("Ingrese el carnet del estudiante (hasta 20 caracteres): ")
    
    if len(carné) > 20:
        print("El carnet debe tener 20 caracteres o menos.")
        return
    
    insertar_estudiante(nombre, carné)

if __name__ == "__main__":
    main()
    conn.close()