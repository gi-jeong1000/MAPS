def findDecision(obj): #obj[0]: Alcohol, obj[1]: Malicacid, obj[2]: Ash, obj[3]: Alcalinity_of_ash, obj[4]: Magnesium, obj[5]: Total_phenols, obj[6]: Flavanoids, obj[7]: Nonflavanoid_phenols, obj[8]: Proanthocyanins, obj[9]: Color_intensity, obj[10]: Hue, obj[11]: 0D280_0D315_of_diluted_wines, obj[12]: Proline
   # {"feature": "Flavanoids", "instances": 142, "metric_value": 1.5655, "depth": 1}
   if obj[6] == 'Less_2.39':
      # {"feature": "Color_intensity", "instances": 65, "metric_value": 1.1648, "depth": 2}
      if obj[9] == 'Less_4.475':
         # {"feature": "Proline", "instances": 22, "metric_value": 0.4395, "depth": 3}
         if obj[12] == 'Less_655.0':
            return '2'
         elif obj[12] == 'Less_1192.5':
            # {"feature": "0D280_0D315_of_diluted_wines", "instances": 7, "metric_value": 0.5917, "depth": 4}
            if obj[11] == 'Less_3.42':
               return '2'
            elif obj[11] == 'Greater_3.42':
               return '1'
            else:
               return '2'
         elif obj[12] == 'Greater_1192.5':
            return '1'
         elif obj[12] == 'Less_679.0':
            return '2'
         else:
            return '2'
      elif obj[9] == 'Greater_6.975':
         return '3'
      elif obj[9] == 'Less_2.6100000000000003':
         return '2'
      elif obj[9] == 'Less_6.975':
         # {"feature": "Proline", "instances": 8, "metric_value": 1.4056, "depth": 3}
         if obj[12] == 'Less_655.0':
            # {"feature": "Ash", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[2] == 'Less_2.5700000000000003':
               # {"feature": "Alcohol", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[0]<=12.88:
                  return '3'
               elif obj[0]>12.88:
                  return '2'
               else:
                  return '3'
            elif obj[2] == 'Less_2.295':
               return '2'
            else:
               return '3'
         elif obj[12] == 'Less_1192.5':
            return '1'
         elif obj[12] == 'Less_679.0':
            return '3'
         else:
            return '3'
      else:
         return '3'
   elif obj[6] == 'Greater_2.39':
      # {"feature": "Proline", "instances": 60, "metric_value": 0.8366, "depth": 2}
      if obj[12] == 'Less_1192.5':
         # {"feature": "Alcohol", "instances": 33, "metric_value": 0.4395, "depth": 3}
         if obj[0]>12.921789033591704:
            # {"feature": "Alcalinity_of_ash", "instances": 31, "metric_value": 0.2056, "depth": 4}
            if obj[3] == 'Less_22.25':
               return '1'
            elif obj[3] == 'Less_16.35':
               return '1'
            elif obj[3] == 'Greater_22.25':
               # {"feature": "Magnesium", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[4] == 'Less_127.5':
                  return '1'
               elif obj[4] == 'Greater_127.5':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[0]<=12.921789033591704:
            return '2'
         else:
            return '2'
      elif obj[12] == 'Greater_1192.5':
         return '1'
      elif obj[12] == 'Less_655.0':
         return '2'
      elif obj[12] == 'Less_679.0':
         return '2'
      else:
         return '2'
   elif obj[6] == 'Less_0.625':
      # {"feature": "Malicacid", "instances": 17, "metric_value": 0.3228, "depth": 2}
      if obj[1] == 'Less_4.08':
         return '3'
