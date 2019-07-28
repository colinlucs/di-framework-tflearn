import yaml


class ApplicationContext:
    """ This is a singleton class initializing the application and working as a classifier factory. """
    __instance = None

    @staticmethod
    def get_instance(name):
        """ Static method of getting the singleton instance """
        if ApplicationContext.__instance is None:
            ApplicationContext(name)
        return ApplicationContext.__instance

    def __init__(self, name):
        """ Private constructor instantiates a singleton object.
            Create classifier instances using reflection based on configurations.
        """
        if ApplicationContext.__instance is None:
            self.classifier_instances = {}
            with open(name) as f:
                self.classifiers = yaml.safe_load(f)['classifiers']
            for classifier in self.classifiers:
                module_name = self.classifiers[classifier]['module']
                class_name = self.classifiers[classifier]['class_name']
                self.classifier_instances[classifier] = getattr(__import__(module_name, fromlist=[class_name]), class_name)(
                        classifier, self.classifiers[classifier])
            ApplicationContext.__instance = self

    def get_classifier(self, classifier):
        """ Method to get classifier instance by its name"""
        return self.classifier_instances[classifier]


