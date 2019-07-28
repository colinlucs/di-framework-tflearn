import sys
from framework.application_context import ApplicationContext


class CustomerRetentionApp:
    def __init__(self):
        self.application = ApplicationContext.get_instance('conf/application_context.yaml')

    def build_model(self, name):
        self.application.get_classifier(name).build_model()

    def predict(self, name, data):
        return self.application.get_classifier(name).predict(data)


if __name__ == '__main__':
    app = CustomerRetentionApp()
    if sys.argv[1] == 'build_model':
        app.build_model(sys.argv[2])
    elif sys.argv[1] == 'predict':
        tony = ['4d316bef-9856-4ea0-aed0-a53e55fed3db', 'Male', 'K-12 student', 20, 'No', 'Yes', 12, 'No', 'No',
                    'Wireless']
        john = ['4d316bef-9856-4ea0-aed0-a53e55fed3df', 'Male', 'Sales and Related', 75, 'Yes', 'Yes', 26, 'Yes',
                    'No', 'Wireless']
        mary = ['7150ae6c-1120-4eb5-b788-0f822f986fae', 'Female', 'Executive/Management', 90, 'No', 'No', 36, 'Yes',
                    'Yes', 'Bundle']
        result = app.predict(sys.argv[2], [tony, john, mary])
        if sys.argv[2] == 'customer_churn':
            print("Customer churn prediction for Tony - churn:{} - score:{}".format(result[0].churn, result[0].score))
            print("Customer churn prediction for John - churn:{} - score:{}".format(result[1].churn, result[1].score))
            print("Customer churn prediction for Mary - churn:{} - score:{}".format(result[2].churn, result[2].score))
        else:
            print("Top3 retention recommendations for Tony: \n 1: {} \n 2: {}  \n 3: {}".format(
                result[0].recommendations[0],
                result[0].recommendations[1],
                result[0].recommendations[2]))
            print("Top3 retention recommendations for John: \n 1: {} \n 2: {}  \n 3: {}".format(
                result[1].recommendations[0],
                result[1].recommendations[1],
                result[1].recommendations[2]))
            print("Top3 retention recommendations for Mary: \n 1: {} \n 2: {}  \n 3: {}".format(
                result[2].recommendations[0],
                result[2].recommendations[1],
                result[2].recommendations[2]))
