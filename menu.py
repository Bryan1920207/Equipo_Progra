class Productos:
    def __init__(self,idProducto,Descripcion,Marca,Comentarios):
        self.idProducto=idProducto
        self.Descripcion=Descripcion
        self.Marca=Marca
        self.Comentarios=Comentarios
        
    def imprimir(self):
        print(f"idProducto {idProducto} Descripcion {Descripcion} Marca {Marca} Comentarios {Comentarios}")
        
def Buscar(idProducto):
    index_buscar = -1
    for index, producto in enumerate(lista_productos):
        if idProducto==producto.idProducto:
            index_buscar=index
            break
        return index_buscar
    
lista_productos=[]

print("1.- Agregar Producto\n" "2.- Agregar Comentario" "3.- Ver Producto\n" "4.- Ver Productos\n" "5.- Eliminar Producto\n" "6.- Modificar Producto\n" "7.- Salir")
opcion=int(input("Que opcion elijes? "))
while True:
    if opcion ==1:
        idProducto=input("idProducto? ")
        Descripcion=input("Descripcion? ")
        Marca=input("Marca? ")
        Comentarios=input("Comentarios? ")
        productoNuevo=Productos(idProducto,Descripcion,Marca,Comentarios)
        lista_productos.append(productoNuevo)
    elif opcion==2:
        idProducto=input("Id del producto a añadir comentarios: ")
        i=buscar(idProducto)
        datosProducto=lista_productos[i]
        Comentario=input("Id del producto a añadir comentarios: ")
        Productos.append(Comentario)
        datosProducto.imprimir()
    elif opcion==3:
        idProducto=input("Id del producto a buscar: ")
        i=buscar(idProducto)
        datosProducto=lista_productos[i]
        datosProducto.imprimir()
    elif opcion==4:
        for producto in lista_productos:
            producto.imprimir()
    elif opcion==5:
        idProducto=input("Id del producto a borrar: ")
        i=buscar(idProducto)
        if i=-1:
            print("No existe el producto")
        else:
            print("Producto a borrar")
            datosProducto=lista_productos[i]
            datosProducto.imprimir()
            confirmar=input("Estas seguro de querer borrarlo? ")
            if confirmar=="S":
                lista_productos.pop(i)
    elif opcion==6:
        idProducto=input("Id del producto a modificar: ")
        i=buscar(idProducto)
        if i=-1:
            print("No existe el producto")
        else:
            print("Datos actuales")
            datosProducto=lista_productos[i]
            datosProducto.imprimir()
            confirmar=input("Estas seguro de querer modificarlo? ")
            if confirmar=="S":
                print("Introduce los nuevos datos")
                idProducto=input("idProducto? ")
                Descripcion=input("Descripcion? ")
                Marca=input("Marca? ")
                Comentarios=input("Comentarios? ")
                productoNuevo=Productos(idProducto,Descripcion,Marca,Comentarios)
                lista_productos.append(productoNuevo[i])
    elif opcion==7:
        break