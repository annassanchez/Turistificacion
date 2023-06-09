import numpy as np

## for changing the scraped ratings from tripadvisor
ratings = {
    '4,0 de 5 burbujas':4.0,
    '4,5 de 5 burbujas':4.5,
    '3,5 de 5 burbujas':3.5,
    '5,0 de 5 burbujas':5.0,
    '3,0 de 5 burbujas':3.0,
    '2,5 de 5 burbujas':2.5,
    '-1,0 de 5 burbujas':-1.0,
    '2,0 de 5 burbujas':2.0,
    '1,0 de 5 burbujas':1.0,
    '1,5 de 5 burbujas':1.5,
    '':np.nan,
    '0 opiniones':0
}

## equivalences for the hotels dataframe
accommodation = {
    'Alojamientos':'Accommodation'
}

accommodation_type = {
    'Hoteles':'Hotels',
    'Hostales':'Hostel',
    'Residencias universitarias':'Dorms',
    'Apartahoteles':'Apartments',
    'Pensiones':'Hostels',
    'Albergues':'Hostels',
    'Camping':'Camping' 
}

hotel_apartments_ratings = {
    '4 estrellas':4.0,
    '2 estrellas':2.0,
    '3 estrellas':3.0,
    '1 estrella':1.0,
    '5 estrellas':5.0,
    '3 llaves':3.0,
    '5 estrellas Gran Lujo':6.0,
    '1 llave':1.0,
    '4 llaves':4.0,
    '2 llaves':2.0, 
    'Segunda categoría':3.
}

