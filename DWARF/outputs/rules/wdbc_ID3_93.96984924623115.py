def findDecision(obj): #obj[0]: concave_points_worst, obj[1]: radius_worst, obj[2]: perimeter_worst, obj[3]: area_worst
   # {"feature": "concave_points_worst", "instances": 171, "metric_value": 0.9792, "depth": 1}
   if obj[0] == 'Less_0.1527':
      # {"feature": "perimeter_worst", "instances": 68, "metric_value": 0.8546, "depth": 2}
      if obj[2] == 'Less_127.75':
         # {"feature": "radius_worst", "instances": 52, "metric_value": 0.7444, "depth": 3}
         if obj[1] == 'Less_21.615':
            # {"feature": "area_worst", "instances": 40, "metric_value": 0.8485, "depth": 4}
            if obj[3] == 'Less_2020.5':
               return 'B'
            else:
               return 'M'
         elif obj[1] == 'Less_13.325':
            return 'B'
         else:
            return 'M'
      elif obj[2] == 'Greater_127.75':
         return 'M'
      elif obj[2] == 'Less_79.745':
         return 'B'
      else:
         return 'M'
   elif obj[0] == 'Less_0.07577500000000001':
      return 'B'
   elif obj[0] == 'Greater_0.15625':
      return 'M'
   elif obj[0] == 'Less_0.15625':
      # {"feature": "radius_worst", "instances": 3, "metric_value": 0.9183, "depth": 2}
      if obj[1] == 'Greater_21.615':
         return 'M'
      elif obj[1] == 'Less_13.325':
         return 'B'
      elif obj[1] == 'Less_21.615':
         return 'M'
      else:
         return 'M'
   else:
      return 'M'
