def Fms_com_2(estado,entrada):
  if estado == 0:
    if entrada == 0:
      estado = 0
      salida =0
    elif entrada == 1:
      estado = 1
      salida = 1
  elif estado == 1:
    if entrada == 0:
      estado = 1
      salida = 1
    elif entrada == 1:
      estado = 1
      salida = 0

  return (estado, salida)

estado = 0
entradas = [0,0,1,1,0,0]

for entrada in entradas:
    print('est. act.:', estado, 'entr:', entrada, end=' ')
    estado, salida = Fms_com_2(estado, entrada)
    print('est_sig', estado, 'sal:', salida)

