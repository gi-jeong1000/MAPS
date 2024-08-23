def findDecision(obj): #obj[0]: concave_points_worst, obj[1]: perimeter_worst, obj[2]: area_worst
   # {"feature": "perimeter_worst", "instances": 171, "metric_value": 0.9819, "depth": 1}
   if obj[1] == 'Less_104.45':
      # {"feature": "concave_points_worst", "instances": 100, "metric_value": 0.4022, "depth": 2}
      if obj[0] == 'Less_0.1456':
         # {"feature": "area_worst", "instances": 95, "metric_value": 0.2519, "depth": 3}
         if obj[2] == 'Less_932.05':
            return 'B'
         elif obj[2] == 'Less_533.85':
            return 'B'
         else:
            return 'M'
      elif obj[0] == 'Greater_0.17025':
         # {"feature": "area_worst", "instances": 4, "metric_value": 0.8113, "depth": 3}
         if obj[2] == 'Less_932.05':
            return 'M'
         elif obj[2] == 'Less_533.85':
            return 'B'
         else:
            return 'M'
      elif obj[0] == 'Less_0.17025':
         return 'M'
      else:
         return 'M'
   elif obj[1] == 'Greater_118.25':
      # {"feature": "concave_points_worst", "instances": 54, "metric_value": 0.133, "depth": 2}
      if obj[0] == 'Greater_0.17025':
         return 'M'
      elif obj[0] == 'Less_0.1456':
         # {"feature": "area_worst", "instances": 9, "metric_value": 0.5033, "depth": 3}
         if obj[2] == 'Less_2081.0':
            return 'M'
         else:
            return 'M'
      elif obj[0] == 'Less_0.17025':
         return 'M'
      else:
         return 'M'
   elif obj[1] == 'Less_118.25':
      # {"feature": "concave_points_worst", "instances": 17, "metric_value": 0.9367, "depth": 2}
      if obj[0] == 'Less_0.1456':
         # {"feature": "area_worst", "instances": 8, "metric_value": 0.9544, "depth": 3}
         if obj[2] == 'Less_932.05':
            return 'B'
         elif obj[2] == 'Less_2081.0':
            return 'M'
         else:
            return 'M'
      elif obj[0] == 'Less_0.17025':
         # {"feature": "area_worst", "instances": 5, "metric_value": 0.7219, "depth": 3}
         if obj[2] == 'Less_932.05':
            return 'M'
         elif obj[2] == 'Less_2081.0':
            return 'M'
         else:
            return 'M'
      elif obj[0] == 'Greater_0.17025':
         return 'M'
      else:
         return 'M'
   else:
      return 'M'
