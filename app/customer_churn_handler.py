class CustomerChurnHandler:
    class CustomerChurnResult:
        def __init__(self, customer_id, churn, score):
            self.id = customer_id
            self.churn = churn
            self.score = score

    def __init__(self, conf_file):
        self.results = []

    def handle_result(self, ids, data):
        self.results = []
        for i in range(len(data)):
            result = CustomerChurnHandler.CustomerChurnResult(ids[i], 'Yes' if data[i][1] >= 0.5 else 'No', round(data[i][0] * 100, 2))
            self.results.append(result)
        return self.results


