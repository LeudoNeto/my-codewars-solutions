class List:
    def remove_(self, integer_list, values_list):
        lista = []
        for x in integer_list:
            if x not in values_list:
                lista.append(x)
        return lista