desc_epigrafe_en = {
    'COMERCIO AL POR MENOR DE VINOS Y ALCOHOLES (BODEGA) SIN CONSUMO':'alcohol',
    'RESTAURANTE':'restaurants', 
    'CAFETERIA':'restaurants',
    'COMERCIO AL POR MENOR DE AVES, HUEVOS Y CAZA SIN OBRADOR':'prox_fresco',
    'COMERCIO AL POR MENOR DE PRODUCTOS ALIMENTICIOS NO PERECEDEROS ENVASADOS':'prox_fresco',
    'COMERCIO AL POR MENOR DE PRODUCTOS DE PRECIO UNICO, BAZARES Y ASIMILABLES':'noalim',
    'BAR RESTAURANTE':'restaurants',
    'SERVICIOS DE COMEDOR EN CENTROS EDUCATIVOS Y CENTROS DE CUIDADO INFANTIL':'educacion',
    'CENTRO DE INFANTIL Y PRIMARIA PUBLICO':'educacion',
    'COMERCIO AL POR MENOR DE PAN Y PRODUCTOS DE PANADERIA Y BOLLERIA SIN OBRADOR':'pastelerias',
    'COMERCIO AL POR MENOR EN ESTABLECIMIENTOS NO ESPECIALIZADOS, CON PREDOMINIO EN PRODUCTOS ALIMENTICIOS, BEBIDAS Y TABACO (AUTOSERVICIO)':'shops24h',
    'COMERCIO AL POR MENOR DE CARNICERIA-CHARCUTERIA':'prox_fresco',
    'COMERCIO AL POR MENOR DE COMPLEMENTOS Y ALIMENTOS PARA ANIMALES DE COMPAÑIA':'noalim',
    'CLINICA VETERINARIA CON TRATAMIENTO HIGIENICO':'desconocidos',
    'COMERCIO AL POR MENOR DE HELADOS SIN OBRADOR':'restaurants',
    'COMERCIO AL POR MENOR DE CHARCUTERIA':'prox_fresco', 
    'BAR SIN COCINA':'fiesta',
    'SERVICIOS DE COMEDOR EN CENTROS PARA MAYORES':'restaurants',
    'ASISTENCIA EN ESTABLECIMIENTOS RESIDENCIALES PARA MAYORES, DISCAPACITADOS, DROGODEPENDIENTES, CENTROS DE CONVALECENCIA, PERSONAS SIN HOGAR':'desconocidos',
    'SERVICIO DE PELUQUERIA':'noalim', 
    'HOTELES Y MOTELES CON RESTAURANTE':'alojamiento',
    'RESTAURANTES DE COMIDA RAPIDA':'restaurants',
    'COMERCIO AL POR MENOR DE PRENDAS DE VESTIR EN ESTABLECIMIENTOS ESPECIALIZADOS':'noalim',
    'COMERCIO AL POR MENOR DE CARNICERIA':'prox_fresco',
    'BAR ESPECIAL SIN ACTUACIONES':'fiesta',
    'CHOCOLATERIA/SALON DE TE Y HELADERIA':'restaurants',
    'COMERCIO AL POR MENOR DE JOYAS, RELOJERIA Y BISUTERIA':'noalim',
    'BAR CON COCINA':'fiesta', 
    'COMERCIO AL POR MENOR DE LIBROS':'noalim',
    'COMERCIO AL POR MENOR DE FRUTOS SECOS Y VARIANTES':'prox_fresco',
    'ACABADO DE EDIFICIOS (CARPINTERIA, REVOCAMIENTO, REVESTIMIENTO DE SUELOS Y PAREDES,  PINTURA, ACRISTALAMIENTO)':'noalim',
    'COMERCIO AL POR MENOR DE ARTICULOS DE PERFUMERIA Y COSMETICA':'noalim',
    'ESTABLECIMIENTOS DE VENTA DE PLATOS PREPARADOS CON OBRADOR':'restaurants',
    'COMERCIO AL POR MENOR DE TABACOS Y ARTICULOS DE FUMADOR':'alcohol',
    'CENTRO DE ESTETICA':'noalim', 
    'PISCINAS DE USO PUBLLICO CLIMATIZADAS':'desconocidos',
    'ACTIVIDADES DE ORGANIZACIONES RELIGIOSAS':'desconocidos',
    'COMERCIO AL POR MENOR DE MUEBLES':'noalim',
    'ESCUELAS INFANTILES DE PRIMER CICLO':'educacion',
    'COMERCIO AL POR MENOR DE CALZADO Y ARTICULOS DE CUERO EN ESTABLECIMIENTOS ESPECIALIZADOS':'noalim',
    'OTRO COMERCIO AL POR MENOR DE PRODUCTOS ALIMENTICIOS (PERECEDEROS Y NO PERECEDEROS) CON VENDEDOR N.C.O.P.':'prox_fresco',
    'OTROS ACTIVIDADES DE SERVICIOS SOCIALES (LABORES DE ASESORAMIENTO Y ORIENTACION) SIN ALOJAMIENTO N.C.O.P.':'desconocidos',
    'SERVICIOS DE COMEDOR EN CENTROS DE ACTIVIDADES DE SERVICIOS SOCIALES':'desconocidos',
    'ESCUELAS INFANTILES DE SEGUNDO CICLO':'educacion',
    'COMERCIO AL POR MENOR DE PESCADOS Y MARISCOS SIN OBRADOR':'prox_fresco',
    'COMERCIO AL POR MENOR DE  PASTELERIA, CONFITERIA, REPOSTERIA CON OBRADOR-SIN BARRA DEGUSTACION':'pastelerias',
    'ESTABLECIMIENTOS DE VENTA DE PLATOS PREPARADOS SIN OBRADOR':'prox_fresco',
    'ENSEÑANZA NO REGLADA (DEPORTIVA Y RECREATIVA, CULTURAL, CLASES DE RECUPERACION, INFORMATICA)':'educacion',
    'COMERCIO AL POR MENOR DE PASTELERIA, CONFITERIA, REPOSTERIA CON OBRADOR-BARRA DEGUSTACION':'pastelerias',
    'COMERCIO AL POR MENOR DE ANIMALES DE COMPAÑIA':'noalim',
    'CENTROS DE CUIDADO INFANTIL':'educacion',
    'COMERCIO AL POR MENOR DE SEMILLAS, ABONOS, PLANTAS Y FLOR CORTADA':'noalim',
    'ACTIVIDADES DE SERVICIOS SOCIALES SIN ALOJAMIENTO PARA PERSONAS MAYORES Y DISCAPACITADOS':'desconocidos',
    'COMERCIO AL POR MENOR DE PAN Y PRODUCTOS DE PANADERIA Y BOLLERIA CON OBRADOR':'pastelerias',
    'INTERMEDIACION MONETARIA: BANCOS, CAJAS DE AHORRO':'noalim',
    'APARCAMIENTOS PRIVADOS':'noalim',
    'JUEGOS DE AZAR Y APUESTAS DE GESTION PRIVADA (BINGOS, CASINOS, MAQUINAS TRAGAPERRAS)':'fiesta',
    'ACTIVIDADES ADMINISTRATIVAS Y AUXILIARES DE OFICINA Y SERVICIOS DE REPROGRAFIA':'noalim',
    'INTERMEDIARIO DEL COMERCIO DE PRODUCTOS ALIMENTICIOS, BEBIDAS Y TABACO':'alcohol',
    'TALLER DE REPARACION DE AUTOMOVILES ESPECIALIZADO EN CHAPA Y PINTURA':'desconocidos',
    'TALLER DE REPARACION DE AUTOMOVILES ESPECIALIZADO EN MECANICA Y ELECTRICIDAD':'desconocidos',
    'COMERCIO AL POR MENOR DE CAFE, INFUSIONES Y CHOCOLATE':'prox_fresco',
    'COMERCIO AL POR MENOR DE CASQUERIA':'prox_fresco',
    'PISCINAS DE USO PUBLICO DE TEMPORADA':'desconocidos', 
    'APARCAMIENTOS MIXTOS':'noalim',
    'CENTROS DE TATUAJE Y/O ANILLADO':'noalim', 
    'LOCAL SIN ACTIVIDAD':'vacios',
    'COMERCIO AL POR MENOR DE FRUTAS Y HORTALIZAS SIN OBRADOR':'prox_fresco',
    'ACTIVIDADES DE DESCONTAMINACION Y OTROS SERVICIOS DE GESTION DE RESIDUOS':'desconocidos',
    'AUTOESCUELA':'educacion', 
    'COMERCIO AL POR MENOR DE CONGELADOS':'supers',
    'PREPARACION, CURTIDO Y ACABADO DEL CUERO. FABRICACION DE ARTICULOS DE MARROQUINERIA, VIAJE, GUARNICIONERIA Y TALABARTERIA. PREPARACION Y TEÑIDO DE PIELES':'noalim',
    'COMERCIO AL POR MENOR DE PRODUCTOS DE TELEFONIA Y TELECOMUNICACIONES':'noalim',
    'SALA DE EXPOSICIONES Y GALERIAS DE ARTE CON VENTA':'noalim',
    'DEPOSITO Y ALMACENAMIENTO':'desconocidos',
    'COMERCIO AL POR MENOR DE MASAS Y PATATAS FRITAS, CHURRERIA CON OBRADOR':'prox_fresco',
    'CENTROS DE BRONCEADO':'noalim',
    'ACTIVIDADES DE CLUBES DEPORTIVOS Y OTRAS ACTIVIDADES DEPORTIVAS':'desconocidos',
    'PTE. CODIFICAR (ACTIV. EMPRESARIALES:INDUST,COMERCIAL,DE SERVICIOS Y MINERAS)':'desconocidos',
    'TEATRO Y ACTIVIDADES ESCENICAS REALIZADAS EN DIRECTO':'fiesta',
    'COMERCIO AL POR MENOR DE CARNICERIA-SALCHICHERIA':'prox_fresco',
    'ACTIVIDADES INMOBILIARIAS (COMPRAVENTA, ALQUILER, AGENTES PROPIEDAD)':'noalim',
    'COMPRAVENTA DE BIENES INMOBILIARIOS POR CUENTA PROPIA':'noalim',
    'LAVADO Y LIMPIEZA DE PRENDAS TEXTILES Y DE PIEL':'noalim',
    'COMERCIO AL POR MENOR DE VINOS Y ALCOHOLES (BODEGA) CON CONSUMO':'alcohol',
    'CONFECCION PRENDAS DE VESTIR (INCLUIDO CUERO Y EXCLUIDA LA PELETERIA Y LAS PRENDAS DE PUNTO)':'noalim',
    'GESTION DE INSTALACIONES DEPORTIVAS':'desconocidos',
    'OTRO COMERCIO AL POR MENOR DEL ARTICULOS NUEVOS N.C.O.P.':'noalim',
    'COMERCIO AL POR MENOR DE HELADOS CON OBRADOR CON BARRA DE DEGUSTACION':'restaurants',
    'COMERCIO AL POR MENOR DE PRODUCTOS DE HERBOLARIO':'noalim', 
    'LOCUTORIOS':'locutoris',
    'HOTELES Y MOTELES SIN RESTAURANTE':'alojamiento',
    'COMERCIO AL POR MENOR DE PRODUCTOS PARAFARMACEUTICOS':'noalim',
    'COMERCIO AL POR MENOR DE GOLOSINAS':'prox_fresco', 
    'CAFE ESPECTACULO':'fiesta',
    'ACTIVIDADES DE LOS GIMNASIOS':'desconocidos', 
    'INSTITUTO DE BELLEZA':'noalim',
    'COMERCIO AL POR MENOR DE PASTELERIA, CONFITERIA, REPOSTERIA SIN OBRADOR':'pastelerias',
    'OTRAS ACTIVIDADES ASOCIATIVAS N.C.O.P.':'desconocidos',
    'CAMBIO Y ENVIO DE MONEDA':'locutoris',
    'CONSULTA DE ESTOMATOLOGOS Y ODONTOLOGOS':'desconocidos',
    'COMERCIO AL POR MENOR EN ESTABLECIMIENTOS NO ESPECIALIZADOS, CON PREDOMINIO EN PRODUCTOS ALIMENTICIOS, BEBIDAS Y TABACO (GRANDES SUPERFICIES)':'supersbig',
    'COMERCIO AL POR MENOR DE FRUTAS Y HORTALIZAS CON OBRADOR':'prox_fresco',
    'CENTRO DE INFANTIL Y PRIMARIA PRIVADO':'educacion',
    'COMERCIO AL POR MENOR EN ESTABLECIMIENTOS NO ESPECIALIZADOS, SIN PREDOMINIO EN PRODUCTOS ALIMENTICIOS, BEBIDAS Y TABACO':'supers',
    'FARMACIA':'noalim', 
    'COMERCIO AL POR MENOR DE INSTRUMENTOS MUSICALES':'noalim',
    'COMERCIO AL POR MENOR DE MATERIAL DE OPTICA':'noalim', 
    'SEGUROS':'desconocidos',
    'DISCOTECAS Y SALAS DE BAILE':'fiesta',
    'COMERCIO AL POR MENOR DE ARTICULOS DE USO DOMESTICO EN ESTABLECIMIENTO ESPECIALIZADO':'noalim',
    'COMERCIO AL POR MAYOR DE LIBROS, PERIODICOS, REVISTAS, PAPELERIA Y ESCRITORIO':'noalim',
    'COMERCIO AL POR MENOR POR CORRESPONDENCIA, INTERNET, A DOMICILIO':'noalim',
    'TABERNA':'fiesta', 
    'COMERCIO AL POR MENOR DE MUEBLES DE COCINA':'noalim',
    'AGENCIAS DE VIAJES,  OPERADORES TURISTICOS Y SERVICIOS DE RESERVAS':'noalim',
    'REPRODUCCION DE SOPORTES GRABADOS':'desconocidos',
    'SALONES DE BANQUETES Y PROVISION COMIDAS PARA EVENTOS':'restaurants',
    'OTROS SERVICIOS DE COMIDAS EN INSTALACIONES DEPORTIVAS, OFICINAS, EMPRESAS O SIMILARES':'restaurants',
    'ALQUILER DE VEHICULOS DE MOTOR':'alquillercoche',
    'COLEGIOS MAYORES Y RESIDENCIAS DE ESTUDIANTES':'alojamiento',
    'COMERCIO AL POR MENOR DE PERIODICOS, REVISTAS Y ARTICULOS DE PAPELERIA':'noalim',
    'COMERCIO DE VEHICULOS DE MOTOR NUEVOS':'noalim',
    'COMERCIO AL POR MENOR DE TEXTILES PARA EL HOGAR':'noalim',
    'COMERCIO AL POR MENOR DE MENAJE DEL HOGAR':'noalim',
    'COMERCIO AL POR MENOR DE APARATOS DE ILUMINACION':'noalim',
    'TIENDA DE CONVENIENCIA (24H)':'shops24h',
    'COMERCIO DE RESPUESTOS Y ACCESORIOS DE VEHICULOS DE MOTOR':'noalim',
    'CENTROS DE FOTODEPILACION':'noalim',
    'COMERCIO AL POR MENOR DE PRODUCTOS INFORMATICOS (ORDENADORES, PROGRAMAS, EQUIPOS PERIFERICOS Y CONSUMIBLES)':'noalim',
    'REPARACION DE ORDENADORES Y EQUIPOS DE COMUNICACION':'noalim',
    'BALNEARIOS Y SPA URBANOS':'desconocidos', 
    'CLINICAS MEDICAS':'desconocidos',
    'COMERCIO AL POR MENOR DE BICICLETAS':'supersbig', 
    'REPARACION DE BICICLETAS':'desconocidos',
    'ACTIVIDADES HOSPITALARIAS':'desconocidos',
    'COMERCIO AL POR MENOR DE ELECTRODOMESTICOS':'noalim',
    'COMERCIO AL POR MENOR DE ARTICULOS DEPORTIVOS':'noalim',
    'COMERCIO AL POR MENOR DE PESCADOS Y MARISCOS CON OBRADOR (INCLUYE COCCION)':'prox_fresco',
    'COMERCIO AL POR MENOR DE AVES, HUEVOS Y CAZA CON OBRADOR':'prox_fresco',
    'CONSULTA DE MEDICINA GENERAL Y ESPECIALIDADES':'desconocidos',
    'DESPACHO DE DIETISTAS':'desconocidos',
    'CONFECCION DE PRENDAS DE VESTIR DE PUNTO':'noalim',
    'BAR ESPECIAL CON ACTUACIONES':'fiesta',
    'FISIOTERAPEUTAS Y OTRAS ACTIVIDADES SANITARIAS':'desconocidos',
    'COMERCIO AL POR MENOR DE PUERTAS, VENTANAS Y PERSIANAS':'noalim',
    'MANTENIMIENTO Y REPARACION DE MOTOCICLETAS Y VENTA DE SUS REPUESTOS Y ACCESORIOS':'desconocidos',
    'APARCAMIENTOS PUBLICOS':'alquillercoche',
    'COMERCIO AL POR MENOR DE MATERIALES DE CONSTRUCCION':'noalim',
    'COMERCIO AL POR MAYOR DE METALES PRECIOSOS, JOYERIA Y RELOJERIA':'noalim',
    'COMERCIO AL POR MENOR DE ARTICULOS DE SEGUNDA MANO':'noalim',
    'COMERCIO AL POR MENOR DE MATERIAL ELECTRONICO':'noalim',
    'COMERCIO AL POR MENOR DE PRODUCTOS DE DROGUERIA':'noalim',
    'DESPACHO DE ESTOMATOLOGO Y ODONTOLOGO':'desconocidos',
    'CENTROS DE JUEGOS O CELEBRACIONES INFANTILES CON COCINA':'fiesta',
    'COMERCIO AL POR MENOR DE JUEGOS Y JUGUETES':'noalim',
    'DESPACHO MEDICO DE MEDICINA GENERAL Y ESPECIALISTAS':'desconocidos',
    'REPARACION DE OTROS EFECTOS PERSONALES Y ARTICULOS DE USO DOMESTICO N.C.O.P.':'desconocidos',
    'COMERCIO AL POR MENOR DE HELADOS CON OBRADOR SIN BARRA DE DEGUSTACION':'restaurants',
    'COMERCIO AL POR MENOR DE ALFOMBRAS, MOQUETAS Y REVESTIMIENTOS DE PAREDES Y SUELOS EN ESTABLECIMIENTOS ESPECIALIZADOS':'noalim',
    'CONSULTA DE OPTICOS-OPTOMETRISTAS':'desconocidos',
    'SALONES DE RECREO Y DIVERSION Y OTRAS ACTIVIDADES RECREATIVAS':'fiesta',
    'ADMINISTRACION DE MERCADOS FINANCIEROS, INTERMEDIACION EN OPERACIONES CON VALORES Y OTROS ACTIVOS':'desconocidos',
    'ADMINISTRACION PUBLICA Y DEFENSA. SEGURIDAD SOCIAL OBLIGATORIA':'desconocidos',
    'CENTRO DE PRIMARIA, SECUNDARIA, BACHILLERATO Y/O FP PRIVADO':'educacion',
    'INSTALACIONES ELECTRICAS, DE FONTANERIA Y OTRAS EN OBRAS DE CONSTRUCCION':'desconocidos',
    'COMERCIO AL POR MAYOR DE PRENDAS DE VESTIR, CALZADO Y ARTICULOS DE CUERO':'noalim',
    'CENTROS PUBLICOS DE EDUCACION PRIMARIA':'educacion', 
    'APART-HOTELES':'alojamiento',
    'SERVICIOS FOTOGRAFICOS':'desconocidos',
    'COMERCIO AL POR MENOR DE MATERIAL FOTOGRAFICO Y FOTOGRAFIA':'noalim',
    'ARREGLO DE ROPA':'noalim', 
    'COMERCIO AL POR MAYOR DE HUEVOS Y DERIVADOS':'supersbig',
    'SITUADOS: HELADOS Y/O BEBIDAS REFRESCANTES':'agrupaciones',
    'TRATAMIENTO HIGIENICO DE ANIMALES (PELUQUERIAS)':'noalim',
    'FABRICACION DE PRODUCTOS METALICOS, EXCEPTO MAQUINARIA Y EQUIPO':'desconocidos',
    'ALMACEN DE DISTRIBUCION POLIVALENTE A TEMPERATURA NO REGULADA':'desconocidos',
    'INTERMEDIARIOS DEL COMERCIO DE TEXTILES, PRENDAS DE VESTIR, PELETERIA, CALZADO Y ARTICULOS DE CUERO':'supersbig',
    'SAUNAS, BAÑOS TURCOS Y SIMILARES':'desconocidos',
    'CENTRO PUBLICO DE SECUNDARIA, BACHILLERATO Y/O FP':'educacion',
    'SALAS DE FIESTA CON RESTAURACION':'fiesta',
    'CENTRO PRIV.CONCERTADO DE PRIMARIA, SECUND., BACHILL. Y/O FP':'educacion',
    'INTERMEDIARIOS DEL COMERCIO ESPECIALIZADOS EN LA VENTA DE OTROS PRODUCTOS ESPECIFICOS':'noalim',
    'COMERCIO AL POR MENOR DE MATERIAL ELECTRICO':'noalim',
    'CONSULTORIO VETERINARIO SIN TRATAMIENTO HIGIENICO ANIMAL':'desconocidos',
    'ACTIVIDADES DE DISEÑO ESPECIALIZADO':'desconocidos',
    'COMERCIO AL POR MAYOR DE METALES FERREOS Y NO FERREOS, MATERIAL DE CONSTRUCCION, PAPEL Y CARTON':'noalim',
    'PRODUCCION, TRANSPORTE Y DISTRIBUCION DE ENERGIA ELECTRICA Y GAS':'desconocidos',
    'REPARACION DE CALZADO':'desconocidos',
    'ACTIVIDADES DE BIBLIOTECAS, ARCHIVOS, MUSEOS Y DE GALERIAS Y SALAS DE EXPOSICIONES SIN VENTA':'desconocidos',
    'ACTIVIDADES DE CREACION, ARTISTICAS Y ESPECTACULOS':'desconocidos',
    'FABRICACION DE PRODUCTOS DE PANADERIA Y PASTELERIA':'pastelerias',
    'ELABORACION, ENVASADO Y CONSERVACION DE FRUTAS, VERDURAS Y DERIVADOS':'desconocidos',
    'TELECOMUNICACIONES':'desconocidos',
    'COMERCIO AL POR MENOR EN TIENDAS DE BRICOLAJE':'noalim',
    'PUBLICIDAD, RELACIONES PUBLICAS Y ESTUDIOS DE MERCADO':'desconocidos',
    'CENTROS PRIVADOS CONCERTADOS EDUC INFANTIL Y EDUC PRIMARIA':'educacion',
    'COMERCIO AL POR MENOR DE ARTICULOS ORTOPEDICOS':'noalim',
    'MANTENIMIENTO Y REPARACION DE VEHICULOS DE MOTOR N.C.O.P.':'desconocidos',
    'COMERCIO AL POR MAYOR DE PLATOS PREPARADOS Y COCINADOS':'supersbig',
    'ACTIVIDADES DE PROGRAMACION Y EMISION DE RADIO Y TELEVISION':'desconocidos',
    'DESPACHO DE PROTESICOS E HIGIENISTAS DENTALES':'desconocidos',
    'VIVIENDAS TURÍSTICAS':'alojamiento',
    'COMERCIO AL POR MENOR DE BACALAO Y SALAZONES':'prox_fresco',
    'PROMOCION INMOBILIARIA':'desconocidos', 
    'CONSULTA DE PODOLOGIA':'desconocidos',
    'SITUADOS: SIN DETERMINAR':'agrupaciones',
    'CENTROS PRIVADOS CONCERTADOS DE EDUCACION PRIMARIA':'educacion',
    'COMERCIO AL POR MENOR DE COLCHONERIA':'noalim',
    'ACTIVIDADES DE CONTABILIDAD, TENEDURIA, AUDITORIA Y ASESORIA FISCAL':'noalim',
    'DESPACHO PROFESIONAL DE ARQUITECTURA E INGENIERIA':'desconocidos',
    'COMERCIO AL POR MENOR DE INSTRUMENTOS MEDICOS Y ORTOPEDICOS':'noalim',
    'COMERCIO AL POR MENOR DE ARTICULOS DE FERRETERIA':'noalim',
    'TALLER DE MONTAJE DE ACCESORIOS PARA EL AUTOMOVIL':'desconocidos',
    'CONSULTORIO VETERINARIO CON TRATAMIENTO HIGIENICO ANIMAL':'desconocidos',
    'DESPACHO DE FISIOTERAPEUTAS':'desconocidos',
    'COMERCIO AL POR MENOR DE LECHE, PRODUCTOS LACTEOS Y BEBIDAS REFRESCANTES':'prox_fresco',
    'VENTA DE MOTOCICLETAS':'noalim',
    'ACTIVIDADES DE GRABACION DE SONIDO Y EDICION MUSICAL':'desconocidos',
    'COMERCIO AL POR MENOR DE COMBUSTIBLE PARA LA AUTOMOCION EN ESTABLECIMIENTOS ESPECIALIZADOS':'noalim',
    'FABRICACION DE INSTRUMENTOS Y SUMINISTROS MEDICOS Y ODONTOLOGICOS':'desconocidos',
    'CENTROS PRIVADOS DE EDUCACION PRIMARIA':'educacion',
    'ACTIVIDADES CINEMATOGRAFICAS, DE VIDEO Y DE TELEVISION (PRODUCCION, DISTRIBUCION Y EXHIBICION)':'desconocidos',
    'EDUCACION UNIVERSITARIA PRIVADA':'educacion',
    'OTRAS ACTIVIDADES PROFESIONALES, CIENTIFICAS Y TECNICAS N.C.O.P.':'desconocidos',
    'COMERCIO AL POR MAYOR DE PERFUMERIA,COSMETICA, DROGUERIA Y LIMPIEZA':'noalim',
    'COMERCIO AL POR MENOR DE ARMAS':'noalim',
    'ACTIVIDADES DE LAS AGENCIAS DE COLOCACION':'noalim',
    'ENSEÑANZA DE IDIOMAS':'educacion',
    'OTRAS ACTIVIDADES DE CONSTRUCCION ESPECIALIZADA (CONSTRUCCION DE CUBIERTAS, CIMENTACION, PISCINAS)':'noalim',
    'CARPINTERIA Y EBANISTERIA':'noalim', 
    'IMPRENTA':'noalim',
    'SERVICIOS DE PREPARACIÓN DE COMIDAS EN HOSPITALES':'desconocidos',
    'COMERCIO DE VEHICULOS DE MOTOR USADOS':'noalim',
    'ALMACEN DE DISTRIBUCION DE PRODUCTOS ALIMENTICIOS':'supersbig',
    'CLINICA VETERINARIA SIN TRATAMIENTO HIGIENICO':'desconocidos',
    'JUEGOS DE AZAR Y APUESTAS DE GESTION PUBLICA O O AUTORIZACION ESPECIAL (ESTADO Y ONCE)':'noalim',
    'TRANSPORTE DE MERCANCIAS POR CARRETERA Y SERVICIOS DE MUDANZAS':'desconocidos',
    'INTERMEDIARIOS DEL COMERCIO DE LA MADERA Y MATERIALES DE CONSTRUCCION':'noalim',
    'EDICION DE LIBROS, PERIODICOS Y OTRAS ACTIVIDADES EDITORIALES':'desconocidos',
    'COMERCIO AL POR MENOR DE EQUIPOS O APARATOS AUDIOVISUALES':'noalim',
    'SERVICIOS DE MENSAJERIA, ACTIVIDADES POSTALES Y DE CORREOS':'desconocidos',
    'COMERCIO AL MAYOR CON ALMACEN':'noalim', 
    'HOSTALES':'alojamiento',
    'SERVICIOS PARASANITARIOS (NATUROPATIA, ACUPUNTURA, HOMEOPATIA)':'desconocidos',
    'AUTOSERVICIO DE RESTAURACION':'restaurants',
    'OTROS SERVICIOS FINANCIEROS(ARRENDAMIENTO FINANCIERO, PRESTAMOS POR ENTIDADES NO FINANCIERAS), EXCEPTO SEGUROS Y FONDOS DE PENSIONES':'desconocidos',
    'CONSULTA DE PROTESICOS E HIGIENISTAS DENTALES':'desconocidos',
    'FABRICACION DE PINTURAS, BARNICES, LACAS Y REVESTIMIENTOS SIMILARES':'desconocidos',
    'COMERCIO AL POR MAYOR DE MATERIAL Y APARATOS ELECTRONICOS PARA LAS TECNOLOGIAS DE LA INFORMACION Y LAS COMUNICACIONES':'noalim',
    'EDUCACION TERCIARIA NO UNIVERSITARIA':'educacion',
    'FABRICACION DE ARTICULOS DE PELETERIA':'desconocidos',
    'FABRICACION DE VEHICULOS DE MOTOR, REMOLQUES Y SEMIRREMOLQUES':'desconocidos',
    'SERIGRAFIA Y SERVICIOS DE PREIMPRESION Y PREPARACION DE SOPORTES':'desconocidos',
    'PISCINAS DE COMUNIDADES DE VECINOS DE TEMPORADA':'desconocidos',
    'COMERCIO AL POR MAYOR DE OTROS PRODUCTOS ALIMENTICIOS':'supersbig',
    'ALBERGUES JUVENILES Y OTROS ALOJAMIENTOS TURISTICOS DE CORTA ESTANCIA':'alojamiento',
    'CIBER-CAFE':'locutoris', 
    'CONSTRUCCION DE EDIFICIOS':'desconocidos',
    'SITUADOS: COMPLEMENTOS, BISUTERIA Y ARTESANIA':'agrupaciones',
    'CENTROS DE JUEGOS O CELEBRACIONES INFANTILES SIN COCINA':'fiesta',
    'DESPACHO PROFESIONAL DE ACTIVIDADES ECONOMICAS (CONTABILIDAD, AUDITORIA Y ASESORIA FISCAL)':'desconocidos',
    'INSTITUTOS O CENTROS CAPILARES':'desconocidos',
    'COMERCIO AL POR MAYOR FRUTAS, VERDURAS Y DERIVADOS':'supersbig', 
    'TAPICERIA':'noalim',
    'TRANSPORTE TERRESTRE URBANO (AUTOBUS, METRO, TAXI) O INTERURBANO (EXCEPTO POR FERROCARRIL)':'desconocidos',
    'COMERCIO AL POR MENOR DE MAQUINARIA Y EQUIPOS DE OFICINA':'noalim',
    'HOSPITALES VETERINARIOS':'desconocidos',
    'COMERCIO AL POR MAYOR DE MAQUINARIA, EQUIPO DE  OFICINA Y SUMINISTROS':'noalim',
    'FABRICACION O ELABORACION DE OTROS PRODUCTOS ALIMENTICIOS N.C.O.P.':'desconocidos',
    'COMERCIO AL POR MAYOR DE OTROS ARTICULOS DE USO DOMESTICO N.C.O.P.':'noalim',
    'SEX-SHOP':'sex', 
    'ACTIVIDADES DE ORGANIZACIONES POLITICAS':'desconocidos',
    'CENTRO DE EDUCACION DE PERSONAS ADULTAS (CEPA)':'educacion',
    'PROGRAMACION Y CONSULTORIA INFORMATICA Y TECNOLOGIAS DE LA INFORMACION':'desconocidos',
    'EDUCACION UNIVERSITARIA PUBLICA':'educacion',
    'COMERCIO AL POR MENOR DE SANEAMIENTOS':'noalim',
    'SERVICIOS TECNICOS DE ARQUITECTURA E INGENIERIA. ENSAYOS Y ANALISIS TECNICOS':'desconocidos',
    'ACTIVIDADES DE APOYO A LAS EMPRESAS N.C.O.P. (AGENCIAS DE COBROS, ENVASADO Y EMPAQUETADO)':'desconocidos',
    'COMERCIO AL POR MAYOR DE INSTRUMENTOS MEDICOS Y ORTOPEDICOS':'noalim',
    'MANTENIMIENTO Y REPARACION DE MAQUINARIA Y EQUIPO, INCLUIDO EL FERROVIARIO':'desconocidos',
    'ORGANIZACION DE CONVENCIONES Y FERIAS DE MUESTRAS':'desconocidos',
    'INDUSTRIA DEL PAPEL':'desconocidos', 
    'ACTIVIDADES JURIDICAS':'desconocidos', 
    'SIN ASIGNAR':'desconocidos',
    'INTERMEDIARIOS DEL COMERCIO DE COMBUSTIBLES, MINERALES, METALES Y PRODUCTOS QUIMICOS INDUSTRIALES':'noalim',
    'COMERCIO AL POR MAYOR DE MATERIAS PRIMAS AGRARIAS, DE ANIMALES VIVOS Y ALIMENTOS PARA ANIMALES':'noalim',
    'FABRICACION ARTICULOS DE FERRETERIA':'desconocidos',
    'OTRAS SERVICIOS PERSONALES (ASTROLOGIA, AGENCIAS DE CONTACTOS) N.C.O.P.':'desconocidos',
    'DESPACHO DE PODOLOGOS':'desconocidos',
    'ALQUILER DE BIENES INMOBILIARIOS POR CUENTA PROPIA':'desconocidos',
    'DESPACHO PROFESIONAL DE ACTIVIDADES JURIDICAS':'desconocidos',
    'FABRICACION PRODUCTOS FARMACEUTICOS':'desconocidos',
    'ACTIVIDADES DE SEGURIDAD PRIVADA':'desconocidos',
    'RECUBRIMIENTOS METALICOS (TRATAMIENTO Y REVESTIMIENTO DE METALES)':'desconocidos',
    'COMERCIO AL POR MAYOR DE TEXTILES':'noalim', 
    'ELABORACION DE HELADOS':'desconocidos',
    'PARQUES ZOOLOGICOS, JARDINES BOTANICOS Y RESERVAS NATURALES':'desconocidos',
    'ACTIVIDADES DE LIMPIEZA':'desconocidos',
    'ACTIVIDADES DE CONSULTORIA DE GESTION EMPRESARIAL':'desconocidos',
    'ADIESTRAMIENTO, CUIDADO DE ANIMALES, RESIDENCIAS CANINAS Y CENTROS DE ANIMALES ABANDONADOS':'desconocidos',
    'COMERCIO AL POR MENOR DE PRODUCTOS AUDIOVISUALES EN ESTABLECIMIENTOS ESPECIALIZADOS (CD,DVD,…)':'noalim',
    'COMERCIO AL POR MAYOR DE PRODUCTOS DE LA PESCA Y MARISCOS (EXCEPTO CONGELADOS)':'supersbig',
    'COMERCIO AL POR MAYOR CARNES Y DERIVADOS, AVES Y CAZA':'supersbig',
    'SERVICIOS DE INFORMACION: PROCESO DE DATOS, PORTALES WEB':'desconocidos',
    'VENDEDOR AMBULANTE DE ALIMENTOS PREPARADOS PARA SU CONSUMO INMEDIATO':'supers',
    'FABRICACION DE ACEITES Y GRASAS VEGETALES Y ANIMALES':'desconocidos',
    'POMPAS FUNEBRES Y ACTIVIDADES RELACIONADAS':'desconocidos',
    'COMERCIO AL POR MAYOR DE APARATOS ELECTRODOMESTICOS':'noalim',
    'COMERCIO AL POR MAYOR DE COMBUSTIBLES, QUIMICOS Y PRODUCTOS SEMIELABORADOS':'supersbig',
    'COMERCIO AL POR MENOR CON MAQUINAS EXPENDEDORAS':'noalim',
    'ACTIVIDADES ANEXAS AL TRANSPORTE':'desconocidos',
    'COMERCIO AL POR MAYOR DE PRODUCTOS FARMACEUTICOS':'noalim',
    'ENCUADERNACION Y SERVICIOS RELACIONADOS CON LA MISMA':'desconocidos',
    'VIDEOCLUB':'desconocidos',
    'ALQUILER DE EFECTOS PERSONALES Y ARTICULOS DE USO DOMESTICO':'desconocidos',
    'PROCESADO Y CONSERVACION DE CARNE Y ELABORACION DE PRODUCTOS CARNICOS, AVES Y CAZA':'desconocidos',
    'FABRICACION DE MUEBLES (INCLUIDOS COLCHONES)':'desconocidos',
    'FABRICACION DE PRODUCTOS DE CAUCHO Y PLASTICOS':'desconocidos',
    'INTERMEDIARIOS DEL COMERCIO DE MAQUINARIA, EQUIPO INDUSTRIAL, EMBARCACIONES Y AERONAVES':'desconocidos',
    'INDUSTRIA DE LA MADERA Y CORCHO (EXCEPTO MUEBLES), CESTERIA Y ESPARTERIA':'desconocidos',
    'COMERCIO AL POR MENOR DE SELLOS, MONEDAS Y MEDALLAS':'noalim',
    'FABRICACION DE MAQUINARIA DE USO GENERAL Y EQUIPO N.C.O.P.':'desconocidos',
    'FABRICACION DE ARTICULOS DE JOYERIA, BISUTERIA Y SIMILARES':'desconocidos',
    'COMERCIO AL POR MAYOR DE BEBIDAS':'alcohol',
    'FABRICACION DE TEJIDOS TEXTILES, ALFOMBRAS, CUERDAS Y OTROS PRODUCTOS TEXTILES (EXCEPTO PRENDAS DE VESTIR)':'desconocidos',
    'PROCESADO Y CONSERVACION DE PLATOS PREPARADOS O PRECOCINADOS Y DIETETICOS':'desconocidos',
    'PISCINA PRIVADA CLIMATIZADA':'desconocidos',
    'COMERCIO AL POR MAYOR DE JUGUETES Y ARTICULOS DE DEPORTE':'noalim',
    'ACTIVIDADES DE LAS SEDES CENTRALES':'desconocidos',
    'FABRICACION DE COMPONENTES ELECTRONICOS Y CIRCUITOS IMPRESOS ENSAMBLADOS':'desconocidos',
    'COMERCIO AL POR MAYOR DE LECHE Y DERIVADOS':'supersbig',
    'FABRICACION DE MATERIAL Y EQUIPO ELECTRICO (EXCEPTO ORDENADORES)':'desconocidos',
    'INDUSTRIAS MANUFACTURERAS N.C.O.P.':'desconocidos', 
    'INVESTIGACION Y DESARROLLO':'desconocidos',
    'INGENIERIA CIVIL':'desconocidos', 
    'ACTIVIDADES DE LAS SOCIEDADES HOLDING':'desconocidos',
    'SERVICIOS DE SISTEMAS DE SEGURIDAD: VIGILANCIA MEDIANTE SISTEMAS ELECTRONICOS':'desconocidos',
    'PENSIONES':'alojamiento', 
    'COMERCIO AL POR MAYOR DE MUEBLES':'noalim',
    'FABRICACION DE CALZADO':'desconocidos', 
    'CASAS DE HUESPEDES':'alojamiento',
    'FABRICACION DE INSTRUMENTOS MUSICALES':'desconocidos',
    'SALAS DE FIESTA SIN RESTAURACION':'fiesta',
    'COMERCIO AL POR MAYOR DE PORCELANA, CRISTALERIA Y ARTICULOS DE LIMPIEZA':'noalim',
    'ACTIVIDADES AUXILIARES A SEGUROS Y FONDOS DE PENSIONES':'desconocidos',
    'FABRICACION DE EQUIPOS DE RADIACION, ELECTROMEDICOS Y ELECTROTERAPEUTICOS':'desconocidos',
    'LOCALES DE EXHIBICIONES EROTICAS':'sex',
    'INSTALACION DE MAQUINAS Y EQUIPOS INDUSTRIALES':'desconocidos',
    'RECOGIDA, TRATAMIENTO Y ELIMINACION DE RESIDUOS. VALORIZACION (PROCESOS DE RECUPERACION)':'desconocidos',
    'COMERCIO AL POR MENOR DE MASAS Y PATATAS FRITAS, CHURRERIA SIN OBRADOR':'prox_fresco',
    'FABRICACION DE JABONES, DETERGENTES Y OTROS ARTICULOS DE LIMPIEZA. PERFUMES Y COSMETICOS':'desconocidos',
    'DESPACHO DE OPTICOS-OPTOMETRISTAS':'noalim',
    'FABRICACION DE PRODUCTOS ELECTRONICOS DE CONSUMO':'desconocidos',
    'FABRICACION DE INSTRUMENTOS DE PRECISION, MEDIDA Y CONTROL. FABRICACION DE RELOJES':'desconocidos',
    'COMERCIO AL POR MAYOR DE CAFE, TE, CACAO Y ESPECIAS':'supersbig',
    'PROCESADO Y CONSERVACION DE LECHE Y DERIVADOS':'desconocidos',
    'TRANSPORTE AEREO':'desconocidos', 
    'CORTE, TALLADO Y ACABADO DE LA PIEDRA':'desconocidos',
    'ACTIVIDADES DE TRADUCCION E INTERPRETACION':'desconocidos',
    'SERVICIOS INTEGRALES A EDIFICIOS E INSTALACIONES':'desconocidos',
    'ACTIVIDADES DE JARDINERIA':'desconocidos',
    'DEMOLICION Y PREPARACION DE TERRENOS':'desconocidos',
    'COMERCIO AL POR MAYOR DE AZUCAR, CHOCOLATE Y CONFITERIA':'supersbig',
    'FABRICACION DE APARATOS ELECTRICOS, ELECTRODOMESTICOS (EXCEPTO ORDENADORES)':'desconocidos',
    'FABRICACION DE VIDRIO Y PRODUCTOS DERIVADOS':'desconocidos',
    'FABRICACION DE PRODUCTOS MINERALES NO METALICOS (HORMIGON, CEMENTO, MORTERO, CAL, YESO, LADRILLOS, CERAMICA)':'desconocidos',
    'INTERMEDIARIOS DEL COMERCIO DE MATERIAS PRIMAS AGRARIAS, ANIMALES VIVOS, MATERIAS PRIMAS TEXTILES Y PRODUCTOS SEMIELABORADOS':'desconocidos',
    'ALQUILER MAQUINARIA Y EQUIPO DE CONSTRUCCION':'desconocidos',
    'SALAS DE DESPIECE':'desconocidos',
    'ALMACEN DE DISTRIBUCION A TEMPERATURA DE REFRIGERACION Y CONGELACION DE CARNE Y DERIVADOS DE CARNE':'desconocidos',
    'REASEGUROS':'desconocidos', 
    'COMERCIO AL POR MAYOR DE ENVASES Y EMBALAJES':'noalim',
    'FABRICACION DE EQUIPOS DE TELECOMUNICACIONES':'desconocidos',
    'FABRICACION DE JUEGOS Y JUGUETES':'desconocidos',
    'FABRICACION DE ARTICULOS DERIVADOS DEL YESO Y/O ESCAYOLA':'desconocidos',
    'PISCINAS PUBLICAS CLIMATIZADAS/TEMPORADA':'desconocidos',
    'FABRICACION DE VAJILLAS Y ARTICULOS PARA EL HOGAR':'noalim',
    'COMERCIO AL POR MAYOR DE PRODUCTOS DE LA PESCA Y MARISCOS CONGELADOS':'supersbig',
    'ACTIVIDADES DE LAS EMPRESAS DE TRABAJO TEMPORAL':'desconocidos',
    'CAPTACION, DEPURACION Y DISTRIBUCION DE AGUA':'desconocidos',
    'FABRICACION DE OTRO MATERIAL DE TRANSPORTE':'desconocidos',
    'FABRICACION DE PASTAS ALIMENTICIAS,CUSCUS Y SIMILARES':'desconocidos',
    'FABRICACION DE PRODUCTOS PARA LA ALIMENTACION ANIMAL':'desconocidos',
    'EXPLOTACIONES AGRICOLAS':'desconocidos', 
    'COMERCIO AL POR MAYOR DE TABACOS':'alcohol',
    'COMERCIO AL POR MAYOR DE ACEITES Y GRASAS COMESTIBLES':'noalim',
    'ACTIVIDADES DE ORGANIZACIONES Y ORGANISMOS EXTRATERRITORIALES':'desconocidos',
    'COMERCIO AL POR MENOR EN PUESTOS DE VENTA Y EN MERCADILLOS':'noalim',
    'ACTIVIDADES DE GESTION DE FONDOS':'desconocidos',
    'COMERCIO AL POR MENOR DE EMBARCACIONES DE RECREO':'noalim',
    'FABRICACION DE OTROS PRODUCTOS QUIMICOS':'desconocidos',
    'DESPACHO DE DIESTISTAS':'desconocidos',
    'ALMACEN Y DISTRIBUCION DE FRUTAS Y HORTALIZAS FRESCAS Y OTROS PRODUCTOS VEGETALES TRANSFORMADOS':'supersbig',
    'INTERMEDIARIOS DEL COMERCIO DE PRODUCTOS FARMACEUTICOS Y DISTRIBUCION DE MEDICAMENTOS':'supersbig',
    'FABRICACION DE INSTRUMENTOS DE OPTICA Y EQUIPO FOTOGRAFICO':'desconocidos',
    'SITUADOS: FLORES Y PLANTAS':'agrupaciones', 
    'VALOR NULO EN ORIGEN':'vacios',
    'METALURGIA. FABRICACION DE PRODUCTOS DE HIERRO, ACERO Y FERROALEACIONES':'desconocidos',
    'RECOGIDA Y TRATAMIENTO DE AGUAS RESIDUALES':'desconocidos',
    'EDICION DE PROGRAMAS INFORMATICOS':'desconocidos',
    'TRANSPORTE INTERURBANO DE PASAJEROS POR FERROCARRIL':'desconocidos',
    'ELABORACION, ENVASADO Y CONSERVACION DE  PRODUCTOS PESQUEROS Y MARISCOS':'supersbig',
    'ACTIVIDADES DE APOYO A LAS INDUSTRIAS EXTRACTIVAS':'desconocidos',
    'EXPLOTACIONES GANADERAS':'desconocidos',
    'ENVASADO DE CARNE Y DERIVADOS DE CARNE':'desconocidos',
    'PUESTO DEL MERCADO CENTRAL DE PESCADOS DE ENVASADO DE PRODUCTOS DE LA PESCA: ENVASADO Y REENVASADO DE PRODUCTOS DE LA PESCA':'prox_fresco',
    'INVERSION COLECTIVA, FONDOS Y ENTIDADES FINANCIERAS SIMILARES':'desconocidos',
    'FABRICACION DE HIELO Y SUMINISTRO DE VAPOR Y AIRE ACONDICIONADO':'supersbig',
    'ALMACEN DE DISTRIBUCION POLIVALENTE A TEMPERATURA DE CONGELACION':'supersbig',
    'ALMACEN DE DISTRIBUCION POLIVALENTE A TEMPERATURA DE REFRIGERACION':'supersbig',
    'ALMACEN DE DISTRIBUCION A TEMPERATURA DE CONGELACION DE PRODUCTOS PESQUEROS Y DE MARISCOS':'supersbig',
    'ALMACEN DISTRIBUCION A TEMPERATURA DE REFRIGERACION DE PRODUCTOS PESQUEROS Y DE MARISCOS':'supersbig',
    'ACTIVIDADES DE LOS CENTROS DE LLAMADAS':'locutoris',
    'OTRAS INDUSTRIAS EXTRACTIVAS':'desconocidos',
    'FABRICACION DE SOPORTES MAGNETICOS Y OPTICOS':'desconocidos',
    'FABRICACION DE BEBIDAS':'desconocidos',
    'FABRICACION DE ORDENADORES Y EQUIPOS INFORMATICOS':'desconocidos',
    'CAMPINGS Y APARCAMIENTOS PARA CARAVANAS':'alojamiento',
    'INTERMEDIARIOS DEL COMERCIO DE MUEBLES':'supersbig',
    'SITUADOS: CHURROS Y FREIDURIAS SIN NINGIN TIPO DE RELLENO':'agrupaciones',
    'ACTIVIDADES DE INVESTIGACION (DETECTIVES Y VIGILANCIA)':'desconocidos',
    'SITUADOS: CONFITERIA Y FRUTOS SECOS Y PATATAS FRITAS':'agrupaciones',
    'SOCIEDADES PROTECTORAS DE ANIMALES':'desconocidos',
    'OTROS SERVICIOS DE INFORMACION: AGENCIAS DE NOTICIAS':'desconocidos',
    'ELABORACION/ENVASADO DE OVOPRODUCTOS':'desconocidos',
    'ARRENDAMIENTO DE LA PROPIEDAD INTELECTUAL (USO DE MARCAS, PATENTES, FRANQUICIAS)':'desconocidos',
    'SILVICULTURA Y EXPLOTACION FORESTAL':'desconocidos',
    'FABRICACION DE PESTICIDAS Y OTROS PRODUCTOS AGROQUIMICOS':'desconocidos',
    'FABRICACION DE PRODUCTOS ABRASIVOS Y PRODUCTOS MINERALES NO METALICOS N.C.O.P.':'desconocidos',
    'TRANSPORTE DE MERCANCIAS POR FERROCARRIL':'desconocidos',
    'FABRICACION DE PRODUCTOS QUIMICOS BASICOS, COMPUESTOS NITROGENADOS, FERTILIZANTES, PLASTICOS Y CAUCHO SINTETICO EN FORMAS PRIMARIAS':'desconocidos',
    'SITUADOS DE OBJETOS Y PUBLICACIONES POLITICO-SOCIAL-ECONOMICO-DEPORTIVA. QUIOSCOS DE PRENSA':'agrupaciones',
    'FABRICACION DE PRODUCTOS DE MOLINERIA (HARINAS), ALMIDONES Y DERIVADOS':'desconocidos',
    'PROCESADO Y CONSERVACION DE CONGELADOS':'desconocidos', 
    'INDUSTRIA DEL TABACO':'alcohol',
    'PUESTO DEL MERCADO CENTRAL DE PESCADOS DE FABRICACION Y/0 ELABORACION Y/O TRANSFORMACION DE PRODUCTOS DE LA PESCA':'prox_fresco',
    'PUESTO DEL MERCADO CENTRAL DE FRUTAS DE ENVASADO DE FRUTAS Y HORTALIZAS FRESCAS':'prox_fresco',
    'ELABORACION Y ENVASADO DE HUEVOS':'desconocidos',
    'CENTROS DE CUIDADO INFANTIL DE ASISTENCIA ESPORADICA':'educacion'
    }

