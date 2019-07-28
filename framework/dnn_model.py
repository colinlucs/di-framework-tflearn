import yaml
import tflearn


class DnnModel:
    def __init__(self, name, conf_file):
        with open(conf_file) as f:
            # use safe_load instead load
            self.model_conf = yaml.safe_load(f)
        self.model = None
        self.name = name
        self.path = 'model/' + self.name + '/' + self.name + '.tfmodel'

    def __load__(self):
        self.model.load(self.path)

    def build(self):
        net = tflearn.input_data(shape=self.model_conf['input_layer']['shape'])
        for i in range(len(self.model_conf['hidden_layers'])):
            net = getattr(tflearn, self.model_conf['hidden_layers'][i]['type'])(net, self.model_conf[
                'hidden_layers'][i]['neuron'], activation=self.model_conf['hidden_layers'][i]['activation'])
            if self.model_conf['hidden_layers'][i]['dropout'] is not None:
                net = tflearn.dropout(net, self.model_conf['hidden_layers'][i]['dropout'])

        net = getattr(tflearn, self.model_conf['output_layer']['type'])(net, self.model_conf[
            'output_layer']['neuron'], activation=self.model_conf['output_layer']['activation'])

        net = tflearn.regression(net, optimizer=self.model_conf['regression']['optimizer'],
                                 loss=self.model_conf['regression']['loss'])

        # Define model
        self.model = tflearn.DNN(net)
        return self.model

    def train(self, data, labels, save_model):
        self.model.fit(data, labels, n_epoch=self.model_conf['fit']['n_epoch'],
                       batch_size=self.model_conf['fit']['batch_size'],
                       show_metric=self.model_conf['fit']['show_metric'])
        if save_model:
            self.model.save(self.path)

    def predict(self, data):
        if self.model is None:
            self.build()
            self.__load__()
        return self.model.predict(data)
