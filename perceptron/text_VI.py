file_handler = open('train_0.txt')
data_set = []
line = file_handler.readline()
while line:  # 遍历文件里的数据
    record = Record()
    item_feature_vector = []
    str_list = line.split()
    item_feature_vector.append(float(str_list[0]))
    item_feature_vector.append(float(str_list[1]))

    record.feature_vector = item_feature_vector
    record.label = float(str_list[2])
    data_set.append(record)
    line = file_handler.readline()
print(len(data_set))

ann = SingleLayerNeuralNetwork()  # 实例化感知机对象
ann.add_input_node()
ann.add_input_node()  # 添加两个输入结点
ann.set_data_set(data_set)  # 设置数据集
ann.run()  # 等待结果