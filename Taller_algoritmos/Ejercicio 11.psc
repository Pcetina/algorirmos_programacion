Algoritmo Nota_final
	
	//Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
	Escribir "Señor Estudiante, porfavor ingrese el valor del parcial 1"
	Leer parcial1
	Escribir"Señor Estudiante, porfavor ingrese el valor del parcial 2"
	Leer parcial2
	Escribir"Señor Estudiante, porfavor ingrese el valor del parcial 3"
	Leer parcial3
	Promedioparciales <- (parcial1+parcial2+parcial3)/3;
	Escribir "Señor estudiante, este es el valor promedio de sus parciales es de " Promedioparciales
	Escribir "Ahora, porfavor ingrese el valor de su examen final"
	Leer Examenfinal
	Escribir"Por ultimo, ingrese el valor de trabajo final"
	Leer Trabajofinal
	Calificacionfinal <- Promedioparciales*0.55+Examenfinal*0.30+Trabajofinal*0.15
	Escribir "Señor estudiante, su calificaciòn final es " Calificacionfinal
	
FinAlgoritmo

	
