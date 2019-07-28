import yaml


class CustomerRetentionHandler:
    class CustomerRetentionResult:
        def __init__(self, customer_id, recommendations):
            self.id = customer_id
            self.recommendations = recommendations

    def __init__(self, conf_file):
        self.results = []
        with open(conf_file) as f:
            # use safe_load instead load
            self.data_conf = yaml.safe_load(f)

        self.recommendation_map = self.data_conf['recommendation_map']

    def handle_result(self, ids, data):
        self.results = []
        for i in range(len(data)):
            retentions = sorted(range(len(data[i])), key=lambda k: data[i][k], reverse=True)[:3]
            retention_labels = list(map(lambda x: self.recommendation_map[x], retentions))
            retention = CustomerRetentionHandler.CustomerRetentionResult(ids[i], retention_labels)
            self.results.append(retention)
        return self.results