cadastral_construction_state = {
    'functional':10,
    '-':0,
    'declined':2,
    'ruin':1,
}

cadastral_typology = {
    '1_residential':'houses',
    '3_industrial':'industrial',
    '4_2_retail':'retail',
    '4_3_publicServices':'publicServices',
    '4_1_office':'office',
    '5_1_hotels':'hotels',
    '2_agriculture':'agriculture'
}

tripadvisor_priceRange = {
    '€':'tp_pricerange_0',
    '€€':'tp_pricerange_1',
    '€€€':'tp_pricerange_2',
    '€€€€':'tp_pricerange_3'
}

h3_operations = {'conditionOfConstruction_clean_hotels' : np.mean, 
                 'conditionOfConstruction_clean_houses':np.mean,
                 'parcs_hotels':np.sum, 
                 'parcs_houses':np.sum,	
                 'srf_hotels':np.sum,	
                 'srf_houses':np.sum,
                 'cad_tot_houses':np.sum,
                 'agrupaciones':np.sum,
                 'alcohol':np.sum,	
                 'alojamiento':np.sum,	
                 'alquillercoche':np.sum,	
                 'desconocidos':np.sum,
                 'educacion':np.sum,	
                 'fiesta':np.sum,	
                 'locutoris':np.sum,
                 'noalim':np.sum,	
                 'pastelerias':np.sum,	
                 'prox_fresco':np.sum,
                 'restaurants':np.sum,	
                 'sex':np.sum,	
                 'shops24h':np.sum,	
                 'supers':np.sum,	
                 'supersbig':np.sum,	
                 'vacios':np.sum,
                 'name_clean':'count',
                 'min_price_fc':np.min,
                 'max_price_fc':np.max,
                 'med_price_fc':np.median,
                 'price_clean_fc':np.mean,
                 'name':'count',
                 'avg_PriceRangeNum':np.mean,
                 'min_PriceRangeNum':np.min,
                 'max_PriceRangeNum':np.max,
                 'med_PriceRangeNum':np.median,
                 'tp_pricerange_0':np.sum,
                 'tp_pricerange_1':np.sum,
                 'tp_pricerange_2':np.sum,
                 'tp_pricerange_3':np.sum,
                 'min_reviews_clean':np.min,
                 'max_reviews_clean':np.max,
                 'med_reviews_clean':np.median,
                 'avg_reviews_clean':np.mean,
                 'min_rating_clean':np.min,
                 'max_rating_clean':np.max,
                 'avg_rating_clean':np.mean,
                 'med_rating_clean':np.median,
                 'host_listings_count':np.sum,       
                 'beds':np.sum,
                 'abnb_tot_price':np.mean,
                 'number_of_reviews':np.sum,
                 'id':'count',
                 'reviews_per_month':np.sum,
}

