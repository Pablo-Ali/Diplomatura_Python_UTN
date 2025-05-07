
if __name__=="__main__": # lo que viene a continuación solo se ejecuta si lo lanzamos desde el main. Se usa para poder probar cosas sin que se ejecute toda la app cuando estamos en otro archivo
    from clases.cls_personas import Personas
    from clases.cls_gerentes import Gerentes

    juan = Personas("Juan Marcelo Barreto", 7, 500)
    susana = Personas("Susana Anna Perez", 6, 300)

    susana.dar_aumento(0.1)
    print(susana.salario)

    tom = Gerentes("Tomás Perez", 10, 1000, "Software")
    tom.dar_aumento(0.3)

    base_personas = [juan, susana, tom]
    for persona in base_personas:
        print(persona.nombre, persona.salario)