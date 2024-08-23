def findDecision(obj): #obj[0]: concave_points_worst, obj[1]: radius_worst, obj[2]: perimeter_worst, obj[3]: concave_points_mean, obj[4]: area_worst
   # {"feature": "area_worst", "instances": 171, "metric_value": 0.966, "depth": 1}
   if obj[4] == 'Less_798.6500000000001':
      # {"feature": "concave_points_worst", "instances": 97, "metric_value": 0.199, "depth": 2}
      if obj[0] == 'Less_0.081535':
         return 'B'
      elif obj[0] == 'Less_0.1844':
         # {"feature": "perimeter_worst", "instances": 45, "metric_value": 0.3534, "depth": 3}
         if obj[2] == 'Less_110.35':
            # {"feature": "radius_worst", "instances": 41, "metric_value": 0.3776, "depth": 4}
            if obj[1] == 'Less_16.165':
               # {"feature": "concave_points_mean", "instances": 41, "metric_value": 0.3776, "depth": 5}
               if obj[3] == 'Greater_0.009776':
                  return 'B'
               else:
                  return 'M'
            else:
               return 'M'
         elif obj[2] == 'Less_74.77':
            return 'B'
         else:
            return 'M'
      else:
         return 'M'
   elif obj[4] == 'Greater_979.3':
      return 'M'
   elif obj[4] == 'Less_979.3':
      # {"feature": "perimeter_worst", "instances": 24, "metric_value": 0.9799, "depth": 2}
      if obj[2] == 'Less_110.35':
         # {"feature": "concave_points_worst", "instances": 14, "metric_value": 0.9403, "depth": 3}
         if obj[0] == 'Less_0.1844':
            # {"feature": "radius_worst", "instances": 12, "metric_value": 0.9183, "depth": 4}
            if obj[1] == 'Greater_16.165':
               # {"feature": "concave_points_mean", "instances": 12, "metric_value": 0.9183, "depth": 5}
               if obj[3] == 'Greater_0.009776':
                  return 'B'
               else:
                  return 'M'
            else:
               return 'M'
         elif obj[0] == 'Less_0.081535':
            return 'B'
         elif obj[0] == 'Greater_0.1844':
            return 'M'
         else:
            return 'M'
      elif obj[2] == 'Greater_110.35':
         # {"feature": "concave_points_worst", "instances": 10, "metric_value": 0.469, "depth": 3}
         if obj[0] == 'Less_0.1844':
            # {"feature": "radius_worst", "instances": 8, "metric_value": 0.5436, "depth": 4}
            if obj[1] == 'Greater_16.165':
               # {"feature": "concave_points_mean", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[3] == 'Greater_0.009776':
                  return 'M'
               else:
                  return 'M'
            elif obj[1] == 'Less_16.165':
               return 'M'
            else:
               return 'M'
         elif obj[0] == 'Greater_0.1844':
            return 'M'
         else:
            return 'M'
      else:
         return 'M'
   else:
      return 'M'