catastro_operation = {
    'conditionOfConstruction_clean_hotels' : np.mean, 
    'conditionOfConstruction_clean_houses':np.mean,
    'parcs_hotels':np.sum, 
    'parcs_houses':np.sum,	
    'srf_hotels':np.sum,	
    'srf_houses':np.sum,
    'cad_tot_houses_houses':np.sum,
    'cad_tot_houses_hotels':np.sum,
}

fotocasa_operation = {
    'name_clean':'count',
    'min_price_fc':np.min,
    'max_price_fc':np.max,
    'med_price_fc':np.median,
    'price_clean_fc':np.sum,
}

airbnb_operation = {
    'host_listings_count':np.sum,       
    'beds':np.sum,
    'abnb_tot_price':np.mean,
    'number_of_reviews':np.sum,
    'id':'count',
    'reviews_per_month':np.sum,
}

locales_operation = {
    'agrupaciones':np.sum,
    'alcohol':np.sum,	
    'alojamiento':np.sum,	
    'alquillercoche':np.sum,	
    'desconocidos':np.sum,
    'educacion':np.sum,	
    'fiesta':np.sum,	
    'locutoris':np.sum,
    'noalim':np.sum,	
    'pastelerias':np.sum,	
    'prox_fresco':np.sum,
    'restaurants':np.sum,	
    'sex':np.sum,	
    'shops24h':np.sum,	
    'supers':np.sum,	
    'supersbig':np.sum,	
    'vacios':np.sum,
}

