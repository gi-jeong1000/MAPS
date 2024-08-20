def findDecision(obj): #obj[0]: alcohol, obj[1]: sulphates, obj[2]: volatile acidity, obj[3]: total sulfur dioxide, obj[4]: chlorides, obj[5]: fixed acidity, obj[6]: pH, obj[7]: citric acid
   # {"feature": "alcohol", "instances": 1598, "metric_value": 0.9965, "depth": 1}
   if obj[0] == 'Less_11.149999999999999':
      # {"feature": "sulphates", "instances": 846, "metric_value": 0.9824, "depth": 2}
      if obj[1] == 'Greater_0.555':
         # {"feature": "chlorides", "instances": 601, "metric_value": 0.9988, "depth": 3}
         if obj[4] == 'Less_0.0935':
            # {"feature": "volatile acidity", "instances": 446, "metric_value": 0.986, "depth": 4}
            if obj[2] == 'Greater_0.4175':
               # {"feature": "total sulfur dioxide", "instances": 308, "metric_value": 0.9995, "depth": 5}
               if obj[3] == 'Less_56.5':
                  return 'good'
               elif obj[3] == 'Greater_56.5':
                  return 'bad'
               else:
                  return 'good'
            elif obj[2] == 'Less_0.4175':
               # {"feature": "citric acid", "instances": 138, "metric_value": 0.8865, "depth": 5}
               if obj[7] == 'Less_0.585':
                  return 'good'
               elif obj[7] == 'Less_0.255':
                  return 'bad'
               elif obj[7] == 'Greater_0.585':
                  return 'bad'
               else:
                  return 'good'
            else:
               return 'good'
