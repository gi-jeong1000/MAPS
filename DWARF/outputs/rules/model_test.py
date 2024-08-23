def findDecision(obj): #obj[0]: perimeter_worst, obj[1]: radius_worst, obj[2]: area_worst, obj[3]: concave_points_mean
   # {"feature": "perimeter_worst", "instances": 398, "metric_value": 0.9502, "depth": 1}
   if obj[0] == 'Less_104.55':
      # {"feature": "area_worst", "instances": 221, "metric_value": 0.3044, "depth": 2}
      if obj[2] == 'Less_676.0':
         # {"feature": "concave_points_mean", "instances": 180, "metric_value": 0.1537, "depth": 3}
         if obj[3] == 'Less_0.08659':
            # {"feature": "radius_worst", "instances": 179, "metric_value": 0.1228, "depth": 4}
            if obj[1] == 'Greater_11.245000000000001':
               return 'B'
            elif obj[1] == 'Less_11.245000000000001':
               return 'B'
            else:
               return 'M'
         elif obj[3] == 'Greater_0.08659':
            return 'M'
         else:
            return 'M'
      elif obj[2] == 'Greater_717.2':
         # {"feature": "radius_worst", "instances": 25, "metric_value": 0.795, "depth": 3}
         if obj[1] == 'Greater_11.245000000000001':
            # {"feature": "concave_points_mean", "instances": 25, "metric_value": 0.795, "depth": 4}
            if obj[3] == 'Less_0.08659':
               return 'B'
            else:
               return 'M'
         else:
            return 'M'
      elif obj[2] == 'Less_717.2':
         # {"feature": "radius_worst", "instances": 16, "metric_value": 0.5436, "depth": 3}
         if obj[1] == 'Greater_11.245000000000001':
            # {"feature": "concave_points_mean", "instances": 16, "metric_value": 0.5436, "depth": 4}
            if obj[3] == 'Less_0.08659':
               return 'B'
            else:
               return 'M'
         else:
            return 'M'
      else:
         return 'M'
   elif obj[0] == 'Greater_111.6':
      # {"feature": "concave_points_mean", "instances": 135, "metric_value": 0.3534, "depth": 2}
      if obj[3] == 'Greater_0.08659':
         return 'M'
      elif obj[3] == 'Less_0.08659':
         # {"feature": "radius_worst", "instances": 62, "metric_value": 0.5976, "depth": 3}
         if obj[1] == 'Greater_11.245000000000001':
            # {"feature": "area_worst", "instances": 62, "metric_value": 0.5976, "depth": 4}
            if obj[2] == 'Greater_717.2':
               return 'M'
            else:
               return 'M'
         else:
            return 'M'
      else:
         return 'M'
   elif obj[0] == 'Less_111.6':
      # {"feature": "concave_points_mean", "instances": 23, "metric_value": 0.9656, "depth": 2}
      if obj[3] == 'Less_0.08659':
         # {"feature": "area_worst", "instances": 22, "metric_value": 0.9457, "depth": 3}
         if obj[2] == 'Greater_717.2':
            # {"feature": "radius_worst", "instances": 19, "metric_value": 0.8997, "depth": 4}
            if obj[1] == 'Greater_11.245000000000001':
               return 'B'
            else:
               return 'M'
         elif obj[2] == 'Less_717.2':
            # {"feature": "radius_worst", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[1] == 'Greater_11.245000000000001':
               return 'M'
            else:
               return 'M'
         else:
            return 'M'
      elif obj[3] == 'Greater_0.08659':
         return 'M'
      else:
         return 'M'
   elif obj[0] == 'Less_66.12':
      return 'B'
   else:
      return 'M'