locales_operation = {
    'agrupaciones':np.sum,
    'alcohol':np.sum,	
    'alojamiento':np.sum,	
    'alquillercoche':np.sum,	
    'desconocidos':np.sum,
    'educacion':np.sum,	
    'fiesta':np.sum,	
    'locutoris':np.sum,
    'noalim':np.sum,	
    'pastelerias':np.sum,	
    'prox_fresco':np.sum,
    'restaurants':np.sum,	
    'sex':np.sum,	
    'shops24h':np.sum,	
    'supers':np.sum,	
    'supersbig':np.sum,	
    'vacios':np.sum,
}

tripadvisor_operation = {
    'name':'count',
    #'avg_PriceRangeNum':np.mean,
    #'min_PriceRangeNum':np.min,
    #'max_PriceRangeNum':np.max,
    #'med_PriceRangeNum':np.median,
    'tp_pricerange_0':np.sum,
    'tp_pricerange_1':np.sum,
    'tp_pricerange_2':np.sum,
    'tp_pricerange_3':np.sum,
    #'max_reviews_clean':np.max,
    #'min_reviews_clean':np.min,
    #'med_reviews_clean':np.median,
    #'avg_reviews_clean':np.mean,
    #'min_rating_clean':np.min,
    #'max_rating_clean':np.max,
    #'avg_rating_clean':np.mean,
    #'med_rating_clean':np.median,
}

