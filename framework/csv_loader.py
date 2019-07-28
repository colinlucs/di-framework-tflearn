import yaml
import numpy as np

from tflearn.data_utils import load_csv


class CsvLoader:
    """A data processor for the csv dataset"""
    def __init__(self, conf_file):
        """ Private constructor initializing the csv data loader with configurations"""
        with open(conf_file) as f:
            # use safe_load instead load
            self.data_conf = yaml.safe_load(f)

        self.rows, self.labels = load_csv(self.data_conf['data_file'],
                                          target_column=self.data_conf['target_column'],
                                          categorical_labels=True, n_classes=self.data_conf['n_classes'])

        self.columns_to_ignore = self.data_conf['columns_to_ignore']
        self.conversion_map = self.data_conf['conversion_map']

    def __pre_process_data__(self, rows):
        """private method of csv data pre-processing"""
        if rows is None:
            rows = self.rows
        # Sort by descending id and delete columns
        for column_to_ignore in sorted(self.columns_to_ignore, reverse=True):
            [row.pop(column_to_ignore) for row in rows]
        for i in range(len(rows)):
            # Converting data by converting_map
            for j in range(len(rows[i])):
                if j in self.conversion_map:
                    rows[i][j] = self.conversion_map[j].index(rows[i][j])
        return np.array(rows, dtype=np.float32)

    def pre_process(self):
        """public method of data pre-processing"""
        self.rows = self.__pre_process_data__(None)

    def process_data(self, rows):
        """public method of data processing"""
        return self.__pre_process_data__(rows)

