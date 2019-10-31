# A Configuration-based Dependency Injection Framework for Building Deep Learning Models on TFLearn

This is a sample project of "Smart Customer Retention" building deep learning models using a configuration-based dependency injection  on TFLearn.

---

## Overview
This sample consists of the following parts:
* __framework__

	A dependency injection frameowrk with pre-built python modules to build deep learning models on TFLearn and TensorFlow.
	
* __app__

    A sample application: "Smart Customer Retntion" having two classifiers of predicting customer churn and providing customer retention recommendations.
    
---

## How to Use
### Prerequisite

* [Python](https://www.python.org/)
* [TensorFlow](https://www.tensorflow.org/)
* [TFLearn](http://tflearn.org/)
* [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)

### Build Deep Learning Model by YAML Configurations
#### Customer Churn
##### Dataset
The sample dataset can be found as [di-framework-tflearn/app/data/customer_churn.csv](https://github.com/colinlucs/di-framework-tflearn/blob/master/app/data/customer_churn.csv)
![](https://github.com/colinlucs/di-framework-tflearn/blob/master/app/res/Sample%20customer%20churn%20data.png)

---

##### Dataset Pre-process Configurations
Prepare a YAML for the dataset pre-processing as [di-framework-tflearn/app/conf/customer_churn/data_conf.yaml](https://github.com/colinlucs/di-framework-tflearn/blob/master/app/conf/customer_churn/data_conf.yaml)
```yaml
# Dataset Pre-processing Configurations for Customer Churn
data_file: data/customer_churn.csv
target_column: 0
n_classes: 2
columns_to_ignore:
  - 0
conversion_map:
  0:
    - 'Female'
    - 'Male'
  1:
    - 'K-12 student'
    - 'Unemployed'
    - 'College/Grad student'
    - 'Food Preparation and Serving Related'
    - 'Personal Care and Service'
    - 'Building and Grounds Cleaning and Maintenance'
    - 'Farming, Fishing, and Forestry'
    - 'Healthcare Support Occupations'
    - 'Self-employed'
    - 'Transportation and Material Moving'
    - 'Office and Administrative Support'
    - 'Production Occupations'
    - 'Sales and Related'
    - 'Retired'
    - 'Protective Service'
    - 'Installation, Maintenance, and Repair'
    - 'Community and Social Service'
    - 'Construction and Extraction'
    - 'Other - Not specified'
    - 'Education, Training, and Library'
    - 'Arts, Design, Entertainment, Sports, and Media'
    - 'Life, Physical, and Social Science'
    - 'Business and Financial Operations'
    - 'Healthcare Practitioners and Technical'
    - 'Architecture and Engineering'
    - 'Computer and Mathematical'
    - 'Legal Occupations'
    - 'Executive/Management'
  3:
    - 'No'
    - 'Yes'
  4:
    - 'No'
    - 'Yes'
  6:
    - 'No'
    - 'Yes'
  7:
    - 'No'
    - 'Yes'
  8:
    - 'Bundle'
    - 'Wireless'
    - 'Internet'
    - 'TV'
    - 'Home Phone'
```

---

##### Deep Learning Model Configurations
Prepare a YAML for the deep learning model configurations [di-framework-tflearn/app/conf/customer_churn/dnn_conf.yaml](https://github.com/colinlucs/di-framework-tflearn/blob/master/app/conf/customer_churn/dnn_conf.yaml)
```yaml
# Deep Neural Network Configurations
input_layer:
  shape:
    -
    - 9
hidden_layers:
    - type: 'fully_connected'
      neuron: 32
      activation: 'relu'
      dropout:
    - type: 'fully_connected'
      neuron: 32
      activation: 'relu'
      dropout:
    - type: 'fully_connected'
      neuron: 32
      activation: 'relu'
      dropout:
output_layer:
    type: 'fully_connected'
    neuron: 2
    activation: 'softmax'
regression:
  optimizer: 'adam'
  loss: 'categorical_crossentropy'
fit:
  n_epoch: 10
  batch_size: 16
  show_metric: True

```

#### Customer Retention Recommendations
##### Dataset
The sample dataset can be found as [di-framework-tflearn/app/data/customer_retention.csv](https://github.com/colinlucs/di-framework-tflearn/blob/master/app/data/customer_retention.csv)
![](https://github.com/colinlucs/di-framework-tflearn/blob/master/app/res/Sample%20customer%20retention%20data.png)

---

##### Dataset Pre-process Configurations
Prepare a YAML for the dataset pre-processing as [di-framework-tflearn/app/conf/customer_retention/data_conf.yaml](https://github.com/colinlucs/di-framework-tflearn/blob/master/app/conf/customer_retention/data_conf.yaml)
```yaml
# Dataset Pre-processing Configurations for Customer Retention
data_file: data/customer_retention.csv
target_column: 0
n_classes: 10
columns_to_ignore:
  - 0
conversion_map:
  0:
    - 'Female'
    - 'Male'
  1:
    - 'K-12 student'
    - 'Unemployed'
    - 'College/Grad student'
    - 'Food Preparation and Serving Related'
    - 'Personal Care and Service'
    - 'Building and Grounds Cleaning and Maintenance'
    - 'Farming, Fishing, and Forestry'
    - 'Healthcare Support Occupations'
    - 'Self-employed'
    - 'Transportation and Material Moving'
    - 'Office and Administrative Support'
    - 'Production Occupations'
    - 'Sales and Related'
    - 'Retired'
    - 'Protective Service'
    - 'Installation, Maintenance, and Repair'
    - 'Community and Social Service'
    - 'Construction and Extraction'
    - 'Other - Not specified'
    - 'Education, Training, and Library'
    - 'Arts, Design, Entertainment, Sports, and Media'
    - 'Life, Physical, and Social Science'
    - 'Business and Financial Operations'
    - 'Healthcare Practitioners and Technical'
    - 'Architecture and Engineering'
    - 'Computer and Mathematical'
    - 'Legal Occupations'
    - 'Executive/Management'
  3:
    - 'No'
    - 'Yes'
  4:
    - 'No'
    - 'Yes'
  6:
    - 'No'
    - 'Yes'
  7:
    - 'No'
    - 'Yes'
  8:
    - 'Bundle'
    - 'Wireless'
    - 'Internet'
    - 'TV'
    - 'Home Phone'

```

---

##### Deep Learning Model Configurations
Prepare a YAML for the deep learning model configurations [di-framework-tflearn/app/conf/customer_retention/dnn_conf.yaml](https://github.com/colinlucs/di-framework-tflearn/blob/master/app/conf/customer_retention/dnn_conf.yaml)
```yaml
# Deep Neural Network Configurations
input_layer:
  shape:
    -
    - 9
hidden_layers:
    - type: 'fully_connected'
      neuron: 32
      activation: 'relu'
      dropout:
    - type: 'fully_connected'
      neuron: 32
      activation: 'relu'
      dropout:
    - type: 'fully_connected'
      neuron: 32
      activation: 'relu'
      dropout:
output_layer:
    type: 'fully_connected'
    neuron: 10
    activation: 'softmax'
regression:
  optimizer: 'adam'
  loss: 'categorical_crossentropy'
fit:
  n_epoch: 10
  batch_size: 16
  show_metric: True

```

##### Result Handling Configurations
Prepare a YAML for the result handling configurations [di-framework-tflearn/app/conf/customer_retention/handler_conf.yaml](https://github.com/colinlucs/di-framework-tflearn/blob/master/app/conf/customer_retention/handler_conf.yaml)
```yaml
# Configurations for the Result Handling
recommendation_map:
  0: 'Service Discount or Account Credit'
  1: 'Plan Upgrade'
  2: 'Service or Plan Downgrade'
  3: 'Additional Add-on Services'
  4: 'Additional Service Usage'
  5: 'Service Quality Upgrade'
  6: 'Free New Install or Move'
  7: 'Extended Promotion or Price Lock Down'
  8: 'Free Devices or Device Upgrade'
  9: 'Free Accessories'

```

### Train Deep Learning Model
#### Traing Model for Customer Churn
```
$ python3 application.py build_model customer_churn

```

Or just add the following python code in your own file:

```python
application = ApplicationContext.get_instance('conf/application_context.yaml')
application.get_classifier('customer_churn').build_model()

```

Model training result:
```
Training Step: 62413  | total loss: 0.44890 | time: 12.836s
| Adam | epoch: 010 | loss: 0.44890 - acc: 0.7902 -- iter: 098608/100000
Training Step: 62414  | total loss: 0.44431 | time: 12.839s
| Adam | epoch: 010 | loss: 0.44431 - acc: 0.7987 -- iter: 098624/100000
Training Step: 62415  | total loss: 0.43820 | time: 12.841s
| Adam | epoch: 010 | loss: 0.43820 - acc: 0.8063 -- iter: 098640/100000
Training Step: 62416  | total loss: 0.44525 | time: 12.843s
| Adam | epoch: 010 | loss: 0.44525 - acc: 0.8007 -- iter: 098656/100000
Training Step: 62417  | total loss: 0.44385 | time: 12.846s
| Adam | epoch: 010 | loss: 0.44385 - acc: 0.8081 -- iter: 098672/100000
Training Step: 62418  | total loss: 0.43768 | time: 12.849s
| Adam | epoch: 010 | loss: 0.43768 - acc: 0.8148 -- iter: 098688/100000
Training Step: 62419  | total loss: 0.43572 | time: 12.852s
| Adam | epoch: 010 | loss: 0.43572 - acc: 0.8146 -- iter: 098704/100000
Training Step: 62420  | total loss: 0.42419 | time: 12.854s
| Adam | epoch: 010 | loss: 0.42419 - acc: 0.8269 -- iter: 098720/100000
Training Step: 62421  | total loss: 0.46038 | time: 12.857s

```

---

#### Traing Model for Customer Retention Recommendations
```
$ python3 application.py build_model customer_retention

```

Or just add the following python code in your own file:

```python
application = ApplicationContext.get_instance('conf/application_context.yaml')
application.get_classifier('customer_retention').build_model()

```

Model training result:
```
Training Step: 46245  | total loss: 0.95121 | time: 9.543s
| Adam | epoch: 010 | loss: 0.95121 - acc: 0.6169 -- iter: 73344/74059
Training Step: 46246  | total loss: 0.92046 | time: 9.545s
| Adam | epoch: 010 | loss: 0.92046 - acc: 0.6427 -- iter: 73360/74059
Training Step: 46247  | total loss: 0.93448 | time: 9.547s
| Adam | epoch: 010 | loss: 0.93448 - acc: 0.6222 -- iter: 73376/74059
Training Step: 46248  | total loss: 0.94637 | time: 9.549s
| Adam | epoch: 010 | loss: 0.94637 - acc: 0.6162 -- iter: 73392/74059
Training Step: 46249  | total loss: 0.92596 | time: 9.550s
| Adam | epoch: 010 | loss: 0.92596 - acc: 0.6296 -- iter: 73408/74059
Training Step: 46250  | total loss: 0.91109 | time: 9.551s
| Adam | epoch: 010 | loss: 0.91109 - acc: 0.6416 -- iter: 73424/74059
Training Step: 46251  | total loss: 0.89691 | time: 9.553s
| Adam | epoch: 010 | loss: 0.89691 - acc: 0.6400 -- iter: 73440/74059
Training Step: 46252  | total loss: 0.90367 | time: 9.555s
| Adam | epoch: 010 | loss: 0.90367 - acc: 0.6447 -- iter: 73456/74059
Training Step: 46253  | total loss: 0.89138 | time: 9.557s
| Adam | epoch: 010 | loss: 0.89138 - acc: 0.6490 -- iter: 73472/74059
Training Step: 46254  | total loss: 0.87089 | time: 9.559s
| Adam | epoch: 010 | loss: 0.87089 - acc: 0.6591 -- iter: 73488/74059
Training Step: 46255  | total loss: 0.86833 | time: 9.561s
| Adam | epoch: 010 | loss: 0.86833 - acc: 0.6557 -- iter: 73504/74059

```

---

### Run Deep Learning Model
#### Run Model for Customer Churn Prediction
```
$ python3 application.py predict customer_churn

```

Or just add the following python code in your own file for the sample customers:

```python
tony = ['4d316bef-9856-4ea0-aed0-a53e55fed3db', 'Male', 'K-12 student', 20, 'No', 'Yes', 12, 'No', 'No',
                    'Wireless']
john = ['4d316bef-9856-4ea0-aed0-a53e55fed3df', 'Male', 'Sales and Related', 75, 'Yes', 'Yes', 26, 'Yes',
                    'No', 'Wireless']
mary = ['7150ae6c-1120-4eb5-b788-0f822f986fae', 'Female', 'Executive/Management', 90, 'No', 'No', 36, 'Yes',
                    'Yes', 'Bundle']
data = [tony, john, mary]
application = ApplicationContext.get_instance('conf/application_context.yaml')
application.get_classifier('customer_churn').predict(data)

```

Prediction result for customer churn and loyalty score:
```
Customer churn prediction for Tony - churn:Yes - score:1.53
Customer churn prediction for John - churn:No - score:73.91
Customer churn prediction for Mary - churn:No - score:99.41

```

#### Run Model for Customer Retention Recommendations
```
$ python3 application.py predict customer_retention

```

Or just add the following python code in your own file for the sample customers:

```python
tony = ['4d316bef-9856-4ea0-aed0-a53e55fed3db', 'Male', 'K-12 student', 20, 'No', 'Yes', 12, 'No', 'No',
                    'Wireless']
john = ['4d316bef-9856-4ea0-aed0-a53e55fed3df', 'Male', 'Sales and Related', 75, 'Yes', 'Yes', 26, 'Yes',
                    'No', 'Wireless']
mary = ['7150ae6c-1120-4eb5-b788-0f822f986fae', 'Female', 'Executive/Management', 90, 'No', 'No', 36, 'Yes',
                    'Yes', 'Bundle']
data = [tony, john, mary]
application = ApplicationContext.get_instance('conf/application_context.yaml')
application.get_classifier('customer_churn').predict(data)

```

Recommended Customer Retention Offers:
```
Top3 retention recommendations for Tony: 
 1: Service or Plan Downgrade 
 2: Service Discount or Account Credit  
 3: Extended Promotion or Price Lock Down
 
Top3 retention recommendations for John: 
 1: Additional Add-on Services 
 2: Service Discount or Account Credit  
 3: Extended Promotion or Price Lock Down
 
Top3 retention recommendations for Mary: 
 1: Additional Service Usage 
 2: Plan Upgrade  
 3: Service Quality Upgrade

```
