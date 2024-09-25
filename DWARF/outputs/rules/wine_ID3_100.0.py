def findDecision(obj): #obj[0]: Alcohol, obj[1]: Malicacid, obj[2]: Ash, obj[3]: Alcalinity_of_ash, obj[4]: Magnesium, obj[5]: Total_phenols, obj[6]: Flavanoids, obj[7]: Nonflavanoid_phenols, obj[8]: Proanthocyanins, obj[9]: Color_intensity, obj[10]: Hue, obj[11]: 0D280_0D315_of_diluted_wines, obj[12]: Proline
   # {"feature": "Proline", "instances": 36, "metric_value": 1.5715, "depth": 1}
   if obj[12]<=776.1388888888889:
      # {"feature": "Flavanoids", "instances": 23, "metric_value": 0.9656, "depth": 2}
      if obj[6] == 'Less_3.34':
         return '2'
      elif obj[6] == 'Less_1.585':
         # {"feature": "Alcohol", "instances": 10, "metric_value": 0.469, "depth": 3}
         if obj[0]>12.33:
            return '3'
         elif obj[0]<=12.33:
            return '2'
         else:
            return '3'
      elif obj[6] == 'Greater_3.34':
         return '2'
      else:
         return '3'
   elif obj[12]>776.1388888888889:
      # {"feature": "Flavanoids", "instances": 13, "metric_value": 0.3912, "depth": 2}
      if obj[6] == 'Less_3.34':
         return '1'
      elif obj[6] == 'Greater_3.34':
         return '1'
      elif obj[6] == 'Less_1.585':
         return '3'
      else:
         return '3'
   else:
      return '3'
