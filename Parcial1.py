import bson
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Productos_Varios"]
collection = db["Productos"]

print("Bienvenido")

while True:
    print("¿Que desea hacer?")
    print("1. Agregar")
    print("2. Actualizar")
    print("3. Eliminar")
    print("4. Categoria")
    print("5. Nombre")
    print("6. Productos")
    print("7. Salir")

    opcion = input("Ingrese un número: ")

    if opcion == "1":
        nombre = input("Ingrese un nombre para el producto: ")
        marca = input("Marca del producto: ")
        cantidad = input("Cantidad disponible: ")
        categoria = input("Ingrese la categoria del producto: ")
        precio = input("Ingrese precio del producto: ")

        producto = {"Nombre": nombre,"Marca":marca, "Cantidad":cantidad, "Categoria":categoria, "Precio":float(precio)}
        resultado = collection.insert_one(producto)

        print("Producto agregado exitosamente. ID: ",resultado.inserted_id)

        producto = collection.find_one({"_id": resultado.inserted_id})
        print("Producto:")
        print(producto)

    elif opcion == "2":
        id_producto = input("Ingrese el ID del producto: ")
        nuevo_nombre = input("Ingrese un nuevo nombre: ")
        nueva_marca = input("Marca del producto: ")
        nueva_cantidad = input("Cantidad disponible: ")
        nueva_categoria = input("Ingrese una nueva categoria: ")
        nuevo_precio = input("Ingrese nuevo precio: ")

        filtro = {"_id": bson.ObjectId(id_producto)}
        nuevo_valor = {"$set": {"Nombre":nuevo_nombre, "Marca":nueva_marca, "Cantidad":nueva_cantidad, "Categoria":nueva_categoria, "Precio":nuevo_precio}}
        update_result = collection.update_one(filtro, nuevo_valor)

        if update_result.modified_count == 1:
            print("Actualizado exitosamente")
        else:
            print("No se encontró ningún producto con ese ID")

    elif opcion == "3":

        id_producto = input("Ingrese el ID del producto: ")

        filtro = {"_id": bson.ObjectId(id_producto)}
        resultado_eliminar = collection.delete_one(filtro)

        if resultado_eliminar.deleted_count == 1:
            print("Eliminado exitosamente")
        else:
            print("No se encontró el producto")

    elif opcion == "4":

        categoria = input("Ingrese la categoría que desea buscar: ")
        filtro = {"Categoria": {"$regex": categoria, "$options": "i"}}
        productos = collection.find(filtro)

        if collection.count_documents(filtro) == 0:
            print("No se encontraron productos en esa categoría")
        else:
            print("Productos en la categoría", categoria)
            for producto in productos:
                print(producto)

    elif opcion == "5":

        nombre = input("Ingrese nombre del producto: ")
        filtro = {"Nombre": {"$regex": nombre, "$options": "i"}}
        productos = collection.find(filtro)

        if collection.count_documents(filtro) == 0:
            print("No se encontró el producto")
        else:
            print("Productos con este nombre", nombre)
            for producto in productos:
                print(producto)

    elif opcion == "6":

        productos = collection.find({})
        productos_count = collection.count_documents({})

        if productos_count == 0:
            print("No hay productos disponibles")
        else:
            print("Productos disponibles")
            for producto in productos:
                print(producto)

    elif opcion == "7":
        print("SALIENDO...")
        break
    else:
        print("Opción no valida. Vuelva a intentarlo.")