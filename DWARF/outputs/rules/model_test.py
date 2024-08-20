def findDecision(obj): #obj[0]: alcohol, obj[1]: sulphates, obj[2]: volatile acidity, obj[3]: total sulfur dioxide, obj[4]: density, obj[5]: chlorides, obj[6]: pH, obj[7]: fixed acidity, obj[8]: free sulfur dioxide, obj[9]: residual sugar
   # {"feature": "alcohol", "instances": 1598, "metric_value": 0.9965, "depth": 1}
   if obj[0] == 'Less_11.850000000000001':
      # {"feature": "sulphates", "instances": 484, "metric_value": 0.9237, "depth": 2}
      if obj[1] == 'Greater_0.665':
         # {"feature": "volatile acidity", "instances": 221, "metric_value": 0.7714, "depth": 3}
         if obj[2] == 'Less_0.405':
            # {"feature": "chlorides", "instances": 92, "metric_value": 0.5281, "depth": 4}
            if obj[5] == 'Less_0.0905':
               # {"feature": "fixed acidity", "instances": 73, "metric_value": 0.4558, "depth": 5}
               if obj[7] == 'Greater_9.149999999999999':
                  return 'good'
               elif obj[7] == 'Less_9.149999999999999':
                  return 'good'
               elif obj[7] == 'Less_7.65':
                  return 'good'
               else:
                  return 'good'
            elif obj[5] == 'Less_0.242':
               # {"feature": "fixed acidity", "instances": 10, "metric_value": 0.7219, "depth": 5}
               if obj[7] == 'Greater_9.149999999999999':
                  return 'good'
               elif obj[7] == 'Less_9.149999999999999':
                  return 'bad'
               else:
                  return 'good'
            elif obj[5] == 'Less_0.058499999999999996':
               # {"feature": "fixed acidity", "instances": 8, "metric_value": 0.5436, "depth": 5}
               if obj[7] == 'Less_9.149999999999999':
                  return 'good'
               elif obj[7] == 'Greater_9.149999999999999':
                  return 'good'
               elif obj[7] == 'Less_7.65':
                  return 'good'
               else:
                  return 'good'
            elif obj[5] == 'Greater_0.242':
               return 'bad'
            else:
               return 'good'
         elif obj[2] == 'Less_0.6174999999999999':
            # {"feature": "density", "instances": 87, "metric_value": 0.8498, "depth": 4}
            if obj[4] == 'Less_0.9978549999999999':
               # {"feature": "residual sugar", "instances": 54, "metric_value": 0.8987, "depth": 5}
               if obj[9] == 'Less_2.75':
                  return 'good'
               elif obj[9] == 'Greater_2.75':
                  return 'bad'
               else:
                  return 'good'
            elif obj[4] == 'Greater_0.99821':
               # {"feature": "fixed acidity", "instances": 15, "metric_value": 0.9183, "depth": 5}
               if obj[7] == 'Greater_9.149999999999999':
                  return 'good'
               elif obj[7] == 'Less_7.65':
                  return 'bad'
               else:
                  return 'good'
            elif obj[4] == 'Less_0.9949950000000001':
               return 'good'
            elif obj[4] == 'Less_0.99821':
               # {"feature": "chlorides", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[5] == 'Less_0.242':
                  return 'bad'
               elif obj[5] == 'Less_0.0905':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[2] == 'Greater_0.6174999999999999':
            # {"feature": "density", "instances": 36, "metric_value": 0.9436, "depth": 4}
            if obj[4] == 'Less_0.9978549999999999':
               # {"feature": "chlorides", "instances": 20, "metric_value": 0.8813, "depth": 5}
               if obj[5] == 'Less_0.0905':
                  return 'good'
               elif obj[5] == 'Less_0.242':
                  return 'good'
               else:
                  return 'good'
            elif obj[4] == 'Greater_0.99821':
               # {"feature": "chlorides", "instances": 13, "metric_value": 0.8905, "depth": 5}
               if obj[5] == 'Less_0.0905':
                  return 'good'
               elif obj[5] == 'Less_0.242':
                  return 'bad'
               else:
                  return 'good'
            elif obj[4] == 'Less_0.9949950000000001':
               return 'bad'
            elif obj[4] == 'Less_0.99821':
               return 'bad'
            else:
               return 'good'
         elif obj[2] == 'Less_0.195':
            # {"feature": "density", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[4] == 'Less_0.9949950000000001':
               # {"feature": "free sulfur dioxide", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[8] == 'Greater_9.5':
                  return 'good'
               elif obj[8] == 'Less_9.5':
                  return 'bad'
               else:
                  return 'good'
            elif obj[4] == 'Greater_0.99821':
               return 'good'
            elif obj[4] == 'Less_0.9978549999999999':
               return 'bad'
            else:
               return 'good'
         else:
            return 'good'
      elif obj[1] == 'Less_0.665':
         # {"feature": "density", "instances": 155, "metric_value": 0.9267, "depth": 3}
         if obj[4] == 'Less_0.9978549999999999':
            # {"feature": "pH", "instances": 103, "metric_value": 0.8703, "depth": 4}
            if obj[6] == 'Less_3.525':
               # {"feature": "chlorides", "instances": 90, "metric_value": 0.8813, "depth": 5}
               if obj[5] == 'Less_0.0905':
                  return 'good'
               elif obj[5] == 'Less_0.242':
                  return 'good'
               elif obj[5] == 'Less_0.058499999999999996':
                  return 'good'
               elif obj[5] == 'Greater_0.242':
                  return 'good'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.815':
               # {"feature": "chlorides", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[5] == 'Less_0.0905':
                  return 'good'
               elif obj[5] == 'Less_0.242':
                  return 'bad'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.075':
               return 'good'
            else:
               return 'good'
         elif obj[4] == 'Greater_0.99821':
            # {"feature": "pH", "instances": 30, "metric_value": 0.971, "depth": 4}
            if obj[6] == 'Less_3.525':
               # {"feature": "volatile acidity", "instances": 26, "metric_value": 0.8905, "depth": 5}
               if obj[2] == 'Less_0.6174999999999999':
                  return 'good'
               elif obj[2] == 'Greater_0.6174999999999999':
                  return 'bad'
               elif obj[2] == 'Less_0.405':
                  return 'good'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.815':
               return 'bad'
            elif obj[6] == 'Less_3.075':
               return 'bad'
            else:
               return 'good'
         elif obj[4] == 'Less_0.9949950000000001':
            # {"feature": "pH", "instances": 16, "metric_value": 0.896, "depth": 4}
            if obj[6] == 'Less_3.525':
               # {"feature": "volatile acidity", "instances": 12, "metric_value": 0.65, "depth": 5}
               if obj[2] == 'Less_0.6174999999999999':
                  return 'good'
               elif obj[2] == 'Greater_0.6174999999999999':
                  return 'good'
               elif obj[2] == 'Less_0.405':
                  return 'bad'
               else:
                  return 'good'
            elif obj[6] == 'Less_3.815':
               # {"feature": "total sulfur dioxide", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[3] == 'Greater_35.5':
                  return 'bad'
               elif obj[3] == 'Less_35.5':
                  return 'bad'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[4] == 'Less_0.99821':
            return 'bad'
         else:
            return 'good'
      elif obj[1] == 'Less_0.575':
         # {"feature": "volatile acidity", "instances": 71, "metric_value": 0.9999, "depth": 3}
         if obj[2] == 'Greater_0.6174999999999999':
            # {"feature": "density", "instances": 31, "metric_value": 0.9072, "depth": 4}
            if obj[4] == 'Less_0.9978549999999999':
               # {"feature": "total sulfur dioxide", "instances": 20, "metric_value": 0.7219, "depth": 5}
               if obj[3] == 'Less_35.5':
                  return 'bad'
               elif obj[3] == 'Greater_35.5':
                  return 'bad'
               else:
                  return 'good'
            elif obj[4] == 'Greater_0.99821':
               # {"feature": "residual sugar", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[9] == 'Greater_2.75':
                  return 'bad'
               elif obj[9] == 'Less_2.75':
                  return 'good'
               else:
                  return 'good'
            elif obj[4] == 'Less_0.9949950000000001':
               # {"feature": "total sulfur dioxide", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[3] == 'Less_35.5':
                  return 'bad'
               elif obj[3] == 'Greater_35.5':
                  return 'good'
               else:
                  return 'good'
            elif obj[4] == 'Less_0.99821':
               return 'bad'
            else:
               return 'good'
         elif obj[2] == 'Less_0.6174999999999999':
            # {"feature": "fixed acidity", "instances": 28, "metric_value": 0.9852, "depth": 4}
            if obj[7] == 'Less_7.65':
               # {"feature": "total sulfur dioxide", "instances": 14, "metric_value": 0.9852, "depth": 5}
               if obj[3] == 'Less_35.5':
                  return 'good'
