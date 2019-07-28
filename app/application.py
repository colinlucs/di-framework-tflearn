from framework.application_context import ApplicationContext


class CustomerRetentionApp:
    def __init__(self):
        self.application = ApplicationContext.get_instance('conf/application_context.yaml')

    def build_model(self, name):
        self.application.get_classifier(name).build_model()

    def predict(self, name, data):
        return self.application.get_classifier(name).predict(data)

