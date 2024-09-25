def findDecision(obj): #obj[0]: Alcohol, obj[1]: Malicacid, obj[2]: Ash, obj[3]: Alcalinity_of_ash, obj[4]: Magnesium, obj[5]: Total_phenols, obj[6]: Flavanoids, obj[7]: Nonflavanoid_phenols, obj[8]: Proanthocyanins, obj[9]: Color_intensity, obj[10]: Hue, obj[11]: 0D280_0D315_of_diluted_wines, obj[12]: Proline
   # {"feature": "Alcohol", "instances": 36, "metric_value": 1.5715, "depth": 1}
   if obj[0] == 'Less_14.14':
      # {"feature": "Malicacid", "instances": 19, "metric_value": 1.36, "depth": 2}
      if obj[1]<=2.16:
         # {"feature": "Ash", "instances": 12, "metric_value": 0.65, "depth": 3}
         if obj[2] == 'Greater_1.73':
            # {"feature": "Proanthocyanins", "instances": 11, "metric_value": 0.4395, "depth": 4}
            if obj[8]>0.73:
               return '1'
            elif obj[8]<=0.73:
               return '2'
            else:
               return '2'
         elif obj[2] == 'Less_1.73':
            return '2'
         else:
            return '2'
      elif obj[1]>2.16:
         return '3'
      else:
         return '3'
   elif obj[0] == 'Less_12.83':
      # {"feature": "Hue", "instances": 14, "metric_value": 0.5917, "depth": 2}
      if obj[10] == 'Greater_0.915':
         return '2'
      elif obj[10] == 'Less_0.76':
         return '3'
      elif obj[10] == 'Less_0.85':
         return '2'
      elif obj[10] == 'Less_0.915':
         return '2'
      else:
         return '3'
   elif obj[0] == 'Greater_14.14':
      return '1'
   elif obj[0] == 'Less_13.04':
      return '3'
   else:
      return '3'
