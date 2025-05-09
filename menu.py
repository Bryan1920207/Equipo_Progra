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
        pass
    elif opcion==2:
        pass
    elif opcion==3:
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        pass
    elif opcion==7:
        break