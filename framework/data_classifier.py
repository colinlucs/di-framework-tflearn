class CsvDataClassifier:
    """A Classifier for data prediction"""
    def __init__(self, name, conf):
        """ Private constructor:
            instantiate a classifier with the following sub objects by loading the configurations
            a) build data processor
            b) build neural network
            c) build result handler
        """
        self.name = name
        self.conf = conf

        self.data_loader = getattr(__import__(self.conf['data_loader']['module'],
                                              fromlist=[self.conf['data_loader']['class_name']]),
                                   self.conf['data_loader']['class_name'])(
            self.conf['data_loader']['data_config'])

        self.neural_network = getattr(__import__(self.conf['neural_network']['module'],
                                      fromlist=[self.conf['neural_network']['class_name']]),
                                      self.conf['neural_network']['class_name'])(name,
            self.conf['neural_network']['dnn_config'])

        self.result_handler = getattr(__import__(self.conf['result_handler']['module'],
                                                 fromlist=[self.conf['neural_network']['class_name']]),
            self.conf['result_handler']['class_name'])(self.conf['result_handler']['handler_config'])

    def build_model(self):
        """ Method to build the classifier:
            a) load and process the data
            b) build the neural network model
            c) train the model
        """
        self.data_loader.pre_process()
        self.neural_network.build()
        self.neural_network.train(self.data_loader.rows, self.data_loader.labels, True)
        return 'Classifier model ' + self.name + ' is built successfully.'

    def predict(self, data):
        """ Method to predict by the input data """
        ids = [row[0] for row in data]
        data = self.data_loader.process_data(data)
        results = self.neural_network.predict(data)
        return self.result_handler.handle_result(ids, results)