rename_dict = {
    'price_clean_fc':'rn_fc_tot_price',
    'name_clean':'fc_tot_offer',
    'id':'abnb_tot_offer',
    'alcohol':'local200_n_prox_alcohol',
    'restaurants':'local200_n_restaurants',
    'fiesta':'local200_n_fiesta',
    'sex':'local200_n_sex',
    'prox_fresco':'local200_n_prox_fresco',
    'supers':'local200_n_prox_supers',
    'noalim':'local200_n_prox_noalim',
    'educacion':'local200_n_prox_educacion',
    'vacios':'local200_n_vacios',
    'restaurants':'local200_n_restaurants',
    'supersbig':'local200_n_prox_supersbig',
    'name':'tp_offers_tot',
    'cad_tot_houses_hotels':'cad_tot_hotels',
    'cad_tot_houses_houses':'cad_tot_houses',
    'cad_tot_houses_hotels':'cad_tot_hotels',
    'srf_houses':'cad_tot_srf_houses',
    'srf_hotels':'cad_tot_srf_hotels',
    'host_listings_count':'abnb_tot_hosts_listings',
}

groupby_agroupations_livingConditions = {
    'fc_tot_offer':np.sum,
    'abnb_tot_offer':np.sum,
    'rn_fc_tot_price':np.mean,
    'abnb_tot_price':np.mean,
}

groupby_agroupations_services = {
    'local200_n_prox_fresco':np.sum,
    'local200_n_prox_supers':np.sum,
    'local200_n_prox_noalim':np.sum,
    'local200_n_prox_educacion':np.sum,
    'local200_n_vacios':np.sum,
    'local200_n_restaurants':np.sum,
    'local200_n_prox_supersbig':np.sum,
    'local200_n_restaurants':np.sum,
    'tp_offers_tot':np.sum
}

groupby_agroupations_sleep = {
    'cad_tot_srf_houses':np.sum,
    'abnb_tot_offer':np.sum,
    'abnb_tot_hosts_listings':np.sum,
    'cad_tot_srf_hotels':np.sum,
    'cad_tot_houses':np.sum
}

groupby_fiesta = {
    'abnb_tot_offer':np.sum,
    'local200_n_prox_alcohol':np.sum,
    'local200_n_restaurants':np.sum,
    'local200_n_fiesta':np.sum,
    'local200_n_sex':np.sum,
    'tp_offers_tot':np.sum,
    'abnb_tot_price':np.mean,
    'cad_tot_hotels':np.sum,
    'cad_tot_houses':np.sum,
}