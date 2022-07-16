from mycollection_class import MyCollection


if __name__ == '__main__':
    input_list = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7),
                  {23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5},
                  {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8},
                  ["ineuron", "data science "]]

    my_list = MyCollection(input_list, 'list')
    my_list.run_all()

    my_tuple = MyCollection(input_list, 'tuple')
    my_tuple.run_all()

    my_set = MyCollection(input_list, 'set')
    my_set.run_all()